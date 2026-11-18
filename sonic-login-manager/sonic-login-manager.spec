

%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
Name:           sonic-login-manager
Version:        6.8.2
Release:        9%{?dist}
License:        BSD-3-Clause and CC0-1.0 and (GPL-2.0-only or GPL-3.0-only) and GPL-2.0-or-later and LGPL-2.0-or-later and LGPL-2.1-or-later
Summary:        QML based login manager for SonicDE

URL:            https://github.com/Sonic-DE/sonic-login-manager
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# README.scripts
Source10:       README.scripts
# sysconfig snippet
Source11:       plasmalogin.sysconfig
# sysusers config file. note these are shipped in the upstream tarball
# but we cannot use the files from the tarball for %%pre scriptlet
# generation, so we duplicate them as source files for that purpose;
# this is an ugly hack that should be removed if it becomes possible.
# see https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/TFDMAU7KLMSQTKPJELHSM6PFVXIZ56GK/
Source12:       soniclogin.sysusers
# sample soniclogin.conf generated with soniclogin --example-config, and entries commented-out
Source13:       plasmalogin.conf
Source14:       soniclogin.tmpfiles

# upstream patches
# XLibre removed -noreset; drop the arg from the X server command line
Patch0:         xlibre-drop-noreset.patch

# proposed patches
## soniclogin.service: +EnvironmentFile=-/etc/sysconfig/soniclogin (FIXME: patch needs update for Sonic-DE source)
#Patch1001:      soniclogin-environment_file.patch
## Workaround for https://pagure.io/fedora-kde/SIG/issue/87 (FIXME: patch needs update for Sonic-DE source)
#Patch1002:      soniclogin-rpmostree-tmpfiles-hack.patch

Provides:       service(graphical-login) = soniclogin
Obsoletes:      plasma-login-manager
Provides:       plasma-login-manager = %{version}-%{release}
Obsoletes:      sddm
Provides:       sddm = %{version}-%{release}
Provides:       sddm%{?_isa} = %{version}-%{release}

BuildRequires:  xorg-x11-server-Xorg
BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 3.22
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  libXcursor-devel
BuildRequires:  libXfixes-devel
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qttools-devel >= 6.11
BuildRequires:  qt6-qtshadertools-devel >= 6.11
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-package-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-auth-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-quick-ui-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-init-info-devel
BuildRequires:  sonic-frameworks-logging-devel
BuildRequires:  sonic-frameworks-ipc-devel
BuildRequires:  sonic-interface-libraries-devel
BuildRequires:  sonic-workspace-devel
BuildRequires:  sonic-screen-library-devel
# verify presence to pull defaults from /etc/login.defs
BuildRequires:  shadow-utils
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  sonic-rpm-macros

# for jxl support
Requires:       sonic-frameworks-image-formats%{?_isa}

Requires:       xorg-x11-xinit
Requires:       xorg-x11-server-Xorg
Requires:       sonic-login-manager-selinux

%{?systemd_requires}

Requires: kf6-filesystem >= 6.31
Requires: sonic-frameworks-auth
Requires(pre): shadow-utils

Recommends:      kde-settings-plasma

# Requires sonic window manager (X11 variant)
Requires: sonic-win%{?_isa}
Recommends:      plasma-systemsettings%{?_isa}

%description
Sonic Login Manager provides a display manager for SonicDE
with a frontend providing a greeter,
wallpaper plugin integration and a System Settings module (KCM).

%package -n kcm-soniclogin
Summary: KDE KCM for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: dbus-common
Recommends:      plasma-systemsettings%{?_isa}
Requires: polkit
Requires: qt6-filesystem >= 6.11
Obsoletes:      kcm-plasmalogin
Provides:       kcm-plasmalogin = %{version}-%{release}

%description -n kcm-soniclogin
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}


%conf
%cmake_kf6 \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DPAM_OS_CONFIGURATION:STRING="fedora" \
  -DSESSION_COMMAND:PATH=/etc/X11/xinit/Xsession \
  -DWAYLAND_SESSION_COMMAND:PATH=/etc/soniclogin/wayland-session \
  -DX_SERVER_EXECUTABLE:PATH=/usr/bin/Xorg


%build
%cmake_build


%install
%cmake_install

%find_lang sonic_login
%find_lang kcm_soniclogin


mkdir -p %{buildroot}%{_sysconfdir}/soniclogin.conf.d
mkdir -p %{buildroot}%{_prefix}/lib/soniclogin/soniclogin.conf.d

mkdir -p %{buildroot}/run/soniclogin
mkdir -p %{buildroot}%{_localstatedir}/lib/soniclogin
install -Dpm644 %{SOURCE12} %{buildroot}%{_sysusersdir}/soniclogin.conf
install -Dpm644 %{SOURCE14} %{buildroot}%{_tmpfilesdir}/soniclogin.conf

# De-conflict the dbus file
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-soniclogin.conf 2>/dev/null || true


%pre
%sysusers_create_compat %{SOURCE12}


%post
%tmpfiles_create soniclogin.conf
%systemd_post soniclogin.service
%systemd_user_post soniclogin.service soniclogin-sonic-win.service soniclogin-x11.target soniclogin-wallpaper.service


%preun
%systemd_preun soniclogin.service
%systemd_user_preun soniclogin.service soniclogin-sonic-win.service soniclogin-x11.target soniclogin-wallpaper.service


