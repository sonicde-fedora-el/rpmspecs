# Generated for SonicDE from Fedora's plasma-disks.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-disks fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-disks
# Upstream KDE project: plasma-disks
%global oldname plasma-disks

#Name:    plasma-disks
Name:           sonic-disks
Summary: Hard disk health monitoring for KDE Plasma
Version:        6.7.4
Release:        1%{?dist}

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
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6KCMUtils)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Core)

BuildRequires:  smartmontools
Requires:       smartmontools
BuildRequires:  desktop-file-utils

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

Provides:       plasma-disks = %{version}-%{release}
Conflicts:      plasma-disks < %{version}-%{release}

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
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
