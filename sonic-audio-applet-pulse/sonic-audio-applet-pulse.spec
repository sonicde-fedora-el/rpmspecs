# Generated for SonicDE from Fedora's plasma-pa.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-audio-applet-pulse fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-audio-applet-pulse
# Upstream KDE project: plasma-pa
%global oldname plasma-pa


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-pa
Name:           sonic-audio-applet-pulse
Version:        6.8.2
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        4%{?dist}
Summary: Plasma applet for audio volume management using PulseAudio

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-keybind-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-package-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-pulseaudio-library-qt6-devel
BuildRequires:  sonic-frameworks-svg-devel
BuildRequires:  sonic-frameworks-status-notification-devel

BuildRequires:  sonic-interface-libraries-devel

BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  perl-generators

# runtime
BuildRequires: sonic-frameworks-quick-ui-devel
BuildRequires: sonic-frameworks-quick-ui-addons-devel
BuildRequires: sonic-frameworks-data-models-devel
Requires: sonic-frameworks-quick-ui
Requires: sonic-frameworks-quick-ui-addons
Requires: sonic-frameworks-data-models

Requires: pulseaudio-daemon


Provides:       plasma-pa = %{version}-%{release}
Provides:       plasma-pa%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-pa

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
%{_kf6_libdir}/libplasma-volume.so.%{libversion}
%{_kf6_datadir}/qlogging-categories6/plasmapa.categories

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-4
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Pin Plasma cmake deps to SonicDE providers (Fedora libplasma 6.8.3 outranks ours)
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
