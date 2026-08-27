# Generated for SonicDE from Fedora's kf6-breeze-icons.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-silver-icons fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-silver-icons
# Upstream KDE project: breeze-icons
%global oldname kf6-breeze-icons

# If KF7 still provides these icons, then their installation should then
# be disabled in KF6 builds.
%bcond install_icons 1
# for compatibility, to be removed once Kexi (and others?) are ported
%bcond install_rcc 1

%global framework breeze-icons

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-silver-icons
Summary: Breeze icon theme library
Version:        6.29.0
Release:        3%{?dist}

# skladnik.svg is CC-BY-SA-4.0
# folder-edit-sign-encrypt.svg is LGPL-2.1-or-later
# src/lib/ is LGPL-2.0-or-later
# all other icons are LGPL-3.0-or-later
License: LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND CC-BY-SA-4.0
#URL:     https://develop.kde.org/frameworks/breeze-icons/
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

## upstream patches


## upstreamable patches


BuildRequires: sonic-frameworks-cmake-modules >= %{version}
BuildRequires: sonic-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
# icon optimizations
BuildRequires: hardlink
# for generate-24px-versions.py
BuildRequires: python3-lxml

%if %{with install_icons}
Requires: breeze-icon-theme = %{version}-%{release}
%else
Requires: breeze-icon-theme
%endif

Provides:       kf6-breeze-icons%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-breeze-icons < %{version}-%{release}

%description
%{summary}.

%if %{with install_icons}
%package -n breeze-icon-theme
Summary:     Breeze icon theme
# analysis above
License:     LGPL-2.1-or-later AND LGPL-3.0-or-later AND CC-BY-SA-4.0
BuildArch:   noarch
Requires:    hicolor-icon-theme
# Needed for proper Fedora logo
Requires:    system-logos
# upstream name
Provides:    breeze-icons = %{version}-%{release}
# package changed arch
Obsoletes:   breeze-icon-theme < 6.3.0-2
# anaconda icon split out into fedora-only subpackage
Obsoletes:   breeze-icon-theme < 6.13.0-2
Conflicts:   breeze-icon-theme < 6.13.0-2
%description -n breeze-icon-theme
%{summary}.

%if 0%{?fedora}
%package -n breeze-icon-theme-fedora
Summary:     Breeze icon theme Fedora specific icons
License:     LGPL-3.0-or-later
BuildArch:   noarch
Requires:    breeze-icon-theme = %{version}-%{release}
# This is for Fedora only
Requires:    fedora-release-common
Supplements: (breeze-icon-theme and fedora-release-kde)
Obsoletes:   breeze-icon-theme < 6.13.0-2
Conflicts:   breeze-icon-theme < 6.13.0-2
%description -n breeze-icon-theme-fedora
%{summary}.
%endif

%endif

%if %{with install_rcc}
%package -n breeze-icon-theme-rcc
Summary:     Breeze Qt resource files
# analysis above
License:     LGPL-2.1-or-later AND LGPL-3.0-or-later AND CC-BY-SA-4.0
BuildArch:   noarch
# package changed arch
Obsoletes:   breeze-icon-theme-rcc < 6.3.0-2
%description -n breeze-icon-theme-rcc
%{summary}.
%endif

%package     devel
Summary:     Breeze icon theme development files
Requires:    %{name} = %{version}-%{release}
# renamed for https://pagure.io/fedora-kde/SIG/issue/530
Provides:    breeze-icon-theme-devel = %{version}-%{release}
Obsoletes:   breeze-icon-theme-devel < 6.3.0-2
Provides:       kf6-breeze-icons-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-breeze-icons-devel < %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{reponame}-%{version}

# Move Fedora installer icon out of normal breeze installs
mkdir -p icons-fedora/apps/48
mv icons/apps/48/org.fedoraproject.AnacondaInstaller.svg icons-fedora/apps/48


%build
%cmake_kf6 \
  -DBINARY_ICONS_RESOURCE:BOOL=%{?with_install_rcc:ON}%{!?with_install_rcc:OFF} \
  -DSKIP_INSTALL_ICONS:BOOL=%{?with_install_icons:OFF}%{!?with_install_icons:ON} \
  %{nil}

%cmake_build


%install
%cmake_install

%if %{with install_icons}

## icon optimizations
du -s .
hardlink -c -v %{buildroot}%{_datadir}/icons/
du -s .

# %%ghost icon.cache
touch %{buildroot}%{_kf6_datadir}/icons/{silver,silver-dark}/icon-theme.cache

%if 0%{?fedora}
install -pm 0644 icons-fedora/apps/48/org.fedoraproject.AnacondaInstaller.svg %{buildroot}%{_kf6_datadir}/icons/silver/apps/48
ln -sr %{buildroot}%{_kf6_datadir}/icons/silver/apps/48/org.fedoraproject.AnacondaInstaller.svg %{buildroot}%{_kf6_datadir}/icons/silver-dark/apps/48/org.fedoraproject.AnacondaInstaller.svg
%endif

## trigger-based scriptlets
%transfiletriggerin -n breeze-icon-theme -- %{_datadir}/icons/silver
gtk-update-icon-cache --force %{_datadir}/icons/silver &>/dev/null || :

%transfiletriggerin -n breeze-icon-theme -- %{_datadir}/icons/silver-dark
gtk-update-icon-cache --force %{_datadir}/icons/silver-dark &>/dev/null || :

%transfiletriggerpostun -n breeze-icon-theme -- %{_datadir}/icons/silver
gtk-update-icon-cache --force %{_datadir}/icons/silver &>/dev/null || :

%transfiletriggerpostun -n breeze-icon-theme -- %{_datadir}/icons/silver-dark
gtk-update-icon-cache --force %{_datadir}/icons/silver-dark &>/dev/null || :

%endif

%files
%license COPYING.LIB
%doc README.md
%{_kf6_libdir}/libKF6BreezeIcons.so.6
%{_kf6_libdir}/libKF6BreezeIcons.so.%{version}

%files devel
%{_kf6_includedir}/BreezeIcons/
%{_kf6_libdir}/cmake/KF6BreezeIcons/
%{_kf6_libdir}/libKF6BreezeIcons.so

%if %{with install_icons}
%files -n breeze-icon-theme
%license COPYING-ICONS
%doc README.md
%ghost %{_datadir}/icons/silver/icon-theme.cache
%{_datadir}/icons/silver/index.theme
%{_datadir}/icons/silver/*/
%ghost %{_datadir}/icons/silver-dark/icon-theme.cache
%{_datadir}/icons/silver-dark/index.theme
%{_datadir}/icons/silver-dark/*/
%exclude %{_datadir}/icons/silver/silver-icons.rcc
%if 0%{?fedora}
%exclude %{_datadir}/icons/silver*/apps/*/org.fedoraproject.AnacondaInstaller.svg
%endif

%if 0%{?fedora}
%files -n breeze-icon-theme-fedora
%{_datadir}/icons/silver*/apps/*/org.fedoraproject.AnacondaInstaller.svg
%endif

%endif

%if %{with install_rcc}
%files -n breeze-icon-theme-rcc
%{_datadir}/icons/silver/silver-icons.rcc
%endif

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
