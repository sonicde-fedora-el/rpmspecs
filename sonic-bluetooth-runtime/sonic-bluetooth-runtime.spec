# Generated for SonicDE from Fedora's bluedevil.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-bluetooth-runtime fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-bluetooth-runtime
# Upstream KDE project: bluedevil
%global oldname bluedevil


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    bluedevil
Name:           sonic-bluetooth-runtime
Summary: Bluetooth stack for KDE
Version:        6.7.4
Release:        1%{?dist}

License: GPL-2.0-or-later
#URL:     https://cgit.kde.org/%%{name}.git
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig


BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KDED)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
# runtime
BuildRequires:  cmake(KF6Kirigami)

# Plasma
BuildRequires:  cmake(Plasma)

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
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

Provides:       bluedevil = %{version}-%{release}
Conflicts:      bluedevil < %{version}-%{release}

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
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
