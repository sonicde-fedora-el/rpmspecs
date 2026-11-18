# Generated for SonicDE from Fedora's powerdevil.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-power-management fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-power-management
# Upstream KDE project: powerdevil
%global oldname powerdevil
#Name:    powerdevil
Name:           sonic-power-management
Version:        6.8.2
Release:        4%{?dist}
Summary: Manages the power consumption settings of a Plasma Shell

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{oldname}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{oldname}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  qt6-qtbase-devel >= 6.11

# Plasma Dependencies
BuildRequires:  sonic-workspace-devel

Provides:       powerdevil = %{version}-%{release}
Provides:       powerdevil%{?_isa} = %{version}-%{release}
Obsoletes:      powerdevil
Conflicts:      powerdevil

# KDE Frameworks 6
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-frameworks-auth-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-keybind-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-idle-tracker-devel
BuildRequires:  sonic-frameworks-data-models-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-quick-ui-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-notification-settings-devel
BuildRequires:  sonic-frameworks-runner-devel
BuildRequires:  sonic-frameworks-device-integration-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-xml-gui-devel
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  sonic-interface-libraries-devel
BuildRequires:  plasma-wayland-protocols-devel >= 1.21.0

BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  cmake(QCoro6)
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtwayland-devel >= 6.11
BuildRequires:  wayland-devel

BuildRequires:  libXrandr-devel
BuildRequires:  libcap-devel
BuildRequires:  sonic-screen-library-devel
BuildRequires:  libxcb-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel

BuildRequires:  sonic-activities-devel

%ifnarch s390 s390x
BuildRequires:  libddcutil-devel
# udev rules
Requires:       ddcutil
Requires: sonic-libworkspace6%{?_isa}
%global DDCUTIL ON
%else
%global DDCUTIL OFF
%endif

# Request a power-profiles-daemon implementation
Recommends: ppd-service
%if 0%{?fedora} && 0%{?fedora} < 41
# Prefer ppd
Suggests: power-profiles-daemon
%else
# Prefer tuned-ppd
Suggests: tuned-ppd
%endif

%description
Powerdevil is an utility for powermanagement. It consists
of a daemon (a KDED module) and a KCModule for its configuration.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html --all-name

# Don't bother with -devel
rm -fv %{buildroot}/%{_libdir}/libpowerdevil{configcommonprivate,core,ui}.so


%files -f %{name}.lang
%license LICENSES/*
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.discretegpuhelper.conf
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.chargethresholdhelper.service
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.chargethresholdhelper.conf
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_datadir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
%{_datadir}/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
%{_datadir}/qlogging-categories6/powerdevil.categories
%{_kf6_libexecdir}/kauth/backlighthelper
%{_kf6_libexecdir}/kauth/discretegpuhelper
%{_kf6_libexecdir}/kauth/chargethresholdhelper
%{_sysconfdir}/xdg/autostart/powerdevil.desktop
%{?with_systemd_cap_workaround:%caps(cap_wake_alarm=ep)} %{_libexecdir}/org_kde_powerdevil
%{_kf6_libdir}/libpowerdevilcore.so.*
%{_kf6_qtplugindir}/powerdevil/
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_powerdevilprofilesconfig.so
%{_kf6_datadir}/knotifications6/powerdevil.notifyrc
%{_kf6_datadir}/applications/kcm_powerdevilprofilesconfig.desktop
%{_kf6_datadir}/applications/kcm_mobile_power.desktop
%{_userunitdir}/plasma-powerdevil.service
%{_qt6_plugindir}/kf6/krunner/krunner_powerdevil.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_power.so
%{_kf6_qmldir}/org/kde/plasma/private/batterymonitor/batterymonitorplugin.qmltypes
%{_kf6_qmldir}/org/kde/plasma/private/batterymonitor/kde-qmlmodule.version
%{_kf6_qmldir}/org/kde/plasma/private/batterymonitor/libbatterymonitorplugin.so
%{_kf6_qmldir}/org/kde/plasma/private/batterymonitor/qmldir
%{_kf6_qmldir}/org/kde/plasma/private/brightnesscontrolplugin/brightnesscontrolplugin.qmltypes
%{_kf6_qmldir}/org/kde/plasma/private/brightnesscontrolplugin/kde-qmlmodule.version
%{_kf6_qmldir}/org/kde/plasma/private/brightnesscontrolplugin/libbrightnesscontrolplugin.so
%{_kf6_qmldir}/org/kde/plasma/private/brightnesscontrolplugin/qmldir
%{_kf6_datadir}/qlogging-categories6/batterymonitor.categories
%{_kf6_datadir}/qlogging-categories6/brightness.categories
%{_kf6_qtplugindir}/plasma/applets/org.kde.plasma*.so
%{_kf6_libexecdir}/kauth/wakeupsourcehelper
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.wakeupsourcehelper.service
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.wakeupsourcehelper.conf
%{_datadir}/polkit-1/actions/org.kde.powerdevil.wakeupsourcehelper.policy

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
- Require sonic-libworkspace6 by name so the SONAME dep cannot
  resolve to Fedora's plasma libkworkspace6 package
* Wed Nov 11 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-1
- 6.8.2, renamed to sonic-power-management from Sonic-DE fork

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-2
- SonicDE build for Enterprise Linux 10, built against sonic-frameworks 6.29.0

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 6.6.4-1
- 6.6.4
