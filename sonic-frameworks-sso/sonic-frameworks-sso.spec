# Generated for SonicDE from Fedora's signon.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-sso fork, not from download.kde.org.
# The SonicDE fork has migrated from qmake to CMake and is Qt6-only
# (find_package(Qt6 6.5 ...) in CMakeLists.txt), so this spec uses the
# CMake build system and no longer ships the Qt5 variant.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-sso
# Upstream KDE project: signond
%global oldname signon

#Name:           signon
Name:           sonic-frameworks-sso
Version:        8.61.2
Release:        6%{?dist}
Summary:        Accounts framework for Linux and POSIX based platforms

License:        LGPL-2.1-only
#URL:            https://gitlab.com/accounts-sso/signond
URL:            https://github.com/Sonic-DE/%{reponame}

Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel

# upstream name: signond
Provides:       signond%{?_isa} = %{version}-%{release}

# conflicting implementation: gsignond

Requires:       dbus

Provides:       signon%{?_isa} = %{version}-%{release}
# The EPEL signon package installs the same D-Bus service file and
# /etc/signond.conf.  Our fork has different library sonames (.so.0
# vs EPEL's .so.1), so signon-qt6 can still coexist, but the daemon
# package itself cannot.
Conflicts:      signon

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package qt6
Summary:        Single Sign On client library for Qt6-based applications
Provides:       signon-qt6%{?_isa} = %{version}-%{release}

%description qt6
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
# upstream name: signond
Provides:       signond-devel%{?_isa} = %{version}-%{release}
Provides:       signon-devel%{?_isa} = %{version}-%{release}
Provides:       signon-qt6-devel%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{reponame}-%{version}
# The fork's CMake tries to install D-Bus interface XML files that are
# not present in the repository.  Drop that install rule so the install
# step succeeds; the introspection data is not needed at runtime.
sed -i '/^install(FILES$/,/dbus-1\/interfaces)/d' cmake/signond/CMakeLists.txt


%build
%cmake -DBUILD_SIGNOND:BOOL=ON -DCMAKE_INSTALL_SYSCONFDIR=/etc
%cmake_build


%install
%cmake_install
# create/own libdir/signond/extensions
mkdir -p %{buildroot}%{_libdir}/signond/extensions/


%files
%license COPYING
%config(noreplace) %{_sysconfdir}/signond.conf
%{_libexecdir}/signond
%{_libdir}/libsignon-extension.so.0*
%{_libdir}/libsignon-plugins-common.so.0*
%{_libdir}/signond/
%{_datadir}/dbus-1/services/*.service

%files qt6
%{_libdir}/libsignon-qt6.so.0{,.*}

%files devel
%{_includedir}/signon-qt6/
%{_libdir}/cmake/SignOnQt6/
%{_libdir}/pkgconfig/libsignon-qt6.pc
%{_libdir}/libsignon-qt6.so
%{_libdir}/libsignon-extension.so
%{_libdir}/libsignon-plugins-common.so

%changelog
* Thu Aug 27 2026 SonicDE <dev@sonicde.org> - 8.61.2-6
- Add Conflicts: signon to prevent D-Bus service file clash with EPEL signon

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 8.61.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
