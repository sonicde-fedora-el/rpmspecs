# Generated for SonicDE from Fedora's polkit-qt-1.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-polkit fork, not from download.kde.org.
# The SonicDE fork is Qt6-only (the upstream CMakeLists hardcodes
# QT_MAJOR_VERSION=6 and requires Qt >= 6.5.0), so this spec no longer
# builds the Qt5 variant that Fedora's polkit-qt-1 shipped.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-polkit
# Upstream KDE project: polkit-qt-1
%global oldname polkit-qt-1

#Name:            polkit-qt-1
Name:           sonic-polkit
Version:        0.201.2
Release:        1%{?dist}
Summary:         Qt bindings for PolicyKit

License:         BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later
#URL:             https://api.kde.org/kdesupport-api/polkit-qt-1-apidocs/
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:         https://download.kde.org/stable/%%{name}/polkit-qt-1-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz


BuildRequires:   cmake
BuildRequires:   gcc-c++
BuildRequires:   pkgconfig(polkit-agent-1)
BuildRequires:   pkgconfig(polkit-gobject-1)

Provides:       polkit-qt-1 = %{version}-%{release}
Conflicts:      polkit-qt-1 < %{version}-%{release}

%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt6-1
Summary: PolicyKit Qt6 bindings
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
Provides:  polkit-qt6-1 = %{version}-%{release}
%description -n polkit-qt6-1
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt6-1-devel
Summary: Development files for PolicyKit Qt6 bindings
Requires: polkit-qt6-1%{?_isa} = %{version}-%{release}
Provides:  polkit-qt6-1-devel = %{version}-%{release}
%description -n polkit-qt6-1-devel
%{summary}.

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake -DBUILD_EXAMPLES:BOOL=OFF
%cmake_build

%install
%cmake_install

%files -n polkit-qt6-1
%doc AUTHORS README
%license LICENSES/*
%{_libdir}/libpolkit-qt6-core-1.so.1*
%{_libdir}/libpolkit-qt6-gui-1.so.1*
%{_libdir}/libpolkit-qt6-agent-1.so.1*

%files -n polkit-qt6-1-devel
%{_includedir}/polkit-qt6-1/
%{_libdir}/libpolkit-qt6-core-1.so
%{_libdir}/libpolkit-qt6-gui-1.so
%{_libdir}/libpolkit-qt6-agent-1.so
%{_libdir}/pkgconfig/polkit-qt6-1.pc
%{_libdir}/pkgconfig/polkit-qt6-core-1.pc
%{_libdir}/pkgconfig/polkit-qt6-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt6-agent-1.pc
%{_libdir}/cmake/PolkitQt6-1/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.201.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