%postun
%systemd_postun soniclogin.service
%systemd_user_postun soniclogin.service soniclogin-sonic-win.service soniclogin-x11.target soniclogin-wallpaper.service


%files -f sonic_login.lang
%license LICENSE LICENSE.* LICENSES/*
%doc README.md
%dir %{_sysconfdir}/soniclogin.conf.d
%dir %{_prefix}/lib/soniclogin
%dir %{_prefix}/lib/soniclogin/soniclogin.conf.d
%config(noreplace) %{_sysconfdir}/pam.d/soniclogin
%config(noreplace) %{_sysconfdir}/pam.d/soniclogin-autologin
%config(noreplace) %{_sysconfdir}/pam.d/soniclogin-greeter
%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-soniclogin.conf
%{_bindir}/soniclogin
%{_bindir}/start-soniclogin-x11
%{_bindir}/soniclogin-wallpaper
%{_libexecdir}/soniclogin-helper
%{_libexecdir}/soniclogin-helper-start-x11user
%{_libexecdir}/soniclogin-greeter
%{_sysusersdir}/soniclogin.conf
%{_tmpfilesdir}/soniclogin.conf
%attr(0711, root, soniclogin) %dir /run/soniclogin
%attr(1770, soniclogin, soniclogin) %dir %{_localstatedir}/lib/soniclogin
%{_unitdir}/soniclogin.service
%{_userunitdir}/soniclogin.service
%{_userunitdir}/soniclogin-sonic-win.service
%{_userunitdir}/soniclogin-x11.target
%{_userunitdir}/soniclogin-wallpaper.service
%{_userunitdir}/soniclogin-apply-kscreen.service
%dir %{_datadir}/soniclogin
%{_datadir}/soniclogin/scripts/
%if 0%{?rhel}
%{_sysconfdir}/init.d/soniclogin
%endif
%{_datadir}/locale/*/LC_MESSAGES/plasma_login.mo


%files -n kcm-soniclogin -f kcm_soniclogin.lang
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_soniclogin.so
%{_datadir}/applications/kcm_soniclogin.desktop
%{_datadir}/locale/*/LC_MESSAGES/kcm_plasmalogin.mo


%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-9
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-8
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-7
- Pin LibKWorkspace/LibKLookAndFeel to sonic-workspace-devel: the
  unversioned cmake() provides also exist in EPEL's plasma-workspace-devel
  (built for Qt 6.10), which won resolution on alma+epel-10-x86_64_v2 and
  broke the buildroot on Qt_6.10_PRIVATE_API.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-6
- Require xorg-x11-server-Xorg at runtime: a display manager cannot
  start a session without its X server; resolves to XLibre where the
  project repo is present, to xorg-x11-server on Fedora.

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 6.8.2-3
- soniclogin.sysusers: add video/input/render memberships for the greeter
  account; the groups live in /usr/lib/group which usermod cannot edit,
  and the daemon's SelfProvisioner is SELinux-denied under xdm_t. Proven
  needed on the live dev image.

* Fri Sep 04 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.5-1
- Update to SonicDE 6.7.4.5

* Tue Jun 30 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.6.4-12
- Add SELinux policy module to allow soniclogin to launch X11 user sessions
- Remove with_X11 condition since we will always be using X11

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 6.6.4-1
- 6.6.4

* Tue Mar 17 2026 Steve Cossette <farchord@gmail.com> - 6.6.3-1
- 6.6.3

* Tue Mar 03 2026 Steve Cossette <farchord@gmail.com> - 6.6.2-1
- 6.6.2

* Tue Feb 24 2026 Steve Cossette <farchord@gmail.com> - 6.6.1-1
- 6.6.1

* Thu Feb 12 2026 Steve Cossette <farchord@gmail.com> - 6.6.0-1
- 6.6.0

* Fri Jan 30 2026 Adam Williamson <awilliam@redhat.com> - 6.5.91-2
- Backport MR #102 to fix idle timeout issues

* Tue Jan 27 2026 Steve Cossette <farchord@gmail.com> - 6.5.91-1
- 6.5.91

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Jan 13 2026 Steve Cossette <farchord@gmail.com> - 6.5.90-1
- 6.5.90

* Tue Jan 13 2026 farchord@gmail.com
- 6.5.90

* Mon Jan 12 2026 Neal Gompa <ngompa@fedoraproject.org> - 0.21.0~git1.20260112.c96b194-3
- Add WIP fix to avoid KCM breaking wallpaper settings

* Mon Jan 12 2026 Neal Gompa <ngompa@fedoraproject.org> - 0.21.0~git1.20260112.c96b194-2
- Fix install path for main config file

* Mon Jan 12 2026 Neal Gompa <ngompa@fedoraproject.org> - 0.21.0~git1.20260112.c96b194-1
- Bump to new git snapshot
- Drop merged patch

* Sun Jan 11 2026 Neal Gompa <ngompa@fedoraproject.org> - 0.21.0~git1.20260111.99ded95-2
- Add patch to read default wallpaper settings

* Sun Jan 11 2026 Neal Gompa <ngompa@fedoraproject.org> - 0.21.0~git1.20260111.99ded95-1
- Bump to new git snapshot

* Wed Dec 03 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.21.0~git1.20251203.68b0122-1
- Bump to new git snapshot
- Add sample soniclogin.conf

* Fri Nov 28 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.21.0~git1.20251128.146250b-1
- Bump to new git snapshot

* Tue Nov 25 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.21.0~git1.20251125.6972b55-1
- Initial package (partly forked from sddm)

