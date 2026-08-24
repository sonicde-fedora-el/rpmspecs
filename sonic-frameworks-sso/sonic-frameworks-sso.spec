# Generated for SonicDE from Fedora's signon.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-sso fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-sso
# Upstream KDE project: signond
%global oldname signon

%global gitdate 20240205
%global commit0 c8ad98249af541514ff7a81634d3295e712f1a39
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag0 VERSION_%{version}

#Name:           signon
Name:           sonic-frameworks-sso
Version:        8.61.2
Release:        1%{?dist}
Summary:        Accounts framework for Linux and POSIX based platforms

License:        LGPL-2.1-only
#URL:            https://gitlab.com/accounts-sso/signond
URL:            https://github.com/Sonic-DE/%{reponame}

# Temporary source, for plasma6 compatibility
#Source0:        https://gitlab.com/nicolasfella/signond/-/archive/%%{commit0}/signond-%%{commit0}.tar.gz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

# Original Sources
#%%if 0%%{?tag0:1}
#Source0:        https://gitlab.com/accounts-sso/signond/repository/archive.tar.gz?ref=%%{tag0}#/%%{name}-%%{version}.tar.gz
#%%else
#Source0:        https://gitlab.com/accounts-sso/signond/repository/archive.tar.gz?ref=%%{commit0}#/%%{name}-%%{shortcommit0}.tar.gz
#%%endif

BuildRequires: make
BuildRequires:  dbus-x11
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libproxy-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  time
BuildRequires:  qt6-qtbase-devel

# signon-qt5 was in ktp-5 COPR
Obsoletes:      signon-qt5 < 8.57-5
Provides:       signon-qt5 = %{version}-%{release}

# upstream name: signond
Provides:       signond = %{version}-%{release}

# conflicting implementation: gsignond
Conflicts:      gsignond

Requires:       dbus

Provides:       signon = %{version}-%{release}
Conflicts:      signon < %{version}-%{release}

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package qt5
Summary:        Single Sign On client library for Qt5-based applications
Provides:       signon-qt5 = %{version}-%{release}
Conflicts:      signon-qt5 < %{version}-%{release}

%description qt5
%{summary}.

%package qt6
Summary:        Single Sign On client library for Qt6-based applications
Provides:       signon-qt6 = %{version}-%{release}
Conflicts:      signon-qt6 < %{version}-%{release}

%description qt6
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# upstream name: signond
Provides:       signond-devel = %{version}-%{release}
Provides:       signon-devel = %{version}-%{release}
Conflicts:      signon-devel < %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package qt5-devel
Summary:        Development files for %{name}-qt5
Provides:       signon-qt5-devel = %{version}-%{release}
Conflicts:      signon-qt5-devel < %{version}-%{release}

%description qt5-devel
%{summary}.

%package qt6-devel
Summary:        Development files for %{name}-qt6
Provides:       signon-qt6-devel = %{version}-%{release}
Conflicts:      signon-qt6-devel < %{version}-%{release}

%description qt6-devel
%{summary}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

Provides:       signon-doc = %{version}-%{release}
Conflicts:      signon-doc < %{version}-%{release}

%description doc
The %{name}-doc package contains documentation for %{name}.


%prep
%autosetup -p1 -n %{reponame}-%{version}


%build
mkdir %{oldname}_qt5
pushd %{oldname}_qt5
%qmake_qt5 \
  CONFIG+=release \
  QMF_INSTALL_ROOT=%{_prefix} LIBDIR=%{_libdir} ../signon.pro
popd
%make_build -C %{oldname}_qt5

mkdir %{oldname}_qt6
pushd %{oldname}_qt6
%qmake_qt6 \
  CONFIG+=release \
  QMF_INSTALL_ROOT=%{_prefix} LIBDIR=%{_libdir} ../signon.pro
popd
%make_build -C %{oldname}_qt6

%install
make install INSTALL_ROOT=%{buildroot} -C %{oldname}_qt5
make install INSTALL_ROOT=%{buildroot} -C %{oldname}_qt6
# Removing additional unneeded files
rm %{buildroot}%{_libdir}/libsignon-qt5.a
rm %{buildroot}%{_libdir}/libsignon-qt6.a

# create/own libdir/extensions
mkdir -p %{buildroot}%{_libdir}/extensions/

%files
## fixme: common/shared _docdir/signon content below gets in the way
#doc README.md TODO NOTES
%license COPYING
%config(noreplace) %{_sysconfdir}/signond.conf
%{_bindir}/signond
%{_bindir}/signonpluginprocess
%{_libdir}/libsignon-extension.so.1*
%{_libdir}/libsignon-plugins-common.so.1*
%{_libdir}/libsignon-plugins.so.1*
%{_libdir}/signon/
%{_datadir}/dbus-1/services/*.service

%files qt5
%{_libdir}/libsignon-qt5.so.1{,.*}

%files qt6
%{_libdir}/libsignon-qt6.so.1{,.*}

%files devel
%{_includedir}/signon-extension/
%{_includedir}/signon-plugins/
%{_includedir}/signond/
%{_libdir}/libsignon-extension.so
%{_libdir}/libsignon-plugins-common.so
%{_libdir}/libsignon-plugins.so
%{_libdir}/pkgconfig/SignOnExtension.pc
%{_libdir}/pkgconfig/signon-plugins-common.pc
%{_libdir}/pkgconfig/signon-plugins.pc
%{_libdir}/pkgconfig/signond.pc

%files qt5-devel
%{_includedir}/signon-qt5/
%{_libdir}/cmake/SignOnQt5/
%{_libdir}/pkgconfig/libsignon-qt5.pc
%{_libdir}/libsignon-qt5.so

%files qt6-devel
%{_includedir}/signon-qt6/
%{_libdir}/cmake/SignOnQt6/
%{_libdir}/pkgconfig/libsignon-qt6.pc
%{_libdir}/libsignon-qt6.so

%files doc
%{_docdir}/signon/
%{_docdir}/libsignon-qt/
%{_docdir}/signon-plugins/
%{_docdir}/signon-plugins-dev/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 8.61.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
