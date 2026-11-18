# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
Name:          flatpak-kcm
Version: 6.8.3
Release:       3%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later
Summary:       Flatpak Permissions Management KCM
Url:           https://invent.kde.org/plasma/flatpak-kcm

Source0:       https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:       https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Patch0:        flatpak-kcm-qml-link.patch

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: gcc-c++
BuildRequires: sonic-rpm-macros
BuildRequires: desktop-file-utils

BuildRequires: sonic-frameworks-qml-bridge-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: sonic-frameworks-data-models-devel
BuildRequires: sonic-frameworks-settings-utils-devel
BuildRequires: sonic-frameworks-icon-themes-devel

BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires: qt6-qtsvg-devel >= 6.11

BuildRequires: pkgconfig(flatpak)

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/kcm_app-permissions.desktop
%find_lang kcm_app-permissions

%files -f kcm_app-permissions.lang
%license LICENSES/*
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_app-permissions.so
%{_kf6_datadir}/applications/kcm_app-permissions.desktop

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.3-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 6.8.3-1
- 6.8.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-2
- SonicDE build for Enterprise Linux 10

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 6.6.4-1
- 6.6.4
