# Written from scratch: a pure QML theme with no build system.
%define _disable_source_fetch 0
%global debug_package %{nil}
%global reponame silver-sddm

Name:           silver-sddm
Version:        1.0.0
Release:        1%{?dist}
Summary:        Sonic Silver login screen themes for SonicDE
License:        GPL-2.0-or-later
URL:            https://github.com/Sonic-DE/%{reponame}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildArch:      noarch

Requires:       sddm
Requires:       qt6-qtdeclarative
Requires:       qt6-qt5compat

%description
The Sonic Silver login screen themes, in a light and a dark variant, for the
SonicDE login manager.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%{nil}

%install
mkdir -p %{buildroot}%{_datadir}/sddm/themes
cp -a Sonic-Silver Sonic-Silver-Light %{buildroot}%{_datadir}/sddm/themes/

%files
%license LICENSE.md
%doc README.md CHANGELOG
%{_datadir}/sddm/themes/Sonic-Silver/
%{_datadir}/sddm/themes/Sonic-Silver-Light/

%changelog
* Mon Aug 24 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.0.0-1
- Initial SonicDE package
