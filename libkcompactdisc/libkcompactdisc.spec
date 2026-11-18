%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}
Name:    libkcompactdisc 
Version: 25.12.3
Release: 2%{?dist}
Summary: A KDE compact disc library

# License for this library is very nebulous.
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/multimedia/libkcompactdisc

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-device-integration-devel
BuildRequires: sonic-frameworks-internationalization-devel
BuildRequires: qt6-qtdeclarative-devel >= 6.11

BuildRequires: qt6-qtbase-devel >= 6.11

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(phonon4qt6)

# historical conflicts
# when split occured (kdemultimedia to libkcompactdisc)
Conflicts: kdemultimedia-libs < 6:4.8.80
# translations moved here (during kf5-libkcompactdisc)
Conflicts: kde-l10n < 17.03
 # translations conflict with kf5-libkcompactdisc
Conflicts: kf5-libkcompactdisc < 24.01.85
Obsoletes: kf5-libkcompactdisc < 24.01.85

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: kf5-libkcompactdisc-devel < 24.01.85
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man

%files -f %{name}.lang
%license COPYING*
%{_kf6_libdir}/libKCompactDisc6.so.5*

%files devel
%{_includedir}/KCompactDisc6/
%{_kf6_libdir}/libKCompactDisc6.so
%{_kf6_libdir}/cmake/KCompactDisc6/
%{_qt6_archdatadir}/mkspecs/modules/qt_KCompactDisc.pri


%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 25.12.3-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 25.12.3-1
- 26.08.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 25.12.3-1
- SonicDE build for Enterprise Linux 10
