# Generated for SonicDE from Fedora's extra-cmake-modules.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-cmake-modules fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_qt6_version 6.11.3
%global reponame sonic-frameworks-cmake-modules
# Upstream KDE project: extra-cmake-modules
%global oldname extra-cmake-modules

%global framework extra-cmake-modules

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

#Name:    extra-cmake-modules
Name:           sonic-frameworks-cmake-modules
Summary: Additional modules for CMake build system
Version:        6.31.0
Release:        5%{?dist}
# kde-modules/clang-format.cmake is MIT
License: BSD-3-Clause AND BSD-2-Clause AND MIT
#URL:     https://api.kde.org/ecm/
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig
BuildArch:      noarch

## upstreamable patches
Patch0: ecm-deterministic-git-test.patch

# do not unconditionally link in base/core libpoppler library
Patch2: extra-cmake-modules-5.39.0-poppler_overlinking.patch

# test
Patch3: 0001-Revert-Add-PYTHONPATH-to-prefix.sh-if-python-is-avai.patch

## downstream patches

BuildRequires: sonic-rpm-macros
BuildRequires: make
# qcollectiongenerator
BuildRequires: qt5-qttools-devel
# sphinx-build
BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-qthelp
%global sphinx_build -DSphinx_BUILD_EXECUTABLE:PATH=%{_bindir}/sphinx-build-3

# Qt5Core is needed for tests to run properly (As-of 5.246.1).
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: qt6-qtbase-devel >= 6.11
%if 0%{?fedora} || 0%{?rhel} < 10
Requires: (kf5-rpm-macros if qt5-qtbase-devel)
%endif
Requires: (sonic-rpm-macros if qt6-qtbase-devel)
Recommends: appstream

Provides:       extra-cmake-modules = %{version}-%{release}
Obsoletes:      extra-cmake-modules

%description
Additional modules for CMake build system needed by KDE Frameworks.

%package        doc
Summary:        Developer Documentation files for %{name}
Provides:       extra-cmake-modules-doc = %{version}-%{release}
Obsoletes:      extra-cmake-modules-doc

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=ON \
  -DBUILD_MAN_DOCS:BOOL=OFF \
  -DBUILD_HTML_DOCS:BOOL=OFF \
  -DBUILD_QTHELP_DOCS:BOOL=ON \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  %{?sphinx_build}
%cmake_build

%install
%cmake_install

# move to qt6 docdir so it shows up in Qt Creator by default
mkdir %{buildroot}%{_qt6_docdir}
mv %{buildroot}%{_kf6_docdir}/ECM/*.qch %{buildroot}%{_qt6_docdir}/

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 300" -C %{_vpath_builddir} ||:
%endif

%files
%doc README.rst
%license LICENSES/*.txt
%{_datadir}/ECM/

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-5
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-4
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
