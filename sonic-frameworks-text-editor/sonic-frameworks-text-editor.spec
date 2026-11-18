# Generated for SonicDE from Fedora's kf6-ktexteditor.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-text-editor fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-frameworks-text-editor
# Upstream KDE project: ktexteditor
%global oldname kf6-ktexteditor

%global framework ktexteditor

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-text-editor
Version:        6.31.0
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 3 with advanced embeddable text editor

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND MIT
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-frameworks-archive-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-ui-components-devel
BuildRequires:  sonic-frameworks-color-scheme-devel
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtspeech-devel >= 6.11
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-syntax-highlighting-devel
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(xkbcommon)
Requires: kf6-filesystem >= 6.31
Requires: git-core

Provides:       kf6-ktexteditor = %{version}-%{release}
Provides:       kf6-ktexteditor%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ktexteditor

%description
KTextEditor provides a powerful text editor component that you can embed in your
application, either as a KPart or using the KF6::TextEditor library (if you need
more control).

The text editor component contains many useful features, from syntax
highlighting and automatic indentation to advanced scripting support, making it
suitable for everything from a simple embedded text-file editor to an advanced
IDE.

%package        devel
Summary:        Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: sonic-frameworks-ui-components-devel
Requires: sonic-frameworks-syntax-highlighting-devel
#Requires:       kf6-syntax-highlighting-devel
Provides:       kf6-ktexteditor-devel = %{version}-%{release}
Provides:       kf6-ktexteditor-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ktexteditor-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-ktexteditor-doc = %{version}-%{release}
Provides:       kf6-ktexteditor-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ktexteditor-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-ktexteditor-html = %{version}-%{release}
Provides:       kf6-ktexteditor-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ktexteditor-html

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
# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/ktexteditor
# Removing empty file
rm -f %{buildroot}%{_kf6_datadir}/katepart5/script/README.md

%files -f %{oldname}.lang
%dir %{_kf6_plugindir}/parts/
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/dbus-1/system-services/org.kde.ktexteditor6.katetextbuffer.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.ktexteditor6.katetextbuffer.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.ktexteditor6.katetextbuffer.policy
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6TextEditor.so.*
%{_kf6_plugindir}/parts/katepart.so
%{_kf6_qtplugindir}/ktexteditor/
%{_kf6_libexecdir}/kauth/kauth_ktexteditor_helper
%{_kf6_bindir}/ktexteditor-script-tester6

%files devel
%{_kf6_datadir}/kdevappwizard/templates/ktexteditor6-plugin.tar.bz2
%{_kf6_includedir}/KTextEditor/
%{_kf6_libdir}/cmake/KF6TextEditor/
%{_kf6_libdir}/libKF6TextEditor.so
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
