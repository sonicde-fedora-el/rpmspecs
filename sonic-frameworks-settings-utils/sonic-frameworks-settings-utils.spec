# Generated for SonicDE from Fedora's kf6-kcmutils.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-settings-utils fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-settings-utils
# Upstream KDE project: kcmutils
%global oldname kf6-kcmutils

%global framework kcmutils

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-settings-utils
Version:        6.29.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon with extra API to write KConfigModules

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

Requires: kf6-filesystem
Requires: qt6qml(org.kde.kirigami)

Provides:       kf6-kcmutils = %{version}-%{release}
Conflicts:      kf6-kcmutils < %{version}-%{release}

%description
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6ConfigWidgets)
Requires:       cmake(KF6Service)
Requires:       cmake(Qt6Qml)
Provides:       kf6-kcmutils-devel = %{version}-%{release}
Conflicts:      kf6-kcmutils-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcmutils-doc = %{version}-%{release}
Conflicts:      kf6-kcmutils-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcmutils-html = %{version}-%{release}
Conflicts:      kf6-kcmutils-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --all-name
# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/kcms

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kcmshell6
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6KCMUtils.so.*
%{_kf6_libdir}/libKF6KCMUtilsCore.so.*
%{_kf6_qmldir}/org/kde/kcmutils/
%{_kf6_qtplugindir}/kcms/
%{_libdir}/libKF6KCMUtilsQuick.so.6
%{_libdir}/libKF6KCMUtilsQuick.so.%{version}

%files devel
%{_kf6_includedir}/KCMUtils/
%{_kf6_includedir}/KCMUtilsCore/
%{_kf6_libdir}/libKF6KCMUtils.so
%{_libdir}/libKF6KCMUtilsQuick.so
%{_kf6_libdir}/libKF6KCMUtilsCore.so
%{_kf6_libdir}/cmake/KF6KCMUtils/
%{_kf6_libexecdir}/kcmdesktopfilegenerator
%{_kf6_includedir}/KCMUtilsQuick
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
