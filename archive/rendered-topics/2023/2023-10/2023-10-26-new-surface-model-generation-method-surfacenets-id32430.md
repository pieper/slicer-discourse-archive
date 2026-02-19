---
topic_id: 32430
title: "New Surface Model Generation Method Surfacenets"
date: 2023-10-26
url: https://discourse.slicer.org/t/32430
---

# New surface model generation method: SurfaceNets

**Topic ID**: 32430
**Date**: 2023-10-26
**URL**: https://discourse.slicer.org/t/new-surface-model-generation-method-surfacenets/32430

---

## Post #1 by @Sam_Horvath (2023-10-26 18:20 UTC)

<p>We have now integrated the <a href="https://www.kitware.com/really-fast-isocontouring/">SurfaceNets isocontouring method</a> into “Show 3D” functionality of the Segment Editor!</p>
<p>The new experimental algorithm provides a ~7x speedup to the generation of surface models from segmentations compared to the default method (Flying Edges).  The option can be enabled from the Show 3D menu in the Segment Editor.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa0f30b0f9126fe9fbe67ffe83bad76b39329926.png" data-download-href="/uploads/short-url/ogpIjO8UmEKSgJymSQj2LvWkMey.png?dl=1" title="Screenshot 2023-10-26 13.52.11"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa0f30b0f9126fe9fbe67ffe83bad76b39329926_2_690x284.png" alt="Screenshot 2023-10-26 13.52.11" data-base62-sha1="ogpIjO8UmEKSgJymSQj2LvWkMey" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa0f30b0f9126fe9fbe67ffe83bad76b39329926_2_690x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa0f30b0f9126fe9fbe67ffe83bad76b39329926_2_1035x426.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa0f30b0f9126fe9fbe67ffe83bad76b39329926.png 2x" data-dominant-color="373F3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-26 13.52.11</span><span class="informations">1345×554 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Default FlyingEdges Method</th>
<th>SurfaceNets with default smoothing (fast)</th>
<th>SurfaceNets with built in Smoothing (faster)</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1d5243a8991793aab9222c2b7167cefe94a9fc4.jpeg" data-download-href="/uploads/short-url/tWgrAh1zmZb6wpgS9fTWnPQKvti.jpeg?dl=1" title="Screenshot 2023-10-26 14.17.35"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1d5243a8991793aab9222c2b7167cefe94a9fc4_2_493x500.jpeg" alt="Screenshot 2023-10-26 14.17.35" data-base62-sha1="tWgrAh1zmZb6wpgS9fTWnPQKvti" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1d5243a8991793aab9222c2b7167cefe94a9fc4_2_493x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1d5243a8991793aab9222c2b7167cefe94a9fc4_2_739x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1d5243a8991793aab9222c2b7167cefe94a9fc4_2_986x1000.jpeg 2x" data-dominant-color="7F909C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-26 14.17.35</span><span class="informations">1511×1467 52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e50e6029b5c590f36c6e264119c0c093a46c73c2.jpeg" data-download-href="/uploads/short-url/wGk8HFjr3yarCb136nvYuaCjvpM.jpeg?dl=1" title="Screenshot 2023-10-26 14.07.37"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e50e6029b5c590f36c6e264119c0c093a46c73c2_2_493x500.jpeg" alt="Screenshot 2023-10-26 14.07.37" data-base62-sha1="wGk8HFjr3yarCb136nvYuaCjvpM" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e50e6029b5c590f36c6e264119c0c093a46c73c2_2_493x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e50e6029b5c590f36c6e264119c0c093a46c73c2_2_739x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e50e6029b5c590f36c6e264119c0c093a46c73c2_2_986x1000.jpeg 2x" data-dominant-color="798D8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-26 14.07.37</span><span class="informations">1310×1327 49.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/816e3979bc17027722d68058710fccdb6e0f6e8c.jpeg" data-download-href="/uploads/short-url/isZKpH04RW6MrmvnOvOLvbCGaHa.jpeg?dl=1" title="Screenshot 2023-10-26 14.07.55"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/816e3979bc17027722d68058710fccdb6e0f6e8c_2_493x500.jpeg" alt="Screenshot 2023-10-26 14.07.55" data-base62-sha1="isZKpH04RW6MrmvnOvOLvbCGaHa" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/816e3979bc17027722d68058710fccdb6e0f6e8c_2_493x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/816e3979bc17027722d68058710fccdb6e0f6e8c_2_739x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/816e3979bc17027722d68058710fccdb6e0f6e8c_2_986x1000.jpeg 2x" data-dominant-color="7E8F99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-26 14.07.55</span><span class="informations">1417×1451 81.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
</tr>
</tbody>
</table>
</div><p>This feature is now available in the preview build of 3D Slicer.</p>
<p><a href="https://github.com/Slicer/Slicer/issues/7103">Issue</a><br>
<a href="https://github.com/Slicer/Slicer/pull/7224">Pull Request</a></p>

---

## Post #2 by @chir.set (2023-11-25 20:28 UTC)

<p>Hi,</p>
<p>I explored a little the new ‘Surface nets’ surface smoothing and made a side-by-side comparison as below with a tubular segment.</p>
<p>Globally, from the default algorithm to the ‘Fast’ and ‘Faster’ ones, it seems that shading and smoothing both decrease in that direction. With high smoothing factor, the difference tends to decrease, at least visually. The speed gain is of course of interest for huge segments.</p>
<p>The whole project can be downloaded <a href="https://disk.yandex.com/d/y7rfv1y2_EE9aA" rel="noopener nofollow ugc">here</a>.</p>
<p>The image below is posted for immediate reference. It uses a cropped isovoxel sample at 0.3 mm spacing (from CTA-cardio).</p>
<p>From left to right: default algorithm, ‘Fast’ and ‘Faster’<br>
From top to bottom: 0% smoothing factor, 10%,…,90%, 100%</p>
<p>Regards.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e745359c1adfd57adaabd97d75416ee5800b44dc.jpeg" data-download-href="/uploads/short-url/wZUzIKvKxyUZjPaZUpSgcK8yegk.jpeg?dl=1" title="SurfaceSmoothing_3x11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e745359c1adfd57adaabd97d75416ee5800b44dc_2_103x500.jpeg" alt="SurfaceSmoothing_3x11" data-base62-sha1="wZUzIKvKxyUZjPaZUpSgcK8yegk" width="103" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e745359c1adfd57adaabd97d75416ee5800b44dc_2_103x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e745359c1adfd57adaabd97d75416ee5800b44dc_2_154x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e745359c1adfd57adaabd97d75416ee5800b44dc_2_206x1000.jpeg 2x" data-dominant-color="151D15"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SurfaceSmoothing_3x11</span><span class="informations">930×4488 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @siqueirl (2023-12-01 19:26 UTC)

<p>Can this Surface generation be triggered from a loadable module and then accessed by this module?</p>

---
