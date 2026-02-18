# High res/ 4K Scaling Issue

**Topic ID**: 910
**Date**: 2017-08-21
**URL**: https://discourse.slicer.org/t/high-res-4k-scaling-issue/910

---

## Post #1 by @stephenc (2017-08-21 13:50 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.70 nightly build 20-08<br>
Expected behavior: Normal display of menus<br>
Actual behavior: Errors with interface, for example install extensions screen (all font and icons are very small), DICOM import screen etc.</p>

---

## Post #2 by @lassoan (2017-08-21 14:02 UTC)

<p>Since the introduction of small screens with very high resolution and very large screens with moderate resolution, user interface scaling has been an issue on most applications on all operating systems.</p>
<p>For now, you can adjust font size in Slicer application settings (Appearance category), or in system settings and application-specific compatibility settings in Windows.</p>
<p>In a couple of months, we’ll update our GUI toolkit to Qt5, which will improve scaling of the application on hi-DPI screens.</p>

---

## Post #3 by @stephenc (2017-08-21 14:22 UTC)

<p>That’s great, thanks for your quick and knowledgable reply!</p>

---

## Post #4 by @mikebind (2019-05-18 06:29 UTC)

<p>Just adding my experience here because this was the top hit when I was looking for issues Slicer issues with a 4K screen, and I had a different solution.  I got a new windows 10 laptop with a 4K display, and when I opened Slicer (4.10.1) the splash screen filled the whole laptop screen and the main window was LARGER than the whole screen, with terrible pixelation and sizing which made Slicer unusable.  By default, my laptop was set to scale applications 250%, which is what led to the terrible-looking scaling.  I was able to correct it on an application-specific basis just for Slicer by following the instructions found here: <a href="https://superuser.com/questions/952120/windows-10-per-app-scaling" rel="nofollow noopener">https://superuser.com/questions/952120/windows-10-per-app-scaling</a>.  Basically, right-click on the Slicer application executable, click Properties, go to “Compatibility” tab, click the “Change High DPI settings” button near bottom, check the “Override high DPI scaling behavior. Scaling performed by” box and select “Application”.  Opening Slicer after making these changes worked fine.</p>

---
