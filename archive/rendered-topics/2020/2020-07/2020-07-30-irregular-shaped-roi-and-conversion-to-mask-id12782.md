---
topic_id: 12782
title: "Irregular Shaped Roi And Conversion To Mask"
date: 2020-07-30
url: https://discourse.slicer.org/t/12782
---

# Irregular shaped ROI and conversion to mask

**Topic ID**: 12782
**Date**: 2020-07-30
**URL**: https://discourse.slicer.org/t/irregular-shaped-roi-and-conversion-to-mask/12782

---

## Post #1 by @rohan_n (2020-07-30 00:10 UTC)

<p>How can I create a 3D ROI of irregular shape (not rectangular prism)? Is the Closed Curve option in the Create and Place menu the only way to do this?<br>
I also want to be able to use this sort of irregular 3D ROI to create a mask within a scripted module that has the same shape as the input image, and has value 0 inside the 3D ROI and 1 outside of it. What would be the syntax for doing this?<br>
Thanks,<br>
Rohan Nadkarni</p>

---

## Post #2 by @lassoan (2020-07-30 00:29 UTC)

<p>There are lots of options for defining 3D ROIs. What shape are you creating? What is your overall goal?</p>

---

## Post #3 by @rohan_n (2020-07-30 17:14 UTC)

<p>I would like some tool that gives the user a lot of flexibility about how to define the shape – irregular contour.<br>
For my application, the 3D ROI, which is defined using a vtkMRMLAnnotationROINode, may contain some unwanted parts of the body in addition to the tumor we are interested in. The irregular shaped 3D region should overlap with the ROI, and this overlapping region is the omit region. For all feature maps computed from the 3D ROI, voxels within the omit region should have a value of 0, so that the feature map doesn’t compute feature values for the unwanted body parts.</p>

---

## Post #4 by @lassoan (2020-07-30 17:43 UTC)

