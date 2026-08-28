Name:           plasma-keyboard
Epoch:          1
Version:        6.7.4
Release:        2%{?dist}
Summary:        Virtual Keyboard for Qt based desktops

License:        LGPL-2.1-only AND GPL-2.0-only AND CC0-1.0 AND LGPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-only
URL:            https://invent.kde.org/plasma/%{name}/

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6VirtualKeyboard)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  qt6-qtvirtualkeyboard-devel

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)

BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(PlasmaQuick)

Requires:       (kcm-%{name}%{?_isa} if plasma-systemsettings%{?_isa})

%description
The plasma-keyboard is a virtual keyboard
based on Qt Virtual Keyboard designed to
integrate in Plasma.

%package -n kcm-%{name}
Summary: KDE KCM for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description -n kcm-%{name}
%{summary}.

%prep
%autosetup -p1


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
%{_kf6_datadir}/applications/org.kde.plasma.keyboard.desktop
%{_kf6_qmldir}/QtQuick/VirtualKeyboard/
%{_kf6_qmldir}/org/kde/plasma/keyboard/
%{_kf6_datadir}/plasma/keyboard/
%{_kf6_metainfodir}/org.kde.plasma.keyboard.metainfo.xml

%files -n kcm-%{name} -f kcm_plasmakeyboard.lang
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plasmakeyboard.so
%{_datadir}/applications/kcm_plasmakeyboard.desktop

%changelog
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1:6.7.4-2
- SonicDE build for Enterprise Linux 10

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.4-1
- 6.6.4
