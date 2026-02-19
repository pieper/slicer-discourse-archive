---
topic_id: 45271
title: "Can Not Use Volume Rendering For Mri Data Shows Only One Sli"
date: 2025-11-29
url: https://discourse.slicer.org/t/45271
---

# Can not use volume rendering for MRI data, shows only one slice

**Topic ID**: 45271
**Date**: 2025-11-29
**URL**: https://discourse.slicer.org/t/can-not-use-volume-rendering-for-mri-data-shows-only-one-slice/45271

---

## Post #1 by @Felix_Jannan (2025-11-29 01:37 UTC)

<p>Hello,</p>
<p>I am quite new to the topic of 3D-reconstruction and imaging but I am trying to learn it for my scientific work. I recently ran into a problem with MRI data, I usually use the program for 3D Models with CT data, it works fine, just load the image sequence with the import dicom files button and everything works. Sadly it just doesnt work with MRI Data and i cant figure it out. If i try to load the volume it just shows one Slice and the other planes are really thin. The error log just says that it could not get the dicom files position.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f64679bbf2861bb4af337e5caca221b2c44d4033.png" data-download-href="/uploads/short-url/z8ErX2Rt6z5yT7oZtM9epBXfAwb.png?dl=1" title="Screenshot_89" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f64679bbf2861bb4af337e5caca221b2c44d4033_2_690x392.png" alt="Screenshot_89" data-base62-sha1="z8ErX2Rt6z5yT7oZtM9epBXfAwb" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f64679bbf2861bb4af337e5caca221b2c44d4033_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f64679bbf2861bb4af337e5caca221b2c44d4033_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f64679bbf2861bb4af337e5caca221b2c44d4033_2_1380x784.png 2x" data-dominant-color="2D2D38"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_89</span><span class="informations">2095×1192 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The funny thing is that if I check the Metadata, i can just scroll through the image series as usual, it also knows how many images belong to the series. I also tried to load it in a freeware dicom viewer and it worked fine, so i just cant figue out why it wont work with 3D Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba93912344dac3fd50c6b7308162738cbaab8857.png" data-download-href="/uploads/short-url/qCwY9xuZ76z9MIcbT4A29m6e939.png?dl=1" title="Screenshot_78" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba93912344dac3fd50c6b7308162738cbaab8857.png" alt="Screenshot_78" data-base62-sha1="qCwY9xuZ76z9MIcbT4A29m6e939" width="690" height="318" data-dominant-color="2D353B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_78</span><span class="informations">729×336 54.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the advanced selection i have those two options but the outcome is alwasy the same no matter what box is checked…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c68296191767c5c1fb7a433004d78c1a3b101564.png" data-download-href="/uploads/short-url/sk6jMqxs8vifeslSpenQFe5gX8U.png?dl=1" title="Screenshot_87" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c68296191767c5c1fb7a433004d78c1a3b101564.png" alt="Screenshot_87" data-base62-sha1="sk6jMqxs8vifeslSpenQFe5gX8U" width="690" height="251" data-dominant-color="242D35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_87</span><span class="informations">1361×496 5.86 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance,</p>
<p>Felix</p>

---

## Post #2 by @pieper (2025-11-29 19:31 UTC)

<p>There can be.a lot of small variations in the dicom headers that prevent loading as you might have expected, especially for uncommon acquisitions or as a result of deidentification or other processing.  Maybe try the DICOMPatcher module.</p>
<p>In the worst case you may need to fall back to writing a custom python script that interprets the headers in the way that is suitable for this data, perhaps modifying them so they are recognized.  If you find a pattern that isn’t handled by the current DICOMPatcher, please consider contributing a pull request.</p>

---
