# Diffusion extensions make Slicer crash on latest nightly Mac version

**Topic ID**: 287
**Date**: 2017-05-09
**URL**: https://discourse.slicer.org/t/diffusion-extensions-make-slicer-crash-on-latest-nightly-mac-version/287

---

## Post #1 by @mrjeffs (2017-05-09 21:01 UTC)

<p>getting multiple errors on restart after loading diffusion exts.</p>
<p>Process:               polydatamerge [14274]<br>
Path:                  /Applications/Slicer_dev_05-06-2017.app/Contents/Extensions-26007/DTIProcess/lib/Slicer-4.7/cli-modules/polydatamerge<br>
Identifier:            polydatamerge<br>
Version:               ???<br>
Code Type:             X86-64 (Native)<br>
Parent Process:        Slicer [14259]<br>
Responsible:           polydatamerge [14274]<br>
User ID:               502</p>
<p>Date/Time:             2017-05-09 13:45:46.650 -0700<br>
OS Version:            Mac OS X 10.10.5 (14F1713)<br>
Report Version:        11<br>
Anonymous UUID:        0B7AEE2A-8B7F-0A03-30CA-5B45449C2A25</p>
<p>Sleep/Wake UUID:       66955CCE-E269-458E-92CD-B25BEBF90412</p>
<p>Time Awake Since Boot: 10000000 seconds<br>
Time Since Wake:       10000000 seconds</p>
<p>Crashed Thread:        0</p>
<p>Exception Type:        EXC_BREAKPOINT (SIGTRAP)<br>
Exception Codes:       0x0000000000000002, 0x0000000000000000</p>
<p>Application Specific Information:<br>
dyld: launch, loading dependent libraries</p>
<p>Dyld Error Message:<br>
Library not loaded: <span class="mention">@rpath</span>/lib/Slicer-4.7/libjsoncpp.0.dylib<br>
Referenced from: /Applications/Slicer_dev_05-06-2017.app/Contents/Extensions-26007/DTIProcess/lib/Slicer-4.7/cli-modules/polydatamerge<br>
Reason: image not found</p>
<p>Binary Images:<br>
0x7fff62672000 -     0x7fff626a8887  dyld (353.2.3)  /usr/lib/dyld</p>
<p>Model: MacPro5,1, BootROM MP51.007F.B03, 12 processors, 6-Core Intel Xeon, 2.93 GHz, 96 GB, SMC 1.39f11<br>
Graphics: ATI Radeon HD 5770, ATI Radeon HD 5770, PCIe, 1024 MB<br>
Graphics: ATI Radeon HD 5770, ATI Radeon HD 5770, PCIe, 1024 MB<br>
Memory Module: DIMM 1, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 2, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 3, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 5, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 6, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 7, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
AirPort: spairport_wireless_card_type_airport_extreme (0x14E4, 0x8E), Broadcom BCM43xx 1.0 (5.106.98.100.24)<br>
Bluetooth: Version 4.3.6f3 16238, 3 services, 27 devices, 1 incoming serial ports<br>
Network Service: Ethernet 1, Ethernet, en0<br>
PCI Card: ATI Radeon HD 5770, Display Controller, Slot-2<br>
PCI Card: ATI Radeon HD 5770, Display Controller, Slot-1<br>
Serial ATA Device: HL-DT-ST DVD-RW GH61N<br>
Serial ATA Device: Samsung SSD 840 EVO 1TB, 1 TB<br>
Serial ATA Device: Hitachi HDS723020BLA642, 2 TB<br>
Serial ATA Device: WDC WD4001FAEX-00MJRA0, 4 TB<br>
Serial ATA Device: WDC WD4001FAEX-00MJRA0, 4 TB<br>
USB Device: USB2.0 Hub<br>
USB Device: USB Multimedia Keyboard<br>
USB Device: USB2.0 Hub<br>
USB Device: iPhone<br>
USB Device: Microsoft Basic Optical Mouse v2.0<br>
USB Device: BRCM2046 Hub<br>
USB Device: Bluetooth USB Host Controller<br>
USB Device: Back-UPS RS 1500G FW:865.L5 .D USB FW:L5<br>
FireWire Device: built-in_hub, Up to 800 Mb/sec<br>
Thunderbolt Bus:</p>

---

## Post #2 by @mrjeffs (2017-05-09 21:05 UTC)

