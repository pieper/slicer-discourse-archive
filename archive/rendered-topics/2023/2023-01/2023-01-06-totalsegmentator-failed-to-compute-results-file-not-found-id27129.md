# TotalSegmentator failed to compute results - file not found

**Topic ID**: 27129
**Date**: 2023-01-06
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-file-not-found/27129

---

## Post #1 by @3omeoneS (2023-01-06 08:20 UTC)

<p>Hello, Lassoan.<br>
Firstly, thank you for sharing this awesome extension, <code>SlicerTotalSegmentator</code></p>
<p>During using this(actually for first time), I faced an error issue<br>
Could you give me any advice about that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b507dfacf8ef42f8889291fcb96494e14677f59.png" data-download-href="/uploads/short-url/m9YsBSlwGu7cKb5WKnELdyeCOTf.png?dl=1" title="이미지 2023 0106 165037 - 복사본" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b507dfacf8ef42f8889291fcb96494e14677f59_2_690x341.png" alt="이미지 2023 0106 165037 - 복사본" data-base62-sha1="m9YsBSlwGu7cKb5WKnELdyeCOTf" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b507dfacf8ef42f8889291fcb96494e14677f59_2_690x341.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b507dfacf8ef42f8889291fcb96494e14677f59_2_1035x511.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b507dfacf8ef42f8889291fcb96494e14677f59_2_1380x682.png 2x" data-dominant-color="AFB0C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">이미지 2023 0106 165037 - 복사본</span><span class="informations">1920×949 302 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>for information, my GPU is <code>GeForce RTX 3090 Ti</code> which has 24GB</p>

---

## Post #2 by @rbumm (2023-01-06 13:09 UTC)

<p>Please try the CTChest sample dataset. Is there still an error message?</p>

---

## Post #3 by @lassoan (2023-01-06 16:38 UTC)

<p><a class="mention" href="/u/3omeones">@3omeoneS</a></p>
<p>Could you please check if you can find more specific error messages in the textbox below the Apply button after clicking OK on the popup?<br>
You can also look for more details in the application log that you can get in menu: Help / Report a bug.</p>

---

## Post #4 by @3omeoneS (2023-01-08 23:55 UTC)

<p>well… what is difference between my sample and CT chest sample?<br>
I think they are same actually. <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @3omeoneS (2023-01-09 00:10 UTC)

<p>well… I posted bug log… but the system made it hidden;;<br>
they thought it was spam -_-;;</p>

---

## Post #6 by @3omeoneS (2023-01-09 00:16 UTC)

<p>TotalSegmentator.py:452) - FileNotFoundError: [Errno 2] No such file or directory: ‘C:\Users\computer\.totalsegmentator\nnunet\results\nnUNet\3d_fullres\Task253_TotalSegmentator_part3_cardiac_1139subj\nnUNetTrainerV2_ep4000_nomirror__nnUNetPlansv2.1\plans.pkl’<br>
TotalSegmentator.py:452) - Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x0000024A418D96A0&gt;<br>
TotalSegmentator.py:452) - AttributeError: ‘DummyFile’ object has no attribute ‘flush’</p>

---

## Post #7 by @lassoan (2023-01-09 14:11 UTC)

<p>A post was split to a new topic: <a href="/t/totalsegmentator-fails-with-error-120/27130">TotalSegmentator fails with error 120</a></p>

---

## Post #8 by @lassoan (2023-01-09 14:14 UTC)

<aside class="quote no-group" data-username="3omeoneS" data-post="6" data-topic="27129">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/3omeones/48/17924_2.png" class="avatar"> 3omeoneS:</div>
<blockquote>
<p>FileNotFoundError: [Errno 2] No such file or directory:</p>
</blockquote>
</aside>
<p>This is very useful information. It means that the first time you have run TotalSegmentator the model download was incomplete (either network transient network problem or you were not patient enough and interrupted).</p>
<p>You can fix this by deleting the <code>C:\Users\computer\.totalsegmentator</code> folder and restart. Normally model download completes within a couple of minutes, but just in case, give it an hour.</p>

---

## Post #9 by @3omeoneS (2023-01-09 00:07 UTC)

