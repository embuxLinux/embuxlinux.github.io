# Installation Guide

```{div} lead
A detailed guide on how to install Embux.
```

```{warning}
Embux installation is not a trivial task and requires technical expertise. It is recommended for experienced users only.
```

```{admonition} TL;DR
Installing Embux involves flashing it onto a USB or SD card, inserting that storage into the target, configuring that target to boot into it, then reboot it.
```

## Prerequisites

Before embarking on the Embux installation process, ensure that you have the necessary prerequisites in place:

* **Technical Expertise:** Possess a strong understanding of Linux systems, embedded systems, and networking concepts.

* **Target Computer:** A target computer with at least 10 MB of RAM. **For Raspberry Pis, see [here](/install_raspberry.html).**

* **Source Computer:** A source computer with access to the internet and the ability to install software. This could be your personal laptop, a desktop workstation, or even a cloud-based virtual machine.

* **Storage**: A USB drive or SD card with at least 2 GB. Insert it into the source computer.

## Signing

Remember to validate the Embux image. Custom images could have malware, including software that could brick the entire device.

### Instructions

::::{tab-set}

:::{tab-item} Linux/macOS
:sync: linux
Run this command in the directory where you downloaded the Embux app:

```
./embux-app-*.sh --sign
```
:::

:::{tab-item} Windows
:sync: win

Open the Embux app and enter the Konami code:
```
↑ ↑ ↓ ↓ ← → ← → B A
```
:::

:::{tab-item} Other or ISO
:sync: other

```{warning}
No known multi-platform signing solution is known by the Embux project. The closest option known is GPG. Your only hope is being vigilant of malicious images. Stay safe on the internet.
```

::::

## Installation Process

::::{tab-set}

:::{tab-item} Linux and macOS
:sync: linux

1. **Download Embux App:** Download the appropriate Embux app shell script (.sh) from the Embux GitHub repository.
   * Please note there are different versions of the shell script for Linux and Mac, the macOS version is labelled `darwin`.
   * You can find a link to the repository in the sidebar.
   * For macOS (not Linux), you will need to install [Homebrew](https://brew.sh). Don't worry, installing Homebrew is a very simple task. You have to run one single command.
   * **Warning:** Don't use packages provided by your system's repositories, AUR, etc. These repositories have been known for hosting outdated software.

3. **Ensure Execution Permissions:** Make sure the script has executable permissions. You can do this by running the following command in the terminal:

    ```bash
    chmod +x embux-app-*.sh
    ```

4. **Optional: Sideload a Custom Embux Image:** If you want to install Embux Beta, a testing version of Embux, or any modified version of Embux, store the ISO in `~/.embux.iso`.

5. **Run Embux App:** Run the Embux app by executing the following command:

    ```bash
    ./embux-app-*.sh
    ```

6. **Follow Embux App Instructions:** The Embux app will guide you through the installation process, including selecting the target device, and initiating the installation.

7. **Monitor Installation Progress:** Observe the progress bar in the Embux app as the installation unfolds. Once the installation is complete, a notification will appear.

8. **Boot Target Device:** Once the installation is complete, power cycle the target device, and insert the Embux device. The device should boot into the newly installed Embux system.
:::

:::{tab-item} Windows
:sync: win

```{warning}
The Embux app is not designed for Windows. Consider installing Linux on the source computer, then follow the procedure for Linux.
```

1. **Download Embux App:** Download the appropriate Embux app executable (.exe) from the Embux GitHub repository.
   * Please note there are 3 builds for Windows: `x86`, `x66_64`, and `arm`. You can still use `x86_64` and `x86` on ARM, but they are not native to ARM processors. Similarly you can still use `x86` on `x86_64` but not `arm`.
   * You can find a link to the repository in the sidebar.
   * **Warning:** Don't use packages provided by chocolatey, etc. These repositories have been known for hosting outdated software.

3. **Optional: Sideload a Custom Embux Image:** If you want to install Embux Beta, a testing version of Embux, or any modified version of Embux, store the ISO in `C:\Embux.iso`.

4. **Run Embux App:** Run the Embux app by finding it in your downloads folder.

5. **Follow Embux App Instructions:** The Embux app will guide you through the installation process, including selecting the target device, and initiating the installation.

6. **Monitor Installation Progress:** Observe the progress bar in the Embux app as the installation unfolds. Once the installation is complete, a notification will appear.

7. **Boot Target Device:** Once the installation is complete, power cycle the target device, and insert the Embux device. The device should boot into the newly installed Embux system.

:::

:::{tab-item} Other or ISO
:sync: other

```{warning}
The Embux app is not supported on platforms other than Linux, Mac and Windows. Thus an alternative way using an ISO flasher will be used in these instructions.
```

1. **Download Embux ISO:** Download the appropriate Embux image (.iso) from the Embux GitHub repository. You can find a link to the repository in the sidebar.

3. **Run ISO Flasher:** Look for a flashing tool available on your system. Most systems do not come with one, but offer one in their repositories. You can try [BalenaEtcher](https://etcher.balena.io).

4. **Import ISO:** Import the ISO into your flasher. Here's the format to help you find it: `embux-MAJOR.MINOR-ARCH-TYPE.iso`. Start flashing the storage device.

5. **Monitor Installation Progress:** Observe the progress bar or another way of tracking the progress as the flashing unfolds.

6. **Boot Target Device:** Once the installation is complete, power cycle the target device, and insert the Embux device. The device should boot into the newly installed Embux system.

:::

::::

## What's next?

### malpeza Package Manager {bdg-primary}`Optional`
Embux offers a lightweight package manager called `malpeza`. To install `malpeza`, execute the `embuxcfg ensure-malpeza` command.

You will need to connect to the ethernet or [setup WiFi](/wlan.html) to run this command.

### Keyboard Layout {bdg-danger}`Important`
Embux defaults to the `en-US` keyboard layout. This means, for example, if your keyboard uses the `en-GB` keyboard layout, attempts to type `"` will result in typing `@`.

To change the keyboard layout, run the `embuxcfg select kbd.layout` command and choose your preferred layout.

### Framebuffer Tool {bdg-primary}`For Developers`
Embux provides a framebuffer tool for C and some Python versions, enabling you to display text and graphics on countdowns, billboards, and other devices.

Refer to the fbtool documentation in the sidebar for detailed usage instructions.
