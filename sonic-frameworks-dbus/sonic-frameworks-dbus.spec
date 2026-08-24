# Generated for SonicDE from Fedora's kf6-kdbusaddons.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-dbus fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-dbus
# Upstream KDE project: kdbusaddons
%global oldname kf6-kdbusaddons

%global framework	kdbusaddons

#Name:			kf6-%%{framework}
Name:           sonic-frameworks-dbus
Version:        6.29.0
Release:        1%{?dist}
Summary:		KDE Frameworks 6 Tier 1 addon with various classes on top of QtDBus
License:		CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
#URL:			https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:		https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:		https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:		sonic-frameworks-cmake-modules >= %{version}
BuildRequires:		sonic-rpm-macros
BuildRequires:		cmake
BuildRequires:		gcc-c++
BuildRequires:		qt6-qtbase-devel
BuildRequires:		qt6-qttools-devel
BuildRequires:          qt6-qtbase-private-devel
BuildRequires:		pkgconfig(xkbcommon)

Requires:		kf6-filesystem

Provides:       kf6-kdbusaddons = %{version}-%{release}
Conflicts:      kf6-kdbusaddons < %{version}-%{release}

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		qt6-qtbase-devel
Provides:       kf6-kdbusaddons-devel = %{version}-%{release}
Conflicts:      kf6-kdbusaddons-devel < %{version}-%{release}

%description		devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kdbusaddons-doc = %{version}-%{release}
Conflicts:      kf6-kdbusaddons-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kdbusaddons-html = %{version}-%{release}
Conflicts:      kf6-kdbusaddons-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kdbusaddons6_qt

%files -f kdbusaddons6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_bindir}/kquitapp6
%{_kf6_libdir}/libKF6DBusAddons.so.*

%files devel
%{_kf6_includedir}/KDBusAddons/
%{_kf6_libdir}/libKF6DBusAddons.so
%{_kf6_libdir}/cmake/KF6DBusAddons/
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
