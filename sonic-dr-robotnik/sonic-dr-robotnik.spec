# Generated for SonicDE from Fedora's plasma-drkonqi.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-dr-robotnik fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-dr-robotnik
# Upstream KDE project: drkonqi
%global oldname plasma-drkonqi

%global base_name drkonqi


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#Name:    plasma-drkonqi
Name:           sonic-dr-robotnik
Summary: DrKonqi crash handler for KF6/Plasma6
Version:        6.8.2
Release:        3%{?dist}
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{base_name}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{base_name}-%%{version}.tar.xz.sig

## upstreamable Patches
# dnf debuginfo-install
Patch:          drkonqi-installdbgsymbols.patch

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-qml-bridge-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-app-info-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-progress-ui-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-keyring-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-idle-tracker-devel
BuildRequires:  sonic-frameworks-status-notification-devel
BuildRequires:  sonic-frameworks-syntax-highlighting-devel
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  systemd-devel
BuildRequires:  git-core

Requires:       sonic-frameworks-quick-ui
Requires:       sonic-frameworks-data-models
Requires:       sonic-frameworks-settings-utils
Requires:       python3dist(psutil)
Requires:       python3dist(pygdbmi)
Recommends:     python3dist(sentry-sdk)
Requires:       systemd-udev
Requires:       elfutils

# retired from plasma-workspace
Obsoletes:      plasma-workspace-drkonqi
Provides: plasma-workspace-drkonqi = %{version}-%{release}

%if (0%{?fedora} && 0%{?fedora} < 41) || (0%{?rhel} && 0%{?rhel} < 11)
Requires: (dnf-command(debuginfo-install) if dnf)
%endif
Requires: sonic-terminal
Requires: polkit


Provides:       plasma-drkonqi = %{version}-%{release}
Provides:       plasma-drkonqi%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-drkonqi

%description
%{summary}


%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 -DWITH_PYTHON_VENDORING=OFF -DWITH_GDB12=ON
%cmake_build

%install
%cmake_install
# installdbgsymbols script
install -p -D -m755 src/doc/examples/installdbgsymbols_fedora.sh \
    %{buildroot}%{_libexecdir}/installdbgsymbols.sh

%find_lang plasma-drkonqi --with-html --with-qt --all-name

%post
%systemd_user_post drkonqi-sentry-postman.service

%preun
%systemd_user_preun drkonqi-sentry-postman.service

%postun
%systemd_user_postun drkonqi-sentry-postman.service

%files -f plasma-drkonqi.lang
%license LICENSES/*
%{_bindir}/drkonqi-sentry-data
%{_libexecdir}/drkonqi
%{_libexecdir}/drkonqi-sentry-postman
%{_libexecdir}/installdbgsymbols.sh
%{_kf6_datadir}/drkonqi/
%{_kf6_datadir}/applications/org.kde.drkonqi.desktop
%{_kf6_datadir}/qlogging-categories6/drkonqi.categories
%{_userunitdir}/drkonqi-sentry-postman.*
%{_userunitdir}/default.target.wants/*
%{_userunitdir}/plasma-core.target.wants/drkonqi-*
%{_userunitdir}/timers.target.wants/drkonqi-*

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
