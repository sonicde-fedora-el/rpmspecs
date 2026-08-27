# Generated for SonicDE from Fedora's kf6-kidletime.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-idle-tracker fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-idle-tracker
# Upstream KDE project: kidletime
%global oldname kf6-kidletime

# Disable X11 for RHEL
# SonicDE is X11-only, so the X11 plugin is always built.
%bcond_without x11

%global		framework kidletime

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-idle-tracker
Version:        6.29.0
Release:        3%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module for idle time detection
License:	CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	sonic-frameworks-cmake-modules >= %{version}
BuildRequires:	sonic-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols-devel
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	cmake(Qt6WaylandClient)
Requires:	kf6-filesystem
%if %{with x11}
Recommends:	%{name}-x11%{?_isa} = %{version}-%{release}
%endif

Provides:       kf6-kidletime%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kidletime < %{version}-%{release}

%description
KDE Frameworks 6 Tier 1 integration module for idle time detection.

%if %{with x11}
%package	x11
Summary:	Idle time detection plugins for X11 environments
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-sync)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xkbcommon)
Requires:	%{name}%{?_isa} = %{version}-%{release}
Conflicts:	%{name} < 6.6.0-1
# X11 is deprecated and this will be removed eventually...
Provides:	deprecated()

Provides:       kf6-kidletime-x11%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kidletime-x11 < %{version}-%{release}

%description	x11
The %{name}-x11 package contains plugins for applications using
%{name} to detect idle time on X11 environments.
%endif

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
Provides:       kf6-kidletime-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kidletime-devel < %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kidletime-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kidletime-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kidletime-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kidletime-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 \
  -DWITH_X11=%{?with_x11:ON}%{?!with_x11:OFF}
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6IdleTime.so.*
%dir %{_kf6_plugindir}/org.kde.kidletime.platforms/
# SonicDE is X11 only: %%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeWaylandPlugin.so

%if %{with x11}
%files x11
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin*.so
%endif

%files devel
%{_kf6_includedir}/KIdleTime/
%{_kf6_libdir}/libKF6IdleTime.so
%{_kf6_libdir}/cmake/KF6IdleTime/
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
