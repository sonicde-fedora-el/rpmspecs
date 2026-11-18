# Generated for SonicDE from Fedora's plasma-sdk.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-theme-sdk fork, not from download.kde.org.
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-theme-sdk
# Upstream KDE project: plasma-sdk
%global oldname plasma-sdk

#Name:    plasma-sdk
Name:           sonic-theme-sdk
Summary:        Applications useful for SonicDE theme development
Version:        6.8.2
Release:        4%{?dist}

License: CC0-1.0 AND BSD-2-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL AND MIT
#URL:     https://invent.kde.org/plasma/%%{oldname}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{oldname}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtsvg-devel >= 6.11
BuildRequires:  qt6-qt5compat-devel >= 6.11

BuildRequires:  sonic-frameworks-archive-devel
BuildRequires:  sonic-frameworks-autocomplete-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-data-models-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-text-editor-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-svg-devel
BuildRequires:  sonic-frameworks-quick-ui-devel

BuildRequires:  sonic-interface-libraries-devel
BuildRequires:  sonic-interface-libraries-devel

Requires: kf6-filesystem >= 6.31

Provides:       plasma-sdk = %{version}-%{release}
Provides:       plasma-sdk%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-sdk
Conflicts:      plasma-sdk

%description
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html --all-name


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.iconexplorer.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.lookandfeelexplorer.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasmoidviewer.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.themeexplorer.desktop


%files -f %{name}.lang
%license LICENSES/*
%doc RELEASE-NOTES.md
%{_bindir}/iconexplorer
%{_bindir}/kqml
%{_bindir}/lookandfeelexplorer
%{_bindir}/plasmoidviewer
%{_bindir}/plasmathemeexplorer
%{_kf6_datadir}/applications/org.kde.iconexplorer.desktop
%{_kf6_datadir}/applications/org.kde.plasma.lookandfeelexplorer.desktop
%{_kf6_datadir}/applications/org.kde.plasmoidviewer.desktop
%{_kf6_datadir}/applications/org.kde.plasma.themeexplorer.desktop
%{_kf6_metainfodir}/org.kde.plasma.iconexplorer.appdata.xml
%{_kf6_metainfodir}/org.kde.plasmoidviewer.appdata.xml
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.iconexplorer.svg
%{_qt6_plugindir}/kf6/ktexteditor/iconexplorerplugin.so
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/
%{_mandir}/*/man1/kqml.1*
%{_mandir}/*/man1/plasmoidviewer.1*
%{_mandir}/man1/kqml.1*
%{_mandir}/man1/plasmoidviewer.1*
%{_datadir}/zsh/site-functions/_kqml
%{_datadir}/zsh/site-functions/_plasmoidviewer

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
* Wed Nov 11 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-1
- Initial SonicDE package for Enterprise Linux 10, renamed from plasma-sdk
