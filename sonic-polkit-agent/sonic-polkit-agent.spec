# Generated for SonicDE from Fedora's polkit-kde.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-polkit-agent fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-polkit-agent
# Upstream KDE project: polkit-kde-agent-1
%global oldname polkit-kde

%global         base_name polkit-kde-agent-1

#Name:    polkit-kde
Name:           sonic-polkit-agent
Summary: PolicyKit integration for KDE Desktop
Version:        6.7.4
Release:        1%{?dist}

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
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Declarative)

BuildRequires:  polkit-qt6-1-devel

Provides: PolicyKit-authentication-agent = %{version}-%{release}
Provides: polkit-kde-1 = %{version}-%{release}
Provides: polkit-kde-agent-1 = %{version}-%{release}

Obsoletes: PolicyKit-kde < 4.5

# Add explicit dependency on polkit, since polkit-libs were split out
Requires: polkit

Provides:       polkit-kde = %{version}-%{release}
Conflicts:      polkit-kde < %{version}-%{release}

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
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
