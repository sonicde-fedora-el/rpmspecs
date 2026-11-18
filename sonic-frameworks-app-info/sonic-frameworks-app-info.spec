# Generated for SonicDE from Fedora's kf6-kservice.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-app-info fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-frameworks-app-info
# Upstream KDE project: kservice
%global oldname kf6-kservice

%global framework kservice

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-app-info
Summary: KDE Frameworks 6 Tier 3 solution for advanced plugin and service introspection
Version:        6.31.0.1
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        3%{?dist}

# The following licenses are in the LICENSES folder but go unused: GPL-2.0-only, GPL-2.0-or-later, GPL-3.0-only, LicenseRef-KDE-Accepted-GPL
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel >= 6.11
# for the Administration category
# Recommends:       redhat-menus

Requires: kf6-filesystem >= 6.31

Provides:       kf6-kservice = %{version}-%{release}
Provides:       kf6-kservice%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kservice

%description
KDE Frameworks 6 Tier 3 solution for advanced plugin and service
introspection.

%package        devel
Summary:        Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: sonic-frameworks-settings-devel
Requires: sonic-frameworks-core-addons-devel
Provides:       kf6-kservice-devel = %{version}-%{release}
Provides:       kf6-kservice-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kservice-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kservice-doc = %{version}-%{release}
Provides:       kf6-kservice-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kservice-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kservice-html = %{version}-%{release}
Provides:       kf6-kservice-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kservice-html

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
mkdir -p %{buildroot}%{_kf6_datadir}/kservices6
mkdir -p %{buildroot}%{_kf6_datadir}/kservicetypes6

%files -f %{oldname}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_bindir}/kbuildsycoca6
%{_kf6_libdir}/libKF6Service.so.6
%{_kf6_libdir}/libKF6Service.so.%{libversion}
%{_kf6_datadir}/kservicetypes6/
%{_kf6_datadir}/kservices6/
%{_kf6_mandir}/man8/kbuildsycoca6.8.gz

%files devel
%{_kf6_includedir}/KService/
%{_kf6_libdir}/libKF6Service.so
%{_kf6_libdir}/cmake/KF6Service/
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
