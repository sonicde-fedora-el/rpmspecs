Name:		sonic-silver-theme
Version:	6.6.0
Release:	1
Source0:	%{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Highly customizable theming for the Sonic Desktop Environment
URL:		https://github.com/Sonic-DE/silver-theme
License:	GPL-2.0-or-later
#Group:		Graphical Desktop/KDE

#BuildSystem:	cmake
#BuildOption:    -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON

BuildRequires:	extra-cmake-modules
BuildRequires:	appstream
BuildRequires:	qt5-qtbase-devel
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  cmake(Qt6ExamplesAssetDownloaderPrivate)
BuildRequires:  pkgconfig(Qt6QmlAssetDownloader)
BuildRequires:  qt6-qtbase-theme-gtk3

%description
Highly customizable theming for the KDE Plasma desktop. Install, and enable in System Settings -> Appearance -> Global Themes (or individually in Window Decorations, Application Style and Icons).

%prep
%autosetup -p1

%build
%cmake_kf6 \
%if %[(0%{?rhel} >= 10)]
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING=OFF \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/%{name}-settings
%{_libdir}/cmake/Klassy
%{_libdir}/libklassycommon*
%{_libdir}/qt5/plugins/styles/klassy5.so
%{_libdir}/qt6/plugins/kstyle_config/klassystyleconfig.so
%{_libdir}/qt6/plugins/org.kde.kdecoration3.kcm/kcm_klassydecoration.so
%{_libdir}/qt6/plugins/org.kde.kdecoration3.kcm/klassydecoration
%{_libdir}/qt6/plugins/org.kde.kdecoration3/org.kde.klassy.so
%{_libdir}/qt6/plugins/styles/klassy6.so
%{_iconsdir}/klassy-dark
%{_iconsdir}/klassy
%{_iconsdir}/hicolor/scalable/apps/klassy-settings.svgz
%{_datadir}/kstyle/themes/%{name}.themerc
%{_datadir}/plasma/desktoptheme/klassy
%{_datadir}/plasma/layout-templates/*
%{_datadir}/plasma/look-and-feel/*
%{_datadir}/applications/kcm_klassydecoration.desktop
%{_datadir}/applications/klassy*
%{_datadir}/color-schemes/Klassy*
