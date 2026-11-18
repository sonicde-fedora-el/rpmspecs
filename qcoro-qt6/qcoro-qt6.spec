# SonicDE compat build of QCoro for Qt6.
# Fedora's qcoro-qt6 is linked against a different qt6 than the pinned
# SonicDE stack. Consumers use cmake(QCoro6) or qcoro-qt6-devel.
%global sonicde_qt6_version 6.11.3

Name:           qcoro-qt6
Version:        0.12.0
Release:        8%{?dist}.sonicde1
Summary:        C++ coroutines for Qt (Qt6)
License:        MIT
URL:            https://qcoro.dvratil.cz/
Source0:        https://github.com/qcoro/qcoro/archive/v%{version}/qcoro-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-private-devel >= 6.11
BuildRequires:  qt6-qtwebsockets-devel >= 6.11

%description
C++ coroutines for Qt, Qt6 flavour. Compat package for the SonicDE
package set built against the pinned SonicDE Qt.

%prep
%autosetup -n qcoro-%{version}

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_QT_VERSION:STRING=6 \
    -DBUILD_TESTING:BOOL=OFF \
    -DQCORO_BUILD_EXAMPLES:BOOL=OFF \
    -DQCORO_ENABLE_ASAN:BOOL=OFF \
    -DQCORO_WITH_QML:BOOL=ON \
    -DQCORO_WITH_QTDBUS:BOOL=ON \
    -DQCORO_WITH_QTNETWORK:BOOL=ON \
    -DQCORO_WITH_QTQUICK:BOOL=ON \
    -DQCORO_WITH_QTWEBSOCKETS:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE LICENSES/MIT.txt
%{_libdir}/libQCoro6Core.so.*
%{_libdir}/libQCoro6DBus.so.*
%{_libdir}/libQCoro6Network.so.*
%{_libdir}/libQCoro6Qml.so.*
%{_libdir}/libQCoro6Quick.so.*
%{_libdir}/libQCoro6WebSockets.so.*

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.

%files devel
%{_includedir}/qcoro6/
%{_libdir}/libQCoro6*.so
%{_libdir}/cmake/QCoro6*/
%{_libdir}/cmake/QCoro6/
%{_libdir}/qt6/mkspecs/modules/qt_QCoro*.pri

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.12.0-8
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.12.0-7
- Bump release above Fedora's -6 so dnf resolves ours deterministically
* Tue Feb 10 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.12.0-1.sonicde1
- Compat build against the pinned SonicDE qt6 stack
