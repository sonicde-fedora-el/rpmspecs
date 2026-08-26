# Generated for SonicDE from Fedora's kcm_wacomtablet.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-drawing-tablet fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-drawing-tablet
# Upstream KDE project: wacomtablet
%global oldname kcm_wacomtablet


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    kcm_wacomtablet
Name:           sonic-drawing-tablet
Summary: KDE Control module for Wacom Graphictablets
Version:        6.7.4
Release:        1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
#URL:     https://invent.kde.org/system/wacomtablet
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/wacomtablet-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/wacomtablet-%%{version}.tar.xz.sig

## upstream patches

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KirigamiPlatform)
BuildRequires: cmake(Plasma5Support)
BuildRequires: cmake(Plasma)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: sonic-rpm-macros

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel

BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xrandr)

ExcludeArch: s390 s390x

Obsoletes: kcm-wacomtablet < 1.3.7-2
Provides:  kcm-wacomtablet = %{version}-%{release}

Provides:       kcm_wacomtablet = %{version}-%{release}
Conflicts:      kcm_wacomtablet < %{version}-%{release}

%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button/pen layouts per profile.


%prep
%autosetup -n %{reponame}-%{version}
sed -i '/pkg_check_modules(XORGWACOM/d' CMakeLists.txt
sed -i 's/XORGWACOM_LIBRARIES//g' CMakeLists.txt
sed -i 's|#include <xorg/wacom-properties.h>|#define WACOM_PROP_SERIALIDS "Wacom Serial IDs"\n#define WACOM_PROP_TABLET_AREA "Wacom Tablet Area"\n#define WACOM_PROP_TOOL_TYPE "Wacom Tool Type"\n#define WACOM_PROP_PRESSURE_THRESHOLD "Wacom Pressure Threshold"\n#define WACOM_PROP_SAMPLEGROUP "Wacom Sample and Group"\n#define WACOM_PROP_PRESSURECURVE "Wacom Pressure Curve"\n#define WACOM_PROP_BUTTONMODES "Wacom Button Modes"\n#define WACOM_PROP_BUTTONACTIONS "Wacom Button Actions"\n#define WACOM_PROP_WHEELBUTTONS "Wacom Wheel Buttons"\n#define WACOM_PROP_STRIPBUTTONS "Wacom Strip Buttons"\n#define WACOM_PROP_ROTATION "Wacom Rotation"\n#define WACOM_PROP_TOUCH "Wacom Enable Touch"\n#define WACOM_PROP_GESTURE_ENABLE "Wacom Enable Gesture"\n#define WACOM_PROP_HOVER "Wacom Hover Enable"\n#define WACOM_PROP_PROXIMITY_THRESHOLD "Wacom Proximity Threshold"\n#define WACOM_PROP_DEBUGLEVEL "Wacom Debug Level"|' src/common/x11input.cpp
sed -i 's|#include <X11/Xwacomdefs.h>|/* #include <X11/Xwacomdefs.h> */|' src/common/x11input.cpp


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{oldname} --all-name --with-html


%files -f %{oldname}.lang
%doc AUTHORS
%license COPYING*
%{_datadir}/dbus-1/interfaces/org.kde.Wacom*.xml
%{_kf6_bindir}/kde_wacom_tabletfinder
%{_kf6_datadir}/applications/kcm_wacomtablet.desktop
%{_kf6_datadir}/applications/kde_wacom_tabletfinder.desktop
%{_kf6_datadir}/knotifications6/wacomtablet.notifyrc
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.wacomtablet/
%{_kf6_datadir}/plasma5support/services/wacomtablet.operations
%{_kf6_datadir}/wacomtablet/
%{_kf6_datadir}/qlogging-categories6/wacomtablet.categories
%{_kf6_metainfodir}/org.kde.wacomtablet.metainfo.xml
%{_qt6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_wacomtablet.so
%{_kf6_plugindir}/kded/wacomtablet.so
%{_qt6_plugindir}/plasma5support/dataengine/plasma_engine_wacomtablet.so

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
