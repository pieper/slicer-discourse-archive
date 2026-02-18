# Display the shape of the bone surface within closed line

**Topic ID**: 23100
**Date**: 2022-04-24
**URL**: https://discourse.slicer.org/t/display-the-shape-of-the-bone-surface-within-closed-line/23100

---

## Post #1 by @zhiyuan (2022-04-24 05:44 UTC)

<p>I would like to ask if slicer has such a function that I draw a closed line on the segmented bone model, and then only display the shape of the bone surface within the closed line</p>

---

## Post #2 by @lassoan (2022-04-24 05:52 UTC)

<p>It is not clear for me what exactly you need, but the <code>Scissors</code> effect in Segment Editor module may be what you are looking for.</p>
<p>If that effect does not fulfill all your needs then please describe the clinical task that you want to solve and provide a few illustrative screenshots.</p>

---

## Post #4 by @zhiyuan (2022-04-24 05:58 UTC)

<p>I use slicer to mark the femur, and then only display the marked 3D model. I want to use certain technology on this model to only need the shape of the blue area. Does slicer have this function, so that I can mark similar areas and then generate the shape of a specific area<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86f761c3def7142b1528f7a68267db7c74b5ec28.png" data-download-href="/uploads/short-url/jfXZE6UVRQ7Qsq73bSGc4kb0kQg.png?dl=1" title="图片1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86f761c3def7142b1528f7a68267db7c74b5ec28_2_622x500.png" alt="图片1" data-base62-sha1="jfXZE6UVRQ7Qsq73bSGc4kb0kQg" width="622" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86f761c3def7142b1528f7a68267db7c74b5ec28_2_622x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86f761c3def7142b1528f7a68267db7c74b5ec28.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86f761c3def7142b1528f7a68267db7c74b5ec28.png 2x" data-dominant-color="1D010B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片1</span><span class="informations">640×514 66.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2022-04-24 19:09 UTC)

<p>Yes, you can do this very easily in Slicer. Export the segmentation to a model (by right-clicking on the segmentation in the Data module) and then use <code>Dynamic modeler</code> module’s <code>Curve cut</code> or <code>Select by points</code> tool to extract a surface patch. Use the most recent Slicer Preview Release, as it contains required fixes and improvements in <code>Dynamic modeler</code> module.</p>

---

## Post #6 by @zhiyuan (2022-04-25 07:51 UTC)

<p>I found this page and have exported the segmentation to the model, but why can’t I cut on the model after clicking curve cut<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/769ec364cb1e0a9a58f42c0fb366322658d90e56.png" data-download-href="/uploads/short-url/gVmuopzXFYV5AgHVh2QWS5bipAW.png?dl=1" title="SH5Y8J3LERYR6N(P647DDDL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/769ec364cb1e0a9a58f42c0fb366322658d90e56_2_268x499.png" alt="SH5Y8J3LERYR6N(P647DDDL" data-base62-sha1="gVmuopzXFYV5AgHVh2QWS5bipAW" width="268" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/769ec364cb1e0a9a58f42c0fb366322658d90e56_2_268x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/769ec364cb1e0a9a58f42c0fb366322658d90e56_2_402x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/769ec364cb1e0a9a58f42c0fb366322658d90e56.png 2x" data-dominant-color="2F3134"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SH5Y8J3LERYR6N(P647DDDL</span><span class="informations">488×908 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2022-04-25 12:29 UTC)

<ol>
<li>You must to use the latest Slicer Preview Release. The screenshot shows an earlier Slicer version.</li>
<li>Click <code>Apply</code> (or check the checkbox on the <code>Apply</code> button for continuous updates).</li>
<li>Make the input model semi-transparent so that it does not occlude your output models</li>
<li>Make the output models different color or create only one output model (because the inside and outside models together make up the complete model, so you will not see that the model has been cut)</li>
</ol>

---
