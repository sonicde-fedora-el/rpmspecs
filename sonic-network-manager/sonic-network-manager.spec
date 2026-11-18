# Generated for SonicDE from Fedora's plasma-nm.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-network-manager fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-network-manager
# Upstream KDE project: plasma-nm
%global oldname plasma-nm


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-nm
Name:           sonic-network-manager
Summary: Plasma for managing network connections
Version:        6.8.2
Release:        4%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig


%ifarch %{qt6_qtwebengine_arches}
%bcond openconnect 1
%else
%bcond openconnect 0
%endif

## upstream patches


BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  gettext

BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Keychain)

BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-app-info-devel
BuildRequires:  sonic-frameworks-autocomplete-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-keyring-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-device-integration-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-networkmanager-devel
BuildRequires:  sonic-frameworks-modemmanager-devel
BuildRequires:  sonic-frameworks-svg-devel
BuildRequires:  sonic-frameworks-quick-charts-devel
# For some reason, it's not pulling it up on s390x
BuildRequires:  pkgconfig(libcrypto)

# Plasma
BuildRequires:  sonic-interface-libraries-devel

# Others
BuildRequires:  pkgconfig(cups)

# Runtime check
BuildRequires:  sonic-frameworks-barcode-devel
BuildRequires:  sonic-frameworks-quick-ui-devel
BuildRequires:  qt6qml(org.kde.kirigamiaddons.formcard)
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)

BuildRequires:  pkgconfig(ModemManager) >= 1.0.0
BuildRequires:  pkgconfig(libnm) >= 1.0.0
BuildRequires:  pkgconfig(mobile-broadband-provider-info)

%if %{with openconnect}
BuildRequires:  pkgconfig(openconnect) >= 4.00
BuildRequires:  qt6-qtwebengine-devel >= 6.11
%else
Obsoletes:      %{name}-openconnect < %{version}-%{release}
%endif

Requires:       NetworkManager >= 1.0.0
Requires:       sonic-frameworks-barcode
Requires:       sonic-frameworks-quick-ui

Obsoletes:      kde-plasma-networkmanagement < 1:0.9.1.0
Obsoletes:      kde-plasma-networkmanagement-libs < 1:0.9.1.0
Obsoletes:      kde-plasma-nm
Provides:       kde-plasma-nm = %{version}-%{release}

Provides:       plasma-nm = %{version}-%{release}
Provides:       plasma-nm%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm

%description
Plasma applet and editor for managing your network connections in KDE 4 using
the default NetworkManager service.


%package        openvpn
Summary:        OpenVPN support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-openvpn
Obsoletes:      kde-plasma-networkmanagement-openvpn < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-openvpn
Provides:       kde-plasma-nm-openvpn = %{version}-%{release}
Provides:       plasma-nm-openvpn = %{version}-%{release}
Provides:       plasma-nm-openvpn%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-openvpn

%description    openvpn
%{summary}.

%if %{with openconnect}
%package        openconnect
Summary:        OpenConnect support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-openconnect
Obsoletes:      kde-plasma-networkmanagement-openconnect < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-openconnect
Provides:       kde-plasma-nm-openconnect = %{version}-%{release}
Provides:       deprecated()
Provides:       plasma-nm-openconnect = %{version}-%{release}
Provides:       plasma-nm-openconnect%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-openconnect

%description    openconnect
%{summary}.
%endif

%package        openswan
Summary:        Openswan support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-openswan
Obsoletes:      kde-plasma-nm-openswan
Provides:       kde-plasma-nm-openswan = %{version}-%{release}
Provides:       plasma-nm-openswan = %{version}-%{release}
Provides:       plasma-nm-openswan%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-openswan

%description    openswan
%{summary}.

%package        strongswan
Summary:        Strongswan support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       strongswan
Obsoletes:      kde-plasma-nm-strongswan
Provides:       kde-plasma-nm-strongswan = %{version}-%{release}
Provides:       plasma-nm-strongswan = %{version}-%{release}
Provides:       plasma-nm-strongswan%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-strongswan

%description    strongswan
%{summary}.

%package        l2tp
Summary:        L2TP support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-l2tp
Obsoletes:      kde-plasma-nm-l2tp
Provides:       kde-plasma-nm-l2tp = %{version}-%{release}
Provides:       plasma-nm-l2tp = %{version}-%{release}
Provides:       plasma-nm-l2tp%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-l2tp

%description    l2tp
%{summary}.

%package        pptp
Summary:        PPTP support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-pptp
Obsoletes:      kde-plasma-networkmanagement-pptp < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-pptp
Provides:       kde-plasma-nm-pptp = %{version}-%{release}
Provides:       plasma-nm-pptp = %{version}-%{release}
Provides:       plasma-nm-pptp%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-pptp

%description    pptp
%{summary}.

%if 0%{?fedora}
%package        sstp
Summary:        SSTP support for %{name}
Requires:       NetworkManager-sstp
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       plasma-nm-sstp = %{version}-%{release}
Provides:       plasma-nm-sstp%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-sstp

%description    sstp
%{summary}.

%package        fortisslvpn
Summary:        Fortigate SSL VPN support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-fortisslvpn
Provides:       plasma-nm-fortisslvpn = %{version}-%{release}
Provides:       plasma-nm-fortisslvpn%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-fortisslvpn

%description    fortisslvpn
%{summary}.
%endif

