# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:          flatpak-kcm
Version:       6.7.4
Release:       2%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later
Summary:       Flatpak Permissions Management KCM
Url:           https://invent.kde.org/plasma/flatpak-kcm

Source0:       https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:       https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: gcc-c++
BuildRequires: sonic-rpm-macros
BuildRequires: desktop-file-utils

BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(Qt6Svg)

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
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-2
- SonicDE build for Enterprise Linux 10

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 6.6.4-1
- 6.6.4
