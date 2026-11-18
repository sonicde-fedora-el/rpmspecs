# Generated for SonicDE from Fedora's ksystemstats.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-system-stats fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-system-stats
# Upstream KDE project: ksystemstats
%global oldname ksystemstats

#Name:    ksystemstats
Name:           sonic-system-stats
Version:        6.8.2
Release:        3%{?dist}
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
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-crash-handler-devel
BuildRequires: sonic-frameworks-dbus-devel
BuildRequires: sonic-frameworks-doctools-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires: sonic-frameworks-icon-themes-devel
BuildRequires: sonic-frameworks-data-views-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-addons-downloader-devel
BuildRequires: sonic-frameworks-notifications-devel
BuildRequires: sonic-frameworks-device-integration-devel
BuildRequires: sonic-frameworks-windowsystem-devel
BuildRequires: sonic-frameworks-networkmanager-devel

BuildRequires: qt6-qtbase-devel >= 6.11

BuildRequires:  libnl3-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  libdrm-devel

Provides:       ksystemstats = %{version}-%{release}
Provides:       ksystemstats%{?_isa} = %{version}-%{release}
Obsoletes:      ksystemstats

%description
KSystemStats is a daemon that collects statistics about the running system.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:       ksystemstats-devel = %{version}-%{release}
Provides:       ksystemstats-devel%{?_isa} = %{version}-%{release}
Obsoletes:      ksystemstats-devel

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
