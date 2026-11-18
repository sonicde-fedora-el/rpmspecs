# Generated for SonicDE from Fedora's kf6-kiconthemes.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-icon-themes fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-frameworks-icon-themes
# Upstream KDE project: kiconthemes
%global oldname kf6-kiconthemes

%global framework kiconthemes

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-icon-themes
Version:        6.31.0.1
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
BuildRequires:  sonic-frameworks-cmake-modules >= %(echo %{version} | cut -d. -f1-3)
BuildRequires:  sonic-rpm-macros

BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtsvg-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qttools-devel >= 6.11
BuildRequires:  sonic-frameworks-archive-devel
BuildRequires:  sonic-frameworks-silver-icons-devel
BuildRequires:  sonic-frameworks-color-scheme-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-data-views-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel

BuildRequires:  pkgconfig(xkbcommon)

Requires:       hicolor-icon-theme

Provides:       kf6-kiconthemes = %{version}-%{release}
Provides:       kf6-kiconthemes%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kiconthemes

%description
KDE Frameworks 6 Tier 3 integration module with icon themes

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Provides:       kf6-kiconthemes-devel = %{version}-%{release}
Provides:       kf6-kiconthemes-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kiconthemes-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kiconthemes-doc = %{version}-%{release}
Provides:       kf6-kiconthemes-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kiconthemes-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kiconthemes-html = %{version}-%{release}
Provides:       kf6-kiconthemes-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kiconthemes-html

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
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0.1-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0.1-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
