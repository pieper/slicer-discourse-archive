---
topic_id: 43824
title: "Scalar Volumes Loading As Sequences Is There A Way To Fix"
date: 2025-07-23
url: https://discourse.slicer.org/t/43824
---

# Scalar volumes loading as sequences, is there a way to fix?

**Topic ID**: 43824
**Date**: 2025-07-23
**URL**: https://discourse.slicer.org/t/scalar-volumes-loading-as-sequences-is-there-a-way-to-fix/43824

---

## Post #1 by @SegmenterSam (2025-07-23 10:22 UTC)

<p>Hi all,</p>
<p>I have a number of patients of whom I have DICOM files of T1w-MRI and rCBV maps pre-and postop. For most patients these load just fine, as scalar volumes as they should. However for some, it only gives the option to load as an Image Sequence, which leaves me with single slice with 19 iterations.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18baa1dbe9ca3ab9737c295541e5756943554aab.png" data-download-href="/uploads/short-url/3wLjEO6Gx8QvykB7AdL8L9kBoLN.png?dl=1" title="afbeelding" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18baa1dbe9ca3ab9737c295541e5756943554aab_2_690x379.png" alt="afbeelding" data-base62-sha1="3wLjEO6Gx8QvykB7AdL8L9kBoLN" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18baa1dbe9ca3ab9737c295541e5756943554aab_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18baa1dbe9ca3ab9737c295541e5756943554aab_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18baa1dbe9ca3ab9737c295541e5756943554aab.png 2x" data-dominant-color="3E3C3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">afbeelding</span><span class="informations">1050×577 24.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I open this sequence in the Sequences module, it wil let me play and it will literally just present all 19 slices in order, so the data is there… The data before importing into 3DSlicer does not look any different at all to another rCBV maps that loads just fine; a DICOM file and the folders with 19 images.</p>
<p>It seems to me that some of the data is “corrupted”, in that it thinks it is a 1 slice sequence with 19 iterations, instead of 19 slices that need to be stacked.</p>
<p>If it helps, I could make a video to explain a bit better what is going on.</p>
<p>TLDR: Some of my scalar volumes only allow loading as Image Sequence, Is there any way to edit something under the hood of this DICOM (or in 3DSlicer) that can rectify this? Thank you very much in advance.</p>

---

## Post #2 by @SegmenterSam (2025-07-23 11:36 UTC)

<p>To add, I have noticed that in properties it says that the Image Dimension is 256x256x1 times 19 (1 being the Z axis and 19 being the time axis). This is what should be 256x256x19 times 1, which it is for the ones that work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a50a77c22ed7a630ad78afca24e5ac8184c79fec.png" data-download-href="/uploads/short-url/ny1d0spiiXcE6KlUCcDbGVHb1Qo.png?dl=1" title="afbeelding" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a50a77c22ed7a630ad78afca24e5ac8184c79fec.png" alt="afbeelding" data-base62-sha1="ny1d0spiiXcE6KlUCcDbGVHb1Qo" width="517" height="105" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">afbeelding</span><span class="informations">715×147 4.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My ideal solution would be to get this to image to 256x256x19, given that I have all the data to do it…</p>

---

## Post #3 by @SegmenterSam (2025-07-23 22:02 UTC)

<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f324633002ebdcec7523348948dc3c8856e3e4ab.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4523ac1404a49454fb0ea5c77afabb7307fcabcc.jpeg" data-video-base62-sha1="yGVZ4CJCA5gf8L5sKjDQ43kxMkX.mp4">
  </div><p></p>
<p>Any ideas to get these sequenced images to stack as a scalar volume? Any ideas greatly appreciated.</p>

---

## Post #4 by @pieper (2025-07-24 06:39 UTC)

<p>There are many <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html">DICOM representations of data</a><br>
that users may want to see as volumes or sequences in Slicer.  We try to handle most of them but not all patterns are easy to detect.  The best solution would be for you to look at the headers and the <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted/DICOMPlugins">sequence and volume dicom plugin python code</a><br>
and find the patterns that apply to your data and propose extensions that would handle the data in the way you need it.  I know this may sound complicated, but if you know what the data is meant to represent and you know something about the acquisition it’s probably straightforward.</p>

---

## Post #5 by @SegmenterSam (2025-07-24 08:49 UTC)

<p>Hi Steve, thanks for your input. I’ve gotten pretty handy with basic 3DSlicer but these kind of problems still stump me. I’ll take a look at your proposed solution and let you know if I make progress!</p>

---

## Post #6 by @SegmenterSam (2025-07-29 08:19 UTC)

<p>Hello everybody.</p>
<p>For people referencing this in the future with possibly the same problem; I managed to, for a large part, get it fixed by using the the dcm2niix tool within MicroGL. I used it to convert my DICOM file into NIfFTY file format, and these .nii files load (almost) perfectly.</p>

---

## Post #7 by @cpinter (2025-07-29 14:11 UTC)

<p>For the record, have you tried selecting the appropriate DICOM loadable? Sometimes the heuristics selecting the best one makes mistakes. I mean</p>
<ul>
<li>Check the Advanced checkbox in the DICOM browser</li>
<li>Click Examine</li>
<li>See the list of the loadables</li>
<li>Ignore those that you are not interested in (sequence), and load the appropriate one (scalar volume)</li>
</ul>

---

## Post #8 by @SegmenterSam (2025-07-29 15:22 UTC)

<p>Hi Csaba,</p>
<p>Yes, the problem that I was having is that it did not even allow me to load as a Scalar Volume, it only gave me the option for an Image Sequence in that menu. So it didn’t even recognize the possibility to load as a Scalar Volume.</p>
<p>To add, even after converting to .nii, the patient positioning values in the original DICOM are apparently invalid/missing (it says this in a warning message when converting DICOM to .nii) which is the reason why it is not able to load as a volume I think.</p>
<p>TLDR: I think the positioning values in the DICOM are invalid/missing, causing the DICOM to load incorrectly, but converting to .nii format at least fixes the Scalar Volume Issue.</p>

---
