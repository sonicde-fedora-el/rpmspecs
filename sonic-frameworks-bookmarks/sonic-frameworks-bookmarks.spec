# Generated for SonicDE from Fedora's kf6-kbookmarks.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-bookmarks fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-bookmarks
# Upstream KDE project: kbookmarks
%global oldname kf6-kbookmarks

%global framework kbookmarks

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-bookmarks
Version:        6.29.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for bookmarks manipulation
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)

Requires:  kf6-filesystem

Provides:       kf6-kbookmarks = %{version}-%{release}
Conflicts:      kf6-kbookmarks < %{version}-%{release}

%description
KBookmarks lets you access and manipulate bookmarks stored using the
XBEL format.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6WidgetsAddons)
Provides:       kf6-kbookmarks-devel = %{version}-%{release}
Conflicts:      kf6-kbookmarks-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kbookmarks-doc = %{version}-%{release}
Conflicts:      kf6-kbookmarks-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kbookmarks-html = %{version}-%{release}
Conflicts:      kf6-kbookmarks-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kbookmarks6_qt

%files -f kbookmarks6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Bookmarks.so.*
%{_kf6_libdir}/libKF6BookmarksWidgets.so.6
%{_kf6_libdir}/libKF6BookmarksWidgets.so.%{version}
%{_kf6_libdir}/libKF6BookmarksWidgets.so.%{version}
%{_kf6_datadir}/qlogging-categories6/%{framework}widgets.categories

%files devel
%{_kf6_includedir}/KBookmarks/
%{_kf6_libdir}/libKF6Bookmarks.so
%{_kf6_libdir}/cmake/KF6Bookmarks/
%{_kf6_includedir}/KBookmarksWidgets/
%{_kf6_libdir}/libKF6BookmarksWidgets.so
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
