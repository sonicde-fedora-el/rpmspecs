%global debug_package %{nil}
%global sonicde_qt6_version 6.11.3
%global		framework kcalendarcore

Name:		kf6-%{framework}
Version: 6.31.0
Release:	2%{?dist}
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
BuildRequires:	qt6-qtbase-devel >= 6.11
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:  qt6-qtdeclarative-devel >= 6.11

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
%find_lang kcalendarcore6_qt --all-name --with-qt

%files -f kcalendarcore6_qt.lang
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
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 6.31.0-1
- 6.31.0

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE build for Enterprise Linux 10
