# Generated for SonicDE from Fedora's kf6-knotifyconfig.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-notification-settings fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-notification-settings
# Upstream KDE project: knotifyconfig
%global oldname kf6-knotifyconfig

%global framework knotifyconfig

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-notification-settings
Version:        6.29.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 module for KNotify configuration

License: CC0-1.0 AND LGPL-2.0-only
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  cmake
BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  sonic-rpm-macros
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6TextToSpeech)
Requires:  kf6-filesystem

Provides:       kf6-knotifyconfig = %{version}-%{release}
Conflicts:      kf6-knotifyconfig < %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Provides:       kf6-knotifyconfig-devel = %{version}-%{release}
Conflicts:      kf6-knotifyconfig-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-knotifyconfig-doc = %{version}-%{release}
Conflicts:      kf6-knotifyconfig-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-knotifyconfig-html = %{version}-%{release}
Conflicts:      kf6-knotifyconfig-html < %{version}-%{release}

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
%{_kf6_datadir}/qlogging-categories6/*%{framework}.*
%{_kf6_libdir}/libKF6NotifyConfig.so.*

%files devel
%{_kf6_includedir}/KNotifyConfig/
%{_kf6_libdir}/libKF6NotifyConfig.so
%{_kf6_libdir}/cmake/KF6NotifyConfig/
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
