---
topic_id: 35923
title: "Is It Possible To Move And Rotate A Model In 3D View And Get"
date: 2024-05-05
url: https://discourse.slicer.org/t/35923
---

# Is it possible to move and rotate a model in 3d view and get the transformtion matrix?

**Topic ID**: 35923
**Date**: 2024-05-05
**URL**: https://discourse.slicer.org/t/is-it-possible-to-move-and-rotate-a-model-in-3d-view-and-get-the-transformtion-matrix/35923

---

## Post #1 by @tdchen (2024-05-05 01:09 UTC)

<p>I can change the transformation matrix to make a model moves in 3d view.<br>
But how can I do the opposite that move and rotate a model in 3d view and get its transformation matrix?<br>
Any method or suggestion?<br>
Thanks.</p>

---

## Post #2 by @pieper (2024-05-05 12:13 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html</a></p>

---

## Post #3 by @tdchen (2024-05-06 00:01 UTC)

<p>Thank you pieper.<br>
But I can’t understand.<br>
In fact, the key of my problem is how I can move a model directly in the 3D view,not in the transformation panel.<br>
Perhapes, it need a widget?</p>

---

## Post #4 by @muratmaga (2024-05-06 00:17 UTC)

<aside class="quote no-group" data-username="tdchen" data-post="3" data-topic="35923">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/858c86/48.png" class="avatar"> tdchen:</div>
<blockquote>
<p>how I can move a model directly in the 3D view,</p>
</blockquote>
</aside>
<p>What do you mean by that? You can use the mouse clicks to rotate/translate a model in 3D view. But that only changes the angle camera is seeing the model. If you want to modify its orientation, you need to use the transforms module.</p>

---

## Post #5 by @Davide_Scorza (2024-05-06 06:59 UTC)

<p>I think there’s no such feature available at the moment.<br>
If I understood correctly, you would like to interact with the module similarly as you do with a markup list.</p>
<p>We achieve a similar behaviour with some custom models (e.g. screws), by reusing a set of slicer nodes (markuplist, model_nodes and tranformnodes), programming a custom object class (it requires a bit of programming).<br>
We use a two-point markup list, aligned with the main direction of the model that we want to interact with, and linked the “markup modified event” to recompute a transform that is then applied automatically to the model node, any time one of the markups is updated.</p>
<p>It is a workaround for a similar behaviour I guess you want to achieve, but it requires to program that part.</p>
<p>Davide</p>

---

## Post #6 by @tdchen (2024-05-08 07:28 UTC)

<p>Thank you muratmaga<br>
Yes, I can change orientation of models with transform module. But it is uneasy to control. I want to design a cutting position with mouse in 3d view, and get the corresponding transform.</p>

---

## Post #7 by @tdchen (2024-05-08 08:05 UTC)

<p>You understand me, Davide_Scorza.<br>
I really want to know if there is an available module to do it.<br>
Now that you’ve told me, I’m ready to program.<br>
Sorry for my poor English.</p>

---

## Post #8 by @philippepellerin (2024-05-08 08:57 UTC)

<p>I never find a way to do that easily with slicer, so I use to do a reslicing with the 3D MPR(multi planar rendering) tool in Horos, export the new set then import this volume to slicer, which give you the volume and the .h5 file which is the transform, you can just aply or harden, as you wish</p>

---

## Post #9 by @emmawilson (2024-05-08 09:18 UTC)

<p>Hello tdchen,<br>
As per my knowledge, To extract a transformation matrix from a 3D model’s movement and rotation, track applied transformations programmatically or use 3D graphics libraries. In code, maintain variables for translation and rotation, composing them into a final matrix. In addition, leverage libraries with functions for model manipulation and matrix retrieval. Some 3D software offer APIs for direct access to transformation data. Choose the method based on project needs and development environment, ensuring efficiency and accuracy in representing the model’s position and orientation.</p>
<p>I hope this will help you.</p>
<p>Thanks<br>
Emma wilson</p>

---

## Post #10 by @cpinter (2024-05-08 10:04 UTC)

<p>If I understand correctly what you’d like to do, here are the steps:</p>
<ol>
<li>
<p>Turn on interactive transform for the model in the Data module (right click the eye not the name)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28f7d9f414a39fba0f293e6aff44849a5398e98f.png" alt="image" data-base62-sha1="5Qq7jpf9pl6oLo1g2XfqYNCktuT" width="622" height="228"></p>
</li>
<li>
<p>Transform the model using the controls<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e08665c2875574b332ea65aa5e769dd8e3411ae.jpeg" data-download-href="/uploads/short-url/fHow8sVobTeMeZOeUAbIw6x7TQy.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e08665c2875574b332ea65aa5e769dd8e3411ae_2_622x500.jpeg" alt="image" data-base62-sha1="fHow8sVobTeMeZOeUAbIw6x7TQy" width="622" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e08665c2875574b332ea65aa5e769dd8e3411ae_2_622x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e08665c2875574b332ea65aa5e769dd8e3411ae.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e08665c2875574b332ea65aa5e769dd8e3411ae.jpeg 2x" data-dominant-color="66856A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">693×557 67.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>See the matrix in the Transforms module<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83aa88bbb6bd94c3199917d049806e839d72431c.png" alt="image" data-base62-sha1="iMLUOc2IOSsvM113ut2uNiANyoc" width="546" height="192"></p>
</li>
</ol>
<p>You’ll need a recent 5.7 preview version to be able to access the new transform interactions.</p>

