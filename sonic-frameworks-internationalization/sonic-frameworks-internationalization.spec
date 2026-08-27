# Generated for SonicDE from Fedora's kf6-ki18n.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-internationalization fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-internationalization
# Upstream KDE project: ki18n
%global oldname kf6-ki18n

%global		framework ki18n

#Name:		kf6-%%{framework}
Name:           sonic-frameworks-internationalization
Version:        6.29.0
Release:        3%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon for localization
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND ODbl-1.0
#URL:		https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:	https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	sonic-frameworks-cmake-modules >= %{version}
BuildRequires:	gettext
BuildRequires:	sonic-rpm-macros
BuildRequires:	perl-interpreter
BuildRequires:	python3
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	pkgconfig(iso-codes)

Requires:	iso-codes
Requires:	kf6-filesystem

Provides:       kf6-ki18n%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ki18n < %{version}-%{release}

%description
KDE Frameworks 6 Tier 1 addon for localization.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	gettext
Requires:	python3
Provides:       kf6-ki18n-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ki18n-devel < %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-ki18n-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ki18n-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-ki18n-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-ki18n-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{oldname} --all-name

%files -f %{oldname}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6I18n.so.6
%{_kf6_libdir}/libKF6I18n.so.%{version}
%{_kf6_libdir}/libKF6I18nQml.so.6
%{_kf6_libdir}/libKF6I18nQml.so.%{version}
%{_kf6_libdir}/libKF6I18nLocaleData.so.6
%{_kf6_libdir}/libKF6I18nLocaleData.so.%{version}
%{_kf6_datadir}/qlogging-categories6/*%{framework}*
%{_kf6_qmldir}/org/kde/i18n/localeData/
%{_kf6_qmldir}/org/kde/ki18n/
%{_kf6_qtplugindir}/kf6/ktranscript.so
%lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS/ki18n6/
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_SCRIPTS/ki18n6/
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/ki18n6/
%lang(gd) %{_datadir}/locale/gd/LC_SCRIPTS/ki18n6/
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/ki18n6/
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/ki18n6/
%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/ki18n6/
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/ki18n6/
%lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS/ki18n6/
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/ki18n6/
%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/ki18n6/
%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n6/
%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/ki18n6/
%lang(sr) %{_datadir}/locale/uk/LC_SCRIPTS/ki18n6/

%files devel
%{_kf6_includedir}/KI18n/
%{_kf6_includedir}/KI18nLocaleData/
%{_kf6_libdir}/libKF6I18n.so
%{_kf6_libdir}/libKF6I18nQml.so
%{_kf6_libdir}/libKF6I18nLocaleData.so
%{_kf6_libdir}/cmake/KF6I18n/
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
