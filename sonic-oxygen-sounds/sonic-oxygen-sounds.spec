# Generated for SonicDE from Fedora's oxygen-sounds.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-oxygen-sounds fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-oxygen-sounds
# Upstream KDE project: oxygen-sounds
%global oldname oxygen-sounds


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:           oxygen-sounds
Name:           sonic-oxygen-sounds
Version:        6.7.4
Release:        3%{?dist}
Summary:        The Oxygen Sound Theme

License:        LGPL-3.0-or-later AND CC0-1.0 AND CC-BY-3.0 AND BSD-2-Clause
#URL:            https://invent.kde.org/plasma/oxygen-sounds
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

Provides:       oxygen-sound-theme = %{version}-%{release}
Obsoletes:      oxygen-sound-theme <= 5.24.50

BuildRequires:  cmake
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel

BuildArch:      noarch

Provides:       oxygen-sounds%{?_isa} = %{version}-%{release}
Obsoletes:      oxygen-sounds < %{version}-%{release}

%description
%{summary}.


%prep
%autosetup -n %{reponame}-%{version}

%build
%{cmake_kf6} -DBUILD_WITH_QT6=ON
%{cmake_build}

%install
%{cmake_install}


%files
%license LICENSES/*.txt
%{_kf6_datadir}/sounds/Oxygen-*
%{_kf6_datadir}/sounds/oxygen/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
