---
topic_id: 19476
title: "Extract Segmentations Models"
date: 2021-09-01
url: https://discourse.slicer.org/t/19476
---

# Extract segmentations models

**Topic ID**: 19476
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/extract-segmentations-models/19476

---

## Post #1 by @NaghmehAnsari (2021-09-01 22:26 UTC)

<p>Hello,</p>
<p>I have segmented the head and ventricles from MRI images and decreased the head segmentation opacity to have ventricles visible.  For my application, I will need both head and ventricles as one model to be able to place the ventricles on the patient’s head accuratly. now I would like to extract them as one model ( single stl or obj file containing both segmentations). Is it possible to do in 3D slicer? and will the head’s segmentation opacity remain as I edited, to have ventricles visible?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-09-02 15:42 UTC)

<p>You can extract all models as one single obj file by checking “Merge into single file” option in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file">Export to files</a>.</p>
<p>Regardless of having those structures in one or more models, their position will not change. So, it should not be necessary to merge the files, and it is better if you don’t merge them because you can show/hide, adjust the opacity of the skin surface independently from the ventricles.</p>
<p>Are you implementing a Unity app for guiding ventriculostomy using HoloLens?</p>

---

## Post #3 by @NaghmehAnsari (2021-09-02 15:45 UTC)

<p>Yes, I need models for Hololens app</p>

---

## Post #4 by @lassoan (2021-09-02 17:44 UTC)

<p>OK, then definitely don’t merge the models, because you’ll just make your life harder.</p>
<p>Many groups have implemented such Unity application for the Hololens, for Burr hole placement for subdural hematoma and ventriculostomy. You don’t need to start from scratch but you can start from/contribute to these existing applications.</p>
<p>For example, you can use our <a href="https://github.com/PerkLab/HololensQuickNav">HololensQuickNav</a> application, which provides user interface for patient-to-hologram registration and selective display of skin surface, brain, target (ventricles, hematoma), planned trajectory. See a short demo video of registration:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="KdUdFQ44h3U" data-video-title="Augmented reality guidance for burr hole placement using HoloLens" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=KdUdFQ44h3U" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/KdUdFQ44h3U/maxresdefault.jpg" title="Augmented reality guidance for burr hole placement using HoloLens" width="" height="">
  </a>
</div>


---
