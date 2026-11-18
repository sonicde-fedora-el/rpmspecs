# Generated for SonicDE from Fedora's kquickimageeditor.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-quick-image-editor fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global sonicde_frameworks_version 6.31.0
%global reponame sonic-quick-image-editor
%global sonicde_qt6_version 6.11.3
# Upstream KDE project: kquickimageeditor
%global oldname kquickimageeditor

#Name:    kquickimageeditor
Name:           sonic-quick-image-editor
Version:        0.7.0.1
Release:        3%{?dist}
Summary: QtQuick components providing basic image editing capabilities
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
#URL:     https://invent.kde.org/libraries/%%{name}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0: https://download.kde.org/stable/%%{name}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires: sonic-frameworks-cmake-modules

BuildRequires: sonic-rpm-macros
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qtdeclarative-devel >= 6.11
BuildRequires: qt6-qtshadertools-devel >= 6.11

BuildRequires: sonic-frameworks-settings-devel

BuildRequires: highway-devel

Provides:       kquickimageeditor = %{version}-%{release}
Provides:       kquickimageeditor%{?_isa} = %{version}-%{release}
Obsoletes:      kquickimageeditor

%description
%{summary}

%package qt6
Summary: Qt6 QtQuick components providing basic image editing capabilities

Provides:       kquickimageeditor-qt6 = %{version}-%{release}
Provides:       kquickimageeditor-qt6%{?_isa} = %{version}-%{release}
Obsoletes:      kquickimageeditor-qt6

%description qt6
%{summary}

%package qt6-devel
Summary: Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}

Provides:       kquickimageeditor-qt6-devel = %{version}-%{release}
Provides:       kquickimageeditor-qt6-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kquickimageeditor-qt6-devel

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
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.7.0.1-3
- Drop version bound on fork Obsoletes so distro packages
  with a higher NVR (e.g. Fedora kf6-6.32) are replaced cleanly
  instead of producing file conflicts.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.7.0.1-2
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 0.6.2.1.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
