# Written from scratch: SonicVia has no KDE or Fedora counterpart.  It replaces
# the qmk-via-api Rust crate used by the QMK D-Bus helper.
%define _disable_source_fetch 0
%global debug_package %{nil}
%global reponame sonic-frameworks-via

Name:           sonic-frameworks-via
Version:        6.29.0
Release:        1%{?dist}
Summary:        VIA HID keyboard protocol library for SonicDE
License:        BSD-2-Clause AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:            https://github.com/Sonic-DE/%{reponame}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
# Without hidapi the library builds as a stub.
BuildRequires:  pkgconfig(hidapi-hidraw)

%description
SonicVia implements the QMK VIA HID protocol for RGB lighting control of
keyboards, as used by SonicDE's QMK D-Bus helper.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Gui)

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
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
