# Generated for SonicDE from Fedora's plasma-disks.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-disks fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-disks
# Upstream KDE project: plasma-disks
%global oldname plasma-disks

#Name:    plasma-disks
Name:           sonic-disks
Summary: Hard disk health monitoring for KDE Plasma
Version:        6.8.2
Release:        3%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-only AND GPL-3.0-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-auth-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-app-info-devel
BuildRequires:  sonic-frameworks-device-integration-devel
BuildRequires:  sonic-frameworks-settings-utils-devel

BuildRequires:  qt6-qtbase-devel >= 6.11

BuildRequires:  smartmontools
Requires:       smartmontools
BuildRequires:  desktop-file-utils

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

Provides:       plasma-disks = %{version}-%{release}
Provides:       plasma-disks%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-disks

%description
Plasma Disks monitors S.M.A.R.T. data of disks and alerts the user when
signs of imminent failure appear.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{oldname} --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_disks.desktop

%files -f %{oldname}.lang
%license LICENSES/*.txt
%{_libexecdir}/kf6/kauth/kded-smart-helper
%{_qt6_plugindir}/plasma/kcms/kinfocenter/kcm_disks.so
%{_kf6_plugindir}/kded/smart.so
%{_kf6_datadir}/applications/kcm_disks.desktop
%{_kf6_datadir}/dbus-1/system-services/org.kde.kded.smart.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.kded.smart.conf
%{_kf6_datadir}/knotifications6/org.kde.kded.smart.notifyrc
%{_kf6_datadir}/metainfo/org.kde.plasma.disks.metainfo.xml
%{_kf6_datadir}/polkit-1/actions/org.kde.kded.smart.policy

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
