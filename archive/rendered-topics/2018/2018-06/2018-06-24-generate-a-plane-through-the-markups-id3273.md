---
topic_id: 3273
title: "Generate A Plane Through The Markups"
date: 2018-06-24
url: https://discourse.slicer.org/t/3273
---

# Generate a plane through the markups

**Topic ID**: 3273
**Date**: 2018-06-24
**URL**: https://discourse.slicer.org/t/generate-a-plane-through-the-markups/3273

---

## Post #1 by @George (2018-06-24 12:34 UTC)

<p>Hello! I’m very sorry if this problem has already been resolved, but I didn’t manage to find the answer. I need to draw (generate?) a large plane that passes through the three points (markups) as depicted in this photoshopped example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/739bd3dd58e268a3edef3ed33a700e0e5470fd51.png" data-download-href="/uploads/short-url/guILCUqVe6lgoIPDC7wE6VhGJuV.png?dl=1" title="Slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/739bd3dd58e268a3edef3ed33a700e0e5470fd51_2_690x412.png" alt="Slicer" data-base62-sha1="guILCUqVe6lgoIPDC7wE6VhGJuV" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/739bd3dd58e268a3edef3ed33a700e0e5470fd51_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/739bd3dd58e268a3edef3ed33a700e0e5470fd51_2_1035x618.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/739bd3dd58e268a3edef3ed33a700e0e5470fd51.png 2x" data-dominant-color="ACB2DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer</span><span class="informations">1234×737 70.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you very much for your help!</p>

---

## Post #2 by @lassoan (2018-06-24 15:45 UTC)

<p>You can create a plane polydata using VTK and set it as polydata of a model node. Probably 6-8 lines of Python code. Check out Slicer script repository for examples. <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_3_markup_fiducials">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_3_markup_fiducials</a></p>
<p>There are many other ways to do this. What would you like to achieve?</p>

---

## Post #3 by @timeanddoctor (2018-06-25 11:58 UTC)

<p>Did you resolve it and I am very interesting for that even I can do it easily in Mimics</p>

---

## Post #4 by @lassoan (2018-06-25 12:18 UTC)

<p>It’s very easy to define a plane using markups (the linked example shows how to create a sphere based on markups). The question is what to do with it once you have it. Just display the plane, or cut models with it, or use it as a reference for measurements, …?</p>

---

## Post #5 by @timeanddoctor (2018-06-25 12:34 UTC)

<p>what I went to do usually in Mimics just to cut a model, define a point or a midline for my model. I think it is important we can extend the plane created by three makeups</p>

---

## Post #6 by @George (2018-06-28 11:34 UTC)

<p>Thank you very much for the prompt answer! The code with shpere looks perfect in this situation, except I don’t have enough coding experience to modify it myself. If you could advise me on how to change figure from the spehere to the plane (rectangle?) and define two additional coordinate points from two additional markups (the first coordinate “SetCenter(centerPointCoord)” would work fine, I think?). And how to define the size of the rectangle/square?<br>
This plane would work as a reference for assessing the site of arterial disease in relation to bony markings, i.e. we will set three marks on the bony structures at predefined sites, then generate the plane trough these marks and look at the diseased arterial segment - if it is situated above or below the plane.<br>
Thank you very much for your assistance!</p>

---

## Post #7 by @chir.set (2018-06-28 13:26 UTC)

<aside class="quote no-group" data-username="George" data-post="6" data-topic="3273">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/71e660/48.png" class="avatar"> George:</div>
<blockquote>
<p>and look at the diseased arterial segment - if it is situated above or below the plane.</p>
</blockquote>
</aside>
<p>Would something like in the attachement be sufficient ? It’s much simpler to do for locating a diseased artery. Your use case context is yet not clear.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34ae0b91e51493cd1a6e5a121624532905f6cb5d.png" data-download-href="/uploads/short-url/7w1IyceWyM9tKqwE2LjxtWIXRBH.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34ae0b91e51493cd1a6e5a121624532905f6cb5d_2_690x428.png" alt="Screenshot" data-base62-sha1="7w1IyceWyM9tKqwE2LjxtWIXRBH" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34ae0b91e51493cd1a6e5a121624532905f6cb5d_2_690x428.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34ae0b91e51493cd1a6e5a121624532905f6cb5d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34ae0b91e51493cd1a6e5a121624532905f6cb5d.png 2x" data-dominant-color="9998C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1017×632 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Arnaud (2018-07-04 14:36 UTC)

<p>Hi,<br>
I’d be interested to know how to cut a model above a plane defined by markup.</p>
<p>thank you</p>

---

## Post #9 by @lassoan (2018-07-04 16:31 UTC)

<p>I’ve added a short example to the script repository that positions the <em>red</em> slice viewer to fit on first 3 points of <em>F</em> markup fiducial list: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_3_markup_fiducials" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p>You can clip a model using a slice view’s plane using <a href="http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/EasyClip">EasyClip extension</a>.</p>
<p>If you segment the structure using Segment Editor module, then you can use <em>Scissors effect</em> with <em>Slice cut</em> option set to positive or negative. It’ll cut only on one side of the slice where you are drawing at.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a45b250d98bd2092eb61b822a5693196c546ad9.jpeg" data-download-href="/uploads/short-url/hrFzGraWKm3IpFzceFczQTucu13.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a45b250d98bd2092eb61b822a5693196c546ad9_2_690x373.jpg" alt="image" data-base62-sha1="hrFzGraWKm3IpFzceFczQTucu13" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a45b250d98bd2092eb61b822a5693196c546ad9_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a45b250d98bd2092eb61b822a5693196c546ad9_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a45b250d98bd2092eb61b822a5693196c546ad9_2_1380x746.jpg 2x" data-dominant-color="747778"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 547 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @Arnaud (2018-07-10 09:50 UTC)

<p>Hi and thanks for the code.<br>
I tried it and it’s very usefull to segment just one side of the skull and make the model</p>
<p>Finally what I’d like to obtain is the mirror of this model but when I use the mirror in surface toolbox I can’t choose the mirror plane that I whant (the same than for the segmentation) and this is what I have <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41f5fb0e800204e1a0d2ea684a8eb79da24c84a9.png" data-download-href="/uploads/short-url/9pw2TOge6mJHBOoBXi1jkTB7u65.png?dl=1" title="21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41f5fb0e800204e1a0d2ea684a8eb79da24c84a9_2_690x330.png" alt="21" data-base62-sha1="9pw2TOge6mJHBOoBXi1jkTB7u65" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41f5fb0e800204e1a0d2ea684a8eb79da24c84a9_2_690x330.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41f5fb0e800204e1a0d2ea684a8eb79da24c84a9_2_1035x495.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41f5fb0e800204e1a0d2ea684a8eb79da24c84a9_2_1380x660.png 2x" data-dominant-color="8B8FB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">21</span><span class="informations">1938×928 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any solution to choose the plane?</p>
<p>Sorry to insist but I’m stuck…</p>
<p>thanks for helping me</p>

---

## Post #11 by @lassoan (2018-07-10 14:30 UTC)

<p>See my response in your other thread: <a href="https://discourse.slicer.org/t/mirror-in-surface-toolbox/3297/2?u=lassoan">Mirror in surface toolbox</a></p>

---

## Post #12 by @haylea.b (2018-07-20 10:14 UTC)

<p>Hi there, I would like to make a reference plane for measurements, are you able to help? many thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #13 by @lassoan (2018-07-23 04:22 UTC)

<p>Please write this question in a new post and give some more details about what exactly you would like to do.</p>

---
