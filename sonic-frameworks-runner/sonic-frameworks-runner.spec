# Generated for SonicDE from Fedora's kf6-krunner.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-runner fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-runner
# Upstream KDE project: krunner
%global oldname kf6-krunner

%global framework krunner

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-runner
Version:        6.29.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution with parallelized query system

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sonic-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(Qt6Core)

BuildRequires:  cmake(KF6ItemModels)

Requires:  kf6-filesystem

Provides:       kf6-krunner = %{version}-%{release}
Conflicts:      kf6-krunner < %{version}-%{release}

%description
KRunner provides a parallelized query system extendable via plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6CoreAddons)
Provides:       kf6-krunner-devel = %{version}-%{release}
Conflicts:      kf6-krunner-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-krunner-doc = %{version}-%{release}
Conflicts:      kf6-krunner-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-krunner-html = %{version}-%{release}
Conflicts:      kf6-krunner-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6Runner.so.*

%files devel
%{_kf6_includedir}/KRunner/
%{_kf6_libdir}/libKF6Runner.so
%{_kf6_libdir}/cmake/KF6Runner/
%{_kf6_datadir}/dbus-1/interfaces/*
%{_kf6_datadir}/kdevappwizard/templates/runner6.tar.bz2
%{_kf6_datadir}/kdevappwizard/templates/runner6python.tar.bz2
%{_libdir}/qt6/metatypes/qt6kf6runner_*.json
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
