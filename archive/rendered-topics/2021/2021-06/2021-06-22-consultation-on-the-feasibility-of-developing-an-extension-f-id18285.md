# Consultation on the feasibility of developing an extension for 3DSlicer

**Topic ID**: 18285
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/consultation-on-the-feasibility-of-developing-an-extension-for-3dslicer/18285

---

## Post #1 by @CharlesChen (2021-06-22 21:50 UTC)

<p>Hello,<br>
I’m new to 3DSlicer, I’d like to ask a few questions about the feasibility of developing an extension/module for calculating the volume proportion of the confocal region in volume rendering.</p>
<p>The measurement of confocal regions is of great interest to many biologists.<br>
Therefore, the main functions/features of the extension/module I’m going to develop are:</p>
<ol>
<li>The image data is visualized in volume rendering.</li>
<li>The proportion of the volume of the confocal region can be calculated. For example, if the image data displayed in volume rendering contains red and green channels, the confocal region(overlapping region) will be displayed in yellow. Then, this extension/module will help us to calculate the volume percentage of the yellow region. In other words, to achieve the proportion calculation of the intersecting region of multiple volumes.</li>
<li>In addition, another feature I’d like to achieve is that the above functions can be integrated into VR so that users can complete the measurement of the volume of the confocal region in VR mode.</li>
</ol>
<p>So my question is:</p>
<ol>
<li>Are the volume rendering and multi-volume rendering of 3Dslicer developed based on VTK?</li>
<li>Is it possible for me to complete this extension/module development with python and VTK? Could you please describe the feasibility of developing this extension/module? And to develop it, where should I start? (I noticed that the Segment Statistics module of 3DSlicer seems can already generate specific volume values.)<br>
Thank you so much!</li>
</ol>
<p>Best Regards,<br>
Charles</p>

---

## Post #2 by @pieper (2021-06-23 13:56 UTC)

<aside class="quote no-group" data-username="CharlesChen" data-post="1" data-topic="18285">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar"> CharlesChen:</div>
<blockquote>
<p>Are the volume rendering and multi-volume rendering of 3Dslicer developed based on VTK?</p>
</blockquote>
</aside>
<p>Yes, Slicer uses the CPU and GPU implementations from VTK for Volume Rendering.  In addition, there is the <a href="https://githubcomets-vis-interactiveslicerprismrendering.readthedocs.io/en/latest/">SlicerPRISM</a> extension for customizing the rendering at the shader level.</p>
<aside class="quote no-group" data-username="CharlesChen" data-post="1" data-topic="18285">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar"> CharlesChen:</div>
<blockquote>
<p>Is it possible for me to complete this extension/module development with python and VTK? Could you please describe the feasibility of developing this extension/module? And to develop it, where should I start? (I noticed that the Segment Statistics module of 3DSlicer seems can already generate specific volume values.)</p>
</blockquote>
</aside>
<p>Yes, this sounds quite doable in python.  You can learn how to do <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers">by following the tutorials</a>.</p>

---

## Post #3 by @CharlesChen (2021-06-24 16:02 UTC)

<p>Hello Pieper,<br>
Thank you for your kind reply!<br>
I’ll dive into the material you provide to learn the module development.<br>
And another thing is that I’ve tested the VR mode(SlicerVR) on my local laptop, but it seems that I can’t do anything beyond moving/rotating/scaling. In the VR scene, I can only see the image data itself but not the GUI panel. Is this normal? In other words, if all the user interfaces in 3D Slicer for a normal flat screen can also be used in VR or not? For example, can I make segmentation in the VR scene?<br>
Thank you so much!</p>

---

## Post #4 by @pieper (2021-06-24 17:10 UTC)

<aside class="quote no-group" data-username="CharlesChen" data-post="3" data-topic="18285">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar"> CharlesChen:</div>
<blockquote>
<p>I can only see the image data itself but not the GUI panel. Is this normal? In other words, if all the user interfaces in 3D Slicer for a normal flat screen can also be used in VR or not?</p>
</blockquote>
</aside>
<p>I know that <a class="mention" href="/u/cpinter">@cpinter</a> has plans for that, using <a href="https://vtk.org/doc/nightly/html/classvtkQWidgetWidget.html">this class</a> but I don’t know when it will be available exactly.</p>

---

## Post #5 by @CharlesChen (2021-06-24 21:13 UTC)

<p>Hello Pieper,<br>
Ok, maybe I can also check with <a class="mention" href="/u/cpinter">@cpinter</a> later.<br>
One more thing is that the loadable module ‘volume rendering’ and the extension ‘SlicerVR’ are both written in C++. Therefore, is it possible to develop an extension based on them in python? Or the development must/better be in C++?<br>
Thank you!</p>

---

## Post #6 by @pieper (2021-06-24 21:41 UTC)

<p>Those are both written in C++ because they involve some hardware access and have performance requirements, but they expose rich APIs to Python, for most use cases I can think of Python gives you more than enough control and performance.  Good luck!</p>

---

## Post #7 by @CharlesChen (2021-06-24 22:13 UTC)

<p>Perfect!<br>
So that’s means I can develop any features I want in python and add them to 3D Slicer?<br>
You mentioned that both of them expose APIs to Python, could you please provide the link?<br>
Thank you so much!</p>

---

## Post #8 by @pieper (2021-06-24 22:19 UTC)

<p>There’s a lot of good material in the developer tutorials that should get you going.  It’s very powerful once you get familiar with it.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers</a></p>

---

## Post #9 by @CharlesChen (2021-06-24 23:18 UTC)

<p>Thank you for your kind help and prompt reply!<br>
I’ll learn from those materials first.<br>
Although for now I’m a beginner and have very limited project development and programming experience, and even I’m not totally clear with the specific feasibility, through communicating with you and the materials you provided, I can feel that I can get a lot of references and help from this community to develop a new module/extension.</p>
<p>Now, I’m learning the basic knowledge of VTK development and Python from some online tutorials.<br>
At first, I think I need to get familiar with how to achieve volume rendering with VTK and python, and after that, I will try to find a way to combine these experiences to develop new features in 3D Slicer.  Even the first step is challenging for me… But I’ll try my best to be familiar with python and VTK development for future extension/module development.<br>
What do you think? If you have any suggestions, please let me know. Thank you so much!</p>

---
