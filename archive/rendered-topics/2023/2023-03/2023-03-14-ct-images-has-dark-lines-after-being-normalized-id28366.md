# CT images has dark lines after being normalized

**Topic ID**: 28366
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/ct-images-has-dark-lines-after-being-normalized/28366

---

## Post #1 by @anusree_sunilkumar (2023-03-14 03:03 UTC)

<p>I am trying to train a model for reconstruction. My CBCT dataset is of DICOM format with datatype uint16. When I normalize the volume to uint8 based on the maximum intensity of the volume, my model doesn’t give expected performance. But when I normalize each axial slices separately, my model performs better. But the images have dark lines in the middle. I understand the reason is because the middle regions are where teeth is located and since the teeth intensity are much larger compared to other regions these slices becomes dark.<br>
Does anyone have suggestions on how to solve this issue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe774d9b5900955ceac6c0cda0130f6b0d694e8b.png" data-download-href="/uploads/short-url/Aj6SLtkC5MV0HSCWag0nb3ZLOTV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe774d9b5900955ceac6c0cda0130f6b0d694e8b_2_690x128.png" alt="image" data-base62-sha1="Aj6SLtkC5MV0HSCWag0nb3ZLOTV" width="690" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe774d9b5900955ceac6c0cda0130f6b0d694e8b_2_690x128.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe774d9b5900955ceac6c0cda0130f6b0d694e8b_2_1035x192.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe774d9b5900955ceac6c0cda0130f6b0d694e8b_2_1380x256.png 2x" data-dominant-color="757575"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1616×300 43.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-03-14 14:02 UTC)

<p>Quantizing to 8 bit is not a good idea in general of course.  You are going to lose detail that may be important.</p>
<p>But also normalizing on a slice-by-slice level will change the relative intensities.  You might choose to normalize by the standard deviation over the volume instead of the max.</p>

---
