# Generated for SonicDE from Fedora's kf6-kquickcharts.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-quick-charts fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_qt6_version 6.11.3
%global reponame sonic-frameworks-quick-charts
# Upstream KDE project: kquickcharts
%global oldname kf6-kquickcharts

%global		framework kquickcharts

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-quick-charts
Summary:	A QtQuick module providing high-performance charts
Version:        6.31.0
Release:        3%{?dist}

License:	BSD-2-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	sonic-frameworks-cmake-modules >= %{version}
BuildRequires:	qt6-qtdeclarative-devel >= 6.11
BuildRequires:	qt6-qtshadertools-devel >= 6.11
BuildRequires:	make
BuildRequires:	pkgconfig(xkbcommon)

Provides:       kf6-kquickcharts = %{version}-%{release}
Provides:       kf6-kquickcharts%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kquickcharts

%description
The Quick Charts module provides a set of charts that can be used from QtQuick
applications. They are intended to be used for both simple display of data as
well as continuous display of high-volume data (often referred to as plotters).
The charts use a system called distance fields for their accelerated rendering,
which provides ways of using the GPU for rendering 2D shapes without loss of
quality.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Provides:       kf6-kquickcharts-devel = %{version}-%{release}
Provides:       kf6-kquickcharts-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kquickcharts-devel

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kquickcharts-doc = %{version}-%{release}
Provides:       kf6-kquickcharts-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kquickcharts-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kquickcharts-html = %{version}-%{release}
Provides:       kf6-kquickcharts-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kquickcharts-html

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
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_qmldir}/org/kde/quickcharts/
%{_libdir}/libQuickCharts.so.*
%{_libdir}/libQuickChartsControls.so*

%files devel
%{_kf6_libdir}/cmake/KF6QuickCharts/
%{_libdir}/libQuickCharts.so
%{_libdir}/libQuickChartsControls.so
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
