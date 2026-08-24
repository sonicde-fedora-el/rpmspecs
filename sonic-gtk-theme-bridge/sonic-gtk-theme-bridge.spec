# Generated for SonicDE from Fedora's kde-gtk-config.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-gtk-theme-bridge fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-gtk-theme-bridge
# Upstream KDE project: kde-gtk-config
%global oldname kde-gtk-config


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    kde-gtk-config
Name:           sonic-gtk-theme-bridge
Summary: Configure the appearance of GTK apps in KDE
Version:        6.7.4
Release:        1%{?dist}

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/kde-gtk-config-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/kde-gtk-config-%%{version}.tar.xz.sig

# upstream patches

## upstreamable patches

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel

BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtk2-devel
BuildRequires:  sassc

# dir ownership
Requires:       sonic-silver-gtk-common
# need kcmshell5 from kde-cli-tools
Requires:       sonic-terminal-tools

# runtime dep checked-for at buildtime
BuildRequires:  xsettingsd
# avoid hard dep for now -- rex
Recommends:     xsettingsd

Provides:       kde-gtk-config = %{version}-%{release}
Conflicts:      kde-gtk-config < %{version}-%{release}

%description
This is a System Settings configuration module for configuring the
appearance of GTK apps in KDE.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*.txt
%{_libexecdir}/gtk3_preview
%{_libdir}/kconf_update_bin/gtk_theme
%{_datadir}/kconf_update/gtkconfig.upd
%{_datadir}/kconf_update/remove_window_decorations_from_gtk_css.sh
%{_libdir}/kconf_update_bin/remove_deprecated_gtk4_option_v2
%{_kf6_plugindir}/kded/gtkconfig.so
%{_libdir}/gtk-3.0/modules/libcolorreload-gtk-module.so
%{_libdir}/gtk-3.0/modules/libwindow-decorations-gtk-module.so
%{_datadir}/themes/Breeze/window_decorations.css
%{_datadir}/kcm-gtk-module/
%{_datadir}/qlogging-categories6/kde-gtk-config.categories

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
