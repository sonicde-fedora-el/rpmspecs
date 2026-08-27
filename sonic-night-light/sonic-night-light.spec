# Generated for SonicDE from Fedora's knighttime.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-night-light fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-night-light
# Upstream KDE project: knighttime
%global oldname knighttime

#Name:           knighttime
Name:           sonic-night-light
Summary:        Helpers for scheduling the dark-light cycle
Version:        6.7.4
Release:        3%{?dist}

License:        GPL-3.0-only AND BSD-3-Clause AND MIT AND GPL-2.0-only AND LGPL-2.1-only AND CC0-1.0 AND LGPL-3.0-only
#URL:            https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

# Upstream Patches

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Positioning)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)

Provides:       knighttime%{?_isa} = %{version}-%{release}
Obsoletes:      knighttime < %{version}-%{release}

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       knighttime-devel%{?_isa} = %{version}-%{release}
Obsoletes:      knighttime-devel < %{version}-%{release}

%description devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       knighttime-doc%{?_isa} = %{version}-%{release}
Obsoletes:      knighttime-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       knighttime-html%{?_isa} = %{version}-%{release}
Obsoletes:      knighttime-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.knighttimed.desktop

%post
%systemd_user_post plasma-knighttimed.service

%preun
%systemd_user_preun plasma-knighttimed.service

%postun
%systemd_user_postun_with_restart plasma-knighttimed.service
%systemd_user_postun_with_reload plasma-knighttimed.service
%systemd_user_postun plasma-knighttimed.service

%files
%license LICENSES/*.txt
%{_userunitdir}/plasma-knighttimed.service
%{_kf6_libdir}/libKNightTime.so.0
%{_kf6_libdir}/libKNightTime.so.%{version}
%{_libexecdir}/knighttimed
%{_datadir}/applications/org.kde.knighttimed.desktop
%{_datadir}/dbus-1/interfaces/org.kde.NightTime.xml
%{_datadir}/dbus-1/services/org.kde.NightTime.service
%{_datadir}/qlogging-categories6/knighttime.categories

%files devel
%{_includedir}/KNightTime/
%{_kf6_libdir}/cmake/KNightTime/
%{_kf6_libdir}/libKNightTime.so

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
