---
topic_id: 13254
title: "How To Create An Open Surface Constrained By Markup Points A"
date: 2020-08-31
url: https://discourse.slicer.org/t/13254
---

# How to create an open surface constrained by markup points，and split the current segment by this surface?

**Topic ID**: 13254
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/how-to-create-an-open-surface-constrained-by-markup-points-and-split-the-current-segment-by-this-surface/13254

---

## Post #1 by @Aitekk (2020-08-31 15:03 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.11<br>
Expected behavior:To creat a surface constrained by markup points, and split a segment by this surface. In addition, if the surface can be created and adjusted in 3D view, it will be more better for annotation work. In order to show the expected operation vividly, I made a demo gif based on Mimics 19.0. The demo takes trachea annotation as an example, but actually the annotation of vessels is more complicated. I will be grateful for your suggestions.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99e2e40c153d429a6bd0ec790dc22badf3cff682.gif" data-download-href="/uploads/short-url/lXlabyiRnn8lR4hRtWfCr6X0iHw.gif?dl=1" title="cut_segmentation_demo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99e2e40c153d429a6bd0ec790dc22badf3cff682_2_690x388.gif" alt="cut_segmentation_demo" data-base62-sha1="lXlabyiRnn8lR4hRtWfCr6X0iHw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99e2e40c153d429a6bd0ec790dc22badf3cff682_2_690x388.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99e2e40c153d429a6bd0ec790dc22badf3cff682.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99e2e40c153d429a6bd0ec790dc22badf3cff682.gif 2x"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cut_segmentation_demo</span><span class="informations">853×480 3.97 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Actual behavior: In fact, I tried Surface Cut extension to complete above operation, but found it difficult to add or move markup points in 3D view, which often deviated from the selected segments. Moreover, Surface Cut effect is to create a closed bubble to split the segment, which requires that the bubble can not contain very complex polygons, and needs a lot of markup points.</p>

---

## Post #2 by @lassoan (2020-08-31 15:30 UTC)

<p>The module that does this is called <code>Dynamic modeler</code>. There are many modes and options, if you need any help figuring out how to use it then let us know.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F6fNMQTxD-4" data-video-title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F6fNMQTxD-4/maxresdefault.jpg" title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" width="" height="">
  </a>
</div>


---

## Post #4 by @Aitekk (2020-09-01 03:35 UTC)

<p>Thanks for your help and your patience. I tried Dynamic modeler module, but found that I couldn’t get a desired surface, which is not suitable for the annotation problem I was facing. In fact, I want to segment the existing lung segments using a surface and to obtain different pulmonary segments, as shown in this gif. Due to the anatomical requirements of pulmonary segment, the surface needs to be constrained by the direction of the pulmonary vessels. Thus, it is necessary to set some markup points according to the vessels to build and adjust the surface. More detailed operation or other effective ways will be helpful to me.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87f745754eece1913b9ce7963f9ad028ccc9eda8.gif" alt="PulmonarySegment_demo" data-base62-sha1="joOeyQPgfQJ4iHgoi4usUsUc680" width="285" height="160"></p>

---

## Post #5 by @lassoan (2020-09-01 04:16 UTC)

<p>We have implemented 3D open surface editing that is very similar to the your animation above, but it will not be released for a few more months (until related papers get published).</p>
<p>However, probably you can do what you need using closed surface. Indeed, 3D control point positioning was not working well in recent Slicer Preview Releases, as we mostly just used 3D views as quick overview and not to move points. The issue was that control points were snapped to visible surfaces by default, so the control point and generated surface iteratively crawled towards the camera as the point position was adjusted.</p>
<p>I’ve changed the behavior now so that now control points are moved in the camera normal plane. Please download Slicer Preview Release tomorrow noon (or later) and in that version you should be able to position the points in 3D views as you expect.</p>
<p>Let us know how it all works. There are many options for improving various aspects as needed.</p>

---

## Post #6 by @Aitekk (2020-09-01 05:57 UTC)

<p>That’s great. The 3D open surface editing is very expected by annotation workers. If I use the version that will be released tomorrow, will the Surface Cut extension work better?</p>

---

## Post #7 by @lassoan (2020-09-01 23:44 UTC)

<p>Surface cut effect improvement is already available in the latest Slicer Preview Release.</p>
<p>There are other groups working on splitting organs to segments based on vasculature in 3D Slicer, such as this liver resection project:</p>
<aside class="quote quote-modified" data-post="1" data-topic="12467">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/alive-research-project/12467">ALive research project</a> <a class="badge-category__wrapper " href="/c/announcements/jobs/22"><span data-category-id="22" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #ED207B;" data-parent-category-id="7" data-drop-close="true" class="badge-category --has-parent" title="This category is primary for posting jobs or offering expertise related to using or developing 3D Slicer and its underlying open-source libraries. We may also accept other medical imaging related job postings if it is described how it is relevant for Slicer users or developers."><span class="badge-category__name">Jobs</span></span></a>
  </div>
  <blockquote>
    ALive Project 
[alive_logo] 
<a href="https://alive-research.no" rel="noopener nofollow ugc">https://alive-research.no</a> 
Dear Slicer community, I would like to call your attention to the ALive project that will start in Autumn 2020. In ALive, we are planning to research new methods for computation and visualization of liver resections. We believe that research software, like 3D Slicer, is an incredible vehicle to increase the impact of our research and its reach to the scientific community and society. In this line, we plan to structure our research around a …
  </blockquote>
</aside>

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> can you give us an update about the status of your curved planar cutting widget?</p>

---

## Post #8 by @Aitekk (2020-09-02 03:18 UTC)

<p>Thanks very much for your help. I tried the latest Slicer Preview Release, which significantly improved the operation of the Surface Cut extension.</p>

---

## Post #9 by @klarlund (2020-09-02 08:50 UTC)

<p>I have used T-splines (Edit “Form”) in 3D Fusion to solve a similar problem after importing structures and landmarks from 3D Slicer. There is a bit of a learning curve for the Fusion T-spline tool, however. The advantage is that one can specify the desired surface with a minimum number of control points. In other cases, lofting along curves in Fusion is easier. Beautiful surfaces result. Here’s the workflow:</p>
<ul>
<li>Export the segmented structures as STL from 3D Slicer. Perhaps make an additional segment with little bit blops for where important control points go. Or make fiducials instead and export to CVS.</li>
<li>Import into 3D Fusion.  Also, fiducial points can be read via a Fusion 360 script that adds them to a 3D sketch. (I don’t remember the details.)</li>
<li>Construct surface using Fusion tools. The Fusion Section Analysis allows viewing cross sections through meshes. With T-splines, control points can be directly placed on imported meshes such as those stemming from bit blops. In any case, a BREP surface eventually  results.</li>
<li>Thicken surface into a BREP body in Fusion, say by .5mm, and export this body as STL.</li>
<li>Import the surface body into 3D Slicer, but remember to click Options to reveal a button that imports in RAS coordinates.</li>
<li>The surface body, now a model in Slicer, can be converted to a segment, so that it becomes a tool in Boolean operations for complicated shape 3D cuts.</li>
</ul>
<p>This workflow could be supported by scripts at both ends. I never got around to writing a 3D slicer/Fusion 360 pair for automating all this.</p>

---

## Post #10 by @Aitekk (2020-09-02 09:08 UTC)

<p>This is an interesting method that I will try. Thanks for your detailed workflow.</p>

---

## Post #11 by @klarlund (2020-09-02 10:28 UTC)

<p>Correction: I meant “Fusion 360” as the suggested 3D surface editing tool (others such as Blender are also possible).</p>

---
