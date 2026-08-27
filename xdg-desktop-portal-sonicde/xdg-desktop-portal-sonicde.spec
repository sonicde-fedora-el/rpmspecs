# Generated for SonicDE from Fedora's xdg-desktop-portal-kde.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/xdg-desktop-portal-sonicde fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame xdg-desktop-portal-sonicde
# Upstream KDE project: xdg-desktop-portal-kde
%global oldname xdg-desktop-portal-kde

#Name:    xdg-desktop-portal-kde
Name:           xdg-desktop-portal-sonicde
Summary: Backend implementation for xdg-desktop-portal using Qt/KF5
Version:        6.7.4
Release:        5%{?dist}

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig
Patch0:         spa-pod-align.patch

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  systemd-rpm-macros

BuildRequires:  qt6-qtbase-devel
# libQt6Gui.so.6(Qt_6.6_PRIVATE_API)(64bit)
# libQt6PrintSupport.so.6(Qt_6.6_PRIVATE_API)(64bit)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtquickcontrols2-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  cmake(Qt6WaylandClient)

BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  wayland-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)

# Plasma
BuildRequires:  cmake(KWayland)

Requires:       xdg-desktop-portal
# See https://bugzilla.redhat.com/show_bug.cgi?id=2240211
Requires:       xdg-desktop-portal-gtk
Supplements:    sonic-desktop-interface

Provides:       xdg-desktop-portal-kde%{?_isa} = %{version}-%{release}
Obsoletes:      xdg-desktop-portal-kde < %{version}-%{release}

%description
A backend implementation for xdg-desktop-portal that is using Qt/KF5 and various
pieces of KDE infrastructure.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang xdg-desktop-portal-kde


%files -f xdg-desktop-portal-kde.lang
%license LICENSES/*
%{_libexecdir}/xdg-desktop-portal-sonicde
%{_libexecdir}/xdg-desktop-portal-kde
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.sonicde.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
%{_datadir}/xdg-desktop-portal/portals/sonicde.portal
%{_datadir}/xdg-desktop-portal/portals/kde.portal
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.sonicde.desktop
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.kde.desktop
%{_datadir}/knotifications6/xdg-desktop-portal-kde.notifyrc
%{_datadir}/qlogging-categories6/xdp-kde.categories
%{_userunitdir}/plasma-xdg-desktop-portal-sonicde.service
%{_userunitdir}/plasma-xdg-desktop-portal-kde.service
%{_datadir}/xdg-desktop-portal/sonicde-portals.conf

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
