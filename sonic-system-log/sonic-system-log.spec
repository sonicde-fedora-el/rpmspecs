# Generated for SonicDE from Fedora's ksystemlog.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-system-log fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-system-log
# Upstream KDE project: ksystemlog
%global oldname ksystemlog


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    ksystemlog
Name:           sonic-system-log
Summary: System Log Viewer for KDE
Version:        26.04.3
Release:        1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
#URL:     https://apps.kde.org/ksystemlog/
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/release-service/%%{version}/src/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

## upstreamable patches

## downstream patches
# fix ksystemlog to find log files in fedora locations
Patch1: ksystemlog-21.12.2-fedora.patch

BuildRequires: desktop-file-utils
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6Network)

BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Crash)

BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(audit)

Provides:       ksystemlog = %{version}-%{release}
Conflicts:      ksystemlog < %{version}-%{release}

%description
This program is developed for beginner users, who don't know how to find
information about their Linux system, and don't know where log files are.

It is also of course designed for advanced users, who quickly want to understand
problems of their machine with a more powerful and graphical tool than tail -f
and less commands.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{oldname} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{oldname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.ksystemlog.appdata.xml


%files -f %{oldname}.lang
%license LICENSES
%{_kf6_bindir}/ksystemlog
%{_kf6_datadir}/applications/org.kde.ksystemlog.desktop
%{_kf6_datadir}/qlogging-categories6/ksystemlog.categories
%{_kf6_metainfodir}/org.kde.ksystemlog.appdata.xml

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
