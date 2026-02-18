# How to Implement Marker-Based Tracking and 3D Visualization in 3D Slicer (Similar to Video Example)

**Topic ID**: 41473
**Date**: 2025-02-03
**URL**: https://discourse.slicer.org/t/how-to-implement-marker-based-tracking-and-3d-visualization-in-3d-slicer-similar-to-video-example/41473

---

## Post #1 by @Navneet (2025-02-03 21:05 UTC)

<p><strong>Hello 3D Slicer Community,</strong></p>
<p>I am looking to replicate a system similar to the one demonstrated in this video: <a href="https://www.youtube.com/watch?v=MOqh6wgOOYs" rel="noopener nofollow ugc">Marker-Based Tracking and Visualization in 3D Slicer</a>. The system involves:</p>
<ol>
<li>Using a physical marker (e.g., fiducial/AR marker) to track an object in real-time.</li>
<li>Aligning and rendering 3D models (e.g., a cylinder or box) based on the position and orientation of the marker.</li>
<li>Real-time updates of the 3D visualization when the marker is moved.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/389b50b247b96d7c0dc158da8dccd3ebc73207f7.png" data-download-href="/uploads/short-url/84LuYJmu1WPzFNxru3BUGwLU1WT.png?dl=1" title="Tracker" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/389b50b247b96d7c0dc158da8dccd3ebc73207f7_2_690x496.png" alt="Tracker" data-base62-sha1="84LuYJmu1WPzFNxru3BUGwLU1WT" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/389b50b247b96d7c0dc158da8dccd3ebc73207f7_2_690x496.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/389b50b247b96d7c0dc158da8dccd3ebc73207f7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/389b50b247b96d7c0dc158da8dccd3ebc73207f7.png 2x" data-dominant-color="454E57"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Tracker</span><span class="informations">919×661 93.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>

---
