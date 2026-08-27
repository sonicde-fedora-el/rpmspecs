# Generated for SonicDE from Fedora's kf6-sonnet.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-spell-check fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-spell-check
# Upstream KDE project: sonnet
%global oldname kf6-sonnet

%global		framework sonnet

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-spell-check
Version:        6.29.0
Release:        3%{?dist}
Summary:	KDE Frameworks 6 Tier 1 solution for spell checking
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig
# patch out default excluded file list to have it empty
# https://bugs.kde.org/show_bug.cgi?id=482376
Patch0:		sonnet6-default-list.patch

BuildRequires:	appstream
BuildRequires:	sonic-frameworks-cmake-modules >= %{version}
BuildRequires:	sonic-rpm-macros
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	zlib-devel
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(aspell)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	hspell-devel
BuildRequires:	pkgconfig(libvoikko)


Requires:	kf6-filesystem
Recommends:	%{name}-hunspell

Provides:       kf6-sonnet%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-sonnet < %{version}-%{release}

%description
KDE Frameworks 6 Tier 1 solution for spell checking.


%package	aspell
Summary:	aspell plugin for %{name}
Requires:	%{name} = %{version}-%{release}
Provides:       kf6-sonnet-aspell%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-sonnet-aspell < %{version}-%{release}

%description	aspell
The %{name}-aspell package contains the aspell spellchecking
plugin for %{name}.

%package	hunspell
Summary:	hunspell plugin for %{name}
Requires:	%{name} = %{version}-%{release}
Provides:       kf6-sonnet-hunspell%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-sonnet-hunspell < %{version}-%{release}

%description	hunspell
The %{name}-hunspell package contains the hunspell spellchecking
plugin for %{name}.

%package	hspell
Summary:	hspell plugin for %{name}
Supplements:	(%{name} and langpacks-he)
Requires:	%{name} = %{version}-%{release}
Requires:	hunspell-he

Provides:       kf6-sonnet-hspell%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-sonnet-hspell < %{version}-%{release}

%description	hspell
The %{name}-hspell package contains the Hebrew hspell spellchecking
plugin for %{name}.

%package	voikko
Summary:	voikko plugin for %{name}
Supplements:	(%{name} and langpacks-fi)
Requires:	%{name} = %{version}-%{release}
Provides:       kf6-sonnet-voikko%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-sonnet-voikko < %{version}-%{release}

%description	voikko
The %{name}-voikko package contains the Finnish voikko spellchecking
plugin for %{name}.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
Provides:       kf6-sonnet-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-sonnet-devel < %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-sonnet-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-sonnet-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-sonnet-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-sonnet-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 sonnet6_qt

%files -f sonnet6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6SonnetCore.so.*
%{_kf6_bindir}/parsetrigrams6
%{_kf6_qmldir}/org/kde/sonnet/
%{_kf6_libdir}/libKF6SonnetUi.so.*

%files aspell
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_aspell.so

%files hunspell
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_hunspell.so

%files hspell
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_hspell.so

%files voikko
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_voikko.so


%files devel
%doc README.md
%license LICENSES/*.txt
%{_kf6_includedir}/Sonnet/
%{_kf6_includedir}/SonnetCore/
%{_kf6_includedir}/SonnetUi/
%{_kf6_libdir}/cmake/KF6Sonnet/
%{_kf6_libdir}/libKF6SonnetCore.so
%{_kf6_libdir}/libKF6SonnetUi.so
%{_kf6_qtplugindir}/designer/sonnet6widgets.so
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
