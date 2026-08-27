# Generated for SonicDE from Fedora's kmenuedit.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-launcher-menu-edit fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-launcher-menu-edit
# Upstream KDE project: kmenuedit
%global oldname kmenuedit

#Name:    kmenuedit
Name:           sonic-launcher-menu-edit
Summary: KDE menu editor
Version:        6.7.4
Release:        3%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  qt6-qtbase-devel

BuildRequires:  desktop-file-utils
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  libappstream-glib

# when split out from kde-workspace-4.11.x
Conflicts:      kde-workspace < 4.11.15-3

Provides:       kmenuedit%{?_isa} = %{version}-%{release}
Obsoletes:      kmenuedit < %{version}-%{release}

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
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kmenuedit.desktop
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
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
