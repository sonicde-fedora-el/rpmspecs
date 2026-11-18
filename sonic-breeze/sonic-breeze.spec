# Generated for SonicDE from Fedora's plasma-breeze.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-breeze fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-breeze
# Upstream KDE project: breeze
%global oldname plasma-breeze

%global  base_name breeze
# SonicDE is a Qt6/KF6-only hard fork; no KF5 packages are shipped.
%bcond_with kf5

#Name:    plasma-breeze
Name:           sonic-breeze
Version:        6.8.2
Release:        7%{?dist}
Summary: Artwork, styles and assets for the Breeze visual style for the Plasma Desktop

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
#URL:     https://invent.kde.org/plasma/%%{base_name}.git
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz.sig
Source2:        normalize-hidpi-layout.py
Source3:        test_normalize_hidpi_layout.py

# Upstream Patches

# Use font metrics to only inset where the text can spare it
# https://invent.kde.org/plasma/breeze/-/commit/a74ad95349ec913f1042f5390dbd95a8341aea06
Patch0:         a74ad95349ec913f1042f5390dbd95a8341aea06.patch

# Misc
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  gettext
BuildRequires:  python3

%if %{with kf5}
# Qt5
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5WindowSystem)

BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)

Requires:       (%{name}-qt5 if qt5-qtbase-gui)
%endif

# Qt6
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-decoration-devel
BuildRequires:  sonic-frameworks-color-scheme-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-qt-integration-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-quick-ui-devel
BuildRequires:  sonic-frameworks-windowsystem-devel

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtsvg-devel >= 6.11

Requires:       %{name}-qt6

# since we provide a cmake dev-like file
Provides:       %{name}-devel = %{version}-%{release}

Provides:       plasma-breeze = %{version}-%{release}
Provides:       plasma-breeze%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-breeze

%description
%{summary}.


%package        qt6
Summary:        Breeze application style for Qt6
Requires:       %{name}-common = %{version}-%{release}
Provides:       plasma-breeze-qt6 = %{version}-%{release}
Provides:       plasma-breeze-qt6%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-breeze-qt6

%description    qt6
%{summary}.

%if %{with kf5}
%package        qt5
Summary:        Breeze application style for Qt5
Requires:       %{name}-common = %{version}-%{release}
Provides:       plasma-breeze-qt5 = %{version}-%{release}
Provides:       plasma-breeze-qt5%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-breeze-qt5

%description    qt5
%{summary}.
%endif

%package        common
Summary:        Common files shared between Plasma 5 and Plasma 6 versions of the Breeze style
BuildArch:      noarch
Provides:       plasma-breeze-common = %{version}-%{release}
Provides:       plasma-breeze-common%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-breeze-common
# Breeze icon files moved from the old separate icon-theme package.
Obsoletes:      breeze-icon-theme < 6.31.0.1
Provides:       breeze-icon-theme = %{version}-%{release}
Provides:       breeze-icons = %{version}-%{release}

%description    common
%{summary}.

%package -n     breeze-cursor-theme
Summary:        Breeze cursor theme
BuildArch:      noarch
Obsoletes:      breeze-icon-theme < 5.17.0
Provides:       breeze-cursor-themes = %{version}-%{release}
%description -n breeze-cursor-theme
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
mkdir -p qt6build
pushd qt6build
%cmake_kf6 -S .. -DBUILD_QT6=ON -DBUILD_QT5=OFF
%cmake_build
popd

%if %{with kf5}
mkdir -p qt5build
pushd qt5build
%cmake_kf5 -S .. -DBUILD_QT6=OFF -DBUILD_QT5=ON
%cmake_build
popd
%endif


%install
%if %{with kf5}
pushd qt5build
%cmake_install
popd
%endif

pushd qt6build
%cmake_install
popd

python3 %{SOURCE2} %{buildroot}%{_datadir}/icons

%find_lang breeze --all-name


%check
python3 %{SOURCE3}


%files -f breeze.lang
%license LICENSES/*.txt
%{_bindir}/breeze-settings6
%{_kf6_datadir}/applications/breezestyleconfig.desktop
%{_kf6_datadir}/applications/kcm_breezedecoration.desktop
%dir %{_kf6_qtplugindir}/kstyle_config/
%{_kf6_qtplugindir}/kstyle_config/breezestyleconfig.so
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_breezedecoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.breeze.so
%{_libdir}/cmake/SonicBreeze/

%if %{with kf5}
%files qt5
%{_kf5_qtplugindir}/styles/breeze5.so
%endif

%files qt6
%{_kf6_qtplugindir}/styles/breeze6.so

%files common
%{_datadir}/color-schemes/*.colors
%{_datadir}/plasma/desktoptheme/
%{_datadir}/plasma/look-and-feel/
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/icons/hicolor/*/apps/breeze-settings.*
%{_datadir}/icons/breeze/
%{_datadir}/icons/breeze-dark/
%dir %{_datadir}/QtCurve/
%{_datadir}/QtCurve/Breeze.qtcurve
%{_datadir}/wallpapers/Next/

%files -n breeze-cursor-theme
%dir %{_kf6_datadir}/icons/Breeze_Light/
%{_kf6_datadir}/icons/Breeze_Light/cursors/
%{_kf6_datadir}/icons/Breeze_Light/cursors_scalable/
%{_kf6_datadir}/icons/Breeze_Light/index.theme
%dir %{_kf6_datadir}/icons/breeze_cursors/
%{_kf6_datadir}/icons/breeze_cursors/cursors/
%{_kf6_datadir}/icons/breeze_cursors/cursors_scalable/
%{_kf6_datadir}/icons/breeze_cursors/index.theme

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-7
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-6
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-5
- Pin cmake() BuildRequires to SonicDE package names so the
  alma+epel-10 solver cannot pick EPEL's Qt 6.10-linked providers
* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 6.8.2-4
- Replace content-identical HiDPI icon variant directories with the
  relative symlinks EL10 ships, verified by normalize-hidpi-layout.py
  before any replacement; unit tests run in %%check.

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 6.8.2-3
- sonic-breeze-common: provide breeze-icon-theme/breeze-icons at the
  real Sonic Breeze version; this package owns the actual Breeze theme
  files, while the Silver theme moved to sonic-silver-icon-theme.

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 6.8.2-2
- sonic-breeze-common: obsolete the old separate breeze-icon-theme
  package whose icon files moved into this package, so upgrades replace
  it instead of file-conflicting.

* Fri Sep 04 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.7-1
- Update to SonicDE 6.7.4.7

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.3-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
