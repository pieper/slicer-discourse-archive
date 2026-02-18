# cannot use mpReviewpreprocessor to convert dicom to nrrd in batch mode 

**Topic ID**: 18717
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/cannot-use-mpreviewpreprocessor-to-convert-dicom-to-nrrd-in-batch-mode/18717

---

## Post #1 by @Vuong_Thuy_Tran (2021-07-14 03:15 UTC)

<p>Hi, I am trying to convert dicom series to nrrd in batch mode by using mpReviewpreprocessor module in 3d slicer 4.10.2, but it always shows error like the photo below. How can I handle it? Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b336cca56e64abf24dfce59b62abc240ab927a56.jpeg" data-download-href="/uploads/short-url/pzoSd7GbAeFG1Rm5w1CEAR6NNGK.jpeg?dl=1" title="3d slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b336cca56e64abf24dfce59b62abc240ab927a56_2_690x388.jpeg" alt="3d slicer" data-base62-sha1="pzoSd7GbAeFG1Rm5w1CEAR6NNGK" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b336cca56e64abf24dfce59b62abc240ab927a56_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b336cca56e64abf24dfce59b62abc240ab927a56_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b336cca56e64abf24dfce59b62abc240ab927a56_2_1380x776.jpeg 2x" data-dominant-color="ACA9A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d slicer</span><span class="informations">1920×1080 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is error message in case photo not appear: Traceback (most recent call last):<br>
File “C:\Users\Vuong Thuy Tran\AppData\Roaming\NA-MIC\Extensions-28257\mpReview\lib\Slicer-4.10\qt-scripted-modules\mpReviewPreprocessor.py”, line 71, in onRunClicked<br>
logic = mpReviewPreprocessorLogic()<br>
File “C:\Users\Vuong Thuy Tran\AppData\Roaming\NA-MIC\Extensions-28257\mpReview\lib\Slicer-4.10\qt-scripted-modules\mpReviewPreprocessor.py”, line 108, in <strong>init</strong><br>
shutil.rmtree(self.dataDir)<br>
File “C:\Program Files\Slicer 4.10.2\lib\Python\Lib\shutil.py”, line 247, in rmtree<br>
rmtree(fullname, ignore_errors, onerror)<br>
File “C:\Program Files\Slicer 4.10.2\lib\Python\Lib\shutil.py”, line 252, in rmtree<br>
onerror(os.remove, fullname, sys.exc_info())<br>
File “C:\Program Files\Slicer 4.10.2\lib\Python\Lib\shutil.py”, line 250, in rmtree<br>
os.remove(fullname)<br>
WindowsError: [Error 32] The process cannot access the file because it is being used by another process: u’C:/Users/Vuong Thuy Tran/AppData/Local/Temp/Slicer\mpReviewPreprocessor\CtkDICOMDatabase\ctkDICOM.sql’</p>

---

## Post #2 by @lassoan (2021-07-14 03:22 UTC)

<p>The issue is probably that you have chosen the DICOM database folder to be inside the folder that the mpReviewPreprocessor is using. Choosing a different folder for DICOM database may fix this.</p>
<p>However, most features of multiparametric image review modules have been incorporated to Slicer core, so most likely you’ll be able to accomplish what you need by just using the current Slicer version. If you describe what you would like to do then we can describe how to do it using Slicer core features.</p>

---

## Post #3 by @Vuong_Thuy_Tran (2021-07-14 03:32 UTC)

<p>Thank you for your reply.<br>
Actually I have a lot of dicom images and masks ( in nii format) and I want to extract features from them using pyradiomics.<br>
But pyradiomics just accepts nrrd format so I need to convert them into nrrd format in batch mode.<br>
And I have another problem is my dicom images and mask not getting space match each other when I run pyradiomics.</p>
<p>If you know how to handle it in batch mode please let me know.<br>
Thank you a lot!</p>

---

## Post #4 by @lassoan (2021-07-14 03:37 UTC)

<p>You can find examples for all these operations in the script repository:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom">import image from DICOM</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file">save volume to file</a></li>
<li>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">process segmentations</a> (import segmentation, export segmentation resampled into a chosen image geometry, etc.)</li>
</ul>

---
