%global debug_package %{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdegraphics-thumbnailers
Summary: Thumbnailers for various graphic types
Version: 26.04.3
Release: 1%{?dist}

# most sources GPLv2+, dscparse.* GPL, gscreator.* LGPLv2+,
License: GPL-2.0-or-later
URL:     https://www.kde.org/applications/graphics/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KExiv2Qt6)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(QMobipocket6)
BuildRequires: cmake(Qt6Gui)
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
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
