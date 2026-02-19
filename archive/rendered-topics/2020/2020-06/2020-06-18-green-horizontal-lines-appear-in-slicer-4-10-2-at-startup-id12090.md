---
topic_id: 12090
title: "Green Horizontal Lines Appear In Slicer 4 10 2 At Startup"
date: 2020-06-18
url: https://discourse.slicer.org/t/12090
---

# Green horizontal lines appear in Slicer-4.10.2 at startup

**Topic ID**: 12090
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/green-horizontal-lines-appear-in-slicer-4-10-2-at-startup/12090

---

## Post #1 by @calvin.kohwy (2020-06-18 10:35 UTC)

<p>Operating system: Windows 10 i7<br>
Slicer version: 4.10.2</p>
<p>Hi all</p>
<p>I have been using slicer with my pc for quite sometime. However, out of the blue, the following happen to my slicer as shown in the image  below. I had tried reinstalling it but it does not work. Do you have any idea what is happening?</p>
<p>Thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb1d7ed425d74d804f617f378364c5d8902f3455.png" data-download-href="/uploads/short-url/sYQ7rSLzIHJsFqSv5Ey1IksZAJ7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb1d7ed425d74d804f617f378364c5d8902f3455_2_690x374.png" alt="image" data-base62-sha1="sYQ7rSLzIHJsFqSv5Ey1IksZAJ7" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb1d7ed425d74d804f617f378364c5d8902f3455_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb1d7ed425d74d804f617f378364c5d8902f3455_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb1d7ed425d74d804f617f378364c5d8902f3455_2_1380x748.png 2x" data-dominant-color="7AAE7D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×1041 71.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-06-18 13:55 UTC)

<p>This looks like a graphics card driver update broke OpenGL rendering on your computer.</p>
<p>What graphics card do you have in the computer and what is the driver version?<br>
Is the behavior the same with latest Slicer Preview Release?<br>
Are other VTK-based applications, such as ParaView, have similar rendering issues?</p>

---

## Post #3 by @calvin.kohwy (2020-06-18 14:30 UTC)

<p>Hi</p>
<p>I am using GTX 1660 Ti v446.14. I was working with this graphic card all these while and it was working perfectly fine with slicer. It just happen to be  crash one day when i was loading dicom files. The next moment when i restarted slicer, this happened.</p>
<p>Paraview is working perfectly fine as well.</p>
<p>Yes, it has the same behavior with the latest preview release.</p>

---

## Post #4 by @lassoan (2020-06-18 14:51 UTC)

<p>Slicer crash may corrupt the application settings file. The strange rendering artifacts is not a typical symptom, but you can give it a try and run Slicer with default settings - see here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Instruction_for_Windows">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Instruction_for_Windows</a> (and delete application settings if that solves the problem).</p>
<p>Another possibility that Windows determined that the crash was due to to application compatibility issue and decided to run Slicer in some compatibility mode. Right-click on SlicerApp-real.exe and play around with settings in “Compatibility” tab.</p>
<p>Is this a laptop with NVidia Optimus? Do you have multiple monitors connected? Any of the monitors are HiDPI?</p>

---

## Post #5 by @calvin.kohwy (2020-06-18 16:18 UTC)

<p>The link you had provided does not work for this case. However, one of the error i had found in event view is the following:</p>
<blockquote>
<p>Faulting application name: SlicerApp-real.exe, version: 0.0.0.0, time stamp: 0x5cddc587<br>
Faulting module name: Qt5Gui.dll, version: 5.10.1.0, time stamp: 0x5a7c816f<br>
Exception code: 0xc0000005<br>
Fault offset: 0x0000000000313186<br>
Faulting process id: 0x3544<br>
Faulting application start time: 0x01d6377bd7b23133<br>
Faulting application path: C:\Program Files\Slicer 4.10.2\bin\SlicerApp-real.exe<br>
Faulting module path: C:\Program Files\Slicer 4.10.2\bin\Qt5Gui.dll<br>
Report Id: 03c680aa-d127-4154-8143-70b34e134720<br>
Faulting package full name:<br>
Faulting package-relative application ID:</p>
</blockquote>
<blockquote>
<p>Faulting application name: SlicerApp-real.exe, version: 0.0.0.0, time stamp: 0x5cddc587<br>
Faulting module name: ig9icd64.dll, version: 26.20.100.8141, time stamp: 0x5e91eea6<br>
Exception code: 0xc0000005<br>
Fault offset: 0x000000000002a7e2<br>
Faulting process id: 0x265c<br>
Faulting application start time: 0x01d625d9f1aac289<br>
Faulting application path: C:\Program Files\Slicer 4.10.2\bin\SlicerApp-real.exe<br>
Faulting module path: C:\WINDOWS\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_0dd7d9c16d9ad9c5\ig9icd64.dll<br>
Report Id: c2874064-8295-43b0-890e-954552200449<br>
Faulting package full name:<br>
Faulting package-relative application ID:</p>
</blockquote>
<p>I tried playing around with the compatibility tab and the following happened:<br>
When i tried to “Run compatibility troubleshooter” → “Try recommended settings” → “Test the program”<br>
I got the following error:</p>
<blockquote>
<p>The code execution cannot proceed because CTKWidgets.dll was not found. Reinstalling the program may fix this problem"</p>
</blockquote>
<p>However, i have tried reinstalling Slicer a couple of times and it does not work.</p>
<p>Seems like the drop down window is fine but not the main window.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/465b125ab7c294f91221fd13a997a376bd8d90b7.png" data-download-href="/uploads/short-url/a2oxFPU4ortiVDTMyZHAqCRI2gv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/465b125ab7c294f91221fd13a997a376bd8d90b7.png" alt="image" data-base62-sha1="a2oxFPU4ortiVDTMyZHAqCRI2gv" width="690" height="494" data-dominant-color="A9CAAB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">835×599 47.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Yes it has Nvidia Optimus. I have multiple monitors but i did test it without multiple monitors as well… None of these monitors are HiDPI. I have been using this system for quite sometime and had no issue previously.</p>

---

## Post #6 by @lassoan (2020-06-18 16:25 UTC)

<p>Could you try running Slicer on the NVidia and on the Intel Integrated Graphics card?</p>
<p>Does deleting all Slicer*.ini files help?</p>
<p>Do you have the issue when the application window is not maximized?</p>
<p>Could you post a screenshot taken of latest Slicer Preview Release?</p>

---

## Post #7 by @calvin.kohwy (2020-06-18 17:01 UTC)

<p>Thank you Iassoan! It works after I delete ALL the .ini files and rename NA-MIC to NA-MIC-backup</p>
<p>It’s back to normal now.</p>
<p>Thank you for your patience!</p>

---

## Post #8 by @markyang19 (2020-10-17 12:06 UTC)

<p>I have the same problem. I solve the problem by stopping my Intel HD Graphics 630 driver and only using the NVIDIA driver.</p>
<p>Regards.</p>

---
