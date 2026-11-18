# Generated for SonicDE from Fedora's polkit-kde.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-polkit-agent fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-polkit-agent
# Upstream KDE project: polkit-kde-agent-1
%global oldname polkit-kde

%global         base_name polkit-kde-agent-1

#Name:    polkit-kde
Name:           sonic-polkit-agent
Summary: PolicyKit integration for KDE Desktop
Version:        6.8.2
Release:        3%{?dist}

License: GPL-2.0-or-later AND CC0-1.0
#URL:     https://invent.kde.org/plasma/%%{base_name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz.sig


## upstreamable patches


BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel

BuildRequires:  polkit-qt6-1-devel

Provides: PolicyKit-authentication-agent = %{version}-%{release}
Provides: polkit-kde-1 = %{version}-%{release}
Provides: polkit-kde-1%{?_isa} = %{version}-%{release}
Provides: polkit-kde-agent-1 = %{version}-%{release}
Provides: polkit-kde-agent-1%{?_isa} = %{version}-%{release}
Obsoletes: PolicyKit-kde < 4.5

# Add explicit dependency on polkit, since polkit-libs were split out
Requires: polkit

Provides:       polkit-kde = %{version}-%{release}
Provides:       polkit-kde%{?_isa} = %{version}-%{release}
Obsoletes:      polkit-kde

%description
Provides Policy Kit Authentication Agent that nicely fits to KDE.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 \
  -DKDE_INSTALL_LIBEXECDIR:PATH=%{_kf6_libexecdir}

%cmake_build

%install
%cmake_install

%find_lang polkit-kde-authentication-agent-1


%files -f polkit-kde-authentication-agent-1.lang
%license LICENSES/*
%{_kf6_libexecdir}/polkit-kde-authentication-agent-1
%{_sysconfdir}/xdg/autostart/polkit-kde-authentication-agent-1.desktop
%{_kf6_datadir}/knotifications6/polkit-kde-authentication-agent-1.notifyrc
%{_kf6_datadir}/applications/org.kde.polkit-kde-authentication-agent-1.desktop
%{_userunitdir}/plasma-polkit-agent.service

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
