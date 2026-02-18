# Dicom File Loading Spacing

**Topic ID**: 5469
**Date**: 2019-01-22
**URL**: https://discourse.slicer.org/t/dicom-file-loading-spacing/5469

---

## Post #1 by @epdawson (2019-01-22 18:31 UTC)

<p>Two Questions:</p>
<ol>
<li>
<p>I have dicom files from MRI which have all necessary metadata, however, only some of the files are consecutive, while others are skipped in between (i.e Dicom 001, Dicom 002, Dicom 007, etc.) The ImagePositionPatient says the spacing is .3mm, and from the 43 files I have, the total length is ~55mm due to skipped slices. However, when loading these Dicom files in, it truncates all the slices so that the first one is positioned correctly, but then each following slice is just .3mm away, even though there are some instances where 5mm should be skipped based on the ImagePositionPatient data. This results in the total length only being 42*.3mm = ~12mm. Is there a way for Slicer to obey this metadata header for all slices so spacing is preserved?</p>
</li>
<li>
<p>For the length of a volume that was created via segmentation, it is possible to get the volume of each slice individually after the model is created? I am interested in the areas of all the segmented slices, but have only been able to do this by loading in a single slice at a time.</p>
</li>
</ol>
<p>Thanks for any help on either of these!</p>
<p>Eli</p>

---

## Post #2 by @pieper (2019-01-22 20:13 UTC)

<p>Hi -</p>
<p>For number question 1, you can turn on geometry regularization and it should automatically handle the missing slices:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06ad143ea55ec65ce5e63e64b795d43fa320e8d7.png" data-download-href="/uploads/short-url/X3Gtj0isM7wDzKlsF9MwIkWlr9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06ad143ea55ec65ce5e63e64b795d43fa320e8d7_2_690x208.png" alt="image" data-base62-sha1="X3Gtj0isM7wDzKlsF9MwIkWlr9" width="690" height="208" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06ad143ea55ec65ce5e63e64b795d43fa320e8d7_2_690x208.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06ad143ea55ec65ce5e63e64b795d43fa320e8d7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06ad143ea55ec65ce5e63e64b795d43fa320e8d7.png 2x" data-dominant-color="EBECEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">887×268 57.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For question 2 I can’t think of an easy way to do this.  A little python script would be the easiest.  Or do it manually to create new segments per slice (maybe using the segment overwrite options in the Segment Editor.</p>

---

## Post #3 by @lassoan (2019-01-22 21:04 UTC)

<aside class="quote no-group" data-username="epdawson" data-post="1" data-topic="5469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/ebca7d/48.png" class="avatar"> epdawson:</div>
<blockquote>
<p>For the length of a volume that was created via segmentation, it is possible to get the volume of each slice individually after the model is created? I am interested in the areas of all the segmented slices, but have only been able to do this by loading in a single slice at a time.</p>
</blockquote>
</aside>
<p>See this topic: <a href="https://discourse.slicer.org/t/calculating-simple-areas/5435" class="inline-onebox">Calculating Simple Areas</a></p>

---

## Post #4 by @epdawson (2019-01-23 19:52 UTC)

<p>Hi Steve and Andras,</p>
<p>Thanks for the responses.</p>
<p>When turning on geometry regularization, the slices are now placed in the correct location. However, when segmenting, I am unable to add masking to any slices that are past the max z location of the previously truncated series. The truncated z<br>
location range went from ~ -4 —&gt; 7.6mm with a thickness of .3mm, while the actual series should be from -4 —&gt; 50mm with a lot being skipped. With geometry regularization turned on, I am only able to add masking to slices up to 7.6mm. The performance of the<br>
program is also drastically slowed. Any ideas on what is going on here?</p>
<p>I am using the latest stable build on Mac as of today.</p>
<p>Thanks,</p>
<p>Eli</p>

---

## Post #5 by @lassoan (2019-01-25 03:34 UTC)

<p>Probably default segmentation labelmap geometry is not computed optimally for non-linearly transformed images. You can adjust it by clicking the button next to the master volume selector (see <a href="https://discourse.slicer.org/t/segment-has-invisible-bounds-smaller-than-master-volume/4676/6?u=lassoan">this post</a> for some instructions).</p>
<p>Or, you can harden the regularization transform using Transforms module.</p>

---

## Post #6 by @Davide_Punzo (2023-11-13 08:31 UTC)

<p>NOTE: Support for regularization transform hardening in DICOM Scalar plugin has been added. See <a href="https://discourse.slicer.org/t/enh-support-regularization-transform-hardening-in-dicom-scalar-plugin/32772">link</a>.</p>

---
