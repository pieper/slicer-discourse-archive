# Convert 4d and 3d ultrasounds from Dicom to STL

**Topic ID**: 28448
**Date**: 2023-03-19
**URL**: https://discourse.slicer.org/t/convert-4d-and-3d-ultrasounds-from-dicom-to-stl/28448

---

## Post #1 by @Diego.Rlz (2023-03-19 12:07 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.2.2<br>
Expected behavior: I want to load the dicom file from a 4d ultrasound and convert it to .stl<br>
Actual behavior: In the 3 view windows just 1 displays an image, the other 2 are basically an horizontal line. Seems like it is just a picture.</p>

---

## Post #2 by @lassoan (2023-03-19 12:10 UTC)

<p>There is no commonly used standard for storing 3D/4D ultrasound. Only some formats can be loaded using SlicerHeart extension. What kind of images do you have (obstetrics, cardiac,…)? What system do you use (Philips, GE,…)?</p>

---

## Post #3 by @Diego.Rlz (2023-03-20 06:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="28448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>no commonly used standard for storing 3D/4D ultrasound. Only some formats can be loaded using SlicerHeart extension. What kind of images do you have (obst</p>
</blockquote>
</aside>
<p>Hi,<br>
I have a 4D ultrasound. When I upload this to 3d slicer, it shows up a picture in the axial window. However, in the sagital and coronal window just shows an horizontal line. Kind of if like this was a flat image and not a 3d file. I am trying to troubleshoot this, I am not sure if it is something I have to o from the 3d slicer or it is related to how this file was saved in the ultrasound machine.</p>

---

## Post #4 by @lassoan (2023-03-20 11:58 UTC)

<p>This is what I described above: only 2D screen capture of the rendering is saved in standard DICOM fields, while the 4D data is saved in private fields.</p>
<p>What kind of images do you have (obstetrics, cardiac,…)? What system do you use (Philips, GE,…)?</p>

---

## Post #5 by @Diego.Rlz (2023-03-20 16:16 UTC)

<p>Thank for following up. I am unsure how this file was saved but I can reach out back to the clinic. I am still new using this 3d slicer so I was still doubting. If you are ok with this, I can share the file with you. Another question I know these are dicom files however the file itself does not have the .dcm extension at the end, not sure if that mattes at all.</p>

---

## Post #6 by @lassoan (2023-03-20 16:54 UTC)

<aside class="quote no-group" data-username="Diego.Rlz" data-post="5" data-topic="28448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e36b37/48.png" class="avatar"> Diego.Rlz:</div>
<blockquote>
<p>I am unsure how this file was saved but I can reach out back to the clinic</p>
</blockquote>
</aside>
<p>Then the file may not even contain the 4D data, maybe it is all just screen capture video of the rendering of the 4D data.</p>
<aside class="quote no-group" data-username="Diego.Rlz" data-post="5" data-topic="28448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e36b37/48.png" class="avatar"> Diego.Rlz:</div>
<blockquote>
<p>Another question I know these are dicom files however the file itself does not have the .dcm extension</p>
</blockquote>
</aside>
<p>Some DICOM files use .dcm extension, but there is no officially designated file extension for DICOM files.</p>
<p>What kind of images do you have (obstetrics, cardiac,…)? What system do you use (Philips, GE,…)?</p>

---

## Post #7 by @Diego.Rlz (2023-03-20 17:04 UTC)

<p>obstretic. it is a 4d ultrasound. The ultrasound machine still dont know the brand of the ultrasound machine</p>

---

## Post #8 by @lassoan (2023-03-20 17:38 UTC)

<p>4D imaging in obstetrics is most commonly used only for keepsake purposes (not for measurements or analysis). When images are exported, usually only the screen capture of the rendering is written to the files (not the voxel data).</p>
<p>SlicerHeart contains an importer for older (Kretz platform based) GE ultrasound systems. Other importers are mainly for cardiovascular ultrasound systems.</p>

---
