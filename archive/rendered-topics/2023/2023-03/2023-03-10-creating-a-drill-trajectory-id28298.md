---
topic_id: 28298
title: "Creating A Drill Trajectory"
date: 2023-03-10
url: https://discourse.slicer.org/t/28298
---

# Creating a drill trajectory

**Topic ID**: 28298
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/creating-a-drill-trajectory/28298

---

## Post #1 by @jtk (2023-03-10 20:19 UTC)

<p>Hi, I am trying to make a drill hole through a segmented CT scan. I was wondering if there was a way to make this in slicer and know the coordinates of the centre of the entry and exit points?</p>

---

## Post #2 by @lassoan (2023-03-11 06:51 UTC)

<p>You can draw a trajectory line using Markups module. If you want to simulate drilling (drill a hole in the image) then you can use Segment Editor - Draw tube effect followed by Mask volume effect.</p>

---

## Post #3 by @jtk (2023-03-18 15:27 UTC)

<p>Thanks Andras, where do I find the draw tube effect?</p>

---

## Post #4 by @lassoan (2023-03-18 17:42 UTC)

<p>Draw Tube effect is provided by SegmentEditorExtraEffects extension. If you install this extension then the effect will show up in Segment Editor.</p>

---

## Post #5 by @jtk (2023-03-19 11:44 UTC)

<p>thanks Andras, I use the effect but it just makes a solid tube, do I need to form a new segmentation to remove this from?</p>
<p>Is there also a way to export my line as a coordinate system?</p>
<p>sorry for all the questions</p>

---

## Post #6 by @lassoan (2023-03-19 12:06 UTC)

<p>What is your end goal? Do you want to display trajectory as surface mesh or using volume tendering, in slice views, 3D views, virtual reality, augmented reality, as volume rendering 3D print it, export it to rgb viewer or to commercial surgical navigation system, or do surgical navigation Slicer, explore what is around the trajectory,… all doable in Slicer.</p>
<p>Please describe the driving clinical application, too (pedicle screw, spinal injections, craniostomy for subdural hematoma, breast/liver/prostate tumour, valve replacement, etc) because we have lots of experience to share about planning and guiding specific procedures in Slicer.</p>

---

## Post #7 by @jtk (2023-03-19 15:25 UTC)

<p>My end goal is to use the trajectory for navigation in slicer and also to produce surgical guides with the same trajectory in blender software, although I would like to be able to do this in slicer if possible. This is for placing a screw in the elbow.</p>
<p>I need to see the trajectory within the slices so I can check it does not exit the bone for drilling the screw.</p>
<p>thanks for offering to help</p>

---

## Post #8 by @lassoan (2023-03-19 20:10 UTC)

<p>I would recommend this workflow:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="2MOAk2oNbKw" data-video-title="Combine patient and CAD models in 3D Slicer using union/intersection/difference operations" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2MOAk2oNbKw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2MOAk2oNbKw/maxresdefault.jpg" title="Combine patient and CAD models in 3D Slicer using union/intersection/difference operations" width="" height="">
  </a>
</div>

<p>If you don’t want to use a 3D-printed guide then you can set up optical or electromagnetic tracking as described in <a href="https://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>.</p>
<p>I would also recommend to consider using ultrasound for real-time imaging and guidance. See for example this demo:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="2vXeJxYFou4" data-video-title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2vXeJxYFou4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2vXeJxYFou4/maxresdefault.jpg" title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" width="" height="">
  </a>
</div>


---

## Post #9 by @BDhoth (2024-10-02 14:50 UTC)

<p>I was looking for assistance on this same topic, though I don’t think the video you shared helps my case. We are looking for a trajectory for a pedicle screw. We are able to have the start and end points show up on the model after going through blender and then to the AR headset, but can’t figure out how to get the trajectory line to be in the model. Thank you for your help.</p>

---

## Post #10 by @lassoan (2024-10-02 17:54 UTC)

