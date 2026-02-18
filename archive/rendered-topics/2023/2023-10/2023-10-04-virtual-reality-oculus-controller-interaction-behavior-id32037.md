# Virtual Reality Oculus controller interaction behavior

**Topic ID**: 32037
**Date**: 2023-10-04
**URL**: https://discourse.slicer.org/t/virtual-reality-oculus-controller-interaction-behavior/32037

---

## Post #1 by @ally7113 (2023-10-04 17:49 UTC)

<p>With the help of several posts, I was able to operate the Slicer virtual reality module on my Oculus Quest2 device.<br>
However, I would like to use rotation, zoom in/out, and two-handed gestures like the YouTube below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dbb8379e288f0dadc058715033bdd918ee668d5.jpeg" data-download-href="/uploads/short-url/kdP4itvsBaSKFdTj9rDnL1kDYUJ.jpeg?dl=1" title="화면 캡처 2023-10-04 191007" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dbb8379e288f0dadc058715033bdd918ee668d5_2_690x414.jpeg" alt="화면 캡처 2023-10-04 191007" data-base62-sha1="kdP4itvsBaSKFdTj9rDnL1kDYUJ" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dbb8379e288f0dadc058715033bdd918ee668d5_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dbb8379e288f0dadc058715033bdd918ee668d5_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dbb8379e288f0dadc058715033bdd918ee668d5_2_1380x828.jpeg 2x" data-dominant-color="A8A2AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">화면 캡처 2023-10-04 191007</span><span class="informations">1402×842 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, as of now, I have only been able to implement the function to grab the model.<br>
What should I do to implement functions such as zooming in, zooming out, and rotating the model?<br>
I don’t know if I need to change it in the settings or code it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08d88b4310edc777738ff834f182c929fe84368f.png" data-download-href="/uploads/short-url/1gfLjswDQVbpXhBXoqZndIjMl1d.png?dl=1" title="화면 캡처 2023-10-04 190500" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d88b4310edc777738ff834f182c929fe84368f_2_684x500.png" alt="화면 캡처 2023-10-04 190500" data-base62-sha1="1gfLjswDQVbpXhBXoqZndIjMl1d" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d88b4310edc777738ff834f182c929fe84368f_2_684x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08d88b4310edc777738ff834f182c929fe84368f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08d88b4310edc777738ff834f182c929fe84368f.png 2x" data-dominant-color="3A3D47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">화면 캡처 2023-10-04 190500</span><span class="informations">855×625 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would really appreciate it if you could tell me how.</p>

---

## Post #2 by @cpinter (2023-10-17 09:38 UTC)

<p>Not having an Oculus Quest, I can only tell you what I posted here</p><aside class="quote" data-post="2" data-topic="32183">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-transform-objects-with-a-oculus-quest2-controller-in-virtual-reality-module/32183/2">How to transform objects with a Oculus Quest2 controller in Virtual Reality module</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    People have been reprting this for Oculus Quest 2 for a while, but since I don’t have such a device I cannot test or try to fix this. Does anyone at Kitware have a Quest 2? We have been receiving these reports and I cannot tell them anything. Thank you! 
Also there is this issue, not sure if related
  </blockquote>
</aside>

<p><a class="mention" href="/u/lucasgandel">@LucasGandel</a> <a class="mention" href="/u/jcfr">@jcfr</a> Do you know why Quest 2 interactions do not seem to work? Many users report the same thing. Thank you!</p>

---

## Post #3 by @LucasGandel (2023-10-18 06:08 UTC)

<p>Sorry I missed your post on the thread, feel free to tag me for XR related questions.<br>
I don’t think we have any action file implemented for the Quest2. Using OpenXR and the work-in-progress action file from <a href="https://gitlab.kitware.com/paraview/paraview/-/issues/22322" rel="noopener nofollow ugc">this issue</a>, I was successful moving an actor with the Quest2. Maybe a similar action file can be implemented for OpenVR</p>

---

## Post #4 by @cpinter (2023-10-18 08:51 UTC)

