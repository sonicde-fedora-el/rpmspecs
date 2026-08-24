# Generated for SonicDE from Fedora's qqc2-breeze-style.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-quick-silver-style fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-quick-silver-style
# Upstream KDE project: qqc2-breeze-style
%global oldname qqc2-breeze-style

#Name:    qqc2-breeze-style
Name:           sonic-frameworks-quick-silver-style
Version:        6.7.4
Release:        1%{?dist}
Summary: QtQuickControls2 breeze style

License: CC0-1.0 and GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

## upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros

BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KirigamiPlatform)
BuildRequires: cmake(KF6QuickCharts)

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

Requires:       sonic-frameworks-quick-charts


Provides:       qqc2-breeze-style = %{version}-%{release}
Conflicts:      qqc2-breeze-style < %{version}-%{release}

%description
This is a pure Qt Quick/Kirigami Qt Quick Controls style.

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files 
%doc README.md
%license LICENSES/*.txt
%{_kf6_plugindir}/kirigami/platform/org.kde.breeze.so
%{_qt6_qmldir}/org/kde/breeze/
%{_kf6_libdir}/cmake/QQC2BreezeStyle/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
