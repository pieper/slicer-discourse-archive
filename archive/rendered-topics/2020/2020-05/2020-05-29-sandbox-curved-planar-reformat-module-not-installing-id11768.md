---
topic_id: 11768
title: "Sandbox Curved Planar Reformat Module Not Installing"
date: 2020-05-29
url: https://discourse.slicer.org/t/11768
---

# Sandbox - Curved Planar Reformat module not installing?

**Topic ID**: 11768
**Date**: 2020-05-29
**URL**: https://discourse.slicer.org/t/sandbox-curved-planar-reformat-module-not-installing/11768

---

## Post #1 by @NiinaIn3D (2020-05-29 04:05 UTC)

<p>Hi all, I’ve recently started to use 3D Slicer and was looking for a curved planar reformat tool to use with anatomical features. I noticed the module should be included in the Sandbox extension, but when I install it the only modules to load are Lights, Line Profile, and User Statistics. I tried with versions 28257 and 29081.</p>
<p>Since I’m new to this it’s completely possible the problem is user based. If there’s a way around this can I get some guidance please?</p>
<p>Thanks!</p>
<p>Niina</p>

---

## Post #2 by @lassoan (2020-05-29 04:13 UTC)

<p>Curved Planar Reformat module appears for me correctly after installing latest Slicer version (revision 29081) and Sandbox extension and restarting the application. Try uninstalling and reinstalling the extension (wait for the “Restart” button to appear). If the you still don’t see the module then copy-paste the application log here (menu: Help / Report a bug).</p>

---

## Post #3 by @NiinaIn3D (2020-06-12 00:06 UTC)

<p>Hi Andras, thanks for the advise! I installed rev 29117 and then the Sandbox extension. All good with the Curved Planar Reformat, but now I’ve got a problem with the program interface. Compared to the 4.10.2 all the icons are in the menu at the top are larger, and when I access the All Modules menu the list extends too far to the left. I actually can’t see the modules past the third column. Is there something in the program setup I could change to fix this?</p>
<p>Thanks again,</p>
<p>Niina</p>

---

## Post #4 by @lassoan (2020-06-12 00:12 UTC)

<p>You may need to set application scaling settings. What operating system do you use? (the exact software version is displayed in menu: Help / Report a bug -&gt; Operating system)</p>
<p>On Windows, scaling settings are available if you right-click on the Slicer application executable (at a location like this: <code>c:\Users\(yourusername)\AppData\Local\NA-MIC\Slicer 4.11.0-2020-06-06\bin\SlicerApp-real.exe</code>), go to “Compatibility” tab, click “Change high DPI settings” and try all setting combinations.</p>

---

## Post #5 by @NiinaIn3D (2020-06-12 00:26 UTC)

<p>Nothing like local knowledge. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"> Changing the scaling settings worked, thanks!</p>

---

## Post #6 by @lassoan (2020-06-12 00:38 UTC)

<p>Scaling should be OK with default settings? What exact operating system version do you use? Do you have a special display configuration (multiple displays, very high-resolution screen, system font size or application scaling settings changed form the defaults, etc.)?</p>

---

## Post #7 by @NiinaIn3D (2020-06-12 07:24 UTC)

<p>I thought it would be too, or at least it is with version 4.10.2.</p>
<p>I’m running Windows /  Personal /  (Build 9200) - 64-bit, nothing exotic, just a small laptop with a 14" screen and default settings.</p>

---

## Post #8 by @lassoan (2020-06-12 16:11 UTC)

<p>Windows Build 9200 is Windows 8! Do you actually have Windows 8 on that computer? That would explain it, as it is very old Windows version, which may not have screen scaling APIs that current Qt toolkit relies on.</p>

---

## Post #9 by @NiinaIn3D (2020-06-14 23:40 UTC)

<p>Interesting considering I installed Win 10 version 2004 a few days ago. <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=9" title=":thinking:" class="emoji" alt=":thinking:"></p>

---

## Post #10 by @muratmaga (2020-06-15 03:37 UTC)

<p>Then somehow your build number is not displayed correctly, since build 9200 is indeed Windows 8<br>
<a href="https://www.gaijin.at/en/infos/windows-version-numbers" class="onebox" target="_blank" rel="nofollow noopener">https://www.gaijin.at/en/infos/windows-version-numbers</a></p>

---

## Post #11 by @NiinaIn3D (2020-06-15 03:47 UTC)

<p>Plot thickens, the old windows version is reported by 4.10.2 (sorry I must have looked at the wrong window previously). 4.11 has it right, just wondering why the stable version thinks I’m living in the past.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/215137b5a26a995894903edc56c218cfff84c803.jpeg" data-download-href="/uploads/short-url/4KJLoAWtqmV9qQYty5CKLSXdAtB.jpeg?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/215137b5a26a995894903edc56c218cfff84c803_2_690x430.jpeg" alt="slicer" data-base62-sha1="4KJLoAWtqmV9qQYty5CKLSXdAtB" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/215137b5a26a995894903edc56c218cfff84c803_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/215137b5a26a995894903edc56c218cfff84c803.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/215137b5a26a995894903edc56c218cfff84c803.jpeg 2x" data-dominant-color="F2F3F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">894×558 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @muratmaga (2020-06-15 04:06 UTC)

<p>As long as the preview is showing the correct version, it is fine.</p>

---
