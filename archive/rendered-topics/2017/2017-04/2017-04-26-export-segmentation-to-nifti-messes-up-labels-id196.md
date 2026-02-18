# Export segmentation to Nifti messes up labels

**Topic ID**: 196
**Date**: 2017-04-26
**URL**: https://discourse.slicer.org/t/export-segmentation-to-nifti-messes-up-labels/196

---

## Post #1 by @Yannick (2017-04-26 14:13 UTC)

<p>Hello,</p>
<p>I have been labelling 3D volumes for a while now, but I always have troubles to export into a format which can be easily read by ImageJ or Fiji. usually, one label is missing and others have incorrect id. Please tell me the recommended way.</p>
<p>The problem:<br>
1- Load a 3D volume (I use Analyze format)<br>
2- Go to the new Segment Editor, create at least 5 segments and draw over the volume. No problem there.<br>
3- The segmentation can be saved as “Segmentation.seg.nrrd” or “Segmentation.nrrd” only.<br>
How do I export to something more usual (Analyze / Nifti are more familiar to me) ? The other formats are not available in the list there.</p>
<p>This doesn’t work:<br>
4- Open a new 3D Slicer window and drop the “Segmentation.nrrd” into it (load as a Volume). The funny thing is I do see the segmented regions. That’s what I want to export.<br>
5- There, I can choose other formats, such as Analywe (.hdr) or Nifti (.nii). This creates a volume on the disk.<br>
6- ImageJ loads a volume which has at least 5 channels, but channel 4 is gone and the channels from 5 and beyond have a index decreased by 1. Is there any explanation to this ?</p>
<p>Thanks for the feedback and explanations on the correct export sequence.</p>

---

## Post #2 by @ihnorton (2017-04-26 14:22 UTC)

<p>For import in to ImageJ/Fiji, why not use NRRD? ImageJ/FIJI had decent support for NRRD last time I used it.</p>
<p>I’m not sure about the Nifti part of the question – do you have any documentation of what format your other software considers as a “Nifti labelmap”? It might be helpful to link a sample dataset.</p>

---

## Post #3 by @Yannick (2017-04-26 15:39 UTC)

<p>Thanks for the reply.</p>
<p>I must be missing something obvious, but I don’t see how to do it:</p>
<ul>
<li>Fiji opens NRRD using the BioFormat plugin. I’ve updated it today.
<ul>
<li>When I throw Segmentation.nrrd on it, it complains that it doesn’t work for more than 3 dimensions.</li>
</ul>
</li>
<li>ImageJ 1.49v and 1.50 only open a text editor when I throw the NRRD file.</li>
</ul>
<p>For now, I assume there is no tool which converts NRRD to Nifti in dimensions higher than 3.<br>
(The Editor in Slicer, seems to create one dimension for each Segment and store binary values for each segment. This allows a voxel to belong to multiple Segments simultaneously)</p>
<p>From a different application, there are reports that conversion using CMTK doesn’t allow more than 3 dimensions (<a href="https://www.nitrc.org/forum/forum.php?thread_id=3573&amp;forum_id=857" rel="nofollow noopener">link</a>).</p>
<p>I’ll be working on a small dataset tomorrow.</p>

---

## Post #4 by @muratmaga (2017-04-26 16:02 UTC)

<p>If you are using  the segment editor, you need to export your segments as label maps, I think. You can use the segmentation module to do that.<br>
m</p>

---

## Post #5 by @ihnorton (2017-04-26 16:03 UTC)

<p>The first thing to figure out is what the Nifti file should look like. What do you consider to be a “more usual” analyze/nifti holding a segmentation? Is it supposed to be a 4d volume, a bitmask, or something else. (if it’s supposed to be a bitmask, try converting the segmentation to a labelmap and export that as nii).</p>
<p>For NRRD, have you tried SCIFIO?</p>

---

## Post #6 by @lassoan (2017-04-26 16:05 UTC)

<p>If your labels are not overlapping then you can convert the segmentation into a labelmap (simple 3D volume, each segment has a different voxel value):</p>
<ul>
<li>Go to Data module (if you don’t use the latest nightly: Subject Hierarchy module)</li>
<li>Right-click on the segmentation node, choose “Export visible segments to binary labelmap”</li>
<li>Save the generated labelmap to file</li>
</ul>

---

## Post #7 by @Yannick (2017-04-27 08:33 UTC)

<p>Thanks to <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/muratmaga">@muratmaga</a> (and the others)</p>
<p>You are all correct: I need to export into a labalmap and I didn’t know this even existed.<br>
I’m using Slicer v4.6.2 and here are the operations I had to do:</p>
<ul>
<li>Module Segmentation, item “copy/move segment (import/export)”
<ul>
<li>Click icon to add a labelmap volume to the scene</li>
<li>Select all segments holding the shift key and press the “+&gt;” button to transfer them to the labelmap</li>
</ul>
</li>
<li>Save the project, Fiji can open the new Segment.nrrd without problem.</li>
</ul>
<p>I was missing this step to convert all the binary segmentations into a labelmap.<br>
You saved my day. Thanks.</p>

---

## Post #8 by @lassoan (2017-04-27 12:15 UTC)

<p>I would strongly recommend to use latest nightly version of Slicer. It has lots of fixes and improvements compared to the last stable version.</p>

---
