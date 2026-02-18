# Advice for system configuration

**Topic ID**: 25261
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/advice-for-system-configuration/25261

---

## Post #1 by @Katya_Stansfield (2022-09-14 13:37 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5<br>
Expected behavior: to work<br>
Actual behavior: it stalls</p>
<p>Dear all,<br>
I am looking for advice on the system configuration. My machine has<br>
|Processor|Intel(R) Core™ i7-9750H CPU @ 2.60GHz   2.59 GHz|<br>
|Installed RAM|32.0 GB (31.9 GB usable)|<br>
|System type|64-bit operating system, x64-based processor|</p>
<p>I also have a NVIDIA dedicated graphics card, which I assigned to Slicer as a default GPU engine.</p>
<p>The problem is that the Slicer is too slow, rendering my work with it impossible and I am puzzled why.</p>
<p>I am now trying to place some landmarks on a surface. The surface file is small (there is no problem with its manipulation in the 3D view). I imported some landmarks from a .csv, saved them as a markup file and am now trying to manipulate the view. Each calculation, i.e. changing the visibility of landmarks, takes a surprisingly long time.</p>
<p>I noticed that the slicer uses up to 15% of the CPU while performing these operations.</p>
<p>Any suggestions? I am starting to lose any hope …</p>

---

## Post #2 by @muratmaga (2022-09-14 16:21 UTC)

<p>What specific version are you using? There was a performance problem in 5.0.2 that was fixed with 5.0.3. See <a href="https://discourse.slicer.org/t/point-list-performance-is-very-slow-with-large-point-list/23591/3" class="inline-onebox">Point list performance is very slow with large point list - #3 by jamesobutler</a></p>
<p>Can you try with the latest stable and report back?</p>

---

## Post #3 by @Katya_Stansfield (2022-09-15 07:34 UTC)

<p>Hi Murat – thank you for the advice – I have installed 5.0.3 and it seems to work as expected. I am very grateful.</p>

---
