# Set Up Slicer Virtual reality environment

**Topic ID**: 4689
**Date**: 2018-11-08
**URL**: https://discourse.slicer.org/t/set-up-slicer-virtual-reality-environment/4689

---

## Post #1 by @M_pavi (2018-11-08 19:25 UTC)

<p>I already installed Slicer VR extension and connected HTC VIVE. This works both 4.9 and 4.10. Moreover, I want to do many changes set up VR boundaries like a room.  Disable moving of the model and some advanced functionality ( to add volume, to do some visualization and manipulating ). So fat I used slicer python kernel<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0b32ee78a7976c7195821f7a7307fb8bbf82490.png" data-download-href="/uploads/short-url/ruHzv5Y6zjescdHosYkiQhk5u0w.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0b32ee78a7976c7195821f7a7307fb8bbf82490.png" alt="image" data-base62-sha1="ruHzv5Y6zjescdHosYkiQhk5u0w" width="690" height="179" data-dominant-color="F6F6FB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">898×234 3.66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>  to do some small changes.<br>
But when it comes to adding multiple features in VR environment how to do this?<br>
Is there any platform to develop it?<br>
The jupyter notebook can support VR development ?</p>

---

## Post #2 by @lassoan (2018-11-08 21:14 UTC)

<aside class="quote no-group" data-username="M_pavi" data-post="1" data-topic="4689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/54ee81/48.png" class="avatar"> M_pavi:</div>
<blockquote>
<p>But when it comes to adding multiple features in VR environment how to do this?<br>
Is there any platform to develop it?</p>
</blockquote>
</aside>
<p>SlicerVirtualReality extension is open-source. Source code is available <a href="https://github.com/KitwareMedical/SlicerVirtualReality">here</a>. Pull requests with fixes and improvements are welcome.</p>
<aside class="quote no-group" data-username="M_pavi" data-post="1" data-topic="4689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/54ee81/48.png" class="avatar"> M_pavi:</div>
<blockquote>
<p>The jupyter notebook can support VR development ?</p>
</blockquote>
</aside>
<p>Yes, you can run scripts in Jupyter notebook that set up VR views, etc. You can also customize behavior by <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial">creating a Python scripted module</a>.</p>

---

## Post #3 by @cpinter (2018-11-09 14:05 UTC)

<aside class="quote no-group" data-username="M_pavi" data-post="1" data-topic="4689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/54ee81/48.png" class="avatar"> M_pavi:</div>
<blockquote>
<p>Disable moving of the model</p>
</blockquote>
</aside>
<p>You can set the Selectable flag on the nodes you don’t want to be movable. You can do it from python or in the Data module by right-clicking the nodes.</p>

---

## Post #4 by @lassoan (2018-11-09 17:42 UTC)

<p>I’ve updated the <a href="https://github.com/KitwareMedical/SlicerVirtualReality#how-to-use-controllers">extension’s documentation</a>. I think all features that have been implemented are now described.</p>

---

## Post #5 by @Nicholas.jacobson (2018-11-27 19:54 UTC)

<p>Are there some basic recommendations for a graphics cards to run VR. We are getting a lot of lag in our VR movements.</p>

---

## Post #6 by @M_pavi (2018-11-27 19:57 UTC)

<p>for me I am using GeForce GTX 1080 Ti FTW3 Gaming 11G - slightly expensive was around CAD 2000.</p>

---

## Post #7 by @cpinter (2018-11-28 03:52 UTC)

<aside class="quote no-group" data-username="Nicholas.jacobson" data-post="5" data-topic="4689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar"> Nicholas.jacobson:</div>
<blockquote>
<p>Are there some basic recommendations</p>
</blockquote>
</aside>
<p>It highly depends on what you want to do. If you want to display a few not too complex models, then you don’t need anything fancy. Even if you render a lower resolution MR volume, a 1060 will do. However once you start volume rendering CTs, then you’ll need a high end GPU.</p>
<p>Keep in mind that you can reduce the lag with changing settings. There are FPS and motion sensitivity controls in the VR module to adjust quality vs speed (click the wrench icon next to the VR headset icon in the toolbar to get there). There is an “optimize scene for VR” button on the toolbar as well (looks like a magic wand) that helps with this. Also helps to change the desktop Slicer layout to one that does not have 3D view. You can also play with volume rendering quality settings directly.</p>

---

## Post #8 by @lassoan (2018-11-28 05:36 UTC)

<aside class="quote no-group" data-username="Nicholas.jacobson" data-post="5" data-topic="4689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar"> Nicholas.jacobson:</div>
<blockquote>
<p>We are getting a lot of lag in our VR movements.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/nicholas.jacobson">@Nicholas.jacobson</a> Make sure you choose Rendering: “VTK GPU Ray Casting” in Volume rendering module.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> Could you add switching to GPU volume rendering method to “Optimize scene for VR”?</p>

---

## Post #9 by @cpinter (2018-11-28 16:04 UTC)

<p>I’m implementing the change you suggested. It seems to me that the best way to implement it is to pass the volume rendering logic to the VR logic in order to be able to do this. Let me know if you have a better idea.</p>
<p>I also added this question to the SlicerVR page’s FAQ section.</p>

---

## Post #10 by @lassoan (2018-11-28 17:34 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="9" data-topic="4689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>pass the volume rendering logic to the VR logic</p>
</blockquote>
</aside>
<p>I think it is the right thing to do.</p>
<p>We should probably add to the extension documentation the list of optimization steps performed.</p>

---

## Post #11 by @cpinter (2018-11-28 18:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="4689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We should probably add to the extension documentation the list of optimization steps performed</p>
</blockquote>
</aside>
<p>I did that but then decided to remove it to keep it simple. I was also thinking about pointing to the dox, where in the header the steps are explained. But whatever you think the best…</p>

---

## Post #12 by @lassoan (2018-11-28 23:33 UTC)

<p>I agree that it could be too complex to show on the GUI, I just meant to add it to the documentation (<a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/README.md" rel="nofollow noopener">https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/README.md</a>).</p>

---

## Post #13 by @cpinter (2018-11-28 23:51 UTC)

<p>Yes that’s how I understood.</p>

---

## Post #14 by @lassoan (2018-11-29 05:19 UTC)

<p>We can also link to the appropriate header file from the FAQ section for the list of exact steps (so that we don’t need to duplicate information).</p>

---

## Post #15 by @cpinter (2018-11-29 14:53 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="11" data-topic="4689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>pointing to the dox</p>
</blockquote>
</aside>
<p>Again, that’s what I meant <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I’ll do this then!</p>

---

## Post #16 by @avimo1 (2024-04-18 13:15 UTC)

<p>Hi,<br>
Was looking at slicervirtualreality for a project, please refer me to a tutorial of implementing the app in an eSy way.</p>

---
