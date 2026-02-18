# MEMOS: New extension for deep-learning based segmentation of 3D fetal mice scans.

**Topic ID**: 27956
**Date**: 2023-02-21
**URL**: https://discourse.slicer.org/t/memos-new-extension-for-deep-learning-based-segmentation-of-3d-fetal-mice-scans/27956

---

## Post #1 by @muratmaga (2023-02-21 18:15 UTC)

<p>We would like to announce a new Slicer extension, <a href="https://github.com/SlicerMorph/SlicerMEMOS">MEMOS</a>, for deep-learning based segmentation of diceCT scans of fetal mice. See the repository for quick installation instructions.</p>
<p>Accompanying paper can be found in Biology Open: <a href="https://journals.biologists.com/bio/article/12/2/bio059698/287076/Deep-learning-enabled-multi-organ-segmentation-of" class="inline-onebox">Deep learning enabled multi-organ segmentation of mouse embryos | Biology Open | The Company of Biologists</a></p>
<p>Using GPU, MEMOs provide segmentation of 50 anatomical structures in the <a href="http://www.mouseimaging.ca/technologies/mouse_atlas/mouse_embryo_atlas.html">E15.5 atlas provided by the International Mouse Phenotyping Consortium</a> in about 40-60 seconds.</p>
<p>In future, we plan to incorporate more developmental time points as a separate trained networks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ebd5113bbda1cd7c1646f1fb157bac72fe914d.jpeg" data-download-href="/uploads/short-url/x5FyY930bv6XVPSYDSVk6pZfzFr.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7ebd5113bbda1cd7c1646f1fb157bac72fe914d_2_686x499.jpeg" alt="image" data-base62-sha1="x5FyY930bv6XVPSYDSVk6pZfzFr" width="686" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7ebd5113bbda1cd7c1646f1fb157bac72fe914d_2_686x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7ebd5113bbda1cd7c1646f1fb157bac72fe914d_2_1029x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ebd5113bbda1cd7c1646f1fb157bac72fe914d.jpeg 2x" data-dominant-color="B6B4AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×932 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Mate_Toth (2023-02-23 13:36 UTC)

<p>Hi, that sounds great, I’d like to try it, but I’m unable to install this extension<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddbb4b376355e4a2b99d18276d4dd81055c5f91c.png" alt="image" data-base62-sha1="vDwNmgsNWcIWKZZX01HmANkyyv2" width="369" height="72"></p>

---

## Post #3 by @muratmaga (2023-02-23 16:08 UTC)

<p>Which os do you use?</p>
<p>That might be related with the patch release last night. I just downloaded and install fresh on windows (v5.2.2), can you try again?</p>

---

## Post #4 by @Mate_Toth (2023-02-23 16:44 UTC)

<p>I’m using WIN10 and slicer 5.2.1 r31317 / 77da381, still not working, I’ll update to 5.2.2 and try again. Thank you</p>

---

## Post #5 by @muratmaga (2023-02-23 16:56 UTC)

<p>İ see. As it is a new extension, it is only available for stable or 5.3.0 (or higher) previews.<br>
Yes, try with latest stable.</p>

---

## Post #6 by @Jan_Lennart (2023-02-24 14:39 UTC)

<p>I have only used Total Segmentator so far but MEMOS also looks fantastic.</p>
<p>Is there anything comparable available for adult mice? I have &gt;1000 CT scans of mice that need to be segmented (mainly liver, kidneys, and heart).</p>
<p>Best, Jan</p>

---

## Post #7 by @muratmaga (2023-02-24 15:17 UTC)

<p>No, we don’t have anything for adult mice. We don’t really do physiology, mostly development.</p>
<p>However, it is getting easier to train deep learning networks for custom segmentation tasks. So if you have already manually segmented ones that can be used as training data, it might be just a matter of putting some GPUs to use.</p>

---

## Post #8 by @lassoan (2024-02-11 12:09 UTC)

<p>12 posts were split to a new topic: <a href="/t/ai-segmentation-of-bird-brain/34246">AI segmentation of bird brain</a></p>

---

## Post #20 by @lassoan (2024-02-21 20:33 UTC)

<p>15 posts were split to a new topic: <a href="/t/problem-using-memos-extension/34456">Problem using MEMOS extension</a></p>

---
