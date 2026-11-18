# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
Name:    kdebugsettings
Summary: Configure debug output from Qt6 applications
Version: 26.08.3
Release: 3%{?dist}

License: LGPL-2.0-or-later
URL:     https://apps.kde.org/kdebugsettings/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  qt6-qtbase-devel >= 6.11

BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-autocomplete-devel
BuildRequires:  sonic-frameworks-xml-gui-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-windowsystem-devel

%description
An application to enable/disable qCDebug


%prep
%autosetup


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man


%check
# desktop-file-validate and appstream checks are skipped on RHEL


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/kdebugsettings
%{_kf6_datadir}/applications/org.kde.kdebugsettings.desktop
%{_kf6_datadir}/kdebugsettings/
%{_kf6_metainfodir}/org.kde.kdebugsettings.*.xml
%{_kf6_datadir}/qlogging-categories6/kde*
%{_kf6_libdir}/libkdebugsettings.so.*
%{_kf6_libdir}/libkdebugsettingscore.so.*

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-2
- SonicDE build for Enterprise Linux 10
