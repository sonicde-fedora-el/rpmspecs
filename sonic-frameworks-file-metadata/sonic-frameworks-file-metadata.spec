# Generated for SonicDE from Fedora's kf6-kfilemetadata.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-file-metadata fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-file-metadata
# Upstream KDE project: kfilemetadata
%global oldname kf6-kfilemetadata

%global framework kfilemetadata

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-file-metadata
Summary:        A Tier 2 KDE Framework for extracting file metadata
Version:        6.29.0
Release:        3%{?dist}

License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(QMobipocket6)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig(exiv2) >= 0.20
# catdoc is dead upstream and will not be in epel10
# https://bugzilla.redhat.com/show_bug.cgi?id=2313773
%if %[!(0%{?rhel} >= 10)]
BuildRequires:  catdoc
Recommends:     catdoc
%endif
BuildRequires:  ebook-tools-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(xkbcommon)

Provides:       kf6-kfilemetadata%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kfilemetadata < %{version}-%{release}

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Provides:       kf6-kfilemetadata-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kfilemetadata-devel < %{version}-%{release}

%description devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kfilemetadata-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kfilemetadata-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-kfilemetadata-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kfilemetadata-html < %{version}-%{release}

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
mkdir -p %{buildroot}%{_kf6_plugindir}/kfilemetadata/writers/

%files -f %{oldname}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/kfilemetadata_dump6
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6FileMetaData.so.*
%dir %{_kf6_plugindir}/kfilemetadata/
%{_kf6_plugindir}/kfilemetadata/kfilemetadata_*.so
%dir %{_kf6_plugindir}/kfilemetadata/writers/
%{_kf6_plugindir}/kfilemetadata/writers/kfilemetadata_taglibwriter.so

%files devel
%{_kf6_libdir}/libKF6FileMetaData.so
%{_kf6_libdir}/cmake/KF6FileMetaData
%{_kf6_includedir}/KFileMetaData/
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
