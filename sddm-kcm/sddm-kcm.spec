# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    sddm-kcm
Version: 6.7.4
Release: 2%{?dist}
Summary: SDDM KDE configuration module

License: GPL-2.0-or-later AND GPL-3.0-only AND CC0-1.0 AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-image-devel

Requires:       sddm


%description
This is a System Settings configuration module for configuring the
SDDM Display Manager

%prep
%autosetup


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang kcmsddm6_qt --with-qt --all-name


%files -f kcmsddm6_qt.lang
%license LICENSES/*
%{_kf6_bindir}/sddmthemeinstaller
%{_kf6_datadir}/applications/kcm_sddm.desktop
%{_kf6_libexecdir}/kauth/kcmsddm_authhelper
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmsddm.conf
%{_datadir}/knsrcfiles/sddmtheme.knsrc
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_sddm.so

%changelog
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-2
- SonicDE build for Enterprise Linux 10

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 6.6.4-1
- 6.6.4
