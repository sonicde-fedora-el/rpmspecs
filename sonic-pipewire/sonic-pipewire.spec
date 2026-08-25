# Generated for SonicDE from Fedora's kpipewire.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-pipewire fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-pipewire
# Upstream KDE project: kpipewire
%global oldname kpipewire

#Name:    kpipewire
Name:           sonic-pipewire
Summary: Set of convenient classes to use PipeWire in Qt projects
Version:        6.7.4
Release:        1%{?dist}

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
Requires:       kf6-filesystem

# KDE Frameworks
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)

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
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtwayland-devel

Provides:       kpipewire = %{version}-%{release}
Conflicts:      kpipewire < %{version}-%{release}

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
Requires:       pipewire-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kpipewire-devel = %{version}-%{release}
Provides:       kpipewire-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kpipewire-devel <= 1:5.2.0

Provides:       kpipewire-devel = %{version}-%{release}
Conflicts:      kpipewire-devel < %{version}-%{release}

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
%{_libdir}/libKPipeWire.so.%{version}
%{_libdir}/libKPipeWireRecord.so.6
%{_libdir}/libKPipeWireRecord.so.%{version}
%{_libdir}/libKPipeWireDmaBuf.so.6
%{_libdir}/libKPipeWireDmaBuf.so.%{version}
%{_qt6_qmldir}/org/kde/pipewire/*
%{_kf6_datadir}/qlogging-categories6/*.categories

%files devel
%{_libdir}/libKPipeWire.so
%{_libdir}/libKPipeWireRecord.so
%{_libdir}/libKPipeWireDmaBuf.so
%dir %{_includedir}/KPipeWire
%{_includedir}/KPipeWire/*
%dir %{_libdir}/cmake/KPipeWire
%{_libdir}/cmake/KPipeWire/*.cmake

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
