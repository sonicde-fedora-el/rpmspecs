#Compat package: upstream layer-shell-qt rebuilt against SonicDE qt6
#(distro layer-shell-qt pins distro qt6 -> uninstallable in our buildroots)
%global sonicde_qt6_version 6.11.3
%global sonicde_frameworks_version 6.31.0

Name:    layer-shell-qt
Version: 6.8.3
Release: 2%{?dist}
Summary: Library to easily use clients based on wlr-layer-shell

License: BSD-3-Clause AND CC0-1.0 AND LGPL-3.0-or-later AND MIT
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz


BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: ecm-compat-find-modules
BuildRequires: sonic-rpm-macros

BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qtbase-private-devel >= 6.11
BuildRequires: qt6-qtwayland-devel >= 6.11
BuildRequires: qt6-qtdeclarative-devel >= 6.11

BuildRequires: libxkbcommon-devel
BuildRequires: plasma-wayland-protocols-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

%description
This component is meant for applications to be able to easily use clients
based on wlr-layer-shell

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_libdir}/libLayerShellQtInterface.so.*
%{_qt6_plugindir}/wayland-shell-integration/
%{_kf6_qmldir}/org/kde/layershell/

%files devel
%{_includedir}/LayerShellQt/
%{_libdir}/libLayerShellQtInterface.so
%{_libdir}/cmake/LayerShellQt/


%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.3-1
- Update to 6.8.3 so our NVR beats Fedora's same-name package
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-1
- Rebuild upstream layer-shell-qt 6.8.2 against SonicDE qt6
