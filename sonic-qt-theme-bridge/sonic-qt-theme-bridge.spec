# Generated for SonicDE from Fedora's plasma-integration.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-qt-theme-bridge fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-qt-theme-bridge
# Upstream KDE project: plasma-integration
%global oldname plasma-integration

# SonicDE is a Qt6/KF6-only hard fork; no KF5 packages are shipped.
%bcond_with kf5

#Name:    plasma-integration
Name:           sonic-qt-theme-bridge
Summary: Qt Platform Theme integration plugin for Plasma
Version:        6.8.2
Release:        3%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  wayland-devel
BuildRequires:  plasma-wayland-protocols-devel >= 1.21.0

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)

BuildRequires:  qt6-qtwayland-devel >= 6.11
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-status-notification-devel

%if %{with kf5}
# Qt5 build
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  qt5-qtbase-private-devel
# Qt5ThemeSupport
BuildRequires:  qt5-qtbase-static

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5GuiAddons)

Requires:       (%{name}-qt5 if qt5-qtbase-gui)
%endif

Requires:       sonic-breeze%{?_isa}
Requires:       breeze-cursor-theme
Requires:       sonic-silver-icon-theme
Recommends:     sonic-workspace

# The default QtQuick styles
Requires:       sonic-frameworks-quick-silver-style%{?_isa}
Requires:       sonic-frameworks-quick-desktop-style%{?_isa}

# The default fonts
Requires:       font(notosans)
Recommends:     font(hack)

Provides:       plasma-integration = %{version}-%{release}
Provides:       plasma-integration%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-integration

%description
%{summary}.

%if %{with kf5}
%package        qt5
Summary:        Qt5 support for %{name}
# The default QtQuick style
Requires:       qqc2-desktop-style%{?_isa}
Provides:       plasma-integration-qt5 = %{version}-%{release}
Provides:       plasma-integration-qt5%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-integration-qt5

%description    qt5
%{summary}.
%endif

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%global _vpath_builddir %{_target_platform}-qt6
%cmake_kf6 -DBUILD_QT5=OFF -DBUILD_QT6=ON
%cmake_build

%if %{with kf5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_kf5 -DBUILD_QT5=ON  -DBUILD_QT6=OFF
%cmake_build
%endif


%install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%if %{with kf5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%endif

%find_lang plasmaintegration5

%files -f plasmaintegration5.lang
%doc README.md
%license LICENSES
%{_qt6_plugindir}/platformthemes/KDEPlasmaPlatformTheme6.so

%if %{with kf5}
%files qt5
%{_qt5_plugindir}/platformthemes/KDEPlasmaPlatformTheme5.so
%endif

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
