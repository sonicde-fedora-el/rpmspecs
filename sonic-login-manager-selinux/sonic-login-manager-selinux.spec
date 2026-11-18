Name:           sonic-login-manager-selinux
Version:        1.2
Release:        5%{?dist}
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
SELinux policy module that allows Sonic Login Manager to launch
X11 user sessions when running under SELinux enforcing mode.

%prep
%setup -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
# Compile the SELinux type enforcement file into a loadable module package
checkmodule -M -m -o plasmalogin-selinux.mod plasmalogin-selinux.te
semodule_package -o plasmalogin-selinux.pp -m plasmalogin-selinux.mod -f plasmalogin-selinux.fc

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
* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 1.2-4
- Allow xdm_t to start/stop/status systemd_unit_file_t services: the
  greeter session's user manager must launch soniclogin-x11.target
  (sonic-win compositor, wallpaper, apply-kscreen). Without it the
  greeter renders a black screen. Proven on the live dev image.

* Thu Nov 12 2026 Devin <devin@users.noreply.github.com> - 1.2-3
- Restore the unconfined_t -> xdm_exec_t entrypoint/execute allow: the
  helper re-execs start-x11user from the user's session context and the
  exec was denied (EACCES), breaking X11 login. Proven on the live dev
  image. File contexts from 1.1 are kept.

* Thu Nov 12 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.0-2
- Replace unconfined_t allow rule with file contexts labeling soniclogin
  binary, helpers, state and runtime dirs as xdm types

* Tue Jun 30 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.0-1
- Initial package with SELinux allow rule for plasmalogin-helper-start-x11user
