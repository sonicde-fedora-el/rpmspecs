%global sonicde_frameworks_version 6.31.0
%global base_name kdeconnect-kde
%global sonicde_qt6_version 6.11.3

Name:    kde-connect
Version: 26.08.3
Release:        2%{?dist}
License: GPL-2.0-or-later
Summary: KDE Connect client for communication with smartphones

Url:     https://community.kde.org/KDEConnect

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/kdeconnect-kde-%{version}.tar.xz

# Doesn't build on i686 as-of 25.03.80
ExcludeArch: %{ix86}

## upstream patches

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  firewalld-filesystem
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(openssl)

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-quick-ui-devel
BuildRequires:  sonic-frameworks-quick-ui-addons-devel
BuildRequires:  sonic-frameworks-modemmanager-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-package-devel
BuildRequires:  kf6-kpeople-devel >= 6.31
BuildRequires:  sonic-frameworks-app-info-devel
BuildRequires:  sonic-frameworks-status-notification-devel
BuildRequires:  sonic-frameworks-quick-desktop-style
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-data-models-devel

BuildRequires:  qt6-qtconnectivity-devel >= 6.11
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtmultimedia-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qt5compat-devel >= 6.11
# wayland/clipboard deps
BuildRequires:  ecm-compat-find-modules
BuildRequires:  qt6-qtwayland-devel >= 6.11
BuildRequires:  plasma-wayland-protocols-devel >= 1.21.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  wayland-protocols-devel
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  cmake(Qca-qt6)

BuildRequires:  sonic-pulseaudio-library-qt6-devel

BuildRequires:  libXtst-devel
BuildRequires:  pkgconfig(libei-1.0)
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libfakekey)

Obsoletes: kde-connect-kde4-ioslave < %{version}-%{release}
Obsoletes: kde-connect-kde4-libs < %{version}-%{release}

# upstream name
Provides:       kdeconnect-kde = %{version}-%{release}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kdeconnectd = %{version}-%{release}

Requires:       fuse-sshfs
Requires:       qca-qt6-ossl%{?_isa}
# /usr/bin/plasmawindowed (make optional at least until this is split out for bug #1286431)
#Recommends:     plasma-workspace
# /usr/bin/kcmshell5
Requires:       sonic-terminal-tools
# /usr/bin/kdeconnect-app
Requires:       sonic-frameworks-quick-ui%{?_isa}
Requires:       sonic-frameworks-quick-ui-addons
# kde-connect app requires the qml definition to launch
Requires:       qt6qml(org.kde.desktop)
# Required for contact synchronization with kde connect
Recommends:     kf6-kpeople >= 6.31

%description
KDE Connect adds communication between KDE and your smartphone.

Currently, you can pair with your Android devices over Wifi using the
KDE Connect 1.0 app from Albert Vaka which you can obtain via Google Play, F-Droid
or the project website.

%package -n kdeconnectd
Summary: KDE Connect service
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description -n kdeconnectd
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
# I think we may want to drop this, forces kdeconnectd to pull in main pkg indirectly -- rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package nautilus
Summary: KDEConnect extention for nautilus
Requires: kdeconnectd = %{version}-%{release}
Requires: nautilus-python
Supplements: (kdeconnectd and nautilus)
%description nautilus
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html

# https://bugzilla.redhat.com/show_bug.cgi?id=1296523
desktop-file-edit --remove-key=OnlyShowIn %{buildroot}%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
	
## unpackaged files
# this is a static version of the shared lib dropped in the beta
rm -fv %{buildroot}%{_kf6_libdir}/libkdeconnectinterfaces.a

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kdeconnect.metainfo.xml
for i in %{buildroot}%{_kf6_datadir}/applications/org.kde.kdeconnect*.desktop ; do
desktop-file-validate $i
done


%files -f %{name}.lang
%dir %{_kf6_datadir}/kdeconnect/
%license LICENSES/*
%{_datadir}/Thunar/
%{_datadir}/contractor/
%{_datadir}/deepin/
%{_datadir}/zsh/
%{_sysconfdir}/ufw/applications.d/kdeconnect
%{_kf6_datadir}/applications/org.kde.kdeconnect*.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/kdeconnect*
%{_kf6_datadir}/icons/hicolor/*/status/*
%{_kf6_bindir}/kdeconnect-*
%{_kf6_datadir}/kdeconnect/kdeconnect_*.qml
%{_kf6_datadir}/knotifications6/*
%{_kf6_datadir}/plasma/plasmoids/org.kde.kdeconnect/
%{_kf6_datadir}/qlogging-categories6/kdeconnect*
%{_kf6_metainfodir}/org.kde.kdeconnect.metainfo.xml
%{_kf6_plugindir}/kfileitemaction/kdeconnectfileitemaction.so
%{_kf6_plugindir}/kio/kdeconnect.so
%{_qt6_archdatadir}/qml/org/kde/kdeconnect/

%files -n kdeconnectd
%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
%{_datadir}/applications/org.kde.kdeconnect.daemon.desktop
%{_kf6_bindir}/kdeconnectd
%{_datadir}/dbus-1/services/org.kde.kdeconnect.service
%{_udevrulesdir}/40-kdeconnect-uinput.rules
%{_datadir}/remoteview/kdeconnect-network.desktop
%{_datadir}/solid/actions/solid_kdeconnect.desktop

%files libs
%{_kf6_libdir}/libkdeconnectcore.so.*
%{_qt6_plugindir}/kdeconnect/

%files nautilus
%{_datadir}/nautilus-python/extensions/kdeconnect-share.py*


%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Thu Aug 27 2026 SonicDE <dev@sonicde.org> - 26.04.3-1
- Update to 26.04.3
- Change Requires from kde-cli-tools to sonic-terminal-tools
- Change Requires from kf6-kirigami2 to sonic-frameworks-quick-ui
* Sun Mar 08 2026 Steve Cossette <farchord@gmail.com> - 25.12.3-1
- 25.12.3

* Thu Feb 12 2026 Steve Cossette <farchord@gmail.com> - 25.12.2-2
- Full Stack Rebuild (kio abi break)

* Mon Nov 16 2026 Steve Cossette <farchord@gmail.com> - 25.12.2-1
- 25.12.2

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 25.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild