# Generated for SonicDE from Fedora's kdecoration.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-decoration fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-decoration
# Upstream KDE project: kdecoration
%global oldname kdecoration

#Name:    kdecoration
Name:           sonic-decoration
Summary: A plugin-based library to create window decorations
Version:        6.7.4
Release:        3%{?dist}

License: LGPL-3.0-only AND LGPL-2.1-only AND CC0-1.0
#URL:     https://invent.kde.org/plasma/kdecoration
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel

# For AutoReq cmake-filesystem
BuildRequires: cmake
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: make

Requires:       kf6-filesystem

Provides:       kdecoration%{?_isa} = %{version}-%{release}
Obsoletes:      kdecoration < %{version}-%{release}

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:       kdecoration-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kdecoration-devel < %{version}-%{release}

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
%{_kf6_libdir}/libkdecorations3.so.%{version}
%{_kf6_libdir}/libkdecorations3private.so.2
%{_kf6_libdir}/libkdecorations3private.so.%{version}
%{_datadir}/locale/*/LC_MESSAGES/kdecoration.mo

%files devel
%{_kf6_libdir}/libkdecorations3.so
%{_kf6_libdir}/libkdecorations3private.so
%{_kf6_libdir}/cmake/KDecoration3/
%{_kf6_includedir}/kdecoration3_version.h
%{_includedir}/KDecoration3

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
