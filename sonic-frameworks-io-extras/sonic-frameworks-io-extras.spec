# Generated for SonicDE from Fedora's kio-extras.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-io-extras fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-io-extras
# Upstream KDE project: kio-extras
%global oldname kio-extras

#Name:    kio-extras
Name:           sonic-frameworks-io-extras
Version:        26.04.3
Release:        1%{?dist}
Summary: Additional components to increase the functionality of KIO Framework

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
#URL:     https://invent.kde.org/network/kio-extras
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/release-service/%%{version}/src/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

## upstramable patches

## upstream patches

BuildRequires:  bzip2-devel
BuildRequires:  gperf

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Notifications)

BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaActivitiesStats)

BuildRequires:  cmake(KDSoap) >= 1.9
BuildRequires:  cmake(KDSoapWSDiscoveryClient)
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  pkgconfig(libproxy-1.0)

BuildRequires:  libjpeg-devel
BuildRequires:  libmtp-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
BuildRequires:  cmake(OpenEXR)
BuildRequires:  perl-generators
BuildRequires:  phonon-qt6-devel
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  taglib-devel > 1.11

# This package provides plugins for KIO
Supplements:    kf6-kio-core

Provides:       kio-extras = %{version}-%{release}
Conflicts:      kio-extras < %{version}-%{release}

%description
%{summary}.

%package info
Summary: Info kioslave
Provides:       kio-extras-info = %{version}-%{release}
Conflicts:      kio-extras-info < %{version}-%{release}

%description info
Kioslave for reading info pages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kio-extras-devel = %{version}-%{release}
Conflicts:      kio-extras-devel < %{version}-%{release}

%description devel
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 -DLIBSSH_LIBRARIES="$(pkg-config --libs libssh)"
%cmake_build


%install
%cmake_install
%find_lang %{oldname} --all-name --with-html


%files -f %{name}.lang
%license LICENSES/*

%{_kf6_plugindir}/kded/
%exclude %{_kf6_plugindir}/kio/info.so
%{_kf6_plugindir}/kio/
%{_kf6_plugindir}/kiod/
%{_kf6_plugindir}/thumbcreator/
%{_kf6_plugindir}/kfileitemaction/
%{_datadir}/config.kcfg/jpegcreatorsettings5.kcfg
%{_datadir}/dbus-1/services/org.kde.kmtpd5.service
%{_datadir}/applications/kcm_*
%{_datadir}/mime/packages/org.kde.kio.smb.xml
%{_datadir}/remoteview/
%{_datadir}/konqueror/
%dir %{_kf6_datadir}/kio_filenamesearch/
%{_kf6_datadir}/kio_filenamesearch/kio-filenamesearch-grep
%{_kf6_datadir}/qlogging-categories6/kio-extras*
%{_kf6_datadir}/solid/actions/solid_afc.desktop
%{_kf6_datadir}/solid/actions/solid_mtp.desktop
%{_kf6_libdir}/libkioarchive6.so.6{,.*}
%{_kf6_libexecdir}/smbnotifier
%{_libexecdir}/wpad-detector-helper
%{_kf6_qtplugindir}/kcm_trash.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_*.so

%files info
%{_kf6_plugindir}/kio/info.so
# perl deps, but required at runtime for the info kioslave to actually work:
%dir %{_datadir}/kio_info/
%{_datadir}/kio_info/kde-info2html*

%files devel
%{_includedir}/KioArchive6/*.h
%{_kf6_libdir}/cmake/KioArchive6/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
