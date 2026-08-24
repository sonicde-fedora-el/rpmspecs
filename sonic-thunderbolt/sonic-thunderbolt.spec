# Generated for SonicDE from Fedora's plasma-thunderbolt.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-thunderbolt fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-thunderbolt
# Upstream KDE project: plasma-thunderbolt
%global oldname plasma-thunderbolt

%global base_name    plasma-thunderbolt


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-thunderbolt
Name:           sonic-thunderbolt
Summary: Plasma integration for controlling Thunderbolt devices
Version:        6.7.4
Release:        1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{base_name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Notifications)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)

BuildRequires:  desktop-file-utils

Requires:       bolt

Provides:       plasma-thunderbolt = %{version}-%{release}
Conflicts:      plasma-thunderbolt < %{version}-%{release}

%description
Plasma Sytem Settings module and a KDED module to handle authorization of
Thunderbolt devices connected to the computer. There's also a shared library
(libkbolt) that implements common interface between the modules and the
system-wide bolt daemon, which does the actual hard work of talking to the
kernel.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{oldname} --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_bolt.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_libdir}/libkbolt.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_bolt.so
%{_kf6_qtplugindir}/kf6/kded/kded_bolt.so
%{_kf6_datadir}/knotifications6/kded_bolt.notifyrc
%{_kf6_datadir}/applications/kcm_bolt.desktop

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
