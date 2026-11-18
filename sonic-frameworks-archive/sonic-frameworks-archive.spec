# Generated for SonicDE from Fedora's kf6-karchive.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-archive fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-frameworks-archive
# Upstream KDE project: karchive
%global oldname kf6-karchive

%global framework karchive

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-archive
Version:        6.31.0
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        3%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with archive functions
License:        LGPL-2.0-or-later AND BSD-2-Clause
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
Requires: kf6-filesystem >= 6.31
BuildRequires:  sonic-rpm-macros

# KDE Frameworks
BuildRequires:  sonic-frameworks-cmake-modules

# Qt
BuildRequires:  qt6-qtbase-devel >= 6.11

# Compression
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

# Others
BuildRequires:  pkgconfig(openssl)

Provides:       kf6-karchive = %{version}-%{release}
Provides:       kf6-karchive%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-karchive

%description
KDE Frameworks 6 Tier 1 addon with archive functions.

%package        devel
Summary:        Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Provides:       kf6-karchive-devel = %{version}-%{release}
Provides:       kf6-karchive-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-karchive-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-karchive-doc = %{version}-%{release}
Provides:       kf6-karchive-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-karchive-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-karchive-html = %{version}-%{release}
Provides:       kf6-karchive-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-karchive-html

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6
%find_lang_kf6 karchive6_qt
# Seems one of the arches generate an extra file. Neal said to delete it, at least for now
# It is being built on all arches, except s390x and i686.
rm -f %{buildroot}%{_qt6_docdir}/karchive/karchivedirectory-obsolete.html

%files -f karchive6_qt.lang
%doc AUTHORS README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Archive.so.6
%{_kf6_libdir}/libKF6Archive.so.%{libversion}

%files devel
%{_kf6_includedir}/KArchive/
%{_kf6_libdir}/cmake/KF6Archive/
%{_kf6_libdir}/libKF6Archive.so
%{_kf6_libdir}/pkgconfig/*
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
