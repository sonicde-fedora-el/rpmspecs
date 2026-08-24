# Generated for SonicDE from Fedora's kf6-kpackage.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-package fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-package
# Upstream KDE project: kpackage
%global oldname kf6-kpackage

%global framework kpackage

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-package
Version:        6.29.0.1
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 library to load and install packages as plugins

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-archive-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  qt6-qtbase-devel
Requires:  kf6-filesystem

Provides:       kf6-kpackage = %{version}-%{release}
Conflicts:      kf6-kpackage < %{version}-%{release}

%description
KDE Frameworks 6 Tier 2 library to load and install non-binary packages as
if they were plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       kf6-kpackage-devel = %{version}-%{release}
Conflicts:      kf6-kpackage-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kpackage-doc = %{version}-%{release}
Conflicts:      kf6-kpackage-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kpackage-html = %{version}-%{release}
Conflicts:      kf6-kpackage-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --all-name --with-man

# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/kpackage/packagestructure/
mkdir -p %{buildroot}%{_kf6_datadir}/kpackage/

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Package.so.*
%{_kf6_qtplugindir}/kpackage/
%{_kf6_datadir}/kpackage/
%{_kf6_bindir}/kpackagetool6
%{_mandir}/man1/kpackagetool6.1*

%files devel
%{_kf6_includedir}/KPackage/
%{_kf6_libdir}/libKF6Package.so
%{_kf6_libdir}/cmake/KF6Package/
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
