# Generated for SonicDE from Fedora's kf6-kxmlgui.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-xml-gui fork, not from download.kde.org.
%define _disable_source_fetch 0
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%define debug_package %{nil}
%global reponame sonic-frameworks-xml-gui
# Upstream KDE project: kxmlgui
%global oldname kf6-kxmlgui

%global framework kxmlgui

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-xml-gui

# pyside6 python bindings are optional (EPEL pyside6 currently uninstallable on EL10)
%bcond_with bindings
Version:        6.31.0.1
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for user-configurable main windows

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %(echo %{version} | cut -d. -f1-3)
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sonic-frameworks-keybind-devel
BuildRequires:  sonic-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  sonic-frameworks-color-scheme-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-settings-ui-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-gui-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires:  sonic-frameworks-icon-themes-devel
BuildRequires:  sonic-frameworks-data-views-devel
BuildRequires:  sonic-frameworks-widgets-addons-devel
BuildRequires:  qt6-qttools-devel >= 6.11
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-private-devel >= 6.11
BuildRequires:  python3-devel
%if %{with bindings}
# required for pyside6 python bindings
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
%if %{with bindings}
BuildRequires:  cmake(PySide6)
%endif
%endif

Requires: kf6-filesystem >= 6.31

Provides:       kf6-kxmlgui = %{version}-%{release}
Provides:       kf6-kxmlgui%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kxmlgui

%description
KDE Frameworks 6 Tier 3 solution for user-configurable main windows.

%if %{with bindings}
%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
Provides:       python3-kf6-kxmlgui = %{version}-%{release}

%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}
%endif

%package        devel
Summary:        Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: sonic-frameworks-settings-devel
Requires: sonic-frameworks-settings-ui-devel
Requires: sonic-frameworks-gui-addons-devel
Requires: qt6-qtbase-devel >= 6.11
Provides:       kf6-kxmlgui-devel = %{version}-%{release}
Provides:       kf6-kxmlgui-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kxmlgui-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kxmlgui-doc = %{version}-%{release}
Provides:       kf6-kxmlgui-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kxmlgui-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kxmlgui-html = %{version}-%{release}
Provides:       kf6-kxmlgui-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kxmlgui-html

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 %{?with_bindings:-DBUILD_PYTHON_BINDINGS=ON}%{!?with_bindings:-DBUILD_PYTHON_BINDINGS=OFF}
%cmake_build_kf6

%install
%cmake_install_kf6

# Own the kxmlgui directory
mkdir -p %{buildroot}%{_kf6_datadir}/kxmlgui5/
%find_lang %{oldname} --all-name

%files -f %{oldname}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6XmlGui.so.*
%dir %{_kf6_datadir}/kxmlgui5/

%if %{with bindings}
%files -n python3-%{name}
%{python3_sitearch}/KXmlGui.cpython-%{python3_version_nodots}*.so

%endif
%files devel
%{_kf6_qtplugindir}/designer/*6widgets.so
%{_kf6_includedir}/KXmlGui/
%{_kf6_libdir}/libKF6XmlGui.so
%{_kf6_libdir}/cmake/KF6XmlGui/
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
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

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
