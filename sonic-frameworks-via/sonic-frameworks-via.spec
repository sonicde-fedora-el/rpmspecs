# Written from scratch: SonicVia has no KDE or Fedora counterpart.  It replaces
# the qmk-via-api Rust crate used by the QMK D-Bus helper.
%define _disable_source_fetch 0
%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}
%global reponame sonic-frameworks-via

Name:           sonic-frameworks-via
Version:        6.31.0.1
Release:        2%{?dist}
Summary:        VIA HID keyboard protocol library for SonicDE
License:        BSD-2-Clause AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:            https://github.com/Sonic-DE/%{reponame}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel >= 6.11
# Without hidapi the library builds as a stub.
BuildRequires:  pkgconfig(hidapi-hidraw)

%description
SonicVia implements the QMK VIA HID protocol for RGB lighting control of
keyboards, as used by SonicDE's QMK D-Bus helper.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel >= 6.11

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=OFF -DBUILD_QCH:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE LICENSES/*
%doc README.md
%{_libdir}/libSonicVia.so.6*

%files devel
%{_includedir}/via/
%{_includedir}/sonicvia_version.h
%{_libdir}/libSonicVia.so
%{_libdir}/cmake/SonicVia/

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0.1-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
