# Generated for SonicDE from Fedora's kf6-kcolorscheme.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-color-scheme fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-color-scheme
# Upstream KDE project: kcolorscheme
%global oldname kf6-kcolorscheme

%global framework kcolorscheme

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-color-scheme
Version:        6.29.0
Release:        3%{?dist}
Summary: Classes to read and interact with KColorScheme
License: BSD-2-Clause and CC0-1.0 and LGPL-2.0-or-later and LGPL-2.1-only and LGPL-3.0-only and (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(xkbcommon)

Requires:       kf6-filesystem

Provides:       kf6-kcolorscheme%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcolorscheme < %{version}-%{release}

%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       kf6-kcolorscheme-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcolorscheme-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcolorscheme-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcolorscheme-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcolorscheme-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcolorscheme-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format


%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang kcolorscheme6 --all-name

%files -f kcolorscheme6.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/kcolorscheme.categories
%{_kf6_libdir}/libKF6ColorScheme.so.6
%{_kf6_libdir}/libKF6ColorScheme.so.%{version}

%files devel
%{_kf6_includedir}/KColorScheme
%{_kf6_libdir}/cmake/KF6ColorScheme
%{_kf6_libdir}/libKF6ColorScheme.so
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
