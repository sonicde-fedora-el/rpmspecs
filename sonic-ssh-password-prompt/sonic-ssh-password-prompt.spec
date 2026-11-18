# Generated for SonicDE from Fedora's ksshaskpass.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-ssh-password-prompt fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-ssh-password-prompt
# Upstream KDE project: ksshaskpass
%global oldname ksshaskpass


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    ksshaskpass
Name:           sonic-ssh-password-prompt
Version:        6.8.2
Release:        3%{?dist}
Summary: A ssh-add helper that uses kwallet and kpassworddialog

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
#URL:     https://cgit.kde.org/%%{name}.git
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  gettext
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-keyring-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  cmake(Qt6Keychain)

Provides:       ksshaskpass = %{version}-%{release}
Provides:       ksshaskpass%{?_isa} = %{version}-%{release}
Obsoletes:      ksshaskpass

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang ksshaskpass

# Setup environment variables
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/
cat >    %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/ksshaskpass.sh << EOF
SSH_ASKPASS=%{_kf6_bindir}/ksshaskpass
export SSH_ASKPASS
EOF


%files -f ksshaskpass.lang
%doc ChangeLog
%license LICENSES/*
%{_kf6_bindir}/ksshaskpass
%{_kf6_datadir}/applications/org.kde.ksshaskpass.desktop
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/env/ksshaskpass.sh
%{_mandir}/man1/ksshaskpass.1*

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
