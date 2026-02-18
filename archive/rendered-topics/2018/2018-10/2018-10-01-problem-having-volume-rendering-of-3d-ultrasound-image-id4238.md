# Problem having volume rendering of 3D ultrasound image

**Topic ID**: 4238
**Date**: 2018-10-01
**URL**: https://discourse.slicer.org/t/problem-having-volume-rendering-of-3d-ultrasound-image/4238

---

## Post #1 by @solstice (2018-10-01 12:27 UTC)

<p>hello</p>
<p>i just downloaded Slicer and new to this. I have a 3d printer at home so i want to try printing fetus files. so i found this video on youtube. <a href="https://www.youtube.com/watch?v=UHq0uyDvhaA" class="inline-onebox" rel="noopener nofollow ugc">View your baby ultrasound and create 3D printable model using free software - YouTube</a>  and found the exact files to try if i can render and have 3d model from a Ultrasound file. but when i put the file to slicer i cant have the same screens and just 1 on top at axial. nothing at sagittal or coronal. when i want to volume render nothing happens. Nothing changes when i choose gpu rendering and hit the eye. i have gaming laptop with i7 7700 chip and  gtx 1070 gb gpu. sharing my screen with you. can you help me with this problem please.</p>
<p>thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de52f2ff6a3ddb347de908cbd44c800f06475c23.jpeg" data-download-href="/uploads/short-url/vILIpsQFyhws3KBDPffsP0FSpph.jpeg?dl=1" title="slicer1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de52f2ff6a3ddb347de908cbd44c800f06475c23_2_690x388.jpeg" alt="slicer1" data-base62-sha1="vILIpsQFyhws3KBDPffsP0FSpph" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de52f2ff6a3ddb347de908cbd44c800f06475c23_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de52f2ff6a3ddb347de908cbd44c800f06475c23_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de52f2ff6a3ddb347de908cbd44c800f06475c23_2_1380x776.jpeg 2x" data-dominant-color="6D686E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer1</span><span class="informations">1920×1080 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2018-10-01 12:46 UTC)

<p>The ultrasound image you have is just a 2D screenshot of a volume rendering. You need actual 3D data to do segmentation or real-time volume rendering.</p>

---

## Post #3 by @lassoan (2018-10-01 12:48 UTC)

<p>What you have loaded is a screenshot (just a 2D volume rendered photo). This happens when 3D information is stored in private fields in the DICOM file.</p>
<p><a href="https://github.com/SlicerHeart/SlicerHeart">SlicerHeart extension</a> has a importers that can decode information from private fields of some DICOM ultrasound files. Install SlicerHeart and try to load the image again.</p>

---

## Post #4 by @solstice (2018-10-01 13:27 UTC)

<p>Hello.<br>
I just discovered slicer for using fetus dcm files to stl and than print.<br>
I found the video on youtube. <a href="https://www.youtube.com/watch?v=UHq0uyDvhaA" rel="nofollow noopener">https://www.youtube.com/watch?v=UHq0uyDvhaA</a>    Downloaded the same files. But i have a different screen not the same at the video. I have a gaming laptop. İ7 7700 with a gtx 1070 8gb gpu. when i do the first step nothing happens. at first i was trying to do cpu rendering, slicer was collapsing. than see the option of gpu but nothing happens. all blank.  what must i do ?</p>
<p>thank you.</p>

---

## Post #5 by @lassoan (2018-10-06 17:38 UTC)

<p>Use the latest nightly version of Slicer, install SlicerHeart extension, and follow the <a href="https://github.com/SlicerHeart/SlicerHeart#loading-ge-kretz-ultrasound-images">instructions for loading images from GE KretzFile format</a>.</p>

---

## Post #6 by @Sakura (2019-07-06 19:44 UTC)

<p>hello Solstice could you foud the way to render it? I have the same issue, wha another file can I use?</p>

---
