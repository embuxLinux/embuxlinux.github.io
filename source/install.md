# Embux Installation Guide

```{warning}
Please note that there are two distributions named Embux. The Embux distribution discussed in this guide is a lightweight Linux distribution specifically designed for embedded systems. It is not to be confused with another Embux distribution, which is less popular and may not be suitable for all applications.
```

```{warning}
Embux installation is not a trivial task and requires technical expertise. It is recommended for experienced users only.
```

## Prerequisites

Before embarking on the Embux installation process, ensure that you have the necessary prerequisites in place:

* **Technical Expertise:** Possess a strong understanding of Linux systems, embedded systems, and networking concepts.

* **Target Computer:** A target computer with at least 10 MB of RAM. This could be a Raspberry Pi, an industrial control system, or any other embedded device with sufficient memory.

* **Source Computer:** A source computer with access to the internet and the ability to install software. This could be your personal laptop, a desktop workstation, or even a cloud-based virtual machine.

* **Storage**: A USB drive or SD card with at least 2 GB. Insert it into the source computer.

## Signing

Remember to validate the Embux image. Custom images could have malware, including software that could brick the entire device.

### Instructions

::::{tab-set}

:::{tab-item} Linux and macOS
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

Refer to your system's manual for instructions on how to verify file checksums.

If you can't find out how to do that, be vigilant of malicious images.

::::

## Installation Process

::::{tab-set}

:::{tab-item} Linux and macOS
:sync: linux

1. **Download Embux App:** Download the appropriate Embux app shell script (.sh) from the Embux GitHub repository. Please note there are different versions of the shell script for Linux and Mac, the macOS version is labelled `darwin`. You can find a link to the repository in the sidebar. For macOS, you will need to install [Homebrew](https://brew.sh).

2. **Ensure Execution Permissions:** Make sure the script has executable permissions. You can do this by running the following command in the terminal:

    ```bash
    chmod +x embux-app-*.sh
    ```

3. **Optional: Sideload a Custom Embux Image:** If you want to install Embux Beta, a testing version of Embux, or any modified version of Embux, store the ISO in `~/.embux.iso`.

4. **Run Embux App:** Run the Embux app by executing the following command:

    ```bash
    ./embux-app.sh
    ```

5. **Follow Embux App Instructions:** The Embux app will guide you through the installation process, including selecting the target device, and initiating the installation.

6. **Monitor Installation Progress:** Observe the progress bar in the Embux app as the installation unfolds. Once the installation is complete, a notification will appear.

7. **Boot Target Device:** Once the installation is complete, power cycle the target device, remove the Raspberry Pi OS SD card (if you use a Pi), and insert the Embux device.. The device should boot into the newly installed Embux system.
:::

:::{tab-item} Windows
:sync: win

```{warning}
The Embux app is not designed for Windows. Consider installing Linux on the source computer, then follow the procedure for Linux.
```

1. **Download Embux App:** Download the appropriate Embux app executable (.exe) from the Embux GitHub repository. You can find a link to the repository in the sidebar.

2. **Optional: Sideload a Custom Embux Image:** If you want to install Embux Beta, a testing version of Embux, or any modified version of Embux, store the ISO in `C:\Embux.iso`.

3. **Run Embux App:** Run the Embux app by finding it in your downloads folder.

4. **Follow Embux App Instructions:** The Embux app will guide you through the installation process, including selecting the target device, and initiating the installation.

5. **Monitor Installation Progress:** Observe the progress bar in the Embux app as the installation unfolds. Once the installation is complete, a notification will appear.

6. **Boot Target Device:** Once the installation is complete, power cycle the target device, remove the Raspberry Pi OS SD card (if you use a Pi), and insert the Embux device. The device should boot into the newly installed Embux system.

:::

:::{tab-item} Other or ISO
:sync: other

```{warning}
The Embux app is not supported on platforms other than Linux, Mac and Windows. Thus an alternative way using an ISO flasher will be used in these instructions.
```

1. **Download Embux ISO:** Download the appropriate Embux image (.iso) from the Embux GitHub repository. You can find a link to the repository in the sidebar.

3. **Run ISO Flasher:** Look for a flashing tool available on your system. Most systems do not come with one, but offer one in their repositories. You can try [BalenaEtcher](https://etcher.balena.io).

4. **Import ISO:** Import the ISO into your flasher. Here's the format to help you find it: `embux-MAJOR.MINOR-ARCH-TYPE.iso`.

5. **Monitor Installation Progress:** Observe the progress bar or another way of tracking the progress as the flashing unfolds.

6. **Boot Target Device:** Once the installation is complete, power cycle the target device, remove the Raspberry Pi OS SD card (if you use a Pi), and insert the Embux device. The device should boot into the newly installed Embux system.

:::

::::

## Additional Considerations

* **malpeza Package Manager:** Embux offers a lightweight package manager called `malpeza`. To install `malpeza`, execute the `embux_getmalpeza` command. You will need to connect to the ethernet (Embux does not support Wi-Fi) to run this command.

* **Keyboard Layout:** Embux defaults to the `en-US` keyboard layout. To change the keyboard layout, run the `embuxcfg select kbd.layout` command and choose your preferred layout.

* **Framebuffer Tool:** Embux provides a framebuffer tool for C and some Python versions, enabling you to display text and graphics on countdowns, billboards, and other devices. Refer to the fbtool documentation in the sidebar for detailed usage instructions.
