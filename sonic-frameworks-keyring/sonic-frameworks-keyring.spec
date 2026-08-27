# Generated for SonicDE from Fedora's kf6-kwallet.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-keyring fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-keyring
# Upstream KDE project: kwallet
%global oldname kf6-kwallet

%global framework kwallet

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-keyring
Version:        6.29.0
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for password management

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6ConfigWidgets)

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  pkgconfig(libsecret-1)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf6-filesystem
Requires:       pinentry-gui
Requires:       qca-qt6-ossl%{?_isa}

Provides:       kf6-kwallet%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kwallet < %{version}-%{release}

%description
KWallet is a secure and unified container for user passwords.

%package        libs
Summary:        KWallet framework libraries
Requires:       (%{name}%{?_isa} = %{version}-%{release} if systemd)
Provides:       kf6-kwallet-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kwallet-libs < %{version}-%{release}

%description    libs
Provides API to access KWallet data from applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel

Provides:       kf6-kwallet-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kwallet-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kwallet-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kwallet-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kwallet-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kwallet-html < %{version}-%{release}

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

%files -f %{oldname}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kwallet-query
%{_kf6_bindir}/kwalletd6
%{_kf6_bindir}/ksecretd
%{_kf6_datadir}/applications/org.kde.ksecretd.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.secretservicecompat.service
%{_kf6_datadir}/dbus-1/services/org.kde.kwalletd5.service
%{_kf6_datadir}/dbus-1/services/org.kde.kwalletd6.service
%{_kf6_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kwallet.service
%{_kf6_datadir}/knotifications6/ksecretd.notifyrc
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_datadir}/xdg-desktop-portal/portals/kwallet.portal
%{_kf6_datadir}/config.kcfg/kwalletsettings.kcfg
%{_mandir}/man1/kwallet-query.1*

%files libs
%{_kf6_libdir}/libKF6Wallet.so.*
%{_libdir}/libKF6WalletBackend.so.*

%files devel
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.KWallet.xml
%{_kf6_includedir}/KWallet/
%{_kf6_libdir}/cmake/KF6Wallet/
%{_kf6_libdir}/libKF6Wallet.so
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
