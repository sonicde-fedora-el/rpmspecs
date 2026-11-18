%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-ipc
%global sonicde_qt6_version 6.11.3

Name:           sonic-frameworks-ipc
Summary:        SonicDE IPC framework library
Version:        6.31.0
Release:        2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:            https://github.com/Sonic-DE/%{reponame}

Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules >= %{version}

BuildRequires:  qt6-qtbase-devel >= 6.11

BuildRequires:  sonic-frameworks-logging-devel >= %{version}
BuildRequires:  cmake(SonicLogging) >= %{version}

%description
SonicIpc is the SonicDE inter-process communication framework library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%doc README.md RELEASE-NOTES.md
%{_kf6_libdir}/libSonicIpc.so.*

%files devel
%{_includedir}/Sonic/Ipc/
%{_kf6_libdir}/cmake/SonicIpc/
%{_kf6_libdir}/libSonicIpc.so

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Wed Nov 11 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-1
- Initial SonicDE package for Enterprise Linux 10
