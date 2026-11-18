# Generated for SonicDE from Fedora's kf6-ksvg.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-svg fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-frameworks-svg
# Upstream KDE project: ksvg
%global oldname kf6-ksvg

%global framework ksvg

#Name:    kf6-ksvg
Name:           sonic-frameworks-svg
Summary: Components for handling SVGs
Version:        6.31.0.1
Release:        3%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

# upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-cmake-modules >= %(echo %{version} | cut -d. -f1-3)

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires: qt6-qtsvg-devel >= 6.11
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: sonic-frameworks-archive-devel
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-gui-addons-devel
BuildRequires: sonic-frameworks-quick-ui-devel
BuildRequires: sonic-frameworks-color-scheme-devel

Provides:       kf6-ksvg = %{version}-%{release}
Provides:       kf6-ksvg%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ksvg

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

Provides:       kf6-ksvg-devel = %{version}-%{release}
Provides:       kf6-ksvg-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ksvg-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-ksvg-doc = %{version}-%{release}
Provides:       kf6-ksvg-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ksvg-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-ksvg-html = %{version}-%{release}
Provides:       kf6-ksvg-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ksvg-html

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
%license LICENSES/*
%{_kf6_libdir}/libKF6Svg.so.*
%{_kf6_libdir}/qt6/qml/org/kde/ksvg
%{_kf6_datadir}/qlogging-categories6/ksvg.categories

%files devel
%{_kf6_includedir}/KSvg
%{_kf6_libdir}/cmake/KF6Svg
%{_kf6_libdir}/libKF6Svg.so
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
