# Generated for SonicDE from Fedora's plasma-firewall.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-firewall fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-firewall
# Upstream KDE project: plasma-firewall
%global oldname plasma-firewall

# Disable ufw for RHEL
# TODO: Consider dropping it for Fedora too
# Cf. https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GNC2UEHAE7VVSN6K24GBJYSIUNCLKJ6L/
%bcond backend_ufw %[%{undefined rhel}]


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-firewall
Name:           sonic-firewall
Version:        6.7.4
Release:        3%{?dist}
Summary: Control Panel for your system firewall

License: BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: qt6-qtbase-devel

# Owns KCM directories
Requires: sonic-frameworks-settings-utils%{?_isa}

Requires: %{name}-backend = %{version}-%{release}
Suggests: %{name}-firewalld

Provides:       plasma-firewall%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-firewall < %{version}-%{release}

%description
%{summary}.

%package firewalld
Summary: FirewallD backend for Plasma Firewall
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-backend = %{version}-%{release}
Conflicts: %{name}-backend
Requires: firewalld

Provides:       plasma-firewall-firewalld%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-firewall-firewalld < %{version}-%{release}

%description firewalld
This package provides the backend code for Plasma Firewall
to interface with FirewallD.

%if %{with backend_ufw}
%package ufw
Summary: UFW backend for Plasma Firewall
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-backend = %{version}-%{release}
Conflicts: %{name}-backend
Requires: ufw
# For dbus directories
Requires: dbus-common
# For polkit directories
Requires: polkit

Provides:       plasma-firewall-ufw%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-firewall-ufw < %{version}-%{release}

%description ufw
This package provides the backend code for Plasma Firewall
to interface with the Uncomplicated Firewall (UFW).
%endif


%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 %{!?with_backend_ufw:-DBUILD_UFW_BACKEND=OFF}
%cmake_build

%install
%cmake_install
%find_lang %{oldname} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml || :
desktop-file-validate %{buildroot}%{_datadir}/applications/kcm_firewall.desktop

%files -f %{oldname}.lang
%license LICENSES/*.txt
%{_libdir}/libkcm_firewall_core.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_firewall.so
%dir %{_qt6_plugindir}/kf6/plasma_firewall
%{_datadir}/applications/kcm_firewall.desktop
%{_metainfodir}/org.kde.plasma.firewall.metainfo.xml

%files firewalld
%{_qt6_plugindir}/kf6/plasma_firewall/firewalldbackend.so

%if %{with backend_ufw}
%files ufw
%{_qt6_plugindir}/kf6/plasma_firewall/ufwbackend.so
%{_libexecdir}/kde_ufw_plugin_helper.py
%{_kf6_libexecdir}/kauth/kde_ufw_plugin_helper
%{_datadir}/dbus-1/system-services/org.kde.ufw.service
%{_datadir}/dbus-1/system.d/org.kde.ufw.conf
%dir %{_datadir}/kcm_ufw
%{_datadir}/kcm_ufw/defaults
%{_datadir}/polkit-1/actions/org.kde.ufw.policy
%endif

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
