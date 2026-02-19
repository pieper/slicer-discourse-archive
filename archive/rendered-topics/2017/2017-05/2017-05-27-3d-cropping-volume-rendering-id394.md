---
topic_id: 394
title: "3D Cropping Volume Rendering"
date: 2017-05-27
url: https://discourse.slicer.org/t/394
---

# 3D Cropping Volume Rendering

**Topic ID**: 394
**Date**: 2017-05-27
**URL**: https://discourse.slicer.org/t/3d-cropping-volume-rendering/394

---

## Post #1 by @cvaughan (2017-05-27 00:34 UTC)

<p>Hi everyone,</p>
<p>I’m currently making 3D volume renderings of arteries from a series of OCT images captured during a constant rate pullback within a vessel. The reconstructions look spectacular after some fine-tuning in the volume rendering module, but I would like the ROI to be freeform (not square) so I can segment specific layers of the volume. I know this is possible from the segmentation module as well as the 3D cropping scissors tool, but only possible after the volume has been converted to model.</p>
<p>Converting the volume to a model would not be an option as this makes the vessel one homogenous color, eliminating layered structures and vessel wall contrast.</p>
<p>Any options on segmenting / freeform cropping a volume rendering so I can keep the detail in the layers (threshold functionality)?</p>

---

## Post #2 by @lassoan (2017-05-27 00:39 UTC)

<p>After you create the mask in Segment editor, export it to a labelmap and use Mask volume module to crop the volume (blank out parts that are outside the mask).</p>

---

## Post #3 by @Mohamed (2017-06-12 17:29 UTC)

<p>I’m sorry but can i know how we can export the 3D model to labelmap again? and is the Mask volume module different than the “crop volume” module?<br>
I use Slicer 4.5.0-1<br>
Thanks</p>

---

## Post #4 by @lassoan (2017-06-12 17:42 UTC)

<p>Please use the latest nightly version of Slicer. Mask Scalar Volume module and Crop Volume module are two different modules. Hit <em>Ctrl+F</em> and enter <em>Mask</em> to find the Mask Scalar Volume module.</p>

---

## Post #5 by @Mohamed (2017-06-14 14:30 UTC)

<p>Alright. Now i’m using 4.7.0-2017-06-11 nightly version.<br>
I’m trying to use the scissors in Segment Editor to have a free-form cut, but the cut shape is not saved. How it can be saved and masked?</p>

---

## Post #6 by @lassoan (2017-06-14 15:44 UTC)

<p>Export to labelmap node (in Data module, right click on the segmentation node and click Export to labelmap) then use Mask Scalar Volume module to mask out regions of the original volume.</p>

---

## Post #7 by @Mohamed (2017-06-15 09:23 UTC)

<p>I tried that procedure with the “scissors” tool but it gave me at the end black screen. I work from nhdr file not a DICOM series. Could that be the problem?<br>
Do I have to use the CT/MRI series itself to activate the segmentation tools?</p>

---

## Post #8 by @lassoan (2017-06-15 11:45 UTC)

<p>Use the latest nightly version of Slicer.</p>
<p>It works with DICOM images, that should be no problem.</p>
<p>Select the CT/MRI as background volume when you enter the Segment Editor - it should select that volume automatically as Master volume.</p>
<p>What do you mean you got black screen? What was black? Can you describe exactly what steps you performed in what order and when something unexpected happened: what happened and what did you expect to happen?</p>

---

## Post #9 by @Mohamed (2017-06-16 03:35 UTC)

<p>I’m sorry isn’t the 4.7.0-2017-06-11 is the latest version?<br>
For the DICOM data, I tried to import the dataset but an error says “can’t load (name of folder) as DWI Volume as a Diffusion Volume”. It was importing normally in the previous version i used for Slicer though.</p>
<p>The steps are as follows:</p>
<ul>
<li>go to Segment Editor, choose Scissors tool, cut the desired part (from the nhdr slices in this case).</li>
<li>go to Data module, right click on the segment made, export visible segments to binary labelmap</li>
<li>go to Mask Scalar Volume, choose the nhdr images as input volume, choose segmentation-label as Mask Volume, create new volume for the output volume.<br>
-click apply.<br>
Then the black window appeared as below. I expexted to see the desired part cut.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b93cc0c0783c0f684fd1bc85c0eb893a484775a.png" data-download-href="/uploads/short-url/3VXxOFy25wAvlWJ1ODc27iN78IW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b93cc0c0783c0f684fd1bc85c0eb893a484775a_2_690x338.png" alt="image" data-base62-sha1="3VXxOFy25wAvlWJ1ODc27iN78IW" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b93cc0c0783c0f684fd1bc85c0eb893a484775a_2_690x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b93cc0c0783c0f684fd1bc85c0eb893a484775a_2_1035x507.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b93cc0c0783c0f684fd1bc85c0eb893a484775a_2_1380x676.png 2x" data-dominant-color="707077"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×941 60 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2017-06-16 03:57 UTC)

<aside class="quote no-group" data-username="Mohamed" data-post="9" data-topic="394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d78d45/48.png" class="avatar"> Mohamed:</div>
<blockquote>
<p>I’m sorry isn’t the 4.7.0-2017-06-11 is the latest version?</p>
</blockquote>
</aside>
<p>It is, so that’s good.</p>
<aside class="quote no-group" data-username="Mohamed" data-post="9" data-topic="394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d78d45/48.png" class="avatar"> Mohamed:</div>
<blockquote>
<p>load (name of folder) as DWI Volume as a Diffusion Volume</p>
</blockquote>
</aside>
<p>To fix this, in the DICOM module click on Advanced settings and disable the DWI plugin.[quote=“Mohamed, post:9, topic:394”]<br>
choose segmentation-label as Mask<br>
[/quote]</p>
<p>Make sure you also select the correct Label value (index of the segment in the segment list, probably 1, 2, 3, 4, …). You can verify what is the correct label value if you show the labelmap volume and you hover over it with the mouse. The Data probe window in the bottom-left corner shows the label value at the mouse pointer position (<code>L</code> layer, last number in the line in parentheses).</p>

---

## Post #11 by @lassoan (2017-11-03 15:46 UTC)

<p>Note that in recent version of Slicer, the workflow is much simpler, as <code>Mask Volume</code> effect allows masking directly from a segment, without leaving the Segment Editor module. <code>Mask Volume</code> will show up in the Segment Editor module after installing <code>SegmentEditorExtraEffects</code> extension.</p>

---

## Post #12 by @lassoan (2021-05-26 16:59 UTC)

<p>A post was split to a new topic: <a href="/t/mask-volume-using-python-scripting/17814">Mask volume using Python scripting</a></p>

---
