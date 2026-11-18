
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
Name:    kamera
Summary: Digital camera support for KDE 
Version: 26.08.3
Release: 2%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://www.kde.org/applications/graphics/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/kamera-%{version}.tar.xz

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qt5compat-devel >= 6.11

BuildRequires: sonic-frameworks-settings-ui-devel
BuildRequires: sonic-frameworks-xml-gui-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-settings-utils-devel
BuildRequires: sonic-frameworks-doctools-devel

BuildRequires: pkgconfig(libgphoto2)

Requires: sonic-terminal-tools

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kcm_%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml


%files -f %{name}.lang
%doc AUTHORS README
%license LICENSES/*.txt
%{_kf6_datadir}/applications/kcm_%{name}.desktop
%{_kf6_datadir}/solid/actions/solid_camera.desktop
%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_%{name}.so
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_kf6_plugindir}/kio/kio_%{name}.so


%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Thu Aug 27 2026 SonicDE <dev@sonicde.org> - 26.04.3-1
- Update to 26.04.3
- Change Requires from kde-cli-tools to sonic-terminal-tools

* Sun Mar 08 2026 Steve Cossette <farchord@gmail.com> - 25.12.3-1
- 25.12.3
