# Generated for SonicDE from Fedora's plasma-activities.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-activities fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-activities
# Upstream KDE project: plasma-activities
%global oldname plasma-activities

#Name:    plasma-activities
Name:           sonic-activities
Summary: Core components for the KDE Activity concept
Version:        6.7.4
Release:        1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:    https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:    https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  boost-devel
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
Requires:  kf6-filesystem

# Renamed from kf6-kactivities
Obsoletes:      kf6-kactivities < 1:%{version}-%{release}
Provides:       kf6-kactivities = 1:%{version}-%{release}

# Renamed from kactivities
Obsoletes:      kactivities < 5.27.81

Provides:       plasma-activities = %{version}-%{release}
Conflicts:      plasma-activities < %{version}-%{release}

%description
KActivities provides the infrastructure needed to manage a user's activities,
allowing them to switch between tasks, and for applications to update their
state to match the user's current activity. This includes a daemon, a library
for interacting with that daemon, and plugins for integration with other
frameworks.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Obsoletes:      kf6-kactivities-devel < 1:%{version}-%{release}
Provides:       kf6-kactivities-devel = 1:%{version}-%{release}
Provides:       plasma-activities-devel = %{version}-%{release}
Conflicts:      plasma-activities-devel < %{version}-%{release}

%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       plasma-activities-doc = %{version}-%{release}
Conflicts:      plasma-activities-doc < %{version}-%{release}

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
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/plasma-activities-cli6
%{_kf6_datadir}/qlogging-categories6/plasma-activities.categories
%{_kf6_datadir}/qlogging-categories6/plasma-activities.renamecategories
%{_kf6_libdir}/libPlasmaActivities.so.7
%{_kf6_libdir}/libPlasmaActivities.so.%{version}
%{_kf6_qmldir}/org/kde/activities/

%files devel
%{_includedir}/PlasmaActivities/
%{_kf6_libdir}/cmake/PlasmaActivities/
%{_kf6_libdir}/libPlasmaActivities.so
%{_kf6_libdir}/pkgconfig/PlasmaActivities.pc
#%%{_qt6_docdir}/*.tags

%files doc
#%%{_qt6_docdir}/*.qch

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
