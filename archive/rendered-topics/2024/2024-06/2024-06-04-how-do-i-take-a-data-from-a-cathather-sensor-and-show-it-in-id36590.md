---
topic_id: 36590
title: "How Do I Take A Data From A Cathather Sensor And Show It In"
date: 2024-06-04
url: https://discourse.slicer.org/t/36590
---

# how do I take  a data from a cathather sensor and show it in a heart

**Topic ID**: 36590
**Date**: 2024-06-04
**URL**: https://discourse.slicer.org/t/how-do-i-take-a-data-from-a-cathather-sensor-and-show-it-in-a-heart/36590

---

## Post #1 by @mayaambar (2024-06-04 13:47 UTC)

<p>Hello<br>
I am working at a startup company, developing cathather for the heart.<br>
we have a sensor that tell as the X Y Z and the roll pitch and azimuth with each movement.<br>
we also have a model of the left atrium that we built in Solid works,(that can be converted to STL)<br>
I wanted to ask if there is a way to do that with 3d slicer?<br>
I will appreciate any help.<br>
thank you<br>
Maya</p>

---

## Post #2 by @lassoan (2024-06-04 14:11 UTC)

<p>Yes, this (and much more) is already working well in Slicer. <a href="https://www.slicerigt.org/wp/user-tutorials/">SlicerIGT tutorials</a> is a good starting point and you can always ask here if you get stuck with anything.</p>
<p>You don’t need to create some artificial left atrium models in SolidWorks but you can load actual models from NavX, Carto3, or Rhythmia mapping systems using SlicerHeart extension’s <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/EAMapReader.md">EA Map Reader module</a>.</p>

---

## Post #3 by @mayaambar (2024-06-18 08:19 UTC)

<p>Thank you for the quick respond<br>
I watched the 3d slicer tutorial as you suggested , I now realize that what I need is to use the IGT extension in order to take the information I’m getting from the pollehmus tracker I have and show it in real time on the slicer , the problem is I can’t seem to find a tutorial on how to use the IGT. DO you know something that can help me?<br>
another problem we are having is that I built a 3d model of the heart from the example data that slicer suggest, but it is not 100% correspond to the real life model we use. we have a model that fit the one we use in solid, is there a way we can use it in slicer ?<br>
thank you and have a great day<br>
Maya</p>

---
