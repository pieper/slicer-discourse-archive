# How to cut polygons

**Topic ID**: 15608
**Date**: 2021-01-21
**URL**: https://discourse.slicer.org/t/how-to-cut-polygons/15608

---

## Post #1 by @slicer365 (2021-01-21 00:30 UTC)

<p>The scissor tool in the segment editor can be set to circle, square, and any shape. However, when cutting any shape, the edge is an irregular curve. Is there a way to set it as the linear shape between two points? I capture a picture, I hope my friends can understand what I mean and give me some suggestions. Of course, I’m talking about doing it in the segment editor, not after exporting the model. Because there are many steps to complete, it is trouble  to export the model repeatedly and then cut. It will be very convenient if scissor can be used  to cut directly to this shape under the line.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58203bc3dae57b592864347fba8eab2340cf3f94.jpeg" data-download-href="/uploads/short-url/czB4MZYYj5v5qqdNHMD57oQf1Dm.jpeg?dl=1" title="11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58203bc3dae57b592864347fba8eab2340cf3f94_2_394x375.jpeg" alt="11" data-base62-sha1="czB4MZYYj5v5qqdNHMD57oQf1Dm" width="394" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58203bc3dae57b592864347fba8eab2340cf3f94_2_394x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58203bc3dae57b592864347fba8eab2340cf3f94.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58203bc3dae57b592864347fba8eab2340cf3f94.jpeg 2x" data-dominant-color="6A8F68"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">11</span><span class="informations">568×539 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-21 00:38 UTC)

<p>If you need to combine segments with a predefined shape (e.g., for creating custom surgical guides) then you can create a model, position it freely using a transform (interactively in the viewer, or adjusting parameters in Transforms module or programmatically), then import it as a segment and combine with other segments using “Logical operators” effect.</p>

---

## Post #3 by @slicer365 (2021-01-21 00:46 UTC)

<p>Thanks to Professor Andras Lasso for the answer, but as you can see, it took me a long time to complete this puzzle. The different bone flaps are cut through straight lines, so it is more regular. Of course I used many steps of logic Calculation<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e46a86b4550f9a1884c108ccf362c7ebc865031.jpeg" data-download-href="/uploads/short-url/4jPHTjoZwyk9FshtIunoQd4qJzP.jpeg?dl=1" title="微信图片_20210121084056" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e46a86b4550f9a1884c108ccf362c7ebc865031_2_472x500.jpeg" alt="微信图片_20210121084056" data-base62-sha1="4jPHTjoZwyk9FshtIunoQd4qJzP" width="472" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e46a86b4550f9a1884c108ccf362c7ebc865031_2_472x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e46a86b4550f9a1884c108ccf362c7ebc865031.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e46a86b4550f9a1884c108ccf362c7ebc865031.jpeg 2x" data-dominant-color="9D9E99"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20210121084056</span><span class="informations">652×690 95.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-01-21 01:06 UTC)

<p>All built-in modules are general-purpose tools. They are very flexible and can be used to design and test a processing workflow.</p>
<p>Once you know exactly what you want to do (validated the workflow on a few dozens of cases manually), you can create application-specific tool, which is as simple and convenient as possible (only show relevant options, require the minimum necessary user inputs). This application-specific tool will be always much, much better for that particular task than any general-purpose tool. In Slicer, these are usually implemented as small Python scripted modules.</p>
<p>For your use case, you could specify a few cut planes and markup points and based on that perform the cutting and remodeling fully automatically (or maybe controlled by a few parameters). You can use Dynamic Modeler module to cut up a model automatically using multiple cutting planes. You may get some inspiration from this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F6fNMQTxD-4" data-video-title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F6fNMQTxD-4/maxresdefault.jpg" title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" width="" height="">
  </a>
</div>


---
