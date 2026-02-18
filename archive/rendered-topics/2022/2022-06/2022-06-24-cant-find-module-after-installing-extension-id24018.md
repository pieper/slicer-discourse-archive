# Can't find module after installing extension

**Topic ID**: 24018
**Date**: 2022-06-24
**URL**: https://discourse.slicer.org/t/cant-find-module-after-installing-extension/24018

---

## Post #1 by @vyvyvyvy (2022-06-24 04:16 UTC)

<p>I installed the SlicerVMTK extension (manual installation) and the relevant modules were not found in the dropdown list. How can I resolve this issue? I currently have the latest version (5.0.2) installed.</p>

---

## Post #2 by @lassoan (2022-06-24 04:23 UTC)

<p>Why did you need to install the extension manually?<br>
Have you downloaded the extension package from the Extensions Catalog or you have compiled Slicer and then compiled SlicerVMTK yourself?<br>
Did you follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection">these instructions</a>?<br>
What operating system do you use?<br>
Were there any error or warning messages in the application log after you installed SlicerVMTK and restarted Slicer?</p>

---

## Post #3 by @vyvyvyvy (2022-06-27 18:20 UTC)

<p>Hi Andras! I ran into an error that stated the package could not be retrieved from <a href="http://kitware.com" rel="noopener nofollow ugc">kitware.com</a>, so I had to follow the same instructions linked to do a manual installation. In Slicer, it does state that extension exists and has been installed, but the modules from the extension themselves do not show up. I am using Windows. There were no errors or warning after I installed SlicerVMTK and restarted. Thank you!</p>

---

## Post #4 by @lassoan (2022-06-27 18:51 UTC)

<p>I’ve just tested VMTK extension installation on the latest Slicer Preview Release on Windows and it worked well:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/201c75ce01bdce763ef547e26813e2869649e939.png" alt="image" data-base62-sha1="4A4fN3vWaeCbcSsXlMDsh5AaXrP" width="677" height="499"></p>
<p>Please test the latest Slicer Preview Release and let us know if the issue still persists.</p>

---

## Post #6 by @vyvyvyvy (2022-06-28 19:31 UTC)

<p>Hi, I’ve resolved this issue. Thanks for your help</p>

---

## Post #7 by @lassoan (2022-06-29 01:51 UTC)

<p>It is great that you could resolve the issue. What was the problem? Just to know if we should improve something in Slicer or its documentation to avoid other users to run into the same problem.</p>

---

## Post #8 by @vyvyvyvy (2022-06-29 15:41 UTC)

<p>I had to change the directory names within my extension files to match my version of Slicer</p>

---
