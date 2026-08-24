# Upstream SonicDE project: sonic-silver (Breeze/Silver derived)
%global reponame sonic-silver

Name:		sonic-silver-theme
Version:	6.7.4.2
Release:	1%{?dist}
Summary:	Silver widget style, window decoration and theme for SonicDE
URL:		https://github.com/Sonic-DE/%{reponame}
Source0:	%{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
License:	GPL-2.0-or-later

BuildRequires:	sonic-frameworks-cmake-modules
BuildRequires:	sonic-rpm-macros
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	qt6-qtbase-private-devel
BuildRequires:	cmake(KDecoration3)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6FrameworkIntegration)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KirigamiPlatform)
BuildRequires:	cmake(KF6WindowSystem)

# SonicDE replaces the Plasma Breeze theme packages.
Provides:	breeze = %{version}-%{release}
Conflicts:	breeze < %{version}-%{release}
Provides:	breeze-cursor-theme = %{version}-%{release}
Conflicts:	breeze-cursor-theme < %{version}-%{release}

%description
Silver is the default widget style, window decoration, color scheme, cursor
theme and wallpaper set of the Sonic Desktop Environment. It is derived from
the Breeze theme of KDE Plasma.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	breeze-devel%{?_isa} = %{version}-%{release}
Conflicts:	breeze-devel < %{version}-%{release}

%description devel
This package contains the CMake configuration and header files needed to
build software against the Silver theme libraries.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=OFF
%cmake_build

%install
%cmake_install
%find_lang silver_kwin_deco
%find_lang silver_style_config
cat silver_style_config.lang >> silver_kwin_deco.lang

%files -f silver_kwin_deco.lang
%license LICENSES/
%doc README.md AUTHORS
%{_bindir}/kcursorgen
%{_bindir}/silver-settings
%{_libdir}/libsilvercommon6.so.6*
%{_kf6_qtplugindir}/styles/silver6.so
%{_kf6_qtplugindir}/kstyle_config/silverstyleconfig.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.silver.so
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_silverdecoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/silverdecoration/
%{_datadir}/applications/kcm_silverdecoration.desktop
%{_datadir}/applications/silver-settings.desktop
%{_datadir}/applications/silverstyleconfig.desktop
%{_datadir}/kstyle/themes/silver.themerc
%{_datadir}/color-schemes/*.colors
%{_datadir}/icons/hicolor/scalable/apps/silver-settings.svgz
%{_datadir}/icons/silver_cursors_dark/
%{_datadir}/icons/silver_cursors_light/
%{_datadir}/plasma/layout-templates/org.kde.silver.*/
%{_datadir}/plasma/look-and-feel/org.kde.silver*/
%{_datadir}/wallpapers/Silver/

%files devel
%{_libdir}/cmake/SonicSilver/
%{_libdir}/cmake/Breeze/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
