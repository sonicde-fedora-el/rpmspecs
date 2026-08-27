# Generated for SonicDE from Fedora's ksystemstats.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-system-stats fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-system-stats
# Upstream KDE project: ksystemstats
%global oldname ksystemstats

#Name:    ksystemstats
Name:           sonic-system-stats
Version:        6.7.4
Release:        4%{?dist}
Summary: KSystemStats is a daemon that collects statistics about the running system.

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires: sonic-sysguard-library-devel

BuildRequires: sonic-rpm-macros
BuildRequires: systemd-rpm-macros
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6NetworkManagerQt)

BuildRequires: cmake(Qt6Widgets)

BuildRequires:  libnl3-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  libdrm-devel

Provides:       ksystemstats%{?_isa} = %{version}-%{release}
Obsoletes:      ksystemstats < %{version}-%{release}

%description
KSystemStats is a daemon that collects statistics about the running system.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:       ksystemstats-devel%{?_isa} = %{version}-%{release}
Obsoletes:      ksystemstats-devel < %{version}-%{release}

%description devel
%{summary}.


%prep
%autosetup -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang ksystemstats_plugins


%files -f ksystemstats_plugins.lang
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/ksystemstats
%{_kf6_bindir}/kstatsviewer
%{_datadir}/dbus-1/services/org.kde.ksystemstats1.service
%{_userunitdir}/plasma-ksystemstats.service
%{_qt6_plugindir}/ksystemstats/
%{_kf6_datadir}/qlogging-categories6/ksystemstats.categories
%caps(cap_perfmon=ep) %{_libexecdir}/ksystemstats_intel_helper

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
