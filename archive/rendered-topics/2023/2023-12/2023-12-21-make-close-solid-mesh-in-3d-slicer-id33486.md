---
topic_id: 33486
title: "Make Close Solid Mesh In 3D Slicer"
date: 2023-12-21
url: https://discourse.slicer.org/t/33486
---

# Make close (solid) mesh in 3D Slicer

**Topic ID**: 33486
**Date**: 2023-12-21
**URL**: https://discourse.slicer.org/t/make-close-solid-mesh-in-3d-slicer/33486

---

## Post #1 by @park (2023-12-21 11:00 UTC)

<p>Hello all,</p>
<p>I am working on creating an implant guide with Slicer.</p>
<p>The issue I’m facing is closing an open dental scan mesh, as shown in the picture.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b719e13535c5d81ca9b9bfa974ad033352cd2539.png" alt="a" data-base62-sha1="q7MP5XSMpbVNWPAL6sqF9TB6RyF" width="506" height="207"></p>
<p>I tried using vtkfillholefilter (surface-toolbox fill holes), but as seen in the image, only some parts were filled, and the rest remained open.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef8d93ac41ea94bc250e330f5d2abea3339fbfd0.png" data-download-href="/uploads/short-url/ybbrqIi3LFMzlc0R2eCzZ0geUj6.png?dl=1" title="b" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef8d93ac41ea94bc250e330f5d2abea3339fbfd0_2_690x281.png" alt="b" data-base62-sha1="ybbrqIi3LFMzlc0R2eCzZ0geUj6" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef8d93ac41ea94bc250e330f5d2abea3339fbfd0_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef8d93ac41ea94bc250e330f5d2abea3339fbfd0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef8d93ac41ea94bc250e330f5d2abea3339fbfd0.png 2x" data-dominant-color="A6A658"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">b</span><span class="informations">704×287 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This resulted in an error when converting the model to a segmentation node.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61113992f225c04a98822793c17a960590216c0f.png" alt="c" data-base62-sha1="dQHdz69hGpz4a8cfshQlTit7YmP" width="360" height="340"></p>
<p>So, my questions are as follows:</p>
<ol>
<li>
<p>Is there an effective way to close the mesh? It’s okay to use a library other than VTK.</p>
</li>
<li>
<p>If closing the mesh proves challenging, is there a way to avoid errors when converting an open mesh to a segmentation node?</p>
</li>
</ol>
<ul>
<li>I would like to perform all process in Slicer not use other program</li>
</ul>
<p>I always receive valuable insights here.</p>
<p>Thank you.</p>

---