%if 0%{?fedora}
%package        vpnc
Summary:        Vpnc support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-vpnc
Obsoletes:      kde-plasma-networkmanagement-vpnc < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-vpnc
Provides:       kde-plasma-nm-vpnc = %{version}-%{release}
Provides:       plasma-nm-vpnc = %{version}-%{release}
Provides:       plasma-nm-vpnc%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-vpnc

%description    vpnc
%{summary}.

%package        ssh
Summary:        SSH suppor for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-ssh
Provides:       plasma-nm-ssh = %{version}-%{release}
Provides:       plasma-nm-ssh%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-ssh

%description    ssh
%{summary}.

%package        iodine
Summary:        Iodine support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-iodine
Provides:       plasma-nm-iodine = %{version}-%{release}
Provides:       plasma-nm-iodine%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-nm-iodine

%description    iodine
%{summary}.
%endif

%prep
%autosetup -p1 -n %{reponame}-%{version}
sed -i 's/Qt6Keychain 0.16.0/Qt6Keychain/' CMakeLists.txt


%build
%cmake_kf6 \
  %{!?with_openconnect:-DBUILD_OPENCONNECT=OFF} \
  %{nil}

%cmake_build


%install
%cmake_install

%if ! 0%{?fedora}
rm -f %{buildroot}%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_vpncui.so
rm -f %{buildroot}%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_sshui.so
rm -f %{buildroot}%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_iodineui.so
rm -f %{buildroot}%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_sstpui.so
rm -f %{buildroot}%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_iodineui.mo
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_sshui.mo
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_vpncui.mo 
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_sstpui.mo
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_fortisslvpnui.mo
%endif
%if %{without openconnect}
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_openconnectui.mo
%endif

%find_lang plasma_applet_org.kde.plasma.networkmanagement
%find_lang plasmanetworkmanagement-kded
%find_lang plasmanetworkmanagement-kcm
%find_lang plasmanetworkmanagement-libs
%find_lang plasmanetworkmanagement_openvpnui
%find_lang kcm_cellular_network
%find_lang kcm_mobile_hotspot
%find_lang kcm_mobile_wifi
%find_lang kcm_mobile_wired
%if %{with openconnect}
%find_lang plasmanetworkmanagement_openconnectui
%endif
%find_lang plasmanetworkmanagement_libreswanui
%find_lang plasmanetworkmanagement_strongswanui
%find_lang plasmanetworkmanagement_l2tpui
%find_lang plasmanetworkmanagement_pptpui
%if 0%{?fedora}
%find_lang plasmanetworkmanagement_sstpui
%find_lang plasmanetworkmanagement_fortisslvpnui
%find_lang plasmanetworkmanagement_vpncui
%find_lang plasmanetworkmanagement_sshui
%find_lang plasmanetworkmanagement_iodineui
%endif


%files -f plasma_applet_org.kde.plasma.networkmanagement.lang -f plasmanetworkmanagement-kded.lang -f plasmanetworkmanagement-libs.lang -f plasmanetworkmanagement-kcm.lang -f kcm_cellular_network.lang -f kcm_mobile_wifi.lang -f kcm_mobile_hotspot.lang -f kcm_mobile_wired.lang
%{_libdir}/libplasmanm_internal.so
%{_libdir}/libplasmanm_editor.so
# plasma-nm applet
%{_qt6_qmldir}/org/kde/plasma/networkmanagement/
%{_kf6_qtplugindir}/plasma/applets/org.kde.plasma.networkmanagement.so
%{_datadir}/qlogging-categories6/plasma-nm.categories
# plasma-nm notifications
%{_kf6_datadir}/knotifications6/networkmanagement.notifyrc
# plasma-nm kded
%{_kf6_plugindir}/kded/networkmanagement.so
%{_libdir}/libplasmanm_cellular.so

# kcm
%{_qt6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_networkmanagement.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_cellular_network.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_hotspot.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_wifi.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_wired.so
%{_datadir}/kcm_networkmanagement/qml/
%{_kf6_datadir}/applications/kcm_networkmanagement.desktop
%{_kf6_datadir}/applications/org.kde.vpnimport.desktop
%{_kf6_datadir}/applications/kcm_cellular_network.desktop
%{_kf6_datadir}/applications/kcm_mobile_hotspot.desktop
%{_kf6_datadir}/applications/kcm_mobile_wifi.desktop
%{_kf6_datadir}/applications/kcm_mobile_wired.desktop


%files openvpn -f plasmanetworkmanagement_openvpnui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openvpnui.so

%if %{with openconnect}
%files openconnect -f plasmanetworkmanagement_openconnectui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_anyconnect.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_globalprotectui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_juniperui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_pulseui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_arrayui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_f5ui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_fortinetui.so
%endif

%files openswan -f plasmanetworkmanagement_libreswanui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_libreswanui.so

%files strongswan -f plasmanetworkmanagement_strongswanui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so

%files l2tp -f plasmanetworkmanagement_l2tpui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so

%files pptp -f plasmanetworkmanagement_pptpui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_pptpui.so

%if 0%{?fedora}
%files sstp -f plasmanetworkmanagement_sstpui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_sstpui.so

%files fortisslvpn -f plasmanetworkmanagement_fortisslvpnui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so

%files vpnc -f plasmanetworkmanagement_vpncui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_vpncui.so

%files ssh -f plasmanetworkmanagement_sshui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_sshui.so

%files iodine -f plasmanetworkmanagement_iodineui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_iodineui.so
%endif

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-4
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Pin Plasma cmake deps to SonicDE providers (Fedora libplasma 6.8.3 outranks ours)
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
