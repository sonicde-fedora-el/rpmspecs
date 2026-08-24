# Generated for SonicDE from Fedora's kf6-kded.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-daemon fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-daemon
# Upstream KDE project: kded
%global oldname kf6-kded

%global framework kded

#Name:    kf6-%%{framework}
Name:           sonic-daemon
Version:        6.29.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon with extensible daemon for system-level services

License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Service)
BuildRequires:  sonic-rpm-macros

BuildRequires:  qt6-qtbase-devel

BuildRequires:  systemd
Requires:  kf6-filesystem

Provides:       kf6-kded = %{version}-%{release}
Conflicts:      kf6-kded < %{version}-%{release}

%description
KDED stands for KDE Daemon which isn't very descriptive. KDED runs
in the background and performs a number of small tasks. Some of these
tasks are built in, others are started on demand.

Custom KDED modules can be provided by 3rd party frameworks and
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf6-kded-devel = %{version}-%{release}
Conflicts:      kf6-kded-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang kded6 --with-man
# create/own this
mkdir -p %{buildroot}%{_kf6_plugindir}/kded

%post
%systemd_user_post  plasma-kded.service

%preun
%systemd_user_preun plasma-kded.service

%files -f kded6.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_bindir}/kded6
%{_kf6_datadir}/applications/org.kde.kded6.desktop
%{_kf6_datadir}/dbus-1/services/*.service
%{_kf6_mandir}/man8/kded6.8*
%dir %{_kf6_plugindir}/kded/
%{_userunitdir}/plasma-kded6.service

%files devel
%{_kf6_libdir}/cmake/KF6KDED/
%{_kf6_datadir}/dbus-1/interfaces/*.xml

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
