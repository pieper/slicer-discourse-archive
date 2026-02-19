---
topic_id: 5355
title: "Seperating Skin Of The Hand From The Bed Of The Ct Scan Mach"
date: 2019-01-13
url: https://discourse.slicer.org/t/5355
---

# seperating skin of the hand from the bed of the ct scan machine. 

**Topic ID**: 5355
**Date**: 2019-01-13
**URL**: https://discourse.slicer.org/t/seperating-skin-of-the-hand-from-the-bed-of-the-ct-scan-machine/5355

---

## Post #1 by @denzil_dsouza (2019-01-13 14:14 UTC)

<p>Operating system:windows<br>
Slicer version:4.10<br>
Expected behavior: only want outside surface of the skin without any foreign objects.<br>
Actual behavior: skin and the bed is showing as the same surface</p>

---

## Post #2 by @lassoan (2019-01-13 14:33 UTC)

<p>If the skin and bed are not connected then you can use Islands effect / Split operation to separate them. If you just want to remove the table then you can use Scissors tool to delete it.</p>

---

## Post #3 by @denzil_dsouza (2019-01-13 15:15 UTC)

<p>thankyou for the valuable feedback but its connected and scissor operation doesnt give better results</p>

---

## Post #4 by @lassoan (2019-01-13 18:08 UTC)

<p>We use the described methods often and they work well. We can give more specific instructions if you tell what you do exactly, what do you expext to happen, and what happens instead. If possible, attach screenshots, they often better explain the issue than words.</p>

---

## Post #5 by @denzil_dsouza (2019-01-15 11:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/496af1cf3244c6e28f7f1c416dbac777b5a71088.jpeg" data-download-href="/uploads/short-url/attYWJOeF5uWjRHhz6wY41BwG6Y.jpeg?dl=1" title="IMG_20190115_172041" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/496af1cf3244c6e28f7f1c416dbac777b5a71088_2_666x500.jpeg" alt="IMG_20190115_172041" data-base62-sha1="attYWJOeF5uWjRHhz6wY41BwG6Y" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/496af1cf3244c6e28f7f1c416dbac777b5a71088_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/496af1cf3244c6e28f7f1c416dbac777b5a71088_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/496af1cf3244c6e28f7f1c416dbac777b5a71088_2_1332x1000.jpeg 2x" data-dominant-color="53565F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20190115_172041</span><span class="informations">4160×3120 3.47 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef8dd0c236b7804ac173def46e3e6b491992c672.jpeg" data-download-href="/uploads/short-url/ybbX7TqPV53IjNDIa8CRg2LYE6e.jpeg?dl=1" title="IMG_20190115_172120" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef8dd0c236b7804ac173def46e3e6b491992c672_2_666x500.jpeg" alt="IMG_20190115_172120" data-base62-sha1="ybbX7TqPV53IjNDIa8CRg2LYE6e" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef8dd0c236b7804ac173def46e3e6b491992c672_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef8dd0c236b7804ac173def46e3e6b491992c672_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef8dd0c236b7804ac173def46e3e6b491992c672_2_1332x1000.jpeg 2x" data-dominant-color="7C8395"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20190115_172120</span><span class="informations">2941×2206 2.92 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>i want to remove this bedsheet which is very close to the hand.</p>

---

## Post #6 by @lassoan (2019-01-15 12:56 UTC)

<p>See how to blank out regions of a volume using <em>Scissors</em> and <em>Volume masking</em> effects in this video:</p>
<div class="lazyYT" data-youtube-id="xZwyW6SaoM4" data-youtube-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #7 by @denzil_dsouza (2019-01-15 13:00 UTC)

<p>thanks for the video i will try this out. the only concern is the part outside the hand skin</p>

---

## Post #8 by @lassoan (2019-01-15 13:02 UTC)

<p>You can rotate the 3D view and remove the cloth piece by piece, zooming in very closely when they get very close.</p>
<p>It is also often possible to make the cloth disappear by choosing a different offset in <em>Volume rendering</em> module or a different threshold in <em>Segment editor</em> module.</p>

---
