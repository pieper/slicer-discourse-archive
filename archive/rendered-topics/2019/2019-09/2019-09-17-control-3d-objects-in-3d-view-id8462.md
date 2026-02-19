---
topic_id: 8462
title: "Control 3D Objects In 3D View"
date: 2019-09-17
url: https://discourse.slicer.org/t/8462
---

# Control 3D objects in 3D view

**Topic ID**: 8462
**Date**: 2019-09-17
**URL**: https://discourse.slicer.org/t/control-3d-objects-in-3d-view/8462

---

## Post #1 by @mikecsu (2019-09-17 07:42 UTC)

<p>Operating system:win10<br>
Slicer version:slicer 4.10.0 / 4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi, everyone.  Recently i have got an idea about control 3D objects to make them rotate, translate, scale in 3D view.</p>
<p>My first move is to develop a function which allows me to select an object. For example, the yellow tumor in the pic.</p>
<p>And then i can move the tumor out of the green liver and then do the rotation … to the tumor,<br>
but the liver needs to keep still.</p>
<p>(I did some experiments:</p>
<p>Since in slicer 3D views , 3D objects(or 3D segments) move  is because of the use the camera, but if we use camera, then all the visible segments are going to move together, which is not what i expect.</p>
<p>Therefore, i created another 3D view window and i tried to seperate them to ensure there is only one segment in both windows, but i failed to do it because these two windows are synchronized.  Is there anyway to make these two windows not synchronized ?)</p>
<p>Is my idea feasible in Slicer ? (Cause these functions ,such as rotation, translation, scaling , they are usually achieved in some modeling softwares.)</p>
<p>Any help would be appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e5d5678ee43d6ff25e49ec343ffc6ee4cd100c4.jpeg" data-download-href="/uploads/short-url/mAXpLB4QB7PPUFBg9FXKDLfpRNa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e5d5678ee43d6ff25e49ec343ffc6ee4cd100c4_2_690x347.jpeg" alt="image" data-base62-sha1="mAXpLB4QB7PPUFBg9FXKDLfpRNa" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e5d5678ee43d6ff25e49ec343ffc6ee4cd100c4_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e5d5678ee43d6ff25e49ec343ffc6ee4cd100c4_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e5d5678ee43d6ff25e49ec343ffc6ee4cd100c4_2_1380x694.jpeg 2x" data-dominant-color="9FA6C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2497×1258 353 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Juicy (2019-09-17 08:01 UTC)

<p>Your version of slicer looks quite old? Can you use the transformation module to move the tumor out of the liver?</p>
<p>You may find some of the tips in this <a href="https://www.youtube.com/watch?v=Uht6Fwtr9hE" rel="nofollow noopener">Video</a> helpful for using the transformation module. From about 5:30 she covers the use of the transformation module to move things around.</p>
<p>I see that both of the segments are under the same segmentation node. If you want to move just the yellow tumor with the transformation module then I think that you will have to move the yellow tumor segment to a separate segmentation node. You can use the copy/move segment part of the segmentation module to move segments to a new node (I can see it in your picture above).</p>

---

## Post #3 by @mikecsu (2019-09-18 07:59 UTC)

<p>Really thanks for the reply.</p>
<p>I can use the transformation module to do the things i want, but the whole operation seems really time-consuming  and inefficient.</p>

---

## Post #4 by @Juicy (2019-09-18 08:09 UTC)

<p>Yes, it seems strange at first and it takes some getting your head around. There are some little tricks to make it work well. You quickly get used to it though. I have found there are some really good advantages to the way the transform module works compared to other 3D CAD programs. It is really handy having direct access to the linear transform matrix and it can be really good being able to bring groups of objects in and out of the transform and harden or not harden them etc.</p>

---

## Post #5 by @lassoan (2019-09-18 11:28 UTC)

<aside class="quote no-group" data-username="mikecsu" data-post="3" data-topic="8462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/3da27b/48.png" class="avatar"> mikecsu:</div>
<blockquote>
<p>I can use the transformation module to do the things i want, but the whole operation seems really time-consuming and inefficient.</p>
</blockquote>
</aside>
<p>Slicer is extremely flexible, there are always several ways to do things, depending on what your constraints are. We were just trying to guess what would work for you but if you can tell more about what you would like to achieve and why do you find the proposed workflow inefficient the we may be able to give more specific advice.</p>
<p>For example, if you want freely grab and move/translate around objects then I would recommend to do it in virtual reality (you can get headset and controllers for a few hundred dollars) - it is much faster than working on a 2D screen with mouse and keyboard. See this demo:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="VzVjvnKuBAE" data-video-title="3D Slicer reconstruction of fragmented bones in virtual reality" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=VzVjvnKuBAE" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/VzVjvnKuBAE/maxresdefault.jpg" title="3D Slicer reconstruction of fragmented bones in virtual reality" width="" height="">
  </a>
</div>


---

## Post #6 by @mikecsu (2019-09-19 02:35 UTC)

