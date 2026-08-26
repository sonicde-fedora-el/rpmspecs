# Generated for SonicDE from Fedora's breeze-gtk.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-silver-gtk fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-silver-gtk
# Upstream KDE project: breeze-gtk
%global oldname breeze-gtk

#Name:    breeze-gtk
Name:           sonic-silver-gtk
Version:        6.7.4
Release:        1%{?dist}
Summary: Breeze widget theme for GTK

License: BSD-3-Clause AND CC0-1.0
#URL:     https://invent.kde.org/plasma/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/plasma/%%{version}/%%{name}-%%{version}.tar.xz.sig

BuildArch:      noarch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtk2-engines
BuildRequires:  sonic-breeze-devel
BuildRequires:  python3-cairo-devel
BuildRequires:  sassc

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros

# not used directly, but is an indirect dep from ECMQueryQmake.cmake
# probably should be fixed there -- rex
BuildRequires:  cmake(Qt6Core)

# main meta package to depend on all subpkgs, for cleaner/simpler upgrade path
Requires: %{name}-gtk2 = %{version}-%{release}
Requires: %{name}-gtk3 = %{version}-%{release}
Requires: %{name}-gtk4 = %{version}-%{release}

Provides:       breeze-gtk = %{version}-%{release}
Conflicts:      breeze-gtk < %{version}-%{release}

%description
%{summary}.

%package common
Summary:        Breeze widget theme for GTK common files
Conflicts:      sonic-silver-gtk < 5.20.2-2

Provides:       breeze-gtk-common = %{version}-%{release}
Conflicts:      breeze-gtk-common < %{version}-%{release}

%description common
%{summary}.

%package gtk2
Summary:        Breeze widget theme for GTK 2
Requires:       gtk2-engines
Requires:       %{name}-common = %{version}-%{release}
Supplements:    (sonic-breeze and gtk2)
Provides:       breeze-gtk-gtk2 = %{version}-%{release}
Conflicts:      breeze-gtk-gtk2 < %{version}-%{release}

%description gtk2
%{summary}.

%package gtk3
Summary:        Breeze widget theme for GTK 3
Requires:       %{name}-common = %{version}-%{release}
Supplements:    (sonic-breeze and gtk3)
Provides:       breeze-gtk-gtk3 = %{version}-%{release}
Conflicts:      breeze-gtk-gtk3 < %{version}-%{release}

%description gtk3
%{summary}.

%package gtk4
Summary:        Breeze widget theme for GTK 4
Requires:       %{name}-common = %{version}-%{release}
Supplements:    (sonic-breeze and gtk4)
Provides:       breeze-gtk-gtk4 = %{version}-%{release}
Conflicts:      breeze-gtk-gtk4 < %{version}-%{release}

%description gtk4
%{summary}.


%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install

%files
# empty metapackage

%files common
%license LICENSES/*.txt
%doc README.md
%dir %{_datadir}/themes/Silver/
%{_datadir}/themes/Silver/assets/
%{_datadir}/themes/Silver/settings.ini
%dir %{_datadir}/themes/Silver-Dark/
%{_datadir}/themes/Silver-Dark/assets/
%{_datadir}/themes/Silver-Dark/settings.ini

%files gtk2
%{_datadir}/themes/Silver/gtk-2.0/
%{_datadir}/themes/Silver-Dark/gtk-2.0/

%files gtk3
%{_datadir}/themes/Silver/gtk-3.0/
%{_datadir}/themes/Silver-Dark/gtk-3.0/

%files gtk4
%{_datadir}/themes/Silver/gtk-4.0/
%{_datadir}/themes/Silver-Dark/gtk-4.0/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.7.4-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
