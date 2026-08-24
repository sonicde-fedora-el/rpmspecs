# Generated for SonicDE from Fedora's kf6-prison.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-barcode fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-barcode
# Upstream KDE project: prison
%global oldname kf6-prison

%define framework prison

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-barcode
Summary:	KDE Frameworks 6 Tier 1 barcode library
Version:        6.29.0
Release:        1%{?dist}
License:	BSD-3-Clause AND CC0-1.0 AND MIT
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	sonic-frameworks-cmake-modules >= %{version}
BuildRequires:	sonic-rpm-macros
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	cmake(ZXing)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	pkgconfig(libqrencode)

Requires:	kf6-filesystem

Provides:       kf6-prison = %{version}-%{release}
Conflicts:      kf6-prison < %{version}-%{release}

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Provides:       kf6-prison-devel = %{version}-%{release}
Conflicts:      kf6-prison-devel < %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-prison-doc = %{version}-%{release}
Conflicts:      kf6-prison-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-prison-html = %{version}-%{release}
Conflicts:      kf6-prison-html < %{version}-%{release}

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
%doc README*
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Prison.so.6
%{_kf6_libdir}/libKF6Prison.so.%{version}
%{_kf6_libdir}/libKF6PrisonScanner.so.6
%{_kf6_libdir}/libKF6PrisonScanner.so.%{version}
%{_qt6_qmldir}/org/kde/prison/

%files devel
%{_kf6_includedir}/Prison/
%{_kf6_includedir}/PrisonScanner/
%{_kf6_libdir}/libKF6Prison.so
%{_kf6_libdir}/libKF6PrisonScanner.so
%{_kf6_libdir}/cmake/KF6Prison/
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
