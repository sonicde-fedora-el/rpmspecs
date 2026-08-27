# Generated for SonicDE from Fedora's kquickimageeditor.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-quick-image-editor fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-quick-image-editor
# Upstream KDE project: kquickimageeditor
%global oldname kquickimageeditor

#Name:    kquickimageeditor
Name:           sonic-quick-image-editor
Version:        0.6.2.1.1
Release:        3%{?dist}
Summary: QtQuick components providing basic image editing capabilities
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
#URL:     https://invent.kde.org/libraries/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/stable/%%{name}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires: sonic-frameworks-cmake-modules

BuildRequires: sonic-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)

BuildRequires: cmake(KF6Config)

BuildRequires: cmake(OpenCV)

Provides:       kquickimageeditor%{?_isa} = %{version}-%{release}
Obsoletes:      kquickimageeditor < %{version}-%{release}

%description
%{summary}

%package qt6
Summary: Qt6 QtQuick components providing basic image editing capabilities

Provides:       kquickimageeditor-qt6%{?_isa} = %{version}-%{release}
Obsoletes:      kquickimageeditor-qt6 < %{version}-%{release}

%description qt6
%{summary}

%package qt6-devel
Summary: Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}

Provides:       kquickimageeditor-qt6-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kquickimageeditor-qt6-devel < %{version}-%{release}

%description qt6-devel
The %{name}-qt6-devel package contains cmake and mkspecs for developing
applications that use %{name}-qt6.

%prep
%autosetup -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files qt6
%{_kf6_qmldir}/org/kde/kquickimageeditor
%{_kf6_libdir}/libKQuickImageEditor.so.0.*
%{_kf6_libdir}/libKQuickImageEditor.so.1

%files qt6-devel
%{_kf6_libdir}/libKQuickImageEditor.so
%{_kf6_libdir}/cmake/KQuickImageEditor
%{_includedir}/KQuickImageEditor/
%{_kf6_archdatadir}/mkspecs/modules/qt_KQuickImageEditor.pri

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.6.2.1.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
