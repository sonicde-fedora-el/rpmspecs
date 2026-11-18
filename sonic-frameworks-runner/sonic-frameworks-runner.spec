# Generated for SonicDE from Fedora's kf6-krunner.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-runner fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-frameworks-runner
# Upstream KDE project: krunner
%global oldname kf6-krunner

%global framework krunner

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-runner
Version:        6.31.0
Release:        3%{?dist}
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

BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-app-info-devel
BuildRequires:  sonic-frameworks-device-integration-devel
BuildRequires:  kf6-threadweaver-devel >= 6.31
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel >= 6.11

BuildRequires:  sonic-frameworks-data-models-devel

Requires: kf6-filesystem >= 6.31

Provides:       kf6-krunner = %{version}-%{release}
Provides:       kf6-krunner%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-krunner

%description
KRunner provides a parallelized query system extendable via plugins.

%package        devel
Summary:        Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Requires: sonic-frameworks-core-addons-devel
Provides:       kf6-krunner-devel = %{version}-%{release}
Provides:       kf6-krunner-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-krunner-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-krunner-doc = %{version}-%{release}
Provides:       kf6-krunner-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-krunner-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-krunner-html = %{version}-%{release}
Provides:       kf6-krunner-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-krunner-html

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
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
