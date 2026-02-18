# Missing menu items from Slicer Application Main Window

**Topic ID**: 2613
**Date**: 2018-04-17
**URL**: https://discourse.slicer.org/t/missing-menu-items-from-slicer-application-main-window/2613

---

## Post #1 by @Andinet_Enquobahrie (2018-04-17 18:55 UTC)

<p>Hi,</p>
<p>I downloaded the nightly Windows installer and installed it on my Windows 10 Pro laptop.</p>
<p>Slicer’s Main Application menu seems to be missing (File, Edit, View and Help). see below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24f51356b7a3429d58e994c4cc7acdcf6eb5332a.png" data-download-href="/uploads/short-url/5gWgaL0acVyPY6B0URtIMqAEKE2.PNG?dl=1" title="0-2018-04-16-screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24f51356b7a3429d58e994c4cc7acdcf6eb5332a_2_690x351.PNG" alt="0-2018-04-16-screenshot" data-base62-sha1="5gWgaL0acVyPY6B0URtIMqAEKE2" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24f51356b7a3429d58e994c4cc7acdcf6eb5332a_2_690x351.PNG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24f51356b7a3429d58e994c4cc7acdcf6eb5332a_2_1035x526.PNG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24f51356b7a3429d58e994c4cc7acdcf6eb5332a_2_1380x702.PNG 2x" data-dominant-color="515251"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0-2018-04-16-screenshot</span><span class="informations">3840×1957 403 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My laptop system information can be found below (**)</p>
<p>Is this an  known issue?</p>
<p>I am happy to provide more information to help resolve the issue</p>
<p>Thank you!<br>
Andinet</p>
<p>PS:</p>
<p>(**)</p>
<p>OS Name	Microsoft Windows 10 Pro<br>
Version	10.0.16299 Build 16299<br>
Other OS Description 	Not Available<br>
OS Manufacturer	Microsoft Corporation<br>
System Name	GONDAR<br>
System Manufacturer	Dell Inc.<br>
System Model	XPS 15 9550<br>
System Type	x64-based PC<br>
System SKU	06E4<br>
Processor	Intel(R) Core™ i7-6700HQ CPU @ 2.60GHz, 2601 Mhz, 4 Core(s), 8 Logical Processor(s)<br>
BIOS Version/Date	Dell Inc. 1.2.29, 7/24/2017<br>
SMBIOS Version	2.8<br>
Embedded Controller Version	255.255<br>
BIOS Mode	UEFI<br>
BaseBoard Manufacturer	Dell Inc.<br>
BaseBoard Model	Not Available<br>
BaseBoard Name	Base Board<br>
Platform Role	Mobile<br>
Secure Boot State	Off<br>
PCR7 Configuration	Elevation Required to View<br>
Windows Directory	C:\WINDOWS<br>
System Directory	C:\WINDOWS\system32<br>
Boot Device	\Device\HarddiskVolume1<br>
Locale	United States<br>
Hardware Abstraction Layer	Version = “10.0.16299.371”<br>
User Name	GONDAR\andinet<br>
Time Zone	Eastern Daylight Time<br>
Installed Physical Memory (RAM)	32.0 GB<br>
Total Physical Memory	31.8 GB<br>
Available Physical Memory	21.0 GB<br>
Total Virtual Memory	36.6 GB<br>
Available Virtual Memory	25.9 GB<br>
Page File Space	4.75 GB<br>
Page File	C:\pagefile.sys<br>
Virtualization-based security	Running<br>
Virtualization-based security Required Security Properties	<br>
Virtualization-based security Available Security Properties	Base Virtualization Support, DMA Protection, UEFI Code Readonly, SMM Security Mitigations 1.0<br>
Virtualization-based security Services Configured	<br>
Virtualization-based security Services Running	<br>
Device Encryption Support	Elevation Required to View<br>
A hypervisor has been detected. Features required for Hyper-V will not be displayed.</p>

---

## Post #2 by @lassoan (2018-04-17 18:59 UTC)

<p>This is a known issue with all Qt5 applications on some laptops that have both Intel and NVidia graphics card. One solution is to set your NVidia application settings to use NVidia for 3D Slicer (SlicerApp-real.exe).</p>
<p><a href="https://communities.intel.com/thread/116003">Intel has acknowledged that this is an issue in their graphics card driver</a> that was introduced in x.x.x.4627 and they fixed the problem in driver version: x.x.x.4729.</p>

---

## Post #3 by @amymanson (2020-01-02 17:14 UTC)

<p>Hi, I am having the same issue. Not sure how to fix it as my computer is not finding any updates for drivers when I try to search for an update?<br>
Thanks,<br>
Amy</p>

---

## Post #4 by @lassoan (2020-01-02 18:00 UTC)

<p>You can find and install updated driver manually or to set your NVidia application settings to use NVidia (high-performance graphics) for 3D Slicer. You need to choose <code>SlicerApp-real.exe</code> (not <code>Slicer.exe</code>) file when you set application-specific settings.</p>

---
