# Generated for SonicDE from Fedora's plasma-keyboard.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-keyboard fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-keyboard
# Upstream KDE project: plasma-keyboard
%global oldname plasma-keyboard
#Name:           plasma-keyboard
Name:           sonic-keyboard
Epoch:          1
Version:        6.8.2
Release:        3%{?dist}
Summary:        Virtual Keyboard for Qt based desktops

License:        LGPL-2.1-only AND GPL-2.0-only AND CC0-1.0 AND LGPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-only
#URL:            https://invent.kde.org/plasma/%%{oldname}/
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{oldname}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

BuildRequires:  qt6-qtvirtualkeyboard-devel >= 6.11
BuildRequires:  qt6-qtwayland-devel >= 6.11
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-crash-handler-devel

BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  sonic-interface-libraries-devel

Requires:       (kcm-%{name}%{?_isa} if sonic-system-settings%{?_isa})

Provides:       plasma-keyboard = %{epoch}:%{version}-%{release}
Provides:       plasma-keyboard%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      plasma-keyboard < %{epoch}:%{version}-%{release}
Conflicts:      plasma-keyboard

%description
The plasma-keyboard is a virtual keyboard
based on Qt Virtual Keyboard designed to
integrate in Plasma.

%package -n kcm-%{name}
Summary: KDE KCM for %{name}
Provides:       kcm-plasma-keyboard = %{epoch}:%{version}-%{release}
Provides:       kcm-plasma-keyboard%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      kcm-plasma-keyboard < %{epoch}:%{version}-%{release}
Conflicts:      kcm-plasma-keyboard
Requires: %{name} = %{epoch}:%{version}-%{release}
%description -n kcm-%{name}
%{summary}.

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang plasma-keyboard
%find_lang kcm_plasmakeyboard

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasma.keyboard.desktop

%files -f plasma-keyboard.lang
%license LICENSES/*
%doc README.md
%{_bindir}/plasma-keyboard
%{_libdir}/libsonickeyboardui.so*
%{_kf6_datadir}/applications/org.kde.plasma.keyboard.desktop
%{_kf6_qmldir}/org/kde/plasma/keyboard/
%{_kf6_datadir}/plasma/keyboard/
%{_kf6_metainfodir}/org.kde.plasma.keyboard.metainfo.xml
%{_qt6_plugindir}/platforminputcontexts/sonicvirtualkeyboardplugin.so
%{_qt6_qmldir}/QtQuick/VirtualKeyboard/
%{_datadir}/config.kcfg/plasmakeyboardsettings.kcfg

%files -n kcm-%{name} -f kcm_plasmakeyboard.lang
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plasmakeyboard.so
%{_datadir}/applications/kcm_plasmakeyboard.desktop

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Pin Plasma cmake deps to SonicDE providers (Fedora libplasma 6.8.3 outranks ours)
* Wed Nov 11 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1:6.8.2-1
- 6.8.2, renamed to sonic-keyboard from Sonic-DE fork

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1:6.7.4-2
- SonicDE build for Enterprise Linux 10

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.4-1
- 6.6.4
