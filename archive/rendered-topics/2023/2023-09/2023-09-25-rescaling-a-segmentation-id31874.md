# Rescaling a segmentation

**Topic ID**: 31874
**Date**: 2023-09-25
**URL**: https://discourse.slicer.org/t/rescaling-a-segmentation/31874

---

## Post #1 by @Windy (2023-09-25 02:13 UTC)

<p>I have a volume that is 15.44 um isotropic. When I loaded it into the slicer and segmented it, I did not know that the Slicer loaded it as a 1mm volume. Now I figured out the measurements are wrong. When I load the correct scale volume to Slicer and try to overlay the segment onto it, I cannot see the segments. How can I handle this without re-segmenting the whole thing again?</p>

---

## Post #2 by @muratmaga (2023-09-25 03:30 UTC)

<p>2D formats do not have way to store the voxel dimensions, so when you read the image sequence into Slicer, Slicer simply reports what’s in the file, often the default 1mm.</p>
<p>if you are working with microCT data, you should look into SlicerMorph extension, and particularly its <code>ImageStacks</code> module, which helps to avoid this type of issues (you can manually edit the image spacing at the time of import).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f0ad3c94357ab2d2b6564c32169777c91976d5d.png" data-download-href="/uploads/short-url/kpptulhcNzvftMIMsWV1g03TvwF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f0ad3c94357ab2d2b6564c32169777c91976d5d_2_690x443.png" alt="image" data-base62-sha1="kpptulhcNzvftMIMsWV1g03TvwF" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f0ad3c94357ab2d2b6564c32169777c91976d5d_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f0ad3c94357ab2d2b6564c32169777c91976d5d_2_1035x664.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f0ad3c94357ab2d2b6564c32169777c91976d5d_2_1380x886.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1396×898 74.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It also allows many other features such as importing sub-regions of the dataset, while preserving their spatial relationships.</p>
<p>If you want to correct the spacing, you should do it both for segmentaiton and the original volume. Original volume is easy, go to Volumes module and enter the correct spacing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e69cf7c5111feb82a00eb981e1a8ad5e321abd2.png" data-download-href="/uploads/short-url/fKLdCrVzFBN0y0bcz9O1kSlicts.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e69cf7c5111feb82a00eb981e1a8ad5e321abd2_2_690x270.png" alt="image" data-base62-sha1="fKLdCrVzFBN0y0bcz9O1kSlicts" width="690" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e69cf7c5111feb82a00eb981e1a8ad5e321abd2_2_690x270.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e69cf7c5111feb82a00eb981e1a8ad5e321abd2_2_1035x405.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e69cf7c5111feb82a00eb981e1a8ad5e321abd2_2_1380x540.png 2x" data-dominant-color="ECEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1384×542 38.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For segmentation, you need to first export it as a label map. Go to the <code>segmentations</code> module and find the export/import tab, and then export it as a labelmap. Then you can use the volumes module to edit the image spacing of the new labelmap, and then reimport it as a segmentation.</p>
<p>Setting the correct spacing at the time of import, or editing prior to segmentation will avoid issues like this.</p>

---

## Post #3 by @Windy (2023-09-26 00:55 UTC)

<p>Thank you. This worked <img src="https://emoji.discourse-cdn.com/twitter/star_struck.png?v=12" title=":star_struck:" class="emoji" alt=":star_struck:" loading="lazy" width="20" height="20"></p>

---
