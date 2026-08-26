# Generated for SonicDE from Fedora's dolphin.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-ecco fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-ecco
# Upstream KDE project: dolphin
%global oldname dolphin

%global tests 0

#Name:           dolphin
Name:           sonic-ecco
Summary:        KDE File Manager
Version:        26.04.3.2
Release:        1%{?dist}

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

BuildRequires:  cmake(KF6Baloo)
# baloo-widget is part of Gear like Dolphin thus both versions need to match.
# We use the major.minor.patch macros to not fail the build on hotfix releases.
BuildRequires:  cmake(KF6BalooWidgets)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6GuiAddons)

BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(packagekitqt6)
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
Conflicts:      dolphin < %{version}-%{release}

%description
%{summary}.

%package        libs
Summary:        Dolphin runtime libraries
Provides:       dolphin-libs = %{version}-%{release}
Conflicts:      dolphin-libs < %{version}-%{release}

%description    libs
%{summary}.

%package        devel
Summary:        Developer files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel%{?_isa}
Requires:       sonic-frameworks-io-devel%{?_isa}
Provides:       dolphin-devel = %{version}-%{release}
Conflicts:      dolphin-devel < %{version}-%{release}

%description    devel
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 \
  %{?flatpak:-DFLATPAK:BOOL=ON} \
  -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

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
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
