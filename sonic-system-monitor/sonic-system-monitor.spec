# Generated for SonicDE from Fedora's plasma-systemmonitor.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-system-monitor fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-system-monitor
# Upstream KDE project: plasma-systemmonitor
%global oldname plasma-systemmonitor


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-systemmonitor
Name:           sonic-system-monitor
Version:        6.7.4
Release:        3%{?dist}
Summary: An application for monitoring system resources

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

## upstream patches

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6NewStuff)
# runtime
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: sonic-system-stats

BuildRequires: sonic-sysguard-library-devel

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel

# runtime
Requires: sonic-frameworks-quick-ui%{?_isa}
Requires: sonic-frameworks-quick-ui-addons%{?_isa}
Requires: sonic-frameworks-icon-themes%{?_isa}
Requires: sonic-system-stats%{?_isa}
Requires: sonic-frameworks-quick-charts%{?_isa}

Obsoletes: ksysguard < 5.23

Provides:       plasma-systemmonitor%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-systemmonitor < %{version}-%{release}

%description
An interface for monitoring system sensors, process information and other system
resources.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{oldname} --all-name --with-html

%files -f %{oldname}.lang
%license LICENSES/*.txt
%{_bindir}/plasma-systemmonitor
%{_datadir}/applications/org.kde.plasma-systemmonitor.desktop
%{_datadir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
%{_kf6_datadir}/kglobalaccel/org.kde.plasma-systemmonitor.desktop
%{_kf6_datadir}/knsrcfiles/
%{_kf6_datadir}/metainfo/org.kde.plasma-systemmonitor.metainfo.xml
%{_kf6_datadir}/ksysguard/sensorfaces/
%{_kf6_datadir}/plasma-systemmonitor/
%{_kf6_qmldir}/org/kde/ksysguard/
%{_libdir}/libPlasmaSystemMonitorPage.so
%{_libdir}/libPlasmaSystemMonitorTable.so
%{_kf6_datadir}/kconf_update/plasma-systemmonitor*

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
