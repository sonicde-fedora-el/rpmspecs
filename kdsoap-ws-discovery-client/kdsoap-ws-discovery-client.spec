%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}
Name:           kdsoap-ws-discovery-client
Version:        0.4.0
Release:        5%{?dist}
Summary:        Library for finding WS-Discovery devices in the network using Qt6 and KDSoap

License:        GPL-3.0-or-later AND LicenseRef-OASIS AND LicenseRef-WS-Addressing AND LicenseRef-Discovery AND W3C
URL:            https://invent.kde.org/libraries/kdsoap-ws-discovery-client/
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  qt6-qtbase-devel >= 6.11

%description
%{summary}.

%package        devel
Summary:        Development libraries and header files for Qt6 %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KDSoap-qt6)
%description    devel
%{summary}.

%prep
%autosetup -p1
sed -i '/add_subdirectory(docs)/d' CMakeLists.txt

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON -DBUILD_QCH=OFF -DBUILD_DOCS=OFF
%cmake_build

%install
%cmake_install

%check
# Tests fail without internet
%ctest || :

%files
%doc README.md
%license LICENSES/*
%{_libdir}/libKDSoapWSDiscoveryClient.so.0{,.*}

%files devel
%{_includedir}/KDSoapWSDiscoveryClient/
%{_libdir}/cmake/KDSoapWSDiscoveryClient/
%{_libdir}/libKDSoapWSDiscoveryClient.so

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.4.0-5
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.4.0-4
- SonicDE build for Enterprise Linux 10
