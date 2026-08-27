# Generated for SonicDE from Fedora's kf6-kitemviews.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-data-views fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-data-views
# Upstream KDE project: kitemviews
%global oldname kf6-kitemviews

%global		framework kitemviews

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-data-views
Version:        6.29.0
Release:        3%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with item views
License:	CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:	fdupes
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	sonic-frameworks-cmake-modules >= %{version}
BuildRequires:	sonic-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	pkgconfig(xkbcommon)

Requires:	kf6-filesystem

Provides:       kf6-kitemviews%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kitemviews < %{version}-%{release}

%description
KDE Frameworks 6 Tier 1 addon with item views.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
Provides:       kf6-kitemviews-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kitemviews-devel < %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kitemviews-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kitemviews-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kitemviews-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kitemviews-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kitemviews6_qt
%fdupes LICENSES

%files -f kitemviews6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6ItemViews.so.*

%files devel
%{_kf6_includedir}/KItemViews/
%{_kf6_libdir}/libKF6ItemViews.so
%{_kf6_libdir}/cmake/KF6ItemViews/
%{_kf6_qtplugindir}/designer/kitemviews6widgets.so
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
