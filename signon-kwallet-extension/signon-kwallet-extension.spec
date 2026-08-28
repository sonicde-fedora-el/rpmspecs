%undefine __cmake_in_source_build

Name:    signon-kwallet-extension
Version: 26.04.3
Release: 1%{?dist}
Summary: KWallet integration for Sign-on framework

License: GPL-2.0-or-later
URL:     https://invent.kde.org/network/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-frameworks-keyring-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  sonic-frameworks-sso-devel

Supplements:    (sonic-frameworks-keyring-libs and sonic-frameworks-sso)

%description
%{summary}.

%prep
%autosetup -p1

# Fix FindSignOnExtension.cmake to look for the actual header filename
# (upstream uses CamelCase but the SonicDE SSO fork installs lowercase headers)
sed -i 's|SignOn/AbstractSecretsStorage|SignOn/abstract-secrets-storage.h|' \
    cmake/modules/FindSignOnExtension.cmake

# Fix includes: SonicDE SSO fork uses lowercase header names
sed -i 's|#include <SignOn/ExtensionInterface>|#include <SignOn/extension-interface.h>|' \
    src/keyringplugin.h
sed -i 's|#include <SignOn/AbstractSecretsStorage>|#include <SignOn/abstract-secrets-storage.h>|' \
    src/keyringplugin.cpp src/secretsstorage.h src/secretsstorage.cpp

%build
%cmake_kf6 \
    -DQT_MAJOR_VERSION=6

%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/signond/extensions/libkeyring-kwallet.so

%changelog
* Fri Aug 28 2026 SonicDE <dev@sonicde.org> - 26.04.3-1
- Build 26.04.3 for SonicDE, link against sonic-frameworks-sso and sonic-frameworks-keyring