<p>There have been lots of work in Slicer for pedicle screw insertion planning and guidance (by augmented reality using HoloLens, ultrasound guidance, etc.).</p>
<p>There is a complete open-source implementation for HoloLens/Slicer see github repository here (and related <a href="https://www.researchgate.net/publication/371537888_Real-time_integration_between_Microsoft_HoloLens_2_and_3D_Slicer_with_demonstration_in_pedicle_screw_placement_planning">paper</a>):</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning">
  <header class="source">

      <a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/586853a027248a7f7464a47332482b38/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" class="thumbnail">

  <h3><a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" target="_blank" rel="noopener">GitHub - BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning: GitHub repository for the IJCARS paper: "Real-Time...</a></h3>

    <p><span class="github-repo-description">GitHub repository for the IJCARS paper: "Real-Time open-source integration between Microsoft HoloLens 2 and 3D Slicer"</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>No need to mess with Blender, but the scene is generated in Slicer and sent to the HoloLens directly from there in real-time. Rendering in this repository is done via Unity, but recent Slicer versions can render directly to any AR/VR headset (via OpenXR API). So, there is no need to use multiple applications and programming languages (everything can be implemented in a single Slicer application, in Python or C++).</p>
<p>What AR headset are you planning to use now that the HoloLens is dead? Video passthrough in Meta Quest 3?</p>

---

## Post #11 by @Guilherme_Augusto (2024-10-18 10:22 UTC)

<p>Is it possible to establish landmarking so that the created image can be superimposed onto the patient’s reality?</p>

---

## Post #12 by @lassoan (2024-10-18 10:30 UTC)

<p>Yes, sure. Tou can segment the skin surface, mark any anatomical landmarks, and draw a trajectory line (for example, using markups, segmentation). You can then put all these under the same transform, grab them with your hand, and manually align with the patient.</p>

---

## Post #13 by @Guilherme_Augusto (2024-10-18 12:05 UTC)

<p>Is there any tutorial on how to draw a trajectory line automatically?"</p>

---

## Post #14 by @JASON (2024-10-18 12:50 UTC)

<p>Here’s an example of creating a line markup</p>
<pre><code class="lang-auto">import numpy as np
lineNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode")
linePoints = np.array((-50,-50,-50), (0,0,0))
slicer.util.updateMarkupsControlPointsFromArray(lineNode, linePoints)
</code></pre>

---

## Post #15 by @Guilherme_Augusto (2024-10-18 13:04 UTC)

<p>Is there any tutorial that explains how to successfully connect Slicer with Unity to interact with the HoloLens after inserting this code? Specifically, are there any additional steps or requirements to ensure smooth communication between Slicer, Unity, and the HoloLens?</p>

---

## Post #16 by @lassoan (2024-10-18 16:52 UTC)

<p>You can use OpenIGTLink for real-time data transfer between Slicer and Unity (see for example <a href="https://discourse.slicer.org/t/creating-a-drill-trajectory/28298/10">above</a>). It can work well for game-like experiences, such as surgical simulations.</p>
<p>However, for actual clinical applications, image-guided surgical interventions, building on a medical image computing platform (Slicer) should work much better than game engines (Unity, Unreal, etc.). You can create the surgical plan, review the images in slice and 3D views, do all the registration you need, including non-linear distortions, etc. do real-time segmentation and everything else you need in Slicer and then with a single click you can display that 3D scene in the HoloLens. The scene remains interactive both in the HoloLens and in Slicer, so you can keep assisting the user who is wearing the HoloLens. No need to synchronize information between multiple applications, everything works in a single environment, single process, single programming language (Python).</p>

---

## Post #17 by @Guilherme_Augusto (2024-10-21 23:14 UTC)

<p>I am having a lot of difficulty using another model besides the pre-programmed spine in the repository. Is there any help available regarding these configurations?</p>
<p>I am having trouble setting up the connection with the clipping plane and pre-programming it for another desired model instead of the default one. Could you provide guidance on how to configure this?</p>

---

## Post #18 by @lassoan (2024-10-21 23:33 UTC)

<p>Which repository, which pre-programmed model, what kind of difficulty you are experiencing, and where (Slicer or Unity)? Please describe in detail what steps you did, what you expected to happen, and what happened instead.</p>

---

## Post #19 by @Guilherme_Augusto (2024-10-22 02:33 UTC)

