# Generated for SonicDE from Fedora's kio-fuse.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-io-fuse fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global sonicde_qt6_version 6.11.3
%global reponame sonic-frameworks-io-fuse
# Upstream KDE project: kio-fuse
%global oldname kio-fuse

%global         min_qt_version 5.12
%global         min_kf_version 5.66

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

#Name:           kio-fuse
Name:           sonic-frameworks-io-fuse
Version:        6.0.0
Release:        5%{?dist}
Summary:        KIO FUSE

License:        GPL-3.0-or-later
#URL:            https://invent.kde.org/system/kio-fuse
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:        https://download.kde.org/stable/%%{name}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/stable/%%{name}/%%{name}-%%{version}.tar.xz.sig
#Source2:        gpgkey-21EC3FD75D26B39E820BE6FBD27C2C1AF21D8BAD.gpg

## upstream fixes

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules  >= %{min_kf_version}

BuildRequires:  pkgconfig(fuse3)

BuildRequires:  qt6-qtbase-devel >= 6.11

BuildRequires:  sonic-frameworks-io-devel
BuildRequires:  sonic-frameworks-core-addons-devel

%if 0%{?tests}
BuildRequires:  dbus-x11
BuildRequires:  sonic-frameworks-io-extras
BuildRequires:  fuse3
%endif

Requires:       systemd
Requires:       dbus-common

Provides:       kio-fuse = %{version}-%{release}
Provides:       kio-fuse%{?_isa} = %{version}-%{release}
Obsoletes:      kio-fuse

%description
KioFuse works by acting as a bridge between KDE's KIO filesystem design and
FUSE.


%prep
# The SonicDE release tarballs come from GitHub and are not GPG signed.
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
dbus-launch --exit-with-session \
%ctest --timeout 30 ||:
%endif


%files
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md DESIGN.md
%{_libexecdir}/kio-fuse
%{_userunitdir}/kio-fuse.service
%{_kf6_datadir}/dbus-1/services/org.kde.KIOFuse.service
%{_tmpfilesdir}/%{oldname}-tmpfiles.conf

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.0.0-5
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.0.0-4
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.0.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
