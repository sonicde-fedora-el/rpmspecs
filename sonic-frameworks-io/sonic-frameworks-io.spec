# Generated for SonicDE from Fedora's kf6-kio.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-io fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-frameworks-io
# Upstream KDE project: kio
%global oldname kf6-kio

%global framework kio

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-io
Version:        6.31.0.1
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for filesystem abstraction

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

# https://invent.kde.org/frameworks/kio/-/issues/26
# I'm not sending this upstream because I'm not sure it's really
# exactly what upstream will want, but it solves the practical
# issue for us for now
Patch0:  0001-Give-the-kuriikwsfiltereng_private-a-VERSION-and-SOV.patch

%if 0%{?flatpak}
# Disable the help: and ghelp: protocol for Flatpak builds, to avoid depending
# on the docbook stack.
Patch101: kio-no-help-protocol.patch
%endif


BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake
BuildRequires:  sonic-frameworks-archive-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-device-integration-devel
BuildRequires:  switcheroo-control
BuildRequires:  sonic-frameworks-color-scheme-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-doctools-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-app-info-devel
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  sonic-frameworks-bookmarks-devel
BuildRequires:  sonic-frameworks-autocomplete-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-data-views-devel
BuildRequires:  sonic-frameworks-progress-ui-devel
BuildRequires:  sonic-frameworks-windowsystem-devel
BuildRequires:  sonic-frameworks-notifications-devel
BuildRequires:  sonic-frameworks-keyring-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  sonic-frameworks-xml-gui-devel

BuildRequires:  libacl-devel
%if !0%{?flatpak}
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
%endif
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  zlib-devel

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qttools-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11

BuildRequires:  sonic-daemon-devel
BuildRequires:  qt6-qt5compat-devel >= 6.11

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

Requires: sonic-daemon

Provides:       kf6-kio = %{version}-%{release}
Provides:       kf6-kio%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio

%description
KDE Frameworks 6 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       sonic-frameworks-bookmarks-devel
Requires:       sonic-frameworks-autocomplete-devel
Requires:       sonic-frameworks-settings-devel
Requires:       sonic-frameworks-core-addons-devel
Requires:       sonic-frameworks-data-views-devel
Requires:       sonic-frameworks-progress-ui-devel
Requires:       sonic-frameworks-app-info-devel
Requires:       sonic-frameworks-device-integration-devel
Requires:       sonic-frameworks-xml-gui-devel
Requires:       sonic-frameworks-windowsystem-devel
Requires: qt6-qtbase-devel >= 6.11
Provides:       kf6-kio-devel = %{version}-%{release}
Provides:       kf6-kio-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires: %{name}-core = %{version}-%{release}
BuildArch:      noarch
Provides:       kf6-kio-doc = %{version}-%{release}
Provides:       kf6-kio-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-doc

%description    doc
Documentation for %{name}.

%package        core
Summary:        Core components of the KIO Framework
%{?kf6_kinit_requires}
Requires: %{name}-core-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
Requires: kf6-filesystem >= 6.31
Recommends:     switcheroo-control
Provides:       kf6-kio-core = %{version}-%{release}
Provides:       kf6-kio-core%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-core

%description    core
KIOCore library provides core non-GUI components for working with KIO.

%package        core-libs
Summary:        Runtime libraries for KIO Core
Provides:       kf6-kio-core-libs = %{version}-%{release}
Provides:       kf6-kio-core-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-core-libs

%description    core-libs
%{summary}.

%package        widgets
Summary:        Widgets for KIO Framework
Requires: %{name}-widgets-libs%{?_isa} = %{version}-%{release}
## org.kde.klauncher6 service referenced from : widgets/krun.cpp
## included here for completeness, even those -core already has a dependency.
%{?kf6_kinit_requires}
Provides:       kf6-kio-widgets = %{version}-%{release}
Provides:       kf6-kio-widgets%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-widgets

%description    widgets
KIOWidgets contains classes that provide generic job control, progress
reporting, etc.

%package        widgets-libs
Summary:        Runtime libraries for KIO Widgets library
Provides:       kf6-kio-widgets-libs = %{version}-%{release}
Provides:       kf6-kio-widgets-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-widgets-libs

%description    widgets-libs
%{summary}.

%package        file-widgets
Summary:        Widgets for file-handling for KIO Framework
Provides:       kf6-kio-file-widgets = %{version}-%{release}
Provides:       kf6-kio-file-widgets%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-file-widgets

%description    file-widgets
The KIOFileWidgets library provides the file selection dialog and
its components.

%package        gui
Summary:        Gui components for the KIO Framework
Provides:       kf6-kio-gui = %{version}-%{release}
Provides:       kf6-kio-gui%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-gui

%description    gui
%{summary}.

%package        qch-doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kio-qch-doc = %{version}-%{release}
Provides:       kf6-kio-qch-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-qch-doc

%description    qch-doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kio-html = %{version}-%{release}
Provides:       kf6-kio-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kio-html

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --all-name --with-man --with-html

%files
%license LICENSES/*.txt
%doc README.md

%files core
%{_kf6_libexecdir}/kioexec
%{_kf6_libexecdir}/kiod6
%{_kf6_libexecdir}/kioworker
%{_kf6_bindir}/ktelnetservice6
%{_kf6_bindir}/ktrash6
%{_kf6_plugindir}/kio/
%{_kf6_plugindir}/kded/
%{_kf6_plugindir}/kiod/
%{_kf6_plugindir}/kio_dnd/
%{_kf6_datadir}/kf6/searchproviders/*.desktop
%{_kf6_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.kde.*.service
%{_kf6_datadir}/qlogging-categories6/*categories

%files core-libs
%{_kf6_libdir}/libKF6KIOCore.so.*

%files doc -f %{oldname}.lang

%files gui
%{_kf6_libdir}/libKF6KIOGui.so.*

%files widgets
%dir %{_kf6_plugindir}/urifilters/
%{_kf6_plugindir}/urifilters/*.so
%{_kf6_libdir}/libkuriikwsfiltereng_private.so.*

%files widgets-libs
%{_kf6_libdir}/libKF6KIOWidgets.so.*

%files file-widgets
%{_kf6_libdir}/libKF6KIOFileWidgets.so.*

%files devel
%{_kf6_includedir}/*
%{_kf6_libdir}/*.so
%{_kf6_libdir}/cmake/KF6KIO/
%{_kf6_datadir}/kdevappwizard/templates/kioworker6.tar.bz2
%{_kf6_qtplugindir}/designer/kio6widgets.so
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files qch-doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0.1-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0.1-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
