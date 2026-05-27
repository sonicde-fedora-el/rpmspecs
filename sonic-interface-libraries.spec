%define _disable_source_fetch 0
%define debug_package %{nil}

Name:           sonic-interface-libraries
Version:        6.4.5
Release:        7%{?dist}
Summary:        Foundation of the SonicDE user interface (fork of libplasma)

License:        LGPL-2.0-or-later
URL:            https://github.com/Sonic-DE/sonic-interface-libraries
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

%global plasma_version %(echo %{version} | cut -d. -f1-3)

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6Su)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Solid)
BuildRequires:  openssl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel

# KDE Frameworks
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(PlasmaWaylandProtocols)

# Qt
BuildRequires:  cmake(Qt6WaylandClient)

# Plasma
BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  wayland-devel
BuildRequires:  kwayland-devel

# X11 Support
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXi-devel

Provides:       libplasma%{?_isa} >= %{plasma_version}
Provides:       libplasma >= %{plasma_version}
Obsoletes:      libplasma <= %{plasma_version}
	
# Renamed from kf6-plasma
Obsoletes:      kf6-plasma < 1:%{version}-%{release}
Provides:       kf6-plasma = 1:%{version}-%{release}

%description
Sonic Interface Libraries is a fork of libplasma, providing the foundational
libraries for themes, applets, and widgets in SonicDE.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Package)
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6Service)
Requires:       cmake(KF6WindowSystem)
Provides:       libplasma-devel%{?_isa} >= %{plasma_version}
Provides:       libplasma-devel >= %{plasma_version}
Obsoletes:      libplasma-devel <= %{plasma_version}

Obsoletes:      kf6-plasma-devel < 1:%{version}-%{release}
Provides:       kf6-plasma-devel = 1:%{version}-%{release}

%description    devel
Development files for sonic-interface-libraries.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_libdir}/libPlasma.so.*
%{_libdir}/libPlasmaQuick.so.*
%{_qt6_plugindir}/kf6/
%{_qt6_qmldir}/org/kde/plasma/
%{_qt6_qmldir}/org/kde/kirigami/styles/Plasma/
%{_datadir}/plasma/
%{_datadir}/qlogging-categories6/*.categories
%{_datadir}/qlogging-categories6/*.renamecategories

%files devel
%{_includedir}/Plasma/
%{_includedir}/PlasmaQuick/
%{_libdir}/libPlasma.so
%{_libdir}/libPlasmaQuick.so
%{_libdir}/cmake/Plasma/
%{_libdir}/cmake/PlasmaQuick/
%{_datadir}/doc/qt6/Plasma.qch
%{_datadir}/doc/qt6/Plasma.tags
%{_datadir}/kdevappwizard/templates/*.tar.bz2

%changelog
* Wed Mar 21 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.4.5-7
- Initial release of SonicDE/KDE Plasma X11 for EL10 (Downgraded to 6.4.5 for EL 10.1 compatibility)
