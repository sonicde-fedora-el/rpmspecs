# Generated for SonicDE from Fedora's kf6-baloo.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-file-search fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-frameworks-file-search
# Upstream KDE project: baloo
%global oldname kf6-baloo

%global framework baloo

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-file-search
Summary: A Tier 3 KDE Frameworks 6 module that provides indexing and search functionality
Version:        6.31.0.1
Release:        3%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND bzip2-1.0.6
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

# Upstream Patches

## upstreamable patches
# http://bugzilla.redhat.com/1235026
Patch100: baloo-5.67.0-baloofile_config.patch

BuildRequires:  sonic-frameworks-cmake-modules >= %(echo %{version} | cut -d. -f1-3)
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-file-metadata-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-idle-tracker-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-device-integration-devel

BuildRequires:  lmdb-devel
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
# for systemd-related macros
BuildRequires:  systemd

Provides:       kf6-baloo = %{version}-%{release}
Provides:       kf6-baloo%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-baloo

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       sonic-frameworks-core-addons-devel
Requires:       sonic-frameworks-file-metadata-devel
Requires: qt6-qtbase-devel >= 6.11

Provides:       kf6-baloo-devel = %{version}-%{release}
Provides:       kf6-baloo-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-baloo-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        file
Summary:        File indexing and search for Baloo
Obsoletes:      kf5-baloo-file < 6
Provides:       kf6-baloo-file = %{version}-%{release}
Provides:       kf6-baloo-file%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-baloo-file

%description    file
%{summary}.

%package        libs
Summary:        Runtime libraries for %{name}
Provides:       kf6-baloo-libs = %{version}-%{release}
Provides:       kf6-baloo-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-baloo-libs

%description    libs
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-baloo-doc = %{version}-%{release}
Provides:       kf6-baloo-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-baloo-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-baloo-html = %{version}-%{release}
Provides:       kf6-baloo-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-baloo-html

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir}
%cmake_build_kf6

%install
%cmake_install_kf6

# baloodb not installed unless BUILD_EXPERIMENTAL is enabled, so omit translations
#rm -fv %%{buildroot}%%{_datadir}/locale/*/LC_MESSAGES/baloodb5.*

%find_lang baloodb6
%find_lang baloo_file6
%find_lang baloo_file_extractor6
%find_lang balooctl6
%find_lang balooengine6
%find_lang baloosearch6
%find_lang balooshow6
%find_lang kio6_baloosearch
%find_lang kio6_tags
%find_lang kio6_timeline

cat kio6_tags.lang kio6_baloosearch.lang kio6_timeline.lang \
    balooctl6.lang balooengine6.lang baloosearch6.lang \
    balooshow6.lang baloodb6.lang \
    > %{oldname}.lang

cat baloo_file6.lang baloo_file_extractor6.lang \
    > %{oldname}-file.lang

%files -f %{oldname}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/baloosearch6
%{_kf6_bindir}/balooshow6
%{_kf6_bindir}/balooctl6
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_datadir}/config.kcfg/baloosettings.kcfg

%files file -f %{oldname}-file.lang
%config(noreplace) %{_kf6_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_userunitdir}/kde-baloo.service
%{_libexecdir}/kf6/baloo_file
%{_libexecdir}/kf6/baloo_file_extractor

%files libs
%license LICENSES/*
%{_kf6_libdir}/libKF6Baloo.so.*
%{_kf6_libdir}/libKF6BalooEngine.so.*
%{_kf6_plugindir}/kio/baloosearch.so
%{_kf6_plugindir}/kio/tags.so
%{_kf6_plugindir}/kio/timeline.so
%{_kf6_plugindir}/kded/baloosearchmodule.so
%{_kf6_qmldir}/org/kde/baloo

%files devel
%{_kf6_libdir}/libKF6Baloo.so
%{_kf6_libdir}/cmake/KF6Baloo/
%{_kf6_libdir}/pkgconfig/KF6Baloo.pc
%{_kf6_includedir}/Baloo/
%{_kf6_datadir}/dbus-1/interfaces/org.kde.baloo.*.xml
%{_kf6_datadir}/dbus-1/interfaces/org.kde.Baloo*.xml
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
