---
topic_id: 1895
title: "How To Get Correct Mask Value From One Segment From Segment"
date: 2018-01-22
url: https://discourse.slicer.org/t/1895
---

# How to get correct mask value from one segment from Segment Editor?

**Topic ID**: 1895
**Date**: 2018-01-22
**URL**: https://discourse.slicer.org/t/how-to-get-correct-mask-value-from-one-segment-from-segment-editor/1895

---

## Post #1 by @spring (2018-01-22 07:23 UTC)

<p>Operating system: win10 64-bit<br>
Slicer version:4.9.0-2017-10-23 r26509</p>
<p>Expected behavior: the mask value of GetBinaryLabelmapRepresentation() is same with original mask<br>
Actual behavior:mask value which got from Binary GetBinaryLabelmapRepresentation()  is different with original inputted mask value.</p>
<p>Hi SlicerExperts:</p>
<pre><code>I am trying to show a segment with the mask value from a json file,below is my steps:
 1.create a vtkImageData,and set the basic values from below lines:
        "mask": {
            "zBegin": "19.104156494140625",
            "xBegin": "67.1884765625",
            "yEnd": "-103.6318359375",
            "zEnd": "25.404266357421875",
            "yBegin": "-99.7353515625",
            "sliceMask": {
                "count": "10",
                "item": "000000000000000000010000000000000000000000000000",
                "item": "000000000111100001111000011111000011100000000000",
                "item": "011110000111110011111100111111000111110000110000",
                "item": "011111001111111011111110111111100111110001111000",
                "item": "011111001111111011111111111111101111111001111100",
                "item": "011111001111111011111111111111111111111001111100",
                "item": "011110001111110011111111111111110111111001111100",
                "item": "001100000111110011111110111111100111110000111000",
                "item": "000000000111100001111000011110000011100000000000",
                "item": "000000000000000000000000000100000000000000000000",
          }
 2. create a vtkMarchingCubes and passed step1's result to setInputData () when creating a corresponding polydata；
 3. create one modelNode ,SetAndObservePolyData(step1's polydata) and  segmentationNode ,used ImportModelToSegmentationNode(modelNode, segmentationNode) to bind the modelNode to segmentationNode;
 4.call rep = segmentationNode.GetBinaryLabelmapRepresentation(segmentID) to get the  specific segment, and assigned   arr = rep.GetPointData().GetArray(0) to get all of the points of this Segment,and output below mask values:
	outputmask=['000000000000000000001000000000000000000000000000', 
                                   '000000000001111000011110001111100001110000000000', 
                                     '000111100011111000111111001111110011111000001100', 
                                      '001111100111111101111111011111110011111000011110', 
                                       '001111100111111111111111011111110111111100111110', 
                                       '001111100111111111111111111111110111111100111110', 
                                       '000111100011111111111111111111110111111000111110', 
                                     '000011000011111001111111011111110011111000011100', 
	                          '000000000001111000011110000111100001110000000000', 
                                   '000000000000000000000000000010000000000000000000']
</code></pre>
<p>The result can not match original mask values,it seems there are some data have been changed ,we want to get the mask value of segment is same with the original data,could you give us some ideas?</p>
<p>Thanks，<br>
Chunbo</p>

---

## Post #2 by @MRI23D (2018-01-22 13:13 UTC)

<p>I am a newbie who has no idea.  So if you send code segment i freeze.  Would you be kind enough to delineate a bit further?</p>

---

## Post #3 by @lassoan (2018-01-22 17:44 UTC)

<p>Marching cubes algorithm is for generating smooth surfaces. In general, conversion between smooth surface and binary labelmap representations is a lossy operation. If you don’t need smooth surface then you can use vtkDiscreteMarchingCubes algorithm instead, which generates small cubes (see picture below - left: smooth surface, right: cubes):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e883c13e954fd210da8a022f0049d7136fda8cf6.png" data-download-href="/uploads/short-url/xaV3vH5ybutv3tngEvMdBKPEOlE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e883c13e954fd210da8a022f0049d7136fda8cf6_2_690x345.png" alt="image" data-base62-sha1="xaV3vH5ybutv3tngEvMdBKPEOlE" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e883c13e954fd210da8a022f0049d7136fda8cf6_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e883c13e954fd210da8a022f0049d7136fda8cf6_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e883c13e954fd210da8a022f0049d7136fda8cf6.png 2x" data-dominant-color="7B7B7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×640 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @spring (2018-01-23 01:26 UTC)

<p>Thanks lassoan,</p>
<pre><code>I have tried vtkDiscreteMarchingCubes,the result is same:can not match original mask values in json file.
</code></pre>
<p>It seems that we can not create MarchingCubes object,correct?</p>
<p>Best，<br>
Chunbo</p>

---

## Post #5 by @lassoan (2018-01-23 01:43 UTC)

<p>I cannot answer your question without actually knowing what is the context, what is the high-level goal of your of your project and what specific problem you are trying to solve.</p>

---

## Post #6 by @spring (2018-01-23 02:06 UTC)

<p>Hi Lassoan,</p>
<pre><code>Thanks for your helps.

The background is:we want to show some regions(original mask value in a json file) like ROIs in Slicer by using Segment Editor (create one SegmentationNode to show all of these regions,each segment  represent one region); 
</code></pre>
<p>The goal is: we can edit the edges of regions and save them into another Json file,then we can get radiomics for each modified regions.</p>
<p>Our methods:<br>
1.create vtkImageData for each masks in json file;<br>
2.create a vtkMarchingCubes,and setInputData(vtkImageData),then create Polydata for this vtkMarchingCubes;<br>
3.create one modelNode ,SetAndObservePolyData(Polydata) ;<br>
4. create segmentationNode,and used ImportModelToSegmentationNode(modelNode, segmentationNode)<br>
5.call rep = segmentationNode.GetBinaryLabelmapRepresentation(segmentID) to get specific segment;<br>
6.assigned   arr = rep.GetPointData().GetArray(0) to get all of the points of this Segment.</p>
<p>Current problem is: we found the output masks from step6  are different with original data even if we did not modified the corresponding Region,there is  a lossy operation.</p>
<pre><code>We have tried: using vtkDiscreteMarchingCubes to replace vtkMarchingCubes.
</code></pre>
<p>Just want to know:how to get the correct masks from segment(same with original data)?</p>
<p>Thanks,<br>
Chunbo</p>

---

## Post #7 by @spring (2018-01-23 03:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>，since convert vtkMarchingCube/vtkDiscreteMarchingCubes to a binary labelmap is a “lossy operation”，so maybe it is impossible to get the same masks from the converted object,correct?</p>

---

## Post #8 by @lassoan (2018-01-23 04:57 UTC)

<aside class="quote no-group" data-username="spring" data-post="6" data-topic="1895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ee59a6/48.png" class="avatar"> spring:</div>
<blockquote>
<p>The goal is: we can edit the edges of regions</p>
</blockquote>
</aside>
<p>You can edit segmentations in Segment Editor module with various tools. Is there some operation that you cannot do in the Segment Editor?</p>
<aside class="quote no-group" data-username="spring" data-post="6" data-topic="1895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ee59a6/48.png" class="avatar"> spring:</div>
<blockquote>
<p>2.create a vtkMarchingCubes,and setInputData(vtkImageData),then create Polydata for this vtkMarchingCubes;</p>
</blockquote>
</aside>
<p>Why do you create polydata manually? Segmentation node can provide you closed surface representation as <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_representation_of_a_segment">shown here</a>.</p>
<aside class="quote no-group" data-username="spring" data-post="6" data-topic="1895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ee59a6/48.png" class="avatar"> spring:</div>
<blockquote>
<ol start="4">
<li>create segmentationNode,and used ImportModelToSegmentationNode(modelNode, segmentationNode)</li>
</ol>
</blockquote>
</aside>
<p>You still have the binary labelmap representation in the segmentation. Why do you import the segment?</p>
<aside class="quote no-group" data-username="spring" data-post="6" data-topic="1895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ee59a6/48.png" class="avatar"> spring:</div>
<blockquote>
<p>We have tried: using vtkDiscreteMarchingCubes to replace vtkMarchingCubes</p>
</blockquote>
</aside>
<p>if you use vtkDiscreteMarchingCubes then it should be possible to convert without losing information, but the result is just a cube for each voxel, so the vtkDiscreteMarchingCubes output is not usable for much.</p>

---

## Post #9 by @spring (2018-01-24 03:17 UTC)

<p>Hi Lassoan,</p>
<pre><code>Below is some updates.

"You can edit segmentations in Segment Editor module with various tools. Is there some operation that you cannot do in the Segment Editor?"
</code></pre>
<p>[Yes,we want to save the modified masks into a json file which can be inputted as a argument when computing Radiomics by a exe file;]</p>
<pre><code>"Why do you create polydata manually? Segmentation node can provide you closed surface representation as shown here."
</code></pre>
<p>[This polydata = vtk.vtkMarchingCubes().GetOutput(),will be used to modelNode.SetAndObservePolyData(polydata) ,then loaded into segmentationNode by ImportModelToSegmentationNode(modelNode, segmentationNode).]</p>
<pre><code>"You still have the binary labelmap representation in the segmentation. Why do you import the segment?"
</code></pre>
<p>[I am not sure when this binary labelmap representation has been <a href="http://created.In" rel="nofollow noopener">created.In</a> our logic,this binary labelmap representation was got  from segmentationNode.GetBinaryLabelmapRepresentation(segmentID) at last step,since we have to get each segment’s mask after all of segments have been added,and save those masks into json file.Pls correct me if I am wrong.]</p>
<pre><code>"if you use vtkDiscreteMarchingCubes then it should be possible to convert without losing information, but the result is just a cube for each voxel, so the vtkDiscreteMarchingCubes output is not usable for much."
</code></pre>
<p>[We have changed to this method: create a vtkImageData to save mask values firstly–&gt;then convert it  to vtkOrientedImageData–&gt;ImportLabelmapToSegmentationNode(vtkOrientedImageData, segmentationNode)–&gt;segmentationNode.GetBinaryLabelmapRepresentation(eachSegmentID)—&gt;Output masks.<br>
And the result (mask value) is same with original one.]</p>
<p>Thanks，<br>
Chunbo</p>

---

## Post #10 by @lassoan (2018-01-24 04:39 UTC)

<p>You can import either labelmaps or models into Segmentation node and you can retrieve labelmap or polydata VTK objects or export to labelmap volume or model node from a segmentation node.</p>
<p>It does not matter what input you originally set in Segmentation node (labelmap or polydata), conversions to any other representation are done automatically. You may tune smoothing and decimation parameters if you want to, but defaults should work well.</p>
<p>If your json file contain labelmap then set a labelmap in your Segmentation node. If your json file contains polydata then set that in your Segmentation node.</p>
<aside class="quote no-group" data-username="spring" data-post="9" data-topic="1895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ee59a6/48.png" class="avatar"> spring:</div>
<blockquote>
<p>we want to save the modified masks into a json file</p>
</blockquote>
</aside>
<p>What modifications do you perform on the masks? With which module? Segment editor?</p>

---

## Post #11 by @spring (2018-01-24 05:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="1895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What modifications do you perform on the masks? With which module? Segment editor?</p>
</blockquote>
</aside>
<p>Yes,Lassoan.We are using Segment Editor to modify the some regions(erase some edges or draw others).Then Saved the changed masks into json file for computing radiomics.</p>
<p>Thanks,<br>
Chunbo</p>

---

## Post #12 by @lassoan (2018-01-24 05:52 UTC)

<p>OK, then you should be able to do everything using Segmentations and Segment Editor modules. I don’t think you need to create model nodes at all.</p>

---

## Post #13 by @spring (2018-01-24 06:09 UTC)

<p>Got it.</p>
<p>Thanks for your helps,Dr. Andras Lasso.</p>

---

## Post #14 by @Christineseven (2019-05-24 13:00 UTC)

<p>Hello there!Did you find a solution for this? I have the same problem.We loaded the masks(uncorrected) for our mri images imgs that our model predicted. And we want just modify some parts of the mask.(adding with draw or delete some parts of the mask without draw all the mask) in order to have a better mask to give it to our model instead of the uncorrected.Thanks</p>

---

## Post #15 by @lassoan (2019-05-24 13:36 UTC)

<aside class="quote no-group" data-username="Christineseven" data-post="14" data-topic="1895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/christineseven/48/3819_2.png" class="avatar"> Christineseven:</div>
<blockquote>
<p>we want just modify some parts of the mask.</p>
</blockquote>
</aside>
<p>You can do this in the Segment Editor module. If you have any specific problem then post it in a new topic.</p>

---
