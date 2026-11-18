# Generated for SonicDE from Fedora's kf6-kcoreaddons.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-core-addons fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-frameworks-core-addons
# Upstream KDE project: kcoreaddons
%global oldname kf6-kcoreaddons

%global		framework kcoreaddons

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-core-addons

# pyside6 python bindings are optional (EPEL pyside6 currently uninstallable on EL10)
%bcond_with bindings
Version:        6.31.0
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
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qttools-devel >= 6.11
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(mount)

BuildRequires:  python3-devel
%if %{with bindings}
# required for pyside6 python bindings
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
%if %{with bindings}
BuildRequires:  cmake(PySide6)
%endif
%endif

Requires: kf6-filesystem >= 6.31

Provides:       kf6-kcoreaddons = %{version}-%{release}
Provides:       kf6-kcoreaddons%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcoreaddons

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%if %{with bindings}
%package -n python3-%{name}
Summary:    Qt for Python bindings for %{name}
Provides:       python3-kf6-kcoreaddons = %{version}-%{release}

%description -n python3-%{name}
The package contains the pyside6 bindings library for %{name}
%endif

%package    devel
Summary:    Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Provides:       kf6-kcoreaddons-devel = %{version}-%{release}
Provides:       kf6-kcoreaddons-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcoreaddons-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch

Provides:       kf6-kcoreaddons-doc = %{version}-%{release}
Provides:       kf6-kcoreaddons-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcoreaddons-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcoreaddons-html = %{version}-%{release}
Provides:       kf6-kcoreaddons-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcoreaddons-html

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 %{?with_bindings:-DBUILD_PYTHON_BINDINGS=ON}%{!?with_bindings:-DBUILD_PYTHON_BINDINGS=OFF}
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

%if %{with bindings}
%files -n python3-%{name}
%{python3_sitearch}/KCoreAddons.cpython-%{python3_version_nodots}*.so

%endif
%files devel
%{_kf6_includedir}/KCoreAddons/
%if %{with bindings}
%dir %{_includedir}/PySide6/KCoreAddons/
%{_includedir}/PySide6/KCoreAddons/kcoreaddons_python.h
%dir %{_kf6_datadir}/PySide6/typesystems/
%{_kf6_datadir}/PySide6/typesystems/typesystem_kcoreaddons.xml
%endif
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
