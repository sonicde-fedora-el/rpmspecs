# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdebugsettings
Summary: Configure debug output from Qt6 applications
Version: 26.04.3
Release: 2%{?dist}

License: LGPL-2.0-or-later
URL:     https://apps.kde.org/kdebugsettings/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6WindowSystem)

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
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-2
- SonicDE build for Enterprise Linux 10
