# Generated for SonicDE from Fedora's kf6-kcrash.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-crash-handler fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-frameworks-crash-handler
# Upstream KDE project: kcrash
%global oldname kf6-kcrash

%global framework kcrash

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-crash-handler
Version:        6.31.0.1
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 2 addon for handling application crashes

License: CC0-1.0 AND LGPL-2.0-or-later
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %(echo %{version} | cut -d. -f1-3)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel >= 6.11
Provides:       kf6-kcrash = %{version}-%{release}
Provides:       kf6-kcrash%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcrash

%description
KCrash provides support for intercepting and handling application crashes.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires: qt6-qtbase-devel >= 6.11
Provides:       kf6-kcrash-devel = %{version}-%{release}
Provides:       kf6-kcrash-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcrash-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcrash-doc = %{version}-%{release}
Provides:       kf6-kcrash-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcrash-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kcrash-html = %{version}-%{release}
Provides:       kf6-kcrash-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kcrash-html

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
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Crash.so.*

%files devel
%{_kf6_includedir}/KCrash/
%{_kf6_libdir}/libKF6Crash.so
%{_kf6_libdir}/cmake/KF6Crash/
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
