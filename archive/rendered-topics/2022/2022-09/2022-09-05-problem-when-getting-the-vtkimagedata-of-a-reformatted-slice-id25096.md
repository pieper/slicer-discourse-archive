---
topic_id: 25096
title: "Problem When Getting The Vtkimagedata Of A Reformatted Slice"
date: 2022-09-05
url: https://discourse.slicer.org/t/25096
---

# Problem when getting the vtkImageData of a reformatted slice shown in Red widget

**Topic ID**: 25096
**Date**: 2022-09-05
**URL**: https://discourse.slicer.org/t/problem-when-getting-the-vtkimagedata-of-a-reformatted-slice-shown-in-red-widget/25096

---

## Post #1 by @Nguyen_My (2022-09-05 10:19 UTC)

<p>SUMMARY</p>
<ul>
<li>Operating system: Windows 10</li>
<li>Slicer version: 5.0.2</li>
<li>Expected behavior: getting the vtkImageData of a reformatted slice shown in Red widget.</li>
<li>Actual behavior: the returned vtkImageData is of another volume in the background layer.</li>
</ul>
<p>DETAIL CONTENT</p>
<p>Hello Prof. Andras and everyone else,</p>
<p>I have a question on how to get the reslice image from a slice node. And all of the following steps were performed by code.</p>
<p>[1] To begin, I have loaded several scalar volumes into 3D Slicer. I suppose their names are in the background-to-foreground order as vol0, vol1, vol2, and vol3.</p>
<p>[2] Next, I have successfully shown a reformatted slice of vol2 as the background layer of the ‘Red’ widget. Please see the attached image for reference.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e660d3416932b191bbcb61b4751a45a63a05ce9b.png" alt="what_I_see" data-base62-sha1="wS1grI8hyJ4PjoCUj4Yy71cCPHR" width="515" height="432"></p>
<p>[3] Now, I want to obtain above reformatted slice as a vtkImageData (not the screenshot) by following code:</p>
<blockquote>
<p>sliceLogic = slicer.app.applicationLogic().GetSliceLogicByLayoutName(‘Red’)<br>
sliceLayerLogic = sliceLogic.GetBackgroundLayer()<br>
sliceLayerLogic.SetVolumeNode(vol2)<br>
reslice = sliceLayerLogic.GetReslice()<br>
reslicedImage = vtk.vtkImageData()<br>
reslicedImage.DeepCopy(reslice.GetOutput())<br>
<em>(reslicedImage is then used for exporting PNG file)</em></p>
</blockquote>
<p>However, when executing the code within my scripted module, the returned image is the slice of vol0 (instead of vol2). Meanwhile, if I type code into the Slicer console, the returned image is as expected (slice of vol2).</p>
<p>I can’t figure out what my mistake is. So I would like to ask for your help or advice.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2022-09-05 17:53 UTC)

<p>Using the rendering infrastructure to do computation is complicated by the fact that many changes don’t occur until the next render cycle, which is event driven.  You should be able to fix this case with the call below added before the DeepCopy.  Excluding user input avoids having some other user click initiate an action in the middle of your code.</p>
<p><code>slicer.app.processEvents(qt.QEventLoop.ExcludeUserInputEvents)</code></p>

---

## Post #3 by @Nguyen_My (2022-09-06 05:51 UTC)

<p>Thank Pieper for the solution and advice!<br>
My code can run as expected now.</p>
<p>Sincerely!</p>

---
