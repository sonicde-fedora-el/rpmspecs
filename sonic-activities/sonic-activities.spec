# Generated for SonicDE from Fedora's plasma-activities.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-activities fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-activities
# Upstream KDE project: plasma-activities
%global oldname plasma-activities

#Name:    plasma-activities
Name:           sonic-activities
Summary: Core components for the KDE Activity concept
Version:        6.8.2
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        3%{?dist}

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
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
Requires: kf6-filesystem >= 6.31

# Renamed from kf6-kactivities
Obsoletes:      kf6-kactivities < 1:%{version}-%{release}
Provides:       kf6-kactivities = 1:%{version}-%{release}

# Renamed from kactivities
Obsoletes:      kactivities < 5.27.81

Provides:       plasma-activities = %{version}-%{release}
Provides:       plasma-activities%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-activities

%description
KActivities provides the infrastructure needed to manage a user's activities,
allowing them to switch between tasks, and for applications to update their
state to match the user's current activity. This includes a daemon, a library
for interacting with that daemon, and plugins for integration with other
frameworks.

%package devel
Summary:        Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Obsoletes:      kf6-kactivities-devel < 1:%{version}-%{release}
Provides:       kf6-kactivities-devel = 1:%{version}-%{release}
Provides:       plasma-activities-devel = %{version}-%{release}
Provides:       plasma-activities-devel%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-activities-devel

%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       plasma-activities-doc = %{version}-%{release}
Provides:       plasma-activities-doc%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-activities-doc

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
%{_kf6_libdir}/libPlasmaActivities.so.%{libversion}
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
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
