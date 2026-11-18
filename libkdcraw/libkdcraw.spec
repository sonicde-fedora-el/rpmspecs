%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}
Name:    libkdcraw
Summary: A C++ interface around LibRaw library
Version: 26.08.3
Release: 2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/%{name}
Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


## upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: pkgconfig(libraw) >= 0.15

Requires: kf6-filesystem >= 6.31

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install


%files
%doc AUTHORS
%license LICENSES/*
%{_kf6_libdir}/libKDcrawQt6.so.*
%{_kf6_datadir}/qlogging-categories6/*

%files devel
%{_kf6_libdir}/libKDcrawQt6.so
%{_includedir}/KDcrawQt6/
%{_kf6_libdir}/cmake/KDcrawQt6/


%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
