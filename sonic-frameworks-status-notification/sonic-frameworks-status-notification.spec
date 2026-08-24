# Generated for SonicDE from Fedora's kf6-kstatusnotifieritem.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-status-notification fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-status-notification
# Upstream KDE project: kstatusnotifieritem
%global oldname kf6-kstatusnotifieritem

%global framework kstatusnotifieritem

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-status-notification
Version:        6.29.0
Release:        1%{?dist}
Summary:        Implementation of Status Notifier Items

License:        CC0-1.0 AND LGPL-2.0-or-later
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:  kf6-filesystem

Provides:       kf6-kstatusnotifieritem = %{version}-%{release}
Conflicts:      kf6-kstatusnotifieritem < %{version}-%{release}

%description
%summary.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
Provides:       python3-kf6-kstatusnotifieritem = %{version}-%{release}
Conflicts:      python3-kf6-kstatusnotifieritem < %{version}-%{release}

%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf6-kstatusnotifieritem-devel = %{version}-%{release}
Conflicts:      kf6-kstatusnotifieritem-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kstatusnotifieritem-doc = %{version}-%{release}
Conflicts:      kf6-kstatusnotifieritem-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kstatusnotifieritem-html = %{version}-%{release}
Conflicts:      kf6-kstatusnotifieritem-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kstatusnotifieritem6_qt

%files -f kstatusnotifieritem6_qt.lang
%{_kf6_libdir}/libKF6StatusNotifierItem.so.*
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.StatusNotifierItem.xml
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.StatusNotifierWatcher.xml
%{_kf6_datadir}/qlogging-categories6/kstatusnotifieritem.categories

%files -n python3-%{name}
%{python3_sitearch}/KStatusNotifierItem.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KStatusNotifierItem
%{_kf6_libdir}/cmake/KF6StatusNotifierItem
%{_kf6_libdir}/libKF6StatusNotifierItem.so
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
