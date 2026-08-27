# Generated for SonicDE from Fedora's kf6-knotifications.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-notifications fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-notifications
# Upstream KDE project: knotifications
%global oldname kf6-knotifications

%global framework knotifications

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-notifications
Version:        6.29.0
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 2 solution with abstraction for system notifications

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  libcanberra-devel
BuildRequires:  cmake(KF6Config)

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Provides:       kf6-knotifications%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-knotifications < %{version}-%{release}

%description
KDE Frameworks 6 Tier 3 solution with abstraction for system
notifications.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
Provides:       python3-kf6-knotifications = %{version}-%{release}

%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Provides:       kf6-knotifications-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-knotifications-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-knotifications-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-knotifications-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-knotifications-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-knotifications-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6
mkdir -p %{buildroot}/%{_kf6_datadir}/knotifications6

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Notifications.so.*
%dir %{_kf6_datadir}/knotifications6
%{_libdir}/qt6/qml/org/kde/notification/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/notification/knotificationqmlplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/notification/libknotificationqmlplugin.so
%{_libdir}/qt6/qml/org/kde/notification/qmldir

%files -n python3-%{name}
%{python3_sitearch}/KNotifications.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KNotifications/
%{_kf6_libdir}/libKF6Notifications.so
%{_kf6_libdir}/cmake/KF6Notifications/
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