<p>polydatatransform also fails:</p>
<p>Process:               polydatatransform [14373]<br>
Path:                  /Applications/Slicer_dev_05-06-2017.app/Contents/Extensions-26007/DTIProcess/lib/Slicer-4.7/cli-modules/polydatatransform<br>
Identifier:            polydatatransform<br>
Version:               ???<br>
Code Type:             X86-64 (Native)<br>
Parent Process:        Slicer [14354]<br>
Responsible:           Slicer [14354]<br>
User ID:               502</p>
<p>Date/Time:             2017-05-09 14:03:58.742 -0700<br>
OS Version:            Mac OS X 10.10.5 (14F1713)<br>
Report Version:        11<br>
Anonymous UUID:        0B7AEE2A-8B7F-0A03-30CA-5B45449C2A25</p>
<p>Sleep/Wake UUID:       66955CCE-E269-458E-92CD-B25BEBF90412</p>
<p>Time Awake Since Boot: 10000000 seconds<br>
Time Since Wake:       10000000 seconds</p>
<p>Crashed Thread:        0</p>
<p>Exception Type:        EXC_BREAKPOINT (SIGTRAP)<br>
Exception Codes:       0x0000000000000002, 0x0000000000000000</p>
<p>Application Specific Information:<br>
dyld: launch, loading dependent libraries</p>
<p>Dyld Error Message:<br>
Library not loaded: <span class="mention">@rpath</span>/lib/Slicer-4.7/libjsoncpp.0.dylib<br>
Referenced from: /Applications/Slicer_dev_05-06-2017.app/Contents/Extensions-26007/DTIProcess/lib/Slicer-4.7/cli-modules/polydatatransform<br>
Reason: image not found</p>
<p>Binary Images:<br>
0x7fff6ad8c000 -     0x7fff6adc2887  dyld (353.2.3)  /usr/lib/dyld</p>
<p>Model: MacPro5,1, BootROM MP51.007F.B03, 12 processors, 6-Core Intel Xeon, 2.93 GHz, 96 GB, SMC 1.39f11<br>
Graphics: ATI Radeon HD 5770, ATI Radeon HD 5770, PCIe, 1024 MB<br>
Graphics: ATI Radeon HD 5770, ATI Radeon HD 5770, PCIe, 1024 MB<br>
Memory Module: DIMM 1, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 2, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 3, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 5, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 6, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
Memory Module: DIMM 7, 16 GB, DDR3 ECC, 1333 MHz, 0x857F, 0x463732324752363846393333334700000000<br>
AirPort: spairport_wireless_card_type_airport_extreme (0x14E4, 0x8E), Broadcom BCM43xx 1.0 (5.106.98.100.24)<br>
Bluetooth: Version 4.3.6f3 16238, 3 services, 27 devices, 1 incoming serial ports<br>
Network Service: Ethernet 1, Ethernet, en0<br>
PCI Card: ATI Radeon HD 5770, Display Controller, Slot-2<br>
PCI Card: ATI Radeon HD 5770, Display Controller, Slot-1<br>
Serial ATA Device: HL-DT-ST DVD-RW GH61N<br>
Serial ATA Device: Samsung SSD 840 EVO 1TB, 1 TB<br>
Serial ATA Device: Hitachi HDS723020BLA642, 2 TB<br>
Serial ATA Device: WDC WD4001FAEX-00MJRA0, 4 TB<br>
Serial ATA Device: WDC WD4001FAEX-00MJRA0, 4 TB<br>
USB Device: USB2.0 Hub<br>
USB Device: USB Multimedia Keyboard<br>
USB Device: USB2.0 Hub<br>
USB Device: iPhone<br>
USB Device: Microsoft Basic Optical Mouse v2.0<br>
USB Device: BRCM2046 Hub<br>
USB Device: Bluetooth USB Host Controller<br>
USB Device: Back-UPS RS 1500G FW:865.L5 .D USB FW:L5<br>
FireWire Device: built-in_hub, Up to 800 Mb/sec<br>
Thunderbolt Bus:</p>

---

## Post #3 by @lassoan (2017-05-09 23:06 UTC)

<p>Thank you for reporting this. For me it is not clear what you mean by “Latest mac dev crashes on download of diff exts”. Brevity may be justified in the title but in the description please use full words/sentences to tell: what do you do, what is the expected outcome, and what is the observed outcome.</p>

---

## Post #4 by @mrjeffs (2017-05-10 21:01 UTC)

<p>sorry, my bad. rushing. this is after deleting ~/.config/www.na-mic.org to have clean start (otherwise extension manager fails - see support item Ext manager and view controller broke) and downloading Slicer_dev_05-06-2017.  after installing the diffusion extensions and restarting the above errors occur and the 2 modules fail to load. outcome should be all installed diffusion modules load without error.</p>

---

## Post #5 by @lassoan (2017-05-11 03:29 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> I wanted to check these modules on Windows but DTIProcess was not available due to a build error. I’ve submitted a pull request to fix it: <a href="https://github.com/NIRALUser/DTIProcessToolkit/pull/36">https://github.com/NIRALUser/DTIProcessToolkit/pull/36</a>.</p>

---

## Post #6 by @ljod (2017-05-11 04:52 UTC)

<p>Thanks!! Hopefully the developers of that extension are on here as well to see this.</p>

---
