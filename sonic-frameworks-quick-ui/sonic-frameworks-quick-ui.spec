# Generated for SonicDE from Fedora's kf6-kirigami.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-quick-ui fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-quick-ui
# Upstream KDE project: kirigami
%global oldname kf6-kirigami

%global framework kirigami

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-quick-ui
Version:        6.29.0.2
Release:        1%{?dist}
Summary:        QtQuick plugins to build user interfaces based on the KDE UX guidelines
License:        BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

# -- UPSTREAM --

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  make
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6ShaderTools)

# Renamed from kf6-kirigami2
Obsoletes:      kf6-kirigami2 < 5.246.0
Provides:       kf6-kirigami2 = %{version}-%{release}
Provides:       kf6-kirigami2%{?_isa} = %{version}-%{release}

Provides:       kf6-kirigami = %{version}-%{release}
Conflicts:      kf6-kirigami < %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Obsoletes:      kf6-kirigami2-devel < 5.246.0
Provides:       kf6-kirigami2-devel = %{version}-%{release}
Provides:       kf6-kirigami2-devel%{?_isa} = %{version}-%{release}
Provides:       kf6-kirigami-devel = %{version}-%{release}
Conflicts:      kf6-kirigami-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kirigami-doc = %{version}-%{release}
Conflicts:      kf6-kirigami-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kirigami-html = %{version}-%{release}
Conflicts:      kf6-kirigami-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6
%find_lang_kf6 libkirigami6_qt
%find_lang_kf6 libkirigami2plugin_qt
cat libkirigami6_qt.lang libkirigami2plugin_qt.lang > all.lang

%files -f all.lang
%doc README.md
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%license LICENSES/*.txt
%{_kf6_qmldir}/org/kde/kirigami
%{_datadir}/qlogging-categories6/kirigami.categories
%{_kf6_libdir}/libKirigami.so.6
%{_kf6_libdir}/libKirigami.so.6.*
%{_kf6_libdir}/libKirigamiDelegates.so.6
%{_kf6_libdir}/libKirigamiDelegates.so.6.*
%{_kf6_libdir}/libKirigamiDialogs.so.6
%{_kf6_libdir}/libKirigamiDialogs.so.6.*
%{_kf6_libdir}/libKirigamiLayouts.so.6
%{_kf6_libdir}/libKirigamiLayouts.so.6.*
%{_kf6_libdir}/libKirigamiLayoutsPrivate.so.6
%{_kf6_libdir}/libKirigamiLayoutsPrivate.so.6.*
%{_kf6_libdir}/libKirigamiPlatform.so.6
%{_kf6_libdir}/libKirigamiPlatform.so.6.*
%{_kf6_libdir}/libKirigamiPrimitives.so.6
%{_kf6_libdir}/libKirigamiPrimitives.so.6.*
%{_kf6_libdir}/libKirigamiPrivate.so.6
%{_kf6_libdir}/libKirigamiPrivate.so.6.*
%{_kf6_libdir}/libKirigamiPolyfill.so.6
%{_kf6_libdir}/libKirigamiPolyfill.so.6.*
%{_kf6_libdir}/libKirigamiTemplates.so.6
%{_kf6_libdir}/libKirigamiTemplates.so.6.*
%{_kf6_libdir}/libKirigamiControls.so.6
%{_kf6_libdir}/libKirigamiControls.so.6.*
%{_kf6_libdir}/libKirigamiForms*.so.6
%{_kf6_libdir}/libKirigamiForms*.so.6.*

%files devel
%dir %{_kf6_datadir}/kdevappwizard/
%dir %{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_datadir}/kdevappwizard/templates/kirigami6.tar.bz2
%{_kf6_includedir}/Kirigami/
%{_kf6_libdir}/cmake/KF6Kirigami{,2}/
%{_kf6_libdir}/cmake/KF6KirigamiPlatform/
%{_kf6_libdir}/libKirigami.so
%{_kf6_libdir}/libKirigamiDelegates.so
%{_kf6_libdir}/libKirigamiDialogs.so
%{_kf6_libdir}/libKirigamiLayouts.so
%{_kf6_libdir}/libKirigamiLayoutsPrivate.so
%{_kf6_libdir}/libKirigamiPlatform.so
%{_kf6_libdir}/libKirigamiPrimitives.so
%{_kf6_libdir}/libKirigamiPrivate.so
%{_kf6_libdir}/libKirigamiPolyfill.so
%{_kf6_libdir}/libKirigamiTemplates.so
%{_kf6_libdir}/libKirigamiControls.so
%{_kf6_libdir}/libKirigamiForms.so
%{_kf6_libdir}/libKirigamiForms*.so
%{_libdir}/qt6/metatypes/qt6kirigamiplatform*.json
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
