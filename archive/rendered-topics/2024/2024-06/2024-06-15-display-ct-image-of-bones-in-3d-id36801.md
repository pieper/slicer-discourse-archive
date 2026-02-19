---
topic_id: 36801
title: "Display Ct Image Of Bones In 3D"
date: 2024-06-15
url: https://discourse.slicer.org/t/36801
---

# Display CT image of bones in 3D

**Topic ID**: 36801
**Date**: 2024-06-15
**URL**: https://discourse.slicer.org/t/display-ct-image-of-bones-in-3d/36801

---

## Post #1 by @WOOPIE (2024-06-15 05:12 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6d5afd15164fe2ab814d98c0430ba51fc5310e7.jpeg" data-download-href="/uploads/short-url/uEw01WTyXbyLIeGEL4Lk8XxILbN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6d5afd15164fe2ab814d98c0430ba51fc5310e7_2_282x500.jpeg" alt="image" data-base62-sha1="uEw01WTyXbyLIeGEL4Lk8XxILbN" width="282" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6d5afd15164fe2ab814d98c0430ba51fc5310e7_2_282x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6d5afd15164fe2ab814d98c0430ba51fc5310e7_2_423x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6d5afd15164fe2ab814d98c0430ba51fc5310e7.jpeg 2x" data-dominant-color="312F2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">541×958 60.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hello, i want to build a 3d model just looking like this picture using slicer program based on CT DICOM file. Is that possile? please help. thank you</p>

---

## Post #2 by @LeidyMoraV (2024-06-17 14:22 UTC)

<p>Yes, it is possible you would need to segment the CT image and then just show the 3D model.</p>
<p>This video might help: <a href="https://www.youtube.com/watch?v=0at15gjk-Ns" rel="noopener nofollow ugc">Creating femur model from CT volume using 3D Slicer (youtube.com)</a></p>

---

## Post #3 by @lassoan (2024-06-17 19:50 UTC)

<p>The screenshots above show a volume rendering of bones and implant from CT images, which don’t even need segmentation. So, all you need to do to achieve what is shown in the image is to go to <code>Data</code> module and drag-and-drop the CT image into a 3D view. You can further edit visualization settings in <code>Volume Rendering</code> module.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68814d74bc0f2ca7562749f5f8c09f779778cc68.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd4831a63a8793979d885924ed8464b7718033ac.jpeg">
  </div><p></p>

---
