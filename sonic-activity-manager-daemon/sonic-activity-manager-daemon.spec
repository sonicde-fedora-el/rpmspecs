# Generated for SonicDE from Fedora's kactivitymanagerd.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-activity-manager-daemon fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-activity-manager-daemon
# Upstream KDE project: kactivitymanagerd
%global oldname kactivitymanagerd

#Name:    kactivitymanagerd
Name:           sonic-activity-manager-daemon
Summary: Plasma service to manage user's activities
Version:        6.7.4
Release:        3%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6GuiAddons)

BuildRequires:  boost-devel

# The kactivitymanagerd was split from KActivities in KF5 5.21,
# but thanks to our clever packaging kf5-kactivities package
# already contained only the kactivitymanagerd files
Obsoletes:      kf5-kactivities < 5.21.0

# older ones (previously in kf5-kactivities)
Obsoletes:      kactivities < 4.90.0
Provides:       kactivities%{?_isa} = %{version}-%{release}
Provides:       kactivities = %{version}-%{release}

Provides:       kactivitymanagerd%{?_isa} = %{version}-%{release}
Obsoletes:      kactivitymanagerd < %{version}-%{release}

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang kactivities6 --with-qt


%files -f kactivities6.lang
%license LICENSES/*
%doc README.md
%{_kf6_datadir}/qlogging-categories6/kactivitymanagerd.categories
%{_libexecdir}/kactivitymanagerd
%{_kf6_libdir}/libkactivitymanagerd_plugin.so
%{_kf6_datadir}/dbus-1/services/org.kde.ActivityManager.service
%{_kf6_datadir}/krunner/dbusplugins/plasma-runnners-activities.desktop
%{_userunitdir}/plasma-kactivitymanagerd.service
%{_qt6_plugindir}/kactivitymanagerd1/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
