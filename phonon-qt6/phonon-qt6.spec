# SonicDE compat build of Phonon for Qt6.
# Fedora's phonon-qt6 is linked against a different qt6 than the pinned
# SonicDE stack. Consumers use cmake(Phonon4Qt6) or pkgconfig(phonon4qt6).
%global sonicde_qt6_version 6.11.3

Name:           phonon-qt6
Version:        4.12.0
Release:        2%{?dist}.sonicde1
Summary:        Multimedia framework library (Qt6)
License:        LGPLv2+
URL:            https://invent.kde.org/libraries/phonon
Source0:        https://download.kde.org/stable/phonon/%{version}/phonon-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse-mainloop-glib) > 0.9.15
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qttools-devel >= 6.11
BuildRequires:  qt6-qt5compat-devel >= 6.11

%description
Phonon multimedia library, Qt6 flavour. Compat package for the SonicDE
package set built against the pinned SonicDE Qt.

%prep
%autosetup -n phonon-%{version}

%build
%cmake -S . \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DPHONON_BUILD_QT5:BOOL=OFF \
  -DPHONON_BUILD_QT6:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%license COPYING.LIB
%{_libdir}/libphonon4qt6.so.*
%{_libdir}/libphonon4qt6experimental.so.*
%{_libdir}/qt6/plugins/designer/phonon4qt6widgets.so
%{_bindir}/phononsettings
%{_datadir}/locale/*/LC_MESSAGES/*.qm

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.

%files devel
%{_includedir}/phonon4qt6/
%{_libdir}/libphonon4qt6.so
%{_libdir}/libphonon4qt6experimental.so
%{_libdir}/cmake/phonon4qt6/
%{_libdir}/pkgconfig/phonon4qt6.pc

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 4.12.0-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Tue Feb 10 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 4.12.0-1.sonicde1
- Compat build against the pinned SonicDE qt6 stack
