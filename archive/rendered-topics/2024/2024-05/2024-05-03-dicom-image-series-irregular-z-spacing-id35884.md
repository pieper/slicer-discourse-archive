---
topic_id: 35884
title: "Dicom Image Series Irregular Z Spacing"
date: 2024-05-03
url: https://discourse.slicer.org/t/35884
---

# DICOM image series irregular z spacing

**Topic ID**: 35884
**Date**: 2024-05-03
**URL**: https://discourse.slicer.org/t/dicom-image-series-irregular-z-spacing/35884

---

## Post #1 by @chz31 (2024-05-03 03:59 UTC)

<p>Hi,</p>
<p>This question is extended from this post by <a class="mention" href="/u/paleomariomm">@paleomariomm</a> : <a href="https://discourse.slicer.org/t/load-specific-dicom-data-with-python-in-slicer-5-6-1/35314/4" class="inline-onebox">Load specific DICOM Data with Python in Slicer 5.6.1 - #4 by lassoan</a>.</p>
<p>The DICOM dataset is here: <a href="https://www.morphosource.org/concern/media/000058941?locale=en" rel="noopener nofollow ugc">https://www.morphosource.org/concern/media/000058941?locale=en</a>.</p>
<p>Basically, the z spacing between slices are quite irregular, so when it was loaded, Slicer gave out a warning <code>0.6 spacing was expected, 0.5 spacing was found between files</code> .</p>
<p>Assuming the 0.6 spacing between slices is correct, I used a dumb way to correct it because I could not find a better way online to correct the z spacing. Basically, I loaded <code>slice i</code> as ds0 and <code>slice i +1</code>  and ds1. I then update the z spacing of <code>slice i+1</code> as the (z of  <code>slice i</code> - 0.6) using <code>ImagePositionPatient[2]</code>:</p>
<p><code>ds1.ImagePositionPatient[2] = ds0.ImagePositionPatient[2] - 0.6</code></p>
<p>The python snippet is here: <a href="https://github.com/chz31/test/blob/main/test_py_dcm_2.py" class="inline-onebox" rel="noopener nofollow ugc">test/test_py_dcm_2.py at main · chz31/test · GitHub</a>. I also manually assigned a big space for slice 5, 105, and 205 according to the values of the space from the original dataset. I guess the skull was scanned in three separate sections then concatenate with each other since it is too large.</p>
<p>I printed out <code>spacing_list</code> to verify that the z spacing between slices is updated to 0.6 uniformly other than the large gaps at slice 5, 105, and 205. However, when I loaded the updated dicom to Slicer, I got more errors:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acafece1174ddb484bbc301772a555bda1eab39c.png" data-download-href="/uploads/short-url/oDF2FSZgDIm8WfrHk1snddVHVi4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acafece1174ddb484bbc301772a555bda1eab39c_2_690x140.png" alt="image" data-base62-sha1="oDF2FSZgDIm8WfrHk1snddVHVi4" width="690" height="140" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acafece1174ddb484bbc301772a555bda1eab39c_2_690x140.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acafece1174ddb484bbc301772a555bda1eab39c_2_1035x210.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acafece1174ddb484bbc301772a555bda1eab39c_2_1380x280.png 2x" data-dominant-color="E9E9E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2271×463 55.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m new to dicom. I believe dicom data is not loaded following the alphabetic order of the dcm? The warning even suggested 0.3 andd 0.1 spacing was found. Could anyone give me some suggestions? Thanks!</p>

---

## Post #2 by @pieper (2024-05-04 14:25 UTC)

<p>You can read about how Slicer handles dicom with irregular spacing <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0">in this commit message</a> and the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#basic-usage">module settings</a>.  Basically Slicer will create a grid transform to position the volume according to the <code>ImagePositionPatient</code> and <code>ImageOrientationPatient</code> and it should handle exactly the situation you describe.  If you harden the transform, you’ll get a volume with equally spaced slices suitable for volume rendering and other tasks.  The code that implements this <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py">is here</a>.</p>

---

## Post #3 by @chz31 (2024-05-06 19:38 UTC)

<p>Thank you! I’m playing with the code implements to see if I can use it to set a rule.</p>
<p>Meanwhile, just a naive question. I just loaded data that used the grid transform to change the volume with equally z space as 0.58, but the correct spacing should be 0.6. Can I just modify the z spacing in the Volumes module in 0.6? Or should I modify the target corners acquired from <a href="https://github.com/Slicer/Slicer/blob/7cef1fff130116376f81882470bd314c22199fdf/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L817C1-L818C66" rel="noopener nofollow ugc">sliceCornersFromDICOM</a>?</p>

