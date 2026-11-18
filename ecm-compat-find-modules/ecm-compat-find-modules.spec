# SonicDE compat package: ECM 6.31 ships these deprecated find-modules in
# its source tree but no longer installs them for Qt6 builds. Packages that
# still call them (kwayland, krfb, others) need them on CMAKE_MODULE_PATH,
# so we install them into the real ECM find-modules dir.
Name:           ecm-compat-find-modules
Version:        6.31.0
Release:        1%{?dist}
Summary:        Uninstalled ECM wayland find-modules for legacy builds

License:        BSD-3-Clause
BuildArch:      noarch

Source0:        FindWayland.cmake
Source1:        FindWaylandScanner.cmake
Source2:        FindWaylandProtocols.cmake
Source3:        FindQtWaylandScanner.cmake
Source4:        ECMFindModuleHelpersStub.cmake

Requires:       sonic-frameworks-cmake-modules

%description
ECM 6.31 keeps its deprecated wayland find-modules in the source tree but
does not install them on Qt6 builds. This package places them in
%{_datadir}/ECM/find-modules/ so legacy packages that still use
ecm_add_wayland_*_protocol and FindQtWaylandScanner keep building.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/ECM/find-modules
install -m644 -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
    %{buildroot}%{_datadir}/ECM/find-modules/

%files
%{_datadir}/ECM/find-modules/FindWayland.cmake
%{_datadir}/ECM/find-modules/FindWaylandScanner.cmake
%{_datadir}/ECM/find-modules/FindWaylandProtocols.cmake
%{_datadir}/ECM/find-modules/FindQtWaylandScanner.cmake
%{_datadir}/ECM/find-modules/ECMFindModuleHelpersStub.cmake

%changelog
* Thu Nov 12 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-1
- SonicDE compat package for uninstalled ECM wayland find-modules
