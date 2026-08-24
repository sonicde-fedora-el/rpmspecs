# Generated for SonicDE from Fedora's kf6-kio.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-io fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-io
# Upstream KDE project: kio
%global oldname kf6-kio

%global framework kio

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-io
Version:        6.29.0.1
Release:        1%{?dist}
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
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  switcheroo-control
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Service)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  libacl-devel
%if !0%{?flatpak}
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
%endif
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  zlib-devel

BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6Qml)

BuildRequires:  cmake(KF6KDED)
BuildRequires:  cmake(Qt6Core5Compat)

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

Requires: sonic-daemon

Provides:       kf6-kio = %{version}-%{release}
Conflicts:      kf6-kio < %{version}-%{release}

%description
KDE Frameworks 6 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       sonic-frameworks-bookmarks-devel
Requires:       cmake(KF6Completion)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6ItemViews)
Requires:       cmake(KF6JobWidgets)
Requires:       cmake(KF6Service)
Requires:       cmake(KF6Solid)
Requires:       cmake(KF6XmlGui)
Requires:       cmake(KF6WindowSystem)
Requires:       qt6-qtbase-devel
Provides:       kf6-kio-devel = %{version}-%{release}
Conflicts:      kf6-kio-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name}-core = %{version}-%{release}
BuildArch:      noarch
Provides:       kf6-kio-doc = %{version}-%{release}
Conflicts:      kf6-kio-doc < %{version}-%{release}

%description    doc
Documentation for %{name}.

%package        core
Summary:        Core components of the KIO Framework
%{?kf6_kinit_requires}
Requires:       %{name}-core-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-doc = %{version}-%{release}
Requires:       kf6-filesystem
Recommends:     switcheroo-control
Provides:       kf6-kio-core = %{version}-%{release}
Conflicts:      kf6-kio-core < %{version}-%{release}

%description    core
KIOCore library provides core non-GUI components for working with KIO.

%package        core-libs
Summary:        Runtime libraries for KIO Core
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Provides:       kf6-kio-core-libs = %{version}-%{release}
Conflicts:      kf6-kio-core-libs < %{version}-%{release}

%description    core-libs
%{summary}.

%package        widgets
Summary:        Widgets for KIO Framework
## org.kde.klauncher6 service referenced from : widgets/krun.cpp
## included here for completeness, even those -core already has a dependency.
%{?kf6_kinit_requires}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Provides:       kf6-kio-widgets = %{version}-%{release}
Conflicts:      kf6-kio-widgets < %{version}-%{release}

%description    widgets
KIOWidgets contains classes that provide generic job control, progress
reporting, etc.

%package        widgets-libs
Summary:        Runtime libraries for KIO Widgets library
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Provides:       kf6-kio-widgets-libs = %{version}-%{release}
Conflicts:      kf6-kio-widgets-libs < %{version}-%{release}

%description    widgets-libs
%{summary}.

%package        file-widgets
Summary:        Widgets for file-handling for KIO Framework
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Provides:       kf6-kio-file-widgets = %{version}-%{release}
Conflicts:      kf6-kio-file-widgets < %{version}-%{release}

%description    file-widgets
The KIOFileWidgets library provides the file selection dialog and
its components.

%package        gui
Summary:        Gui components for the KIO Framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Provides:       kf6-kio-gui = %{version}-%{release}
Conflicts:      kf6-kio-gui < %{version}-%{release}

%description    gui
%{summary}.

%package        qch-doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kio-qch-doc = %{version}-%{release}
Conflicts:      kf6-kio-qch-doc < %{version}-%{release}

%description    qch-doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kio-html = %{version}-%{release}
Conflicts:      kf6-kio-html < %{version}-%{release}

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

%files doc -f %{name}.lang

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
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
