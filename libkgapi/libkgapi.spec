%global debug_package %{nil}
# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# https://bugzilla.redhat.com/show_bug.cgi?id=1895674
%global _lto_cflags %{nil}

Name:    libkgapi
Version: 26.04.3
Release: 1%{?dist}
Summary: Library to access to Google services

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  qt6-qttools-static

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)

BuildRequires:  cyrus-sasl-devel

Obsoletes:      libkgoogle < 0.3.2
Provides:       libkgoogle = %{version}-%{release}

%description
Library to access to Google services, this package is needed by kdepim-runtime
to build akonadi-google resources.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6CalendarCore)
Requires:       cmake(KF6Contacts)
Obsoletes:      libkgoogle-devel < 0.3.2
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
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
