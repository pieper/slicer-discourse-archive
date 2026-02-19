---
topic_id: 21510
title: "Measuring In 3D Ct"
date: 2022-01-18
url: https://discourse.slicer.org/t/21510
---

# Measuring in 3d CT

**Topic ID**: 21510
**Date**: 2022-01-18
**URL**: https://discourse.slicer.org/t/measuring-in-3d-ct/21510

---

## Post #1 by @akil.prabhakar (2022-01-18 06:30 UTC)

<p>I am using 3d slicer for the first time. Can someone please guide me regarding how to draw a perpendicular line in 3D CT. When i try using the markup function, the angle gets calculated in a different plane.  (see image 1 and 2)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2353f936096009683b45c68e68e3859de6d3ff07.jpeg" data-download-href="/uploads/short-url/52wCFXqtrcSMYgECS0AoMrQIt4r.jpeg?dl=1" title="Picture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2353f936096009683b45c68e68e3859de6d3ff07_2_690x496.jpeg" alt="Picture2" data-base62-sha1="52wCFXqtrcSMYgECS0AoMrQIt4r" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2353f936096009683b45c68e68e3859de6d3ff07_2_690x496.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2353f936096009683b45c68e68e3859de6d3ff07_2_1035x744.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2353f936096009683b45c68e68e3859de6d3ff07_2_1380x992.jpeg 2x" data-dominant-color="6C857A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture2</span><span class="informations">1411×1015 52.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d75cf6f13cd91436fbcdc6a93b76ef43a9634b46.jpeg" data-download-href="/uploads/short-url/uJbPzUz04SJcfkhkgAxkDjLsKxw.jpeg?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d75cf6f13cd91436fbcdc6a93b76ef43a9634b46_2_690x495.jpeg" alt="Picture1" data-base62-sha1="uJbPzUz04SJcfkhkgAxkDjLsKxw" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d75cf6f13cd91436fbcdc6a93b76ef43a9634b46_2_690x495.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d75cf6f13cd91436fbcdc6a93b76ef43a9634b46_2_1035x742.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d75cf6f13cd91436fbcdc6a93b76ef43a9634b46_2_1380x990.jpeg 2x" data-dominant-color="8792AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">1505×1081 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2022-01-18 10:15 UTC)

<p>Hi! Measuring and drawing are quite different operations. What do you want to achieve?</p>

---

## Post #3 by @akil.prabhakar (2022-01-18 10:41 UTC)

