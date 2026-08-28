%global debug_package %{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdenetwork-filesharing
Summary: Network filesharing
Version: 26.04.3
Release: 1%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/network/%{name}
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


# upstream patches

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: gettext
BuildRequires: sonic-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickWidgets)

BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WidgetsAddons)

BuildRequires: cmake(packagekitqt6)
BuildRequires: cmake(QCoro6Core)

# or gets pulled in via PK at runtime
Recommends: samba
Recommends: samba-usershares

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kdenetwork-filesharing.metainfo.xml


%files -f %{name}.lang
%license LICENSES/*
%dir %{_kf6_plugindir}/propertiesdialog/
%{_kf6_plugindir}/propertiesdialog/sambausershareplugin.so
%{_kf6_plugindir}/propertiesdialog/SambaAcl.so
%{_kf6_metainfodir}/org.kde.kdenetwork-filesharing.metainfo.xml
%{_kf6_libexecdir}/kauth/sambausershareplugin_authhelper
%{_kf6_datadir}/dbus-1/system-services/org.kde.filesharing.samba.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.filesharing.samba.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.filesharing.samba.policy


%changelog
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
