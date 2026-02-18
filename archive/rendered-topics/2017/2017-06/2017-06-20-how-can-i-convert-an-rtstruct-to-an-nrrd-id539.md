# How can I convert an rtstruct to an nrrd

**Topic ID**: 539
**Date**: 2017-06-20
**URL**: https://discourse.slicer.org/t/how-can-i-convert-an-rtstruct-to-an-nrrd/539

---

## Post #1 by @Josiah_McAllister (2017-06-20 13:48 UTC)

<p>Operating system: Windows<br>
Slicer version:4.6.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2017-06-20 14:19 UTC)

<p>In Segmentations module change Master representation to binary labelmap (click <code>Make master</code> button in the <code>Binary labelmap</code> row in Representations section) then save the scene. Structure sets may overlap, therefore the nrrd file will be a 4-dimensional volume, each segment is stored in a separate 3D subvolume.</p>
<p>Use latest nightly build, it’s stable and contains many fixes and improvements.</p>

---

## Post #3 by @Josiah_McAllister (2017-06-20 14:38 UTC)

<p>Thank you for the help</p>

---

## Post #4 by @gcsharp (2017-06-20 15:02 UTC)

<p>Andras, is there a way to create a separate 3D volume file for each segment?</p>
<p>The information in this e-mail is intended only for the person to whom it is<br>
addressed. If you believe this e-mail was sent to you in error and the e-mail<br>
contains patient information, please contact the Partners Compliance HelpLine at<br>
<a href="http://www.partners.org/complianceline" rel="nofollow noopener">http://www.partners.org/complianceline</a> . If the e-mail was sent to you in error<br>
but does not contain patient information, please contact the sender and properly<br>
dispose of the e-mail.</p>

---

## Post #5 by @Josiah_McAllister (2017-06-20 15:17 UTC)

<p>Andras, is there a way to get my segmentation and my image to both be the<br>
same dimensions?</p>

---

## Post #6 by @lassoan (2017-06-20 15:19 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="4" data-topic="539">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Andras, is there a way to create a separate 3D volume file for each segment?</p>
</blockquote>
</aside>
<p>This option is not easily available for the user. You can load the .seg.nrrd file as a volume sequence if you choose “Volume Sequence” in the Add data dialog and then save it, but by default it is saved again as a 4D sequence. You would need to change the default storage node to vtkMRMLSequenceStorageNode to save as a zip file that contains each volume as a separate file.</p>
<p>ITK and VTK can both read volume sequences from 4D files, we also have a Matlab reader/writer that supports 4D volumes, so we never needed them as separate volumes.</p>

---

## Post #7 by @lassoan (2017-06-20 15:25 UTC)

<aside class="quote no-group" data-username="Josiah_McAllister" data-post="5" data-topic="539" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ccd318/48.png" class="avatar"> Josiah_McAllister:</div>
<blockquote>
<p>is there a way to get my segmentation and my image to both be the<br>
same dimensions?</p>
</blockquote>
</aside>
<p>Segmentation will have the same origin, axis direction, and spacing as the input image, but extent usually does not match the input image.</p>
<p>Note that the nrrd header contains SegmentN_Extent:=imin imax jmin jmax kmin kmax field that you can use to efficiently extract only that part of the 3D volume where your particular segment is. You can copy that extent into a larger volume that matches extent of your image.</p>

---

## Post #8 by @lassoan (2017-06-20 20:12 UTC)

<p>2 posts were split to a new topic: <a href="/t/convert-image-and-segmentation-to-dicom/543">Convert image and segmentation to DICOM</a></p>

---

## Post #9 by @lassoan (2017-06-21 16:18 UTC)

<p>A post was merged into an existing topic: <a href="/t/convert-image-and-segmentation-to-dicom/543">Convert image and segmentation to DICOM</a></p>

---

## Post #10 by @mete_naz (2018-03-05 21:21 UTC)

<p>Andras,</p>
<p>Is there a way to share the code with us? I have been trying to figure out how to read my segmented nrrd file however i has been giving me a lot of issues so I couldn’t… I would appreciate if you could possible share your code with me.</p>
<p>Thanks!</p>

---

## Post #11 by @lassoan (2018-03-05 23:06 UTC)

<p>Segmentation is a 4D image in standard nrrd format. You can read it using either VTK or ITK nrrd reader or any nrrd reader that supports 4D volumes. See for example how Slicer reads it: <a href="https://github.com/Slicer/Slicer/blob/0ab294089b4827fea3272417a23c321d57e391b4/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.cxx#L290">https://github.com/Slicer/Slicer/blob/0ab294089b4827fea3272417a23c321d57e391b4/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.cxx#L290</a></p>

---
