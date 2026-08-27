# Generated for SonicDE from Fedora's kf6-kguiaddons.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-gui-addons fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-gui-addons
# Upstream KDE project: kguiaddons
%global oldname kf6-kguiaddons

%global 	framework kguiaddons

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-gui-addons
Version:        6.29.0
Release:        3%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtGui

License:	BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  pkgconfig(wayland-protocols)

BuildRequires:  cmake(Qt6WaylandClient)

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:       kf6-filesystem

Provides:       kf6-kguiaddons%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kguiaddons < %{version}-%{release}

%description
%{summary}.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
Provides:       python3-kf6-kguiaddons = %{version}-%{release}

%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qtbase-devel

Provides:       kf6-kguiaddons-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kguiaddons-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kguiaddons-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kguiaddons-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kguiaddons-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kguiaddons-html < %{version}-%{release}

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
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kde-geo-uri-handler
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6GuiAddons.so.*
%{_kf6_datadir}/applications/*-handler.desktop
%{_kf6_qmldir}/org/kde/guiaddons/

%files -n python3-%{name}
%{python3_sitearch}/KGuiAddons.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KGuiAddons/
%{_kf6_libdir}/libKF6GuiAddons.so
%{_kf6_libdir}/cmake/KF6GuiAddons/
%{_kf6_libdir}/pkgconfig/KF6GuiAddons.pc
%{_libdir}/qt6/metatypes/qt6kf6guiaddons*.json
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
