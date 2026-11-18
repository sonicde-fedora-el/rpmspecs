# SonicDE compat package: deprecated Plasma KWayland client library,
# still required as cmake(KWayland) by krfb, sonic-win, sonic-workspace
# and xdg-desktop-portal-sonicde. Bundles ECM's uninstalled
# FindWaylandScanner/FindWaylandProtocols modules because ECM 6.31 no
# longer installs them while kwayland still uses them.
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%if 0%{?fedora}
%global kwayland_version 6.8.3
%else
%global kwayland_version 6.7.5
%endif

Name:       kwayland
Version:    %{kwayland_version}
Release:    10%{?dist}
Summary:    Qt-style API to interact with the wayland-client API

License:    BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT-CMU AND MIT
URL:        https://invent.kde.org/plasma/%{name}

Source0:    kwayland-%{version}.tar.xz
Source1:    FindWaylandScanner.cmake
Source2:    FindWaylandProtocols.cmake
Source3:    ECMFindModuleHelpersStub.cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  ecm-compat-find-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtbase-static >= 6.11
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  qt6-qttools-devel >= 6.11
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

BuildRequires:  plasma-wayland-protocols-devel >= 1.21.0
BuildRequires:  qt6-qtwayland-devel >= 6.11

Requires: kf6-filesystem >= 6.31

# Renamed from kf6-kwayland
Obsoletes:      kf6-kwayland < 1:%{version}-%{release}
Provides:       kf6-kwayland = 1:%{version}-%{release}

%description
%{summary}.

%package    devel
Summary:    Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Obsoletes:  kf6-kwayland-devel < 1:%{version}-%{release}
Provides:   kf6-kwayland-devel = 1:%{version}-%{release}
Provides:   sonicde-kwayland-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:    Developer Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains developer documentation for %{name}.

%prep
%autosetup -p1
mkdir -p compat-find-modules
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} compat-find-modules/
sed -i 's|include(${CMAKE_CURRENT_LIST_DIR}/../modules/ECMFindModuleHelpers.cmake)|include(${ECM_MODULE_DIR}/ECMFindModuleHelpers.cmake)|' compat-find-modules/ECMFindModuleHelpersStub.cmake
sed -i 's|set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH})|set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH} ${CMAKE_SOURCE_DIR}/compat-find-modules)|' CMakeLists.txt

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_libdir}/libKWaylandClient.so.6
%{_libdir}/libKWaylandClient.so.%{version}

%files devel
%doc README.md
%license LICENSES/*.txt
%{_includedir}/KWayland/
%{_libdir}/cmake/KWayland/
%{_libdir}/libKWaylandClient.so
%{_libdir}/pkgconfig/KWaylandClient.pc
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.5-10
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.5-1
- SonicDE compat build; bundle uninstalled ECM wayland find modules
