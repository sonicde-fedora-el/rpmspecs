%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdegraphics-thumbnailers
Summary: Thumbnailers for various graphic types
Version: 26.08.3
Release: 3%{?dist}

# most sources GPLv2+, dscparse.* GPL, gscreator.* LGPLv2+,
License: GPL-2.0-or-later
URL:     https://www.kde.org/applications/graphics/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-archive-devel
BuildRequires: sonic-exiv2-library-qt6-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: cmake(QMobipocket6)
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: cmake(KDcrawQt6)

%description
%{summary}.


%prep
%autosetup


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install


%files
%license COPYING*
%{_kf6_metainfodir}/org.kde.kdegraphics-thumbnailers.metainfo.xml
%{_kf6_qtplugindir}/kf6/thumbcreator/blenderthumbnail.so
%{_kf6_qtplugindir}/kf6/thumbcreator/gsthumbnail.so
%{_kf6_qtplugindir}/kf6/thumbcreator/mobithumbnail.so
%{_kf6_qtplugindir}/kf6/thumbcreator/rawthumbnail.so


%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Pin cmake() BuildRequires to SonicDE package names so the
  alma+epel-10 solver cannot pick EPEL's Qt 6.10-linked providers
* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
