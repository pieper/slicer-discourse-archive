---
topic_id: 14267
title: "Only Black Image Shown In Red Green Yellow View"
date: 2020-10-27
url: https://discourse.slicer.org/t/14267
---

# Only black image shown in red/green/yellow view

**Topic ID**: 14267
**Date**: 2020-10-27
**URL**: https://discourse.slicer.org/t/only-black-image-shown-in-red-green-yellow-view/14267

---

## Post #1 by @torquil (2020-10-27 10:45 UTC)

<p>Hi!</p>
<p>When importing DICOM files to the newest 3d Slicer from today on Linux, the red, green and yellow views remain black no matter what I do. I did not have this problem in the earlier 3D Slicer I was using, which was from september 16. When I select to show the red/green/yellow slices inside the 3D view, they show up there fine, so it is not a case of wrong viewing area relative to the physical volume. Is this a known problem with a solution, or do I have to “bisect” among the recent Slicer versions to pinpoint the problematic change?</p>
<p>As I mentioned, when embedding each slice view inside the 3d view, they show up there fine, with correct image pixels. It is only within the red/green/yellow views that the image is always completely black. I have not seen this problem before among the different 3D Slicer versions I have used.</p>
<p>I’m using 3D Slicer 4.13.0-2020-10-25 r29444 / 228f187.</p>

---

## Post #2 by @torquil (2020-10-27 12:01 UTC)

<p>I tried some different versions of 3D Slicer:</p>
<p>r29407: only black slices in the red/green/yellow views<br>
r29402: everything works fine</p>
<p>So the problem appeared somewhere between those two versions.</p>

---

## Post #3 by @ngillingham (2020-10-27 20:07 UTC)

<p>I’m just commenting to say that I’m having the exact same issue (works fine in the stable version but black screen in the nightly release) and I hope a forthcoming update can resolve this issue!</p>

---

## Post #4 by @lassoan (2020-10-27 20:08 UTC)

<p>I just see that the report is for Slicer-4.13. We are still working on making this latest preview release work with latest VTK9 version. We think we are close but it may take a few more days. You can monitor the status here: <a href="https://github.com/Slicer/Slicer/issues/5220">https://github.com/Slicer/Slicer/issues/5220</a></p>
<p>Until it gets fixed, you can use the latest stable release.</p>

---

## Post #5 by @ngillingham (2020-10-27 20:09 UTC)

<p>2015 MacBook Pro for me (not to hijack the original post)</p>

---
