---
topic_id: 32206
title: "I Broke My Totalsegmentator"
date: 2023-10-13
url: https://discourse.slicer.org/t/32206
---

# I broke my totalsegmentator

**Topic ID**: 32206
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/i-broke-my-totalsegmentator/32206

---

## Post #1 by @Matteboo (2023-10-13 11:57 UTC)

<p>Hello,<br>
I’ve been using total segmentator manually for some time and  it was working well.<br>
I’ve recently tried too automatize the process and installed total segmentator directly by running</p>
<blockquote>
<p>pip install TotalSegmentator</p>
</blockquote>
<p>in the window powershell. After some trial and error, I think I got total-segmentator working directly outside of slicer.<br>
After that, I tried to run a segmentation in slicer and it’s not working anymore, I get the following error:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\bin\Python\slicer\util.py”, line 3146, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/matte/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 271, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/matte/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 868, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/matte/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 701, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/matte/AppData/Local/slicer.org/Slicer 5.4.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/matte/AppData/Local/Temp/Slicer/__SlicerTemp__2023-10-13_13+50+57.707/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/matte/AppData/Local/Temp/Slicer/__SlicerTemp__2023-10-13_13+50+57.707/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>
</blockquote>
<p>I tried to uninstall/reinstall slicer and the total segmentator extension but the error doesn’t change.<br>
If somebody has a fix I would be very interested.</p>

---

## Post #2 by @lassoan (2023-10-13 18:24 UTC)

<aside class="quote no-group" data-username="Matteboo" data-post="1" data-topic="32206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<p>pip install TotalSegmentator</p>
</blockquote>
</aside>
<p>TotalSegmentator has some <a href="https://github.com/wasserth/TotalSegmentator/blob/216397e52ec70d098e495793a980527999e6805c/setup.py#L4-L11">incorrectly hardcoded dependencies for Python-3.9</a>, which makes it incompatible with many Python environments, including Slicer’s. In SlicerTotalSegmentator extension we run a custom installation procedure that discards these incorrect entries.</p>
<p>To fix your TotalSegmentator in Slicer: delete your entire Slicer installation tree, reinstall Slicer, and install TotalSegmentator using the TotalSegmentator Slicer extension. You can do this from Python scripts, too.</p>
<p>You can use pip to install TotalSegmentator in a virtual Python environment where you don’t need to run anything else than TotalSegmentator.</p>

---

## Post #3 by @Matteboo (2023-10-16 12:37 UTC)

<p>I tried to do that and it’s still not working.<br>
Is there some hidden part of the Slicer installation tree ? I just uninstall slicer from window and deleted the <a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a> file is there something else I should have done ?</p>
<p>When reinstalling total segmentator module I got these warnings</p>
<pre><code class="lang-auto">  WARNING: The script isympy.exe is installed in 'C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts convert-caffe2-to-onnx.exe, convert-onnx-to-caffe2.exe and torchrun.exe are installed in 'C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts' which is not on PATH.
 WARNING: The scripts lsm2bin.exe, tiff2fsspec.exe, tiffcomment.exe and tifffile.exe are installed in 'C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts' which is not on PATH.
</code></pre>
<p>Should I add them to the path ? If yes how do I do it ?<br>
Sorry if my questions are obvious, I’m not very familiar with python</p>

---

## Post #4 by @Matteboo (2023-10-16 12:42 UTC)

<p>To add information, the error changed, now this is what I get:</p>
<pre><code class="lang-auto">  File "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator", line 93, in &lt;module&gt;
    main()
  File "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator", line 86, in main
    totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
  File "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 157, in totalsegmentator
    download_pretrained_weights(task_id)
  File "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\libs.py", line 183, in download_pretrained_weights
    download_url_and_unpack(WEIGHTS_URL, config_dir)
  File "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\libs.py", line 69, in download_url_and_unpack
    raise e
  File "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\libs.py", line 56, in download_url_and_unpack
    r.raise_for_status()
  File "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\requests\models.py", line 1021, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://zenodo.org/record/6802052/files/Task256_TotalSegmentator_3mm_1139subj.zip?download=1
</code></pre>
<p>It seems like the issue is that I can’t download the weight for the network</p>

---

## Post #5 by @lassoan (2023-10-16 14:41 UTC)

<p>This is a valid, working download URL. If Slicer has problems accessing this URL then your organization might interfere with your network access. You can find  more information about this issue and how to resolve it <a href="https://github.com/lassoan/SlicerTotalSegmentator/tree/main#fail-to-download-model-files">here</a>.</p>

---

## Post #6 by @Matteboo (2023-10-17 08:09 UTC)

<p>Thank you it works again <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @Matteboo (2023-10-17 11:58 UTC)

<p>I’m just adding in case anyone read this later. I tried to manually import the weight but it was failing.<br>
The reason it was failing was because one of the charater of the path <strong>where the downoladed weight were</strong> contained a special caracter (é) wich was making it impossible for slicer to manually import the weight.<br>
I just moved the weight to another folder and imported them again to fix the issue</p>

---
