# SonicDE compat build of PackageKit-Qt for Qt6.
# Fedora's PackageKit-Qt6 is linked against a different qt6 than the
# pinned SonicDE stack. Consumers use PackageKit-Qt6-devel.
%global sonicde_qt6_version 6.11.3

Name:           packagekit-qt6
Version:        1.1.4
Release:        2%{?dist}.sonicde1
Summary:        PackageKit Qt6 client library
License:        GPLv2+
URL:            https://www.freedesktop.org/software/PackageKit/
Source0:        https://github.com/hughsie/PackageKit-Qt/archive/v%{version}.tar.gz#/PackageKit-Qt-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  PackageKit >= 0.9.1

%description
Qt6 client library for PackageKit. Compat package for the SonicDE
package set built against the pinned SonicDE Qt.

%prep
%autosetup -n PackageKit-Qt-%{version}

%build
%cmake -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/libpackagekitqt6.so.*

%package devel
Summary:        Development files for %{name}
Provides:       PackageKit-Qt6-devel = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.

%files devel
%{_includedir}/PackageKitQt/
%{_libdir}/libpackagekitqt6.so
%{_libdir}/cmake/packagekitqt6/
%{_libdir}/pkgconfig/packagekitqt6.pc

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.1.4-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Tue Feb 10 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.1.4-1.sonicde1
- Compat build against the pinned SonicDE qt6 stack
