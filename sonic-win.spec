%define _disable_source_fetch 0
%define debug_package %{nil}

Name:           sonic-win
Version:        6.4.5
Release:        8%{?dist}
Summary:        KWin window manager for SonicDE (fork of kwin)

%global plasma_version %{version}

License:        GPL-2.0-or-later
URL:            https://github.com/Sonic-DE/sonic-win
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros

# Qt
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsensors-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Multimedia)

# X11/OpenGL
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libxcb-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXcursor-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libcap-devel

BuildRequires:  lcms2-devel
BuildRequires:  glib2-devel
BuildRequires:  pipewire-devel

# Wayland
BuildRequires:  wayland-devel >= 1.22.0
BuildRequires:  wayland-protocols-devel
BuildRequires:  pkgconfig(libinput) >= 0.10
BuildRequires:  pkgconfig(libudev)

%if 0%{?rhel} == 10
# Integrate with Xlibre on EL10
BuildRequires:  xlibre-xserver-devel
Requires:       xlibre-xserver-Xorg
Requires:       xlibre-xf86-input-libinput
%else
BuildRequires:  pkgconfig(xwayland)
%endif

# KF6
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Svg)

# Workspace components
BuildRequires:  cmake(KDecoration3)
BuildRequires:  kscreenlocker-devel
BuildRequires:  plasma-breeze-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  cmake(KGlobalAccelD)
BuildRequires:  libdisplay-info-devel

BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  libeis-devel
BuildRequires:  pkgconfig(libcanberra)

# Conflicts with kwin-x11
Conflicts:      kwin-x11

Requires:       sonic-interface-libraries%{?_isa} >= %{plasma_version}
Requires:       kscreenlocker%{?_isa}
Requires:       kf6-kirigami2%{?_isa}
Requires:       kf6-kdeclarative%{?_isa}
Requires:       qt6-qtmultimedia%{?_isa}
Requires:       qt6-qtdeclarative%{?_isa}

%description
Sonic Win is a fork of KWin, the window manager and compositor for SonicDE,
focusing on an optimized X11 experience.

%package        libs
Summary:        KWin libraries for SonicDE
Conflicts:      kwin-x11-libs

%description    libs
Shared libraries for sonic-win.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      kwin-x11-devel

%description    devel
Development files for sonic-win.
Provides:       kwin-devel = %{version}-%{release}
Provides:       kwin-x11-devel = %{version}-%{release}
Provides:       cmake(KWinDBusInterface) = %{version}

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
# Create compatibility CMake files for sonic-workspace
mkdir -p %{buildroot}%{_libdir}/cmake/KWinDBusInterface
cat <<EOF > %{buildroot}%{_libdir}/cmake/KWinDBusInterface/KWinDBusInterfaceConfig.cmake
find_package(KWinX11DBusInterface REQUIRED)
include(\${KWinX11DBusInterface_DIR}/KWinX11DBusInterfaceConfig.cmake)
EOF

# Create compatibility symlinks for DBus interfaces
pushd %{buildroot}%{_datadir}/dbus-1/interfaces/
for f in kwin_x11_*.xml; do
    newname=$(echo $f | sed 's/kwin_x11_//')
    ln -s "$f" "$newname"
done
popd

# The translation domain in the source is likely still 'kwin'
%find_lang kwin --all-name --with-html

%files -f kwin.lang
%license LICENSES/*
# Binares and specialized folders
%{_bindir}/kwin_x11
%{_libdir}/kconf_update_bin/kwin*
%{_libexecdir}/kwin*
%{_userunitdir}/plasma-kwin_x11.service

# Database and plugins
%{_libdir}/qt6/plugins/
%{_qt6_qmldir}/org/kde/*/

# Data and Assets
%{_datadir}/kwin-x11/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/icons/hicolor/*/apps/kwin-x11.*
%{_datadir}/kconf_update/kwin-x11.upd
%{_datadir}/knotifications6/kwin-x11.notifyrc
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/krunner/dbusplugins/*.desktop
%{_datadir}/qlogging-categories6/*.categories

%files libs
# Libraries
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/
%{_libdir}/lib*.so
%{_libdir}/cmake/

%changelog
* Wed Mar 21 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.4.5-8
- Initial release of SonicDE/KDE Plasma X11 for EL10 (Downgraded to 6.4.5 for EL 10.1 compatibility)
