# Generated for SonicDE.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-gamma fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-gamma
# Upstream KDE project: kgamma
%global oldname kgamma

#Name:    kgamma
Name:           sonic-gamma
Summary:        X11 display gamma configuration for SonicDE
Version:        6.8.2
Release:        3%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
#URL:     https://invent.kde.org/plasma/%%{oldname}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{oldname}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules

BuildRequires:  qt6-qtbase-devel >= 6.11

BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-settings-utils-devel

BuildRequires:  libX11-devel
BuildRequires:  libXxf86vm-devel

Provides:       kgamma = %{version}-%{release}
Provides:       kgamma%{?_isa} = %{version}-%{release}
Obsoletes:      kgamma
Conflicts:      kgamma

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang kcmkgamma --with-html --all-name


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kcm_kgamma.desktop


%files -f kcmkgamma.lang
%license LICENSES/*
%{_datadir}/kgamma/
%{_datadir}/applications/kcm_kgamma.desktop
%{_qt6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kgamma.so
%{_qt6_plugindir}/plasma/kcminit/kcm_kgamma_init.so

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Wed Nov 11 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-1
- Initial SonicDE package for Enterprise Linux 10, renamed from kgamma
