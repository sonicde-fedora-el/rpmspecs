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
Release:        9%{?dist}
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

# Install plugin development files (CMake fork doesn't install these)
# Plugin headers
mkdir -p %{buildroot}%{_includedir}/signon-plugins/SignOn
cp -a %{_builddir}/%{reponame}-%{version}/lib/plugins/SignOn/*.h \
      %{buildroot}%{_includedir}/signon-plugins/SignOn/
cp -a %{_builddir}/%{reponame}-%{version}/lib/plugins/*.h \
      %{buildroot}%{_includedir}/signon-plugins/ 2>/dev/null || true
cp -a %{_builddir}/%{reponame}-%{version}/src/plugins/example/exampledata.h \
      %{buildroot}%{_includedir}/signon-plugins/ 2>/dev/null || true
cp -a %{_builddir}/%{reponame}-%{version}/src/plugins/example/exampleplugin.h \
      %{buildroot}%{_includedir}/signon-plugins/ 2>/dev/null || true
cp -a %{_builddir}/%{reponame}-%{version}/src/plugins/password/passwordplugin.h \
      %{buildroot}%{_includedir}/signon-plugins/ 2>/dev/null || true
# Create CamelCase forwarding headers (upstream plugins use #include <SignOn/AuthPluginInterface>)
# AuthPluginInterface -> authpluginif.h (note: not authplugininterface.h)
echo "#include <SignOn/authpluginif.h>" > %{buildroot}%{_includedir}/signon-plugins/SignOn/AuthPluginInterface
echo "#include <SignOn/uisessiondata.h>" > %{buildroot}%{_includedir}/signon-plugins/SignOn/UiSessionData
# Error and SessionData are in signon-qt6, but plugins include them via SignOn/
# Create forwarding headers that point to the qt6 versions
echo "#include <SignOn/signonerror.h>" > %{buildroot}%{_includedir}/signon-plugins/SignOn/Error
echo "#include <SignOn/sessiondata.h>" > %{buildroot}%{_includedir}/signon-plugins/SignOn/SessionData
# Copy the actual qt6 headers that plugins need (signonerror.h, sessiondata.h, libsignoncommon.h)
# since the forwarding headers above include them from SignOn/ which resolves
# to signon-plugins/SignOn/
cp -a %{buildroot}%{_includedir}/signon-qt6/SignOn/signonerror.h \
      %{buildroot}%{_includedir}/signon-plugins/SignOn/ 2>/dev/null || true
cp -a %{buildroot}%{_includedir}/signon-qt6/SignOn/sessiondata.h \
      %{buildroot}%{_includedir}/signon-plugins/SignOn/ 2>/dev/null || true
cp -a %{buildroot}%{_includedir}/signon-qt6/SignOn/libsignoncommon.h \
      %{buildroot}%{_includedir}/signon-plugins/SignOn/ 2>/dev/null || true
# Extension headers
mkdir -p %{buildroot}%{_includedir}/signon-extension/SignOn
cp -a %{_builddir}/%{reponame}-%{version}/lib/signond/SignOn/*.h \
      %{buildroot}%{_includedir}/signon-extension/SignOn/
# signond internal headers (needed by some plugins)
mkdir -p %{buildroot}%{_includedir}/signond
cp -a %{_builddir}/%{reponame}-%{version}/src/signond/*.h \
      %{buildroot}%{_includedir}/signond/ 2>/dev/null || true
# Create pkgconfig files (the .pc.in templates use qmake $$ syntax, not CMake)
cat > %{buildroot}%{_libdir}/pkgconfig/signon-plugins.pc << 'PCEOF'
prefix=/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include
plugin_includedir=${includedir}/signon-plugins/SignOn
plugindir=${libdir}/signond

Name: signon-plugins
Description: SignonPlugins
Version: %{version}
Libs: -L${libdir} -lsignon-plugins-common
Cflags: -I${includedir}/signon-plugins -I${includedir}/signon-plugins/SignOn
PCEOF
cat > %{buildroot}%{_libdir}/pkgconfig/SignOnExtension.pc << 'PCEOF'
prefix=/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include
plugindir=${libdir}/signond/extensions

Name: SignOnExtension
Description: SignOn extension development
Version: %{version}
Requires: Qt6Core
Libs: -L${libdir} -lsignon-extension
Cflags: -I${includedir}/signon-extension
PCEOF
cat > %{buildroot}%{_libdir}/pkgconfig/signon-plugins-common.pc << 'PCEOF'
prefix=/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include
plugin_includedir=${includedir}/signon-plugins/SignOn

Name: signon-plugins-common
Description: SignonPluginsCommon
Version: %{version}
Libs: -L${libdir} -lsignon-plugins-common
Cflags: -I${includedir}/signon-plugins -I${includedir}/signon-plugins/SignOn
PCEOF
# Create libsignon-plugins.so symlink (plugins link against this)
ln -sf libsignon-plugins-common.so %{buildroot}%{_libdir}/libsignon-plugins.so


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
%{_includedir}/signon-plugins/
%{_includedir}/signon-extension/
%{_includedir}/signond/
%{_libdir}/cmake/SignOnQt6/
%{_libdir}/pkgconfig/libsignon-qt6.pc
%{_libdir}/pkgconfig/signon-plugins.pc
%{_libdir}/pkgconfig/SignOnExtension.pc
%{_libdir}/pkgconfig/signon-plugins-common.pc
%{_libdir}/libsignon-qt6.so
%{_libdir}/libsignon-extension.so
%{_libdir}/libsignon-plugins-common.so
%{_libdir}/libsignon-plugins.so

%changelog
* Fri Aug 28 2026 SonicDE <dev@sonicde.org> - 8.61.2-9
- Fix forwarding headers: AuthPluginInterface->authpluginif.h, add libsignoncommon.h

* Fri Aug 28 2026 SonicDE <dev@sonicde.org> - 8.61.2-8
- Add CamelCase forwarding headers and qt6 headers for plugin builds

* Fri Aug 28 2026 SonicDE <dev@sonicde.org> - 8.61.2-7
- Install plugin development files (headers, pkgconfig, symlinks) needed
  to build signon-plugin-oauth2 and signon-kwallet-extension against SSO

* Thu Aug 27 2026 SonicDE <dev@sonicde.org> - 8.61.2-6
- Add Conflicts: signon to prevent D-Bus service file clash with EPEL signon

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 8.61.2-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
