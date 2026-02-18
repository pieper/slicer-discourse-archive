# How to Get skeleton of pulmonary vascular system

**Topic ID**: 13502
**Date**: 2020-09-16
**URL**: https://discourse.slicer.org/t/how-to-get-skeleton-of-pulmonary-vascular-system/13502

---

## Post #1 by @shahrokh (2020-09-16 14:00 UTC)

<p>Hello Dear Developers and Users</p>
<p>Excuse me for asking a question that might be obvious to many:<br>
Is there a difference between <strong>Skeleton</strong> and <strong>Centerline</strong>?</p>
<p>I want to extract a skeleton of the pulmonary vascular system (vascular tree) .</p>
<p>To do this, I did the following steps:</p>
<p>1- Segment pulmonary vascular system (tree) using <em>Frangi filter</em> on <strong>VMTK</strong> with  <em>vmtkimagevesselenhancement</em>.</p>
<p>2- Convert it to labelMapVolume</p>
<p>3- In the last step, I want to use the <strong>Extract Skeleton</strong> module to extract <em>the skeleton of vascular tree</em>.</p>
<p>I have the following questions about this module:</p>
<p>A. What is the difference between tow modes <strong>1D</strong> and <strong>2D</strong> in <strong>Skeleton Type</strong>?</p>
<p>B. This module does not finish when I select <strong>Skeleton Type</strong> in <strong>2D</strong> mode.</p>
<p>Although I select the number of 100 in the <strong>Number Of Points</strong> section, I see the coordinates of fewer points (about 40) in the <strong>skeleton.txt</strong> file. Why?</p>
<p>Why am I not able to get/see the <strong>Skeleton</strong> of these vessels in 3D view?</p>
<p>The image below is a demonstration of these pulmonary vessels in the type of <strong>Model</strong>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22a7807e2bfd0c176b63aeed6f86009fff30af9a.jpeg" data-download-href="/uploads/short-url/4Wz6wrFPkYD8uDTEZ4KdaRdGPAS.jpeg?dl=1" title="vessels" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22a7807e2bfd0c176b63aeed6f86009fff30af9a_2_688x500.jpeg" alt="vessels" data-base62-sha1="4Wz6wrFPkYD8uDTEZ4KdaRdGPAS" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22a7807e2bfd0c176b63aeed6f86009fff30af9a_2_688x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22a7807e2bfd0c176b63aeed6f86009fff30af9a_2_1032x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22a7807e2bfd0c176b63aeed6f86009fff30af9a.jpeg 2x" data-dominant-color="7B8998"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vessels</span><span class="informations">1260×915 861 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Please guide me.<br>
Thanks a lot.<br>
Shahrokh.</p>

---

## Post #2 by @shahrokh (2020-09-17 07:26 UTC)

<p>Hello<br>
I hope I have explained what I mean clearly.<br>
I do not understand why the <strong>Extract Skeleton</strong> module cannot extract the skeleton.<br>
Is this node (LabelMapVolume node) too complicated?</p>
<p>As can be seen in the following image, some parts of the vessels are disconnected and not connected to each other. Does this prevent this module from extracting the skeleton of vascular tree?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3dd751f47e10542459934969f266dd57c0bc00.jpeg" data-download-href="/uploads/short-url/fry3LuvqjH2qL3rp50u7inDt0uk.jpeg?dl=1" title="SceneView" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3dd751f47e10542459934969f266dd57c0bc00_2_688x500.jpeg" alt="SceneView" data-base62-sha1="fry3LuvqjH2qL3rp50u7inDt0uk" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3dd751f47e10542459934969f266dd57c0bc00_2_688x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3dd751f47e10542459934969f266dd57c0bc00_2_1032x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3dd751f47e10542459934969f266dd57c0bc00.jpeg 2x" data-dominant-color="6B7F7F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView</span><span class="informations">1260×915 976 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Can I have to isotropic spacing CT images at the beginning of processing?</p>
<p>Please guide me.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #3 by @shahrokh (2020-09-21 15:44 UTC)

