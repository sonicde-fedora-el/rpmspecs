# Generated for SonicDE from Fedora's kf6-kcoreaddons.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-core-addons fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-core-addons
# Upstream KDE project: kcoreaddons
%global oldname kf6-kcoreaddons

%global		framework kcoreaddons

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-core-addons
Version:        6.29.0
Release:        3%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtCore
License:	BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND MPL-1.1 AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-2.1-only WITH Qt-LGPL-exception-1.1
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6DBusTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlTools)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(mount)

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:       kf6-filesystem

Provides:       kf6-kcoreaddons%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcoreaddons < %{version}-%{release}

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package -n python3-%{name}
Summary:    Qt for Python bindings for %{name}
Provides:       python3-kf6-kcoreaddons = %{version}-%{release}

%description -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package    devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   qt6-qtbase-devel
Provides:       kf6-kcoreaddons-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcoreaddons-devel < %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch

Provides:       kf6-kcoreaddons-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcoreaddons-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcoreaddons-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcoreaddons-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kcoreaddons6_qt
%find_lang_kf6 kde6_xml_mimetypes
cat *.lang > all.lang

%files -f all.lang
%doc README.md
%{_kf6_datadir}/mime/packages/kde6.xml
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6CoreAddons.so.*
%{_kf6_libdir}/qt6/qml/org/kde/coreaddons/libkcoreaddonsplugin.so
%{_kf6_libdir}/qt6/qml/org/kde/coreaddons/qmldir
%{_datadir}/kf6/jsonschema/kpluginmetadata.schema.json
%{_libdir}/qt6/qml/org/kde/coreaddons/kcoreaddonsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/coreaddons/kde-qmlmodule.version

%files -n python3-%{name}
%{python3_sitearch}/KCoreAddons.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KCoreAddons/
%dir %{_includedir}/PySide6/KCoreAddons/
%{_includedir}/PySide6/KCoreAddons/kcoreaddons_python.h
%dir %{_kf6_datadir}/PySide6/typesystems/
%{_kf6_datadir}/PySide6/typesystems/typesystem_kcoreaddons.xml
%{_kf6_libdir}/cmake/KF6CoreAddons/
%{_kf6_libdir}/pkgconfig/KF6CoreAddons.pc
%{_kf6_libdir}/libKF6CoreAddons.so
%{_libdir}/qt6/metatypes/qt6kf6coreaddons*
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
