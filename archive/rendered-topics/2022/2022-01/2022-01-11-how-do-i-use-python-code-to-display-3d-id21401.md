---
topic_id: 21401
title: "How Do I Use Python Code To Display 3D"
date: 2022-01-11
url: https://discourse.slicer.org/t/21401
---

# How do I use Python code to display 3D？

**Topic ID**: 21401
**Date**: 2022-01-11
**URL**: https://discourse.slicer.org/t/how-do-i-use-python-code-to-display-3d/21401

---

## Post #1 by @pleuvoir (2022-01-11 04:56 UTC)

<p><strong>Software version:</strong> 4.11.20210226 R29738/7A593C8<br>
<strong>Problem description:</strong> from the official web page, find the following code: segmentation. CreateClosedSurfaceRepresentation ()  。<br>
I tried to realize the “Create_” function of clicking the button next to “Closed surface” under the “Representations” function of  “Segmentations” module in the software, but it kept prompting errors or did not show the effect.</p>

---

## Post #2 by @pleuvoir (2022-01-11 05:33 UTC)

<p>As shown in the previous post, I tried to change the statement in the diagram to:<br>
LabelmapVolumeNode = slicer. Util. GetNode (" label “)<br>
Seg = slicer. MrmlScene. AddNewNodeByClass (” vtkMRMLSegmentationNode ")<br>
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, seg)<br>
seg.CreateClosedSurfaceRepresentation()<br>
To achieve the “create” button effect in software.<br>
But the runtime keeps saying: Label cannot be found.<br>
Can you offer some ideas or solutions?  Thank you so much!!</p>

---

## Post #3 by @pleuvoir (2022-01-11 06:05 UTC)

<p>The indexth node where name or ID matches is used to obtain the indexth node where name or ID matches.  Seems to be the reason for my error.  However, the problem is still unresolved. If I just use getNode(“label”), I will be told there is no “label” node or something.  Could you please tell me how I can implement python code to display a 3D image of the current 2D slice .</p>

---

## Post #4 by @lassoan (2022-01-11 19:42 UTC)

<p>The latest version of the documentation (<a href="https://slicer.readthedocs.io/en/latest/">https://slicer.readthedocs.io/en/latest/</a>) is applicable to the latest Slicer Preview Release. Please use the latest Slicer Preview Release and let us know if you still have questions.</p>

---

## Post #5 by @pleuvoir (2022-01-12 01:38 UTC)

<p>all right,I can try it ,thank you very much</p>

---

## Post #6 by @pleuvoir (2022-01-12 08:07 UTC)

<p>Dear Mr. Lassoan, thank you for your reply.  I do have a question that needs to be answered, as shown below:<br>
I followed your guidance to find Python code that I think can be used instead of GUI to display 3D operations.  However, the copy fails to run in Python on the software interface.  I changed getNode(“label”) to getNode(“Segment_2001”) and It`s failed .<br>
then I changed getNode(“label”)to Silcer.uitl.getNode (“”) on the same line as the error  .<br>
Thank you very much and look forward to your reply!!!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/580aa76c7e605d58836285b582486b8253acacb6.png" data-download-href="/uploads/short-url/cyQQimI9Ze44dU6JG15YgeFD4cC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/580aa76c7e605d58836285b582486b8253acacb6_2_690x284.png" alt="image" data-base62-sha1="cyQQimI9Ze44dU6JG15YgeFD4cC" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/580aa76c7e605d58836285b582486b8253acacb6_2_690x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/580aa76c7e605d58836285b582486b8253acacb6_2_1035x426.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/580aa76c7e605d58836285b582486b8253acacb6_2_1380x568.png 2x" data-dominant-color="80807B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1875×774 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @pleuvoir (2022-01-12 08:12 UTC)

<p>And,This is an error after I changed getNode(“label”) to slicer.util.getNode(“label”) :<br>
Error:Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “D:\software\PycharmProjects\For Xv of Tiantan\For Xv of Tiantan\ColorMapper\Mapper.py”, line 83, in execute<br>
labelmapVolumeNode = slicer.util.getNode(“label”)<br>
File “D:\software\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 1312, in getNode<br>
raise MRMLNodeNotFoundException(“could not find nodes in the scene by name or id ‘%s’” % (pattern if (isinstance(pattern, str)) else “”))<br>
slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘label’</p>

---

## Post #8 by @pleuvoir (2022-01-21 01:44 UTC)

<p>I’ve worked out this problem</p>

---