<p>Sorry to late reply</p>
<p>well… the log file can’t be uploaded;;<br>
so I look into log and here is the point where the bug was started</p>
<pre><code class="lang-auto">--------------------------------------------------------------------------------
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) -   File "C:\Users\@@@@\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\shutil.py", line 264, in copyfile
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) -     with open(src, 'rb') as fsrc:
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\@@@@\\.totalsegmentator\\nnunet\\results\\nnUNet\\3d_fullres\\Task253_TotalSegmentator_part3_cardiac_1139subj\\nnUNetTrainerV2_ep4000_nomirror__nnUNetPlansv2.1\\plans.pkl'
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x0000024A418D96A0&gt;
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - AttributeError: 'DummyFile' object has no attribute 'flush'
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - Downloading pretrained weights for Task 254 (~230MB) ...
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - Download finished. Extracting...
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) -   downloaded in 65.10s
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - Downloading pretrained weights for Task 255 (~230MB) ...
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - Download finished. Extracting...
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) -   downloaded in 59.25s
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - Resampling...
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) -   Resampled in 6.94s
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - Predicting part 0 of 5 ...
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - Predicting part 1 of 5 ...
[INFO][Python] 09.01.2023 08:56:07 [Python] (C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:452) - Predicting part 2 of 5 ...
[ERROR][Python] 09.01.2023 08:56:08 [Python] (C:\Users\@@@@\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py:2730) - Failed to compute results.

Command '['C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\@@@@\\AppData\\Local\\NA-MIC\\Slicer 5.2.1\\lib\\Python\\Scripts\\TotalSegmentator', '-i', 'C:/Users/@@@@/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-09_08+53+26.103/total-segmentator-input.nii', '-o', 'C:/Users/@@@@/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-09_08+53+26.103/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 120.
[CRITICAL][Stream] 09.01.2023 08:56:44 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 09.01.2023 08:56:44 [] (unknown:0) -   File "C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 258, in onApplyButton
[CRITICAL][Stream] 09.01.2023 08:56:44 [] (unknown:0) -     self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
[CRITICAL][Stream] 09.01.2023 08:56:44 [] (unknown:0) -   File "C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 715, in process
[CRITICAL][Stream] 09.01.2023 08:56:44 [] (unknown:0) -     self.logProcessOutput(proc)
[CRITICAL][Stream] 09.01.2023 08:56:44 [] (unknown:0) -   File "C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 624, in logProcessOutput
[CRITICAL][Stream] 09.01.2023 08:56:44 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 09.01.2023 08:56:44 [] (unknown:0) - subprocess.CalledProcessError: Command '['C:/Users/@@@@/AppData/Local/NA-MIC/Slicer 5.2.1/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\@@@@\\AppData\\Local\\NA-MIC\\Slicer 5.2.1\\lib\\Python\\Scripts\\TotalSegmentator', '-i', 'C:/Users/@@@@/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-09_08+53+26.103/total-segmentator-input.nii', '-o', 'C:/Users/@@@@/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-09_08+53+26.103/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 120.
--------------------------------------------------------------------------------

cf) I changed my computer's domain name to '@@@@'
</code></pre>

---

## Post #10 by @lassoan (2023-01-09 14:22 UTC)

<aside class="quote no-group" data-username="3omeoneS" data-post="9" data-topic="27129">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/3omeones/48/17924_2.png" class="avatar"> 3omeoneS:</div>
<blockquote>
<p>well… the log file can’t be uploaded;;</p>
</blockquote>
</aside>
<p>File uploads should be kept at minimum to keep hosting costs under control. You can upload any files anywhere (your dropbox, onedrive, google drive, etc.) and just post the link here.</p>

---

## Post #11 by @3omeoneS (2023-01-10 00:45 UTC)

<p>WOW AMAZING! It worked!!!</p>
<p>I think, the problem was GPU issue.<br>
When I uses this for first time, my computer GPU status was running on other works(deep learning stuff).<br>
And for following your adivce, I cleaned whole GPU cash, and delete <code>TotalSegmentator</code> and restart → finally It worked.</p>
<p>Thank you.</p>

---

## Post #12 by @michaelli (2023-10-17 22:02 UTC)

