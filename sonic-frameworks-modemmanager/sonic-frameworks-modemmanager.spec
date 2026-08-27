# Generated for SonicDE from Fedora's kf6-modemmanager-qt.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-modemmanager fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-modemmanager
# Upstream KDE project: modemmanager-qt
%global oldname kf6-modemmanager-qt

%global framework modemmanager-qt

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-modemmanager
Version:        6.29.0
Release:        3%{?dist}
Summary: A Tier 1 KDE Frameworks module wrapping ModemManager DBus API
License: GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ModemManager-devel >= 1.0.0
BuildRequires:  qt6-qtbase-devel

Requires:       kf6-filesystem

Provides:       kf6-modemmanager-qt%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-modemmanager-qt < %{version}-%{release}

%description
A Qt 6 library for ModemManager.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ModemManager-devel
Requires:       qt6-qtbase-devel
Provides:       kf6-modemmanager-qt-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-modemmanager-qt-devel < %{version}-%{release}

%description    devel
Qt 6 libraries and header files for developing applications
that use ModemManager.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-modemmanager-qt-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-modemmanager-qt-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-modemmanager-qt-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-modemmanager-qt-html < %{version}-%{release}

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
%doc README README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*.categories
%{_kf6_datadir}/qlogging-categories6/*.renamecategories
%{_kf6_libdir}/libKF6ModemManagerQt.so.*

%files devel
%{_kf6_libdir}/libKF6ModemManagerQt.so
%{_kf6_libdir}/cmake/KF6ModemManagerQt/
%{_kf6_includedir}/ModemManagerQt/
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
