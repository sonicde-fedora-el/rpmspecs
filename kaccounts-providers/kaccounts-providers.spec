%global sonicde_qt6_version 6.11.3
Name:    kaccounts-providers
Version: 26.08.3
Release: 2%{?dist}
Summary: Additional service providers for KAccounts framework
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://invent.kde.org/network/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
ExclusiveArch: x86_64 aarch64 riscv64 x86_64_v2

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  intltool
BuildRequires:  sonic-accounts-integration-qt6-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-io-devel

BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtwebengine-devel >= 6.11
BuildRequires:  qcoro-qt6-devel

Requires:       signon-ui

# google provider
Recommends:     signon-plugin-oauth2

# https://pagure.io/fedora-kde/SIG/issue/66
Supplements:    kaccounts-integration-qt6

# switched to arch'd pkg
Obsoletes: kaccounts-providers < 15.12.0

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name


%files -f %{name}.lang
%license LICENSES/*
%config %{_sysconfdir}/signon-ui/webkit-options.d/*
%{_datadir}/accounts/providers/kde/
%dir %{_kf6_datadir}/kpackage/genericqml
%{_kf6_datadir}/kpackage/genericqml/org.kde.kaccounts.owncloud/
%dir %{_qt6_plugindir}/kaccounts/
%dir %{_qt6_plugindir}/kaccounts/ui/
%{_qt6_plugindir}/kaccounts/ui/nextcloud_plugin_kaccounts.so
%{_datadir}/accounts/services/kde/
%{_qt6_plugindir}/kaccounts/ui/owncloud_plugin_kaccounts.so
%{_kf6_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/
%{_kf6_datadir}/icons/hicolor/*/*/*


%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Thu Aug 27 2026 SonicDE <dev@sonicde.org> - 26.04.3-1
- Update to 26.04.3
- Change BuildRequires to sonic-* packages
- Change signon-plugin-oauth2 from Requires to Recommends
  (SonicDE does not ship signon-plugin-oauth2 yet)

* Sun Mar 08 2026 Steve Cossette <farchord@gmail.com> - 25.12.3-1
- 25.12.3
