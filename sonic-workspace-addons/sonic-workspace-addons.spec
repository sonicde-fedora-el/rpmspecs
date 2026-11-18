# Generated for SonicDE from Fedora's kdeplasma-addons.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-workspace-addons fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-workspace-addons
# Upstream KDE project: kdeplasma-addons
%global oldname kdeplasma-addons

#Name:    kdeplasma-addons
Name:           sonic-workspace-addons
Summary: Additional Plasmoids for Plasma 6
Version:        6.8.2
Release:        3%{?dist}

%global source_licenses %{shrink:
    BSD-3-Clause AND
    CC0-1.0 AND
    GPL-2.0-only AND
    GPL-2.0-or-later AND
    GPL-3.0-only AND
    GPL-3.0-or-later AND
    LGPL-2.0-only AND
    LGPL-2.0-or-later AND
    LGPL-2.1-only AND
    LGPL-2.1-or-later AND
    LGPL-3.0-only AND
    LGPL-3.0-or-later AND
    (GPL-2.0-only OR GPL-3.0-only) AND
    (LGPL-2.1-only OR LGPL-3.0-only) AND
    MIT
    }
License: %{source_licenses}
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig


ExcludeArch: %{ix86}

%ifarch %{qt6_qtwebengine_arches}
BuildRequires:  qt6-qtwebengine-devel >= 6.11
%endif

## upstream patches

Obsoletes: kdeplasma-addons-libs < 5.0.0

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-holidays-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-addons-downloader-devel
BuildRequires:  sonic-frameworks-runner-devel
BuildRequires:  sonic-frameworks-app-info-devel
BuildRequires:  sonic-frameworks-keybind-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-spell-check-devel
BuildRequires:  sonic-frameworks-unit-conversion-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-svg-devel
BuildRequires:  sonic-frameworks-quick-ui-devel
BuildRequires:  sonic-plasma5-support-library-devel
BuildRequires:  sonic-rpm-macros >= 5.25.0-2
BuildRequires:  libicu-devel
BuildRequires:  libxcb-devel
BuildRequires:  qt6-qtquick3d-devel >= 6.11
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qt5compat-devel >= 6.11
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-workspace-devel
BuildRequires: sonic-sysguard-library-devel
BuildRequires:  sonic-frameworks-xml-gui-devel

BuildRequires:  sonic-interface-libraries-devel
BuildRequires:  sonic-activities-devel

# The SonicDE fork implements the QMK VIA helper in C++ on top of SonicVia
# instead of the Rust qmk-via-api crate.
BuildRequires:  cmake(SonicVia)
BuildRequires:  polkit-qt6-1-devel

# for notes.svgz
Requires:       sonic-interface-libraries

# Quickshare applet runtime dep
BuildRequires:  sonic-frameworks-purpose-devel
BuildRequires:  sonic-frameworks-logging-devel
Recommends:     sonic-frameworks-purpose%{?_isa}

# Cube effect
Requires:       qt6-qtquick3d%{?_isa}

Requires:       sonic-frameworks-data-models%{?_isa}
Requires:       sonic-frameworks-quick-ui-addons%{?_isa}

Provides:       kdeplasma-addons = %{version}-%{release}
Provides:       kdeplasma-addons%{?_isa} = %{version}-%{release}
Obsoletes:      kdeplasma-addons < %{version}-%{release}

%description
%{summary}.

%package -n kate-krunner-plugin
Summary: KRunner plugin for searching Kate sessions
License: %{source_licenses}
Requires: kate
Supplements: kate
# Before the split
Conflicts: sonic-workspace-addons < 5.92.0-3
%description -n kate-krunner-plugin
%{summary}.

%package devel
Summary:        Development files for %{name}
License: %{source_licenses}
# headers only: fixme: confirm need for dep on main pkg? -- rdieter
Requires: %{name} = %{version}-%{release}
#find_dependency(Qt5Gui "5.12.0")
#find_dependency(KF5CoreAddons "5.58.0")
Requires: qt6-qtbase-devel >= 6.11
Requires: sonic-frameworks-core-addons-devel
Provides:       kdeplasma-addons-devel = %{version}-%{release}
Provides:       kdeplasma-addons-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kdeplasma-addons-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%conf
%cmake_kf6

