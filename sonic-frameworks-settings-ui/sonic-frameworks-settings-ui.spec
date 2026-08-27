# Generated for SonicDE from Fedora's kf6-kconfigwidgets.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-settings-ui fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-settings-ui
# Upstream KDE project: kconfigwidgets
%global oldname kf6-kconfigwidgets

%global framework kconfigwidgets

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-settings-ui
Version:        6.29.0
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for creating configuration dialogs

# The following licenses are in LICENSES but go unused: BSD-3-Clause, MIT
License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  pkgconfig(xkbcommon)

Requires:  kf6-filesystem

Provides:       kf6-kconfigwidgets%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kconfigwidgets < %{version}-%{release}

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       sonic-frameworks-auth-devel
Requires:       sonic-frameworks-text-codec-devel
Requires:       cmake(KF6ColorScheme)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6WidgetsAddons)
Provides:       kf6-kconfigwidgets-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kconfigwidgets-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kconfigwidgets-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kconfigwidgets-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kconfigwidgets-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kconfigwidgets-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --with-man --all-name

%files -f %{oldname}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6ConfigWidgets.so.*
%{_datadir}/locale/*/kf6_entry.desktop
%{_kf6_datadir}/qlogging-categories6/%{framework}*

%files devel
%{_kf6_includedir}/KConfigWidgets/
%{_kf6_libdir}/libKF6ConfigWidgets.so
%{_kf6_libdir}/cmake/KF6ConfigWidgets/
%{_kf6_libdir}/qt6/plugins/designer/kconfigwidgets6widgets.so
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
