# Having trouble to fuse MRI PET images from mice brain-newbie

**Topic ID**: 34770
**Date**: 2024-03-08
**URL**: https://discourse.slicer.org/t/having-trouble-to-fuse-mri-pet-images-from-mice-brain-newbie/34770

---

## Post #1 by @Aurorasp (2024-03-08 00:18 UTC)

<p>Operating system: Windows11 pro<br>
Slicer version: 5.4<br>
Expected behavior:<br>
Actual behavior:<br>
Hi all<br>
I am very new to all this, and Slicer was the only tool I found online for Windows. I know very well the neuropathology of rodents but have never worked with imaging or anything related to radiology as of now. I have two sets of data, PET and MR, from the same mice in a day (4 mice scanned in one session), but mice obviously moved for PET, so now I like to register PET to MR images, but sort of lost from the beginning. I converted the PET folder to an nii file that seems to be being opened more smoothly in the software but I face errors entering my MR data folder into the software(Images are not equally spaced …)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e83372c481b466cd34c2565f0af0b6f5f145ff3.png" data-download-href="/uploads/short-url/4lVs1KiuOic6SA7BL8ofXFFrks3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e83372c481b466cd34c2565f0af0b6f5f145ff3_2_690x245.png" alt="image" data-base62-sha1="4lVs1KiuOic6SA7BL8ofXFFrks3" width="690" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e83372c481b466cd34c2565f0af0b6f5f145ff3_2_690x245.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e83372c481b466cd34c2565f0af0b6f5f145ff3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e83372c481b466cd34c2565f0af0b6f5f145ff3.png 2x" data-dominant-color="EFF1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">884×315 66.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
If I ignore this message when I get to put landmarks on the image for fucidial registration, nothing happens or at least I am not sure doing it right. PET images seem to be way larger than MR, and at the end of the day, tweaking options didn’t help with a neat overlap of PET to MR in a very short time. I wish SB working a lot on rodent help with a visual step-by-step guide. I really appreciate any help! Blessings!</p>

---

## Post #2 by @pieper (2024-03-08 21:20 UTC)

<p>Usually the localizer isn’t a 3D volume, so you can ignore that.</p>
<p>For the PET and MR registration, there should be nothing special required.  If you can try with sample data and instructions from the modules you use then you should be able to do the same on your data.  If are still running into problems you can maybe share screenshots of examples of the data you are using and probably someone can give you specific suggestions.</p>

---
