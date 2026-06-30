Name:           sonic-login-manager-selinux
Version:        1.0.1
Release:        1%{?dist}
Summary:        SELinux policy module for Sonic Login Manager
License:        MIT
URL:            https://github.com/Sonic-DE/sonic-login-manager
Source0:        plasmalogin-selinux.te
Source1:        plasmalogin-selinux.fc

BuildArch:      noarch

BuildRequires:  selinux-policy-devel
BuildRequires:  checkpolicy
Requires:       selinux-policy-targeted
Requires(post): policycoreutils
Requires(postun): policycoreutils

%description
SELinux policy module that labels the Sonic Login Manager binaries as
xdm_exec_t so systemd runs the daemon in the xdm_t domain. This lets
Sonic Login Manager launch X11 user sessions under SELinux enforcing
mode without granting broad unconfined_t permissions.

%prep
%setup -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
# Compile the SELinux type enforcement file and file context rules into a loadable module package
checkmodule -M -m -o plasmalogin-selinux.mod plasmalogin-selinux.te
semodule_package -o plasmalogin-selinux.pp -m plasmalogin-selinux.mod -f plasmalogin-selinux.fc

%install
install -D -m 644 plasmalogin-selinux.pp %{buildroot}%{_datadir}/selinux/packages/targeted/plasmalogin-selinux.pp

%post
# Load the SELinux policy module and apply file contexts to the plasmalogin binaries
semodule -i %{_datadir}/selinux/packages/targeted/plasmalogin-selinux.pp || :
restorecon -Rv /usr/bin/plasmalogin /usr/libexec/plasmalogin-helper /usr/libexec/plasmalogin-helper-start-x11user /usr/libexec/plasma-login-greeter || :

%postun
if [ $1 -eq 0 ]; then
    # Remove the SELinux policy module and restore default file contexts on uninstall
    semodule -r plasmalogin-selinux || :
    restorecon -Rv /usr/bin/plasmalogin /usr/libexec/plasmalogin-helper /usr/libexec/plasmalogin-helper-start-x11user /usr/libexec/plasma-login-greeter || :
fi

%files
%{_datadir}/selinux/packages/targeted/plasmalogin-selinux.pp

%changelog
* Tue Jun 30 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.0.1-1
- Use with file context rules labeling plasmalogin binaries as xdm_exec_t instead

* Tue Jun 30 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.0-1
- Initial package with SELinux allow rule for plasmalogin-helper-start-x11user