%global debug_package %{nil}
%global framework kcontacts

Name:    kf6-%{framework}
Version: 6.29.0
Release: 1%{?dist}
Summary: The KContacts Library

# The following licenses are present in LICENSES but go unused: BSD-3-Clause, MIT, Unicode-DFS-2016
License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://projects.kde.org/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires: sonic-rpm-macros
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Config)
BuildRequires: cmake(KF6Codecs)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6I18n)
Requires:       cmake(KF6Codecs)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*%{framework}.*
%{_kf6_libdir}/libKF6Contacts.so.*
%{_kf6_qmldir}/org/kde/contacts/

%files devel
%{_kf6_includedir}/KContacts/
%{_kf6_libdir}/libKF6Contacts.so
%{_kf6_libdir}/cmake/KF6Contacts/
%{_kf6_qmldir}/org/kde/contacts/libkcontactsqml.so
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE build for Enterprise Linux 10
