# Generated for SonicDE from Fedora's kf6-kunitconversion.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-unit-conversion fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-unit-conversion
# Upstream KDE project: kunitconversion
%global oldname kf6-kunitconversion

%global framework kunitconversion

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-unit-conversion
Version:        6.29.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 2 addon for unit conversions

License: CC0-1.0 AND LGPL-2.0-or-later
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6I18n)
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:  kf6-filesystem

Provides:       kf6-kunitconversion = %{version}-%{release}
Conflicts:      kf6-kunitconversion < %{version}-%{release}

%description
KDE Frameworks 6 Tier 2 addon for unit conversions.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
Provides:       python3-kf6-kunitconversion = %{version}-%{release}
Conflicts:      python3-kf6-kunitconversion < %{version}-%{release}

%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Provides:       kf6-kunitconversion-devel = %{version}-%{release}
Conflicts:      kf6-kunitconversion-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kunitconversion-doc = %{version}-%{release}
Conflicts:      kf6-kunitconversion-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kunitconversion-html = %{version}-%{release}
Conflicts:      kf6-kunitconversion-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --all-name --with-man

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6UnitConversion.so.*
%{_kf6_datadir}/qlogging-categories6/%{framework}.*

%files -n python3-%{name}
%{python3_sitearch}/KUnitConversion.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KUnitConversion/
%{_kf6_libdir}/libKF6UnitConversion.so
%{_kf6_libdir}/cmake/KF6UnitConversion/
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
