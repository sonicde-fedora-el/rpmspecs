%global sonicde_frameworks_version 6.31.0
%global debug_package %{nil}
%global sonicde_qt6_version 6.11.3
%global framework kcontacts

Name:    kf6-%{framework}
Version: 6.31.0
Release: 2%{?dist}
Summary: The KContacts Library

# The following licenses are present in LICENSES but go unused: BSD-3-Clause, MIT, Unicode-DFS-2016
License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://projects.kde.org/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
BuildRequires: sonic-frameworks-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires: sonic-rpm-macros
BuildRequires:  sonic-frameworks-core-addons-devel
BuildRequires:  sonic-frameworks-internationalization-devel
BuildRequires:  sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-text-codec-devel
BuildRequires:  qt6-qtbase-devel >= 6.11
BuildRequires:  qt6-qtdeclarative-devel >= 6.11
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       sonic-frameworks-core-addons-devel
Requires:       sonic-frameworks-internationalization-devel
Requires:       sonic-frameworks-text-codec-devel
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
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 6.31.0-1
- 6.31.0

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE build for Enterprise Linux 10
