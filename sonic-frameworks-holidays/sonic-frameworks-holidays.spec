# Generated for SonicDE from Fedora's kf6-kholidays.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-holidays fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-holidays
# Upstream KDE project: kholidays
%global oldname kf6-kholidays

%global		framework kholidays

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-holidays
Version:        6.29.0
Release:        3%{?dist}
Summary:	The KHolidays Library

License:	BSD-2-Clause AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later WITH Bison-exception-2.2
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:	sonic-frameworks-cmake-modules >= %{version}
BuildRequires:	sonic-rpm-macros
BuildRequires:	cmake
BuildRequires:	gcc-c++

BuildRequires: 	pkgconfig(Qt6Core)
BuildRequires: 	pkgconfig(Qt6Qml)
BuildRequires: 	qt6-qttools-static
BuildRequires:	make
BuildRequires:  flex
BuildRequires:  bison

Provides:       kf6-kholidays%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kholidays < %{version}-%{release}

%description
The KHolidays library provides a C++ API that determines holiday
and other special events for a geographical region.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Provides:       kf6-kholidays-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kholidays-devel < %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kholidays-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kholidays-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kholidays-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kholidays-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 libkholidays6_qt

%files -f libkholidays6_qt.lang
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Holidays.so.*
%{_kf6_qmldir}/org/kde/kholidays/

%files devel
%{_kf6_includedir}/KHolidays/
%{_kf6_libdir}/cmake/KF6Holidays/
%{_kf6_libdir}/libKF6Holidays.so
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
