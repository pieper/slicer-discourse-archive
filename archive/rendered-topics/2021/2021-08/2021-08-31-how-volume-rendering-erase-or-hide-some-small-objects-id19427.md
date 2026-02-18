# How volume rendering erase or hide some small objects?

**Topic ID**: 19427
**Date**: 2021-08-31
**URL**: https://discourse.slicer.org/t/how-volume-rendering-erase-or-hide-some-small-objects/19427

---

## Post #1 by @StephenLeePeng (2021-08-31 09:17 UTC)

<p>When I load a CT-Chest volume with a lung nodule inside, I want to crop a region contain the lung nodule, and rendering volume to display the nodule and the vessel arround the nodule.</p>
<p>The problem is, when I adjust shift slider, Scalar Opacity Mapping, or some other parameters, volume rendering result is not ideal. When I set the lower threshold too much, some more small, discontinuous objects will appear, when I set the lower threshold too high, some small, may important vessel will disappear.</p>
<p>When I asked the Radiology doctors, they say there exist a button or module in their PACS postprocess workstation, can erase some small tiny objects in the volume rendering result.</p>
<p>So I want to know, is there exist a module similar to above description to realize the effect to clear those some tiny objects.</p>
<p>As follow is a volume rendering picture, there exist some small tiny,  discontinuous vessel parts, and I want to erase them to make the result more clearly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/852e99f5af3d95f2207b91d9e17bd98465d845a9.jpeg" data-download-href="/uploads/short-url/j0blupaNG1sFnujTrcJkAuY9rmN.jpeg?dl=1" title="volume_rendering1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/852e99f5af3d95f2207b91d9e17bd98465d845a9_2_690x437.jpeg" alt="volume_rendering1" data-base62-sha1="j0blupaNG1sFnujTrcJkAuY9rmN" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/852e99f5af3d95f2207b91d9e17bd98465d845a9_2_690x437.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/852e99f5af3d95f2207b91d9e17bd98465d845a9_2_1035x655.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/852e99f5af3d95f2207b91d9e17bd98465d845a9.jpeg 2x" data-dominant-color="553920"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume_rendering1</span><span class="informations">1233×781 61.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-09-01 03:07 UTC)

<p>The feature is called “Mask volume”, it is available in Segment Editor. See step-by-step instructions in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html#hide-certain-regions-of-the-volume">module documentation</a> and in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' width="" height="">
  </a>
</div>


---
