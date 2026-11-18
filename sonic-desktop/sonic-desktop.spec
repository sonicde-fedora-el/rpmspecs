Name:           sonic-desktop
Version:        6.8.2
Release:        4%{?dist}
Summary:        SonicDE desktop environment metapackage

License:        GPL-2.0-or-later
BuildArch:      noarch

# EPEL's sddm Recommends sddm-wayland-plasma, which ships a broken Plasma
# Wayland session entry; SonicDE is X11-only
Conflicts:      sddm-wayland-plasma

Requires:       sonic-activities
Requires:       sonic-activities-stats
Requires:       sonic-activity-manager-daemon
Requires:       sonic-audio-applet-pulse
Requires:       sonic-bluetooth-runtime
Requires:       sonic-breeze
Requires:       sonic-browser-integration
Requires:       sonic-daemon
Requires:       sonic-decoration
Requires:       sonic-desktop-interface
Requires:       sonic-disks
Requires:       sonic-dr-robotnik
Requires:       sonic-drawing-tablet
Requires:       sonic-ecco
Requires:       sonic-file-search-ui
Requires:       sonic-firewall
Requires:       sonic-gamma
Requires:       sonic-gtk-theme-bridge
Requires:       sonic-interface-libraries
Requires:       sonic-keybind-daemon
Requires:       sonic-keyboard
Requires:       sonic-launcher-menu-edit
Requires:       sonic-login-manager
Requires:       sonic-login-manager-selinux
Requires:       sonic-network-manager
Requires:       sonic-night-light
Requires:       sonic-oxygen
Requires:       sonic-oxygen-icons
Requires:       sonic-oxygen-sounds
Requires:       sonic-partition-manager
Requires:       sonic-pipewire
Requires:       sonic-plasma5-support-library
Requires:       sonic-polkit-agent
Requires:       sonic-power-management
Requires:       sonic-print-management
Requires:       sonic-qt-accounts-library
Requires:       sonic-qt-theme-bridge
Requires:       sonic-rdp-server
Requires:       sonic-screen
Requires:       sonic-screen-library
Requires:       sonic-screenies
Requires:       sonic-screenlocker
Requires:       sonic-silver-gtk
Requires:       sonic-silver-sound-theme
Requires:       sonic-silver-theme
Requires:       sonic-ssh-password-prompt
Requires:       sonic-sysguard-library
Requires:       sonic-system-info
Requires:       sonic-system-log
Requires:       sonic-system-monitor
Requires:       sonic-system-settings
Requires:       sonic-system-stats
Requires:       sonic-terminal
Requires:       sonic-terminal-tools
Requires:       sonic-theme-sdk
Requires:       sonic-thunderbolt
Requires:       sonic-vault
Requires:       sonic-welcome-center
Requires:       sonic-win
Requires:       sonic-workspace
Requires:       sonic-workspace-addons
Requires:       sonic-workspace-wallpapers
Requires:       sonic-workspace-x11
Requires:       sonic-write-daemon

Requires:       sonic-accounts-integration-qt6
Requires:       sonic-crypto-library-qt6
Requires:       sonic-crypto-library-qt6-ossl
Requires:       sonic-exiv2-library-qt6
Requires:       sonic-pulseaudio-library-qt6
Requires:       sonic-quick-image-editor-qt6
Requires:       sonic-frameworks-sso-qt6
Requires:       polkit-qt6-1

