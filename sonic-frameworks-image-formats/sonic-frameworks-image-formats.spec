# Generated for SonicDE from Fedora's kf6-kimageformats.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-image-formats fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-image-formats
# Upstream KDE project: kimageformats
%global oldname kf6-kimageformats

%undefine __cmake_in_source_build
%global framework kimageformats

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-image-formats
Version:        6.29.0
Release:        3%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with additional image plugins for QtGui

License:        LGPLv2+
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}

#Source0: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1: http://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

# upstream patches

BuildRequires:  sonic-frameworks-cmake-modules >= %{majmin_ver_kf6}.0
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sonic-rpm-macros
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  pkgconfig(cups)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(libavif)
BuildRequires:  pkgconfig(libheif) >= 1.10.0
%if !((0%{?fedora} && 0%{?fedora} < 41) || (0%{?rhel} && 0%{?rhel} < 10))
BuildRequires:  pkgconfig(libjxl) >= 0.9.4
BuildRequires:  pkgconfig(libjxl_threads) >= 0.9.4
BuildRequires:  pkgconfig(libjxl_cms) >= 0.9.4
%endif
BuildRequires:  cmake(OpenJPEG)
BuildRequires:  pkgconfig(libraw) >= 0.20.2
BuildRequires:  pkgconfig(libraw_r) >= 0.20.2
BuildRequires:  jxrlib-devel

Requires:       kf6-filesystem
# for eps plugin read/write support
Recommends:     poppler-utils
Recommends:     ghostscript

Provides:       kf6-kimageformats%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kimageformats < %{version}-%{release}

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf6-kimageformats-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kimageformats-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 \
  -DKIMAGEFORMATS_HEIF:BOOL=OFF \
  -DKIMAGEFORMATS_JXR:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_qtplugindir}/imageformats/*.so

%files devel
%{_kf6_libdir}/cmake/KF6ImageFormats/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
