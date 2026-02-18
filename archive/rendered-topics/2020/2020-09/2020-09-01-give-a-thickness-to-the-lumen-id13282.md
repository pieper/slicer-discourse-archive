# Give a thickness to the lumen

**Topic ID**: 13282
**Date**: 2020-09-01
**URL**: https://discourse.slicer.org/t/give-a-thickness-to-the-lumen/13282

---

## Post #1 by @Hamid (2020-09-01 17:48 UTC)

<p>I extracted a Aorta lumen from a dicom files using 3d slicer, at this point  I am looking for an open source software to give the lumen a desired thickness. if you know a software please leave a note.<br>
many thanks</p>

---

## Post #2 by @lassoan (2020-09-01 17:49 UTC)

<p>You can use Hollow effect in Segment Editor module to create a thick shell from a solid segment.</p>

---

## Post #3 by @Hamid (2020-09-02 00:02 UTC)

<p>Lassoan many thanks to you,It works perfect.<br>
and also is there any way in slicer 3D to make and add <em><strong>cannula</strong></em> (plastic tube using to bypass the left ventricular connecting it to the aorta in LVAD system) to the segmented aorta.<br>
Thanks again.</p>

---

## Post #4 by @lassoan (2020-09-02 00:05 UTC)

<p>Yes, you can draw tubes using “Draw tube” effect in Segment editor. This effect is provided by SegmentEditorExtraEffects extension (you need to install this extension in Extension manager and restart Slicer).</p>

---

## Post #5 by @Hamid (2020-09-02 00:33 UTC)

<p>I did it,but the Draw tube effect is not added to the editor! however some other effects are added like: fast marching, surface cut,split volume,watershed,…</p>

---

## Post #6 by @lassoan (2020-09-02 00:43 UTC)

<p>Are you using latest Slicer Preview Release?</p>

---

## Post #7 by @Hamid (2020-09-02 00:52 UTC)

<p>I am using 4.10.2 version</p>

---

## Post #8 by @Hamid (2020-09-02 00:55 UTC)

<p>I see I am using stable, I just saw the preview version 4.11 in the website. Do I need to install 4.11?</p>

---

## Post #9 by @lassoan (2020-09-02 00:56 UTC)

<p>Yes, the stable version is very old now, so it lacks many features and fixes, so I would recommend to use the most recent preview release.</p>

---

## Post #10 by @Hamid (2020-09-02 00:57 UTC)

<p>Thank you so much. I’ll do and will be back to you if there is any issues.</p>

---

## Post #11 by @Hamid (2020-09-02 14:39 UTC)

<p>Thank you Lassoan! The new release is perfect.<br>
I have a question:<br>
1-‘Hollow’ :how can I have the lumen and shell at the same time?<br>
when I make the shell with considering the current segment as inside surface,apparently the lumen vanishes.Is there any possibility to make shell and also hold the lumen in different color for visualization?</p>

---

## Post #12 by @Hamid (2020-09-02 14:56 UTC)

<p><strong>"Draw tube" effect:</strong> I don’t know how to use this effect in the point of connection(cannula to aorta shell) in order to make a neat and precise connection, and also is there any option to give them an angle in the connection point?<br>
when I make a cannula by Draw tube it seems it is connected to aorta in 3d but when I rotate the view It appears in different direction!</p>

---

## Post #13 by @lassoan (2020-09-02 15:05 UTC)

<aside class="quote no-group" data-username="Hamid" data-post="11" data-topic="13282">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/5fc32e/48.png" class="avatar"> Hamid:</div>
<blockquote>
<p>how can I have the lumen and shell at the same time?</p>
</blockquote>
</aside>
<p>You can make a copy of the segment (create a new segment and use Logical operators to copy content from other segment). [quote=“Hamid, post:12, topic:13282”]<br>
I don’t know how to use this effect in the point of connection(cannula to aorta shell) in order to make a neat and precise connection<br>
[/quote]</p>
<p>You can adjust the control points of the curve in any of the 3D views. Connection of a large-diameter tube can result in quite complex geometry, so maybe you need to clean up some edges or intersections using Paint effect.</p>

