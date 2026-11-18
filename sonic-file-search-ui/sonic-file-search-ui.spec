# Generated for SonicDE from Fedora's plasma-milou.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-file-search-ui fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-file-search-ui
# Upstream KDE project: milou
%global oldname plasma-milou

%define         base_name milou


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-%%{base_name}
Name:           sonic-file-search-ui
Version:        6.8.2
Release:        4%{?dist}
Summary: A dedicated KDE search application built on top of Baloo

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{base_name}.git
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz.sig

BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  sonic-frameworks-file-search-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-data-models-devel
BuildRequires:  sonic-frameworks-runner-devel
BuildRequires:  sonic-frameworks-svg-devel
BuildRequires:  sonic-frameworks-quick-ui-devel

# Qt
BuildRequires:  qt6-qtbase-devel >= 6.11
# Plasma
BuildRequires:  sonic-interface-libraries-devel

Requires: kf6-filesystem >= 6.31

Obsoletes:      kde-plasma-milou
Provides:       kde-plasma-milou = %{version}-%{release}

Provides:       plasma-milou = %{version}-%{release}
Provides:       plasma-milou%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-milou

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang milou --with-qt --all-name


%files -f milou.lang
%license LICENSES/*
%{_kf6_qmldir}/org/kde/milou/
%{_kf6_qtplugindir}/plasma/applets/org.kde.milou.so

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-4
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Pin Plasma cmake deps to SonicDE providers (Fedora libplasma 6.8.3 outranks ours)
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
