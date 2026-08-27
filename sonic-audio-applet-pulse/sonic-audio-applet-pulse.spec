# Generated for SonicDE from Fedora's plasma-pa.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-audio-applet-pulse fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-audio-applet-pulse
# Upstream KDE project: plasma-pa
%global oldname plasma-pa


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-pa
Name:           sonic-audio-applet-pulse
Version:        6.7.4
Release:        3%{?dist}
Summary: Plasma applet for audio volume management using PulseAudio

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6PulseAudioQt)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6StatusNotifierItem)

BuildRequires:  cmake(Plasma)

BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  qt6-qtbase-devel

BuildRequires:  perl-generators

# runtime
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6ItemModels)
Requires: sonic-frameworks-quick-ui
Requires: sonic-frameworks-quick-ui-addons
Requires: sonic-frameworks-data-models

Requires: pulseaudio-daemon


Provides:       plasma-pa%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-pa < %{version}-%{release}

%description
%{summary}.


%prep
%autosetup -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{oldname} --all-name --with-html
# Not clear why we would need this. Deleting
rm -fv %{buildroot}%{_kf6_libdir}/libplasma-volume.so


%files -f %{oldname}.lang
%license LICENSES/*
%{_kf6_qmldir}/org/kde/plasma/private/volume/
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_pulseaudio.so
%{_kf6_qtplugindir}/kf6/kded/audioshortcutsservice.so
%{_kf6_qtplugindir}/plasma/applets/org.kde.plasma.volume.so
%{_kf6_datadir}/applications/kcm_pulseaudio.desktop
%{_kf6_libdir}/libplasma-volume.so.6
%{_kf6_libdir}/libplasma-volume.so.%{version}
%{_kf6_datadir}/qlogging-categories6/plasmapa.categories

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
