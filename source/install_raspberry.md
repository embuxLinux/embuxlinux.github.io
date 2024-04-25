# Embux on a Raspberry Pi

This guide explains installing Embux on Raspberry Pis. Raspberry Pis are small and cheap computers around the size of a credit card.
Raspberry Pis are based on ARM processors, so this means we will use an ARM image.

## Requirements

* **Raspberry Pi:** A Raspberry Pi. This document covers Raspberry Pis 3 to 5. Other Raspberry Pis are supported officially but are less common and thus not documented here. This device will later be referred to as a "Pi".
* **Computer:** Besides a Pi, a larger computer.
* **SD Card:** An SD card. This is where the Embux system will be stored. Pis do not have a hard disk so they rely on portable storage solutions like SD cards. A USB is also supported. **Don't flash the old Pi OS SD card, as we will be keeping it as a backup.**

## Disclaimer

Tinkering with your Pi can cause damage, which could potentially brick it. Be careful with your actions.

## Instructions

1. Download the Embux image from the repository linked in the sidebar: **Embux Repository**. You may need to scroll down.
2. Open a flashing tool. Embux recommends [balenaEtcher](https://etcher.balena.io) for flashing images. You can also try [Rufus](https://rufus.ie) on Windows.
3. Insert the USB or the SD card. The device must have at least 2 GB for it to store the `tiny` image, or around 3.5 GB for the `template` image. Choose an image with `piboot` in the name, the others contain the installer but we are looking for an image that can be used as a portable OS.
4. Click the flash button to flash the Embux installer onto your storage device.
5. Remove the storage device. Shut the Pi down, then insert the storage device into it.
6. Power on the Pi again. Login with username `piboot`, password `embux`.

Congrats! You have a working Embux setup on your Pi!