<p>I got the same error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d585f9ce7a1e276d8bdb2e40e6ba26e408e95e4c.png" data-download-href="/uploads/short-url/usUK4h8B5XusTdtePUDZchgxkni.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d585f9ce7a1e276d8bdb2e40e6ba26e408e95e4c_2_690x340.png" alt="image" data-base62-sha1="usUK4h8B5XusTdtePUDZchgxkni" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d585f9ce7a1e276d8bdb2e40e6ba26e408e95e4c_2_690x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d585f9ce7a1e276d8bdb2e40e6ba26e408e95e4c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d585f9ce7a1e276d8bdb2e40e6ba26e408e95e4c.png 2x" data-dominant-color="ECEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">697×344 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is log message popped up by TotalSegmentator:</p>
<blockquote>
<p>Processing started<br>
Writing input file to C:/Users/username/AppData/Local/Temp/Slicer/__SlicerTemp__2023-10-17_17+57+36.230/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/username/AppData/Local/Temp/Slicer/__SlicerTemp__2023-10-17_17+57+36.230/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/username/AppData/Local/Temp/Slicer/__SlicerTemp__2023-10-17_17+57+36.230/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
C:\Users\username\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator:5: DeprecationWarning: pkg_resources is deprecated as an API. See <a href="https://setuptools.pypa.io/en/latest/pkg_resources.html" class="inline-onebox" rel="noopener nofollow ugc">Package Discovery and Resource Access using pkg_resources - setuptools 69.0.2.post20231121 documentation</a><br>
from pkg_resources import require</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" class="inline-onebox" rel="noopener nofollow ugc">[2208.05868] TotalSegmentator: robust segmentation of 104 anatomical structures in CT images</a></p>
<p>Using ‘fast’ option: resampling to lower resolution (3mm)<br>
Downloading pretrained weights for Task 256 (~230MB) …<br>
Traceback (most recent call last):<br>
File “C:\Users\username\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator”, line 93, in <br>
main()<br>
File “C:\Users\username\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator”, line 86, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “C:\Users\username\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 157, in totalsegmentator<br>
download_pretrained_weights(task_id)<br>
File “C:\Users\username\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 183, in download_pretrained_weights<br>
download_url_and_unpack(WEIGHTS_URL, config_dir)<br>
File “C:\Users\username\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 69, in download_url_and_unpack<br>
raise e<br>
File “C:\Users\username\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 56, in download_url_and_unpack<br>
r.raise_for_status()<br>
File “C:\Users\username\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\requests\models.py”, line 1021, in raise_for_status<br>
raise HTTPError(http_error_msg, response=self)<br>
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: <a href="https://zenodo.org/record/6802052/files/Task256_TotalSegmentator_3mm_1139subj.zip?download=1" rel="noopener nofollow ugc">https://zenodo.org/record/6802052/files/Task256_TotalSegmentator_3mm_1139subj.zip?download=1</a></p>
</blockquote>
<blockquote>
<p>Blockquote</p>
</blockquote>

---

## Post #13 by @michaelli (2023-10-17 22:04 UTC)

<p>Whether use fast mode or not, the error is the same.</p>
<p>It prompted me that my GPU mem is less than 7GB. I clicked yes.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7a32cb03c8be0661ff74ea1ea5caa9aaae15260.png" alt="image" data-base62-sha1="qcwYzwx5Z06KbgPany1wMIGt9cs" width="607" height="129"></p>
<p>The second time, I clicked no, but the error was the same.</p>
<p>By the way, do I need to install CUDA myself to use GPU? I’m working on Win 10.</p>

---

## Post #14 by @michaelli (2023-10-17 22:13 UTC)

<p>By the way, I have deleted the folder. TotalSegmentator and restarted.</p>
<p>The data is from the sample ‘CTchest’.</p>

---

## Post #15 by @fedorov (2023-10-17 22:18 UTC)

<p>If you have Docker and git installed on your system, you can try MRunner extension: <a href="https://github.com/MHubAI/SlicerMRunner" class="inline-onebox">GitHub - MHubAI/SlicerMRunner: Beta Version. Browse and run all mhub models directly within 3D Slicer.</a>. It also has TotalSegmentator, packaged using different means.</p>
<p>fyi <a class="mention" href="/u/denbonte">@denbonte</a></p>

---

## Post #16 by @rbumm (2023-10-18 00:00 UTC)

<p>We are having problems with the Zenodo servers currently so users run into problems when they want to use TotalSegmentator from the extension. We will push an update and switch to TS version 1.5.7 where weights get loaded from GitHub.You would need to install the update when available and force install TotalSegmentator once.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49b35b3883ad1d9ba715cd8bba96d9beb4de91bf.png" alt="image" data-base62-sha1="avZ7ICcizIGd1L1Tluk9mzZoCuP" width="596" height="156"></p>
<p>The displayed package information should be 1.5.7</p>

---

## Post #17 by @michaelli (2023-10-18 12:31 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="16" data-topic="27129">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>ll TotalSegmentator onc</p>
</blockquote>
</aside>
<p>Thanks for the information. Looking forward to the update.</p>

---

## Post #18 by @hina-shah (2023-10-20 18:50 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> : Do you have an estimate when this will be ready? I see that SlicerTotalSegmentator has been updated to use totalsegmentator 1.5.7.</p>

---

## Post #19 by @fedorov (2023-10-20 20:08 UTC)

<p>MRunner extension mentioned in <a href="https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-file-not-found/27129/15" class="inline-onebox">TotalSegmentator failed to compute results - file not found - #15 by fedorov</a> has weights packaged within the docker container, so it should work independently of the regression in the TotalSegmentator release.</p>

---

## Post #20 by @lassoan (2023-10-21 12:41 UTC)

<p>MRunner can be great option if you have docker.</p>
<p>We have fixed TotalSegmentator extension (using 1.5.7). Install latest Slicer Stable Release and update or reinstall TotalSegmentator extension. Or inatall latest Slicer Preview Release and install TotalSegmentator extension.</p>
<p>We will release a new version of TotalSegmentator Slicer extension next week that works with TotalSegmentator 2.0.5, which brings imepoved accuracy and new segments.</p>

---
