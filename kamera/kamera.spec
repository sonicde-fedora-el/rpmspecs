
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kamera
Summary: Digital camera support for KDE 
Version: 26.04.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://www.kde.org/applications/graphics/
Source0: kamera-%{version}.tar.xz

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6DocTools)

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
* Thu Aug 27 2026 SonicDE <dev@sonicde.org> - 26.04.3-1
- Update to 26.04.3
- Change Requires from kde-cli-tools to sonic-terminal-tools

* Sun Mar 08 2026 Steve Cossette <farchord@gmail.com> - 25.12.3-1
- 25.12.3
