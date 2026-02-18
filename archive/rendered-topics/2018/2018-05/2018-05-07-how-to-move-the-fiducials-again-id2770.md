# How to move the fiducials again?

**Topic ID**: 2770
**Date**: 2018-05-07
**URL**: https://discourse.slicer.org/t/how-to-move-the-fiducials-again/2770

---

## Post #1 by @esurechao (2018-05-07 18:12 UTC)

<p>Operating system:  windows 10<br>
Slicer version: 4.6.2</p>
<p>I am trying to obtain the 3D coordinates of the organ landmarks.<br>
These are my steps:<br>
Load CT DICOM files<br>
Use segment editor module to visualize the structure in the 3D viewer<br>
Place fiducials in the 2D viewer (usually in axial slices)<br>
Save the scene</p>
<p>I have two problems after I saved the scenes.</p>
<p>The first problem is:<br>
When I opened these scenes again, I cannot find the fiducials in the axial slice. Usually I had to look for these fiducials in the sagittal or coronal slices. Although the coordinates of the fiducials did not change, the distribution of the axial slices changed.</p>
<p>The second problem is:<br>
After I found the fiducial, the fiducial was “duplicated” when I moved it. There will be two identical fiducials with identical text in the viewers.</p>
<p>Did I miss something?<br>
Thank you very much.</p>

---

## Post #2 by @pieper (2018-05-07 23:52 UTC)

<p>Hi -</p>
<p>Please try the latest Slicer nightly builds to see if there is still an issue.  If so can you confirm that things work if you leave out the Segment Editor step?</p>
<p>Thanks for reporting,<br>
Steve</p>

---

## Post #3 by @esurechao (2018-05-08 04:49 UTC)

<p>Thank you for your response!</p>
<p>I tried the same steps in the latest slicer nightly builds. It still happened.<br>
I also simplified my operation into only two steps: Load CT DICOM files, Save the scene. But it still happened.</p>
<p>For example:<br>
After loading chest CT DICOM files, the distribution of superior coordinate of the axial slices was: 1499.500, 1504.500, 1509.500……<br>
I saved the files in one directory, without editing segment or placing fiducial.<br>
Then I chose the directory to add data into the scene. The distribution of superior coordinate of the axial sliced became 1492.00, 1497.00, 1502.00……</p>
<p>Thank you again.</p>

---

## Post #4 by @pieper (2018-05-08 11:48 UTC)

<p>Hi -</p>
<aside class="quote no-group" data-username="esurechao" data-post="3" data-topic="2770">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/c5a1d2/48.png" class="avatar"> esurechao:</div>
<blockquote>
<p>the distribution of superior coordinate of the axial slices was: 1499.500, 1504.500, 1509.500……</p>
</blockquote>
</aside>
<p>Can you clarify where you are getting these numbers?  Is it from the slider <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Slice_Viewers">above the slice view</a> then those are continuous values in patient space and not slice locations.</p>

---

## Post #5 by @esurechao (2018-05-08 13:17 UTC)

<p>Thank you.<br>
Yes, I used the number on the right side of the slice selector.<br>
In a given axial slice, the number was equal to the Z coordinate of any points in the slice, so I thought the number was the Z coordinate of the axial slice.</p>

---

## Post #6 by @pieper (2018-05-08 14:19 UTC)

<p>Yes, it is the slice offset (foot to head for axial view) and it can set many ways depending on the view mode etc (by default when it’s loaded the offset is set to be in the center of the volume).  The fiducials show up on any slice location within a tolerance.  You can enable slice jumping in the Markups interface if you want to see the exact slice where the fiducial is displayed.</p>

---
