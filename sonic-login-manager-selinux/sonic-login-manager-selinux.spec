Name:           sonic-login-manager-selinux
Version:        1.0
Release:        1%{?dist}
Summary:        SELinux policy module for Sonic Login Manager
License:        MIT
URL:            https://github.com/Sonic-DE/sonic-login-manager
Source0:        plasmalogin-selinux.te

BuildArch:      noarch

BuildRequires:  selinux-policy-devel
BuildRequires:  checkpolicy
Requires:       selinux-policy-targeted
Requires(post): policycoreutils
Requires(postun): policycoreutils

%description
SELinux policy module that allows Sonic Login Manager to launch
X11 user sessions when running under SELinux enforcing mode.

%prep
%setup -c -T
cp %{SOURCE0} .

%build
# Compile the SELinux type enforcement file into a loadable module package
checkmodule -M -m -o plasmalogin-selinux.mod plasmalogin-selinux.te
semodule_package -o plasmalogin-selinux.pp -m plasmalogin-selinux.mod

%install
install -D -m 644 plasmalogin-selinux.pp %{buildroot}%{_datadir}/selinux/packages/targeted/plasmalogin-selinux.pp

%post
# Load the SELinux policy module
semodule -i %{_datadir}/selinux/packages/targeted/plasmalogin-selinux.pp || :

%postun
if [ $1 -eq 0 ]; then
    # Remove the SELinux policy module on package uninstall
    semodule -r plasmalogin-selinux || :
fi

%files
%{_datadir}/selinux/packages/targeted/plasmalogin-selinux.pp

%changelog
* Tue Jun 30 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.0-1
- Initial package with SELinux allow rule for plasmalogin-helper-start-x11user
