# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
Name:           aurorae
Summary:        Aurorae is a themeable window decoration for KWin
Version: 6.8.3
Release:        3%{?dist}
License:        GPL-2.0-or-later AND MIT AND CC0-1.0
URL:            https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig


BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-cmake-modules

BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires: qt6-qttools-devel >= 6.11

BuildRequires: sonic-frameworks-color-scheme-devel
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: sonic-frameworks-settings-utils-devel
BuildRequires: sonic-frameworks-addons-downloader-devel
BuildRequires: sonic-frameworks-package-devel
BuildRequires: sonic-frameworks-svg-devel
BuildRequires: sonic-frameworks-windowsystem-devel

BuildRequires: sonic-decoration-devel

# Account for being split out of kwin
Conflicts:     kwin < 6.3.90
Supplements:   kwin%{?_isa} >= %{version}

%description
Aurorae is a themeable window decoration for KWin.
It supports theme files consisting of several SVG files for
decoration and buttons. Themes can be installed and selected
directly in the configuration module of KWin decorations.
Please have a look at theme-description on how to write a theme file.

%package devel
Summary: Development libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS TODO
%license LICENSES/*
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_auroraedecoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.so
%{_kf6_qmldir}/org/kde/kwin/decoration/AppMenuButton.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/ButtonGroup.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/decorationplugin.qmltypes
%{_kf6_qmldir}/org/kde/kwin/decoration/Decoration.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/DecorationButton.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/MenuButton.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/kde-qmlmodule.version
%{_kf6_qmldir}/org/kde/kwin/decoration/libdecorationplugin.so
%{_kf6_qmldir}/org/kde/kwin/decoration/qmldir
%{_kf6_qmldir}/org/kde/kwin/decorations/plastik/libplastikplugin.so
%{_kf6_qmldir}/org/kde/kwin/decorations/plastik/qmldir
%{_libexecdir}/plasma-apply-aurorae
%{_kf6_datadir}/knsrcfiles/aurorae.knsrc
%{_kf6_datadir}/kwin/aurorae/
%{_kf6_datadir}/kwin/decorations/kwin4_decoration_qml_plastik/
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.v2.so

%files devel
%{_kf6_libdir}/cmake/Aurorae/

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.3-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.3-2
- Pin cmake() BuildRequires to SonicDE package names so the
  alma+epel-10 solver cannot pick EPEL's Qt 6.10-linked providers
* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 6.8.3-1
- 6.8.3

* Mon Aug 31 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- Rebuilt aurorae 6.7.4 for SonicDE on Enterprise Linux 10
