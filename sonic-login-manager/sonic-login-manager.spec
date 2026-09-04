

Name:           sonic-login-manager
Version:        6.7.4.5
Release:        1%{?dist}
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
Source12:       plasmalogin.sysusers
# sample soniclogin.conf generated with soniclogin --example-config, and entries commented-out
Source13:       plasmalogin.conf

# upstream patches

# proposed patches
## soniclogin.service: +EnvironmentFile=-/etc/sysconfig/soniclogin (FIXME: patch needs update for Sonic-DE source)
#Patch1001:      soniclogin-environment_file.patch
## Workaround for https://pagure.io/fedora-kde/SIG/issue/87 (FIXME: patch needs update for Sonic-DE source)
#Patch1002:      soniclogin-rpmostree-tmpfiles-hack.patch

Provides:       service(graphical-login) = soniclogin
Obsoletes:      plasma-login-manager < %{version}-%{release}
Provides:       plasma-login-manager = %{version}-%{release}

BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 3.22
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(LibKLookAndFeel)
BuildRequires:  cmake(KF6Screen)
# verify presence to pull defaults from /etc/login.defs
BuildRequires:  shadow-utils
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  sonic-rpm-macros

# for jxl support
Requires:       sonic-frameworks-image-formats%{?_isa}

Requires:       xorg-x11-xinit
Requires:       sonic-login-manager-selinux

%{?systemd_requires}

Requires:      kf6-filesystem
Requires:      sonic-frameworks-auth
Requires(pre): shadow-utils

Recommends:      kde-settings-plasma

# Requires sonic window manager (X11 variant)
Requires:      sonic-win%{?_isa}
Recommends:      plasma-systemsettings%{?_isa})

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
Requires: qt6-filesystem
Obsoletes:      kcm-plasmalogin < %{version}-%{release}
Provides:       kcm-plasmalogin = %{version}-%{release}

%description -n kcm-soniclogin
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '/find_native_x_server(X_SERVER_EXECUTABLE_REAL/,/)/c\set(X_SERVER_EXECUTABLE_REAL "/usr/bin/Xwayland")' CMakeLists.txt


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

# De-conflict the dbus file
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-soniclogin.conf 2>/dev/null || true


%pre
%sysusers_create_compat %{SOURCE12}


%post
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
%{_sysconfdir}/init.d/soniclogin
%{_datadir}/locale/*/LC_MESSAGES/plasma_login.mo


%files -n kcm-soniclogin -f kcm_soniclogin.lang
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_soniclogin.so
%{_datadir}/applications/kcm_soniclogin.desktop
%{_datadir}/locale/*/LC_MESSAGES/kcm_plasmalogin.mo


%changelog
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

