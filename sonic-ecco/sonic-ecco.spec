# Generated for SonicDE from Fedora's dolphin.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-ecco fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-ecco
# Upstream KDE project: dolphin
%global oldname dolphin

%global tests 0

#Name:           dolphin
Name:           sonic-ecco
Summary:        KDE File Manager
Version:        26.08.3
Release:        5%{?dist}

License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:            https://invent.kde.org/system/dolphin
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:        https://download.kde.org/%%{stable_kf6}/release-service/%%{maj_ver_kf6}.%%{min_ver_kf6}.%%{bug_ver_kf6}/src/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

# Upstream

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  systemd-rpm-macros

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  sonic-frameworks-file-search-devel
# baloo-widget is part of Gear like Dolphin thus both versions need to match.
# We use the major.minor.patch macros to not fail the build on hotfix releases.
BuildRequires:  baloo-widgets-devel = 26.08.3
BuildRequires:  sonic-frameworks-bookmarks-devel
BuildRequires:  sonic-frameworks-text-codec-devel
BuildRequires:  sonic-frameworks-autocomplete-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-file-metadata-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-addons-downloader-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-ui-components-devel
BuildRequires:  sonic-frameworks-device-integration-devel
BuildRequires:  sonic-frameworks-text-widgets-devel
BuildRequires:  sonic-frameworks-user-feedback-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-gui-addons-devel

BuildRequires:  sonic-activities-devel

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtmultimedia-devel >= 6.11
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  packagekit-qt6-devel
BuildRequires:  cmake(Phonon4Qt6)

%if 0%{?tests}
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: rubygem(test-unit)
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Recommends:     konsole-part%{?_isa}
Recommends:     kio-fuse%{?_isa}
Recommends:     sonic-frameworks-io-extras%{?_isa}
Recommends:     %{name}-plugins
# Image Previews
Recommends:     sonic-frameworks-image-formats%{?_isa}
Recommends:     qt6-qtimageformats%{?_isa}
Recommends:     ffmpegthumbs%{?_isa}

Provides:       dolphin = %{version}-%{release}
Provides:       dolphin%{?_isa} = %{version}-%{release}
Obsoletes:      dolphin

%description
%{summary}.

%package        libs
Summary:        Dolphin runtime libraries
Provides:       dolphin-libs = %{version}-%{release}
Provides:       dolphin-libs%{?_isa} = %{version}-%{release}
Obsoletes:      dolphin-libs

%description    libs
%{summary}.

%package        devel
Summary:        Developer files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel%{?_isa}
Requires:       sonic-frameworks-io-devel%{?_isa}
Provides:       dolphin-devel = %{version}-%{release}
Provides:       dolphin-devel%{?_isa} = %{version}-%{release}
Obsoletes:      dolphin-devel

%description    devel
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 \
  %{?flatpak:-DFLATPAK:BOOL=ON} \
  -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir} \
  -DBUILD_TESTING:BOOL=%{?with_tests:ON}%{!?with_tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang dolphin --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{oldname}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{oldname}.desktop
%if 0%{?tests}
xvfb-run -a bash -c "%ctest" || :
%endif


%files -f dolphin.lang
%license LICENSES/*
%doc README*
%{_kf6_datadir}/qlogging-categories6/dolphin.*
%{_kf6_bindir}/dolphin
%{_kf6_bindir}/servicemenuinstaller
%{_kf6_datadir}/config.kcfg/dolphin_*
%{_kf6_datadir}/knsrcfiles/*
%if 0%{?flatpak}
%{_datadir}/dbus-1/services/org.freedesktop.FileManager1.service
%else
%{_datadir}/dbus-1/services/org.kde.dolphin.FileManager1.service
%endif
%{_userunitdir}/plasma-dolphin.service
%{_kf6_metainfodir}/org.kde.%{oldname}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{oldname}.desktop
%dir %{_kf6_datadir}/kglobalaccel/
%{_kf6_datadir}/kglobalaccel/org.kde.dolphin.desktop
%{_kf6_datadir}/kconf_update/dolphin_detailsmodesettings.upd
%{_kf6_datadir}/kconf_update/dolphin_replace_view_mode_with_view_settings_in_toolbar.py
%{_kf6_datadir}/kconf_update/dolphin_replace_view_mode_with_view_settings_in_toolbar.upd
%{_kf6_libdir}/kconf_update_bin/dolphin_25.04_update_statusandlocationbarssettings
%{_kf6_datadir}/kconf_update/dolphin_statusandlocationbarssettings.upd
%dir %{_kf6_datadir}/dolphin
%{_kf6_datadir}/dolphin/dolphinpartactions.desktop
%{_kf6_datadir}/zsh/site-functions/_dolphin
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.dolphin.svg
%{_kf6_libdir}/kconf_update_bin/dolphin_update_splitviewsettings
%{_kf6_datadir}/kconf_update/dolphin_tab_key_shortcut_for_focus_other_view.py
%{_kf6_datadir}/kconf_update/dolphin_tab_key_shortcut_for_focus_other_view.upd

%files libs
%{_kf6_libdir}/libdolphinprivate.so.*
%{_kf6_libdir}/libdolphinvcs.so.*
%{_kf6_plugindir}/parts/dolphinpart.so
%{_kf6_qtplugindir}/dolphin/
%{_kf6_qtplugindir}/kf6/kfileitemaction/movetonewfolderitemaction.so
%{_kf6_qtplugindir}/kf6/kfileitemaction/setfoldericonitemaction.so
%{_kf6_qtplugindir}/kf6/kfileitemaction/hidefileitemaction.so

%files devel
%{_includedir}/Dolphin/
%{_includedir}/dolphin*_export.h
%{_kf6_libdir}/cmake/DolphinVcs/
%{_kf6_libdir}/libdolphinvcs.so
%{_datadir}/dbus-1/interfaces/org.freedesktop.FileManager1.xml

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-5
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-4
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Pin cmake() BuildRequires to SonicDE package names so the
  alma+epel-10 solver cannot pick EPEL's Qt 6.10-linked providers
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Pin Plasma cmake deps to SonicDE providers (Fedora libplasma 6.8.3 outranks ours)
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
