# Mandibular reconstruction in Slicer

**Topic ID**: 14228
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/mandibular-reconstruction-in-slicer/14228

---

## Post #1 by @mau_igna_06 (2020-10-24 21:34 UTC)

<p>This is a question for experts in python scripting here on the Slicer Forum: Is it possible to develop <a href="https://youtu.be/KYZlEP9mHvw?t=45" rel="noopener nofollow ugc">this</a> surgical planning on Slicer? I mean achieving in Slicer everything that is done in that video including the osteotomy over the fibula and the reconstruction on the mandible with the fibula-pieces</p>

---

## Post #2 by @lassoan (2020-10-25 01:27 UTC)

<p>Yes, it is certainly possible. All the necessary infrastructure is already available in Slicer and you only need custom Python script for automatically generating the cut-outs from the fibula based on the line segments drawn on the mirrored mandible (should be quite straightforward) and for putting everything together in a nice, convenient graphical user interface.</p>
<p>You can define cutting planes almost exactly the same, then you can use Dynamic modeler module to cut models and mirror the healthy side:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F6fNMQTxD-4" data-video-title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F6fNMQTxD-4/maxresdefault.jpg" title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" width="" height="">
  </a>
</div>

<p>You can define line segments by placing Markups Curve on the mirrored surface. This could be made even more automated than it is shown in the demo video, as you could extract centerline of the bone (using VMTK extension) and initialize the curve using that.</p>
<p>Slicer is not just for planning but can be also used for navigation of the bone cuts, either using commercial navigation systems or other position trackers.</p>
<p>Of course, you need to do risk assessment, testing, obtain institutional or regulatory approval, etc. before using anything that you develop to treat patients.</p>

---

## Post #4 by @lassoan (2020-10-28 04:13 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/custom-fitting-surgical-guides-on-slicer/14270/2">Custom‐fitting Surgical Guides on Slicer</a></p>

---

## Post #5 by @lassoan (2021-05-16 13:07 UTC)

<p>A post was split to a new topic: <a href="/t/new-3d-slicer-extension-for-planning-and-surgical-guide-generation-for-mandibular-bone-reconstruction/17638">New 3D Slicer extension for planning and surgical guide generation for mandibular bone reconstruction</a></p>

---
