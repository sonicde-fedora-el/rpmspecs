# Generated for SonicDE from Fedora's plasma-activities-stats.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-activities-stats fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-activities-stats
# Upstream KDE project: plasma-activities-stats
%global oldname plasma-activities-stats

#Name:    plasma-activities-stats
Name:           sonic-activities-stats
Summary: Library to access the usage statistics data collected by the KDE activity manager
Version:        6.8.2
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        4%{?dist}

License: CC0-1.0, GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:    https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:    https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  boost-devel
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-rpm-macros
BuildRequires:  pkgconfig

BuildRequires:  sonic-activities-devel

BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtbase-devel >= 6.11
# Renamed from kf6-kactivities-stats
Obsoletes:      kf6-kactivities-stats < 1:%{version}-%{release}
Provides:       kf6-kactivities-stats = 1:%{version}-%{release}

# Renamed from kactivities-stats
Obsoletes:      kactivities-stats < 5.27.81

Provides:       plasma-activities-stats = %{version}-%{release}
Provides:       plasma-activities-stats%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-activities-stats

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Obsoletes:      kf6-kactivities-stats-devel < 1:%{version}-%{release}
Provides:       kf6-kactivities-stats-devel = 1:%{version}-%{release}
Provides:       plasma-activities-stats-devel = %{version}-%{release}
Provides:       plasma-activities-stats-devel%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-activities-stats-devel

%description devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       plasma-activities-stats-doc = %{version}-%{release}
Provides:       plasma-activities-stats-doc%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-activities-stats-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc MAINTAINER README.developers TODO
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{oldname}.*
%{_kf6_libdir}/libPlasmaActivitiesStats.so.1
%{_kf6_libdir}/libPlasmaActivitiesStats.so.%{libversion}

%files devel
%{_includedir}/PlasmaActivitiesStats/
%{_kf6_libdir}/cmake/PlasmaActivitiesStats/
%{_kf6_libdir}/libPlasmaActivitiesStats.so
%{_kf6_libdir}/pkgconfig/PlasmaActivitiesStats.pc
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-4
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Pin Plasma cmake deps to SonicDE providers (Fedora libplasma 6.8.3 outranks ours)
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
