---
topic_id: 2405
title: "Crop Surface Mesh Vtk File"
date: 2018-03-22
url: https://discourse.slicer.org/t/2405
---

# Crop surface mesh (vtk file)

**Topic ID**: 2405
**Date**: 2018-03-22
**URL**: https://discourse.slicer.org/t/crop-surface-mesh-vtk-file/2405

---

## Post #1 by @Joelle (2018-03-22 19:35 UTC)

<p>Hi</p>
<p>I got a surface mesh (vtk PolyData) and would like to extract a certain part of it and save it as a new file. All the tutorials I found were for volume mesh.</p>
<p>Thanks for the help.</p>
<p>Cheers Joëlle</p>

---

## Post #2 by @lassoan (2018-03-22 20:04 UTC)

<p>All tutorials are for surface mesh. The segment editor always creates a closed surface mesh. Maybe you mean that you would like to create an open surface where you cut?</p>

---

## Post #3 by @Joelle (2018-03-24 19:22 UTC)

<p>I use the following model. I’m not sure what you mean by open surface. I assume you mean a volume which isn’t closed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c41fb990e431f7d9cce0389ccf59a0124a33d40.jpeg" data-download-href="/uploads/short-url/6jwnk8mNCJTdLLW5mnaNYRbWzJe.jpg?dl=1" title="15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_690x352.jpg" alt="15" data-base62-sha1="6jwnk8mNCJTdLLW5mnaNYRbWzJe" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_690x352.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_1035x528.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_1380x704.jpg 2x" data-dominant-color="A3A4C6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">15</span><span class="informations">5104×2608 1.23 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c41fb990e431f7d9cce0389ccf59a0124a33d40.jpeg" data-download-href="/uploads/short-url/6jwnk8mNCJTdLLW5mnaNYRbWzJe.jpg?dl=1" title="15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_690x352.jpg" alt="15" data-base62-sha1="6jwnk8mNCJTdLLW5mnaNYRbWzJe" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_690x352.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_1035x528.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_1380x704.jpg 2x" data-dominant-color="A3A4C6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">15</span><span class="informations">5104×2608 1.23 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c41fb990e431f7d9cce0389ccf59a0124a33d40.jpeg" data-download-href="/uploads/short-url/6jwnk8mNCJTdLLW5mnaNYRbWzJe.jpg?dl=1" title="15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_690x352.jpg" alt="15" data-base62-sha1="6jwnk8mNCJTdLLW5mnaNYRbWzJe" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_690x352.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_1035x528.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c41fb990e431f7d9cce0389ccf59a0124a33d40_2_1380x704.jpg 2x" data-dominant-color="A3A4C6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">15</span><span class="informations">5104×2608 1.23 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like to cut a certain area of this model. Is there an easy way to do this?</p>
<p>Thanks in advance.</p>

---

## Post #4 by @lassoan (2018-03-24 20:53 UTC)

<p>OK. For this, since you probably want to keep the open surface, probably the best tool is the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelClip">ModelClip module</a> (available in ModelClip extension).</p>

---

## Post #5 by @Joelle (2018-03-25 18:03 UTC)

<p>Hey<br>
My goal is to compare symmetry of the surface. But only on a certain part of the model. For this I need to be able to cut the model and save it as a new one.</p>
<p>I tried to work with ROI but I didn’t manage to only compare the ROI with each other.</p>
<p>To compare the surface I already asked once <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> (see link) <a href="https://discourse.slicer.org/t/surface-similarity-of-a-model/2287">Surface similarity of a model</a><br>
Thanks again</p>

---