---

## Post #11 by @tdchen (2024-05-08 13:55 UTC)

<p>Yes, philippepellerin. We have plan that export data to other software and get the transformation.</p>

---

## Post #12 by @tdchen (2024-05-08 14:10 UTC)

<p>Thanks for your suggestion, emmawilson.<br>
I think Slicer must have the ability to realize your plan, and I need to find it.</p>

---

## Post #13 by @philippepellerin (2024-05-08 15:18 UTC)

<p>Thank you for your feedback. I perfectly know this way, as well as in 2D using the interaction in the cross, which is very useful, but it is very difficult to get a new volume oriented as a series .dicom or.NRRD. It is much more convenient in Horos.<br>
It depend what you want to do, if it is just to oriente the 3D use the cross interaction to get the plane you want, then draw a plane, it is efficient.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0014d4138263190560b3d94638cc1219ef0519b0.jpeg" data-download-href="/uploads/short-url/ICJj4qU7r7xjceWdPZfzfF98k.jpeg?dl=1" title="PastedGraphic-1.png" rel="noopener nofollow ugc"><img width="682" alt="PastedGraphic-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0014d4138263190560b3d94638cc1219ef0519b0_2_682x500.jpeg" data-base62-sha1="ICJj4qU7r7xjceWdPZfzfF98k" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0014d4138263190560b3d94638cc1219ef0519b0_2_682x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0014d4138263190560b3d94638cc1219ef0519b0_2_1023x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0014d4138263190560b3d94638cc1219ef0519b0_2_1364x1000.jpeg 2x" data-dominant-color="8D88A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1.png</span><span class="informations">2560×1876 520 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @tdchen (2024-05-08 15:59 UTC)

<p>Great! That is what I want!<br>
It appears in the document now.<br>
But how did you find it？ I have never installed the beta version.</p>

---

## Post #15 by @cpinter (2024-05-08 16:07 UTC)

<aside class="quote no-group" data-username="tdchen" data-post="14" data-topic="35923">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/858c86/48.png" class="avatar"> tdchen:</div>
<blockquote>
<p>But how did you find it？ I have never installed the beta version.</p>
</blockquote>
</aside>
<p>Download the preview version from <a href="https://download.slicer.org/">https://download.slicer.org/</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f18bafcb4a625315ab2d74d3d5d2f94918e7dccb.png" data-download-href="/uploads/short-url/ysOlyJ1strkKYf5N2rCEMck2ShB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f18bafcb4a625315ab2d74d3d5d2f94918e7dccb_2_690x295.png" alt="image" data-base62-sha1="ysOlyJ1strkKYf5N2rCEMck2ShB" width="690" height="295" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f18bafcb4a625315ab2d74d3d5d2f94918e7dccb_2_690x295.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f18bafcb4a625315ab2d74d3d5d2f94918e7dccb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f18bafcb4a625315ab2d74d3d5d2f94918e7dccb.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">893×383 21.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="philippepellerin" data-post="13" data-topic="35923">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>I perfectly know this way, as well as in 2D using the interaction in the cross</p>
</blockquote>
</aside>
<p>That is a different function. Look at my screenshots please and you’ll see.</p>

---

## Post #16 by @philippepellerin (2024-05-08 16:27 UTC)

<p>I am running 5.7.0, easily found; let me know if you have any problems. Are you specifically interested in drawing a reference plane? I can make a tutorial if you want.</p>

---

## Post #17 by @tdchen (2024-05-08 16:29 UTC)

<p>Thank you cpinter.<br>
I was using the stable version 5.2, and I found out it already have this feature, which I never noticed.</p>

---

## Post #18 by @tdchen (2024-05-08 16:35 UTC)

<p>Thank you philippepellerin<br>
Let me try it first and contact you if I have any questions.</p>

---

## Post #19 by @tdchen (2024-05-08 17:07 UTC)

<p>Now, I understand what you told me.<br>
Thanks.</p>

---

## Post #20 by @tdchen (2024-05-08 17:11 UTC)

<p>You are right, muratmaga.<br>
I should read the document carefully.<br>
It is not a problem in slicer.</p>

---