---

## Post #4 by @pieper (2024-05-06 21:10 UTC)

<p>Hi <a class="mention" href="/u/chz31">@chz31</a> -</p>
<p>Since you are very familiar with this dataset by now it would be great if you could print out these corner locations and confirm that the dicom ones correspond with the ImagePositionPatient[2] values you set in your script and then look at the bounds of the resulting volume.  It’s possible that the hardening step is using a different sampling grid than the original dicoms and that 0.58 is correct in the context of that grid (thus changing to 0.6 would change the aspect ratio and distort the volume).  We might need a different sampling grid if you want 0.6 slice spacing.</p>

---

## Post #5 by @chz31 (2024-05-07 21:46 UTC)

<p>Thanks! <a class="mention" href="/u/pieper">@pieper</a></p>
<p>The z positions of the raw images (raw_corners) &amp; the ones I set up manually in my script are quite different from the ones I got from both <a href="https://github.com/Slicer/Slicer/blob/7cef1fff130116376f81882470bd314c22199fdf/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L817C4-L818C66" rel="noopener nofollow ugc">originalCorners and targetCorners</a> before and after grid transforms.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab26e09cb8003cd9a85435b524923f81294c7356.png" data-download-href="/uploads/short-url/oq4WoyQuXwbAu0kujk76YX2yNbU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab26e09cb8003cd9a85435b524923f81294c7356.png" alt="image" data-base62-sha1="oq4WoyQuXwbAu0kujk76YX2yNbU" width="345" height="48" data-dominant-color="F4F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×128 3.55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c5901eefe0a34ff493b84be0bf4cdc6fb8138a8.png" data-download-href="/uploads/short-url/hK1U3vvHb5vmuchbAMu6ehyl9zO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c5901eefe0a34ff493b84be0bf4cdc6fb8138a8.png" alt="image" data-base62-sha1="hK1U3vvHb5vmuchbAMu6ehyl9zO" width="345" height="221" data-dominant-color="F6F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">934×601 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the raw slices, there are large gaps between slices 5 and 6, slices 105 and 106, and slices 205 and 206 (-61, -116 and -116 respectively). When it was loaded, the z spacing between adjacent slices was all updated to 0.58:</p>
<p>This is indeed a very weird dataset. I felt like the scans were acquired 3 separate times and concatenated together. I suspected the slice below might show the poor concatenation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/959a865731795fa61480eb83b4ee07a9cc9f7142.jpeg" data-download-href="/uploads/short-url/llsd4DTz11Jauot2Gpy8l13bD6W.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/959a865731795fa61480eb83b4ee07a9cc9f7142_2_345x182.jpeg" alt="image" data-base62-sha1="llsd4DTz11Jauot2Gpy8l13bD6W" width="345" height="182" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/959a865731795fa61480eb83b4ee07a9cc9f7142_2_345x182.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/959a865731795fa61480eb83b4ee07a9cc9f7142_2_517x273.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/959a865731795fa61480eb83b4ee07a9cc9f7142_2_690x364.jpeg 2x" data-dominant-color="161515"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1140×604 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2024-05-08 12:58 UTC)

<aside class="quote no-group" data-username="chz31" data-post="5" data-topic="35884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chz31/48/77363_2.png" class="avatar"> chz31:</div>
<blockquote>
<p>might show the poor concatenation</p>
</blockquote>
</aside>
<p>I’m not sure - to me that looks like the skull was glued back together.  If it were a concatenation issue I’d expect a sharper discontinuity.</p>
<p>In the code you linked, <code>self.sliceCornersFromDICOM(volumeNode)</code> would be the list of per-slice corners in RAS where, if there is no rotation in the image orientation, the <code>S</code> value should match what you put in the <code>ImagePositionPatient</code>.  The grid transform should be the mapping of the regularly-spaced image data such that each slice is moved to the correct spot as defined by the dicom tags by stretching the volume in the places where the spacing is larger.</p>

---

## Post #7 by @muratmaga (2024-05-08 19:01 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="35884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’m not sure - to me that looks like the skull was glued back together</p>
</blockquote>
</aside>
<p>Exactly! Some of these specimens have cut into calvaria (and old practice predating mCT to see internal structures). Because the bone is ground, they will not line up correctly. That’s probably a some sort of a clay or glue to keep the calvaria in place during the scan.</p>

---

## Post #8 by @chz31 (2024-05-09 04:58 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> ! I’ll take a bit more time to play with the data.</p>

---
