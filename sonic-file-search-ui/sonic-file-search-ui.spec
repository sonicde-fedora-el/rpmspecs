# Generated for SonicDE from Fedora's plasma-milou.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-file-search-ui fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-file-search-ui
# Upstream KDE project: milou
%global oldname plasma-milou

%define         base_name milou


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-%%{base_name}
Name:           sonic-file-search-ui
Version:        6.7.4
Release:        1%{?dist}
Summary: A dedicated KDE search application built on top of Baloo

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{base_name}.git
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6KirigamiPlatform)

# Qt
BuildRequires:  qt6-qtbase-devel

# Plasma
BuildRequires:  cmake(Plasma)

Requires:       kf6-filesystem

Obsoletes:      kde-plasma-milou < 5.0.0
Provides:       kde-plasma-milou = %{version}-%{release}

Provides:       plasma-milou = %{version}-%{release}
Conflicts:      plasma-milou < %{version}-%{release}

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang milou --with-qt --all-name


%files -f milou.lang
%license LICENSES/*
%{_kf6_qmldir}/org/kde/milou/
%{_kf6_qtplugindir}/plasma/applets/org.kde.milou.so

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
