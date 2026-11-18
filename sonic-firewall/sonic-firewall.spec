# Generated for SonicDE from Fedora's plasma-firewall.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-firewall fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
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
Version:        6.8.2
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
BuildRequires: systemd-rpm-macros
BuildRequires: sonic-frameworks-settings-utils-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-init-info-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: sonic-frameworks-logging-devel
BuildRequires: sonic-frameworks-ipc-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
%if %{with backend_ufw}
BuildRequires: ufw
%endif

BuildRequires: qt6-qtbase-devel >= 6.11
# Owns KCM directories
Requires: sonic-frameworks-settings-utils%{?_isa}

Requires: %{name}-backend = %{version}-%{release}
Suggests: %{name}-firewalld

Provides:       plasma-firewall = %{version}-%{release}
Provides:       plasma-firewall%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-firewall

%description
%{summary}.

%package firewalld
Summary: FirewallD backend for Plasma Firewall
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-backend = %{version}-%{release}
Conflicts: %{name}-backend
Requires: firewalld

Provides:       plasma-firewall-firewalld = %{version}-%{release}
Provides:       plasma-firewall-firewalld%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-firewall-firewalld

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

Provides:       plasma-firewall-ufw = %{version}-%{release}
Provides:       plasma-firewall-ufw%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-firewall-ufw

%description ufw
This package provides the backend code for Plasma Firewall
to interface with the Uncomplicated Firewall (UFW).
%endif


%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 %{!?with_backend_ufw:-DBUILD_UFW_BACKEND=OFF} \
  -DMANUAL_INITS=ON -DSYSTEMD_FOUND=ON
%cmake_build

%install
%cmake_install
%find_lang %{oldname} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml || :
desktop-file-validate %{buildroot}%{_datadir}/applications/kcm_firewall.desktop

%post
%systemd_post sonic-firewall-service.service

%preun
%systemd_preun sonic-firewall-service.service

%postun
%systemd_postun_with_restart sonic-firewall-service.service

%files -f %{oldname}.lang
%license LICENSES/*.txt
%{_libdir}/libkcm_firewall_core.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_firewall.so
%dir %{_qt6_plugindir}/kf6/plasma_firewall
%{_datadir}/applications/kcm_firewall.desktop
%{_metainfodir}/org.kde.plasma.firewall.metainfo.xml
%{_unitdir}/sonic-firewall-service.service
%{_libexecdir}/sonic-firewall-service
%{_kf6_libexecdir}/kauth/kcm_firewall_service_helper
%{_datadir}/dbus-1/system-services/org.sonicde.firewall.servicehelper.service
%{_datadir}/dbus-1/system.d/org.sonicde.firewall.servicehelper.conf
%{_datadir}/polkit-1/actions/org.sonicde.firewall.servicehelper.policy

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
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
