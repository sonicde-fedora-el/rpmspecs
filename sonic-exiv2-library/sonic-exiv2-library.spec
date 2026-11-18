# Generated for SonicDE from Fedora's libkexiv2.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-exiv2-library fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_qt6_version 6.11.3
%global reponame sonic-exiv2-library
# Upstream KDE project: libkexiv2
%global oldname libkexiv2

#Name:    libkexiv2
Name:           sonic-exiv2-library
Summary: A wrapper around Exiv2 library
Version:        26.08.3
Release:        3%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
#URL:     https://invent.kde.org/graphics/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: http://download.kde.org/%%{stable_kf6}/release-service/%%{version}/src/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

## upstream patches (master branch)

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qt5compat-devel >= 6.11
BuildRequires: pkgconfig(exiv2)


%global _description %{expand:
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures metadata
as EXIF IPTC and XMP.}

Provides:       libkexiv2 = %{version}-%{release}
Provides:       libkexiv2%{?_isa} = %{version}-%{release}
Obsoletes:      libkexiv2

%description %{_description}

%package qt6
Summary: Qt6 version of %{name}
Provides:       libkexiv2-qt6 = %{version}-%{release}
Provides:       libkexiv2-qt6%{?_isa} = %{version}-%{release}
Obsoletes:      libkexiv2-qt6

%description qt6
%{_description}

%package qt6-devel
Summary:  Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Provides:       libkexiv2-qt6-devel = %{version}-%{release}
Provides:       libkexiv2-qt6-devel%{?_isa} = %{version}-%{release}
Obsoletes:      libkexiv2-qt6-devel

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
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
