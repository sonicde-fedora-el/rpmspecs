# Written from scratch: upstream libaccounts-qt has no Fedora Qt 6 package.
%define _disable_source_fetch 0
%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}
%global reponame sonic-qt-accounts-library

Name:           sonic-qt-accounts-library
Version:        1.17.2
Release:        4%{?dist}
Summary:        Qt 6 bindings for libaccounts-glib, as used by SonicDE
License:        LGPL-2.1-only
URL:            https://github.com/Sonic-DE/%{reponame}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(glib-2.0)

Provides:       accounts-qt6 = %{version}-%{release}
Provides:       accounts-qt6%{?_isa} = %{version}-%{release}
Obsoletes:      libaccounts-qt6 < %{version}-%{release}

%description
Qt 6 bindings for libaccounts-glib, the accounts and single sign-on database
used by the SonicDE online accounts integration.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel >= 6.11
Provides:       accounts-qt6-devel = %{version}-%{release}
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
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.17.2-4
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.17.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
