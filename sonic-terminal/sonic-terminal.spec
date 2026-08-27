# Generated for SonicDE from Fedora's konsole.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-terminal fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
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
Version:        26.04.3.1
Release:        4%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://www.kde.org/applications/system/konsole/
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/release-service/%%{version}/src/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

## upstreamable patches

## upstream patches

## downstream patches
Patch200: konsole-history_location_default.patch
# custom konsolerc that sets default to cache as well
Source10: konsolerc

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig(zlib)

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Pty)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: libappstream-glib
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)
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

Provides:       konsole%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package part
Summary: Konsole kpart plugin
Provides:       konsole-part%{?_isa} = %{version}-%{release}
Obsoletes:      konsole-part < %{version}-%{release}
Obsoletes:      konsole < %{version}-%{release}

%description part
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 \
  %{?flatpak:-DINSTALL_ICONS:BOOL=ON} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

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
%{_kf6_qtplugindir}/konsoleplugins/
%{_kf6_qtplugindir}/kf6/parts/konsolepart.so

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
