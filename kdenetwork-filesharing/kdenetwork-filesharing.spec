%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdenetwork-filesharing
Summary: Network filesharing
Version: 26.08.3
Release: 3%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/network/%{name}
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


# upstream patches

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: gettext
BuildRequires: sonic-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qtdeclarative-devel >= 6.11

BuildRequires: sonic-frameworks-auth-devel
BuildRequires: sonic-frameworks-autocomplete-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-widgets-addons-devel

BuildRequires: packagekit-qt6-devel
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
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Pin cmake() BuildRequires to SonicDE package names so the
  alma+epel-10 solver cannot pick EPEL's Qt 6.10-linked providers
* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