<p>I am using the repository at <a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" class="inline-onebox" rel="noopener nofollow ugc">GitHub - BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning: GitHub repository for the IJCARS paper: "Real-Time open-source integration between Microsoft HoloLens 2 and 3D Slicer"</a>, specifically the pre-programmed spine model. My difficulty lies in trying to apply the connection and clipping plane to a different anatomical model while using HoloLens. I managed to add a new model, specifically <strong>Segmentation 1</strong>, connect it to Slicer, and apply it to the HoloLens, but I am unable to use the functions, such as the clipping plane, with the new model.</p>
<p>As shown in the attached images, I tried deleting the <strong>Spine</strong> model, but every time I press Play, it reappears automatically in the <strong>Models</strong> section, interfering with my attempt to work with the new <strong>Segmentation 1</strong> model. Even though I apply the <strong>Clipping_mat</strong> and set up everything as expected, the Spine model keeps returning, and I can’t use the clipping plane or other intended functions with the new model.</p>
<p>Could you please provide guidance on how to stop the <strong>Spine</strong> model from automatically reappearing and how to properly configure the system so that I can work with other models and use the functionalities like the clipping plane?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c4edc5c77073c944665bd7a80686c064cb9aa72.png" data-download-href="/uploads/short-url/daASULF0rz4XPmFpZzrAgh6dtK2.png?dl=1" title="Screenshot 2024-10-21 at 23.29.54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c4edc5c77073c944665bd7a80686c064cb9aa72_2_523x500.png" alt="Screenshot 2024-10-21 at 23.29.54" data-base62-sha1="daASULF0rz4XPmFpZzrAgh6dtK2" width="523" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c4edc5c77073c944665bd7a80686c064cb9aa72_2_523x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c4edc5c77073c944665bd7a80686c064cb9aa72_2_784x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c4edc5c77073c944665bd7a80686c064cb9aa72.png 2x" data-dominant-color="313131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-21 at 23.29.54</span><span class="informations">984×940 74.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae07d68c03dce46dd2797e42447cac735634cf5a.png" data-download-href="/uploads/short-url/oPxS7fAa7PGzEu1d5kO2B2gqzUe.png?dl=1" title="Screenshot 2024-10-21 at 23.30.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae07d68c03dce46dd2797e42447cac735634cf5a_2_523x500.png" alt="Screenshot 2024-10-21 at 23.30.06" data-base62-sha1="oPxS7fAa7PGzEu1d5kO2B2gqzUe" width="523" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae07d68c03dce46dd2797e42447cac735634cf5a_2_523x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae07d68c03dce46dd2797e42447cac735634cf5a_2_784x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae07d68c03dce46dd2797e42447cac735634cf5a.png 2x" data-dominant-color="303030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-21 at 23.30.06</span><span class="informations">984×940 78.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b1e59b0bdcb88d16aa4bd625c0fa0424174996f.png" data-download-href="/uploads/short-url/m8f23OHASk0xXn4pDTFVH2g0ktp.png?dl=1" title="Screenshot 2024-10-21 at 23.30.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1e59b0bdcb88d16aa4bd625c0fa0424174996f_2_365x500.png" alt="Screenshot 2024-10-21 at 23.30.27" data-base62-sha1="m8f23OHASk0xXn4pDTFVH2g0ktp" width="365" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1e59b0bdcb88d16aa4bd625c0fa0424174996f_2_365x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1e59b0bdcb88d16aa4bd625c0fa0424174996f_2_547x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1e59b0bdcb88d16aa4bd625c0fa0424174996f_2_730x1000.png 2x" data-dominant-color="313131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-21 at 23.30.27</span><span class="informations">780×1068 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #20 by @lassoan (2024-10-22 02:50 UTC)

<p>Others (maybe <a class="mention" href="/u/aliciapose">@AliciaPose</a>) might be able to comment on how to use Unity.</p>
<p>My advice would be to render to the HoloLens directly from Slicer, using Slicer’s VirtualReality extension. It just simplifies everything and you can do so much more.</p>

---

## Post #21 by @Guilherme_Augusto (2024-10-23 09:52 UTC)

<p>Thank you for the suggestion! I’ve actually tried using the VirtualReality extension in Slicer, but I haven’t been able to achieve some key functionalities I need, like performing the examination simultaneously, placing markups in Markup, and especially using the clipping plane functions. If you’re able to help me with any of these, I’d be extremely grateful</p>

---

## Post #22 by @lassoan (2024-10-23 19:18 UTC)

<p>Adjusting markups and clipping planes are the same function (clipping ROI, planes, etc. are all markups). Manipulating markups in virtual/augmented reality is on our todo list, but I’m not sure when we’ll get to it (not within weeks, but maybe in months). Would you be interested in helping with implementing this feature? (it needs to be implemented mostly in C++)</p>

---

## Post #23 by @Guilherme_Augusto (2024-10-23 21:28 UTC)

<p>Thank you for the opportunity! I am a doctor and an enthusiast in segmentation and technology, having worked with these tools for the past 10 years. While I have the knowledge for such development, it would be difficult for me to assist at a high level with C++ specifically. However, I am still interested and willing to contribute where possible.</p>

---
