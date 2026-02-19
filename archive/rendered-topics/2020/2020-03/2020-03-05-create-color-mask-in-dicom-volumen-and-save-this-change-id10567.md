---
topic_id: 10567
title: "Create Color Mask In Dicom Volumen And Save This Change"
date: 2020-03-05
url: https://discourse.slicer.org/t/10567
---

# create color mask in dicom volumen and save this change.

**Topic ID**: 10567
**Date**: 2020-03-05
**URL**: https://discourse.slicer.org/t/create-color-mask-in-dicom-volumen-and-save-this-change/10567

---

## Post #1 by @Carlos_Ferro (2020-03-05 20:11 UTC)

<p>it´s posible to create color mask and add this color mask in dicom volume, without that this mask to see in binary.<br>
or is possible create color mask of fiducial an save this mask in dicom volume .</p>

---

## Post #3 by @lassoan (2020-03-05 20:15 UTC)

<p>Yes, you can define colored masks in Segment Editor module and export it to DICOM (RT structure set or as segmentation object). You need to install SlicerRT (for RT structure set) and Quantitative Reporting (for segmentation object) extensions before initiating DICOM export.</p>

---

## Post #4 by @Carlos_Ferro (2020-03-05 20:22 UTC)

<p>How do I export it without the masks becoming binary?</p>
<p>I do not get it.<br>
Could you give me a step by step.</p>

---

## Post #5 by @lassoan (2020-03-05 20:39 UTC)

<p>You can add any number of segments and you can assign a color to each segment. See tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">here</a>.</p>

---

## Post #6 by @Carlos_Ferro (2020-03-05 20:53 UTC)

<p>If I understand the segmentation.<br>
What I don’t understand is how to export these rgb segmentations in the dicom volume without looking binary.</p>

---

## Post #7 by @Carlos_Ferro (2020-03-05 22:46 UTC)

<p>in mask volume i can save the mask in binary, but how i can save this mask in color?</p>

---

## Post #8 by @lassoan (2020-03-05 23:03 UTC)

<p>Segment colors are saved in both RT structure sets and DICOM segmentation objects.</p>
<p>What would you like to do with the created DICOM data objects? What software will use them and for what purpose?</p>

---

## Post #9 by @Carlos_Ferro (2020-03-05 23:22 UTC)

<p>I need to make one volumen whit this color segmentation and fiducials points to  generate navigate imagen.</p>
<p>This is posible?</p>

---

## Post #10 by @lassoan (2020-03-06 00:06 UTC)

<p>Would you like to use it for surgical navigation? What software/system would you like to import the data into? Medtronic, BrainLab, some radiation therapy treatment planning system, …?</p>
<p>FYI, you can do surgical planning and navigation in Slicer. You can also run Medtronic StealthStation/BrainLab in parallel with Slicer, get registration and real-time navigation information from the commercial navigation system and deploy experimental features in Slicer. See more information at <a href="http://www.slicerigt.org">www.slicerigt.org</a>.</p>
<p>Example of parallel navigation in Slicer and StealthStation:</p>
<div class="lazyYT" data-youtube-id="UHmv5u-sB5g" data-youtube-title="Integration of 3D Slicer with Medtronic StealthStation navigation system" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #11 by @Carlos_Ferro (2020-03-06 13:32 UTC)

<p>hello, thank’s for the information.<br>
i have other question.</p>
<p>I would like to mount this image with the color masks in the fiagon system, or the brainlab one.<br>
What I want is to generate the dicom image already in color and that it be put into the system to perform the procedure.</p>

---

## Post #12 by @lassoan (2020-03-06 14:05 UTC)

<p>I don’t think either these systems can load color image volumes. BrainLab can load segmentations exported from Slicer.</p>

---

## Post #13 by @pieper (2020-03-06 14:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="10567">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>BrainLab can load segmentations exported from Slicer.</p>
</blockquote>
</aside>
<p>Yes, that’s true, and also diffusion tractography results in dicom format.  But only their most recent systems support this.</p>

---

## Post #14 by @Carlos_Ferro (2020-03-06 14:35 UTC)

<p>Hello, how can I export the segmentation in dicom format, in addition to the fiducials that I put in the mask also in dicom.</p>

---

## Post #15 by @lassoan (2020-03-06 15:23 UTC)

<aside class="quote no-group" data-username="Carlos_Ferro" data-post="14" data-topic="10567">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carlos_ferro/48/6209_2.png" class="avatar"> Carlos_Ferro:</div>
<blockquote>
<p>Hello, how can I export the segmentation in dicom format</p>
</blockquote>
</aside>
<p>See instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export" class="inline-onebox">Documentation/Nightly/Modules/DICOM - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="Carlos_Ferro" data-post="14" data-topic="10567">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carlos_ferro/48/6209_2.png" class="avatar"> Carlos_Ferro:</div>
<blockquote>
<p>fiducials that I put in the mask also in dicom</p>
</blockquote>
</aside>
<p>I am not aware of any commonly used DICOM data object that could store landmark points that commercial surgical navigation systems can import. You can draw small segments and mark them manually in the commercial system. 3D Slicer is essential for surgical planning and navigation research exactly because of such trivial limitations. The usual surgical navigation research/prototyping setup is that Slicer runs in parallel with commercial systems and you develop all new features in Slicer. Clinicians primarily rely on the commercial system, while they may look at additional information provided by the research system.</p>

---
