# Generated for SonicDE from Fedora's bluedevil.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-bluetooth-runtime fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-bluetooth-runtime
# Upstream KDE project: bluedevil
%global oldname bluedevil


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    bluedevil
Name:           sonic-bluetooth-runtime
Summary: Bluetooth stack for KDE
Version:        6.8.2
Release:        4%{?dist}

License: GPL-2.0-or-later
#URL:     https://cgit.kde.org/%%{name}.git
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig


BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  sonic-frameworks-bluetooth-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-daemon-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-svg-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
# runtime
BuildRequires:  sonic-frameworks-quick-ui-devel

# Plasma
BuildRequires:  sonic-interface-libraries-devel

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  shared-mime-info
BuildRequires:  desktop-file-utils

Provides:       dbus-bluez-pin-helper

Obsoletes:      kbluetooth < 0.4.2-3
Obsoletes:      bluedevil-devel < 2.0.0-0.10

Requires:       bluez >= 5
Requires:       bluez-obexd
Requires:       sonic-daemon
Requires:       pulseaudio-module-bluetooth
# runtime
Requires:       sonic-frameworks-quick-ui

# When -autostart was removed
Obsoletes:      bluedevil-autostart < 5.2.95
Obsoletes:      bluedevil

Provides:       bluedevil = %{version}-%{release}
Provides:       bluedevil%{?_isa} = %{version}-%{release}
%description
BlueDevil is the bluetooth stack for KDE.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{oldname} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.bluedevilsendfile.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.bluedevilwizard.desktop


%files -f %{oldname}.lang
%doc README
%{_datadir}/mime/packages/bluedevil-mime.xml
%{_kf6_bindir}/bluedevil-sendfile
%{_kf6_bindir}/bluedevil-wizard
%{_kf6_datadir}/applications/kcm_bluetooth.desktop
%{_kf6_datadir}/applications/org.kde.bluedevilsendfile.desktop
%{_kf6_datadir}/applications/org.kde.bluedevilwizard.desktop
%{_kf6_datadir}/bluedevilwizard/
%{_kf6_datadir}/knotifications6/bluedevil.notifyrc
%{_kf6_qmldir}/org/kde/bluedevil/
%{_kf6_qtplugindir}/plasma/applets/org.kde.plasma.bluetooth.so
%{_kf6_datadir}/qlogging-categories6/bluedevil.categories
%{_kf6_datadir}/remoteview/bluetooth-network.desktop
%{_kf6_plugindir}/kded/*.so
%{_kf6_plugindir}/kio/*.so
%{_kf6_qmldir}/org/kde/plasma/private/bluetooth/
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_bluetooth.so

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
- Pin Plasma cmake deps to SonicDE providers (Fedora libplasma 6.8.3 outranks ours)
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
