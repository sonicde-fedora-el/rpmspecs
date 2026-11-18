# Generated for SonicDE from Fedora's kactivitymanagerd.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-activity-manager-daemon fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-activity-manager-daemon
# Upstream KDE project: kactivitymanagerd
%global oldname kactivitymanagerd

#Name:    kactivitymanagerd
Name:           sonic-activity-manager-daemon
Summary: Plasma service to manage user's activities
Version:        6.8.2
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
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qt5compat-devel >= 6.11

BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-keybind-devel
BuildRequires:  sonic-frameworks-xml-gui-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-gui-addons-devel

BuildRequires:  boost-devel

# The kactivitymanagerd was split from KActivities in KF5 5.21,
# but thanks to our clever packaging kf5-kactivities package
# already contained only the kactivitymanagerd files
Obsoletes:      kf5-kactivities < 5.21.0

# older ones (previously in kf5-kactivities)
Obsoletes:      kactivities
Provides:       kactivities = %{version}-%{release}
Provides:       kactivities%{?_isa} = %{version}-%{release}
Provides:       kactivities = %{version}-%{release}

Provides:       kactivitymanagerd = %{version}-%{release}
Provides:       kactivitymanagerd%{?_isa} = %{version}-%{release}
Obsoletes:      kactivitymanagerd

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
