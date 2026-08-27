# Generated for SonicDE from Fedora's kf6-kdeclarative.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-qml-bridge fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-qml-bridge
# Upstream KDE project: kdeclarative
%global oldname kf6-kdeclarative

%global framework kdeclarative

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-qml-bridge
Version:        6.29.0
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for Qt declarative

License: CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  cmake
BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  libepoxy-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
Requires:  kf6-filesystem

Provides:       kf6-kdeclarative%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kdeclarative < %{version}-%{release}

%description
KDE Frameworks 6 Tier 3 addon for Qt declarative

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Config)
Requires:       cmake(KF6Package)
Requires:       qt6-qtdeclarative-devel
Provides:       kf6-kdeclarative-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kdeclarative-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kdeclarative-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kdeclarative-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kdeclarative-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kdeclarative-html < %{version}-%{release}

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
%{_kf6_libdir}/libKF6CalendarEvents.so.*
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%{_kf6_qmldir}/org/kde/draganddrop/
%{_kf6_qmldir}/org/kde/graphicaleffects/
%{_kf6_qmldir}/org/kde/kquickcontrols/
%{_kf6_qmldir}/org/kde/private/kquickcontrols/
%{_kf6_qmldir}/org/kde/kquickcontrolsaddons/
%{_kf6_libdir}/libkquickcontrolsprivate.so.0
%{_kf6_libdir}/libkquickcontrolsprivate.so.%{version}

%files devel
%{_kf6_includedir}/KDeclarative/
%{_kf6_libdir}/libKF6CalendarEvents.so
%{_kf6_libdir}/cmake/KF6Declarative/
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
