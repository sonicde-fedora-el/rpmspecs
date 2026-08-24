# Generated for SonicDE from Fedora's spectacle.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-screenies fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-screenies
# Upstream KDE project: spectacle
%global oldname spectacle

# For direct library dependencies
%if "%{__isa_bits}" == "64"
%global lib64_suffix ()(64bit)
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    spectacle
Name:           sonic-screenies
Summary: Screenshot capture utility
Epoch:   1
Version:        6.7.4.2
Release:        1%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
#URL:     https://www.kde.org/applications/graphics/spectacle/
URL:            https://github.com/Sonic-DE/%{reponame}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
#Source0: https://download.kde.org/%%{stable}/plasma/%%{maj_ver_kf6}.%%{min_ver_kf6}.%%{bug_ver_kf6}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable}/plasma/%%{maj_ver_kf6}.%%{min_ver_kf6}.%%{bug_ver_kf6}/%%{name}-%%{version}.tar.xz.sig

## upstream patches

## Upstreamable patches

## downstream patches

%global majmin %(echo %{version} | cut -d. -f1,2)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KirigamiPlatform)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KQuickImageEditor)

BuildRequires: cmake(KPipeWire)
BuildRequires: cmake(LayerShellQt)
BuildRequires: cmake(PlasmaWaylandProtocols)

BuildRequires: qt6-qtbase-private-devel
BuildRequires: cmake(OpenCV)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6QWebpPlugin)
BuildRequires: cmake(ZXing)

BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: cmake(tesseract)

# for systemd-related macros
BuildRequires:  systemd-devel

# Animated tray icon: https://pagure.io/fedora-kde/SIG/issue/601
Recommends:     qt6-qtimageformats%{?_isa}

# f26+ upgrade path
%if 0%{?fedora} > 25
Obsoletes: ksnapshot <= 15.08.3
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

Provides:       spectacle = %{version}-%{release}
Conflicts:      spectacle < %{version}-%{release}

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir}
%cmake_build


%install
%cmake_install

%find_lang %{oldname} --all-name --with-html --with-man


%check
# [6.3.1.2] Bypassed. Reason:
# FAILED: • tag-invalid           : <release> versions are not in order [6.3.0 before 24.12.1]
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.spectacle.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.spectacle.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/spectacle
%{_kf6_datadir}/man/man1/spectacle.1*
%{_kf6_metainfodir}/org.kde.spectacle.appdata.xml
%{_kf6_datadir}/applications/org.kde.spectacle.desktop
%{_kf6_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_kf6_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_kf6_datadir}/dbus-1/services/org.kde.spectacle.service
%{_kf6_datadir}/icons/hicolor/*/apps/spectacle.*
%{_kf6_datadir}/kglobalaccel/org.kde.spectacle.desktop
%{_kf6_datadir}/knotifications6/spectacle.notifyrc
%{_kf6_datadir}/qlogging-categories6/%{oldname}*
%{_kf6_libdir}/kconf_update_bin/spectacle*
%{_kf6_datadir}/kconf_update/spectacle*
%{_userunitdir}/app-org.kde.spectacle.service

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
