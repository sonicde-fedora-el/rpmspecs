Name:    powerdevil
Version:        6.7.4
Release:        2%{?dist}
Summary: Manages the power consumption settings of a Plasma Shell

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# Plasma Dependencies
BuildRequires:  sonic-workspace-devel

# KDE Frameworks 6
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaWaylandProtocols)

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6WaylandClient)
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

BuildRequires:  cmake(PlasmaActivities)

%ifnarch s390 s390x
BuildRequires:  libddcutil-devel
# udev rules
Requires:       ddcutil
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
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang powerdevil6 --with-html --all-name

# Don't bother with -devel
rm -fv %{buildroot}/%{_libdir}/libpowerdevil{configcommonprivate,core,ui}.so


%files -f powerdevil6.lang
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
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-2
- SonicDE build for Enterprise Linux 10, built against sonic-frameworks 6.29.0

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 6.6.4-1
- 6.6.4
