# Generated for SonicDE from Fedora's libkexiv2.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-exiv2-library fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-exiv2-library
# Upstream KDE project: libkexiv2
%global oldname libkexiv2

#Name:    libkexiv2
Name:           sonic-exiv2-library
Summary: A wrapper around Exiv2 library
Version:        26.04.3
Release:        1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
#URL:     https://invent.kde.org/graphics/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: http://download.kde.org/%%{stable_kf6}/release-service/%%{version}/src/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

## upstream patches (master branch)

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: pkgconfig(exiv2)


%global _description %{expand:
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures metadata
as EXIF IPTC and XMP.}

Provides:       libkexiv2 = %{version}-%{release}
Conflicts:      libkexiv2 < %{version}-%{release}

%description %{_description}

%package qt6
Summary: Qt6 version of %{name}
Provides:       libkexiv2-qt6 = %{version}-%{release}
Conflicts:      libkexiv2-qt6 < %{version}-%{release}

%description qt6
%{_description}

%package qt6-devel
Summary:  Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Gui)
Provides:       libkexiv2-qt6-devel = %{version}-%{release}
Conflicts:      libkexiv2-qt6-devel < %{version}-%{release}

%description qt6-devel
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install


%files qt6
%doc AUTHORS README
%license LICENSES/*
%{_datadir}/qlogging-categories6/*%{oldname}.*
%{_libdir}/libKExiv2Qt6.so.0
%{_libdir}/libKExiv2Qt6.so.5.1.0

%files qt6-devel
%{_libdir}/libKExiv2Qt6.so
%{_includedir}/KExiv2Qt6/
%{_libdir}/cmake/KExiv2Qt6/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
