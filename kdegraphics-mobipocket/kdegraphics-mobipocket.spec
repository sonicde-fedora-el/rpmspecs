%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}
Name:    kdegraphics-mobipocket
Summary: A collection of plugins to handle mobipocket files
Version: 26.08.3
Release: 3%{?dist}

License: GPL-2.0-or-later AND CC0-1.0 AND LGPL-2.1-or-later
URL:     https://www.kde.org/applications/graphics/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qt5compat-devel >= 6.11

Obsoletes:      qmobipocket
Provides:  qmobipocket = %{version}-%{release}
Provides:  qmobipocket = %{version}-%{release}
Provides:  qmobipocket%{?_isa} = %{version}-%{release}
%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      qmobipocket-devel
Provides:  qmobipocket-devel = %{version}-%{release}
Provides:  qmobipocket-devel = %{version}-%{release}
Provides:  qmobipocket-devel%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%license LICENSES/*
%{_libdir}/libQMobipocket6.so.3*
%{_datadir}/qlogging-categories6/qmobipocket.categories

%files devel
%{_libdir}/libQMobipocket6.so
%{_includedir}/QMobipocket6/
%{_libdir}/cmake/QMobipocket6/


%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