<aside class="quote no-group" data-username="LucasGandel" data-post="3" data-topic="32037">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucasgandel/48/18202_2.png" class="avatar"> LucasGandel:</div>
<blockquote>
<p>moving an actor with the Quest2</p>
</blockquote>
</aside>
<p>Thanks!</p>
<p>I think what the commenters mean is the two-handed gesture. (When people have just one thing in the scene and use that gesture they tend to think they manipulate the object but in reality they manipulate the physical to world transform)</p>
<p>What do you think would be best? Escape ahead and wait for the OpenXR implementation to be complete and robust (this raises the question of when of course), or try to fix Quest2 with OpenVR?</p>

---

## Post #5 by @LucasGandel (2023-10-18 12:37 UTC)

<p>Sorry I read too fast. I now understand that multi-gesture is the problem.<br>
I think fixing OpenVR should not be a huge effort as opposed to waiting for a robust implementation with OpenXR (which still does not support controller models for instance).<br>
Regarding this specific problem, I’m not sure I can be of much help right now as the code path in SlicerVirtualReality and VTK are so different. For instance, in VTK, the pinch event is handled by changing the scale, but this same line is commented in SlicerVirtualReality (see <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/MRML/vtkVirtualRealityViewInteractor.cxx#L166" rel="noopener nofollow ugc">here</a>). Instead the interactor style seems to handle it in SlicerVirtualReality.</p>
<p>Anyway, my understanding is that the code above works (maybe unreliably?) with other controllers, but not at all for the Quest2, do you confirm?<br>
I suspect that if the Quest have touch-buttons that fire events as soon as your finger/palm touches it, it could potentially not pass the condition here: <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/MRML/vtkVirtualRealityViewInteractor.cxx#L130" rel="noopener nofollow ugc">https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/MRML/vtkVirtualRealityViewInteractor.cxx#L130</a></p>
<p>I won’t have access to a Quest2 before a few weeks, but it would be great to see if a simple VTK example is OK</p>

---

## Post #6 by @cpinter (2023-10-18 12:44 UTC)

<aside class="quote no-group" data-username="LucasGandel" data-post="5" data-topic="32037">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucasgandel/48/18202_2.png" class="avatar"> LucasGandel:</div>
<blockquote>
<p>Anyway, my understanding is that the code above works (maybe unreliably?) with other controllers, but not at all for the Quest2, do you confirm?</p>
</blockquote>
</aside>
<p>Yes, basically that’s it.<br>
For reference, about the unreliably, we have <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/124">this ticket</a>. It used to work 100%, now sometimes the gesture is not reconized.</p>
<blockquote>
<p>I suspect that if the Quest have touch-buttons that fire events as soon as your finger/palm touches it</p>
</blockquote>
<p>It’s great to have a theory, something to get started along. We do not plan to buy Quest 2 (also do not have any funded projects currently related to VR) so I cannot personally help in this effort. Just trying to make a problem visible that many people seem to have. Thanks a lot Lucas for the responses!</p>

---

## Post #7 by @rbumm (2023-10-18 17:28 UTC)

<p>I gave this another systematic try.<br>
Was able to call up a volume rendering with the Quest 2 in 5.4.3 and move the skeleton back and forth. with the right joystick.<br>
Then I pressed the “b” Button on the left controller which brought me to a panel where I could select controller configurations, I did not use “Standard” but user-defined and found a VTK configuration panel, which I selected and also published again. With that I was able to grab the object and turn it apart from moving with the right joystick. .<br>
I think this is all about what the program can do . The unreliability may be caused because you really have to grab short with the grab keys (not the trigger keys)  to get hold of the object.<br>
Good luck</p>

---

## Post #8 by @rbumm (2023-10-19 05:27 UTC)

<p>Rotate: Grab and rotate your arms with controllers.<br>
Push: Grab an push your arms.<br>
Pull: Grab and pull your arms.<br>
Right joystick: Move the world back and forth.</p>

---
