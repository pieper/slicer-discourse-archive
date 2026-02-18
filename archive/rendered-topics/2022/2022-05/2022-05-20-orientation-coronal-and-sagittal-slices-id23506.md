# Orientation coronal and sagittal slices

**Topic ID**: 23506
**Date**: 2022-05-20
**URL**: https://discourse.slicer.org/t/orientation-coronal-and-sagittal-slices/23506

---

## Post #1 by @anon29823344 (2022-05-20 11:34 UTC)

<p>Hello everybody.</p>
<p>I have a question about how Slicer displays data from a DICOM. Below I show you two screenshots of the segmentation of two different samples. If you look closely, the orientation of the coronal and sagittal slices is oriented differently. Can anyone tell me the reason for this situation? Why is Slicer not always able to display data in the same orientation? Is there a field in the DICOM standard that indicates information about this (I couldn’t find the correct label, if exists)? 3D reconstructions also come out flipped, something that also happens in output STLs.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b794eccd60004025200545e35760995cc1d98d4.jpeg" data-download-href="/uploads/short-url/hCiD2oFd9lbWXVAB3PLnSwAfWxC.jpeg?dl=1" title="33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b794eccd60004025200545e35760995cc1d98d4_2_655x500.jpeg" alt="33" data-base62-sha1="hCiD2oFd9lbWXVAB3PLnSwAfWxC" width="655" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b794eccd60004025200545e35760995cc1d98d4_2_655x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b794eccd60004025200545e35760995cc1d98d4_2_982x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b794eccd60004025200545e35760995cc1d98d4.jpeg 2x" data-dominant-color="564149"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">33</span><span class="informations">1212×924 88.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4608d14c39a89acc9f44743b3d499ef82529bbb.jpeg" data-download-href="/uploads/short-url/pJGNSk1esUj1WoW5jtawmCh8NXt.jpeg?dl=1" title="51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4608d14c39a89acc9f44743b3d499ef82529bbb.jpeg" alt="51" data-base62-sha1="pJGNSk1esUj1WoW5jtawmCh8NXt" width="690" height="495" data-dominant-color="513C43"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">51</span><span class="informations">1048×753 62.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2022-05-20 14:45 UTC)

<p>This is due to the orientation of the patient with respect to the scanner.  If you want to normalize it you can either adjust the view using the <a href="https://github.com/SlicerDMRI/SlicerDMRI/commit/717e4e7158d8cea3657c6fe74597dbcfaeaca047">Reformat</a> option or apply a <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html">Transform</a> to the data to put it in a desired orientation.</p>
<p>Regarding the flipping of the STL output, probably you need to pay attention to the Coordinate system option when using the Export to files option of the Segmentations module.</p>

---
