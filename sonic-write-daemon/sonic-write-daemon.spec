# Generated for SonicDE from Fedora's kwrited.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-write-daemon fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-write-daemon
# Upstream KDE project: kwrited
%global oldname kwrited

#Name:    kwrited
Name:           sonic-write-daemon
Summary: KDE Write Daemon
Version:        6.8.2
Release:        3%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-pseudo-terminal-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  git-core

# Owns /usr/share/knotifications5
Requires:       sonic-frameworks-notifications

# TODO: Remove once kwrited is split from kde-workspace
Conflicts:      kde-workspace < 5.0.0-1

Provides:       kwrited = %{version}-%{release}
Provides:       kwrited%{?_isa} = %{version}-%{release}
Obsoletes:      kwrited

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%{_qt6_plugindir}/kf6/kded/kwrited.so
%{_kf6_datadir}/knotifications6/kwrited.notifyrc

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
