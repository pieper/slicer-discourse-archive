---
topic_id: 36688
title: "Error When Running Totalsegmentator Failed To Obtain Launche"
date: 2024-06-11
url: https://discourse.slicer.org/t/36688
---

# Error when running TotalSegmentator: "Failed to obtain launcher executable name"

**Topic ID**: 36688
**Date**: 2024-06-11
**URL**: https://discourse.slicer.org/t/error-when-running-totalsegmentator-failed-to-obtain-launcher-executable-name/36688

---

## Post #1 by @khajta (2024-06-11 02:11 UTC)

<p>Dear experts,</p>
<p>I tried to use TotalSegmentator extionsion, but it showed the error. Thank you in advance for suggestions.</p>
<p>Failed to compute results.</p>
<p>Command ‘[‘C:/Users/アイソトープ部/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\アイソトープ部\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-11_11+11+08.463/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-11_11+11+08.463/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\アイソトープ部\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/アイソトープ部/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 298, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/アイソトープ部/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 961, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/Users/アイソトープ部/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1035, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/Users/アイソトープ部/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 807, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/アイソトープ部/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\アイソトープ部\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-11_11+11+08.463/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-11_11+11+08.463/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>
<p>The box of the left hand side show this error:</p>
<p>Processing started</p>
<p>Writing input file to C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-11_11+11+08.463/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-11_11+11+08.463/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-11_11+11+08.463/segmentation’, ‘–ml’, ‘–task’, ‘total’]</p>
<p>error: Failed to obtain launcher executable name !</p>

---

## Post #2 by @lassoan (2024-06-11 12:02 UTC)

<p>Please try to install Slicer in a directory that does not have special characters in its name.</p>

---

## Post #3 by @khajta (2024-06-11 12:06 UTC)

<p>Thank you for your suggestion. It is an office computer in Japan. I will find another folder and let you know the result.</p>

---

## Post #4 by @khajta (2024-06-12 03:32 UTC)

