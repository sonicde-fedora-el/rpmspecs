# Generated for SonicDE from Fedora's kmenuedit.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-launcher-menu-edit fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-launcher-menu-edit
# Upstream KDE project: kmenuedit
%global oldname kmenuedit

#Name:    kmenuedit
Name:           sonic-launcher-menu-edit
Summary: KDE menu editor
Version:        6.8.2
Release:        3%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  desktop-file-utils
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-xml-gui-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-data-views-devel
BuildRequires:  sonic-frameworks-spell-check-devel
BuildRequires:  sonic-frameworks-keybind-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  libappstream-glib

# when split out from kde-workspace-4.11.x
Conflicts:      kde-workspace < 4.11.15-3

Provides:       kmenuedit = %{version}-%{release}
Provides:       kmenuedit%{?_isa} = %{version}-%{release}
Obsoletes:      kmenuedit

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kmenuedit5 --with-html --all-name


%check
# commented out until upstream fixes a duplicate entries problem
#appstream-util validate-relax --nonet %%{buildroot}%%{_metainfodir}/*.appdata.xml

%files -f kmenuedit5.lang
%license LICENSES/*
%{_bindir}/kmenuedit
%{_datadir}/kmenuedit/
%{_datadir}/applications/org.kde.kmenuedit.desktop
%{_datadir}/icons/hicolor/*/apps/kmenuedit.*
%{_kf6_datadir}/qlogging-categories6/kmenuedit.categories
%{_kf6_datadir}/metainfo/org.kde.kmenuedit.appdata.xml

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
