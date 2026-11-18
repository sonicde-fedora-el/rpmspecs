# Generated for SonicDE from Fedora's qqc2-breeze-style.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-quick-silver-style fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-frameworks-quick-silver-style
# Upstream KDE project: qqc2-breeze-style
%global oldname qqc2-breeze-style

#Name:    qqc2-breeze-style
Name:           sonic-frameworks-quick-silver-style
Version:        6.8.2
Release:        3%{?dist}
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

BuildRequires: sonic-frameworks-color-scheme-devel
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-gui-addons-devel
BuildRequires: sonic-frameworks-icon-themes-devel
BuildRequires: sonic-frameworks-quick-ui-devel
BuildRequires: sonic-frameworks-quick-charts-devel

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
Requires:       sonic-frameworks-quick-charts


Provides:       qqc2-breeze-style = %{version}-%{release}
Provides:       qqc2-breeze-style%{?_isa} = %{version}-%{release}
Obsoletes:      qqc2-breeze-style

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
