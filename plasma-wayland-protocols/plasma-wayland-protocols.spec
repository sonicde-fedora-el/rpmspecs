Name:       plasma-wayland-protocols
Version:    1.23.0
Release:    1%{?dist}
Summary:    Plasma Wayland Protocols

License:    BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND MIT-CMU
URL:        https://invent.kde.org/libraries/plasma-wayland-protocols
Source0:    %{name}-%{version}.tar.xz

BuildArch:  noarch

BuildRequires:  cmake
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

# Samme filsæt som EPELs -devel-underpakke i én noarch-pakke.
Provides:       plasma-wayland-protocols-devel = %{version}-%{release}
Provides:       plasma-wayland-protocols-devel%{?_isa} = %{version}-%{release}

%description
Wayland protocols used by KDE Plasma and its clients.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%dir %{_datadir}/plasma-wayland-protocols
%{_datadir}/plasma-wayland-protocols/*.xml
%dir %{_datadir}/cmake/PlasmaWaylandProtocols
%{_datadir}/cmake/PlasmaWaylandProtocols/*.cmake

%changelog
* Fri Nov 14 2025 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.21.0-1
- SonicDE compat: ship PlasmaWaylandProtocols 1.21.0 because the Alma
  EPEL rebuild lags at 1.20.0 and kwayland requires >= 1.21.0.
