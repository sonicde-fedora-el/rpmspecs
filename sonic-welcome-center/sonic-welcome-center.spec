# Generated for SonicDE from Fedora's plasma-welcome.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-welcome-center fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-welcome-center
# Upstream KDE project: plasma-welcome
%global oldname plasma-welcome

%global orgname org.kde.plasma-welcome

#Name:           plasma-welcome
Name:           sonic-welcome-center
Version:        6.7.4.1
Release:        1%{?dist}
License:        GPL-2.0-or-later and BSD-3-Clause
Summary:        Plasma Welcome
Url:            https://invent.kde.org/plasma/%{name}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

# Upstream patches

BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6Crash)

BuildRequires:  cmake(Plasma)

Requires:       sonic-frameworks-user-feedback

Provides:       plasma-welcome-app = %{version}-%{release}
Obsoletes:      plasma-welcome-app < 5.27.0-2

Provides:       plasma-welcome = %{version}-%{release}
Conflicts:      plasma-welcome < %{version}-%{release}

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
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{orgname}.desktop

%files -f %{name}.lang
%license LICENSES/{BSD-3-Clause.txt,GPL-2.0-or-later.txt,FSFAP.txt}
%doc README.md
%{_kf6_bindir}/plasma-welcome
%{_kf6_datadir}/applications/%{orgname}.desktop
%{_kf6_metainfodir}/%{orgname}.*.xml
%{_kf6_plugindir}/kded/kded_plasma_welcome.so
%{_kf6_qmldir}/org/kde/plasma/welcome/
%{_kf6_datadir}/qlogging-categories6/welcome.categories

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
