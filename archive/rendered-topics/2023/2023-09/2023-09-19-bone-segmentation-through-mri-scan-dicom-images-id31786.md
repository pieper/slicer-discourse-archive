# Bone segmentation through MRI scan dicom images

**Topic ID**: 31786
**Date**: 2023-09-19
**URL**: https://discourse.slicer.org/t/bone-segmentation-through-mri-scan-dicom-images/31786

---

## Post #1 by @Bibi_Ayisha (2023-09-19 11:13 UTC)

<p>I was provided a MRI scan of a patient. I have seen different series in the data and the data does not load completely. If I load all the files together it is not showing images properly. Is the issue related to dicom images or this can be fixed? I am new to 3D slicer. Series are in image 1.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd50a39be748f883f29a2c5fd66bacc37a231782.png" data-download-href="/uploads/short-url/A8VzfhVhPQjAVPl5UfWl7GC2Aj8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd50a39be748f883f29a2c5fd66bacc37a231782_2_690x338.png" alt="image" data-base62-sha1="A8VzfhVhPQjAVPl5UfWl7GC2Aj8" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd50a39be748f883f29a2c5fd66bacc37a231782_2_690x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd50a39be748f883f29a2c5fd66bacc37a231782_2_1035x507.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd50a39be748f883f29a2c5fd66bacc37a231782_2_1380x676.png 2x" data-dominant-color="C2DCED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1514×743 28.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If i load only one series this is what i get but in this way i can do the segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a2dc9a2b3844240ccd5470bb7e9ae4919e65ecf.jpeg" data-download-href="/uploads/short-url/cRL4soNG1vYkTCZE2m2F5tydhMj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a2dc9a2b3844240ccd5470bb7e9ae4919e65ecf_2_690x431.jpeg" alt="image" data-base62-sha1="cRL4soNG1vYkTCZE2m2F5tydhMj" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a2dc9a2b3844240ccd5470bb7e9ae4919e65ecf_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a2dc9a2b3844240ccd5470bb7e9ae4919e65ecf_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a2dc9a2b3844240ccd5470bb7e9ae4919e65ecf_2_1380x862.jpeg 2x" data-dominant-color="4E4E5B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1461×913 67.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This appears if i open all the files altogether:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b124341bd1f983e9e61e770dee0a9703c86ac028.jpeg" data-download-href="/uploads/short-url/ph44PTwWug6cVyTz6t5iDyHbwjS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b124341bd1f983e9e61e770dee0a9703c86ac028_2_690x405.jpeg" alt="image" data-base62-sha1="ph44PTwWug6cVyTz6t5iDyHbwjS" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b124341bd1f983e9e61e770dee0a9703c86ac028_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b124341bd1f983e9e61e770dee0a9703c86ac028_2_1035x607.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b124341bd1f983e9e61e770dee0a9703c86ac028_2_1380x810.jpeg 2x" data-dominant-color="42414D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1521×893 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-09-19 20:40 UTC)

<p>You might try turning on advanced mode and picking different plugins to load.  There can be a lot of complexity about when collections of instances should be grouped as a volume.  If it’s still an issue maybe you can share a deidentified dataset that illustrates the issue maybe someone can have a look.</p>

---

## Post #3 by @lassoan (2023-09-21 13:17 UTC)

<aside class="quote no-group" data-username="Bibi_Ayisha" data-post="1" data-topic="31786">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bibi_ayisha/48/65979_2.png" class="avatar"> Bibi_Ayisha:</div>
<blockquote>
<p>This appears if i open all the files altogether:</p>
</blockquote>
</aside>
<p>What do you mean by this? How did you load all files altogether (using Data window or the DICOM module, what options did you select)?</p>

---
