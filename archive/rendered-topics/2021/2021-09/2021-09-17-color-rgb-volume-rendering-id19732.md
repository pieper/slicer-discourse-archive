# Color (RGB) volume rendering

**Topic ID**: 19732
**Date**: 2021-09-17
**URL**: https://discourse.slicer.org/t/color-rgb-volume-rendering/19732

---

## Post #1 by @lassoan (2021-09-17 23:56 UTC)

<p>In recent Slicer Preview Releases, color volume rendering has been made much easier to access. While previously an alpha channel had to be created manually for rendering color RGB volumes, now the alpha channel is created automatically (from the luminance of the image).</p>
<p>To render an RGB volume, just load the image stack and drag-and-drop the volume from the Data module to a 3D view (or use Volume Rendering module). When a color volume is loaded then “Scalar Color Mapping” section is not displayed in Volume Rendering module, as no color mapping is performed - but the specified voxel colors are used directly.</p>
<p>Example 1: <a href="https://www.nlm.nih.gov/research/visible/visible_human.html">Visible human project</a> female data set cryosection:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="sCKLRAXTSFQ" data-video-title="Color (RGB) volume rendering" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=sCKLRAXTSFQ" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/sCKLRAXTSFQ/maxresdefault.jpg" title="Color (RGB) volume rendering" width="" height="">
  </a>
</div>

<p>Example 2: Sample data set <a href="https://discourse.slicer.org/t/retain-image-color-in-volume-rendering/12294/10">provided by a Slicer user</a>:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="o5I_XWkm1nk" data-video-title="Color volume rendering" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=o5I_XWkm1nk" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/o5I_XWkm1nk/maxresdefault.jpg" title="Color volume rendering" width="" height="">
  </a>
</div>


---
