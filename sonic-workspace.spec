%define _disable_source_fetch 0
%define debug_package %{nil}

Name:           sonic-workspace
Version:        6.4.5
Release:        5%{?dist}
Summary:        Core workspace components for SonicDE (fork of plasma-workspace)

License:        GPL-2.0-or-later
URL:            https://github.com/Sonic-DE/sonic-workspace
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

%global plasma_version %(echo %{version} | cut -d. -f1-3)

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtdeclarative-private-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  qt6-qtlocation-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qcoro-qt6-devel
BuildRequires:  phonon-qt6-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KDED)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6QuickCharts)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  kf6-kdesu-devel
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  sonic-win-devel
BuildRequires:  sonic-interface-libraries-devel
BuildRequires:  kdecoration-devel
BuildRequires:  libkscreen-devel
BuildRequires:  libksysguard-devel
BuildRequires:  plasma-activities-devel
BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  cmake(KScreenLocker)
BuildRequires:  cmake(Breeze)
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KPipeWire)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaActivitiesStats)
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(LayerShellQt)

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  systemd-devel
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  glib2-devel
BuildRequires:  polkit-qt6-1-devel
BuildRequires:  PackageKit-Qt6-devel
BuildRequires:  appstream-qt-devel
BuildRequires:  iso-codes-devel
BuildRequires:  libcanberra-devel
BuildRequires:  fontconfig-devel
BuildRequires:  zlib-devel
BuildRequires:  libicu-devel

Requires:       sonic-win
Requires:       xmessage
Requires:       xprop
Requires:       xrdb
Requires:       xsetroot

Conflicts:      plasma-workspace-x11

Provides:       plasma-workspace%{?_isa} >= %{plasma_version}
Provides:       plasma-workspace >= %{plasma_version}
Obsoletes:      plasma-workspace <= %{plasma_version}

Provides:       plasma-workspace-libs%{?_isa} >= %{plasma_version}
Provides:       plasma-workspace-libs >= %{plasma_version}
Obsoletes:      plasma-workspace-libs <= %{plasma_version}

Provides:       libkworkspace6%{?_isa} >= %{plasma_version}
Provides:       libkworkspace6 >= %{plasma_version}
Obsoletes:      libkworkspace6 <= %{plasma_version}

Provides:       desktop-notification-daemon

%description
Core workspace components for SonicDE, fork of plasma-workspace.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      plasma-workspace-devel

%description    devel
Development files for sonic-workspace.

%package        x11
Summary:        SonicDE X11 session
#Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xlibre-xserver-Xorg
Conflicts:      plasma-workspace-x11

%description    x11
SonicDE X11 session.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
# Many translation files have different names than the package
%find_lang plasmanetworkmanagement --all-name || :
%find_lang plasmashell --all-name || :

%files
%license LICENSES/*
%{_bindir}/plasma*
%{_bindir}/krunner
%{_bindir}/ksmserver
%{_bindir}/ksplashqml
%{_bindir}/kcminit*
%{_bindir}/kde-systemd-start-condition
%{_bindir}/lookandfeeltool
%{_bindir}/kcolorschemeeditor
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/xembedsniproxy
%{_bindir}/gmenudbusmenuproxy
%{_bindir}/startplasma-wayland
%{_libdir}/lib*.so.*
%{_libdir}/kconf_update_bin/
%{_libexecdir}/ksmserver-logout-greeter
%{_libexecdir}/plasma*
%{_libexecdir}/kf6/kauth/
%{_libexecdir}/kfontprint
%{_libexecdir}/baloorunner
%{_qt6_plugindir}/plasma/
%{_qt6_plugindir}/kf6/
%{_qt6_plugindir}/phonon_platform/
%{_qt6_plugindir}/plasma5support/
%{_qt6_plugindir}/plasmacalendarplugins/
%{_qt6_qmldir}/org/kde/
%{_userunitdir}/plasma*
%{_datadir}/plasma/
%{_datadir}/plasma5support/
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/
%{_datadir}/config.kcfg/
%{_datadir}/dbus-1/
%{_datadir}/doc/
%{_datadir}/icons/
%{_datadir}/kconf_update/
%{_datadir}/kfontinst/
%{_datadir}/kglobalaccel/
%{_datadir}/kio*/
%{_datadir}/knotifications6/
%{_datadir}/knsrcfiles/
%{_datadir}/konqsidebartng/
%{_datadir}/krunner/
%{_datadir}/kstyle/
%{_datadir}/kxmlgui5/
%{_datadir}/polkit-1/
%{_datadir}/qlogging-categories6/
%{_datadir}/solid/
%{_datadir}/timezonefiles/
%{_datadir}/wayland-sessions/
%{_datadir}/xdg-desktop-portal/
%{_datadir}/zsh/
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_sysconfdir}/xdg/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/kworkspace6/
%{_includedir}/taskmanager/
%{_includedir}/notificationmanager/
%{_includedir}/colorcorrect/
%{_includedir}/krdb/
%{_includedir}/plasma5support/
%{_libdir}/lib*.so
%{_libdir}/cmake/*/

%files x11
%defattr(-,root,root,-)
%{_datadir}/xsessions/plasmax11.desktop
%{_bindir}/startplasma-x11

%changelog
* Wed Mar 21 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.4.5-5
- Initial release of SonicDE/KDE Plasma X11 for EL10 (Downgraded to 6.4.5 for EL 10.1 compatibility)
