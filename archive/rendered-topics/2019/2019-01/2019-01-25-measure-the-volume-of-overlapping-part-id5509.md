# Measure the volume of overlapping part

**Topic ID**: 5509
**Date**: 2019-01-25
**URL**: https://discourse.slicer.org/t/measure-the-volume-of-overlapping-part/5509

---

## Post #1 by @Hyeon (2019-01-25 14:05 UTC)

<p>[Environment]<br>
Slicer 4.10.1/Win10</p>
<p>Hello. I need a help.</p>
<p>I have made a 3D model of bone using thrashold paint function in editor module.<br>
I want to create the cylinder model, and put it into the model of bone I made, and measure the volume of the overlapping part like pedicle screw simulator (<a href="https://github.com/smclach/PedicleScrewSimulator" rel="nofollow noopener">https://github.com/smclach/PedicleScrewSimulator</a>).</p>
<p>I’ve attempt to insert screws function in pedicle screw simulator module, however, it does not work as I wanted due to I’ve made a other bone model, not spine.</p>
<p>Is there any module which could make 3D cylinder shape over 3d reconstructed bone model or measure the volume of overlapping segment?</p>

---

## Post #2 by @lassoan (2019-01-31 02:27 UTC)

<p>It should be possible to make PedicleScrewSimulator work for any kind of bone, maybe with slight modifications.</p>
<p>You can use Segment Editor module’s “Logical operators” effect to create a segment from overlap of two segments. If you have models, create a segmentation node and import the models into it using Segmentations module.</p>

---

## Post #4 by @Hyeon (2019-02-01 08:11 UTC)

<p>Thank you prof. lassoan. However, my problem is not still solved.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a73b0e000ee192e8abd6b18be3cdda41f7f25446.jpeg" data-download-href="/uploads/short-url/nRogdMQ5o5M0kt0DU7H5QTueK6a.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a73b0e000ee192e8abd6b18be3cdda41f7f25446_2_690x431.jpeg" alt="1" data-base62-sha1="nRogdMQ5o5M0kt0DU7H5QTueK6a" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a73b0e000ee192e8abd6b18be3cdda41f7f25446_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a73b0e000ee192e8abd6b18be3cdda41f7f25446_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a73b0e000ee192e8abd6b18be3cdda41f7f25446_2_1380x862.jpeg 2x" data-dominant-color="A08E9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1456×910 76.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I have modified the PedicleScrewSimulator. And I have succeeded in setting the screw insertion as shown in the attached figure. However, I can not actually measure the grade of screw in the next step (grade step).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bf9cf777fc7b35ef860cf1ca2635d84c9c0cc37.jpeg" data-download-href="/uploads/short-url/mfPdU5OBBRBKX9NQgpqg4oQEnIP.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9bf9cf777fc7b35ef860cf1ca2635d84c9c0cc37_2_690x438.jpeg" alt="2" data-base62-sha1="mfPdU5OBBRBKX9NQgpqg4oQEnIP" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9bf9cf777fc7b35ef860cf1ca2635d84c9c0cc37_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9bf9cf777fc7b35ef860cf1ca2635d84c9c0cc37_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9bf9cf777fc7b35ef860cf1ca2635d84c9c0cc37_2_1380x876.jpeg 2x" data-dominant-color="AD9D98"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1456×925 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This seems to be becaused I used 3d recontructed bone model (.vtk) rather than actual dicom file. However, when define ROI using a DICOM file, the scapula is obscured by humerus, and can not place the correct screw insertion point.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b460a962114c243e7a61c09de82b59cee1301da9.jpeg" data-download-href="/uploads/short-url/pJH2yOSqKsmenG2i0CFVWjEuE3v.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b460a962114c243e7a61c09de82b59cee1301da9_2_690x438.jpeg" alt="3" data-base62-sha1="pJH2yOSqKsmenG2i0CFVWjEuE3v" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b460a962114c243e7a61c09de82b59cee1301da9_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b460a962114c243e7a61c09de82b59cee1301da9_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b460a962114c243e7a61c09de82b59cee1301da9_2_1380x876.jpeg 2x" data-dominant-color="A995A1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1456×925 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Furthermore, I just want to measure the volume of overlapping part between reconstructed bone model (scapula.vtk which I made) and screw model (which included in PedicleScrewSimulator extension).</p>
<p>Is there a way to measure the volume of overlapping part between .vtk format 3D objects?</p>

---

## Post #5 by @lassoan (2019-02-02 01:06 UTC)

<p>You can position the screw model using a transform (you can display a box that you can translate and rotate), import into segmentation node, and use Logical operators effect to get the volume of the screw inside the bone.</p>
<p>Note that the screw grading in PedicleScrewSimulator is more accurate, as it also takes into account the bone density.</p>

---
