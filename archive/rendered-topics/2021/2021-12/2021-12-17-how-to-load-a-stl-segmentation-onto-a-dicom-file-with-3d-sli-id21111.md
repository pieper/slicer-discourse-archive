---
topic_id: 21111
title: "How To Load A Stl Segmentation Onto A Dicom File With 3D Sli"
date: 2021-12-17
url: https://discourse.slicer.org/t/21111
---

# How to load a .stl segmentation onto a DICOM file with 3D slicer?

**Topic ID**: 21111
**Date**: 2021-12-17
**URL**: https://discourse.slicer.org/t/how-to-load-a-stl-segmentation-onto-a-dicom-file-with-3d-slicer/21111

---

## Post #1 by @Callas (2021-12-17 12:23 UTC)

<p>Hello,</p>
<p>I am quite new to 3D slicer and I have an issue loading a .stl format segmentation onto a DICOM file.<br>
I have the DICOM file (which is a stack of images from a MRI image) and a .stl segmentation. I would like to load the segmentation onto the MRI image, but the segmentation only appears in on the top right corner, but not overlaid on the MR images (please see screenshot). Is there a way to see the segmented volume on the MR image?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b21389e715420c5e22a1aae49ab1357200cd81dc.jpeg" data-download-href="/uploads/short-url/ppkQLUwrI3gUM0SVQfqomqOBy0s.jpeg?dl=1" title="3DSlicer_Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b21389e715420c5e22a1aae49ab1357200cd81dc_2_690x353.jpeg" alt="3DSlicer_Screenshot" data-base62-sha1="ppkQLUwrI3gUM0SVQfqomqOBy0s" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b21389e715420c5e22a1aae49ab1357200cd81dc_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b21389e715420c5e22a1aae49ab1357200cd81dc_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b21389e715420c5e22a1aae49ab1357200cd81dc.jpeg 2x" data-dominant-color="A4A4A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3DSlicer_Screenshot</span><span class="informations">1059×542 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you for the reply.</p>

---

## Post #2 by @DNeil (2021-12-17 12:43 UTC)

<p>Hello!</p>
<p>yes there is:<br>
your STL file will be classified as a model.<br>
Navigate to the model module, click on your model<br>
scroll down where you will find slice display and check ‘visible’.<br>
That should do the trick.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3a46002352f389420d356409e776a7338bff40a.jpeg" data-download-href="/uploads/short-url/yLmce3nnfZ6wEgzSvnQy9KvgLdU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3a46002352f389420d356409e776a7338bff40a_2_690x416.jpeg" alt="image" data-base62-sha1="yLmce3nnfZ6wEgzSvnQy9KvgLdU" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3a46002352f389420d356409e776a7338bff40a_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3a46002352f389420d356409e776a7338bff40a_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3a46002352f389420d356409e776a7338bff40a_2_1380x832.jpeg 2x" data-dominant-color="35373C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1159 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af2e66b8ab05bc740852a256f9344f7cd11542d8.jpeg" data-download-href="/uploads/short-url/oZIYeFR0EyDz83TURr4YIGTvV7a.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af2e66b8ab05bc740852a256f9344f7cd11542d8_2_690x416.jpeg" alt="image" data-base62-sha1="oZIYeFR0EyDz83TURr4YIGTvV7a" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af2e66b8ab05bc740852a256f9344f7cd11542d8_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af2e66b8ab05bc740852a256f9344f7cd11542d8_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af2e66b8ab05bc740852a256f9344f7cd11542d8_2_1380x832.jpeg 2x" data-dominant-color="35373C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1159 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
