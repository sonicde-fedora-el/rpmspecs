%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}
Name:    libkcddb 
Version: 26.08.3
Release: 2%{?dist}
Summary: CDDB retrieval library

# Automatically converted from old format: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later - review is highly recommended.
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/multimedia/libkcddb

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-doctools-devel
BuildRequires: sonic-frameworks-text-codec-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires: sonic-frameworks-settings-utils-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-widgets-addons-devel

BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qt5compat-devel >= 6.11

BuildRequires: pkgconfig(libmusicbrainz5)

Requires:  %{name}-doc = %{version}-%{release}

# kcmshell5
Recommends:   kde-cli-tools

# when split occured (kdemultimedia to libkcddb)
Conflicts: kdemultimedia-libs < 6:4.8.80
# translations moved here (kf5-libkcddb)
Conflicts: kde-l10n < 17.03
Obsoletes: kf5-libkcddb-kcm < 24.01.85


%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# when split occured
Conflicts: kdemultimedia-devel < 6:4.8.80
%description devel
%{summary}.

%package doc
Summary: Documentation for %{name}
# Automatically converted from old format: GFDL - review is highly recommended.
License: LicenseRef-Callaway-GFDL
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
# now ahead of kf5-libkcddb
Conflicts: kf5-libkcddb-doc < 24.01.85
Obsoletes: kf5-libkcddb-doc < 24.01.85
%description doc
Documentation for %{name}.


%prep
%autosetup -p1


%build

%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-man
%find_lang %{name}-doc --all-name --with-html --without-mo

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_libdir}/libKCddb6.so.5*
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%{_kf6_datadir}/applications/kcm_cddb.desktop
%{_kf6_datadir}/config.kcfg/libkcddb5.kcfg
%{_kf6_datadir}/qlogging-categories6/*

%files devel
%{_kf6_libdir}/libKCddb6.so
%{_includedir}/KCddb6/
%{_kf6_libdir}/cmake/KCddb6/
%{_qt6_archdatadir}/mkspecs/modules/qt_KCddb.pri

%files doc -f %{name}-doc.lang


%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
