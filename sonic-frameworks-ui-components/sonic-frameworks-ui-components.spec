# Generated for SonicDE from Fedora's kf6-kparts.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-ui-components fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-ui-components
# Upstream KDE project: kparts
%global oldname kf6-kparts

%global framework kparts

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-ui-components
Version:        6.29.0
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for KParts

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  pkgconfig(xkbcommon)
Requires:  kf6-filesystem

Provides:       kf6-kparts%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kparts < %{version}-%{release}

%description
KDE Frameworks 6 Tier 3 solution for KParts

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6KIO)
Requires:       cmake(KF6TextWidgets)
Requires:       cmake(KF6XmlGui)
Provides:       kf6-kparts-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kparts-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kparts-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kparts-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kparts-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kparts-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --all-name --with-html
# create/own parts plugin dir
mkdir -p %{buildroot}%{_kf6_plugindir}/parts/

%files -f %{oldname}.lang
%doc README.md AUTHORS
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Parts.so.*
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%dir %{_kf6_plugindir}/parts/

%files devel
%{_kf6_includedir}/KParts/
%{_kf6_libdir}/libKF6Parts.so
%{_kf6_libdir}/cmake/KF6Parts/
%dir %{_kf6_datadir}/kdevappwizard/
%dir %{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_datadir}/kdevappwizard/templates/kparts6-app.tar.bz2
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
