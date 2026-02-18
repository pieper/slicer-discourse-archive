# Oculomotor muscles segmentation in Total Segmentator

**Topic ID**: 42585
**Date**: 2025-04-16
**URL**: https://discourse.slicer.org/t/oculomotor-muscles-segmentation-in-total-segmentator/42585

---

## Post #1 by @philippepellerin (2025-04-16 13:39 UTC)

<p>Hi, Jakob; Congratulations on the Oculomotor muscles segmentation you implemented in Total segmentator. I spent much time doing the 20 manual segmentations, but it was worth it. I tried your new module, and the results are quite accurate. I do not doubt that it will be a great help to all those who are, as I am, interested in facial surgery.<br>
It has been a pleasure to work with you like it has been on the masticatory muscles.<br>
Best.</p>

---

## Post #2 by @chz31 (2025-04-16 17:06 UTC)

<p>It was really impressive! It predicted a reasonable boundary between the superior palpebrae &amp; superior rectus, which was very hard for me to differentiate visually.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443813681e39a47d69a10b398d1d6622c71bcf1f.png" data-download-href="/uploads/short-url/9JuBOhgLk5jCG4gAN9yFQW0Q1z1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443813681e39a47d69a10b398d1d6622c71bcf1f.png" alt="image" data-base62-sha1="9JuBOhgLk5jCG4gAN9yFQW0Q1z1" width="287" height="120"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">574×241 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f24cfb14f2c69b7afa88ef2ad7e5d2198405ea1.png" data-download-href="/uploads/short-url/kqj93Gi2FdO9jgBw54x0KSjzMcx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f24cfb14f2c69b7afa88ef2ad7e5d2198405ea1.png" alt="image" data-base62-sha1="kqj93Gi2FdO9jgBw54x0KSjzMcx" width="319" height="137"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">639×275 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @robertf (2025-04-21 00:47 UTC)

<p>I can see that the segmentation looks reasonable, but how confident can you be that it is actually correct? I’m not very familiar with the oculomotor muscles, but I have similar concerns about segmenting middle-ear structures in CT scans.</p>
<ul>
<li>Robert</li>
</ul>

---

## Post #4 by @philippepellerin (2025-04-21 13:28 UTC)

<p>The reliability of segmentation depends on the resolution of the CT scan. Oculomotor muscles are quite easily discerned since they are homogeneous in density and surrounded by the fat inside the Tenon’s capsule, which has a very low Houston value. Thus, the effectiveness of the module.<br>
I do not use the automatic segmentation for the middle-ear, but it looks the same to me.<br>
If you want to discern the muscles in the CT scan, you need to set the correct WL-WW. This is what you get with. 350-40.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/036575caafcbeb3884a07dd7fdf8fa339a2442f9.png" data-download-href="/uploads/short-url/u2OcA19FaQEZZAQZtd3VjNeO93.png?dl=1" title="PastedGraphic-1.png" rel="noopener nofollow ugc"><img width="398" alt="PastedGraphic-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036575caafcbeb3884a07dd7fdf8fa339a2442f9_2_398x305.png" data-base62-sha1="u2OcA19FaQEZZAQZtd3VjNeO93" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036575caafcbeb3884a07dd7fdf8fa339a2442f9_2_398x305.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036575caafcbeb3884a07dd7fdf8fa339a2442f9_2_597x457.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036575caafcbeb3884a07dd7fdf8fa339a2442f9_2_796x610.png 2x" data-dominant-color="767676"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1.png</span><span class="informations">796×610 79.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #5 by @robertf (2025-04-22 00:35 UTC)

<p>Thank you, Philippe.<br>
Robert</p>

---

## Post #6 by @chz31 (2025-06-19 14:40 UTC)

<p>Hi Philippe <a class="mention" href="/u/philippepellerin">@philippepellerin</a>,</p>
<p>Is there any citations associated with the TotalSegmentor oculomoter muscle segmentations? I did not see any publication listed in the <a href="https://github.com/wasserth/TotalSegmentator#:~:text=oculomotor_muscles%3A%20skull%2C%20eyeball_right,inferior_oblique_muscle_left%2C%20inferior_rectus_muscle_left%2C%20optic_nerve_right*" rel="noopener nofollow ugc">README</a></p>
<p>Thanks!</p>

---

## Post #7 by @philippepellerin (2025-06-20 07:03 UTC)

<p>Hi Robert, I did not published on this topic, but just did the 20 manual segmentations and give them to Jakob who trained his IA on it. So if you want to quote in a publication you can quote the module and if you like you could give the credit for the segmentation from 20 CT scans of normal patients.<br>
Best regards.</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---
