# Written from scratch: upstream libaccounts-qt has no Fedora Qt 6 package.
%define _disable_source_fetch 0
%global debug_package %{nil}
%global reponame sonic-qt-accounts-library

Name:           sonic-qt-accounts-library
Version:        1.17.2
Release:        3%{?dist}
Summary:        Qt 6 bindings for libaccounts-glib, as used by SonicDE
License:        LGPL-2.1-only
URL:            https://github.com/Sonic-DE/%{reponame}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(glib-2.0)

Provides:       accounts-qt6%{?_isa} = %{version}-%{release}
Obsoletes:      libaccounts-qt6 < %{version}-%{release}

%description
Qt 6 bindings for libaccounts-glib, the accounts and single sign-on database
used by the SonicDE online accounts integration.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Provides:       accounts-qt6-devel%{?_isa} = %{version}-%{release}
Obsoletes:      libaccounts-qt6-devel < %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md NOTES
%{_libdir}/libaccounts-qt6.so.1*

%files devel
%{_includedir}/accounts-qt6/
%{_libdir}/libaccounts-qt6.so
%{_libdir}/cmake/AccountsQt6/
%{_libdir}/pkgconfig/accounts-qt6.pc

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.17.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
