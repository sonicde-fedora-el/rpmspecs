# Generated for SonicDE from Fedora's kaccounts-integration.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-accounts-integration fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-accounts-integration
# Upstream KDE project: kaccounts-integration
%global oldname kaccounts-integration

# SonicDE is a Qt6/KF6-only hard fork; no KF5 packages are shipped, so the
# Qt5/KF5 compat build is never produced.
%bcond_with kf5

#Name:    kaccounts-integration
Name:           sonic-accounts-integration
Version:        26.04.3
Release:        3%{?dist}
Summary: Small system to administer web accounts across the KDE desktop
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later
#URL:     https://invent.kde.org/network/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/release-service/%%{version}/src/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

## upstream fixes

## upstreamable fixes

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-keyring-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  cmake(QCoro6)

BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Qml)

BuildRequires:  pkgconfig(accounts-qt6)
BuildRequires:  pkgconfig(libaccounts-glib) >= 1.21
BuildRequires:  cmake(SignOnQt6)

%if %{with kf5}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  cmake(QCoro5)

BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  pkgconfig(accounts-qt5)
BuildRequires:  cmake(SignOnQt5)
%endif

# For AutoReq cmake-filesystem
BuildRequires:  cmake

Provides:       kaccounts-integration%{?_isa} = %{version}-%{release}
Obsoletes:      kaccounts-integration < %{version}-%{release}

%description
Small system to administer web accounts for the sites and services
across the KDE desktop.

%if %{with kf5}
%package        qt5
Summary:        qt5 runtime for %{name}
Obsoletes:      kaccounts < 15.03
Provides:       kaccounts = %{version}-%{release}
Obsoletes:      sonic-accounts-integration < 24.01.75
Provides:       sonic-accounts-integration = %{version}-%{release}
# translations moved here
Conflicts: kde-l10n < 17.03

Provides:       kaccounts-integration-qt5%{?_isa} = %{version}-%{release}
Obsoletes:      kaccounts-integration-qt5 < %{version}-%{release}

%description    qt5
Small system to administer web accounts for the sites and services
across the KDE desktop.

%package        qt5-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt5Widgets)
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(AccountsQt5)
Requires:       cmake(SignOnQt5)
Requires:       pkgconfig(libaccounts-glib)
Requires:       intltool
Obsoletes:      kaccounts-integration-devel < 24.01.75
Provides:       kaccounts-integration-devel%{?_isa} = %{version}-%{release}

Provides:       kaccounts-integration-qt5-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kaccounts-integration-qt5-devel < %{version}-%{release}

%description    qt5-devel
Headers, development libraries and documentation for %{name}.
%endif

%package        qt6
Summary:        qt6 runtime for %{name}

Provides:       kaccounts-integration-qt6%{?_isa} = %{version}-%{release}
Obsoletes:      kaccounts-integration-qt6 < %{version}-%{release}

%description    qt6
Small system to administer web accounts for the sites and services
across the KDE desktop.

%package        qt6-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Widgets)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(AccountsQt6)
Requires:       cmake(SignOnQt6)
Requires:       pkgconfig(libaccounts-glib)
Requires:       intltool

Provides:       kaccounts-integration-qt6-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kaccounts-integration-qt6-devel < %{version}-%{release}

%description    qt6-devel
Headers, development libraries and documentation for %{name}.



%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
mkdir %{oldname}_qt6
pushd %{oldname}_qt6
%cmake_kf6 -S ..
%cmake_build
popd

%if %{with kf5}
mkdir %{oldname}_qt5
pushd %{oldname}_qt5
%cmake_kf5 -DKF6_COMPAT_BUILD=ON -S ..
%cmake_build
popd
%endif

%install
pushd %{oldname}_qt6
%cmake_install
popd
%find_lang %{oldname} --all-name --with-html

%if %{with kf5}
pushd %{oldname}_qt5
%cmake_install
popd
%endif

%files qt6 -f %{oldname}.lang
%doc README*
%license LICENSES/*
%{_kf6_datadir}/applications/kcm_kaccounts.desktop
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_kaccounts.so
%{_kf6_plugindir}/kded/kded_accounts.so
%dir %{_qt6_plugindir}/kaccounts/daemonplugins
%{_qt6_plugindir}/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
%{_kf6_libdir}/libkaccounts6.so.*
%{_kf6_qmldir}/org/kde/kaccounts/
%{_kf6_datadir}/qlogging-categories6/kaccounts.categories

%files qt6-devel
%{_kf6_libdir}/libkaccounts6.so
%{_kf6_libdir}/cmake/KAccounts6/
%{_includedir}/KAccounts6/

%if %{with kf5}
%files qt5
%doc README*
%license LICENSES/*
%{_kf5_libdir}/libkaccounts.so.*
%{_kf5_qmldir}/org/kde/kaccounts/
%{_kf5_datadir}/qlogging-categories5/kaccounts.categories

%files qt5-devel
%{_kf5_libdir}/libkaccounts.so
%{_kf5_libdir}/cmake/KAccounts/
%{_includedir}/KAccounts/
%endif

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
