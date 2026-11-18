# Generated for SonicDE from Fedora's plasma-workspace-wallpapers.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-workspace-wallpapers fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-workspace-wallpapers
# Upstream KDE project: plasma-workspace-wallpapers
%global oldname plasma-workspace-wallpapers


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-workspace-wallpapers
Name:           sonic-workspace-wallpapers
Version:        6.8.2
Release:        3%{?dist}
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
BuildRequires:  qt6-qtbase-devel >= 6.11
Requires:       kde-filesystem

# Elarun moved here
Conflicts:      kde-wallpapers < 15.08.3-10

# when we went noarch
Obsoletes:      sonic-workspace-wallpapers < 5.2.0-2


Provides:       plasma-workspace-wallpapers = %{version}-%{release}
Provides:       plasma-workspace-wallpapers%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-workspace-wallpapers

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
%{_datadir}/wallpapers/*/

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
