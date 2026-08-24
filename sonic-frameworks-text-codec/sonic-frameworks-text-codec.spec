# Generated for SonicDE from Fedora's kf6-kcodecs.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-text-codec fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-text-codec
# Upstream KDE project: kcodecs
%global oldname kf6-kcodecs

%global		framework kcodecs

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-text-codec
Version:        6.29.0
Release:        1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with string manipulation methods
License:	BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND MPL-1.1
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:	fdupes
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gperf
BuildRequires:	sonic-frameworks-cmake-modules >= %{version}
BuildRequires:	sonic-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel

Requires:	kf6-filesystem

Provides:       kf6-kcodecs = %{version}-%{release}
Conflicts:      kf6-kcodecs < %{version}-%{release}

%description
KDE Frameworks 6 Tier 1 addon with string manipulation methods.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
Provides:       kf6-kcodecs-devel = %{version}-%{release}
Conflicts:      kf6-kcodecs-devel < %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcodecs-doc = %{version}-%{release}
Conflicts:      kf6-kcodecs-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcodecs-html = %{version}-%{release}
Conflicts:      kf6-kcodecs-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kcodecs6_qt
%fdupes LICENSES

%files -f kcodecs6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Codecs.so.*

%files devel
%{_kf6_includedir}/KCodecs/
%{_kf6_libdir}/libKF6Codecs.so
%{_kf6_libdir}/cmake/KF6Codecs/
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
