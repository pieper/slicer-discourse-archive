# Problem during segmentation of MRI scans and image spacing

**Topic ID**: 20033
**Date**: 2021-10-06
**URL**: https://discourse.slicer.org/t/problem-during-segmentation-of-mri-scans-and-image-spacing/20033

---

## Post #1 by @Jonathan (2021-10-06 06:18 UTC)

<p>Hi there!</p>
<p>I encountered two issues while trying to segment and reconstruct cardiac MRI scans.</p>
<ol>
<li>
<p>While trying to perform manual segmentation of the images using paint (segmentation Editor).<br>
I was only able to segment the first image. It seems as if this feature was unresponsive for the following images, although the volume is properly defined.<br>
I tried to use both the data loader and the DICOM loader, but without any success.</p>
</li>
<li>
<p>I was trying to increase the image spacing in the Z direction. However, manual alteration caused colour distortion and the images were blurred and indistinct. Can one alter the image spacing to all images at once?</p>
</li>
</ol>
<p>Thank you for your help!</p>
<p>Jonathan</p>
<p>Link to the files: <a href="https://drive.google.com/drive/folders/1PZAFyMkXvhUEK5v11aHJI8lFCMHSUffu?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1PZAFyMkXvhUEK5v11aHJI8lFCMHSUffu?usp=sharing</a></p>
<p>Version: 4.11.20200930</p>

---

## Post #2 by @lassoan (2021-10-06 17:54 UTC)

<p>In your data set, each frame is stored as a separate series (has different series instance UID), therefore Slicer does not allow to load them as a single volume.</p>
<p>You can use “DICOM Patcher” module to fix this, by enabling the “Force same series instance UID in each directory” option. If you import and load the patched files using DICOM module then you’ll see the volume loaded correctly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/907a787dfa5cd1970b7322a3aaddb85ecec8956c.jpeg" data-download-href="/uploads/short-url/kC79aIAV1TzO1HvFQTAwzunFAIc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/907a787dfa5cd1970b7322a3aaddb85ecec8956c_2_690x420.jpeg" alt="image" data-base62-sha1="kC79aIAV1TzO1HvFQTAwzunFAIc" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/907a787dfa5cd1970b7322a3aaddb85ecec8956c_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/907a787dfa5cd1970b7322a3aaddb85ecec8956c_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/907a787dfa5cd1970b7322a3aaddb85ecec8956c_2_1380x840.jpeg 2x" data-dominant-color="393839"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1169 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This splitting of each slice position into a separate series makes sense if you acquire a cine-MRI, with multiple time points. If you load a data set like this with multiple time points then Slicer will recognize it as a 4D data set (spread across multiple series) and will load it as a volume sequence.</p>

---

## Post #3 by @Jonathan (2021-10-07 06:37 UTC)

<p>I thank you very much for the quick reply.</p>
<p>I tried segmenting the images using the “DICOM Patcher” as you suggested.<br>
The issue with the image following the alteration of image spacing was resolved.<br>
However, half of the slices still cannot be manually segmented (apex to mid-height).</p>
<p>I attached the reconstruction image and a screenshot of the DICOM loader after patching.</p>
<p>Jonathan<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43b7eac24d69744f195a2df7b750e05a8e176d89.jpeg" alt="rec" data-base62-sha1="9F41UUoySWO08ABGH8YiW2utEvL" width="301" height="233"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/181b6a1d02ec0b80aa1c09d74ca70fbed995ca12.png" data-download-href="/uploads/short-url/3rgc41YbIv8U07QOU0x7qj3hzhw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/181b6a1d02ec0b80aa1c09d74ca70fbed995ca12_2_572x500.png" alt="image" data-base62-sha1="3rgc41YbIv8U07QOU0x7qj3hzhw" width="572" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/181b6a1d02ec0b80aa1c09d74ca70fbed995ca12_2_572x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/181b6a1d02ec0b80aa1c09d74ca70fbed995ca12_2_858x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/181b6a1d02ec0b80aa1c09d74ca70fbed995ca12.png 2x" data-dominant-color="CCE1EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1086×948 31.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-10-07 12:38 UTC)

<p>Remove the original (unpatched) list of series from the database before you import the patches series (a single 3D volume), as having all those single-slice series in the scene may be confusing.</p>
<p>If you load a single 3D volume then you don’t need to worry about how you can segment each slice:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaae592ff155dc510538cacfe932d43a434f2d00.jpeg" data-download-href="/uploads/short-url/olUHZZi6UwXCGGgDfphTmcXu42Q.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaae592ff155dc510538cacfe932d43a434f2d00_2_690x419.jpeg" alt="image" data-base62-sha1="olUHZZi6UwXCGGgDfphTmcXu42Q" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaae592ff155dc510538cacfe932d43a434f2d00_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaae592ff155dc510538cacfe932d43a434f2d00_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaae592ff155dc510538cacfe932d43a434f2d00_2_1380x838.jpeg 2x" data-dominant-color="404546"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1166 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Jonathan (2021-10-08 06:17 UTC)

<p>Thanks for your advice.</p>
<p>I tried to do just that after reading the patcher online documentation yet, I wasn’t able to load the series as a single 3D volume.<br>
The screenshot of the DICOM loader was taken after the patching process. The DICOM database was empty.</p>
<p>In the file system,17 subdirectories were created by the patcher, containing one file in each. The files were saved under the same name.<br>
Given that the data should have been saved as a single series, I’m not convinced this is the anticipated result.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a2b9d51c267aabe59691dc8a76663f0a6c30639.png" alt="image" data-base62-sha1="8iB8uyTqlpWmcrc0TVNaYgE5oDf" width="549" height="375"></p>
<p>Despite the fact that I followed your directions to the letter, I am most likely making a mistake.<br>
Would you mind sending me a short video to show me the ropes?</p>
<p>Thank you very much</p>
<p>Jonathan</p>

---
