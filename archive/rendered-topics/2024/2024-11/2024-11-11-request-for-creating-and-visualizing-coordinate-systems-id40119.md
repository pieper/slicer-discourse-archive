---
topic_id: 40119
title: "Request For Creating And Visualizing Coordinate Systems"
date: 2024-11-11
url: https://discourse.slicer.org/t/40119
---

# Request for Creating and Visualizing Coordinate Systems

**Topic ID**: 40119
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/request-for-creating-and-visualizing-coordinate-systems/40119

---

## Post #1 by @evaherbst (2024-11-11 11:32 UTC)

<p>Hello,</p>
<p>Would it be possible to introduce rendering for planes (for use in showing local coordinate systems) that looks like the interactive handles for planes, but does NOT enable interaction to prevent accidental changes in the coordinate system?<br>
for example like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73fb3312ae6ec30f00741106a9068d5f863f96f9.png" data-download-href="/uploads/short-url/gy16inJSQOLbtGmp36PQ3vTYUrv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73fb3312ae6ec30f00741106a9068d5f863f96f9.png" alt="image" data-base62-sha1="gy16inJSQOLbtGmp36PQ3vTYUrv" width="418" height="499" data-dominant-color="848564"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">726×868 31.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is also another feature that would be very helpful for the creation of coordinate systems. I know this is possible writing a custom Python but I think it might be a useful feature. The feature is as follows:</p>
<p>-in Autodesk Maya, you can make objects that are coordinate system objects. you can then reorient them by “snapping” the axes to points you have placed in the scene, for example aligning the X axis to a specific anatomical landmark. This would be quite useful for easily generating anatomical coordinate systems for models.</p>

---

## Post #2 by @pieper (2024-11-11 16:26 UTC)

<p>For the first question you can go into the properties of the plane and lock the control point, while leaving the interaction mode active.</p>
<p>The second idea sounds great and could be implemented something like the the way curves can be snapped to the surface of models.  It would be a medium sized effort and would be good for someone who wants to learn more about the internals.</p>

---

## Post #3 by @evaherbst (2024-11-11 17:25 UTC)

<p>Thanks so much <a class="mention" href="/u/pieper">@pieper</a> for the quick reply.</p>
<p>For the first answer, this still enables rotation though, right?<br>
I wanted to see the XYZ axes without any change of interaction. If that is not a possibility though then I will just be careful.</p>
<p>For point 2, yes exactly like that snapping. I will keep it in mind for future students, would also love to try it myself but at the moment none in my time including me can set aside the time. Or maybe for a future project week, I hope I can attend one year.<br>
If you know anyone else such as a student interested in implementing it that would be great and I can share some more info about the Maya feature.</p>
<p>Thanks again!<br>
Eva</p>

---

## Post #4 by @pieper (2024-11-11 17:43 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="3" data-topic="40119">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>For the first answer, this still enables rotation though, right?</p>
</blockquote>
</aside>
<p>If you turn of the rotation and scale handles then you get the axes, and maybe that’s enough?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2fd1c70219524c8c7a13c794c15e1c6bfa0ff10.png" data-download-href="/uploads/short-url/nfRDzi8CgFrE7iOMu3Ldfr0vLH2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2fd1c70219524c8c7a13c794c15e1c6bfa0ff10_2_689x188.png" alt="image" data-base62-sha1="nfRDzi8CgFrE7iOMu3Ldfr0vLH2" width="689" height="188" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2fd1c70219524c8c7a13c794c15e1c6bfa0ff10_2_689x188.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2fd1c70219524c8c7a13c794c15e1c6bfa0ff10_2_1033x282.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2fd1c70219524c8c7a13c794c15e1c6bfa0ff10.png 2x" data-dominant-color="C0C3DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1194×326 38.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regarding the snapping it may also be useful for robotics so I hope someone will find some time and enthusiasm to work on it.</p>
<p>As for Project Week, yes, you would be most welcome.  The page is up and the dates and location are set and the organizing calls will start before too long.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW42_2025_GranCanaria/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/" target="_blank" rel="noopener">Welcome to the web page for the 42nd Project Week!</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @evaherbst (2024-11-12 11:27 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> !<br>
I guess for now that is enough - I just worry that a student could accidentally translate the coordinate system, but I don’t think there is a high chance of it so I will leave it for now.</p>
<p>Yes I can see it translating to robotics too. I will keep my eye out for anyone looking for a project.</p>
<p>RE Project Week, I would love to go but don’t think I can make it in person and I see this time there is no remote option.</p>

---
