%global sonicde_frameworks_version 6.31.0
%global debug_package %{nil}
%global sonicde_qt6_version 6.11.3
# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# https://bugzilla.redhat.com/show_bug.cgi?id=1895674
%global _lto_cflags %{nil}

Name:    libkgapi
Version: 26.08.3
Release: 3%{?dist}
Summary: Library to access to Google services

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qttools-static >= 6.11
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-keyring-devel
BuildRequires:  sonic-frameworks-windowsystem-devel

BuildRequires:  kf6-kcalendarcore-devel >= 6.31
BuildRequires:  kf6-kcontacts-devel >= 6.31

BuildRequires:  cyrus-sasl-devel

Obsoletes:      libkgoogle
Provides:       libkgoogle = %{version}-%{release}

%description
Library to access to Google services, this package is needed by kdepim-runtime
to build akonadi-google resources.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       sonic-frameworks-core-addons-devel
Requires:       kf6-kcalendarcore-devel >= 6.31
Requires:       kf6-kcontacts-devel >= 6.31
Obsoletes:      libkgoogle-devel
Provides:       libkgoogle-devel = %{version}-%{release}
%description devel
Libraries and header files for developing applications that use akonadi-google
resources.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf6 -DBUILD_QCH=OFF -DBUILD_DOCS=OFF
%cmake_build

%install
%cmake_install
%find_lang libkgapi_qt --all-name --with-html --with-man --with-qt

%files -f libkgapi_qt.lang
%doc README*
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_libdir}/sasl2/libkdexoauth2.so*
%{_kf6_libdir}/libKPim6GAPI*.so.6
%{_kf6_libdir}/libKPim6GAPI*.so.6.*

%files devel
%{_kf6_libdir}/libKPim6GAPI*.so
%{_kf6_libdir}/cmake/KPim6GAPI/
%dir %{_includedir}/KPim6/
%{_includedir}/KPim6/KGAPI/

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
