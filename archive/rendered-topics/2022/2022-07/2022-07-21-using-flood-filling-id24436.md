---
topic_id: 24436
title: "Using Flood Filling"
date: 2022-07-21
url: https://discourse.slicer.org/t/24436
---

# Using flood filling

**Topic ID**: 24436
**Date**: 2022-07-21
**URL**: https://discourse.slicer.org/t/using-flood-filling/24436

---

## Post #1 by @harrykwon0524 (2022-07-21 20:06 UTC)

<p>hi i am a newbie using the 3dslicer program and had some questions along the way. I am trying to segment the vessels from the brain and was wondering how to use the floor filling. Is it possible to click the vessels on the very left image and try to segment the vessels? Thank you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59bee374f7b210354ee545af260eea283dda0c56.jpeg" data-download-href="/uploads/short-url/cNVteQ6yutwPtlC2UHgZg6Ml5BQ.jpeg?dl=1" title="Screenshot from 2022-07-21 14-51-17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59bee374f7b210354ee545af260eea283dda0c56_2_690x388.jpeg" alt="Screenshot from 2022-07-21 14-51-17" data-base62-sha1="cNVteQ6yutwPtlC2UHgZg6Ml5BQ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59bee374f7b210354ee545af260eea283dda0c56_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59bee374f7b210354ee545af260eea283dda0c56_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59bee374f7b210354ee545af260eea283dda0c56_2_1380x776.jpeg 2x" data-dominant-color="9091A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-07-21 14-51-17</span><span class="informations">1920×1080 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-07-23 08:28 UTC)

<p>Flood filling is rarely effective for vessel segmentation. The vessels are usually too thin and often the intensity range is not distinctive enough for such simple region growing method to work reliably.</p>
<p>Due to the window/level setting you have set in the slice view everything appears to be too bright, so it is hard to tell how the vessels look like (how different is their intensity compared to surrounding areas). Could you <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level">adjust the window/level</a> to make the vessels stand out as much as possible and post another screenshot, or even better share an example data set (upload to onedrive/dropbox/google drive and post the link here)?</p>

---

## Post #3 by @harrykwon0524 (2022-07-25 16:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be0c454b42e19c9ceec785143e27f5b99e8d5b18.jpeg" data-download-href="/uploads/short-url/r7f0zltyXuR9G9YuT2nkt9cIZja.jpeg?dl=1" title="Screenshot from 2022-07-25 12-48-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be0c454b42e19c9ceec785143e27f5b99e8d5b18_2_690x388.jpeg" alt="Screenshot from 2022-07-25 12-48-16" data-base62-sha1="r7f0zltyXuR9G9YuT2nkt9cIZja" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be0c454b42e19c9ceec785143e27f5b99e8d5b18_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be0c454b42e19c9ceec785143e27f5b99e8d5b18_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be0c454b42e19c9ceec785143e27f5b99e8d5b18_2_1380x776.jpeg 2x" data-dominant-color="81829F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-07-25 12-48-16</span><span class="informations">1920×1080 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Will this screenshot be enough to tell?</p>

---

## Post #4 by @harrykwon0524 (2022-07-26 19:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7231e1960bd4597618e44b0c23c597bbbac379dd.jpeg" data-download-href="/uploads/short-url/gidiHlMKa5oddiPAuiGqSVbcoEt.jpeg?dl=1" title="Screenshot from 2022-07-26 15-23-59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7231e1960bd4597618e44b0c23c597bbbac379dd_2_690x388.jpeg" alt="Screenshot from 2022-07-26 15-23-59" data-base62-sha1="gidiHlMKa5oddiPAuiGqSVbcoEt" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7231e1960bd4597618e44b0c23c597bbbac379dd_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7231e1960bd4597618e44b0c23c597bbbac379dd_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7231e1960bd4597618e44b0c23c597bbbac379dd_2_1380x776.jpeg 2x" data-dominant-color="6B6C80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-07-26 15-23-59</span><span class="informations">1920×1080 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2022-07-26 19:27 UTC)

<p>These screenshots are useful. It seems that you can segment the vessels using simple thresholding (<code>Threshold</code> effect in <code>Segment Editor</code> module).</p>

---

## Post #6 by @harrykwon0524 (2022-07-27 15:09 UTC)

<p>Is there any advanced methods on segmenting the vessels? Like using simple segmentation and other methods together to segment the brain vessels more accurately?</p>

---

## Post #7 by @lassoan (2022-08-02 11:08 UTC)

<p>You can try to improve vessel contrast using Vesselness Filtering module in VMTK extension. If you want to segment small vessels then it can help if the image is resampled to have smaller voxels (for example, using Crop Volume module).</p>

---

## Post #8 by @harrykwon0524 (2022-08-03 19:00 UTC)

<p>I did try using vesselness filtering, but the 3d slicer gets automatically stopped and breaks eventually. Is it because I have not set the seed point right?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0c137a09a84628c29eb7dbcd47c6a2692102926.jpeg" data-download-href="/uploads/short-url/w4gV0Es5VVDeWBHgwI3BwT0eriK.jpeg?dl=1" title="Screenshot from 2022-08-03 14-59-53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c137a09a84628c29eb7dbcd47c6a2692102926_2_690x388.jpeg" alt="Screenshot from 2022-08-03 14-59-53" data-base62-sha1="w4gV0Es5VVDeWBHgwI3BwT0eriK" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c137a09a84628c29eb7dbcd47c6a2692102926_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c137a09a84628c29eb7dbcd47c6a2692102926_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c137a09a84628c29eb7dbcd47c6a2692102926_2_1380x776.jpeg 2x" data-dominant-color="787990"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-08-03 14-59-53</span><span class="informations">1920×1080 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @harrykwon0524 (2022-08-04 19:42 UTC)

<p>I did manage to create the segmentation result by using vesselness filtering and had questions along the way</p>
<ol>
<li>How can I save the segmentation result?</li>
<li>Will adding more seed points in the vessels result in creating more sophisticated vessel segmentation result?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b366b10c4536ca5f4e2f08251aeff816082ee7bd.jpeg" data-download-href="/uploads/short-url/pB3tWoRz9xS8UKfVgx7d6L75YTj.jpeg?dl=1" title="Screenshot from 2022-08-04 15-42-08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b366b10c4536ca5f4e2f08251aeff816082ee7bd_2_690x388.jpeg" alt="Screenshot from 2022-08-04 15-42-08" data-base62-sha1="pB3tWoRz9xS8UKfVgx7d6L75YTj" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b366b10c4536ca5f4e2f08251aeff816082ee7bd_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b366b10c4536ca5f4e2f08251aeff816082ee7bd_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b366b10c4536ca5f4e2f08251aeff816082ee7bd_2_1380x776.jpeg 2x" data-dominant-color="777189"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-08-04 15-42-08</span><span class="informations">1920×1080 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>

---