%build
%cmake_build

%install
%cmake_install
%find_lang kdeplasmaaddons5_qt --with-qt --all-name

%files -f kdeplasmaaddons5_qt.lang
%license LICENSES/*.txt
%{_kf6_datadir}/kwin/effects/cube/
%{_kf6_datadir}/plasma/plasmoids/*
%{_kf6_datadir}/plasma/desktoptheme/default/widgets/*
%{_kf6_datadir}/plasma/desktoptheme/default/weather/
%{_kf6_datadir}/plasma/wallpapers/*
%{_kf6_datadir}/plasma/layout-templates/
%{_kf6_datadir}/qlogging-categories6/kdeplasma-addons.categories
%{_kf6_datadir}/qlogging-categories6/kdeplasma-addons.renamecategories
%{_kf6_qtplugindir}/plasma/applets/*.so
%{_kf6_plugindir}/krunner/kcms/kcm_krunner_charrunner.so
%{_kf6_plugindir}/krunner/kcms/kcm_krunner_dictionary.so
%{_kf6_plugindir}/krunner/kcms/kcm_krunner_spellcheck.so
%{_kf6_plugindir}/krunner/krunner_charrunner.so
%{_kf6_plugindir}/krunner/krunner_dictionary.so
%{_kf6_plugindir}/krunner/krunner_konsoleprofiles.so
%{_kf6_plugindir}/krunner/krunner_spellcheck.so
%{_kf6_plugindir}/krunner/org.kde.datetime.so
%{_kf6_plugindir}/krunner/unitconverter.so
%{_kf6_plugindir}/packagestructure/*.so
%{_kf6_qtplugindir}/plasmacalendarplugins/
%{_kf6_qtplugindir}/kwin/effects/configs/kwin_cube_config.so
%{_kf6_qtplugindir}/potd/
%{_kf6_qmldir}/org/kde/plasma/*
%{_kf6_datadir}/knotifications6/plasma_applet_timer.notifyrc
%{_datadir}/kwin/tabbox/
%{_datadir}/icons/hicolor/scalable/apps/accessories-dictionary.svgz
%{_datadir}/knsrcfiles/comic.knsrc
%{_kf6_libdir}/libplasmapotdprovidercore.so.*
%{_libdir}/qt6/qml/org/kde/plasmacalendar/astronomicaleventsconfig/*
%{_kf6_plugindir}/kded/kameleon.so
%{_kf6_plugindir}/krunner/krunner_colors.so
%{_kf6_libexecdir}/kauth/kameleonhelper
%{_kf6_datadir}/dbus-1/system-services/org.kde.kameleonhelper.service
%{_kf6_datadir}/dbus-1/system-services/org.kde.kameleon.qmk.helper.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.kameleonhelper.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.kameleonhelper.policy
%{_libdir}/libplasmaweatherdata.so.*
%{_libdir}/libplasmaweatherion.so.*
%{_kf6_qtplugindir}/plasma/weather_ions/bbcukmet.so
%{_kf6_qtplugindir}/plasma/weather_ions/dwd.so
%{_kf6_qtplugindir}/plasma/weather_ions/envcan.so
%{_kf6_qtplugindir}/plasma/weather_ions/noaa.so
%{_datadir}/plasma/weather/noaa_station_list.xml
%{_datadir}/kwin/scripts/virtualdesktopsonlyonprimary/
%{_kf6_libexecdir}/kameleon-qmk-helper
%{_kf6_datadir}/dbus-1/system.d/org.kde.kameleon.qmk.helper.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.kameleon.qmk.helper.policy

%files -n kate-krunner-plugin
%{_kf6_plugindir}/krunner/krunner_katesessions.so

%files devel
%{_libdir}/libplasmaweatherdata.so
%{_libdir}/libplasmaweatherion.so
%{_libdir}/cmake/PlasmaPotdProvider/
%{_includedir}/plasma/potdprovider/
%{_kf6_datadir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2
%{_kf6_libdir}/libplasmapotdprovidercore.so
%{_includedir}/plasma/weather/
%{_libdir}/cmake/PlasmaWeather/

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
