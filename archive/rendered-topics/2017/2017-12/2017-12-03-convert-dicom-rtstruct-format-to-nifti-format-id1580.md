# Convert DICOM-RTSTRUCT format to Nifti format

**Topic ID**: 1580
**Date**: 2017-12-03
**URL**: https://discourse.slicer.org/t/convert-dicom-rtstruct-format-to-nifti-format/1580

---

## Post #1 by @glhfgg1024 (2017-12-03 05:17 UTC)

<p>Hi all, I’m facing another problem. I’m using machine learning method to do segmentation for medical images, and at first I convert the DICOM files to Nifti format. I have several DICOM directories and their corresponding DICOM-RTSTRUCT file as the segmentation masks. The problem is: for several cases, the python script can convert the DICOM-RTSTRUCT file to a valid Nifti file, but for other cases, the generated Nifti file of DICOM-RTSTRUCT has inconsistency image origin information as that of the corresponding DICOM files. I have asked one physician in our group for help, he said that the files may come from different DICOM imaging system, and thus has different meta information. But the commercial software (like 3D Slicer) can handle these issues automatically. Could you please suggest some software to convert DICOM-RTSTRUCT file to Nifti format? It seems the 3D Slicer doesn’t have this functionality. Thanks a lot.</p>

---

## Post #2 by @lassoan (2017-12-03 06:13 UTC)

<aside class="quote no-group quote-post-not-found" data-username="glhfgg1024" data-post="3" data-topic="1562">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/glhfgg1024/48/947_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-show-dicom-and-the-corresponding-rt-structure/1562/3">How to show DICOM and the corresponding RT STRUCTURE?</a></div>
<blockquote>
<p>Could you please suggest some software to convert DICOM-RTSTRUCT file to Nifti format? It seems the 3D Slicer doesn’t have this functionality.</p>
</blockquote>
</aside>
<p>Slicer can certainly read DICOM RTSTRUCT and save it as a labelmap in Nifti format.</p>
<aside class="quote no-group quote-post-not-found" data-username="glhfgg1024" data-post="3" data-topic="1562">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/glhfgg1024/48/947_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-show-dicom-and-the-corresponding-rt-structure/1562/3">How to show DICOM and the corresponding RT STRUCTURE?</a></div>
<blockquote>
<p>for other cases, the generated Nifti file of DICOM-RTSTRUCT has inconsistency image origin information as that of the corresponding DICOM files</p>
</blockquote>
</aside>
<p>By default, when you export a segmentation to a labelmap volume, Slicer uses the smallest necessary image extent, so the input grayscale volume’s geometry will not be the same as labelmap volume’s. If your software requires the grayscale and labelmap volumes to have the exact same geometry then you just need to specify the grayscale volume as reference volume for labelmap export (see Segmentations module Export/import… / Advanced section).</p>

---

## Post #3 by @glhfgg1024 (2017-12-03 16:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks a lot! Now I can export the contours successfully!</p>

---

## Post #4 by @Zone1314 (2019-05-22 01:29 UTC)

<p>Does the value of the ROI outline defined in the labelmap exported by this segmentation module be 1 or 0?</p>

---

## Post #5 by @lassoan (2019-05-22 02:35 UTC)

<p>If you export to labelmap, each segment will be assigned a unique voxel value, starting from 1. Voxel value of 0 means outside of all segments.</p>

---

## Post #6 by @Zone1314 (2019-05-22 07:30 UTC)

<p>Thank you for your answer!</p>

---

## Post #7 by @Marianne (2020-08-26 08:53 UTC)

<p>When I am saving a CTV RTstructure as a labelmap, I am not able to save this as a nifti. The choices are STL or OBJ. What am I missing here? I am using the T1 MRI as grayscale reference volume, and I need to save the labelmap as a nifti in order to use in python and compare to machine learning-derived CTV. Any suggestions? I am using 3Dslicer 4.10.2</p>

---

## Post #8 by @cpinter (2020-08-26 09:18 UTC)

<p>First of all, please use the latest nightly because 4.10.2 is almost two years old.</p>
<p>To save a segmentation as nifti, you need to export it to labelmap, but it seems you exported it to models.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a2a7809a88551e17d311303b1588d17b8ba7656.png" alt="image" data-base62-sha1="aA6jXN625xpU8h5jHR4rEX4uXwW" width="522" height="212"></p>
<p>Then you can save the labelmap to nifti using the save function</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1820eecfdeb51bb29b8229ca09fb588aee36621c.png" alt="image" data-base62-sha1="3rs15IvsVVikXO7OugLBx9dvgTi" width="474" height="393"></p>

---

## Post #9 by @Marianne (2020-08-26 10:07 UTC)

<p>Thank you!! You made my day <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #10 by @lassoan (2021-09-12 00:38 UTC)

<p>A post was split to a new topic: <a href="/t/rt-structure-set-has-holes-after-exporting-to-labelmap/19625">RT structure set has holes after exporting to labelmap</a></p>

---

## Post #11 by @qaz158aaa (2025-01-27 07:00 UTC)

<p>When I was about to create the binary map, the software just had no response. Do you know why? My version is the newest one.</p>

---

## Post #12 by @qaz158aaa (2025-01-27 07:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e07d67cb4ad8783ea4ee9cabbf0981d75fc6891.jpeg" data-download-href="/uploads/short-url/b8i2bgTnAyfpfmOC5UHfhhKvB1T.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e07d67cb4ad8783ea4ee9cabbf0981d75fc6891_2_690x410.jpeg" alt="image" data-base62-sha1="b8i2bgTnAyfpfmOC5UHfhhKvB1T" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e07d67cb4ad8783ea4ee9cabbf0981d75fc6891_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e07d67cb4ad8783ea4ee9cabbf0981d75fc6891_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e07d67cb4ad8783ea4ee9cabbf0981d75fc6891_2_1380x820.jpeg 2x" data-dominant-color="81818C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1142 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I choose this option.</p>

---
