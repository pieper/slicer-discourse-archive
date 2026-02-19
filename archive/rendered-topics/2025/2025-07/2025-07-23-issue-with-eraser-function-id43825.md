---
topic_id: 43825
title: "Issue With Eraser Function"
date: 2025-07-23
url: https://discourse.slicer.org/t/43825
---

# Issue with eraser function

**Topic ID**: 43825
**Date**: 2025-07-23
**URL**: https://discourse.slicer.org/t/issue-with-eraser-function/43825

---

## Post #1 by @noi9 (2025-07-23 14:43 UTC)

<p>Hi,</p>
<p>Two issues which  may be related.</p>
<ol>
<li>
<p>When I used the eraser function, there is still faint markings left. It does not fully erase.</p>
</li>
<li>
<p>There appears to be artefact when I used the threshold button to fill out multiple different slice sections.</p>
</li>
</ol>
<p>Any ideas on how to solve this?</p>
<p>Best,<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/793c7e860860f584603419783883072007902c86.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7360196f4beaf42a2973e09eda4bc6865d2cc8.png" data-video-base62-sha1="hivnHfKBRWCcM9c1DCB2Mq7ZYSW.mp4">
  </div><p></p>

---

## Post #2 by @SegmenterSam (2025-07-23 15:16 UTC)

<p>Hi,<br>
Is it reproducable when you exit the program and do the same steps? Or does that fix the issue?</p>

---

## Post #3 by @noi9 (2025-07-23 15:19 UTC)

<p>Hi,</p>
<p>When exiting and restarting the system I still have the same problem.</p>
<p>I have not discovered a fix yet.</p>
<p>Kind regards,</p>
<p>Nachika</p>

---

## Post #4 by @mau_igna_06 (2025-07-23 15:29 UTC)

<p>Please be sure the 2D views are not in a <code>reformat</code> state, see picture below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/009c26b91d4f212415ed7439122865d0682371dd.jpeg" data-download-href="/uploads/short-url/5oyfWPVNZV56yOzB5xexpXzNCJ.jpeg?dl=1" title="Screenshot from 2025-07-23 12-12-00_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/009c26b91d4f212415ed7439122865d0682371dd_2_690x389.jpeg" alt="Screenshot from 2025-07-23 12-12-00_2" data-base62-sha1="5oyfWPVNZV56yOzB5xexpXzNCJ" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/009c26b91d4f212415ed7439122865d0682371dd_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/009c26b91d4f212415ed7439122865d0682371dd_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/009c26b91d4f212415ed7439122865d0682371dd_2_1380x778.jpeg 2x" data-dominant-color="A6A4AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-07-23 12-12-00_2</span><span class="informations">1920×1085 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you see, the lower arrow should point to “Axial” on the selector</p>
<p>HIH</p>

---

## Post #5 by @noi9 (2025-07-24 07:08 UTC)

<p>Hi,</p>
<p>I changed settings as you described and still no luck.</p>
<p>Kind regards,</p>
<p>Nachika</p>

---

## Post #6 by @cpinter (2025-08-26 14:33 UTC)

<p>Do you still have this issue? It seems to me that you have more than one volumes loaded and maybe more than one segmentation node in the scene. It is important to select the appropriate source volume when you paint, because it only considers the extent of that volume and you cannot paint outside of it.</p>

---
