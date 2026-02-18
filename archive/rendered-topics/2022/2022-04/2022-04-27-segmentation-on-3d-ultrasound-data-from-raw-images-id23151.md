# Segmentation on 3D ultrasound data from raw images?

**Topic ID**: 23151
**Date**: 2022-04-27
**URL**: https://discourse.slicer.org/t/segmentation-on-3d-ultrasound-data-from-raw-images/23151

---

## Post #1 by @MCrouzier (2022-04-27 15:05 UTC)

<p>Dear all,</p>
<p>I am using 3D slicer (v4.11) to collect 3D-ultrasound data of some human body tendons.</p>
<p>I noticed that when I reconstruct a 3D volume from an ultrasound acquisition, I loose <strong>a lot</strong> in image quality (even when there is one single scan)</p>
<p>Thus, when I try to identify a structure (in my case, the Achilles tendon), which is quite clear on the raw ultrasound image, it gets really blurry in my 3D volume, and its very difficult to see accurately the edges.</p>
<p>I was wondering if it would be possible to do the segmentation on the raw images?<br>
In the “segment editor” module, it is so far not possible.</p>
<p>Thank you for your help,</p>
<p>Marion</p>

---

## Post #2 by @lassoan (2022-04-27 15:13 UTC)

<p>You can choose arbitrarily high resolution for your output 3D volume. There is no image quality loss then.</p>
<p>However, setting up very high resolution output volume for the reconstruction is often impractical, as you end up with an enormous volume that uses lots of memory and all computations take long time. You also tend to get more holes between the slices (because slices are thinner).</p>
<p>If you need to segment fine details in the image then it may be better to segment the image slices (where all the fine details are well visible) and then insert the segmented image into the volume. This is how we reconstruct bone surface in 3D using “AI” segmentation: the bone detection works on the 2D slice and the result is inserted into the 3D output volume:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="l0BcW8c9CnI" data-video-title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=l0BcW8c9CnI" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/l0BcW8c9CnI/maxresdefault.jpg" title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" width="" height="">
  </a>
</div>


---

## Post #3 by @Erick_Martinez (2024-12-02 12:34 UTC)

<p>I noticed that the AI segmentation uses a tissue specific pre-trained model, I am trying with ultrasound of a prostate phantom, is there any advice to achieve the 3D ultrasound segmentation of prostate? I would like to get a well segmented prostate ultrasound for further volume reconstruction and volume calculation.</p>

---

## Post #4 by @Blackmasc (2025-02-17 16:21 UTC)

<p>I’m working on a project to convert 2D ultrasound images into 3D models. I’m looking for open-source datasets that I can use to train my AI model.</p>
<p>Do you know of any publicly available datasets for 2D-to-3D ultrasound reconstruction? If not, could you recommend any resources or tools that might help me create my own dataset?</p>
<p>Thank you for your help!</p>

---
