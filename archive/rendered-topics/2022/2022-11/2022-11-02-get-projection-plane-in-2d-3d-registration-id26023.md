---
topic_id: 26023
title: "Get Projection Plane In 2D 3D Registration"
date: 2022-11-02
url: https://discourse.slicer.org/t/26023
---

# Get projection plane in 2D-3D Registration

**Topic ID**: 26023
**Date**: 2022-11-02
**URL**: https://discourse.slicer.org/t/get-projection-plane-in-2d-3d-registration/26023

---

## Post #1 by @domP (2022-11-02 08:17 UTC)

<p>Hello everybody,<br>
I’m trying to register a CT volume with a 2D XA (fluoroscopic image). My issue is to find the projection plane from CT volume that matches with the XA one using DICOM information of fluoroscopic image like SID, SOD, Primary and Secondary Angles etc.<br>
I have found “DRR generation” module that computes a projection of the CT volume but it requires some parameters that I can’t reach from DICOM header such as the projection plane ones.<br>
Is there a way to get these informations?</p>
<p>P.S.: I’m only interested to get the projection plane. The projection image could me help to check the correct matching.</p>

---

## Post #2 by @gcsharp (2022-11-03 14:40 UTC)

<p>Hi domP.  In general, it is not easy to recover these parameters if they are not recorded.  You might need to do 2D-3D registration.  But before doing that, you should first constrain the results:</p>
<ol>
<li>Review the DICOM header of the XA, including private tags, to see what information is available.  You might be able to get gantry angle.</li>
<li>Review the user/service manual of the device.  You may be able to get SID.</li>
</ol>

---

## Post #3 by @lassoan (2022-11-03 15:29 UTC)

<p>On modern C-arms SID, SOD, and anatomical angles are all available in standard DICOM tags. However, these are mostly just approximate values. The reported angles may have a few degrees error, SOD assumes that the object is at a specific distance above the table in the center, mechanical deformation of the arm is not taken into account, most clinical C-arms are not isocentric, etc.</p>
<p>Therefore, all the values that you can find in the DICOM header are only usable as initial guess for 2D/3D registration. Accurate 2D/3D registration based on visible anatomy is challenging for many reasons, mainly due to the fact that accuracy and robustness greatly depends on geometry and appearance of the anatomical region on X-ray images.</p>
<p>To overcome this, many research groups experimented with adding special radio-opaque marker arrangement in the C-arm’s field of view, adding external optical tracking, inside-out tracking (using camera or surface scanner), but each of these solutions has serious limitations, so they are not generally applicable and have not become widely used. If you plan to explore these options then you also need to keep in mind that you are competing with quick cone-beam 3D reconstruction that is widely available on all modern clinical C-arms, which allows much easier registration.</p>

---

## Post #4 by @gcsharp (2022-11-03 15:34 UTC)

<p>Yes, it would be good to see those header values.  Also, I don’t know what is meant by “projection plane.”  What parameterization do you seek?</p>

---

## Post #5 by @domP (2022-11-03 15:39 UTC)

<p>Hi Andras,<br>
in what way could I use DICOM informations for an initial guess for registration?<br>
I have the gantry angles (Primary and Secondary Angles), SID and SOD.</p>

---

## Post #6 by @lassoan (2022-11-03 15:45 UTC)

<p>The goal of 2D/3D registration is to determine all the unknown projection parameters. You would need to have a good initial guess for all these parameters and then use a non-linear optimizer to tune them so that you get better match between the DRR and the actual fluoro image. SID, SOD, and primare and secondary angles help in having a better estimation for some of the projection parameters. Plastimatch documentation pages such as <a href="http://plastimatch.org/proj_geometry_15.html">this</a> may help in getting a better understanding of the projection geometry and what parametrization you can use.</p>

---

## Post #7 by @domP (2022-11-03 16:29 UTC)

<p>Thanks for the reply. However, I can’t understand in which way I can use these parameters.<br>
For example, in DRR generation module, I have to set these parameters:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3090ea4e480cb981671ff6e219af1c6d3365c9f8.png" alt="Screenshot (1)" data-base62-sha1="6VDoGfrSCVIFGSWifnipT0BJOFq" width="627" height="171"></p>
<p>What are “View-Up vector” and “Normal Vector” ? In what way I can set them? Are they have any relationship with Primary and Secondary angles?</p>

---

## Post #8 by @lassoan (2022-11-03 16:38 UTC)

<p>Specifying view up and normal vector is a common way to parametrize camera orientation in computer graphics. Primary and secondary angles is a different parametrization of camera orientation - see the DICOM standard for exact definition.</p>

---

## Post #9 by @drvarunagarwal (2024-11-03 11:02 UTC)

<aside class="quote quote-modified" data-post="1" data-topic="39995">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drvarunagarwal/48/8914_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/programmer-wanted-for-registration-workflow-development/39995">Programmer wanted for Registration workflow Development</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hello all, 
We are looking for a freelancer or dedicated programmer for our slicer based navigation system development. 
Currently we require to implement the following task: 
The task: 
We need to implement a new Registration workflow in 3D Slicer. The registration workflow should register a Pre Op CT to 2 IntraOp Fluro X-Rays. 

  <a href="https://www.youtube.com/watch?v=I_XjU1t-RrQ" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    [CT/C-arm Image Registration (New Version)]
  </a>


User journey: 
• Ask user to take 2 fluro shots. 1 in AP and 1 in oblique (or lateral, whichever suits to desig…
  </blockquote>
</aside>


---
