# Generated for SonicDE from Fedora's kf6-kwidgetsaddons.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-widgets-addons fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-widgets-addons
# Upstream KDE project: kwidgetsaddons
%global oldname kf6-kwidgetsaddons

%global		framework kwidgetsaddons

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-widgets-addons
Version:        6.29.0
Release:        3%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtWidgets
License:	BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	sonic-frameworks-cmake-modules >= %{majmin_ver_kf6}
BuildRequires:	sonic-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	qt6-qttools-static
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	fdupes

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:	kf6-filesystem

Provides:       kf6-kwidgetsaddons%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kwidgetsaddons < %{version}-%{release}

%description
KDE Frameworks 6 Tier 1 addon with various classes on top of QtWidgets.

%package	-n python3-%{name}
Summary:        Qt for Python bindings for %{name}
Provides:       python3-kf6-kwidgetsaddons = %{version}-%{release}

%description	-n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
Provides:       kf6-kwidgetsaddons-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kwidgetsaddons-devel < %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kwidgetsaddons-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kwidgetsaddons-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kwidgetsaddons-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kwidgetsaddons-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kwidgetsaddons6_qt
%fdupes %{buildroot}/%{_kf6_includedir}/KWidgetsAddons/
%fdupes LICENSES

%files -f kwidgetsaddons6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6WidgetsAddons.so.*
%{_kf6_datadir}/qlogging-categories6/*categories

%files -n python3-%{name}
%{python3_sitearch}/KWidgetsAddons.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KWidgetsAddons/
%{_kf6_libdir}/libKF6WidgetsAddons.so
%{_kf6_libdir}/cmake/KF6WidgetsAddons/
%{_kf6_qtplugindir}/designer/kwidgetsaddons6widgets.so
%{_kf6_datadir}/PySide6/typesystems/typesystem_kwidgetsaddons.xml
%{_includedir}/PySide6/KWidgetsAddons/
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