<p>To do this, I did the following steps.<br>
The following steps were performed to extract the skeleton of pulmonary vascular system, respectively.</p>
<p>1- Segment the lung region from the chest CT image</p>
<p>2- Segment the pulmonary vessels by applying the <strong>Frangi filter</strong> (argument) in the command of <strong>vmtkimagevesselenhancement</strong></p>
<p>3- Apply <strong>Threshold Effect</strong> in the module of <strong>Segment Editor</strong></p>
<p>4- Removal of the outer edge of the lung region and the common border between the lung and the heart by the <strong>Sobel filter</strong> in the module of <strong>Simple Fiters</strong></p>
<p>5- Split segmented vessel tree by <strong>Island Effect</strong> (<strong>Split islands to segments</strong>) in the module of <strong>Segment Editor</strong></p>
<p>6- Convert the result of the previous step to <strong>Model</strong> and save them in <strong>vtp</strong> format</p>
<p>7- Merge vessel component models by the <strong>MergeModels</strong> (CLI)</p>
<p>The following image is shown in the result of above steps.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/037e40e06f19a9bcef5b152a4f0e9e693a01d75c.jpeg" data-download-href="/uploads/short-url/uTVByKbVSap9C0XwaaXK97suHa.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/037e40e06f19a9bcef5b152a4f0e9e693a01d75c_2_677x499.jpeg" alt="1" data-base62-sha1="uTVByKbVSap9C0XwaaXK97suHa" width="677" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/037e40e06f19a9bcef5b152a4f0e9e693a01d75c_2_677x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/037e40e06f19a9bcef5b152a4f0e9e693a01d75c_2_1015x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/037e40e06f19a9bcef5b152a4f0e9e693a01d75c.jpeg 2x" data-dominant-color="8F97B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1260×930 706 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can be seen in the following image, the centerline of some parts of the vessels has not been extracted. Why?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4577681fb957e21ad865404f8bed00283bf3f277.jpeg" data-download-href="/uploads/short-url/9UwLWdjYwIv3EEt6Bgmk5JdwYp9.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4577681fb957e21ad865404f8bed00283bf3f277_2_688x500.jpeg" alt="2" data-base62-sha1="9UwLWdjYwIv3EEt6Bgmk5JdwYp9" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4577681fb957e21ad865404f8bed00283bf3f277_2_688x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4577681fb957e21ad865404f8bed00283bf3f277_2_1032x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4577681fb957e21ad865404f8bed00283bf3f277.jpeg 2x" data-dominant-color="8792A3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1260×915 949 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In these regions, I extracted the centerlines using the module of <strong>Extract Centerline</strong>.</p>
<p>Please guide me.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #4 by @lassoan (2020-09-21 18:36 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="13502">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Is there a difference between <strong>Skeleton</strong> and <strong>Centerline</strong> ?</p>
</blockquote>
</aside>
<p>No difference, they both refer to the same thing: medial line or surface.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="13502">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>What is the difference between tow modes <strong>1D</strong> and <strong>2D</strong> in <strong>Skeleton Type</strong> ?</p>
</blockquote>
</aside>
<p>1D enforces extraction of a line (medial line), 2D extracts a surface (medial surface).</p>
<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="13502">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>This module does not finish when I select <strong>Skeleton Type</strong> in <strong>2D</strong> mode.</p>
</blockquote>
</aside>
<p>Computation time may be very long for 2D mode.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="13502">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Although I select the number of 100 in the <strong>Number Of Points</strong> section, I see the coordinates of fewer points (about 40) in the <strong>skeleton.txt</strong> file.</p>
</blockquote>
</aside>
<p>Number of points specifies the maximum. If your image has lower resolution and the centerline is short then the line may be represented with less points than what you have requested. If you need more points then you can get arbitrarily resampling of the curve using markups module.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="13502">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Why am I not able to get/see the <strong>Skeleton</strong> of these vessels in 3D view?</p>
</blockquote>
</aside>
<p>Result of “Extract skeleton” module is a labelmap volume. You can use volume rendering or you can import it into Segmentation to visualize in 3D views.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="2" data-topic="13502">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Can I have to isotropic spacing CT images at the beginning of processing?</p>
</blockquote>
</aside>
<p>If the difference between spacing along different axis is more than a few ten percent then I would recommend to use Crop volume to crop and resample the volume using isotropic spacing.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="3" data-topic="13502">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Split segmented vessel tree by <strong>Island Effect</strong> ( <strong>Split islands to segments</strong> ) in the module of <strong>Segment Editor</strong></p>
<p>6- Convert the result of the previous step to <strong>Model</strong> and save them in <strong>vtp</strong> format</p>
<p>7- Merge vessel component models by the <strong>MergeModels</strong> (CLI)</p>
</blockquote>
</aside>
<p>This is unnecessarily complicated and slow way of removing small islands. You can achieve the same by using “Remove small islands” method in Islands effect.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="3" data-topic="13502">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>As you can be seen in the following image, the centerline of some parts of the vessels has not been extracted. Why?</p>
</blockquote>
</aside>
<p>Probably those branches are too small. If you share the scene that contains the segmentation that you created using Thresholding effect (but before Island effect applied or other further processing is done) then I may have a look.</p>

---

## Post #5 by @shahrokh (2020-09-23 14:52 UTC)

<p>Dear Dr. Andras Lassoan</p>
<p>Thank you so much for your detailed explanation. Excuse me, but I do not understand how to share with you the scene that contains the segmentation. Do you mean a scene with .mrml extension (MRML scene) or .mrb extension (Medical Reality Bundle)? Where should I upload this file?</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #6 by @lassoan (2020-09-23 14:57 UTC)

<p>Upload the mrb file anywhere (dropbox, onedrive, google drive, …) and post the link here. Make sure not patient information is included.</p>

---

## Post #7 by @shahrokh (2020-09-24 20:38 UTC)

<p>I upload .mrb file in dropbox.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/c0avqviz6mhb6cz/Scene.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/c0avqviz6mhb6cz/Scene.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">Scene.mrb</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thanks a lot.<br>
Shahrokh.</p>

---

## Post #8 by @Montes_de_Oca_Delgad (2022-09-22 05:32 UTC)

<p>Hello.</p>
<p>I have a question. To which volume have you applied the filter? I have some problems with the segmentation of the vessels.</p>
<p>Thank you</p>

---
