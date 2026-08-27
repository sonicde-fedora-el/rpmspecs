# Generated for SonicDE from Fedora's kf6-kuserfeedback.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-user-feedback fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-user-feedback
# Upstream KDE project: kuserfeedback
%global oldname kf6-kuserfeedback

%global framework kuserfeedback

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-user-feedback
Summary: Framework for collecting user feedback for apps via telemetry and surveys
Version:        6.29.0
Release:        3%{?dist}

License: MIT AND CC0-1.0 AND BSD-3-Clause
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

## upstream patches

BuildRequires: cmake
BuildRequires: gnupg2
BuildRequires: gcc-c++

BuildRequires: sonic-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
BuildRequires: sonic-frameworks-cmake-modules

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Charts)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6LinguistTools)

BuildRequires: bison
BuildRequires: flex

Provides:       kf6-kuserfeedback%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kuserfeedback < %{version}-%{release}

%description
%{summary}.

%package        console
Summary:        Analytics and administration tool for UserFeedback servers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtcharts%{?_isa}
# Obsolete the qt5 version
Obsoletes:      kuserfeedback-console < %{version}-%{release}
Provides:       kuserfeedback-console = %{version}-%{release}
Provides:       kuserfeedback-console%{?_isa} = %{version}-%{release}

Provides:       kf6-kuserfeedback-console%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kuserfeedback-console < %{version}-%{release}

%description    console
Analytics and administration tool for UserFeedback servers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)

Provides:       kf6-kuserfeedback-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kuserfeedback-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kuserfeedback-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kuserfeedback-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kuserfeedback-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kuserfeedback-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 \
   -DENABLE_DOCS:BOOL=OFF \
   -DENABLE_CONSOLE=ON

%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang userfeedbackconsole6 --with-qt
%find_lang userfeedbackprovider6 --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kuserfeedback-console.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kuserfeedback-console.desktop


%files -f userfeedbackprovider6.lang
%doc README.md
%license LICENSES/*
%{_bindir}/userfeedbackctl
%{_libdir}/libKF6UserFeedbackCore.so.*
%{_libdir}/libKF6UserFeedbackWidgets.so.*
%{_kf6_qmldir}/org/kde/userfeedback/
%{_kf6_datadir}/qlogging-categories6/org_kde_UserFeedback.categories

%files console -f userfeedbackconsole6.lang
%{_bindir}/UserFeedbackConsole
%{_datadir}/applications/org.kde.kuserfeedback-console.desktop
%{_kf6_metainfodir}/org.kde.kuserfeedback-console.appdata.xml

%files devel
%{_kf6_includedir}/KUserFeedback/
%{_kf6_includedir}/KUserFeedbackCore/
%{_kf6_includedir}/KUserFeedbackWidgets/
%{_libdir}/libKF6UserFeedbackCore.so
%{_libdir}/libKF6UserFeedbackWidgets.so
%{_kf6_libdir}/cmake/KF6UserFeedback/
%{_kf6_archdatadir}/mkspecs/modules/qt_KF6UserFeedback*.pri
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
