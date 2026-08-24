# Generated for SonicDE from Fedora's kf6-kdesu.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-root-shell fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-root-shell
# Upstream KDE project: kdesu
%global oldname kf6-kdesu

%global framework kdesu

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-root-shell
Version:        6.29.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 integration with su

License: CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Pty)
#BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel
Requires:  kf6-filesystem

%if 0%{?rhel} || 0%{?fedora} >= 42
Requires:  sudo
%endif

Provides:       kf6-kdesu = %{version}-%{release}
Conflicts:      kf6-kdesu < %{version}-%{release}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Pty)
Provides:       kf6-kdesu-devel = %{version}-%{release}
Conflicts:      kf6-kdesu-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kdesu-doc = %{version}-%{release}
Conflicts:      kf6-kdesu-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kdesu-html = %{version}-%{release}
Conflicts:      kf6-kdesu-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6 \
%if 0%{?rhel} || 0%{?fedora} >= 42
    -DKDESU_USE_SUDO_DEFAULT:BOOL=TRUE
%endif
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang kdesu6_qt --all-name

%files -f kdesu6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*
%{_kf6_libdir}/libKF6Su.so.*
%{_kf6_libexecdir}/kdesu_stub
%{_kf6_libexecdir}/kdesud

%files devel
%{_kf6_includedir}/KDESu/
%{_kf6_libdir}/libKF6Su.so
%{_kf6_libdir}/cmake/KF6Su/
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
