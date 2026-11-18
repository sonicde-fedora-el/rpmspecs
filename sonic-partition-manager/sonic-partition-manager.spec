# Generated for SonicDE from Fedora's kde-partitionmanager.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-partition-manager fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-partition-manager
# Upstream KDE project: partitionmanager
%global oldname kde-partitionmanager

%global base_name partitionmanager

%global kf6min 5.240.0
%global qt6min 6.5.0
%global kpmcoremin 24.01


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:           kde-partitionmanager
Name:           sonic-partition-manager
Version:        26.08.3
Release:        3%{?dist}
Summary:        KDE Partition Manager

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND CC-BY-4.0 AND CC0-1.0 AND GFDL-1.2-or-later
#URL:            https://apps.kde.org/partitionmanager/
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:        https://download.kde.org/%%{stable_kf6}/release-service/%%{version}/src/partitionmanager-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  gettext
BuildRequires:  sonic-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  qt6-qtbase-devel >= 6.11

BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-progress-ui-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-xml-gui-devel
BuildRequires:  sonic-frameworks-doctools-devel

BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(KPMcore) >= %{kpmcoremin}

Requires: kf6-filesystem >= 6.31

Provides:       kde-partitionmanager = %{version}-%{release}
Provides:       kde-partitionmanager%{?_isa} = %{version}-%{release}
Obsoletes:      kde-partitionmanager

%description
KDE Partition Manager is a utility program to help you manage the disk devices,
partitions and file systems on your computer. It allows you to easily create, 
copy, move, delete, resize without losing data, backup and restore partitions.

KDE Partition Manager supports a large number of file systems, 
including ext2/3/4, reiserfs, NTFS, FAT16/32, jfs, xfs and more.

Starting from version 1.9.50 KDE Partition Manager has become the GUI part of 
KPMcore (KDE PartitionManager core) which contain the libraries used to 
manipulate filesystems.


%prep
%autosetup -p1 -n %{reponame}-%{version}
sed -i 's/set(KPMCORE_MIN_VERSION.*/set(KPMCORE_MIN_VERSION "25.12")/' CMakeLists.txt


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang partitionmanager --with-kde --with-html

%check
# Validate .desktop file
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*partitionmanager.desktop
# Validate appdata file
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml


%files -f partitionmanager.lang
%license LICENSES/*
%{_kf6_bindir}/partitionmanager
%{_kf6_datadir}/applications/*partitionmanager.desktop
%{_kf6_datadir}/solid/actions/open_in_partitionmanager.desktop
%{_kf6_datadir}/config.kcfg/partitionmanager.kcfg
%{_datadir}/icons/hicolor/*/*/*
%{_kf6_metainfodir}/*partitionmanager.appdata.xml

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
