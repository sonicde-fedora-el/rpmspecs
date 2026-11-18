# Based on Fedora's kf6.spec, reduced to the RPM macros.  The directories the
# frameworks install into are still owned by the distribution's kf6-filesystem
# package, which contains no code and therefore needs no fork.
%global sonicde_qt6_version 6.11.3
%global debug_package %{nil}

# Keep in sync with the SonicDE frameworks release train.
%global sonicde_frameworks_version 6.31.0
# Keep in sync with the SonicDE Plasma release train.
%global sonicde_plasma_version 6.8.2

Name:           sonic-rpm-macros
Version:        %{sonicde_frameworks_version}
Release:        8%{?dist}
Summary:        RPM macros for building SonicDE packages
License:        BSD-3-Clause
URL:            https://github.com/Sonic-DE
Source0:        macros.kf6
Source1:        LICENSE

BuildArch:      noarch

Requires:       cmake >= 3
Requires:       qt6-rpm-macros >= 6
Requires:       gcc-c++
Requires:       doxygen
Requires:       qt6-doc-devel
# Hard dep: COPR/mock buildroots do not install Recommends, and the
# doc targets run by the kf6 build macro need these template files.
Requires:       kde-qdoc-common
Requires:       qt6-qttools-devel >= 6.11
# Directory ownership only, no KDE code.
# NB: inline conditional, not the _sonicde_*_eq macros — this package
# cannot use its own macros during its own build (unexpanded text lands
# in the header).
Requires: kf6-filesystem >= 6.31

# SonicDE ships its own copy of the KF6 macros, so it replaces the ones from
# the distribution.
Provides:       kf6-rpm-macros = %{version}-%{release}
Conflicts:      kf6-rpm-macros < %{version}-%{release}

%description
RPM macros for building the SonicDE hard fork of KDE Frameworks 6 and Plasma
on Enterprise Linux 10 and Fedora.

%prep
%autosetup -c -T
cp -p %{SOURCE0} %{SOURCE1} .

%build
%{nil}

%install
install -Dpm644 macros.kf6 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6
install -Dpm644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
sed -i \
  -e "s|@@kf6_VERSION@@|%{sonicde_frameworks_version}|g" \
  -e "s|@@sonicde_frameworks_VERSION@@|%{sonicde_frameworks_version}|g" \
  -e "s|@@sonicde_plasma_VERSION@@|%{sonicde_plasma_version}|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6

%files
%license LICENSE
%{_rpmconfigdir}/macros.d/macros.kf6

%changelog
* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-8
- Flat >= 6.11 / >= 6.31 floors on ALL flavors (user decision): no EL/FC
  split anymore - identical dep expressions everywhere, nothing
  conditional left to expand wrongly in COPR's bare dist-git buildsrpm.
  Spec deps now use literal >= floors; _eq macros kept only for
  local-eval compatibility (never use them in spec dependency lines)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-7
- EL side of _sonicde_*_eq becomes >= <our version> floors: Qt6/KF6 patch
  bumps then roll out without rebuilding every consumer (= forced a
  full-tree rebuild per qt6 bump; >= still excludes EPEL's older qt6/kf6)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-6
- Leading space inside _sonicde_*_eq expansions: rpm does not split a
  glued operator, so name%{_eq} recorded name">=" plus the version as
  a separate bogus dep name. Requires space: name %{_eq} -> name >= V

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-5
- Inline the flavor-conditional Requires: this package cannot expand
  its own %{_sonicde_*_eq} macros during its own build, so -4 recorded
  literal macro text in its Requires (broke all COPR buildroots)

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.31.0-4
- Add %{_sonicde_qt6_eq}/%{_sonicde_kf6_eq} flavor pins: exact = on EL,
  >= 6.11 / >= 6.31 floors on Fedora so the distro's own Qt6/KF6 stack
  satisfies deps without forced downgrades

* Sat Nov 14 2026 Devin <devin@users.noreply.github.com> - 6.31.0-2
- kde-qdoc-common: Recommends -> Requires (mock skips weak deps, qdoc fails)

* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0.1-1
- Initial SonicDE macros package, based on Fedora's kf6.spec
