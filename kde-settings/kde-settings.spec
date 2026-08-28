%global debug_package %{nil}
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%bcond initialsetup_gui_backend 0
%else
%bcond initialsetup_gui_backend 0
%endif

Summary: Config files for KDE
Name:    kde-settings
Version: 44.0
Release: 2%{?dist}

License: MIT
URL:     https://forge.fedoraproject.org/kde/kde-settings
Source0: %{url}/archive/%{version}.tar.gz#/kde-settings-%{version}.tar.gz
Source1: COPYING

BuildArch: noarch

BuildRequires: kde-filesystem
# ssh-agent.service
BuildRequires: systemd-rpm-macros
Source10: ssh-agent.sh

# when kdebugrc was moved here
Conflicts: kf5-kdelibs4support < 5.7.0-3

Obsoletes: kde-settings-ksplash < 24-2
Obsoletes: kde-settings-minimal < 24-3

Requires: kde-filesystem
%if 0%{?el10}
Requires: xdg-user-dirs >= 0.18-7
%else
Requires: xdg-user-dirs >= 0.18-9
%endif
## add breeze deps here? probably, need more too -- rex
Requires: breeze-icon-theme
# Baseline mimeapps associations, e.g. LibreOffice
Requires: shared-mime-info

%description
%{summary}.

%package plasma
Summary: Configuration files for plasma
Requires: %{name} = %{version}-%{release}
Requires: google-noto-sans-fonts
# Not required but expected by users as we use other fonts from the noto "family"
Recommends: google-noto-serif-fonts
%if 0%{?rhel} && 0%{?rhel} < 9
Requires: google-noto-mono-fonts
%else
Requires: google-noto-sans-mono-fonts
%endif
%description plasma
%{summary}.

%package sddm
Summary: Configuration files for sddm
Requires: sddm
Requires: breeze-cursor-theme
%description sddm
%{summary}.

%package pulseaudio
Summary: Enable pulseaudio support in KDE
# nothing here to license
License: LicenseRef-Not-Copyrightable
Requires: %{name} = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 9
Requires: pulseaudio
%else
Requires: pulseaudio-daemon
%endif
## legacy apps
Requires: (pipewire-alsa if pipewire-pulseaudio)
Requires: (alsa-plugins-pulseaudio if pulseaudio)
%description pulseaudio
%{summary}.

%prep
%autosetup -n %{name} -p1

# omit crud
rm -fv Makefile

%build
# Intentionally left blank.  Nothing to see here.

%install
tar cpf - . | tar --directory %{buildroot} -xvpf -

if [ %{_prefix} != /usr ] ; then
   pushd %{buildroot}
   mv %{buildroot}/usr %{buildroot}%{_prefix}
   mv %{buildroot}/etc %{buildroot}%{_sysconfdir}
   popd
fi

cp -p %{SOURCE1} .

# Drop files from removed Wayland/qt-settings/plasmalogin subpackages
rm -f %{buildroot}%{_sysconfdir}/Trolltech.conf
rm -rf %{buildroot}%{_prefix}/lib/plasmalogin

# legacy default wallpaper symlink
mkdir -p %{buildroot}%{_datadir}/wallpapers
ln -s Default %{buildroot}%{_datadir}/wallpapers/Fedora

%if 0%{?rhel} && 0%{?rhel} < 9
# for rhel 8 and older with older noto fonts
sed -e "s/Noto Sans Mono/Noto Mono/g" \
    -i %{buildroot}%{_datadir}/kde-settings/kde-profile/default/{share/config/kdeglobals,xdg/kdeglobals}
%endif

# for ssh-agent.serivce, set SSH_AUTH_SOCK
install -p -m644 -D %{SOURCE10} %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/ssh-agent.sh

%if ! %{with initialsetup_gui_backend}
rm -rv %{buildroot}%{_libexecdir}/initial-setup
%endif

%check
test -e %{_datadir}/wallpapers/Default || ls -l %{_datadir}/wallpapers

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/profile.d/kde*
%{_sysconfdir}/fonts/conf.d/10-sub-pixel-rgb-for-kde.conf
%{_sysconfdir}/kde/env/env.sh
%{_sysconfdir}/kde/env/gpg-agent-startup.sh
%{_sysconfdir}/kde/shutdown/gpg-agent-shutdown.sh
%{_sysconfdir}/kde/env/gtk2_rc_files.sh
%if 0%{?fedora} || 0%{?rhel} > 7
%{_sysconfdir}/kde/env/fedora-bookmarks.sh
%{_datadir}/kde-settings/
# these can probably go now -- rex
%{_prefix}/lib/rpm/plasma4.prov
%{_prefix}/lib/rpm/plasma4.req
%{_prefix}/lib/rpm/fileattrs/plasma4.attr
%{_datadir}/polkit-1/rules.d/11-fedora-kde-policy.rules
%endif
%config(noreplace) %{_sysconfdir}/xdg/kcm-about-distrorc
%config(noreplace) %{_sysconfdir}/xdg/kdebugrc
%dir %{_sysconfdir}/pam.d
%config(noreplace) %{_sysconfdir}/pam.d/kcheckpass
%config(noreplace) %{_sysconfdir}/pam.d/kscreensaver
# drop noreplace, so we can be sure to get the new kiosk bits
%config %{_sysconfdir}/kderc
%config %{_sysconfdir}/kde4rc
%if 0%{?rhel} && 0%{?rhel} <= 7
%exclude %{_datadir}/kde-settings/kde-profile/default/share/apps/plasma-desktop/init/00-defaultLayout.js
%endif

%files plasma
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates/00-start-here-2.js
%{_sysconfdir}/xdg/plasma-workspace/env/env.sh
%{_sysconfdir}/xdg/plasma-workspace/env/gtk2_rc_files.sh
%{_sysconfdir}/xdg/plasma-workspace/env/gtk3_scrolling.sh
%dir %{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora*.desktop/contents/plasmoidsetupscripts/
%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora*.desktop/contents/plasmoidsetupscripts/org.kde.plasma.kicker.js
%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora*.desktop/contents/plasmoidsetupscripts/org.kde.plasma.kickerdash.js
%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora*.desktop/contents/plasmoidsetupscripts/org.kde.plasma.kickoff.js
%{_datadir}/wallpapers/Fedora
%{_sysconfdir}/xdg/plasma-workspace/env/ssh-agent.sh

%files sddm
%{_prefix}/lib/sddm/sddm.conf.d/kde_settings.conf

%files pulseaudio
# nothing, this is a metapackage

%changelog
* Fri Aug 28 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 44.0-2
- SonicDE build for Enterprise Linux 10
