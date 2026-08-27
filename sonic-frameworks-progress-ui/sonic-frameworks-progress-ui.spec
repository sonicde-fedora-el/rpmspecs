# Generated for SonicDE from Fedora's kf6-kjobwidgets.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-progress-ui fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-progress-ui
# Upstream KDE project: kjobwidgets
%global oldname kf6-kjobwidgets

%global framework kjobwidgets

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-progress-ui
Version:        6.29.0
Release:        3%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon for KJobs
# The following are in the LICENSES folder, but go unused: LGPL-3.0-only, LicenseRef-KDE-Accepted-LGPL
License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  pkgconfig(shiboken6)
BuildRequires:  pkgconfig(pyside6)
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel

BuildRequires:  pkgconfig(xkbcommon)
Requires:       kf6-filesystem

Provides:       kf6-kjobwidgets%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kjobwidgets < %{version}-%{release}

%description
%{summary}.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
Provides:       python3-kf6-kjobwidgets = %{version}-%{release}

%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6CoreAddons)
Provides:       kf6-kjobwidgets-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kjobwidgets-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kjobwidgets-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kjobwidgets-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kjobwidgets-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kjobwidgets-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kjobwidgets6_qt

%files -f kjobwidgets6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6JobWidgets.so.*

%files -n python3-%{name}
%{python3_sitearch}/KJobWidgets.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KJobWidgets/
%{_kf6_libdir}/libKF6JobWidgets.so
%{_kf6_libdir}/cmake/KF6JobWidgets/
%{_kf6_datadir}/dbus-1/interfaces/*.xml
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
