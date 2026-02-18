# Coordinate Systems and Transformations in 3D Object Manipulation

**Topic ID**: 29618
**Date**: 2023-05-24
**URL**: https://discourse.slicer.org/t/coordinate-systems-and-transformations-in-3d-object-manipulation/29618

---

## Post #1 by @Dwij_Mistry (2023-05-24 04:46 UTC)

<p>Is there any direct option to translate or rotate an object using local coordinates?</p>
<p>By default, the translation and rotation actions in the 3D view operate in global coordinates.</p>
<p>The camera’s target always remains in the same position, but the body does move and shift around the target.</p>
<p>When performing a crop operation, it rotates with reference to its parent coordinate system instead of taking into account the reference of its own newly modified region to rotate.</p>
<h3><a name="p-95228-in-slicer-1" class="anchor" href="#p-95228-in-slicer-1" aria-label="Heading link"></a>in slicer</h3>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09da5a808719c9338d7b5a9466fbcf6a69e9fed9.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27028bcf767e5d32688a5301393f7b3161c692b6.jpeg" data-video-base62-sha1="1pa7hFLCojkzRxyhMwy0TaB6WSZ.mp4">
  </div><p></p>
<h3><a name="p-95228-in-blender-2" class="anchor" href="#p-95228-in-blender-2" aria-label="Heading link"></a>in blender</h3>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b4633259c0a314ecd37540c0940b155ab19111e.mp4">
  </div><p></p>

---

## Post #2 by @pieper (2023-05-24 17:50 UTC)

<p>Maybe you are looking for this feature:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#modify-transform" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#modify-transform</a></p>
<div class="youtube-onebox lazy-video-container" data-video-id="bbikx7Edv4g" data-video-title="Transforming objects using Data module in 3D Slicer" data-video-start-time="0" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=bbikx7Edv4g" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/bbikx7Edv4g/hqdefault.jpg" title="Transforming objects using Data module in 3D Slicer" width="480" height="360">
  </a>
</div>


---
