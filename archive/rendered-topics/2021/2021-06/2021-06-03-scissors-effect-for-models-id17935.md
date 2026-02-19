---
topic_id: 17935
title: "Scissors Effect For Models"
date: 2021-06-03
url: https://discourse.slicer.org/t/17935
---

# Scissors effect for models

**Topic ID**: 17935
**Date**: 2021-06-03
**URL**: https://discourse.slicer.org/t/scissors-effect-for-models/17935

---

## Post #1 by @slicer365 (2021-06-03 15:44 UTC)

<p>Is there a good way for STL as is shown in the video,</p>
<p>Can we use Slicer to cut the part of model in the selected field of view.</p>
<p>The tool will be  very helpful.</p>
<p>Similar functions can be processed with scissors in segmentation,<br>
but I want to implement this function for a single stl model<br>
and I don’t want to convert the stl model to segmentation,<br>
because it will change the details of the model<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ffc22d66a8ab19d96281f2580a4bff5dfd1f102.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ffc22d66a8ab19d96281f2580a4bff5dfd1f102.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ffc22d66a8ab19d96281f2580a4bff5dfd1f102.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @muratmaga (2021-06-03 16:25 UTC)

<p>Scissors tool will do exactly this.</p>
<p>Default segmentation geometry estimated from stl to segmentation conversion may not be high enough (if you are loosing detail during the conversion process).</p>
<p>You can either try to use the oversampling (in the segmentation geometry setting), or create a blank high-resolution volume (ImageMaker extension) with small voxel size, and use the Segmentations-&gt;Import tab models  and refer that as the reference volume.</p>

---

## Post #3 by @lassoan (2021-06-03 19:31 UTC)

<p>I agree with <a class="mention" href="/u/muratmaga">@muratmaga</a> - for anatomical images that you show above Segment Editor should be perfect.</p>
<p>For cases when you need to combine anatomical models with CAD models (that tend to have sharp edges and may have very small details and tight tolerances) you may want to perform Boolean operations (add/remove/intersect) by keeping everything as surface mesh.</p>
<p>We don’t have an integrated “Scissors” tools for models yet, but you can achieve this function in a few steps:</p>
<ul>
<li>Create the cutting model: you can use Segment Editor’s Scissors effect for this (Fill mode) and export the created segment to mode; or create a model directly using MarkupsToModel extension; or load a model from an file and position it using a transform.<br>
-Use Combine models module (in Sandbox extension) to cut out this model from the other model.</li>
</ul>
<p>We plan to add surface editing features to the Segment Editor or add a dedicated Model Editor module (to keep things simpler). You can get a preview of what tools this new editor will have if you go to the “Dynamic modeler” module. For many years, having model editing capabilities were out of Slicer’s scope, because we did not want to step into the mesh editing arena. However, since mesh editing capabilities of MeshLab, Mesmhixer, Mimics, etc. essentially all stopped improving about 5 years ago, it is tempting to just add these features so that users don’t need to switch between multiple applications to implement their processing workflows. If there was dedicated funding or new developers interested in working on this then direct those to us. Without that, we can just develop it slowly, piece by piece, as side products from related funded projects.</p>

---

## Post #4 by @slicer365 (2021-06-03 23:27 UTC)

<p>Thank you very much for the efforts of the Slicer development team!</p>

---
