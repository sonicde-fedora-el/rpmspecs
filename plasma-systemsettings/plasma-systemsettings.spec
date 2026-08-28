%global  base_name systemsettings

Name:    plasma-%{base_name}
Summary: KDE System Settings application
Version:        6.7.4
Release:        2%{?dist}

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{base_name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: desktop-file-utils

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6JobWidgets)

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(PlasmaActivities)

BuildRequires: cmake(KF6Kirigami2)
Requires:      kf6-kirigami2%{?_isa}

# https://bugzilla.redhat.com/show_bug.cgi?id=1268493
# doc/HTML/en/systemsettings conflicts
Conflicts: kde-workspace < 5.0

# /usr/share/kservices5/settings-system-administration.desktop file conflict
Conflicts: kcm_systemd < 1.2.1-15

Provides:  plasma-systemsettings-devel = %{version}-%{release}
Obsoletes: plasma-systemsettings-devel < 5.20.90

%description
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang systemsettings6 --with-qt --with-html --all-name


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kdesystemsettings.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/systemsettings.desktop


%files -f systemsettings6.lang
%license LICENSES/*
%{_bindir}/systemsettings
%{_datadir}/systemsettings/
%{_datadir}/applications/kdesystemsettings.desktop
%{_datadir}/applications/systemsettings.desktop
%{_datadir}/metainfo/org.kde.systemsettings.metainfo.xml
%{_datadir}/zsh/site-functions/_systemsettings
%{_kf6_datadir}/kglobalaccel/systemsettings.desktop
%{_kf6_datadir}/qlogging-categories6/systemsettings.categories
%{_kf6_plugindir}/krunner/krunner_systemsettings.so

%changelog
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-2
- SonicDE build for Enterprise Linux 10

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 6.6.4-1
- 6.6.4
