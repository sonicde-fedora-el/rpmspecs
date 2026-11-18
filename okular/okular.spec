%global sonicde_frameworks_version 6.31.0
%global debug_package %{nil}
%global sonicde_qt6_version 6.11.3
## uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%if 0%{?fedora}
%global chm 1
%global ebook 1
%global postscript 1
%endif
# uncomment to include -mobile (currently doesn't work)
# it links libokularpart.so, but fails to file/load at runtime
%global mobile 0
%endif

Name:    okular
Summary: A document viewer
Version: 26.08.3
Release: 3%{?dist}

License: GPL-2.0-only
URL:     https://www.kde.org/applications/graphics/okular/

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches (master branch)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: sonic-frameworks-cmake-modules
BuildRequires: sonic-rpm-macros
BuildRequires: sonic-frameworks-archive-devel
BuildRequires: sonic-frameworks-bookmarks-devel
BuildRequires: sonic-frameworks-autocomplete-devel
BuildRequires: sonic-frameworks-settings-devel
BuildRequires: sonic-frameworks-settings-ui-devel
BuildRequires: sonic-frameworks-core-addons-devel
BuildRequires: sonic-frameworks-crash-handler-devel
BuildRequires: sonic-frameworks-dbus-devel
BuildRequires: sonic-frameworks-doctools-devel
BuildRequires: sonic-frameworks-icon-themes-devel
BuildRequires: sonic-frameworks-io-devel
BuildRequires: sonic-frameworks-ui-components-devel
BuildRequires: kf6-threadweaver-devel >= 6.31
BuildRequires: sonic-frameworks-keyring-devel
BuildRequires: sonic-frameworks-windowsystem-devel

BuildRequires: qt6-qtbase-private-devel >= 6.11
BuildRequires: qt6-qtbase-devel >= 6.11
BuildRequires: qt6-qtsvg-devel >= 6.11
BuildRequires: qt6-qtdeclarative-devel >= 6.11

# okular-mobile
Requires: sonic-frameworks-purpose%{?_isa}

BuildRequires: pkgconfig(phonon4qt6)
BuildRequires: cmake(Qca-qt6)

## generater/plugin deps
BuildRequires: sonic-exiv2-library-qt6-devel
BuildRequires: cmake(QMobipocket6)
%if 0%{?chm}
BuildRequires: chmlib-devel
BuildRequires: pkgconfig(libzip)
%endif
%if 0%{?ebook}
BuildRequires: ebook-tools-devel
%endif
%if 0%{?postscript}
BuildRequires: pkgconfig(libspectre)
%endif
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libmarkdown)
BuildRequires: (pkgconfig(poppler-qt6) or fedora-release >= 46)
BuildRequires: pkgconfig(zlib)
%if 0%{?fedora}
BuildRequires: pkgconfig(ddjvuapi) 
%endif

%if !0%{?bootstrap}
BuildRequires:  qt6-qtspeech-devel >= 6.11
%endif

Requires: %{name}-part%{?_isa} = %{version}-%{release}

%description
%{summary}.

%if 0%{?mobile}
%package mobile
Summary: Document viewer for plasma mobile
# included last in okular-15.12.3-1.fc23
Obsoletes: okular-active < 16.04
%description mobile
%{summary}.
%endif

%package devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package  libs 
Summary:  Runtime files for %{name} 
%if 0%{?fedora}
# use Recommends to avoid hard deps -- rex
## lpr
Recommends: cups-client
## ps2pdf,pdf2ps
Recommends: ghostscript-core
%endif
%description libs 
%{summary}.

%package part
Summary: Okular kpart plugin
# translations moved here
Conflicts: kde-l10n < 17.03
%description part
%{summary}.


%prep
%autosetup -p1
# Skip poppler generator if installed poppler is too old
sed -i 's|if(Poppler_Qt6_FOUND)|if(Poppler_Qt6_FOUND AND Poppler_VERSION VERSION_GREATER_EQUAL "24.08.0")|' generators/CMakeLists.txt

%if ! 0%{?mobile}
# disable/omit mobile, it doesn't work -- rex
sed -i -e 's|^add_subdirectory( mobile )|#add_subdirectory( mobile )|' CMakeLists.txt
%endif


%build
%cmake_kf6 -DOKULAR_UI=desktop \
	-DFORCE_NOT_REQUIRED_DEPENDENCIES="CHM;LibZip;DjVuLibre;EPub;KF6Purpose;Qt6TextToSpeech;Poppler%{!?postscript:;LibSpectre}"

%cmake_build


%install
%cmake_install

%find_lang all --all-name --with-html --with-man
grep -v \
  -e %{_mandir} \
  -e %{_kf6_docdir} \
  all.lang > okular-part.lang
cat all.lang okular-part.lang | sort | uniq -u > okular.lang


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.okular.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.okular.appdata.xml
%if 0%{?mobile}
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.okular.kirigami.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.okular.kirigami.appdata.xml
%endif

%files -f okular.lang
%license LICENSES/*
%{_kf6_bindir}/okular
%{_kf6_datadir}/applications/org.kde.okular.desktop
%{_kf6_metainfodir}/org.kde.okular.appdata.xml
%{_kf6_datadir}/applications/okularApplication_*.desktop
%{_kf6_metainfodir}/org.kde.okular-*.metainfo.xml
%{_kf6_datadir}/okular/
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/okular.1*
%{_kf6_datadir}/qlogging-categories6/okular.categories

%if 0%{?mobile}
%files mobile
%{_kf6_bindir}/okularkirigami
%{_qt6_qmldir}/org/kde/okular/
%{_kf6_metainfodir}/org.kde.okular.kirigami.appdata.xml
%{_kf6_datadir}/applications/org.kde.okular.kirigami.desktop
%{_kf6_datadir}/applications/org.kde.mobile.okular_*.desktop
%endif

%files devel
%{_includedir}/okular/
%{_libdir}/libOkular6Core.so
%{_libdir}/cmake/Okular6/

%ldconfig_scriptlets libs

%files libs
%{_libdir}/libOkular6Core.so.*

%files part -f okular-part.lang
%if 0%{?fedora}
# Disabled upstream?
# %%{_kf6_plugindir}/kio/kio_msits.so
%endif
%{_kf6_datadir}/config.kcfg/*.kcfg
%dir %{_qt6_plugindir}/okular_generators/
%{_qt6_plugindir}/okular_generators/okularGenerator_*.so
%{_kf6_plugindir}/parts/okularpart.so


%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-3
- Relax Qt6/KF6 version pins via %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq}:
  exact = on EL, >= floor on Fedora so the distro Qt6/KF6 stack
  satisfies deps (soft transition, no forced downgrade)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.08.3-2
- Pin cmake() BuildRequires to SonicDE package names so the
  alma+epel-10 solver cannot pick EPEL's Qt 6.10-linked providers
* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 26.08.3-1
- 26.08.3

* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 26.04.3-1
- SonicDE build for Enterprise Linux 10
