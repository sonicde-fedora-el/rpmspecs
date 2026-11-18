# SonicDE compat build of QCA (Qt Cryptographic Architecture) for Qt6.
# Fedora's qca-qt6 is linked against a different qt6 than the pinned
# SonicDE stack, so it cannot be installed in our buildroots on rawhide.
# This builds the qt6 flavour only; consumers use cmake(Qca-qt6).
%global sonicde_qt6_version 6.11.3

Name:           qca-qt6
Version:        2.3.12
Release:        1%{?dist}.sonicde1
Summary:        Qt Cryptographic Architecture (Qt6)
License:        LGPLv2+
URL:            https://invent.kde.org/libraries/qca
Source0:        https://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz

BuildRequires:  cmake >= 2.8.12
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel = %{sonicde_qt6_version}
BuildRequires:  qt6-qt5compat-devel = %{sonicde_qt6_version}
BuildRequires:  pkgconfig(libcrypto) pkgconfig(libssl)

%description
Qt Cryptographic Architecture built for Qt6. Compat package for the
SonicDE package set: upstream QCA built against the pinned SonicDE Qt
instead of the distribution qt6.

%prep
%autosetup -n qca-%{version}

%build
# https://fedoraproject.org/wiki/Changes/dropingOfCertPemFile
export QC_CERTSTORE_PATH=/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
%cmake -Wno-dev \
  -DQT6=ON \
  -DBUILD_TESTS:BOOL=OFF \
  -DQCA_INSTALL_IN_QT_PREFIX:BOOL=ON \
  -DQCA_BINARY_INSTALL_DIR:STRING=%{_bindir} \
  -DQCA_MAN_INSTALL_DIR:PATH=%{_mandir} \
  -DQCA_PLUGINS_INSTALL_DIR:PATH=%{_qt6_plugindir} \
  -DQCA_LIBRARY_INSTALL_DIR:PATH=%{_qt6_libdir} \
  -DQCA_FEATURE_INSTALL_DIR:PATH=%{_qt6_archdatadir}/mkspecs/features \
  -DQCA_INCLUDE_INSTALL_DIR:PATH=%{_qt6_headerdir} \
  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_qt6_headerdir}
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_qt6_libdir}/libqca-qt6.so.*
%{_qt6_plugindir}/crypto/
%{_bindir}/qcatool-qt6
%{_bindir}/mozcerts-qt6
%{_mandir}/man1/qcatool-qt6.1*

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.

%files devel
%{_qt6_headerdir}/QtCrypto/
%{_qt6_libdir}/libqca-qt6.so
%{_qt6_libdir}/cmake/Qca-qt6/

%changelog
* Tue Feb 10 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 2.3.12-1.sonicde1
- Compat build against the pinned SonicDE qt6 stack
