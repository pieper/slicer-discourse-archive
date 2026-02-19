---
topic_id: 1456
title: "Incorrect Display Of Registration Result Image"
date: 2017-11-14
url: https://discourse.slicer.org/t/1456
---

# Incorrect display of registration result image

**Topic ID**: 1456
**Date**: 2017-11-14
**URL**: https://discourse.slicer.org/t/incorrect-display-of-registration-result-image/1456

---

## Post #1 by @Eloise (2017-11-14 14:52 UTC)

<p>Hi slicer developers,</p>
<p>I am new to Slicer and I am working on a C++ loadable module to do image registration.<br>
My registration module runs without any error and the resulting node is displayed in Slicer. The output has correct origin, spacing and orientation information, but the problem is that I can’t see the registered image : data is all black but when I mouse over the output volume slices, I can see that the intensity values of the image are not all 0, they are non null values.<br>
And, when I save this output (either as a nifti file or as a dicom file) and reload it, the display is correct, I can see the registered image overlay with the fixed one.</p>
<p>Do you have any idea where this problem might come from ?</p>
<p>Thanks for your help,</p>
<p>Eloïse</p>

---

## Post #2 by @lassoan (2017-11-14 16:05 UTC)

<p>You need to set the window/level values for display: after you create your output volume and set the input image, create a display node (<code>volumeNode-&gt;CreateDefaultDisplayNodes()</code>) and then call <code>volumeNode-&gt;GetDisplayNode()-&gt;AutoWindowLevelOn()</code>.</p>

---

## Post #3 by @Eloise (2017-11-15 14:35 UTC)

<p>Hi Andras,</p>
<p>Thank you for your response. I’ve set the window/level settings as suggested, they are correct in the Volumes module but it does not solve my problem, the view remains black but I can read values when I mouse over the slices.</p>

---

## Post #4 by @lassoan (2017-11-15 15:29 UTC)

<p>Can you fix the window/level by left-click and drag on the image?</p>
<p>Does it help if you force resetting window/level by calling volumeNode-&gt;GetDisplayNode()-&gt;AutoWindowLevelOff() and then volumeNode-&gt;GetDisplayNode()-&gt;AutoWindowLevelOn()? Maybe instead of using the heuristics of automatic window/level, it would be even better to copy window/level setting from the input moving volume.</p>
<p>Maybe the order of adding nodes and setting various information in the nodes are not correct. Can you send a link to the source code of your module to the part where you create and initialize the output volume node?</p>

---
