# Generated for SonicDE from Fedora's kpipewire.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-pipewire fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-pipewire
# Upstream KDE project: kpipewire
%global oldname kpipewire

#Name:    kpipewire
Name:           sonic-pipewire
Summary: Set of convenient classes to use PipeWire in Qt projects
Version:        6.8.2
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        3%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig
# ffmpeg8 compat patch not needed; the fork works with ffmpeg 7.x in EPEL10

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
BuildRequires:  sonic-rpm-macros
Requires: kf6-filesystem >= 6.31

# KDE Frameworks
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  ecm-compat-find-modules
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel

# Misc
BuildRequires:  libdrm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  pipewire-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)

# Plasma
BuildRequires:  plasma-wayland-protocols-devel

# Qt
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtwayland-devel >= 6.11
Provides:       kpipewire = %{version}-%{release}
Provides:       kpipewire%{?_isa} = %{version}-%{release}
Obsoletes:      kpipewire

%description
It is developed in C++ and it's main use target is QML components.
As it's what's been useful, this framework focuses on graphical PipeWire
features. If it was necessary, these could be included.

At the moment we offer two main components:

- KPipeWire: offers the main components to connect to and render
PipeWire into your app.
- KPipeWireRecord: using FFmpeg, helps to record a PipeWire video stream
into a file.

%package        devel
Summary:        Development files for %{name}
# This requires pipewire headers to be installed
Requires: pipewire-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:       kpipewire-devel = %{version}-%{release}
Provides:       kpipewire-devel%{?_isa} = %{version}-%{release}
Provides:       kpipewire-devel = %{version}-%{release}
Provides:       kpipewire-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kpipewire-devel

Provides:       kpipewire-devel = %{version}-%{release}
Provides:       kpipewire-devel%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{oldname} --with-qt --all-name

%files -f %{oldname}.lang
%license LICENSES/*
%{_libdir}/libKPipeWire.so.6
%{_libdir}/libKPipeWire.so.%{libversion}
%{_libdir}/libKPipeWireRecord.so.6
%{_libdir}/libKPipeWireRecord.so.%{libversion}
%{_libdir}/libKPipeWireDmaBuf.so.6
%{_libdir}/libKPipeWireDmaBuf.so.%{libversion}
%{_libdir}/libKPipeWireMonitor.so.6
%{_libdir}/libKPipeWireMonitor.so.%{libversion}
%{_qt6_qmldir}/org/kde/pipewire/*
%{_kf6_datadir}/qlogging-categories6/*.categories

%files devel
%{_libdir}/libKPipeWire.so
%{_libdir}/libKPipeWireRecord.so
%{_libdir}/libKPipeWireDmaBuf.so
%{_libdir}/libKPipeWireMonitor.so
%dir %{_includedir}/KPipeWire
%{_includedir}/KPipeWire/*
%dir %{_libdir}/cmake/KPipeWire
%{_libdir}/cmake/KPipeWire/*.cmake

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
