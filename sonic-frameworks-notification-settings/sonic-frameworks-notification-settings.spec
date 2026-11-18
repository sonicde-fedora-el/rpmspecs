# Generated for SonicDE from Fedora's kf6-knotifyconfig.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-notification-settings fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-frameworks-notification-settings
# Upstream KDE project: knotifyconfig
%global oldname kf6-knotifyconfig

%global framework knotifyconfig

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-notification-settings
Version:        6.31.0
Release:        3%{?dist}
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
BuildRequires:  sonic-frameworks-autocomplete-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-xml-gui-devel
BuildRequires:  sonic-rpm-macros
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtspeech-devel >= 6.11
Requires: kf6-filesystem >= 6.31

Provides:       kf6-knotifyconfig = %{version}-%{release}
Provides:       kf6-knotifyconfig%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-knotifyconfig

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Provides:       kf6-knotifyconfig-devel = %{version}-%{release}
Provides:       kf6-knotifyconfig-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-knotifyconfig-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-knotifyconfig-doc = %{version}-%{release}
Provides:       kf6-knotifyconfig-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-knotifyconfig-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-knotifyconfig-html = %{version}-%{release}
Provides:       kf6-knotifyconfig-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-knotifyconfig-html

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
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
