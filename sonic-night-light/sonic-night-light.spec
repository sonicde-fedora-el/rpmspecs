# Generated for SonicDE from Fedora's knighttime.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-night-light fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-night-light
# Upstream KDE project: knighttime
%global oldname knighttime

#Name:           knighttime
Name:           sonic-night-light
Summary:        Helpers for scheduling the dark-light cycle
Version:        6.8.2
%global libversion %(echo %{version} | cut -d. -f1-3)
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

BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtpositioning-devel >= 6.11

BuildRequires:  sonic-frameworks-settings-devel
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-dbus-devel
BuildRequires:  sonic-frameworks-holidays-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11

Provides:       knighttime = %{version}-%{release}
Provides:       knighttime%{?_isa} = %{version}-%{release}
Obsoletes:      knighttime

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       knighttime-devel = %{version}-%{release}
Provides:       knighttime-devel%{?_isa} = %{version}-%{release}
Obsoletes:      knighttime-devel

%description devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       knighttime-doc = %{version}-%{release}
Provides:       knighttime-doc%{?_isa} = %{version}-%{release}
Obsoletes:      knighttime-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       knighttime-html = %{version}-%{release}
Provides:       knighttime-html%{?_isa} = %{version}-%{release}
Obsoletes:      knighttime-html

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6
sed '/^OnlyShowIn=/d' %{buildroot}%{_datadir}/applications/org.kde.knighttimed.desktop > %{_tmppath}/knighttimed.desktop
desktop-file-validate %{_tmppath}/knighttimed.desktop
rm -f %{_tmppath}/knighttimed.desktop

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
%{_kf6_libdir}/libKNightTime.so.%{libversion}
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
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
