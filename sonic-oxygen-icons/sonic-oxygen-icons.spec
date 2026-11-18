# Written from scratch: Fedora retired its oxygen-icon-theme package.
# Upstream KDE project: oxygen-icons
%define _disable_source_fetch 0
%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}
%global reponame sonic-oxygen-icons

Name:           sonic-oxygen-icons
Version:        6.31.0.1
Release:        2%{?dist}
Summary:        Oxygen icon theme for SonicDE
License:        LGPL-3.0-or-later
URL:            https://github.com/Sonic-DE/%{reponame}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel >= 6.11

Requires:       hicolor-icon-theme

Provides:       oxygen-icon-theme = %{version}-%{release}
Conflicts:      oxygen-icon-theme < %{version}-%{release}

%description
The Oxygen icon theme, as shipped by SonicDE.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%{_datadir}/icons/oxygen/
%{_metainfodir}/org.kde.oxygenicon.metainfo.xml

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0.1-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