---

## Post #14 by @Hamid (2020-09-02 16:40 UTC)

<p>Thanks for the great help!</p>

---

## Post #15 by @Hamid (2020-09-04 03:47 UTC)

<p>I have 2 sets of DICOM files.one of them contains 150 images and other has 3000 images,both are the same CT-scan images and in the second one It seems like they are repeat themselves! and I am told the 2nd set is flow data.Is there any open source software to read flow data?</p>

---

## Post #16 by @lassoan (2020-09-04 04:27 UTC)

<p>Recent Slicer Preview Releases should be able to read correctly many of the 4D flow data sets, but if you have problems with this one then share an anonymized/phantom/animal data set with us (upload the data set somewhere and post the link here) and we’ll investigate.</p>

---

## Post #17 by @Hamid (2020-09-06 02:43 UTC)

<p>would you please tell me briefly  which tabs or effects should be used to read the flow data? I have not done it before so I have no idea how the flow data will appear in 3d slicer from loading CT images. what form of data should be seen?</p>

---

## Post #18 by @lassoan (2020-09-06 05:14 UTC)

<p>You can load 4D data by switching to DICOM module, drag-and-dropping the DICOM folder to the Slicer application window, wait for the indexing to complete, then double-click on the patient, study, or series that you want to load.</p>

---

## Post #19 by @Hamid (2020-09-06 13:12 UTC)

<p>How can I extract e.g the ‘flow rate’ or any type of flow data from those data?</p>

---

## Post #20 by @lassoan (2020-09-06 18:01 UTC)

<p>You can segment vessels and extract centerline using VMTK extension, straighten the vessel image and flow field using Curved planar reformat module (in Sandbox extension), and then get the average flow rate with a trivial Python script.</p>
<p>The main question is how the flow field can be imported from DICOM. It may need some tuning of the DICOM importer. We can help with this if you provide a sample data set (phantom, animal, or anonymized patient).</p>

---

## Post #21 by @Hamid (2020-09-13 02:18 UTC)

<p>Thank you again for your help!</p>

---

## Post #22 by @Hamid (2020-09-14 02:19 UTC)

<p>Is there any tutorial for ‘<strong>Draw Tube</strong>’?<br>
I am trying to use it to add a tube to my segmentation and I need to know how to adjust the control points of the curve in any of the 3D views.</p>

---

## Post #23 by @Hamid (2020-09-15 00:10 UTC)

<p>I have  Aorta and cannula segmented, I want to merge them first then use Hollow to make thick shell from lumen. How can I merge those first?</p>

---

## Post #24 by @lassoan (2020-09-20 15:44 UTC)

<p>You can combine segments using Logical operators effect.</p>

---

## Post #25 by @Hamid (2020-09-20 22:06 UTC)

<p>Perfect,worked.<br>
Many thanks Lassoan!</p>

---

## Post #26 by @Hamid (2020-09-23 22:36 UTC)

<p>I want to see inside the thick shell. Is there any way to hide a portion of the shell temporarily to see the remain part?</p>

---

## Post #27 by @lassoan (2020-09-24 00:07 UTC)

<p>You can make the model surface transparent or enable slice clipping in Models module to make the model appear clipped, or use Dynamic Modeler module to create a clipped copy of the node.</p>

---

## Post #28 by @Hamid (2020-09-26 03:09 UTC)

<p>Slice clipping worked perfectly,appreciate Lassoan!</p>

---

## Post #29 by @lassoan (2020-09-26 20:23 UTC)

<p>3 posts were split to a new topic: <a href="/t/how-to-measure-vessel-diameter/13713">How to measure vessel diameter</a></p>

---
