# Generated for SonicDE from Fedora's kde-cli-tools.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-terminal-tools fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-terminal-tools
# Upstream KDE project: kde-cli-tools
%global oldname kde-cli-tools

#Name:    kde-cli-tools
Name:           sonic-terminal-tools
Version:        6.8.2
Release:        3%{?dist}

Summary: Tools based on KDE Frameworks 5 to better interact with the system

License: Artistic-2.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

## upstream patches

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  qt6-qtsvg-devel >= 6.11

BuildRequires:  sonic-rpm-macros

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-settings-utils-devel
BuildRequires:  sonic-frameworks-root-shell-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-ui-components-devel
BuildRequires:  sonic-frameworks-xml-gui-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-workspace-devel >= %{version}
Requires:       sonic-workspace-libs%{?_isa} >= %{version}

# upgrade path, from when this wasn't split out
Requires:       kdesu >= 1:%{version}

# unversioned utilitized landed here in 5.23.90, see also
# https://phabricator.kde.org/T14763
# https://invent.kde.org/plasma/kde-cli-tools/-/merge_requests/23
Conflicts: kde-runtime < 17.08.3-23

Provides:       kde-cli-tools = %{version}-%{release}
Provides:       kde-cli-tools%{?_isa} = %{version}-%{release}
Obsoletes:      kde-cli-tools

%description
Provides several KDE and Plasma specific command line tools to allow
better interaction with the system.

%package -n kdesu
Summary: Runs a program with elevated privileges
Epoch: 1
Conflicts: kde-runtime < 14.12.3-2
Conflicts: kde-runtime-docs < 14.12.3-2
Obsoletes:      kdesu < 1:6.7.4-2.el10
%description -n kdesu
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang kdeclitools_qt --with-qt --with-kde --all-name

ln -s %{_kf6_libexecdir}/kdesu %{buildroot}%{_bindir}/kdesu


%files -f kdeclitools_qt.lang
%{_bindir}/kbroadcastnotification
%{_bindir}/kdecp
%{_bindir}/kdecp5
%{_bindir}/kde-inhibit
%{_bindir}/kdemv
%{_bindir}/kdemv5
%{_bindir}/kde-open
%{_bindir}/kde-open5
%{_bindir}/keditfiletype
%{_bindir}/keditfiletype5
%{_bindir}/kinfo
%{_bindir}/kioclient
%{_bindir}/kioclient5
%{_bindir}/kmimetypefinder
%{_bindir}/kmimetypefinder5
%{_bindir}/kstart
%{_bindir}/kstart5
%{_bindir}/ksvgtopng
%{_bindir}/ksvgtopng5
%{_bindir}/plasma-open-settings
%{_kf6_libexecdir}/kdeeject
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so
%{_datadir}/doc/HTML/*/kcontrol6
%{_datadir}/applications/org.kde.keditfiletype.desktop
%{_datadir}/applications/org.kde.plasma.settings.open.desktop
%{_datadir}/applications/kcm_filetypes.desktop
%{_datadir}/zsh/site-functions/_kde-inhibit

%files -n kdesu
%{_bindir}/kdesu
%{_kf6_libexecdir}/kdesu
%{_mandir}/man1/kdesu.1.gz
%{_mandir}/*/man1/kdesu.1.gz
## FIXME: %%lang'ify
%{_datadir}/doc/HTML/*/kdesu

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
