# Generated for SonicDE from Fedora's plasma-vault.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-vault fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-vault
# Upstream KDE project: plasma-vault
%global oldname plasma-vault


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-vault
Name:           sonic-vault
Summary: Plasma Vault offers strong encryption features in a user-friendly way
Version:        6.8.2
Release:        4%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

# Upstream changes

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-networkmanager-devel
BuildRequires:  sonic-frameworks-data-models-devel
BuildRequires:  sonic-sysguard-library-devel
BuildRequires:  sonic-frameworks-quick-ui-devel

# Plasma

BuildRequires:  sonic-interface-libraries-devel
BuildRequires:  sonic-activities-devel

# Qt
BuildRequires:  qt6-qtdeclarative-devel >= 6.11

## Runtime backends
Recommends: cryfs
Recommends: fuse-encfs
Requires: gocryptfs

Provides:       plasma-vault = %{version}-%{release}
Provides:       plasma-vault%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-vault

%description
Plasma Vault allows to lock and encrypt sets of documents and hide them from
prying eyes even when the user is logged in.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{oldname} --all-name

%files -f %{oldname}.lang
%license LICENSES/*
%{_kf6_plugindir}/kded/plasmavault.so
%dir %{_qt6_plugindir}/plasma/applets/
%{_qt6_plugindir}/plasma/applets/org.kde.plasma.vault.so
%{_qt6_plugindir}/kf6/kfileitemaction/plasmavaultfileitemaction.so
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.vault/

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
- Pin cmake() BuildRequires to SonicDE package names so the
  alma+epel-10 solver cannot pick EPEL's Qt 6.10-linked providers
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
