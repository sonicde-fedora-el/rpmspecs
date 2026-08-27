# Generated for SonicDE from Fedora's plasma5support.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-plasma5-support-library fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-plasma5-support-library
# Upstream KDE project: plasma5support
%global oldname plasma5support

#Name:    plasma5support
Name:           sonic-plasma5-support-library
Summary: Support components for porting from KF5/Qt5 to KF6/Qt6
Version:        6.7.4
Release:        4%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:  https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:  https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  sonic-sysguard-library-devel
BuildRequires:  cmake(Plasma)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(libgps)
Requires:  kf6-filesystem

# Renamed from kf6-plasma5support
Obsoletes:      kf6-plasma5support < 1:%{version}-%{release}
Provides:       kf6-plasma5support = 1:%{version}-%{release}
# Geolocation libs got split off from plasma-workspace
Obsoletes: plasma-workspace-geolocation < 6.2.90-1
Provides:  plasma-workspace-geolocation = %{version}-%{release}
Obsoletes: plasma-workspace-geolocation-libs < 6.2.90-1
Provides:  plasma-workspace-geolocation-libs = %{version}-%{release}

Provides:       plasma5support%{?_isa} = %{version}-%{release}
Obsoletes:      plasma5support < %{version}-%{release}

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Obsoletes:      kf6-plasma5support-devel < 1:%{version}-%{release}
Provides:       kf6-plasma5support-devel = 1:%{version}-%{release}
# Geolocation devel components were part of plasma-workspace-devel
Conflicts: plasma-workspace-devel < 6.2.90-1
Provides:       plasma5support-devel%{?_isa} = %{version}-%{release}
Obsoletes:      plasma5support-devel < %{version}-%{release}

%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       plasma5support-doc%{?_isa} = %{version}-%{release}
Obsoletes:      plasma5support-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang libplasma5support --with-qt --with-kde --all-name

%files -f libplasma5support.lang
%doc README.md
%license LICENSES/*.txt
%{_qt6_qmldir}/org/kde/plasma/plasma5support/
%{_datadir}/plasma5support/
%{_datadir}/qlogging-categories6/plasma5support.categories
%{_datadir}/qlogging-categories6/plasma5support.renamecategories
%{_kf6_libdir}/libPlasma5Support.so.6
%{_kf6_libdir}/libPlasma5Support.so.%{version}
%{_kf6_qtplugindir}/plasma5support/
%{_libdir}/libplasma-geolocation-interface.so.6
%{_libdir}/libplasma-geolocation-interface.so.%{version}
%{_libdir}/libweather_ion.so.7
%{_libdir}/libweather_ion.so.7.0.0
%{_kf6_datadir}/plasma/weather_legacy/noaa_station_list.xml

%files devel
%{_includedir}/Plasma5Support/
%{_kf6_libdir}/cmake/Plasma5Support/
%{_qt6_docdir}/*.tags
%{_kf6_libdir}/libPlasma5Support.so
%{_libdir}/libweather_ion.so
%{_libdir}/libplasma-geolocation-interface.so
%{_includedir}/plasma/geolocation/
%{_includedir}/plasma5support/

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
