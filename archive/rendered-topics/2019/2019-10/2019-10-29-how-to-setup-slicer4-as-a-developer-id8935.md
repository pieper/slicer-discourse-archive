# How to setup Slicer4 as a developer

**Topic ID**: 8935
**Date**: 2019-10-29
**URL**: https://discourse.slicer.org/t/how-to-setup-slicer4-as-a-developer/8935

---

## Post #1 by @Samuel (2019-10-29 11:46 UTC)

<p>Hi 3D slicer,<br>
I want to setup the slicer4 as a developer but could not find any guide. Can you guide me about this?<br>
Thanks</p>

---

## Post #2 by @rprueckl (2019-10-29 11:47 UTC)

<p>There are build instructions here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a></p>
<p>If you get stuck, the community here is very helpful.</p>

---

## Post #3 by @lassoan (2019-10-29 12:13 UTC)

<p>If you program in C++ then you need to build Slicer as <a class="mention" href="/u/rprueckl">@rprueckl</a> describes above.</p>
<p>If program in Python then you don’t need to build Slicer but start development right away. See for example this tutorial: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials</a></p>

---

## Post #4 by @Samuel (2019-11-13 15:30 UTC)

<p>Hi Andras Lasso,<br>
Thank you for the answer and it helped me understand more. But I still quite don`t understand how to build it. Is it possible for you to make a video tutorial on youtube using python. Thank you.</p>

---

## Post #5 by @lassoan (2019-11-14 01:28 UTC)

<p>You don’t need to build Slicer to develop modules for it - as long as you implement your modules in Python.</p>
<p>In case you want to work in C++ then you need to follow the written build instructions and ask specific questions if you get stuck anywhere. Video tutorials would not be ideal for describing a software build procedure and it would be very hard to maintain.</p>

---

## Post #6 by @Samuel (2019-11-14 09:24 UTC)

<p>okay… Thanks for the help.</p>

---

## Post #8 by @Samuel (2019-11-18 15:16 UTC)

<p>I could not find the markups data. Do you know where the data is located?</p>

---

## Post #9 by @lassoan (2019-11-18 21:51 UTC)

<p>What do you mean by markups data?</p>

---

## Post #10 by @Samuel (2019-11-20 07:02 UTC)

<p>In the scripting and module development tutorial, slide 27 manipulating markups.<br>
The command : f = getNode(‘F’)<br>
I<code>m not sure what is the 'F' in the command because it</code>s not stated in the tutorial and couldn`t find the data to load.</p>

---

## Post #11 by @pieper (2019-11-20 13:02 UTC)

<p><code>F</code> is the name of the node (the default name).  It’s the one that shows up in the user interface.</p>

---

## Post #12 by @Samuel (2019-11-20 20:42 UTC)

<p>Hi pieper thanks for trying to help me but I think u got the wrong idea of my question.<br>
What I`m trying to say is I do not know where is the F data stored because in order for me to run this command: f = getNode(‘F’). I need to able to load the F data before typing the command.</p>
<p>Sorry I <code>m not good at explaining. Hope you can understand what I</code> m trying to say. Thank you.</p>

---

## Post #13 by @lassoan (2019-11-20 20:51 UTC)

<p>You do not need to “load” the <code>F</code> node. You just need to follow instructions on the slide “Create 2 markup points”. These markup points will be stored in a new node and the node’s name will be <code>F</code> by default.</p>

---

## Post #14 by @Samuel (2020-03-20 13:02 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hi, I would like to ask something about the segmentation module.<br>
What type of segmentation method is used to segment the image. Is it 3d closed surface segmentation?</p>

---

## Post #15 by @lassoan (2020-03-20 15:52 UTC)

<p>There are many segmentation tools (“segment editor effects”). Which ones you are interested in?</p>
<p>Or, are you interested in how the segmentation data is represented in Slicer? You can find the answer <a href="https://www.slicer.org/wiki/Documentation/Labs/Segmentations">here</a>.</p>

---

## Post #16 by @Samuel (2020-03-22 04:24 UTC)

<p>In the segmentation tutorial of " <a href="https://youtu.be/BJoIexIvtGo" rel="nofollow noopener">Video tutorial: Whole heart segmentation from cardiac CT</a>", what is the segmentation algorithm used to segment the heart.</p>
<p>Sorry for the trouble, the community here is indeed very fast response and helpful. Thank you.</p>

---

## Post #17 by @lassoan (2020-03-22 04:32 UTC)

<p>“Grow from seeds” is based on the “Fast grow-cut method” - see more information here: <a href="http://interactivemedical.org/imic2014/CameraReadyPapers/Paper%204/IMIC_ID4_FastGrowCut.pdf">http://interactivemedical.org/imic2014/CameraReadyPapers/Paper%204/IMIC_ID4_FastGrowCut.pdf</a></p>

---

## Post #18 by @Samuel (2020-03-22 11:54 UTC)

<p>Thanks, you really helped me alot. Have a nice day!!!</p>

---
