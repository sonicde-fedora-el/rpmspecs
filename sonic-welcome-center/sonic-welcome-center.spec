# Generated for SonicDE from Fedora's plasma-welcome.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-welcome-center fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-welcome-center
# Upstream KDE project: plasma-welcome
%global oldname plasma-welcome

%global orgname org.kde.plasma-welcome

#Name:           plasma-welcome
Name:           sonic-welcome-center
Version:        6.8.2
Release:        4%{?dist}
License:        GPL-2.0-or-later and BSD-3-Clause
Summary:        Plasma Welcome
Url:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

# Upstream patches

BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtsvg-devel >= 6.11

BuildRequires:  sonic-frameworks-quick-ui-devel
BuildRequires:  sonic-frameworks-quick-ui-addons-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-addons-downloader-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-app-info-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-svg-devel
BuildRequires:  sonic-frameworks-keybind-devel
BuildRequires:  sonic-frameworks-crash-handler-devel

BuildRequires:  sonic-interface-libraries-devel

Requires:       sonic-frameworks-user-feedback

Provides:       plasma-welcome-app = %{version}-%{release}
Provides:       plasma-welcome-app%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-welcome-app
Obsoletes:      plasma-welcome

Provides:       plasma-welcome = %{version}-%{release}
Provides:       plasma-welcome%{?_isa} = %{version}-%{release}
%description
A Friendly onboarding wizard for Plasma.

%prep
%autosetup -p1 -n %{reponame}-%{version}
# It is for generate pot file for translate so we can ignore it.
rm Messages.sh

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{oldname} --all-name --with-html
rm -fv %{buildroot}%{_kf6_libdir}/libplasma-welcome-publicplugin.a
%check
# commented out until upstream fixes duplicate entries
#appstream-util validate-relax --nonet %%{buildroot}%%{_kf6_metainfodir}/%%{orgname}.*.xml

%files -f %{oldname}.lang
%license LICENSES/{BSD-3-Clause.txt,GPL-2.0-or-later.txt,FSFAP.txt}
%doc README.md
%{_kf6_bindir}/plasma-welcome
%{_kf6_datadir}/applications/%{orgname}.desktop
%{_kf6_metainfodir}/%{orgname}.*.xml
%{_kf6_plugindir}/kded/kded_plasma_welcome.so
%{_kf6_qmldir}/org/kde/plasma/welcome/
%{_kf6_datadir}/qlogging-categories6/welcome.categories

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
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
