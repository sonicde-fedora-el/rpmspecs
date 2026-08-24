# Generated for SonicDE from Fedora's plasma-workspace-wallpapers.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-workspace-wallpapers fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-workspace-wallpapers
# Upstream KDE project: plasma-workspace-wallpapers
%global oldname plasma-workspace-wallpapers


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-workspace-wallpapers
Name:           sonic-workspace-wallpapers
Version:        6.7.4.1
Release:        1%{?dist}
Summary: Additional wallpapers for Plasma workspace
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License: LGPL-3.0-only
#URL:     https://cgit.kde.org/%%{name}.git
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig
BuildArch: noarch

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel

Requires:       kde-filesystem

# Elarun moved here
Conflicts:      kde-wallpapers < 15.08.3-10

# when we went noarch
Obsoletes:      sonic-workspace-wallpapers < 5.2.0-2


Provides:       plasma-workspace-wallpapers = %{version}-%{release}
Conflicts:      plasma-workspace-wallpapers < %{version}-%{release}

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%cmake_install


%files
%license COPYING.LGPL3
%{_datadir}/wallpapers/Altai/
%{_datadir}/wallpapers/Autumn/
%{_datadir}/wallpapers/BytheWater/
%{_datadir}/wallpapers/Canopee/
%{_datadir}/wallpapers/Cascade/
%{_datadir}/wallpapers/Cluster/
%{_datadir}/wallpapers/ColdRipple/
%{_datadir}/wallpapers/ColorfulCups/
%{_datadir}/wallpapers/DarkestHour/
%{_datadir}/wallpapers/Elarun/
%{_datadir}/wallpapers/EveningGlow/
%{_datadir}/wallpapers/FallenLeaf/
%{_datadir}/wallpapers/FlyingKonqui/
%{_datadir}/wallpapers/Flow/
%{_datadir}/wallpapers/Grey/
%{_datadir}/wallpapers/Honeywave/
%{_datadir}/wallpapers/IceCold/
%{_datadir}/wallpapers/Kay/
%{_datadir}/wallpapers/Kite/
%{_datadir}/wallpapers/Kokkini/
%{_datadir}/wallpapers/MilkyWay/
%{_datadir}/wallpapers/Mountain/
%{_datadir}/wallpapers/Nexus/
%{_datadir}/wallpapers/Nuvole/
%{_datadir}/wallpapers/OneStandsOut/
%{_datadir}/wallpapers/Opal/
%{_datadir}/wallpapers/PastelHills/
%{_datadir}/wallpapers/Patak/
%{_datadir}/wallpapers/Path/
%{_datadir}/wallpapers/SafeLanding/
%{_datadir}/wallpapers/ScarletTree/
%{_datadir}/wallpapers/Shell/
%{_datadir}/wallpapers/summer_1am/
%{_datadir}/wallpapers/Volna/
%{_datadir}/wallpapers/Coast/
%{_datadir}/wallpapers/Orionids/
%{_datadir}/wallpapers/Sub-Arctic/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
