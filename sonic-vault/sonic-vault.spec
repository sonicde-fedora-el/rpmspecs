# Generated for SonicDE from Fedora's plasma-vault.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-vault fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-vault
# Upstream KDE project: plasma-vault
%global oldname plasma-vault


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-vault
Name:           sonic-vault
Summary: Plasma Vault offers strong encryption features in a user-friendly way
Version:        6.7.4
Release:        1%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

# Upstream changes

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(KF6KirigamiPlatform)

# Plasma

BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)

# Qt
BuildRequires:  cmake(Qt6Quick)

## Runtime backends
Recommends: cryfs
Recommends: fuse-encfs
Requires: gocryptfs

Provides:       plasma-vault = %{version}-%{release}
Conflicts:      plasma-vault < %{version}-%{release}

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

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_plugindir}/kded/plasmavault.so
%dir %{_qt6_plugindir}/plasma/applets/
%{_qt6_plugindir}/plasma/applets/org.kde.plasma.vault.so
%{_qt6_plugindir}/kf6/kfileitemaction/plasmavaultfileitemaction.so
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.vault/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
