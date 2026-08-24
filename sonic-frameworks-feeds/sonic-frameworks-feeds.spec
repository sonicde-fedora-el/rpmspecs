# Generated for SonicDE from Fedora's kf6-syndication.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-feeds fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-feeds
# Upstream KDE project: syndication
%global oldname kf6-syndication

%global framework syndication

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-feeds
Version:        6.29.0
Release:        1%{?dist}
Summary: The Syndication Library

# Qt-Commercial-exception-1.0 is also found in the LICENSES folder, but is unused except for tests which we don't use anyway
License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(KF6KIO)
Requires:  kf6-filesystem

Provides:       kf6-syndication = %{version}-%{release}
Conflicts:      kf6-syndication < %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       kf6-syndication-devel = %{version}-%{release}
Conflicts:      kf6-syndication-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-syndication-doc = %{version}-%{release}
Conflicts:      kf6-syndication-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-syndication-html = %{version}-%{release}
Conflicts:      kf6-syndication-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Syndication.so.*

%files devel
%{_kf6_includedir}/Syndication/
%{_kf6_libdir}/cmake/KF6Syndication/
%{_kf6_libdir}/libKF6Syndication.so
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
