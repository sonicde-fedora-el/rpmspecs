# Generated for SonicDE from Fedora's kf6-qqc2-desktop-style.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-quick-desktop-style fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-quick-desktop-style
# Upstream KDE project: qqc2-desktop-style
%global oldname kf6-qqc2-desktop-style

%global framework qqc2-desktop-style

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-quick-desktop-style
Version:        6.29.0
Release:        1%{?dist}
Summary: QtQuickControls2 style for consistency between QWidget and QML apps
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KFQF-Accepted-GPL
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires: sonic-frameworks-cmake-modules >= %{version}
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: sonic-rpm-macros
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: pkgconfig(xkbcommon)

# Doesn't need qtbase-private-devel, but private stuff from qtdeclarative
# so we still need to rebuild it
#BuildRequires: qt6-qtbase-private-devel

Requires:      sonic-frameworks-spell-check

Provides:       kf6-qqc2-desktop-style = %{version}-%{release}
Conflicts:      kf6-qqc2-desktop-style < %{version}-%{release}

%description
This is a style for QtQuickControls 2 that uses QWidget's QStyle for
painting, making possible to achieve an higher degree of consistency
between QWidget-based and QML-based apps.


%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{oldname} --all-name --with-man --with-qt

%files -f %{oldname}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/cmake/KF6QQC2DesktopStyle/
%{_qt6_qmldir}/org/kde/desktop/
%{_qt6_qmldir}/org/kde/qqc2desktopstyle/
%{_kf6_plugindir}/kirigami/platform/org.kde.desktop.so

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
