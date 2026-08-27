# Generated for SonicDE from Fedora's kf6-bluez-qt.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-bluetooth fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-bluetooth
# Upstream KDE project: bluez-qt
%global oldname kf6-bluez-qt

%global framework bluez-qt
 
#Name:           kf6-%%{framework}
Name:           sonic-frameworks-bluetooth
Summary:        A Qt wrapper for Bluez
Version:        6.29.0
Release:        3%{?dist}
 
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
 
%global versiondir %(echo %{version} | cut -d. -f1-2)
#Source0: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

BuildRequires:  sonic-frameworks-cmake-modules >= %{version}
BuildRequires:  sonic-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:	gcc-c++
BuildRequires:  cmake
 
# For %%{_udevrulesdir}
BuildRequires:  systemd
 
Requires:       kf6-filesystem
Recommends:     bluez >= 5
 
Provides:       kf6-bluez-qt%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-bluez-qt < %{version}-%{release}

%description
BluezQt is Qt-based library written handle all Bluetooth functionality.
 
%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Provides:       kf6-bluez-qt-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-bluez-qt-devel < %{version}-%{release}

%description    devel
Development files for %{name}.
 
%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-bluez-qt-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-bluez-qt-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-bluez-qt-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-bluez-qt-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}
 
%build
 %{cmake_kf6} \
  -DUDEV_RULES_INSTALL_DIR:PATH="%{_udevrulesdir}"
%cmake_build_kf6
 
%install
%cmake_install_kf6

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_libdir}/libKF6BluezQt.so.*
%{_kf6_qmldir}/org/kde/bluezqt/
 
%files devel
%{_kf6_includedir}/BluezQt/ 
%{_kf6_libdir}/libKF6BluezQt.so
%{_kf6_libdir}/cmake/KF6BluezQt/
%{_kf6_libdir}/pkgconfig/KF6BluezQt.pc
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
