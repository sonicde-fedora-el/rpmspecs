# Generated for SonicDE from Fedora's kf6-frameworkintegration.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-qt-integration fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-qt-integration
# Upstream KDE project: frameworkintegration
%global oldname kf6-frameworkintegration

%global framework frameworkintegration

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-qt-integration
Version:        6.29.0
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 4 workspace and cross-framework integration plugins
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Package)
BuildRequires:  sonic-rpm-macros
BuildRequires:  libXcursor-devel
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(AppStreamQt) >= 1.0
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  cmake(KF6ColorScheme)
Requires:  kf6-filesystem

Provides:       kf6-frameworkintegration%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-frameworkintegration < %{version}-%{release}

%description
Framework Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

Applications do not need to link to this directly.

%package        libs
Summary:        Runtime libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf6-frameworkintegration-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-frameworkintegration-libs < %{version}-%{release}

%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6IconThemes)
Requires:       cmake(KF6ConfigWidgets)

Provides:       kf6-frameworkintegration-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-frameworkintegration-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains files to develop for %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-frameworkintegration-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-frameworkintegration-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-frameworkintegration-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-frameworkintegration-html < %{version}-%{release}

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
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/knotifications6/plasma_workspace.notifyrc
%dir %{_kf6_libexecdir}/kpackagehandlers
%{_kf6_libexecdir}/kpackagehandlers/knshandler

%files libs
%{_kf6_libdir}/libKF6Style.so.*
%{_kf6_plugindir}/FrameworkIntegrationPlugin.so
%{_kf6_libexecdir}/kpackagehandlers/appstreamhandler

%files devel
%{_kf6_includedir}/FrameworkIntegration/
%{_kf6_includedir}/KStyle/
%{_kf6_libdir}/libKF6Style.so
%{_kf6_libdir}/cmake/KF6FrameworkIntegration/
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
