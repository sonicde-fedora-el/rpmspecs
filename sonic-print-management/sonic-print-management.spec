# Generated for SonicDE from Fedora's print-manager.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-print-management fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-print-management
# Upstream KDE project: print-manager
%global oldname plasma-print-manager
%global  base_name print-manager

#Name:    plasma-print-manager

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           sonic-print-management
Summary: Printer management for KDE
Version:        6.8.2
Release:        4%{?dist}

License: BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{base_name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: gettext
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros

BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-settings-ui-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-dbus-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: sonic-frameworks-icon-themes-devel
BuildRequires: sonic-frameworks-settings-utils-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-quick-ui-devel
BuildRequires: sonic-frameworks-quick-ui-addons-devel
BuildRequires: sonic-frameworks-data-models
BuildRequires: sonic-frameworks-qml-bridge
BuildRequires: sonic-frameworks-notifications-devel
BuildRequires: sonic-frameworks-widgets-addons-devel
BuildRequires: sonic-frameworks-windowsystem-devel

BuildRequires: qt6-qt5compat-devel >= 6.11
BuildRequires: qt6-qtdeclarative-devel >= 6.11

BuildRequires: sonic-interface-libraries-devel

BuildRequires: cmake(packagekitqt6)

BuildRequires: cups-devel >= 1.5.0
# /usr/bin/smbspool (runtime dep, but checked-for at build-time)
BuildRequires: cups
BuildRequires: samba-client

# Renamed from kde-print-manager
Obsoletes:      kde-print-manager < 1:%{version}-%{release}
Provides:       kde-print-manager = 1:%{version}-%{release}

Provides:       plasma-print-manager = %{version}-%{release}
Provides:       plasma-print-manager%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-print-manager
Conflicts:      plasma-print-manager

Requires: sonic-workspace

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# currently requires local cups for majority of proper function
Requires: cups
# required for the com.redhat.NewPrinterNotification D-Bus service
Requires: system-config-printer-libs
# /usr/bin/smbspool
Recommends: samba-client

%description
Printer management for KDE.

%package  libs
Summary:  Runtime files for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes:      kde-print-manager-libs < 1:%{version}-%{release}
Provides:       kde-print-manager-libs = 1:%{version}-%{release}
Provides:       plasma-print-manager-libs = %{version}-%{release}
Provides:       plasma-print-manager-libs%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-print-manager-libs
Conflicts:      plasma-print-manager-libs
%description libs
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.ConfigurePrinter.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.printqueue.desktop


%files -f %{name}.lang
%license LICENSES/*
%{_bindir}/plasma-print-queue
%{_bindir}/configure-printer
%{_kf6_qmldir}/org/kde/plasma/printmanager/
%{_kf6_datadir}/qlogging-categories6/pmlogs.categories
%{_kf6_datadir}/knotifications6/printmanager.notifyrc
%{_kf6_datadir}/applications/kcm_printer_manager.desktop
%{_kf6_datadir}/applications/org.kde.ConfigurePrinter.desktop
%{_kf6_datadir}/applications/org.kde.plasma.printqueue.desktop
%{_kf6_metainfodir}/org.kde.print-manager.metainfo.xml
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_printer_manager.so


%files libs
%{_libdir}/libkcups.so
%{_kf6_plugindir}/kded/printmanager.so
%{_kf6_qtplugindir}/plasma/applets/org.kde.plasma.printmanager.so

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
* Wed Nov 11 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-1
- 6.8.2, renamed to sonic-print-management from Sonic-DE fork

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-2
- SonicDE build for Enterprise Linux 10

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 6.6.4-1
- 6.6.4