<p>Do you want to segment tumors? Then the most suitable tool is probably Segment Editor.</p>
<p>If there is visible brightness difference between the tumor and surrounding region then probably the fastest is to use “Grow from seeds” (see “Tumor segmentation” section of <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Neurosurgical_Planning_Tutorial">Neurosurgical planning tutorial</a> for step-by-step instructions).</p>
<p>You can also segment tumors fully automatically using Nvidia <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#nvidia-ai-assisted-annotation-aiaa-for-3d-slicer">AI-based segmentation tool</a>.</p>
<p>If you need quick, <a href="https://youtu.be/90l0T1ADe_Y?t=55">intraoperative tumor segmentation on a touch screen</a> then you may use Surface Cut effect with a custom user interface (large buttons that makes it easy to use Slicer on a touchscreen).</p>
<p>There are many other tools and approaches implemented in Slicer. If you tell us more about what exactly you are trying to achieve then we can give more targeted advice.</p>

---

## Post #5 by @rohan_n (2020-07-30 18:18 UTC)

<p>Thanks for the comment, but segmentation is not the issue I’m concerned with. In fact, the whole purpose of my module is to perform a specific method of tumor segmentation within the region that the user specifies as containing tumor.</p>
<p>The problem I’m concerned with is related to ROI selection. Specifically, how to define a smaller region within the ROI that should have a value of 0 within the tumor mask.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77d305ba5b1c25a66e15aa838e4da488eb01315e.png" data-download-href="/uploads/short-url/h60VNTRf3wWUXYw0Sge4AnzgtWe.png?dl=1" title="tumorroiselection" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77d305ba5b1c25a66e15aa838e4da488eb01315e_2_690x496.png" alt="tumorroiselection" data-base62-sha1="h60VNTRf3wWUXYw0Sge4AnzgtWe" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77d305ba5b1c25a66e15aa838e4da488eb01315e_2_690x496.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77d305ba5b1c25a66e15aa838e4da488eb01315e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77d305ba5b1c25a66e15aa838e4da488eb01315e.png 2x" data-dominant-color="1D1C1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tumorroiselection</span><span class="informations">940×676 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please look at this image. My module computes a tumor mask within the region defined by the vtkMRMLAnnotationROINode. However, if we do not have an “omit region”, the heart (in bottom left of ROI) will be labeled incorrectly as tumor (value 1) in the tumor mask created by my module. I want to allow the user to define an omit region (shown in the image as the red shape) so that the module knows that the region of overlap between the red shape and the vtkMRMLAnnotationROINode should have value of 0 in the tumor mask. I’m asking how to make a 3D omit region of arbitrary shape.</p>
<p>I hope this is clear now.</p>
<p>Thanks for your help,<br>
Rohan</p>

---

## Post #6 by @lassoan (2020-07-30 19:19 UTC)

<p>For quick approximate segmentation (to create include/exclude regions) you can use Surface Cut effect:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' width="" height="">
  </a>
</div>

<p>You can also add/remove entire regions using Scissors effect in slice views.</p>
<p>You may also be able to create mask from a single click, by combination of Thresholding and Island effects.</p>
<p>It all depends on what are your constraints. If you just need to create training data set for deep learning based segmentation then using a combination of effects in Segment Editor effects should be good. After you segmented a few dozen images, you should be able to create your mask within a minute using existing tools.</p>

---

## Post #7 by @manjula (2020-07-30 23:05 UTC)

<p>Is there a way that we can create a cylinder and a cube by defining points in slicer view like in the case,</p>
<blockquote>
<p>Manipulating objects in the slice viewer in the 3D slicer scrip repository which creates a sphere.</p>
</blockquote>
<ul>
<li>How to define/edit a circular region of interest in a slice</li>
</ul>

---

## Post #8 by @lassoan (2020-07-31 00:29 UTC)

<p>Yes, instead of a <code>vtkSphereSource</code>, you can use a <code>vtkCylinderSource</code> or <code>vtkCubeSource</code>.</p>

---

## Post #10 by @mohammed_alshakhas (2021-03-02 09:23 UTC)

<p>found this searching for the same exact point .<br>
i want to create ROI around a mandible " very irregular shape" so i can  do different rendering for the mandible only , then segment a lesion within the mandible .</p>
<p>with the regular cube , i have to include maxilla and part of temporal bone .</p>
<p>if possible to create a ROI with a selection then render it as a volume would be great</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47d91d93c921c8947efbcea3a06be6cf7298c2d2.jpeg" data-download-href="/uploads/short-url/afB4ew8MZMw58fKrg6Xgdc8rKYG.jpeg?dl=1" title="Screen Shot 2021-03-02 at 12.22.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47d91d93c921c8947efbcea3a06be6cf7298c2d2_2_690x388.jpeg" alt="Screen Shot 2021-03-02 at 12.22.27" data-base62-sha1="afB4ew8MZMw58fKrg6Xgdc8rKYG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47d91d93c921c8947efbcea3a06be6cf7298c2d2_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47d91d93c921c8947efbcea3a06be6cf7298c2d2_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47d91d93c921c8947efbcea3a06be6cf7298c2d2_2_1380x776.jpeg 2x" data-dominant-color="91918D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-02 at 12.22.27</span><span class="informations">1920×1080 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @pieper (2021-03-02 12:40 UTC)

<p>You should be able to use the Mask Volume effect for that:</p>
<aside class="quote quote-modified" data-post="1" data-topic="699">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-editor-effects-mask-volume-and-surface-cut/699">New segment editor effects: Mask volume and Surface cut</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    See short demo video of the new “Mask volume” and “Surface cut” Segment editor effects here: 

These effects were developed by Kyle Macneil (Med-i Lab, Queen’s University; SPL, Brigham and Women’s Hospital), with help from <a class="mention" href="/u/lassoan">@lassoan</a>  and <a class="mention" href="/u/fedorov">@fedorov</a> . Thank you for your contribution! 
Mask volume: Blanks out a segment or surrounding area in a volumetric image. Useful for quick removal of unwanted objects (such as CT table) or showing only a selected organ. It can also be used for creating a binary m…
  </blockquote>
</aside>


---

## Post #12 by @slicer365 (2021-03-07 02:23 UTC)

<p>How to replace it, I know a little about python</p>

---

## Post #13 by @lassoan (2021-03-07 06:14 UTC)

<p>You don’t need to use Python, you can do everything via the graphical user interface.</p>
<p>To render the mandible differently, do as <a class="mention" href="/u/pieper">@pieper</a> suggested above: go to Segment Editor module, segment the mandible, then use Mask volume effect to blank out (set to -1000) everything outside the mandible segment. You can then use volume rendering to display just the mandible.</p>
<p>Are you planning to resect tumor and reconstruct the mandible using fibula free flap?</p>

---
