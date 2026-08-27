# Generated for SonicDE from Fedora's kf6-syntax-highlighting.spec.
# SonicDE is a hard fork of KDE Plasma; the sources come from the
# https://github.com/Sonic-DE/sonic-frameworks-syntax-highlighting fork, not from download.kde.org.
%define _disable_source_fetch 0
%define debug_package %{nil}
%global reponame sonic-frameworks-syntax-highlighting
# Upstream KDE project: syntax-highlighting
%global oldname kf6-syntax-highlighting

%global framework syntax-highlighting

#Name:           kf6-%%{framework}
Name:           sonic-frameworks-syntax-highlighting
Version:        6.29.0
Release:        3%{?dist}
Summary:        KDE Frameworks 6 Syntax highlighting engine for Kate syntax definitions
License:        MIT AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later
#URL:            https://invent.kde.org/frameworks/%%{framework}
URL:            https://github.com/Sonic-DE/%{reponame}
#Source0:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
#Source1:        https://download.kde.org/%%{stable_kf6}/frameworks/%%{majmin_ver_kf6}/%%{framework}-%%{version}.tar.xz.sig

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# KDE Frameworks
BuildRequires:  sonic-frameworks-cmake-modules

# Fedora
Requires:       kf6-filesystem
BuildRequires:  sonic-rpm-macros

# Other
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(xerces-c)

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)

Provides:       kf6-syntax-highlighting%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-syntax-highlighting < %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf6-syntax-highlighting-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-syntax-highlighting-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-syntax-highlighting-doc%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-syntax-highlighting-doc < %{version}-%{release}

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
Provides:       kf6-syntax-highlighting-html%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-syntax-highlighting-html < %{version}-%{release}

%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=ON
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 syntaxhighlighting6_qt

%check
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:

%files -f syntaxhighlighting6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/ksyntaxhighlighter6
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6SyntaxHighlighting.so.6
%{_kf6_libdir}/libKF6SyntaxHighlighting.so.%{version}
%{_kf6_qmldir}/org/kde/syntaxhighlighting

%files devel
%{_kf6_includedir}/KSyntaxHighlighting/
%{_kf6_libdir}/libKF6SyntaxHighlighting.so
%{_kf6_libdir}/cmake/KF6SyntaxHighlighting/
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0-1
- SonicDE hard fork build for Enterprise Linux 10 and Fedora
