# Generated for SonicDE from Fedora's kf6-kdoctools.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-doctools fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-doctools
# Upstream KDE project: kdoctools
%global oldname kf6-kdoctools

%global framework kdoctools

#Name:    kf6-%%{framework}
Name:           sonic-frameworks-doctools
Version:        6.29.0
Release:        3%{?dist}
Summary: KDE Frameworks 6 Tier 2 addon for generating documentation

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:     https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  cmake
BuildRequires:  sonic-rpm-macros
BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Any::URI::Escape)
BuildRequires:  qt6-qtbase-devel
Requires:       docbook-dtds
Requires:       docbook-style-xsl

Provides:       kf6-kdoctools%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kdoctools < %{version}-%{release}

%description
Provides tools to generate documentation in various format from DocBook files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf6-kdoctools-static%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       perl(Any::URI::Escape)
Provides:       kf6-kdoctools-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kdoctools-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kdoctools-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kdoctools-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kdoctools-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kdoctools-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --all-name --with-man --with-html

%files -f %{oldname}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6DocTools.so.6
%{_kf6_libdir}/libKF6DocTools.so.%{version}
%{_kf6_bindir}/checkXML6
%{_kf6_bindir}/meinproc6
%{_kf6_mandir}/man1/*.1*
%{_kf6_mandir}/man7/*.7*
%{_kf6_datadir}/kf6/kdoctools/

%files devel
%{_kf6_includedir}/KDocTools/
%{_kf6_libdir}/libKF6DocTools.so
%{_kf6_libdir}/cmake/KF6DocTools/
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
