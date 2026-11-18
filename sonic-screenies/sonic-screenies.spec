# Generated for SonicDE from Fedora's spectacle.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-screenies fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
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
Version:        6.8.2
Release:        3%{?dist}

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
BuildRequires:  ecm-compat-find-modules
BuildRequires: sonic-rpm-macros

BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-dbus-devel
BuildRequires: sonic-frameworks-doctools-devel
BuildRequires: sonic-frameworks-keybind-devel
BuildRequires: sonic-frameworks-gui-addons-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-quick-ui-devel
BuildRequires: sonic-frameworks-notifications-devel
BuildRequires: sonic-frameworks-purpose-devel
BuildRequires: sonic-frameworks-windowsystem-devel
BuildRequires: sonic-frameworks-xml-gui-devel
BuildRequires: sonic-frameworks-status-notification-devel
BuildRequires: sonic-frameworks-barcode-devel
BuildRequires: sonic-frameworks-crash-handler-devel
BuildRequires: cmake(KQuickImageEditor)

BuildRequires: sonic-pipewire-devel
BuildRequires: ffmpeg-free-devel
BuildRequires: cmake(LayerShellQt)
BuildRequires: plasma-wayland-protocols-devel >= 1.21.0

BuildRequires: qt6-qtbase-private-devel >= 6.11
BuildRequires: cmake(OpenCV)
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires: qt6-qtwayland-devel >= 6.11
BuildRequires: qt6-qtmultimedia-devel >= 6.11
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
Provides:       spectacle%{?_isa} = %{version}-%{release}
Obsoletes:      spectacle

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

%files -f %{oldname}.lang
%license LICENSES/*
%{_kf6_bindir}/sonic-screenies
%{_kf6_datadir}/man/man1/sonic-screenies.1*
%{_kf6_metainfodir}/org.kde.spectacle.appdata.xml
%{_kf6_datadir}/applications/org.kde.spectacle.desktop
%{_kf6_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_kf6_datadir}/dbus-1/interfaces/org.sonicde.Screenies.xml
%{_kf6_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_kf6_datadir}/dbus-1/services/org.kde.spectacle.service
%{_kf6_datadir}/dbus-1/services/org.sonicde.screenies.service
%{_kf6_datadir}/icons/hicolor/*/apps/sonic-screenies.*
%{_kf6_datadir}/kglobalaccel/org.kde.spectacle.desktop
%{_kf6_datadir}/knotifications6/spectacle.notifyrc
%{_kf6_datadir}/qlogging-categories6/%{oldname}*
%{_kf6_libdir}/kconf_update_bin/spectacle*
%{_kf6_datadir}/kconf_update/spectacle*
%{_userunitdir}/app-org.kde.spectacle.service
%{_userunitdir}/app-org.sonicde.screenies.service

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