<p>I want to make 2 points on the base of coracoid( where there is a curve on the en face view of glenoid)process and extend it downwards ( this extension should be a perfect straight line ( 180 degree with the base of coracoid line). Hope you understood what I am trying to explain and thank you so much for your reply</p>

---

## Post #4 by @cpinter (2022-01-18 13:42 UTC)

<p>I’m not familiar with a feature that would directly achieve this.</p>
<p>The only thing I think of right now that only involves the GUI is to put a transform on the line and extend it by scaling it, but calculating the transform is not that straightforward (the origin needs to be carefully set).</p>
<p>I’d probably create a very simple Python module that takes your line and extends it by a given amount in the direction of ControlPoint0-&gt;ControlPoint1. This involves using the Extension wizard to create a new module, the Qt Designer to modify a bit the module GUI, and the Python code to calculate the new point and apply it. It would probably take 2 hours to an experienced Slicer programmer, but to a novice it could take weeks… not sure if anyone else has an idea.</p>

---

## Post #5 by @cpinter (2022-01-18 13:45 UTC)

<p>Or to go more DIY a simple Python script that you call from the console would do it too, but that little code has to be written (get vector between two points, apply it in a certain distance, set new control point 1 position).</p>
<p>I just tested this and it works for me:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; f = getNode('Model fixed points') # Replace with the name of your node (Data module, double click item name, copy)
&gt;&gt;&gt; f.GetNumberOfControlPoints()
2
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; p0 = np.zeros(3)
&gt;&gt;&gt; p1 = np.zeros(3)
&gt;&gt;&gt; f.GetNthControlPointPositionWorld(0,p0)
1
&gt;&gt;&gt; p0
array([ 0.43038881, -4.647295  ,  0.6284796 ])
&gt;&gt;&gt; f.GetNthControlPointPositionWorld(1,p1)
1
&gt;&gt;&gt; p1
array([14.29884148, -4.90982199, 21.0538559 ])
&gt;&gt;&gt; v01 = p1 - p0
&gt;&gt;&gt; p1p = p1 + v01 * 2 # Instead of "* 2" whatever elongation you want
&gt;&gt;&gt; f.SetNthControlPointPositionWorld(1,p1p)
</code></pre>

---

## Post #6 by @akil.prabhakar (2022-01-18 14:17 UTC)

<p>Thanks for your guide, but i have zero knowledge about coding and python</p>

---

## Post #7 by @cpinter (2022-01-18 14:25 UTC)

<p>I just did it for you. Edit my code accordingly in an editor (see the two comments), open the Python interactor in Slicer, and copy-paste the code there.</p>
<p>EDIT: You need to ignore the lines not starting with <code>&gt;&gt;&gt; </code>, and for the rest delete the <code>&gt;&gt;&gt; </code>. Then copy-paste and run.</p>

---

## Post #8 by @akil.prabhakar (2022-01-20 05:36 UTC)

<p>thank you so much for your help mate. But I think I am not with coding, can you suggest me some other Dicom Viewer were I would be able to do this measurements (Best DICOM viewer for measuring (angles, area of a circles, to draw a perpendicular line) in 3D CT.</p>
<p>Thanks again Mate</p>

---

## Post #9 by @philippepellerin (2022-01-20 08:16 UTC)

<p>Horos or Osirix lite</p>

---

## Post #10 by @Juicy (2022-01-20 08:19 UTC)

<p>Could you explain a little more clearly what you want to do and what you are ultimately trying to measure on the scapula? I am sure 3D slicer can do what you want. If I get a bit more of an idea of exactly what you want I could make a step by step video on how to use cpinters code in slicer. It is not too complicated seeing as the code is already written.</p>

---

## Post #11 by @akil.prabhakar (2022-01-20 11:54 UTC)

<p>Thank you Juicy, I am doing this to check the glenoid bone loss % (% of glenoid bone loss determines the type of treatment a patient will receive). We take an en-face view of the glenoid (Glenoid facing you). we have to make two points on the base of glenoid (one superior and one inferior - on the enface view this appears like a straight line, but in reality it has a lot complicated 3d structure). Next we have to connect the two points and extend it downwards. If I am able to do this then I can calculate the glenoid bone loss from it.</p>
<p>Thanks again Juicy. and is it possible to draw a circle and measure the area within the circle in slicer??</p>

---

## Post #12 by @akil.prabhakar (2022-01-20 11:55 UTC)

<p>Thanks brother. Osirix is for Mac. I hope Horos is available for Windows!!!</p>

---

## Post #13 by @chir.set (2022-01-20 12:28 UTC)

<aside class="quote no-group" data-username="akil.prabhakar" data-post="11" data-topic="21510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akil.prabhakar/48/13849_2.png" class="avatar"> akil.prabhakar:</div>
<blockquote>
<p>is it possible to draw a circle and measure the area within the circle in slicer??</p>
</blockquote>
</aside>
<p>You should be able to do that with <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/StenosisMeasurement2D.md" rel="noopener nofollow ugc">this</a> tool. Install SlicerVMTK extension in a recent preview release.</p>

---

## Post #14 by @akil.prabhakar (2022-01-21 13:22 UTC)

<p>My bad Osirix and Horos are both MAC based</p>

---

## Post #15 by @akil.prabhakar (2022-01-21 13:23 UTC)

<p>Thank you Chi.set, will give it a try</p>

---

## Post #16 by @Juicy (2022-01-26 04:59 UTC)

<p>Ok, I still don’t understand exactly where you want the points on the glenoid. It seems that 3D slicer could do what you need but if you are not wanting to do any coding then perhaps you could try RadiAnt DICOM. It is easy to get a free trial of the software. It has a 3D MPR mode where you can orient the slice views any way through the volume and has the ability to draw perfect circles, angles in a plane and lengths. Maybe this would be an easier way to do what you want? In the image below I have loaded a scan of a scapula and reoriented the slices so the top left view is looking straight at the glenoid. I have drawn some circles, angles and lines to demonstrate the tools. RadiAnt DICOM can make a 3D model of your scan but you cant really put measurement points on the model. See if this works for you otherwise, there will definitely be ways to do it in slicer using python code. I can show you how to use the code as it is simple enough to paste code into the python interactor.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38582c03add5d65b66a41f671ec3dbe73d882ecf.jpeg" data-download-href="/uploads/short-url/82rE2ATjCRTupRyZs5X77IAzAqb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38582c03add5d65b66a41f671ec3dbe73d882ecf_2_620x500.jpeg" alt="image" data-base62-sha1="82rE2ATjCRTupRyZs5X77IAzAqb" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38582c03add5d65b66a41f671ec3dbe73d882ecf_2_620x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38582c03add5d65b66a41f671ec3dbe73d882ecf_2_930x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38582c03add5d65b66a41f671ec3dbe73d882ecf_2_1240x1000.jpeg 2x" data-dominant-color="383536"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1263×1018 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
