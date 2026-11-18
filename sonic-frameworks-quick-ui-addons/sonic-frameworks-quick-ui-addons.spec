# Generated for SonicDE from Fedora's kf6-kirigami-addons.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-quick-ui-addons fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-frameworks-quick-ui-addons
# Upstream KDE project: kirigami-addons
%global oldname kf6-kirigami-addons

%global framework kirigami-addons

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-quick-ui-addons
Version:        1.13.1
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        5%{?dist}
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND LicenseRef-KFQF-Accepted-GPL
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://github.com/Sonic-DE/%{reponame}
#Source:         https://download.kde.org/stable/%%{framework}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-keybind-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-quick-ui-devel
BuildRequires:  sonic-frameworks-svg-devel
BuildRequires:  sonic-frameworks-color-scheme-devel
BuildRequires:  sonic-frameworks-crash-handler-devel
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11

# Doesn't need qtbase-private-devel, but private stuff from qtdeclarative
# so we still need to rebuild it
#BuildRequires: qt6-qtbase-private-devel >= 6.11
Requires: kf6-filesystem >= 6.31

### Renamed from kf6-kirigami2-addons (which was at epoch 1)
Obsoletes: kf6-kirigami2-addons < 1:0.11.76-5
Provides:  kf6-kirigami2-addons = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons%{?_isa} = 1:%{version}-%{release}
### Merged subpackages back into main package
# The old name
Obsoletes: kf6-kirigami2-addons-dateandtime < 1:0.11.76-5
Provides:  kf6-kirigami2-addons-dateandtime = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-dateandtime = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-dateandtime%{?_isa} = 1:%{version}-%{release}
Obsoletes: kf6-kirigami2-addons-treeview < 1:0.11.76-5
Provides:  kf6-kirigami2-addons-treeview = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-treeview = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-treeview%{?_isa} = 1:%{version}-%{release}
# The new name
Obsoletes:      kf6-kirigami-addons-dateandtime
Provides:  kf6-kirigami-addons-dateandtime = %{version}-%{release}
Provides:  kf6-kirigami-addons-dateandtime%{?_isa} = %{version}-%{release}
Provides:  kf6-kirigami-addons-dateandtime = %{version}-%{release}
Provides:  kf6-kirigami-addons-dateandtime%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kirigami-addons-treeview
Provides:  kf6-kirigami-addons-treeview = %{version}-%{release}
Provides:  kf6-kirigami-addons-treeview%{?_isa} = %{version}-%{release}
Provides:  kf6-kirigami-addons-treeview = %{version}-%{release}
Provides:  kf6-kirigami-addons-treeview%{?_isa} = %{version}-%{release}
Provides:       kf6-kirigami-addons = %{version}-%{release}
Provides:       kf6-kirigami-addons%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kirigami-addons

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package   devel
Summary:   Development files for %{name}
Requires: %{name} = %{version}-%{release}
Conflicts: sonic-frameworks-quick-ui-addons < 1.4.0
Provides:       kf6-kirigami-addons-devel = %{version}-%{release}
Provides:       kf6-kirigami-addons-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kirigami-addons-devel

%description devel
The %{name}-devel package contains CMake definitions, libraries
and header files for developing applications that use %{name}.

%prep
%autosetup -n %{reponame}-%{version}

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install
%find_lang %{orig_name}6 --all-name

%files -f %{orig_name}6.lang
%doc README.md
%license LICENSES/
%dir %{_kf6_qmldir}/org/kde
%{_kf6_qmldir}/org/kde/kirigamiaddons
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so.{6,%{version}}
%{_kf6_libdir}/libKirigamiApp.so.%{libversion}
%{_kf6_libdir}/libKirigamiApp.so.6
%{_kf6_libdir}/libKirigamiAddonsComponents.so.%{libversion}
%{_kf6_libdir}/libKirigamiAddonsComponents.so.6

%files devel
%{_kf6_libdir}/libKirigamiAddonsComponents.so
%{_kf6_libdir}/libKirigamiApp.so
%{_includedir}/KirigamiAddons/
%{_kf6_libdir}/cmake/KF6KirigamiAddons
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so
%{_includedir}/KirigamiAddonsStatefulApp/
%{_kf6_datadir}/kdevappwizard/templates/kirigamiaddons6.tar.bz2
%{_kf6_datadir}/kdevappwizard/templates/librarymanager6.tar.bz2

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.13.1-5
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.13.1-4
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.13.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
