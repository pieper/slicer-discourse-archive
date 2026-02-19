---
topic_id: 8437
title: "3D Modeling Of Abdominal Aorta Aneurysm"
date: 2019-09-15
url: https://discourse.slicer.org/t/8437
---

# 3D modeling of abdominal aorta aneurysm 

**Topic ID**: 8437
**Date**: 2019-09-15
**URL**: https://discourse.slicer.org/t/3d-modeling-of-abdominal-aorta-aneurysm/8437

---

## Post #1 by @eran_eichler (2019-09-15 18:14 UTC)

<p>Hello everyone!<br>
In starting a new research project in biomechanics.</p>
<p>For this project i need to model abdominal aorta aneurysm from ct files into 3D stl file and finaly perform flow simulation in ANSYS fluent.</p>
<p>I am really struggling creating the model from ct files, i didnt found any specific tutorial for the AAA case.</p>
<p>I really need your help in learning how to do this task, and if anyone have tutorials for simulation of AAA FSI in fluent it would be amazing.</p>
<p>Thanku and have a wonderful day!</p>

---

## Post #2 by @Amine (2019-09-15 20:18 UTC)

<p>I can only help with the segmentation part:<br>
First make a threshold that has both vascular and bone tissue then use this to separate the two</p><aside class="quote quote-modified" data-post="4" data-topic="8432">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/cut-3d-surface-from-the-whole-with-accuracy/8432/4">Cut 3d surface from the whole with accuracy</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, grow from seeds will not have an extent over the whole segment by default, that is why you either paint the limits you want it to have on a dummy segment (outside the segment you want to split, it will not be taken as a seed since its outside the editable area but will still define the boundaries of GFS) 
I see you only have one seeding segment, so it is normal for GFS to not work, you need to place seeds in the vertebra AND make another segment with seeds in the sacrum AND a segment outside…
  </blockquote>
</aside>
<p>
This describes the same process with an Abdominal Aneurysm :</p><aside class="quote quote-modified" data-post="2" data-topic="6006">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/suggestion-quicker-scissor-tool-and-seed-growing-to-split-a-segment-in-two-parts/6006/2">Suggestion: Quicker scissor tool and Seed growing to split a segment in two parts</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    As for the Second Proposition, i tought id make an illustrated description because it is really important, 
So the goal is to separate this threshold into vascular and Bone 
[1] 
To do this, the method i found is to use editable=inside that layer to paint seeding regions in two new segments 
[2] 
Then hide the original threshold, and do a growfromseeds with editable=Inside the hidden layer, to get this: 
[3] 
The problem here as you see is that grow from seeds defines  cropping region limited to…
  </blockquote>
</aside>

<p>Ps: in this case you could just remove the bone using a sphere eraser</p>

---

## Post #3 by @justdcinaus (2019-09-19 02:29 UTC)

<p>Good day to you.<br>
My suggestion is similar to the above, however after setting the threshold I use the sphere tool to highlight the aorta (simply run it up the length), while not being to concerned about getting small sections of the spine.</p>
<p>Then I use islands to keep only the largest island.</p>
<p>Finally I do another 4 steps<br>
1 create a new segment<br>
2 use logical operators to copy the aorta (making sure you are not overwriting segments)<br>
3 use Margins to grow by a small amount (1.6 mm)<br>
4 back to logical operators to subtract your original segment from the new one - leaving you with a hollow artery.</p>
<p>Hopefully this is sufficient for your purposes<br>
David</p>

---
