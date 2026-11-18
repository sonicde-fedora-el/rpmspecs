# Generated for SonicDE from Fedora's konsole.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-terminal fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global reponame sonic-terminal
# Upstream KDE project: konsole
%global oldname konsole

%if  0%{?rhel} && 0%{?rhel} >= 10
# Tests require x11
# x11 is not in RHEL 10
%global tests 0
%else
%global tests 1
%endif

#Name:    konsole
Name:           sonic-terminal
Summary: KDE Terminal emulator
Version:        26.08.3
Release:        4%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://www.kde.org/applications/system/konsole/
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/release-service/%%{version}/src/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

## upstreamable patches

## upstream patches
# Backport of upstream commit 75ba4c3 (issue #5): keep the terminal window
# when it is minimized
Patch100: konsole-minimize-keep-window.patch

## downstream patches
Patch200: konsole-history_location_default.patch
# custom konsolerc that sets default to cache as well
Source10: konsolerc

%global sonicde_qt6_version 6.11.3
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig(zlib)

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-bookmarks-devel
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-settings-ui-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-crash-handler-devel
BuildRequires: sonic-frameworks-dbus-devel
BuildRequires: sonic-frameworks-doctools-devel
BuildRequires: sonic-frameworks-keybind-devel
BuildRequires: sonic-frameworks-gui-addons-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: sonic-frameworks-icon-themes-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-logging-devel
BuildRequires: sonic-frameworks-ipc-devel
BuildRequires: sonic-frameworks-qml-bridge
BuildRequires: sonic-frameworks-quick-ui
BuildRequires: sonic-frameworks-quick-desktop-style
BuildRequires: sonic-frameworks-addons-downloader-devel
BuildRequires: sonic-frameworks-notifications-devel
BuildRequires: sonic-frameworks-notification-settings-devel
BuildRequires: sonic-frameworks-ui-components-devel
BuildRequires: sonic-frameworks-pseudo-terminal-devel
BuildRequires: sonic-frameworks-app-info-devel
BuildRequires: sonic-frameworks-text-widgets-devel
BuildRequires: sonic-frameworks-widgets-addons-devel
BuildRequires: sonic-frameworks-windowsystem-devel
BuildRequires: sonic-frameworks-xml-gui-devel

BuildRequires: libappstream-glib
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qtmultimedia-devel >= 6.11
BuildRequires: qt6-qt5compat-devel >= 6.11
BuildRequires: libicu-devel
BuildRequires: cmake(libssh)

%if 0%{?tests}
BuildRequires: pkgconfig(x11)
BuildRequires: appstream
BuildRequires: xorg-x11-server-Xvfb dbus-x11
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

Requires: %{name}-part%{?_isa} = %{version}-%{release}
Requires: keditbookmarks

Obsoletes: konsole5 < 24.01.75

Provides:       konsole = %{version}-%{release}
Provides:       konsole%{?_isa} = %{version}-%{release}
%description
%{summary}.

%package part
Summary: Konsole kpart plugin
Provides:       konsole-part = %{version}-%{release}
Provides:       konsole-part%{?_isa} = %{version}-%{release}
Obsoletes:      konsole-part
Obsoletes:      konsole

%description part
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 \
  %{?flatpak:-DINSTALL_ICONS:BOOL=ON} \
  %{?with_tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build


%install
%cmake_install

install -m644 -p -D %{SOURCE10} %{buildroot}%{_kf6_sysconfdir}/xdg/konsolerc

%find_lang konsole --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.konsole.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.konsole.desktop
%if 0%{?tests}
xvfb-run -a bash -c "%ctest" || :
%endif


%files -f konsole.lang
%doc README*
%{_kf6_bindir}/konsole
%{_kf6_bindir}/konsoleprofile
%{_kf6_datadir}/applications/org.kde.konsole.desktop
%{_kf6_datadir}/kglobalaccel/org.kde.konsole.desktop
%{_kf6_datadir}/kio/servicemenus/konsolerun.desktop
%{_kf6_datadir}/knotifications6/konsole.notifyrc
%{_kf6_datadir}/qlogging-categories6/konsole.*
%{_kf6_datadir}/zsh/site-functions/_konsole
%{_kf6_metainfodir}/org.kde.konsole.appdata.xml
%if 0%{?flatpak}
%{_kf6_datadir}/icons/hicolor/*/apps/utilities-terminal.*
%endif


%files part
%config(noreplace) %{_kf6_sysconfdir}/xdg/konsolerc
%{_kf6_libdir}/libkonsoleapp.so.*
%{_kf6_libdir}/libkonsoleprivate.so.*
%{_qt6_qmldir}/org/sonicde/terminal/
%{_kf6_qtplugindir}/konsoleplugins/
%{_kf6_qtplugindir}/kf6/parts/konsolepart.so

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-4
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Backport upstream fix (commit 75ba4c3, issue #5): keep the terminal
  window when minimized - never propagate WindowMinimized to the hidden
  compat window, which made Qt hide the QML window (withdrawn on X11)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
