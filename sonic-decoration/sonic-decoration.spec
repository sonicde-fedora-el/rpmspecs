# Generated for SonicDE from Fedora's kdecoration.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-decoration fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-decoration
# Upstream KDE project: kdecoration
%global oldname kdecoration

#Name:    kdecoration
Name:           sonic-decoration
Summary: A plugin-based library to create window decorations
Version:        6.8.2
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        3%{?dist}

License: LGPL-3.0-only AND LGPL-2.1-only AND CC0-1.0
#URL:     https://invent.kde.org/plasma/kdecoration
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel >= 6.11
# For AutoReq cmake-filesystem
BuildRequires: cmake
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: make

Requires: kf6-filesystem >= 6.31

Provides:       kdecoration = %{version}-%{release}
Provides:       kdecoration%{?_isa} = %{version}-%{release}
Obsoletes:      kdecoration

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:       kdecoration-devel = %{version}-%{release}
Provides:       kdecoration-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kdecoration-devel

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
# create/own plugin dir
mkdir -p %{buildroot}%{_kf6_qtplugindir}/org.kde.kdecoration2/

%files
%license LICENSES/*.txt
%{_kf6_libdir}/libkdecorations3.so.6
%{_kf6_libdir}/libkdecorations3.so.%{libversion}
%{_kf6_libdir}/libkdecorations3private.so.2
%{_kf6_libdir}/libkdecorations3private.so.%{libversion}
%{_datadir}/locale/*/LC_MESSAGES/kdecoration.mo

%files devel
%{_kf6_libdir}/libkdecorations3.so
%{_kf6_libdir}/libkdecorations3private.so
%{_kf6_libdir}/cmake/KDecoration3/
%{_kf6_includedir}/kdecoration3_version.h
%{_includedir}/KDecoration3

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
