# Generated for SonicDE from Fedora's krdp.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-rdp-server fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-rdp-server
# Upstream KDE project: krdp
%global oldname krdp

%global qt6minver 6.6.0
%global kf6minver 6.2


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:           krdp
Name:           sonic-rdp-server
Summary:        Desktop sharing using RDP
Version:        6.8.0
Release:        3%{?dist}

License:        LGPL-2.1-only OR LGPL-3.0-only
#URL:            https://invent.kde.org/plasma/krdp
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig


BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  ecm-compat-find-modules >= %{kf6minver}
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-status-notification-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtwayland-devel >= 6.11
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(FreeRDP) >= 3.1
BuildRequires:  cmake(WinPR) >= 3.1
BuildRequires:  cmake(FreeRDP-Server) >= 3.1
BuildRequires:  sonic-pipewire-devel >= 5.27.80
BuildRequires:  plasma-wayland-protocols-devel >= 1.21.0
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  /usr/bin/winpr-makecert
BuildRequires:  qt6qml(org.kde.kirigamiaddons.formcard)
BuildRequires:  pkgconfig(epoxy)
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)
Requires:       /usr/bin/openssl

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-server < 6.0.90
Provides:       %{name}-server = %{version}-%{release}
Provides:       %{name}-server = %{version}-%{release}
Provides:       %{name}-server%{?_isa} = %{version}-%{release}
Provides:       krdp = %{version}-%{release}
Provides:       krdp%{?_isa} = %{version}-%{release}
Obsoletes:      krdp

%description
%{summary}.


%package libs
Summary:        Library for creating an RDP server
Requires:       /usr/bin/winpr-makecert
Conflicts:      %{name} < 6.0.90
Conflicts:      %{name}-server < 6.0.90

Provides:       krdp-libs = %{version}-%{release}
Provides:       krdp-libs%{?_isa} = %{version}-%{release}
Obsoletes:      krdp-libs

%description libs
%{summary}.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Provides:       krdp-devel = %{version}-%{release}
Provides:       krdp-devel%{?_isa} = %{version}-%{release}
Obsoletes:      krdp-devel

%description devel
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{oldname} --with-html --all-name

%post
%systemd_user_post app-org.kde.krdpserver.service

%preun
%systemd_user_preun app-org.kde.krdpserver.service

%postun
%systemd_user_postun_with_restart app-org.kde.krdpserver.service
%systemd_user_postun_with_reload app-org.kde.krdpserver.service
%systemd_user_postun app-org.kde.krdpserver.service

%files -f %{oldname}.lang
%doc README.md
%{_kf6_bindir}/krdpserver
%{_kf6_datadir}/applications/kcm_krdpserver.desktop
%{_kf6_datadir}/applications/org.kde.krdpserver.desktop
%{_kf6_datadir}/qlogging-categories6/kcm_krdpserver.categories
%{_kf6_datadir}/qlogging-categories6/krdp.categories
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_krdpserver.so
%{_userunitdir}/app-org.kde.krdpserver.service
%{_userpresetdir}/00-krdp.preset

%files libs
%license LICENSES/LGPL-*.txt LICENSES/LicenseRef-KDE-*
%{_kf6_libdir}/libKRdp.so.6{,.*}

%files devel
%{_kf6_libdir}/libKRdp.so
%{_kf6_libdir}/cmake/KRdp/

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.0-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.0-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
