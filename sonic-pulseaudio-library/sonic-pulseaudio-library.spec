# Generated for SonicDE from Fedora's pulseaudio-qt.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-pulseaudio-library fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-pulseaudio-library
# Upstream KDE project: pulseaudio-qt
%global oldname pulseaudio-qt

#Name:    pulseaudio-qt
Name:           sonic-pulseaudio-library
Summary: Qt bindings for PulseAudio
Version:        1.8.1
Release:        1%{?dist}

License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
#URL:     https://invent.kde.org/libraries/pulseaudio-qt
URL:            https://github.com/Sonic-DE/%{reponame}
#Source:  https://download.kde.org/stable/%%{name}/%%{name}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildRequires:  sonic-frameworks-cmake-modules
BuildRequires:  sonic-rpm-macros
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)

Provides:       pulseaudio-qt = %{version}-%{release}
Conflicts:      pulseaudio-qt < %{version}-%{release}

%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package qt6
Summary: Qt6 bindings for PulseAudio
Provides:       pulseaudio-qt-qt6 = %{version}-%{release}
Conflicts:      pulseaudio-qt-qt6 < %{version}-%{release}

%description qt6
%{summary}.

%package qt6-devel
Summary: Development files for %{name} (Qt6)
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Provides:       pulseaudio-qt-qt6-devel = %{version}-%{release}
Conflicts:      pulseaudio-qt-qt6-devel < %{version}-%{release}

%description qt6-devel
%{summary}.

%package qt6-doc
Summary: Developer Documentation files for %{name}
Provides:       pulseaudio-qt-qt6-doc = %{version}-%{release}
Conflicts:      pulseaudio-qt-qt6-doc < %{version}-%{release}

%description qt6-doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.


%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_kf6_includedir}/pulseaudioqt_version.h

%files qt6
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKF6PulseAudioQt.so.5
%{_kf6_libdir}/libKF6PulseAudioQt.so.%{version}

%files qt6-devel
%{_kf6_includedir}/KF6PulseAudioQt/
%{_kf6_libdir}/libKF6PulseAudioQt.so
%{_kf6_libdir}/cmake/KF6PulseAudioQt/
%{_kf6_libdir}/pkgconfig/KF6PulseAudioQt.pc
%{_qt6_docdir}/*.tags

%files qt6-doc
%{_qt6_docdir}/*.qch

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.8.1-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
