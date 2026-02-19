---
topic_id: 1611
title: "Real Time Distance Measurement Between The Needle Tip And Ta"
date: 2017-12-07
url: https://discourse.slicer.org/t/1611
---

# Real-time distance measurement between the needle tip and target with PlusToolkit and 3D Slicer

**Topic ID**: 1611
**Date**: 2017-12-07
**URL**: https://discourse.slicer.org/t/real-time-distance-measurement-between-the-needle-tip-and-target-with-plustoolkit-and-3d-slicer/1611

---

## Post #1 by @Serg (2017-12-07 16:35 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I’m a newbie in 3d Slicer and amazed its functionality. Great work!</p>
<p>I’m looking for the solution to dynamically measure the distance between the needle tip and the target by using the electromagnetic tracking device in 3d space. Within the PlusServer, I can track the needle in Slicer. Would be possible to make the measurement in real-time by using the PlusToolkit within the Slicer? If so, can you suggest, what should be done?<br>
Thank you!</p>

---

## Post #2 by @cpinter (2017-12-07 16:52 UTC)

<p>You can put two Markups Fiducials in the two coordinate systems (under the NeedleTipToReference and TargetToReference transforms), manually set their position to (0,0,0), then calculate their position when either of the parent transforms are modified (connect to the Modified event). Where would you like to display that distance? It sounds to me like you’d want a very simple module. A few lines of python code should do the trick. Unless there is already a module that can do it that I’m not aware of…</p>

---

## Post #3 by @Serg (2017-12-07 17:35 UTC)

<p>Thank you for the quick response! Actually I want to display the distance in 3d viewer. You’re right - i would like to use a very simple module. Could you suggest, what should be written in python?</p>

---

## Post #6 by @cpinter (2017-12-07 18:20 UTC)

<p>Once you reached this state for markups and transforms (this shows the Data module)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80e852a5c57185f5c27fdd0429f48c4a5e0b5d58.png" alt="image" data-base62-sha1="iomRFpi2JTVY4a0IEDLDz3Ubuk0" width="317" height="145"><br>
(make sure the markups each have one fiducial at origin)<br>
then you can get the distance between them like this:</p>
<pre><code>f=getNode('F')
f1=getNode('F_1')
fp=[0]*4
f.GetNthFiducialWorldCoordinates(0,fp)
f1p=[0]*4
f1.GetNthFiducialWorldCoordinates(0,f1p)
import math
d=math.sqrt((f1p[0]-fp[0])**2 + (f1p[1]-fp[1])**2 + (f1p[2]-fp[2])**2)
</code></pre>
<p>This works if you paste it in the python interactor. However if you want to have a module, then you need to start from a module template, add data selectors, and use a considerably cleaned up version of this code (no herdcoded node names, proper variable names, error checks, etc.) in it.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Scripted_Modules" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Scripted_Modules</a></p>

---

## Post #7 by @lassoan (2017-12-07 18:51 UTC)

<p>I think Breach Warning module in SlierIGT does exactly what you need: it shows distance of the needle tip from a selected model, in 3D view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f509c0948a102f4c8aa2f1c1dd334484ef80e9e.png" data-download-href="/uploads/short-url/fSJHFnsfw8orKqKrZblq8JJRW4S.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f509c0948a102f4c8aa2f1c1dd334484ef80e9e_2_690x391.png" alt="image" data-base62-sha1="fSJHFnsfw8orKqKrZblq8JJRW4S" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f509c0948a102f4c8aa2f1c1dd334484ef80e9e_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f509c0948a102f4c8aa2f1c1dd334484ef80e9e_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f509c0948a102f4c8aa2f1c1dd334484ef80e9e.png 2x" data-dominant-color="C1C5DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1152×654 53.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @Serg (2017-12-07 19:40 UTC)

<p>Andras and Csaba, thank you for your help! Yes, these are exactly two things what i’m looking for: (1) the python solution and (2) the simple measurement visualization in 3d view.<br>
Quick question: how to assign NeedleToRAS? This was somewhere in the tutorial. However, I can’t find it now.<br>
Thanks.</p>

---

## Post #12 by @lassoan (2017-12-07 20:07 UTC)

<p>NeedleToRAS is the transform that defines the needle tip position and orientation in the RAS (world) coordinate system. You can create a transform and just move it using sliders in Transforms module, or you can get the transform from a tracker through OpenIGTLink. The transform name in tutorials would be probably StylusTipTo… or NeedleTipTo… (Needle coordinate system is usually the coordinate system of the sensor that is attached to the needle, which is not exactly located at the needle tip).</p>

---

## Post #13 by @Serg (2017-12-07 20:44 UTC)

<p>Yes! I created a transform (NeedleToRAS) in Transforms module and it works just fine. Thank you very much for the tremendous help! It saved a lot of time.</p>

---

## Post #14 by @Vinny (2018-03-10 19:01 UTC)

<p>I’d like to calculate the distance between AC and PC on a AC-PC aligned T1.  I only got as far as displaying the connecting line between AC and PC using the Markups to Model module.  For the Breach Warning Module, I do not know what transform to use.  Also, I’d like to use the Python Interactor to do a similar calculation.  Thanks for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba489f0cb64e907fe58505b8f0d518f506d97232.jpeg" data-download-href="/uploads/short-url/qzWoNc9itx1vV4fCNnH11AyAhDY.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba489f0cb64e907fe58505b8f0d518f506d97232_2_690x370.jpg" alt="image" data-base62-sha1="qzWoNc9itx1vV4fCNnH11AyAhDY" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba489f0cb64e907fe58505b8f0d518f506d97232_2_690x370.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba489f0cb64e907fe58505b8f0d518f506d97232_2_1035x555.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba489f0cb64e907fe58505b8f0d518f506d97232_2_1380x740.jpg 2x" data-dominant-color="959596"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1030 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @lassoan (2018-03-11 02:41 UTC)

<aside class="quote no-group" data-username="Vinny" data-post="14" data-topic="1611">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vinny/48/7052_2.png" class="avatar"> Vinny:</div>
<blockquote>
<p>I’d like to calculate the distance between AC and PC on a AC-PC aligned T1</p>
</blockquote>
</aside>
<p>You can very easily compute distance between two fiducial points in Python, but if you want to display distance between two points in the viewer, like a ruler, then it is probably better to use the annotation ruler. Click on the small down-arrow button next to the fiducial place icon on the toolbar and select placement of ruler, then click on the two points in the image.</p>

---
