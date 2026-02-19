---
topic_id: 6159
title: "4D Ct Animation"
date: 2019-03-15
url: https://discourse.slicer.org/t/6159
---

# 4D CT animation

**Topic ID**: 6159
**Date**: 2019-03-15
**URL**: https://discourse.slicer.org/t/4d-ct-animation/6159

---

## Post #1 by @Carlos_Arrieta (2019-03-15 17:35 UTC)

<p>I am trying to create an animation from a 4D CT… What I want to create is a model of a 4D CT where systole and diastole are animated, then export this model to view in hololens/magic leap AR glasses. I am not sure if this can be done using Slicer… Not sure if what i need to do is to create an STL of each cycle then export all of them and somehow use a 3d modeling software to merge them ?</p>

---

## Post #2 by @pieper (2019-03-18 12:20 UTC)

<p>Hi -</p>
<p>For viewing cine CT, I’d suggest using volume rendering and not surface models (STL).  For this, you should be able to load the data as a volume sequence (see <a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/Sequences" rel="nofollow noopener">the sequences extension</a>) and then view it with a headset compatible with the <a href="https://github.com/KitwareMedical/SlicerVirtualReality" rel="nofollow noopener">SlicerVR</a> extension).  You’ll get better visualization and lots of interaction and analysis possibilities that you would never have when exporting an STL.</p>

---

## Post #3 by @lassoan (2019-03-18 13:03 UTC)

<p>I fully agree with Steve. Clinical augmented reality is still in its infancy, there are too many limitations, which make it hard to find applications that make sense and feasible to implement. On the other hand, virtual reality is here, it is very powerful and inexpensive already, and there are already many applications where it makes a difference.</p>
<p>Anyway, if you are determined to go forward with augmented reality and can accept limitations of using surface rendering as visualization (as opposed to volume rendering), then you can use Slicer to do all the processing and use a very simple Unity-based viewer on the HoloLens or MagicLeap to view these surface meshes.</p>
<p>You can create surface mesh (STL, OBJ, …) file from cardiac CT as shown here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="BJoIexIvtGo" data-video-title="Whole heart segmentation from cardiac CT in 10 minutes" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=BJoIexIvtGo" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/BJoIexIvtGo/maxresdefault.jpg" title="Whole heart segmentation from cardiac CT in 10 minutes" width="" height="">
  </a>
</div>

<p>If you just need to visualize displacement due to cardiac motion then it may be enough to segment only a single phase, then use Sequence Registration extension to compute displacement field over the entire cardiac cycle, and apply the transformation sequence to your segmentation to get a full 4D segmentation. If you need higher-fidelity then you need to segment several phases manually (you might reuse initial seeds from one phase, potentially saving a few minutes of work per phase). See more information in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="5214">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/load-multiple-cardiac-phases-for-segmentation-virtual-reality/5214">Load multiple cardiac phases for segmentation/virtual reality</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: windows 10 
Slicer version: 4.10 
Expected behavior: See cine motion of all phases in volume render/segmentation and then virtual reality 
Actual behavior: Not working 
Hello everyone, 
I read the prior discussions about loading multiple volumes. I loaded a dicom file of CT Heart with 10 phases in order to segment them or see them in volume rendering. But after loading the file, all i see is one volume and have used sequences and sequence browser. But I am unable to work any fu…
  </blockquote>
</aside>


---
