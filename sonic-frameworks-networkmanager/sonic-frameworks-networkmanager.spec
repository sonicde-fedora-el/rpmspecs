# Generated for SonicDE from Fedora's kf6-networkmanager-qt.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-networkmanager fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-networkmanager
# Upstream KDE project: networkmanager-qt
%global oldname kf6-networkmanager-qt

%undefine __cmake_in_source_build

%global framework networkmanager-qt

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-networkmanager
Version:        6.29.0
Release:        3%{?dist}
Summary:        A Tier 1 KDE Frameworks 6 module that wraps NetworkManager DBus API
License:        LGPL-2.0-or-later AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND CC0-1.0
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# KDE Frameworks
BuildRequires:  sonic-frameworks-cmake-modules

# Fedora
Requires:       kf6-filesystem
BuildRequires:  sonic-rpm-macros

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)

# Other
BuildRequires:  pkgconfig(libnm)
Recommends:     NetworkManager

Provides:       kf6-networkmanager-qt%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-networkmanager-qt < %{version}-%{release}

%description
A Tier 1 KDE Frameworks 6 Qt library for NetworkManager.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       pkgconfig(libnm)
Provides:       kf6-networkmanager-qt-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-networkmanager-qt-devel < %{version}-%{release}

%description    devel
Qt libraries and header files for developing applications
that use NetworkManager.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-networkmanager-qt-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-networkmanager-qt-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-networkmanager-qt-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-networkmanager-qt-html < %{version}-%{release}

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
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6NetworkManagerQt.so.6
%{_kf6_libdir}/libKF6NetworkManagerQt.so.%{version}
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/kde-qmlmodule.version
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/libnetworkmanagerqtqml.so
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/networkmanagerqtqml.qmltypes
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/qmldir

%files devel
%{_kf6_includedir}/NetworkManagerQt/
%{_kf6_libdir}/libKF6NetworkManagerQt.so
%{_kf6_libdir}/cmake/KF6NetworkManagerQt/
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
