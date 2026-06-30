# SonicDE for Enterprise Linux 10

This repository contains both source code and instructions on how to install the SonicDE third-party packages on Enterprise Linux 10 distributions like [AlmaLinux](https://almalinux.org/), [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux), [Oracle Linux](https://www.oracle.com/linux), and [Rocky Linux](https://rockylinux.org).

## Installation Instructions

Step 1: Since EL10 doesn't have any X11 server by default or in the official repos, you need to install one. We recommend using the XLibre X11 server.
Follow the installation instructions on the [XLibre for Fedora and EL Github page](https://github.com/xlibre-fedora-el/rpmspecs)

Step 2: Enable the repository

Add the SonicDE repository to your system:

```shell
sudo dnf config-manager --add-repo https://copr.fedorainfracloud.org/coprs/g/SonicDE/SonicDE-EL10/repo/rhel+epel-10/group_SonicDE-SonicDE-EL10-rhel+epel-10.repo
```

Step 3: Install the SonicDE packages and other needed X11 packages.

When XLibre has been installed, you can install the SonicDE packages and other needed X11 packages by running this command:

```shell
sudo dnf install --allowerasing xorg-x11-xinit xkbcomp xinput xrandr sonic-workspace sonic-workspace-libs sonic-workspace-common sonic-workspace-x11 sonic-win sonic-desktop-interface sonic-interface-libraries sonic-keybind-daemon sonic-frameworks-windowsystem sonic-system-info sonic-screen sonic-screen-library sonic-sysguard-library
```

Step 4: Install Sonic Login Manager

This step may be optional, but it is recommended. It may or may not work with SDDM Wayland, but I know that it works with Sonic Login Manager.

Install it with the following command:

```shell
sudo dnf remove sddm && \
    sudo dnf install --allowerasing sonic-login-manager
```

Step 5: Reboot your system

Now reboot your system. When it starts the display manager, then in the left corner make sure to choose Plasma (X11) as the session type.