# Inquiries about module types

**Topic ID**: 18464
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/inquiries-about-module-types/18464

---

## Post #1 by @CharlesChen (2021-07-01 16:34 UTC)

<p>Hello,<br>
I’m new to 3D Slicer, and now I am learning how to develop a new module in 3D Slicer to implement new features.<br>
This module’s main function/feature will be: it can be used to calculate the proportion of the confocal regions(overlapping regions) of Z-stack image data displayed in volume rendering mode. For example, if the image data displayed in volume rendering contains red and green channels, the confocal region(overlapping region) will be displayed in yellow. Then, this module will help to calculate the volume and volume percentage of the yellow region. In other words, to achieve the proportion calculation of the intersecting region of multiple volumes.<br>
As I’ve learned, the modules in 3D Slicer include 3 types: CLI, Scripted(in Python), Loadable(in C++), and I noticed that the ‘volume rendering’ belongs to the ‘loadable’ type and is written in C++.<br>
Therefore, if I want to add a module to the ‘volume rendering’ to calculate the volume and proportion of the intersection regions, can this module be of ‘scripted’ type? In other words, can this new module be written in Python or it must be written in C++?<br>
I look forward to and appreciate any help! Thank you!</p>

---

## Post #2 by @lassoan (2021-07-02 05:06 UTC)

<p>Volume rendering is only a visualization technique. It does not help with any kind of measurements. Instead, you can specify regions using Segmentations module (probably Thresholding effect will suffice), get difference, intersection, etc. of the segments (using “Logical operators” effect), and then get volumes using “Segment statistics” module.</p>

---

## Post #3 by @CharlesChen (2021-07-02 15:24 UTC)

<p>Hello Lassoan,<br>
Thank you for your quick and kind reply!<br>
Maybe I didn’t fully elaborate.<br>
I see that the ‘segment statistics’ module can be used to calculate the volume. But letting the user also be able to measure the volume of a specific region in the 3D view/scene of volume rendering is what I want to do.<br>
For example, the user can define an ROI box in the 3D view/scene of volume rendering(Or a similar way) to get the specific region to be measured and then click a button to get the volume value and proportion enclosed by the box. (In the 3D scene of volume rendering, the volume proportion of the intersecting region can be judged and calculated by the ray segmentation. A similar principle is shown in the figure below)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cf04a90d3c5b19acb792c70e2c0f2bb230b9467.png" alt="Ray segmentation in Volume rendering" data-base62-sha1="k6NFo1nP2VhM6KIIwcAo9t1ZZ2L" width="351" height="270"></p>
<p>Therefore, for example, if I want to extend a new module that achieves the above features to the existing ‘Volume rendering’ (A loadable module in C++) in 3D Slicer, Can it be of ‘Scripted’ type(written in Python)?  Or it must also be of loadable type(written in C++)?<br>
Thank you so much!</p>

---

## Post #4 by @lassoan (2021-07-02 17:17 UTC)

<aside class="quote no-group" data-username="CharlesChen" data-post="3" data-topic="18464">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar"> CharlesChen:</div>
<blockquote>
<p>volume of a specific region in the 3D view/scene of volume rendering is what I want to do.</p>
</blockquote>
</aside>
<p>This is exactly what segmentations are for. You can specify and edit regions using Segment Editor module (and you can also import regions from models or labelmap volumes).</p>
<p>You can easily split up a region (a segment) into subregion (several segments), for example by using the scissor tool (see for example <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">here</a>).</p>
<p>If you want to make things very convenient for users then you can create a simple Python scripted module that takes a segmentation, maybe some additional inputs, such as a planes or lines, and then computes all the volumes you need.</p>

---

## Post #5 by @CharlesChen (2021-07-02 20:13 UTC)

<p>Hello Lassoan,<br>
Thank you for your kind reply and materials!<br>
Therefore, in other words, for example, if I want to extend a new module to the ‘Volume rendering’ module, this new module created by me can also be the type of ‘scripted’ written in Python (even the ‘volume rendering’ in 3D Slicer is a loadable module written in C++), right?<br>
Thank you!</p>

---

## Post #6 by @lassoan (2021-07-03 19:51 UTC)

<p>You would not change any Slicer core module, but create your own scripted module. Modules provide high-level widgets that you can place into your own module’s GUI in Qt Designer. To get started you can use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">PerkLab Slicer Bootcamp programming tutorial</a>.</p>

---

## Post #7 by @CharlesChen (2021-07-04 17:43 UTC)

<p>Got you, thank you! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #8 by @WilliamDaniel (2021-07-07 22:25 UTC)

<blockquote>
<p>You would not change any Slicer core module, but create your own scripted module.</p>
</blockquote>
<p>Hello Lassoan,<br>
I am also a beginner in learning 3D Slicer, and I also have an idea similar to <a class="mention" href="/u/charleschen">@CharlesChen</a>: To create a new extension/module in 3D Slicer so that users can directly add visual annotation marks on the 3D images in the volume rendering scene.<br>
So, what you mean is that the ‘Volume rendering’ is a core module of 3D Slicer, so we can’t add/expand new features/modules for it but can only develop a new extension/module in addition (Completely independent of this module)?<br>
If so, does it mean that I should re-implement the volume rendering effect first in my own module (then other features I want)?<br>
Could you please just give a further clarify?<br>
Thank you so much!</p>

---

## Post #9 by @lassoan (2021-07-07 23:41 UTC)

<p>Slicer core modules expose a lot of features in the most general-purpose way possible. If you want to add custom features or implement custom workflows then you don’t modify existing core modules but add custom modules - regardless of what programming language a Slicer core module is implemented in.</p>
<p>If you want to implement a workflow where the user places markups on a volume-rendered image in a 3D view then you’ll add a custom module that has a simple GUI, for example with a volume node selector and a markups place widget. When the user selects an image, the module sets up the views, volume rendering display, etc. Then the user can click the place button to place markups in the views.</p>
<aside class="quote no-group" data-username="WilliamDaniel" data-post="8" data-topic="18464">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/williamdaniel/48/13425_2.png" class="avatar"> WilliamDaniel:</div>
<blockquote>
<p>If so, does it mean that I should re-implement the volume rendering effect first in my own module (then other features I want)?</p>
</blockquote>
</aside>
<p>No need to reimplement any core module, because you can use features of any module from any other module. In term of user interface, usually in a custom end-user workflow you only need to expose a tiny fraction of the options that you see in a core module, because you know a lot about what data you work with and what the user wants to do with it. For example, you probably all the features you need from volume rendering module is a checkbox to show/hide volume rendering and maybe the “Offset” slider.</p>

---

## Post #10 by @CharlesChen (2021-07-08 00:07 UTC)

<p>Hello Lassoan,<br>
Thank you for your brief but clear explanation on this issue, which further deepened my understanding of developing new modules in 3D Slicer. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"> It makes me feel that the features I want to achieve are quite doable(by customizing my own Python scripted module in 3D Slicer).<br>
<a class="mention" href="/u/williamdaniel">@WilliamDaniel</a> Thank you for your further consultation to make this question more specific and clear <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=9" title=":clap:" class="emoji" alt=":clap:"></p>

---

## Post #11 by @WilliamDaniel (2021-07-08 00:14 UTC)

<p>Hello Lassoan,<br>
That’s more clear to me, thank you very much!<br>
<a class="mention" href="/u/charleschen">@CharlesChen</a> Thanks for the discussion with both of you!</p>

---
