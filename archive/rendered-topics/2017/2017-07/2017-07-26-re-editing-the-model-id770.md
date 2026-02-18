# Re-editing the model

**Topic ID**: 770
**Date**: 2017-07-26
**URL**: https://discourse.slicer.org/t/re-editing-the-model/770

---

## Post #1 by @Albert_Lee (2017-07-26 12:26 UTC)

<p>I am beginner in using 3D slicer and would like to use it in buidling 3D model for numerical analysis.<br>
What I want to do is virtual surgery, so I have to make a preoperative model and then remove different parts of this model to simulate the postoperative conidtion. However, I have some problem in  doing the virtual surgery. I have built the preoperative model and save the model in nrrd, stl vtk, mrml files.When I want to load these files and do virtual surgery by removing some parts of the model, I though I can use the "segmentation -&gt; editor " function to do the virtual surgery, but it does not work… even if I use the paint or eraser function to add and remove some parts of the original model, I can not save a new STL file for further analysis. Is there a right way to re-edit the preoperative model (do the virtual surgery) ?</p>
<p>Thanks !!</p>

---

## Post #2 by @lassoan (2017-07-26 12:43 UTC)

<p>Implementation options depend on what surgical operation you would like to simulate. Would you like to simulate bone removal? Cut and displacement of bones? Cutting of soft tissue?</p>

---

## Post #3 by @lassoan (2017-07-26 14:58 UTC)

<p>If you simply need two models (before and after surgery) and not realistic real-time tissue removal then it’s very simple to do with Segment editor module (instead of legacy Editor module) in recent nightly builds. You can directly edit (cut, paint, etc) on Slicer using scissors, paint, and other effects. Whenever you have a state that you want to 3D print, go to Data module and right-click on your segmentation node, ans choose Export visible segments to models.</p>
<p>See tutorial here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_3D_Printing">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_3D_Printing</a></p>

---

## Post #4 by @Albert_Lee (2017-07-27 00:05 UTC)

<p>Thank you so much for your prompt reply. After asking the question, I tried<br>
again and found that after loading the mrml file, I can then add CT dicom<br>
files . The two set of images can appear simultaneously and I can also edit<br>
the images in segmentation .</p>
<p>So I have solved this problem, but is it correct way to do ? The surgery I<br>
am doing is nasal surgery, I try to do different types of turbinectomy to<br>
see the results. That is the removal of soft tissue and some bony parts of<br>
the nose.</p>
<p>Thanks !!</p>

---

## Post #5 by @lassoan (2017-07-27 00:19 UTC)

<p>In the long term, I would recommend to switch to the latest nightly version of Slicer and to Segment editor, as that module is much more powerful than the legacy Editor module.</p>

---

## Post #6 by @Albert_Lee (2017-07-27 00:26 UTC)

<p>Thank you, sorry I did see your second reply …<br>
Yes the problem is I would like to do two types of surgeries and compare<br>
their results. So I built a pre op model first, save it , and then perform<br>
the  first virtual surgery and save it too with no prpblem. But when I want<br>
to load the preop file and do the second surgery , I failed at this step.<br>
But I manage to do it last night using the way I have described in last<br>
mail. If there is anything more easy or correct to do this step, please let<br>
me know.</p>
<p>Thank you again for you r kind help</p>

---

## Post #7 by @lassoan (2017-07-27 00:44 UTC)

<p>It should all work well with the Segment editor and the nightly version of Slicer as I described above. If you still have problems then describe what exactly fails by explaining what you expected to happen and what happened instead.</p>

---
