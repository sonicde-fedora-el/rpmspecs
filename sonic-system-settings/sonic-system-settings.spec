# Generated for SonicDE from Fedora's systemsettings.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-system-settings fork, not from download.kde.org.
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-system-settings
# Upstream KDE project: systemsettings
%global oldname plasma-systemsettings
%global  base_name systemsettings

#Name:    plasma-systemsettings

Name:           sonic-system-settings
Summary: KDE System Settings application
Version:        6.8.2
Release:        4%{?dist}

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{base_name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: desktop-file-utils
BuildRequires: qt6-qtbase-devel >= 6.11

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-auth-devel
BuildRequires: sonic-frameworks-crash-handler-devel
BuildRequires: sonic-frameworks-data-views-devel
BuildRequires: sonic-frameworks-settings-utils-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-app-info-devel
BuildRequires: sonic-frameworks-icon-themes-devel
BuildRequires: sonic-frameworks-widgets-addons-devel
BuildRequires: sonic-frameworks-windowsystem-devel
BuildRequires: sonic-frameworks-xml-gui-devel
BuildRequires: sonic-frameworks-dbus-devel
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-doctools-devel
BuildRequires: sonic-frameworks-data-models-devel
BuildRequires: sonic-frameworks-gui-addons-devel
BuildRequires: sonic-frameworks-runner-devel
BuildRequires: sonic-frameworks-color-scheme-devel
BuildRequires: sonic-frameworks-progress-ui-devel

BuildRequires: qt6-qtdeclarative-devel >= 6.11

BuildRequires: sonic-activities-devel

BuildRequires: sonic-frameworks-quick-ui-devel
Requires:      sonic-frameworks-quick-ui%{?_isa}

# https://bugzilla.redhat.com/show_bug.cgi?id=1268493
# doc/HTML/en/systemsettings conflicts
Conflicts: kde-workspace < 5.0

# /usr/share/kservices5/settings-system-administration.desktop file conflict
Conflicts: kcm_systemd < 1.2.1-15

Provides:       plasma-systemsettings = %{version}-%{release}
Provides:       plasma-systemsettings%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-systemsettings
Conflicts:      plasma-systemsettings

Provides:  plasma-systemsettings-devel = %{version}-%{release}
Obsoletes:      plasma-systemsettings-devel

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-qt --with-html --all-name


%check


%files -f %{name}.lang
%license LICENSES/*
%{_bindir}/systemsettings
%{_datadir}/systemsettings/
%{_datadir}/applications/sonicdesystemsettings.desktop
%{_datadir}/applications/systemsettings.desktop
%{_datadir}/metainfo/org.kde.systemsettings.metainfo.xml
%{_datadir}/zsh/site-functions/_systemsettings
%{_kf6_datadir}/kglobalaccel/systemsettings.desktop
%{_kf6_datadir}/qlogging-categories6/systemsettings.categories
%{_qt6_plugindir}/kf6/krunner/krunner_systemsettings.so

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
- 6.8.2, renamed to sonic-system-settings from Sonic-DE fork

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-2
- SonicDE build for Enterprise Linux 10

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 6.6.4-1
- 6.6.4