Requires:       sonic-frameworks-addons-downloader
Requires:       sonic-frameworks-app-info
Requires:       sonic-frameworks-archive
Requires:       sonic-frameworks-auth
Requires:       sonic-frameworks-autocomplete
Requires:       sonic-frameworks-barcode
Requires:       sonic-frameworks-bluetooth
Requires:       sonic-frameworks-bookmarks
Requires:       sonic-frameworks-color-scheme
Requires:       sonic-frameworks-core-addons
Requires:       sonic-frameworks-crash-handler
Requires:       sonic-frameworks-data-models
Requires:       sonic-frameworks-data-views
Requires:       sonic-frameworks-dbus
Requires:       sonic-frameworks-device-integration
Requires:       sonic-frameworks-doctools
Requires:       sonic-frameworks-feeds
Requires:       sonic-frameworks-file-metadata
Requires:       sonic-frameworks-file-search
Requires:       sonic-frameworks-file-search-file
Requires:       sonic-frameworks-file-search-libs
Requires:       sonic-frameworks-gui-addons
Requires:       sonic-frameworks-holidays
Requires:       sonic-frameworks-icon-themes
Requires:       sonic-frameworks-idle-tracker
Requires:       sonic-frameworks-image-formats
Requires:       sonic-frameworks-init-info
Requires:       sonic-frameworks-internationalization
Requires:       sonic-frameworks-io
Requires:       sonic-frameworks-io-extras
Requires:       sonic-frameworks-io-fuse
Requires:       sonic-frameworks-ipc
Requires:       sonic-frameworks-keybind
Requires:       sonic-frameworks-keyring
Requires:       sonic-frameworks-keyring-pam
Requires:       sonic-frameworks-logging
Requires:       sonic-frameworks-modemmanager
Requires:       sonic-frameworks-networkmanager
Requires:       sonic-frameworks-notification-settings
Requires:       sonic-frameworks-notifications
Requires:       sonic-frameworks-open-collab
Requires:       sonic-frameworks-package
Requires:       sonic-frameworks-progress-ui
Requires:       sonic-frameworks-pseudo-terminal
Requires:       sonic-frameworks-purpose
Requires:       sonic-frameworks-qml-bridge
Requires:       sonic-frameworks-qt-integration
Requires:       sonic-frameworks-quick-charts
Requires:       sonic-frameworks-quick-desktop-style
Requires:       sonic-frameworks-quick-silver-style
Requires:       sonic-frameworks-quick-ui
Requires:       sonic-frameworks-quick-ui-addons
Requires:       sonic-frameworks-root-shell
Requires:       sonic-frameworks-runner
Requires:       sonic-frameworks-settings
Requires:       sonic-frameworks-settings-ui
Requires:       sonic-frameworks-settings-utils
Requires:       sonic-frameworks-silver-icons
Requires:       sonic-frameworks-spell-check
Requires:       sonic-frameworks-sso
Requires:       sonic-frameworks-status-notification
Requires:       sonic-frameworks-svg
Requires:       sonic-frameworks-syntax-highlighting
Requires:       sonic-frameworks-text-codec
Requires:       sonic-frameworks-text-editor
Requires:       sonic-frameworks-text-widgets
Requires:       sonic-frameworks-ui-components
Requires:       sonic-frameworks-unit-conversion
Requires:       sonic-frameworks-user-feedback
Requires:       sonic-frameworks-via
Requires:       sonic-frameworks-widgets-addons
Requires:       sonic-frameworks-windowsystem
Requires:       sonic-frameworks-xml-gui
Requires:       sonic-frameworks-zeroconf

Requires:       xdg-desktop-portal-sonicde

Requires:       accounts-qml-module-qt6
Requires:       ark
Requires:       audiocd-kio
Requires:       baloo-widgets
Requires:       breeze-cursor-theme
Requires:       dolphin-plugins
Requires:       ffmpegthumbs
Requires:       flatpak
Requires:       flatpak-kcm
Requires:       kcharselect
Requires:       kde-inotify-survey
Requires:       kde-settings-plasma
Requires:       kdebugsettings
Requires:       kdegraphics-mobipocket
Requires:       kdegraphics-thumbnailers
Requires:       kdenetwork-filesharing
Requires:       kdialog
Requires:       kdnssd
Requires:       kdsoap-ws-discovery-client
Requires:       keditbookmarks
Requires:       kf6-kcalendarcore
Requires:       kf6-kcontacts
Requires:       kf6-kpeople
Requires:       kf6-ktexttemplate
Requires:       kf6-threadweaver
Requires:       kfind
Requires:       kio-admin
Requires:       kjournald
Requires:       kpmcore
Requires:       kwalletmanager5
Requires:       kwrite
Requires:       layer-shell-qt
Requires:       libkcddb
Requires:       libkdcraw
Requires:       libkgapi
Requires:       plasma-discover
Requires:       plasma-discover-flatpak
Requires:       qt6-qttranslations
Requires:       signon-plugin-oauth2

# the display manager cannot start a session without an X server;
# the name is provided by xlibre on EL10, by xorg-x11-server on Fedora
Requires:       xorg-x11-server-Xorg

# hard webengine consumers, excluded from ppc64le where qt6-qtwebengine
# cannot be built (upstream V8 port gap); weak deps so the metapackage
# still installs there
Recommends:     kaccounts-providers
Recommends:     khelpcenter
Recommends:     kio-gdrive
Recommends:     signon-ui


%description
SonicDE is a desktop environment forked from KDE Plasma 6 and KDE
Frameworks 6, tuned for X11. This metapackage installs the complete
desktop: the workspace, display manager, frameworks, applications and
the X server.

After installation, enable the display manager with:
    systemctl enable soniclogin.service


%files


%changelog
* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-4
- Require kde-inotify-survey: restored to the stack (kded module
  that warns when inotify limits are exceeded).

* Tue Nov 17 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-3
- Re-release; kde-settings stays in the stack (sonic-desktop-interface
  no longer obsoletes it), so Requires: kde-settings-plasma is kept.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-2
- Conflict with sddm-wayland-plasma: EPEL's sddm Recommends it, and its
  Plasma Wayland session entry is broken on this X11-only desktop.

* Mon Nov 16 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 6.8.2-1
- Metapackage pulling in the complete SonicDE desktop, so a single
  "dnf install sonic-desktop" installs a working system.
