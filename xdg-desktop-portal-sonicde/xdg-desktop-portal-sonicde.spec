# Generated for SonicDE from Fedora's xdg-desktop-portal-kde.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/xdg-desktop-portal-sonicde fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame xdg-desktop-portal-sonicde
# Upstream KDE project: xdg-desktop-portal-kde
%global oldname xdg-desktop-portal-kde

#Name:    xdg-desktop-portal-kde
Name:           xdg-desktop-portal-sonicde
Summary: Backend implementation for xdg-desktop-portal using Qt/KF5
Version:        6.8.2
Release:        4%{?dist}

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig
Patch0:         spa-pod-align.patch
Patch1:         xdg-desktop-portal-sonicde-no-autotests.patch

Conflicts:   xdg-desktop-portal-kde
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  ecm-compat-find-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  systemd-rpm-macros

BuildRequires:  qt6-qtbase-devel >= 6.11
# libQt6Gui.so.6(Qt_6.6_PRIVATE_API)(64bit)
# libQt6PrintSupport.so.6(Qt_6.6_PRIVATE_API)(64bit)
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  qt6-qtbase-static >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtquickcontrols2-devel >= 6.11
BuildRequires:  qt6-qtwayland-devel >= 6.11

BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  wayland-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  libei-devel
BuildRequires:  libeis-devel

BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-keybind-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-quick-ui-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-status-notification-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-windowsystem-devel

# Plasma

Requires:       xdg-desktop-portal
# See https://bugzilla.redhat.com/show_bug.cgi?id=2240211
Requires:       xdg-desktop-portal-gtk
Supplements:    sonic-desktop-interface

Provides:       xdg-desktop-portal-kde = %{version}-%{release}
Provides:       xdg-desktop-portal-kde%{?_isa} = %{version}-%{release}
Obsoletes:      xdg-desktop-portal-kde

%description
A backend implementation for xdg-desktop-portal that is using Qt/KF5 and various
pieces of KDE infrastructure.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 -DBUILD_TESTING=OFF

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
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-4
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Conflict with xdg-desktop-portal-kde so the two portal backends cannot
  be installed together
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
