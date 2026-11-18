# Generated for SonicDE from Fedora's plasma5support.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-plasma5-support-library fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-plasma5-support-library
# Upstream KDE project: plasma5support
%global oldname plasma5support

#Name:    plasma5support
Name:           sonic-plasma5-support-library
Summary: Support components for porting from KF5/Qt5 to KF6/Qt6
Version:        6.8.0
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        3%{?dist}

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
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-app-info-devel
BuildRequires:  sonic-frameworks-device-integration-devel
BuildRequires:  sonic-frameworks-idle-tracker-devel
BuildRequires:  sonic-frameworks-networkmanager-devel
BuildRequires:  sonic-frameworks-unit-conversion-devel
BuildRequires:  sonic-frameworks-holidays-devel
BuildRequires:  sonic-activities-devel
BuildRequires:  sonic-sysguard-library-devel
BuildRequires:  sonic-interface-libraries-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(libgps)
Requires: kf6-filesystem >= 6.31

# Renamed from kf6-plasma5support
Obsoletes:      kf6-plasma5support < 1:%{version}-%{release}
Provides:       kf6-plasma5support = 1:%{version}-%{release}
# Geolocation libs got split off from plasma-workspace
Obsoletes:      plasma-workspace-geolocation
Provides:  plasma-workspace-geolocation = %{version}-%{release}
Obsoletes:      plasma-workspace-geolocation-libs
Provides:  plasma-workspace-geolocation-libs = %{version}-%{release}

Provides:       plasma5support = %{version}-%{release}
Provides:       plasma5support%{?_isa} = %{version}-%{release}
Obsoletes:      plasma5support

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Obsoletes:      kf6-plasma5support-devel < 1:%{version}-%{release}
Provides:       kf6-plasma5support-devel = 1:%{version}-%{release}
# Geolocation devel components were part of plasma-workspace-devel
Conflicts: plasma-workspace-devel < 6.2.90-1
Provides:       plasma5support-devel = %{version}-%{release}
Provides:       plasma5support-devel%{?_isa} = %{version}-%{release}
Obsoletes:      plasma5support-devel

%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       plasma5support-doc = %{version}-%{release}
Provides:       plasma5support-doc%{?_isa} = %{version}-%{release}
Obsoletes:      plasma5support-doc

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
%{_kf6_libdir}/libPlasma5Support.so.%{libversion}
%{_kf6_qtplugindir}/plasma5support/
%{_libdir}/libplasma-geolocation-interface.so.6
%{_libdir}/libplasma-geolocation-interface.so.%{libversion}
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
