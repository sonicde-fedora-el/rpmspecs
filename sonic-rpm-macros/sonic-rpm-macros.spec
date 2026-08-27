# Based on Fedora's kf6.spec, reduced to the RPM macros.  The directories the
# frameworks install into are still owned by the distribution's kf6-filesystem
# package, which contains no code and therefore needs no fork.
%global debug_package %{nil}

# Keep in sync with the SonicDE frameworks release train.
%global sonicde_frameworks_version 6.29.0.1
# Keep in sync with the SonicDE Plasma release train.
%global sonicde_plasma_version 6.7.4.6

Name:           sonic-rpm-macros
Version:        %{sonicde_frameworks_version}
Release:        3%{?dist}
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
Recommends:      kde-qdoc-common
Requires:       cmake(Qt6ToolsTools)
# Directory ownership only, no KDE code.
Requires:       kf6-filesystem

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
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.29.0.1-1
- Initial SonicDE macros package, based on Fedora's kf6.spec
