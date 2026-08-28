%global debug_package %{nil}
%global		framework kcalendarcore

Name:		kf6-%{framework}
Version:	6.29.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 KCalendarCore Library
License:	BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires:	bison
BuildRequires:	libical-devel
BuildRequires:	qt6-qtbase-devel
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:  cmake(Qt6Qml)

%description
%{summary}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	libical-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 -DBUILD_PYTHON_BINDINGS=OFF
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*kcalendarcore.*
%{_kf6_libdir}/libKF6CalendarCore.so.*
%{_kf6_qmldir}/org/kde/calendarcore/

%files devel
%{_kf6_includedir}/KCalendarCore/
%{_kf6_libdir}/libKF6CalendarCore.so
%{_kf6_libdir}/cmake/KF6CalendarCore/
%{_kf6_libdir}/pkgconfig/KF6CalendarCore.pc
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE build for Enterprise Linux 10
