# Generated for SonicDE from Fedora's kf6-kiconthemes.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-icon-themes fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-icon-themes
# Upstream KDE project: kiconthemes
%global oldname kf6-kiconthemes

%global framework kiconthemes

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-icon-themes
Version:        6.29.0
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 3 integration module with icon themes

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  sonic-rpm-macros

BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6BreezeIcons)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  pkgconfig(xkbcommon)

Requires:       hicolor-icon-theme

Provides:       kf6-kiconthemes%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kiconthemes < %{version}-%{release}

%description
KDE Frameworks 6 Tier 3 integration module with icon themes

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Provides:       kf6-kiconthemes-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kiconthemes-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kiconthemes-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kiconthemes-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kiconthemes-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kiconthemes-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --all-name

%files -f %{oldname}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kiconfinder6
%{_kf6_libdir}/libKF6IconThemes.so.*
%{_kf6_libdir}/libKF6IconWidgets.so.*
%{_kf6_qtplugindir}/kiconthemes6/iconengines/KIconEnginePlugin.so
%{_kf6_libdir}/qt6/qml/org/kde/iconthemes/
%{_kf6_datadir}/qlogging-categories6/%{framework}.*

%files devel
%{_kf6_includedir}/KIconThemes
%{_kf6_includedir}/KIconWidgets
%{_kf6_libdir}/libKF6IconThemes.so
%{_kf6_libdir}/libKF6IconWidgets.so
%{_kf6_libdir}/cmake/KF6IconThemes/
%{_kf6_qtplugindir}/designer/kiconthemes6widgets.so
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
