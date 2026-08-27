# Generated for SonicDE from Fedora's plasma-browser-integration.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-browser-integration fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-browser-integration
# Upstream KDE project: plasma-browser-integration
%global oldname plasma-browser-integration

#Name:    plasma-browser-integration
Name:           sonic-browser-integration
Summary: %{name} provides components necessary to integrate browsers into the Plasma Desktop
Version:        6.7.4
Release:        3%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND MIT
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

## downstream patches

## upstream patches

## upstreamable patches

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6StatusNotifierItem)

BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  sonic-workspace-devel >= %{version}

Supplements: (sonic-workspace and chromium)
Supplements: (sonic-workspace and firefox)

Provides:       plasma-browser-integration%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-browser-integration < %{version}-%{release}

%description
%{name} coupled with a browser plugin provides integration of the browser in the desktop.

For more information, see
https://community.kde.org/Plasma/Browser_Integration


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 \
  -DMOZILLA_DIR:PATH=%{_libdir}/mozilla \
  -DLIBREWOLF_DIR:PATH=%{_libdir}/librewolf \
  -DWATERFOX_DIR:PATH=%{_libdir}/waterfox
%cmake_build


%install
%cmake_install
%find_lang %{oldname} --all-name


%files -f %{oldname}.lang
%license LICENSES/*
%config %{_sysconfdir}/chromium/native-messaging-hosts/org.kde.plasma.browser_integration.json
%config %{_sysconfdir}/opt/chrome/native-messaging-hosts/org.kde.plasma.browser_integration.json
%config %{_sysconfdir}/opt/edge/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_libdir}/waterfox/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_bindir}/plasma-browser-integration-host
%{_libdir}/mozilla/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_libdir}/librewolf/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_kf6_plugindir}/kded/browserintegrationreminder.so
%{_kf6_datadir}/krunner/dbusplugins/plasma-runner-browserhistory.desktop
%{_kf6_datadir}/krunner/dbusplugins/plasma-runner-browsertabs.desktop
%{_kf6_datadir}/applications/org.kde.plasma.browser_integration.host.desktop
%{_kf6_qtplugindir}/kf6/kded/browserintegrationflatpakintegrator.so

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
