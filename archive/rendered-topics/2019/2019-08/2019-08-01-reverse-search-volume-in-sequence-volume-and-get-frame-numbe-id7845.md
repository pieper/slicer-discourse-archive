# Reverse search volume in sequence volume and get frame number

**Topic ID**: 7845
**Date**: 2019-08-01
**URL**: https://discourse.slicer.org/t/reverse-search-volume-in-sequence-volume-and-get-frame-number/7845

---

## Post #1 by @che85 (2019-08-01 21:45 UTC)

<p>Hi,</p>
<p>I got an extracted frame (volume) from a sequence and I would not like to go back and figure out which frame it originally was. Is there a way to search a sequence for a given volume and extract the original frame number?</p>
<p>Szenario A (creation):</p>
<ol>
<li>user loads a sequence into 3D Slicer</li>
<li>user extracts frame</li>
<li>user saves MRML scene</li>
<li>repeat 1-3 on hundreds of datasets</li>
</ol>
<p>Szenario B (reverse search):</p>
<ol>
<li>user loads MRML scene</li>
<li>user puts sequence and extracted frame next to each other and compares frame by frame visually</li>
</ol>
<p>I would want to automate Szenario B somehow. Is this possible?</p>
<p>Best,<br>
Christian</p>

---

## Post #2 by @lassoan (2019-08-02 03:26 UTC)

<p>This looks very similar to what is implemented in the <a href="https://github.com/SlicerIGT/UsAnnotationExport" rel="nofollow noopener">utrasound annotation export module</a>, which generates training data for deep-learning-based segmentation. Probably the same method can be used to link extracted frames to the original frames.</p>
<p>The module might be usable in your workflow as is, or with small modifications.</p>
<p><a class="mention" href="/u/ungi">@ungi</a></p>

---

## Post #3 by @ungi (2019-08-02 03:40 UTC)

<p>Yes. Look at how the SingleSliceSegmentation module in the link Andras provided. It hides the original frame number in the segmentation as a MRML node attribute. However, if you just want to compare the segmentation with the original image, there is a more convenient method that does not require a custom module. You can create another sequence and save there both the segmentation and the original image. That will be a copy, so that is not super storage efficient. But it works in Slicer as is.</p>

---

## Post #4 by @che85 (2019-08-02 14:51 UTC)

<p>Thanks for the replies.</p>
<p>I think, it’s a bit more complicated when I go back to old mrmlScenes where I only have the original sequence and an extracted frame as a scalar volume.</p>
<p>Basically, I want to look at those old cases where I don’t have any information saved anywhere about which frame was extracted.</p>

---

## Post #5 by @che85 (2019-08-02 15:22 UTC)

<p>I think another way would be to use <code>Subtract Scalar Volumes</code> with 0 interpolation iterating over every frame of the Sequence subtracting the scalar volume I am looking for.</p>
<p>The resulting volume would (if it is the frame we are looking for) have only pixel values 0.</p>
<p>This wouldn’t work though if the scalar volume was modified after extraction.</p>

---

## Post #6 by @lassoan (2019-08-02 17:28 UTC)

<p>You can compute histogram of the difference and if most of the voxels have no or small difference then most likely the volumes match.</p>

---