<p>Really thanks for the reply.  What i want to achieve is the video demo that  you recommend to me above.</p>
<p>I want to achieve those functions displayed in that video, including grab, move,etc.  But i want to do it in 3D view with mouse and keyboard .</p>
<p>Could you tell me why it is  hard or inconvenient  to achieve these functions in 3D view?</p>
<p>I tried to find the reasons,then i found this in the source code. but still not sure i totally understand it.</p>
<p>Why is it expensive ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2a1bd5720779c9f33df8cc7cb2e83a1969415b4.png" data-download-href="/uploads/short-url/yCq4y1h7pa21pwouRAjroQWmrGI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2a1bd5720779c9f33df8cc7cb2e83a1969415b4_2_690x268.png" alt="image" data-base62-sha1="yCq4y1h7pa21pwouRAjroQWmrGI" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2a1bd5720779c9f33df8cc7cb2e83a1969415b4_2_690x268.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2a1bd5720779c9f33df8cc7cb2e83a1969415b4_2_1035x402.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2a1bd5720779c9f33df8cc7cb2e83a1969415b4.png 2x" data-dominant-color="F5F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1178×458 77.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is it possible to obtain the accurate coordinates (x,y,z)  of cursor in 3D views ?</p>

---

## Post #7 by @lassoan (2019-09-19 03:58 UTC)

<aside class="quote no-group" data-username="mikecsu" data-post="6" data-topic="8462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/3da27b/48.png" class="avatar"> mikecsu:</div>
<blockquote>
<p>Could you tell me why it is hard or inconvenient to achieve these functions in 3D view?</p>
</blockquote>
</aside>
<p>Because a mouse has only 2 degrees of freedom (up/down, left/right) and a virtual reality controller has 6 degrees of freedom (translation and rotation around 3 axes) and we typically use two of these controllers.</p>
<p>Setting position/orientation accurately using a mouse is so tedious that we almost never do it but use image intensity, landmark, or surface matching based registrations instead. Registration methods are usually much more accurate and faster than manual visual alignment.</p>
<aside class="quote no-group" data-username="mikecsu" data-post="6" data-topic="8462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/3da27b/48.png" class="avatar"> mikecsu:</div>
<blockquote>
<p>I tried to find the reasons,then i found this in the source code. but still not sure i totally understand it. Why is it expensive ?</p>
</blockquote>
</aside>
<p>To determine what is displayed at the current mouse position is a computationally expensive operation because a model may consists of hundreds of thousands of triangles that you need to check if intersect with the view ray. There are various tricks to make this fast, but it is not a simple operation.</p>
<p>We plan to improve model picking for virtual reality and as a side effect, desktop/mouse based picking may be improved as well - probably within a year you will be able to select a model by clicking on it. Still, translation/rotation by using mouse would work essentially the same way as now when you use the transform widget - very cumbersome compared to direct grabbing and moving with 6-DOF controllers.</p>
<p>If you can give information about what is the high-level goal you would like to achieve (what anatomy, disease, treatment method, etc.) then we can give more specific advice.</p>

---

## Post #8 by @mikecsu (2019-09-19 10:08 UTC)

<p>These advice are really helpful.  Thanks again.</p>
<p>For now , i do not have a specific goal to achieve.   I admit that we can use the HTC Vive controller (the VR equipment that i am using) to grab 3D objects in VR view and then the VR view can synchronize to 3D view in slicer, which is amazing.</p>
<p>But there is a scene that i am considering . If there is a doctor who wants to show some visualization data to his or her patient. He or she can only do operations in 3D view and these operations can synchronize to VR view (put a VR headset on the patient’s head).</p>
<p>In this scene, a doctor can easily show the visualization data to his or her patient and uses mouse instead of the controller, and the patient just need to focus on what he or she can see in VR view and can understand each step/operation that the doctor did.</p>
<p>Based on this scene, i came up with the question i posted.</p>

---

## Post #9 by @lassoan (2019-09-19 12:25 UTC)

<p>Patient education and collaborative review/planning are indeed important use cases for virtual reality and it is already available in Slicer (by loading the same scene on two computers and sharing a few transforms between them using OpenIGTLink):</p>
<div class="lazyYT" data-youtube-id="rG9ST6xv6vg" data-youtube-title="Collaborative surgery planning in virtual reality" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #10 by @mikecsu (2019-09-20 02:55 UTC)

<p>This video is great.</p>
<p>But personally, i do not think doctors are willing to put on a headset to do a demostration to their patients.</p>
<p>The headset is kind of heavy and not convenient to use when they use the controller to control 3D objects, while the mouse is usually more accurate than the controller and more easier to manipulate.</p>

---

## Post #11 by @Amine (2019-09-20 04:44 UTC)

<p>I guess the best way of using just a mouse to do interactive transforms as you say without changing the way slicer work (in the future) is to make a transform for each selected node on the 3d viewer then change its matrix without hardening the transform as you pull some axises on the 3d view as you would do with blender or other modeling software.<br>
The caveat though is that this method (even in blender where it is already available) is not very efficient in explaining to a patient interactively and you will be better off using a VR controller (even without a headset) to freely move your models or some other kind of stereotactic device.</p>

---

## Post #12 by @lassoan (2019-09-21 14:38 UTC)

<aside class="quote no-group" data-username="mikecsu" data-post="10" data-topic="8462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/3da27b/48.png" class="avatar"> mikecsu:</div>
<blockquote>
<p>But personally, i do not think doctors are willing to put on a headset to do a demostration to their patients.</p>
</blockquote>
</aside>
<p>The idea is that both patients and doctors would be in the virtual world. If the doctor is not willing to put on a headset then just using the VR controllers could be an option, as <a class="mention" href="/u/amine">@Amine</a> suggests. You can also use scene views to save pre-configured views and switch between those (it may be then enough to move/rotate the camera around). If eye contact with the patient is important and visualization of static models is enough then you may export segmentation to obj model file and view them on an augmented reality headset (converting and uploading models takes some effort and I’m not sure if multi-user model viewer is readily available).</p>

---
