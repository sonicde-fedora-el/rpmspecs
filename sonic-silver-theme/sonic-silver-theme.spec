# Upstream SonicDE project: sonic-silver (Breeze/Silver derived)
%global sonicde_frameworks_version 6.31.0
%global reponame sonic-silver
%global sonicde_qt6_version 6.11.3

Name:		sonic-silver-theme
Version:	6.8.2
Release:        3%{?dist}
Summary:	Silver widget style, window decoration and theme for SonicDE
URL:		https://github.com/Sonic-DE/%{reponame}
Source0:	%{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
License:	GPL-2.0-or-later

BuildRequires:	sonic-frameworks-cmake-modules
BuildRequires:	sonic-rpm-macros
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	qt6-qtbase-devel >= 6.11
BuildRequires:	qt6-qtdeclarative-devel >= 6.11
BuildRequires:	qt6-qtsvg-devel >= 6.11
BuildRequires:	qt6-qtbase-private-devel >= 6.11
BuildRequires:	sonic-decoration-devel
BuildRequires:	sonic-frameworks-color-scheme-devel
BuildRequires:	sonic-frameworks-settings-devel
BuildRequires:	sonic-frameworks-logging-devel
BuildRequires:	sonic-frameworks-core-addons-devel
BuildRequires:	sonic-frameworks-qt-integration-devel
BuildRequires:	sonic-frameworks-gui-addons-devel
BuildRequires:	sonic-frameworks-internationalization-devel
BuildRequires:	sonic-frameworks-icon-themes-devel
BuildRequires:	sonic-frameworks-settings-utils-devel
BuildRequires:	sonic-frameworks-quick-ui-devel
BuildRequires:	sonic-frameworks-windowsystem-devel

# SonicDE replaces the Plasma Breeze theme packages.
Provides:	breeze = %{version}-%{release}
Provides:	breeze-cursor-theme = %{version}-%{release}

%description
Silver is the default widget style, window decoration, color scheme, cursor
theme and wallpaper set of the Sonic Desktop Environment. It is derived from
the Breeze theme of KDE Plasma.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	breeze-devel = %{version}-%{release}
Provides:	breeze-devel%{?_isa} = %{version}-%{release}
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
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Pin cmake() BuildRequires to SonicDE package names so the
  alma+epel-10 solver cannot pick EPEL's Qt 6.10-linked providers
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
