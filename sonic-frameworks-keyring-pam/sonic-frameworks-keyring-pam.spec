# Generated for SonicDE from Fedora's pam-kwallet.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-keyring-pam fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global reponame sonic-frameworks-keyring-pam
# Upstream KDE project: kwallet-pam
%global oldname pam-kwallet


%global  base_name kwallet-pam


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    pam-kwallet
Name:           sonic-frameworks-keyring-pam
Summary: PAM module for KWallet
Version:        6.8.2
Release:        2%{?dist}
License: LGPL-2.0-or-later
#URL:     https://invent.kde.org/plasma/%%{base_name}.git
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz.sig

## upstream patches

## upstreamable patches

Provides: %{base_name} = %{version}-%{release}

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: systemd-rpm-macros
BuildRequires: libgcrypt-devel >= 1.5.0
BuildRequires: pam-devel
BuildRequires: sonic-frameworks-keyring-devel
BuildRequires: socat

# https://bugzilla.redhat.com/show_bug.cgi?id=1155873
Requires: socat
# pam module makes little sense without the actually kwallet service
Requires: sonic-frameworks-keyring

Provides:       pam-kwallet = %{version}-%{release}
Provides:       pam-kwallet%{?_isa} = %{version}-%{release}
Obsoletes:      pam-kwallet

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%{_sysconfdir}/xdg/autostart/pam_kwallet_init.desktop
%{_userunitdir}/plasma-kwallet-pam.service
%{_libexecdir}/pam_kwallet_init
%{_libdir}/security/pam_kwallet5.so

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
