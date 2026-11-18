# Generated for SonicDE from Fedora's kf6-purpose.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-purpose fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global reponame sonic-frameworks-purpose
# Upstream KDE project: purpose
%global oldname kf6-purpose

%global framework purpose

#Name:    kf6-purpose
Name:           sonic-frameworks-purpose
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
Version:        6.31.0
%global libversion %(echo %{version} | cut -d. -f1-3)
Release:        4%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

# upstream patches

%global sonicde_qt6_version 6.11.3
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires: sonic-frameworks-cmake-modules >= %{version}
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: cmake
BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-quick-ui-devel
BuildRequires: sonic-frameworks-notifications-devel
BuildRequires: sonic-accounts-integration-qt6-devel
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qtdeclarative-devel >= 6.11

Recommends:     accounts-qml-module-qt6
BuildRequires: sonic-frameworks-qml-bridge-devel
Requires:      sonic-frameworks-qml-bridge
BuildRequires: sonic-frameworks-barcode-devel
Requires:      sonic-frameworks-barcode
BuildRequires: sonic-frameworks-data-models
Requires:      qt6qml(org.kde.kitemmodels)


Requires: hicolor-icon-theme
Requires: sonic-frameworks-bluetooth >= %{version}

Provides:       kf6-purpose = %{version}-%{release}
Provides:       kf6-purpose%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-purpose

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: sonic-frameworks-core-addons-devel
Provides:       kf6-purpose-devel = %{version}-%{release}
Provides:       kf6-purpose-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-purpose-devel

%description devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-purpose-doc = %{version}-%{release}
Provides:       kf6-purpose-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-purpose-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-purpose-html = %{version}-%{release}
Provides:       kf6-purpose-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-purpose-html

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --all-name

%files -f %{oldname}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Purpose.so.6
%{_kf6_libdir}/libKF6Purpose.so.%{libversion}
%{_kf6_libdir}/libKF6PurposeWidgets.so.6
%{_kf6_libdir}/libKF6PurposeWidgets.so.%{libversion}
%{_kf6_libexecdir}/purposeprocess
%{_kf6_datadir}/kf6/purpose/
%{_kf6_datadir}/accounts/services/kde/*.service
%{_kf6_plugindir}/purpose/
%dir %{_kf6_plugindir}/kfileitemaction/
%{_kf6_plugindir}/kfileitemaction/sharefileitemaction.so
%{_kf6_qmldir}/org/kde/purpose/
%{_datadir}/icons/hicolor/*/apps/*-purpose6.*

%files devel
%{_kf6_libdir}/libKF6Purpose.so
%{_kf6_libdir}/libKF6PurposeWidgets.so
%{_kf6_includedir}/Purpose/
%{_kf6_includedir}/PurposeWidgets/
%{_kf6_libdir}/cmake/KF6Purpose/
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-4
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-2
- Pin cmake() BuildRequires to SonicDE package names so the
  alma+epel-10 solver cannot pick EPEL's Qt 6.10-linked providers
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