<p>This is another error of another PC.</p>
<p>Failed to compute results.</p>
<p>Command ‘[‘C:/Users/khajt/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/khajt/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-12_11+12+07.371/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/khajt/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-12_11+12+07.371/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/khajt/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 298, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/khajt/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 961, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/Users/khajt/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1035, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/Users/khajt/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 807, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/khajt/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/khajt/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-12_11+12+07.371/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/khajt/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-12_11+12+07.371/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>
<p>Processing started<br>
Writing input file to C:/Users/khajt/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-12_11+12+07.371/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/khajt/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-12_11+12+07.371/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/khajt/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-12_11+12+07.371/segmentation’, ‘–ml’, ‘–task’, ‘total’]<br>
Traceback (most recent call last):<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
return _run_code(code, main_globals, None,<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
exec(code, run_globals)<br>
File "C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe_<em>main</em></em>.py", line 7, in <br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 127, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 293, in totalsegmentator<br>
seg_img, ct_img = nnUNet_predict_image(input, output, task_id, model=model, folds=folds,<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 375, in nnUNet_predict_image<br>
nnUNetv2_predict(tmp_dir, tmp_dir, tid, model, folds, trainer, tta,<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 178, in nnUNetv2_predict<br>
predict_from_raw_data(dir_in,<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 347, in predict_from_raw_data<br>
[i.get() for i in r]<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\multiprocessing\pool.py”, line 736, in <strong>exit</strong><br>
self.terminate()<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\multiprocessing\pool.py”, line 654, in terminate<br>
self._terminate()<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\multiprocessing\util.py”, line 224, in <strong>call</strong><br>
res = self._callback(*self._args, **self._kwargs)<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\multiprocessing\pool.py”, line 713, in _terminate_pool<br>
p.terminate()<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\multiprocessing\process.py”, line 133, in terminate<br>
self._popen.terminate()<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\multiprocessing\popen_spawn_win32.py”, line 123, in terminate<br>
_winapi.TerminateProcess(int(self._handle), TERMINATE)<br>
PermissionError: [WinError 5] Access is denied<br>
Exception in thread Thread-20:<br>
Traceback (most recent call last):<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\threading.py”, line 973, in _bootstrap_inner<br>
self.run()<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\threading.py”, line 910, in run<br>
self._target(*self._args, **self._kwargs)<br>
File “C:\Users\khajt\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\batchgenerators\dataloading\multi_threaded_augmenter.py”, line 92, in results_loop<br>
raise RuntimeError(“One or more background workers are no longer alive. Exiting. Please check the print”<br>
RuntimeError: One or more background workers are no longer alive. Exiting. Please check the print statements above for the actual error message<br>
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x0000018BCF7F5100&gt;<br>
AttributeError: ‘DummyFile’ object has no attribute ‘flush’</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ or the <code>--roi_subset</code> option can help to reduce runtime.<br>
Resampling…<br>
Resampled in 5.04s<br>
Predicting part 1 of 5 …<br>
Predicting part 2 of 5 …<br>
Predicting part 3 of 5 …<br>
Predicting part 4 of 5 …<br>
Predicting part 5 of 5 …</p>

---

## Post #5 by @Matteboo (2024-06-12 14:00 UTC)

<aside class="quote no-group" data-username="khajta" data-post="4" data-topic="36688">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/khajta/48/76581_2.png" class="avatar"> khajta:</div>
<blockquote>
<p>PermissionError: [WinError 5] Access is denied</p>
</blockquote>
</aside>
<p>I’ve never seen that it’s weird. Here is a list of thing that might help :</p>
<ol>
<li>Check that totalSegmentator run on fast mode on the sample data provided by slicer (click the “fast” checkbox to enable this mode)</li>
<li>Check that you have enough free space on your computer (If your disk is almost full it can cause issues, if you have 10Go of free space it’s good)</li>
<li>Since it’s a permissionerror maybe try to run slicer as Administrator to see if it solves the issue</li>
</ol>

---

## Post #6 by @khajta (2024-06-15 05:40 UTC)

<p>I notice that when I use CT images of Abdomen, it can run without any error. However, it had an error when I use CT inages of Chest + whole abdomen. The error showed following:</p>
<p>Failed to compute results.</p>
<p>Command ‘[‘F:/Slicer/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘F:\Slicer\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/matsubaralab/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-15_14+28+53.265/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/matsubaralab/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-15_14+28+53.265/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120<br>
Traceback (most recent call last):<br>
File “F:\Slicer\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “F:/Slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 298, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “F:/Slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 961, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “F:/Slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1035, in processVolume<br>
self.logProcessOutput(proc)<br>
File “F:/Slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 807, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘F:/Slicer/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘F:\Slicer\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/matsubaralab/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-15_14+28+53.265/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/matsubaralab/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-15_14+28+53.265/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>
<p>Processing started<br>
Writing input file to C:/Users/matsubaralab/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-15_14+28+53.265/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/matsubaralab/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-15_14+28+53.265/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/matsubaralab/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-15_14+28+53.265/segmentation’, ‘–ml’, ‘–task’, ‘total’]<br>
Traceback (most recent call last):<br>
File “F:\Slicer\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
return _run_code(code, main_globals, None,<br>
File “F:\Slicer\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
exec(code, run_globals)<br>
File "F:\Slicer\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe_<em>main</em></em>.py", line 7, in <br>
File “F:\Slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 127, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “F:\Slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 293, in totalsegmentator<br>
seg_img, ct_img = nnUNet_predict_image(input, output, task_id, model=model, folds=folds,<br>
File “F:\Slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 375, in nnUNet_predict_image<br>
nnUNetv2_predict(tmp_dir, tmp_dir, tid, model, folds, trainer, tta,<br>
File “F:\Slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 178, in nnUNetv2_predict<br>
predict_from_raw_data(dir_in,<br>
File “F:\Slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 333, in predict_from_raw_data<br>
np.save(ofile + ‘.npy’, prediction)<br>
File “F:\Slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\npyio.py”, line 546, in save<br>
format.write_array(fid, arr, allow_pickle=allow_pickle,<br>
File “F:\Slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\format.py”, line 730, in write_array<br>
array.tofile(fp)<br>
OSError: 1363934700 requested and 0 written<br>
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x00000207772AB970&gt;<br>
AttributeError: ‘DummyFile’ object has no attribute ‘flush’</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ or the <code>--roi_subset</code> option can help to reduce runtime.<br>
Resampling…<br>
Resampled in 14.75s<br>
Predicting part 1 of 5 …</p>
<p>Could you suggest for this issue.</p>

---

## Post #7 by @lassoan (2024-06-18 19:51 UTC)

<p>If TotalSegmentator works for smaller volumes but not for larger ones then most likely it means that it runs out of memory. You can fix it by cropping and/or resampling the input image using Crop Volume module or upgrade your computer with more memory.</p>

---
