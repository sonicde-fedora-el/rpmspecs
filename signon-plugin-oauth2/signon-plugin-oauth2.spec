%global gitdate 20231216
%global commit0 fab698862466994a8fdc9aa335c87b4f05430ce6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           signon-plugin-oauth2
Version:        0.25^%{gitdate}.%{shortcommit0}
Release:        5%{?dist}
Summary:        OAuth2 plugin for the Accounts framework

License:        LGPL-2.1-or-later
URL:            https://gitlab.com/accounts-sso/signon-plugin-oauth2

Source0:        https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/archive/%{commit0}/%{name}-%{commit0}.tar.gz

BuildRequires: make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  sonic-frameworks-sso-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libproxy-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
%qmake_qt6 \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    CONFIG+=nomake_tests \
    LIBDIR=%{?_libdir} \
    signon-oauth2.pro

%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# Delete examples (if built)
rm -fv %{buildroot}/%{_bindir}/oauthclient 2>/dev/null || true
rm -rvf %{buildroot}/%{_sysconfdir} 2>/dev/null || true

%files
%{_libdir}/signond/liboauth2plugin.so

%files devel
%{_includedir}/signon-plugins/*.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc

%changelog
* Fri Aug 28 2026 SonicDE <dev@sonicde.org> - 0.25^20231216.fab6988-5
- Bump release to 5 to supersede EPEL's release 4

* Fri Aug 28 2026 SonicDE <dev@sonicde.org> - 0.25^20231216.fab6988-1
- Build for SonicDE, link against sonic-frameworks-sso
