# Import segmentation nodes seperately

**Topic ID**: 7094
**Date**: 2019-06-09
**URL**: https://discourse.slicer.org/t/import-segmentation-nodes-seperately/7094

---

## Post #1 by @Jainey (2019-06-09 04:23 UTC)

<p>I want to import several segmented models into slicer to do segment registration. I tried doing that, but instead of separate models, it shows a heavily overlapped single model. Could you please advise.<br>
Thanks</p>

---

## Post #2 by @lassoan (2019-06-09 12:21 UTC)

<p>How do you import the models exactly? Can you attach a screenshot?</p>

---

## Post #3 by @Jainey (2019-06-16 15:48 UTC)

<p>Thanks Prof Lasso. <a class="mention" href="/u/lassoan">@lassoan</a><br>
Screenshot attached.<br>
I have segmented bones separately. if they are from the same frame/time point, they show up on proper positions according to their coordinates.<br>
How I add- from data I open file and select my segmentation.<br>
But when I add the same bone from two time points, in a dynamic study, say frame 1 and frame 5 they show me an overlapped view. (The bone positions only change few degrees 5-10 in rotation) so its like two 3 D models overlapped on one another with slight mismatch.<br>
What I want to do is, separately load segmented bone from various time points and do segment registration.</p>
<p>Could you kindly advise, please</p>
<p>Thanks<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33ed7f816dde0e0af0ee23cb19d251580dacdc1d.png" data-download-href="/uploads/short-url/7pnbFFedaPz6bLHe5Q0jv85a43j.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33ed7f816dde0e0af0ee23cb19d251580dacdc1d_2_690x388.png" alt="image" data-base62-sha1="7pnbFFedaPz6bLHe5Q0jv85a43j" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33ed7f816dde0e0af0ee23cb19d251580dacdc1d_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33ed7f816dde0e0af0ee23cb19d251580dacdc1d_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33ed7f816dde0e0af0ee23cb19d251580dacdc1d_2_1380x776.png 2x" data-dominant-color="67656C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Tom</p>

---

## Post #4 by @lassoan (2019-06-18 03:22 UTC)

<p>It is fine if they appear overlapped. You can go to Data module and show/hide them to see only what you are interested in. If you want to show an animated view, you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Creating_sequences_from_a_set_of_nodes" rel="nofollow noopener">create a sequence using Sequences extension</a>.</p>
<p>When you do segment registration, you can select two segments from any of the already loaded segmentations.</p>

---

## Post #5 by @Jainey (2019-06-18 20:15 UTC)

<p>Thank you Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
