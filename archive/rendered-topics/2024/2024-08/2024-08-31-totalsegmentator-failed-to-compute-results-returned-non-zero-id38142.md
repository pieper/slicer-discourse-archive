# TotalSegmentator Failed to compute results....returned non-zero exit status 1

**Topic ID**: 38142
**Date**: 2024-08-31
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-returned-non-zero-exit-status-1/38142

---

## Post #1 by @yk_Chen (2024-08-31 14:13 UTC)

<p>Operating system: Windows 10<br>
Slicer version:5.6.2<br>
Hi,<br>
I have properly installed Pytorch and other python packages, and restarted and reinstalled Slicer several times. But when I hit Apply, I get this error. I suspect that I may have downloaded the relevant package in the wrong folder, but I am not sure how to solve it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7e29a4de335e943da3cdd4952b580faea8cb889.png" data-download-href="/uploads/short-url/swgvFpNLTWSQaO7ZcjuoNDZGV3b.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7e29a4de335e943da3cdd4952b580faea8cb889_2_690x380.png" alt="image" data-base62-sha1="swgvFpNLTWSQaO7ZcjuoNDZGV3b" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7e29a4de335e943da3cdd4952b580faea8cb889_2_690x380.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7e29a4de335e943da3cdd4952b580faea8cb889_2_1035x570.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7e29a4de335e943da3cdd4952b580faea8cb889_2_1380x760.png 2x" data-dominant-color="C6D0D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2133×1175 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And here is the detail:</p>
<pre><code class="lang-auto">[Python] Failed to compute results.
[Python] Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 298, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 971, in process
    self.processVolume(inputFile, inputVolume,
  File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1045, in processVolume
    self.logProcessOutput(proc)
  File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 817, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
</code></pre>
<p>The following is more detailed info from “report a bug”</p>
<pre><code class="lang-auto">[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - Session start time .......: 20240831_215946
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19041, Code Page 65001) - 64-bit
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - Memory ...................: 64665 MB physical, 130201 MB virtual
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 9 7900X 12-Core Processor            , 24 cores, 24 logical processors
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - Application path .........: C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin
[DEBUG][Qt] 31.08.2024 21:59:46 [] (unknown:0) - Additional module paths ..: 
[DEBUG][Python] 31.08.2024 21:59:47 [Python] (C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 31.08.2024 21:59:47 [Python] (C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 31.08.2024 21:59:47 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 31.08.2024 21:59:55 [] (unknown:0) - "Volume" Reader has successfully read the file "D:/DicomDate Dep1Astd/3-403193.nii.gz" "[0.17s]"
[DEBUG][Qt] 31.08.2024 21:59:59 [] (unknown:0) - Switch to module:  "TotalSegmentator"
[INFO][Stream] 31.08.2024 22:00:01 [] (unknown:0) - Looking in indexes: 
[INFO][Stream] 31.08.2024 22:00:01 [] (unknown:0) - Requirement already satisfied: pillow&lt;10.1 in c:\users\administrator\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (10.0.1)
[INFO][Python] 31.08.2024 22:00:02 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch...
[INFO][Python] 31.08.2024 22:00:02 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.4.0+cu118 imported successfully
[INFO][Python] 31.08.2024 22:00:02 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: True
[INFO][Python] 31.08.2024 22:00:02 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Processing started
[INFO][Python] 31.08.2024 22:00:02 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Writing input file to C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/total-segmentator-input.nii
[INFO][Python] 31.08.2024 22:00:02 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Creating segmentations with TotalSegmentator AI...
[INFO][Python] 31.08.2024 22:00:02 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Total Segmentator arguments: ['-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/segmentation', '--ml', '--task', 'total']
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Traceback (most recent call last):
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     return _run_code(code, main_globals, None,
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 87, in _run_code
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     exec(code, run_globals)
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 7, in &lt;module&gt;
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 138, in main
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 126, in totalsegmentator
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py", line 30, in &lt;module&gt;
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py", line 11, in &lt;module&gt;
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     from acvl_utils.cropping_and_padding.padding import pad_nd_image
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - ModuleNotFoundError: No module named 'acvl_utils'
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - If you use this tool please cite: 
[INFO][Python] 31.08.2024 22:00:04 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -
[ERROR][Python] 31.08.2024 22:00:04 [Python] (C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Failed to compute results.

Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 298, in onApplyButton
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) -     self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 971, in process
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) -     self.processVolume(inputFile, inputVolume,
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1045, in processVolume
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) -     self.logProcessOutput(proc)
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 817, in logProcessOutput
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 31.08.2024 22:00:16 [] (unknown:0) - subprocess.CalledProcessError: Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+00+02.786/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
[INFO][Python] 31.08.2024 22:09:03 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch...
[INFO][Python] 31.08.2024 22:09:03 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.4.0+cu118 imported successfully
[INFO][Python] 31.08.2024 22:09:03 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: True
[INFO][Python] 31.08.2024 22:09:03 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Processing started
[INFO][Python] 31.08.2024 22:09:03 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Writing input file to C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+09+03.824/total-segmentator-input.nii
[INFO][Python] 31.08.2024 22:09:03 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Creating segmentations with TotalSegmentator AI...
[INFO][Python] 31.08.2024 22:09:03 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Total Segmentator arguments: ['-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+09+03.824/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+09+03.824/segmentation', '--ml', '--task', 'total']
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Traceback (most recent call last):
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     return _run_code(code, main_globals, None,
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 87, in _run_code
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     exec(code, run_globals)
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 7, in &lt;module&gt;
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 138, in main
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 126, in totalsegmentator
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py", line 30, in &lt;module&gt;
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py", line 11, in &lt;module&gt;
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     from acvl_utils.cropping_and_padding.padding import pad_nd_image
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - ModuleNotFoundError: No module named 'acvl_utils'
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) 
[INFO][Python] 31.08.2024 22:09:05 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -
[ERROR][Python] 31.08.2024 22:09:05 [Python] (C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Failed to compute results.

Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+09+03.824/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+09+03.824/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 298, in onApplyButton
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) -     self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 971, in process
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) -     self.processVolume(inputFile, inputVolume,
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1045, in processVolume
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) -     self.logProcessOutput(proc)
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 817, in logProcessOutput
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 31.08.2024 22:10:42 [] (unknown:0) - subprocess.CalledProcessError: Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+09+03.824/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-08-31_22+09+03.824/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de6d2938c87fdb4bf49f81d7eed93b813d64b7a9.png" data-download-href="/uploads/short-url/vJFSeVLNOobHYqDKmsgFmeeTvIt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de6d2938c87fdb4bf49f81d7eed93b813d64b7a9_2_468x500.png" alt="image" data-base62-sha1="vJFSeVLNOobHYqDKmsgFmeeTvIt" width="468" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de6d2938c87fdb4bf49f81d7eed93b813d64b7a9_2_468x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de6d2938c87fdb4bf49f81d7eed93b813d64b7a9_2_702x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de6d2938c87fdb4bf49f81d7eed93b813d64b7a9_2_936x1000.png 2x" data-dominant-color="EAEEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1232×1314 86.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-08-31 14:17 UTC)

<p>Use the “Help-&gt;Report a bug” menu to get the full log file for a failed run and look at it for more diagnostic info.  If you still need help, post the log here (make sure it doesn’t have patient information in it).</p>

---

## Post #3 by @yk_Chen (2024-08-31 14:28 UTC)

<p>I’ve updated it in the post. I need your help. Thank you very much!</p>

---

## Post #4 by @lassoan (2024-08-31 14:47 UTC)

<p>The detailed log was helpful. Here is the error:</p>
<aside class="quote no-group" data-username="yk_Chen" data-post="1" data-topic="38142">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yk_chen/48/77786_2.png" class="avatar"> yk_Chen:</div>
<blockquote>
<p><code>ModuleNotFoundError: No module named 'acvl_utils'</code></p>
</blockquote>
</aside>
<p>It means that some of the required Python packages were not installed. Did you see any error messages when you first started segmentation and Python dependencies were installed?</p>
<p>You can fix it by clicking <code>Force reinstall</code> button in <code>Advanced</code> section.</p>

---

## Post #5 by @yk_Chen (2024-09-04 13:47 UTC)

<p>yeah, i have solved the problem, thank you very much!</p>

---

## Post #6 by @Carlos_Arrieta (2024-11-09 16:20 UTC)

<p>I have a MacBook Pro M4 and I have the same error… I tried force reinstalling the python packages and still get the same error… I am running 5.7.0</p>
<p>Processing started<br>
Writing input file to /private/var/folders/72/n0v1btkn7q5gdq7rg3_s_1s00000gn/T/Slicer-carlosarrieta/__SlicerTemp__2024-11-09_11+14+38.364/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘/private/var/folders/72/n0v1btkn7q5gdq7rg3_s_1s00000gn/T/Slicer-carlosarrieta/__SlicerTemp__2024-11-09_11+14+38.364/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/72/n0v1btkn7q5gdq7rg3_s_1s00000gn/T/Slicer-carlosarrieta/__SlicerTemp__2024-11-09_11+14+38.364/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–device’, ‘cpu’]</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator”, line 8, in <br>
sys.exit(main())<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/bin/TotalSegmentator.py”, line 141, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/python_api.py”, line 127, in totalsegmentator<br>
from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/nnunet.py”, line 30, in <br>
from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunetv2/inference/predict_from_raw_data.py”, line 22, in <br>
from nnunetv2.inference.data_iterators import PreprocessAdapterFromNpy, preprocessing_iterator_fromfiles, <br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunetv2/inference/data_iterators.py”, line 12, in <br>
from nnunetv2.preprocessing.preprocessors.default_preprocessor import DefaultPreprocessor<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunetv2/preprocessing/preprocessors/default_preprocessor.py”, line 25, in <br>
from nnunetv2.preprocessing.cropping.cropping import crop_to_nonzero<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunetv2/preprocessing/cropping/cropping.py”, line 5, in <br>
from acvl_utils.cropping_and_padding.bounding_boxes import get_bbox_from_mask, crop_to_bbox, bounding_box_to_slice<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/acvl_utils/cropping_and_padding/bounding_boxes.py”, line 5, in <br>
import blosc2<br>
ModuleNotFoundError: No module named ‘blosc2’</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3295, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-33089/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 307, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/Applications/Slicer.app/Contents/Extensions-33089/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 1002, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “/Applications/Slicer.app/Contents/Extensions-33089/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 1076, in processVolume<br>
self.logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/Extensions-33089/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 848, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/72/n0v1btkn7q5gdq7rg3_s_1s00000gn/T/Slicer-carlosarrieta/__SlicerTemp__2024-11-09_11+20+01.602/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/72/n0v1btkn7q5gdq7rg3_s_1s00000gn/T/Slicer-carlosarrieta/__SlicerTemp__2024-11-09_11+20+01.602/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>

---

## Post #7 by @jamesobutler (2024-11-09 17:04 UTC)

<p>It appears MIC-DFZ has messed up their packages with a recent new dependency release. See the following link below for details:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/MIC-DKFZ/acvl_utils/issues/2#issuecomment-2462308453">
  <header class="source">

      <a href="https://github.com/MIC-DKFZ/acvl_utils/issues/2#issuecomment-2462308453" target="_blank" rel="noopener nofollow ugc">github.com/MIC-DKFZ/acvl_utils</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/MIC-DKFZ/acvl_utils/issues/2#issuecomment-2462308453" target="_blank" rel="noopener nofollow ugc">broken nnunetv2 import</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-07" data-time="12:44:14" data-timezone="UTC">12:44PM - 07 Nov 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jeandre-db" target="_blank" rel="noopener nofollow ugc">
          <img alt="jeandre-db" src="https://avatars.githubusercontent.com/u/103255762?v=4" class="onebox-avatar-inline" width="20" height="20">
          jeandre-db
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">ImportError: cannot import name 'crop_to_bbox' from 'acvl_utils.cropping_and_pad<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ding.bounding_boxes' (/local_disk0/.ephemeral_nfs/cluster_libraries/python/lib/python3.11/site-packages/acvl_utils/cropping_and_padding/bounding_boxes.py)
File &lt;command-1458388170907476&gt;, line 7
      5 import pyspark.sql.functions as f
      6 from nnunetv2.imageio.simpleitk_reader_writer import SimpleITKIO
----&gt; 7 from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
      8 from nnunetv2.paths import nnUNet_results, nnUNet_raw
      9 import torch
      
      
It seems that the update to acvl broke nnunetv2 imports. locking the version to 0.2 fixes this issue.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/MIC-DKFZ/nnUNet/issues/2589">
  <header class="source">

      <a href="https://github.com/MIC-DKFZ/nnUNet/issues/2589" target="_blank" rel="noopener nofollow ugc">github.com/MIC-DKFZ/nnUNet</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/MIC-DKFZ/nnUNet/issues/2589" target="_blank" rel="noopener nofollow ugc">`nnunetv2.inference` crashes on import (`No module named 'blosc2'`) due to buggy `acvl_utils` release</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-07" data-time="17:31:56" data-timezone="UTC">05:31PM - 07 Nov 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/joshuacwnewton" target="_blank" rel="noopener nofollow ugc">
          <img alt="joshuacwnewton" src="https://avatars.githubusercontent.com/u/16181459?v=4" class="onebox-avatar-inline" width="20" height="20">
          joshuacwnewton
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Traceback:

```
  File "/home/runner/sct_0.0/spinalcordtoolbox/deepseg/infere<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nce.py", line 27, in &lt;module&gt;
    import spinalcordtoolbox.deepseg.nnunet as ds_nnunet
  File "/home/runner/sct_0.0/spinalcordtoolbox/deepseg/nnunet.py", line 13, in &lt;module&gt;
    from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor   # noqa: E402
  File "/home/runner/sct_0.0/python/envs/venv_sct/lib/python3.9/site-packages/nnunetv2/inference/predict_from_raw_data.py", line 22, in &lt;module&gt;
    from nnunetv2.inference.data_iterators import PreprocessAdapterFromNpy, preprocessing_iterator_fromfiles, \
  File "/home/runner/sct_0.0/python/envs/venv_sct/lib/python3.9/site-packages/nnunetv2/inference/data_iterators.py", line 12, in &lt;module&gt;
    from nnunetv2.preprocessing.preprocessors.default_preprocessor import DefaultPreprocessor
  File "/home/runner/sct_0.0/python/envs/venv_sct/lib/python3.9/site-packages/nnunetv2/preprocessing/preprocessors/default_preprocessor.py", line 23, in &lt;module&gt;
    from nnunetv2.preprocessing.cropping.cropping import crop_to_nonzero
  File "/home/runner/sct_0.0/python/envs/venv_sct/lib/python3.9/site-packages/nnunetv2/preprocessing/cropping/cropping.py", line 5, in &lt;module&gt;
    from acvl_utils.cropping_and_padding.bounding_boxes import get_bbox_from_mask, crop_to_bbox, bounding_box_to_slice
  File "/home/runner/sct_0.0/python/envs/venv_sct/lib/python3.9/site-packages/acvl_utils/cropping_and_padding/bounding_boxes.py", line 5, in &lt;module&gt;
    import blosc2
ModuleNotFoundError: No module named 'blosc2'
```

This is a duplicate of https://github.com/MIC-DKFZ/acvl_utils/issues/2, but I'm re-reporting here just in case anyone else runs into this bug and tries to find it by checking nnUNet's issues.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @alireza-hokmabadi (2024-11-09 20:14 UTC)

<p>To resolve the issue temporarily, you can downgrade <code>acvl_utils</code> until the <code>nnUNet</code> team includes the missing <code>crop_to_bbox</code> function in a future update.</p>
<p>Run the following command to downgrade:<br>
<code>pip install acvl_utils==0.2</code></p>

---

## Post #9 by @lassoan (2024-11-11 18:44 UTC)

<p>nnunet is still not fixed. If anyone comes across this issue, the current workaround is to open Slicer’s Python console (<code>Ctrl</code>+<code>3</code>) and type this command:</p>
<pre><code>pip_install("acvl_utils==0.2")
</code></pre>
<p>I’ve pushed a <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/c4144875e600705f4c4b30a44b49d05d27ffb757">fix (a temporary workaround)</a> to the Slicer TotalSegmentator extension that automatically gets a working acvl_utils package version. This will fix the problem for all new Slicer installations from tomorrow.</p>

---

## Post #10 by @teliq846 (2025-01-16 07:08 UTC)

<p>Click the Python button on the far right of the toolbar to display the Python terminal (&gt;&gt;&gt;)</p>
<p>Enter in the terminal:</p>
<blockquote>
<p>import sys<br>
print(sys.executable)</p>
</blockquote>
<p>To find the path of Python actually used by 3D Slicer, for example:</p>
<blockquote>
<p>C:\Program Files\Slicer 4.xx.x\bin\PythonSlicer.exe</p>
</blockquote>
<p>cd to the path (C:\Program Files\Slicer 4.xx.x\bin), run in the terminal:</p>
<blockquote>
<p>PythonSlicer.exe -m pip install acvl_utils==0.2</p>
</blockquote>
<p>Wait for installation to succeed</p>

---

## Post #11 by @jamesobutler (2025-01-16 14:04 UTC)

<p>Following up here I issued a PR to the SlicerNNUnet extension which is involved in installing acvl_utils and fixed the installation issues. So manually calling pip_install here is no longer needed as long as you have updated your extension to this latest version.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/KitwareMedical/SlicerNNUnet/pull/11">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerNNUnet/pull/11" target="_blank" rel="noopener nofollow ugc">github.com/KitwareMedical/SlicerNNUnet</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/KitwareMedical/SlicerNNUnet/pull/11" target="_blank" rel="noopener nofollow ugc">nnUNetv2 install workaround fixes</a>
      </h4>

    <div class="branches">
      <code>KitwareMedical:main</code> ← <code>jamesobutler:install-backports-from-slicertotalsegmentator</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-01-02" data-time="00:13:44" data-timezone="UTC">12:13AM - 02 Jan 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="5 commits changed 1 files with 27 additions and 23 deletions">
          <a href="https://github.com/KitwareMedical/SlicerNNUnet/pull/11/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+27</span>
            <span class="removed">-23</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This includes several commits from the [SlicerTotalSegmentator](https://github.c<span class="show-more-container"><a href="https://github.com/KitwareMedical/SlicerNNUnet/pull/11" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">om/lassoan/SlicerTotalSegmentator) extension which had workaround fixes associated with installing nnunetv2 and its dependencies.  As originally discussed at https://github.com/Slicer/ExtensionsIndex/pull/2016#issuecomment-2004337762, this extension is to serve as a way to centrally maintain the install of nnUNet in Slicer.

This therefore closes https://github.com/KitwareMedical/SlicerNNUnet/issues/10 where an error was observed during install of nnunetv2.


## Testing with SlicerDentalSegmentator
I have tested this in the context of [SlicerDentalSegmentator](https://github.com/gaudot/SlicerDentalSegmentator) where this closes https://github.com/gaudot/SlicerDentalSegmentator/issues/21. I am now able to run DentalSegmentator using the CBCT Dental Surgery sample data set and get successful results where previously I ran into issues during install of python packages. I used a fresh install of Slicer 5.7.0-2024-12-31 with a cleared out system pip cache so that all downloads would be fresh.
![image](https://github.com/user-attachments/assets/ffc72bd8-cfcf-4962-94c1-5d0538d8c6a5)

&lt;details&gt;
  &lt;summary&gt;DentalSegmentator python console output click here&lt;/summary&gt;

```
Python 3.9.10 (main, Dec 31 2024, 23:19:20) [MSC v.1939 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
[Qt] void __cdecl qMRMLSegmentEditorWidget::setSourceVolumeNode(class vtkMRMLNode *)  failed: need to set segment editor and segmentation nodes first
Collecting nnunetv2
  Downloading nnunetv2-2.5.1.tar.gz (196 kB)
     ------------------------------------ 197.0/197.0 kB 919.8 kB/s eta 0:00:00
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: nnunetv2
  Building wheel for nnunetv2 (pyproject.toml): started
  Building wheel for nnunetv2 (pyproject.toml): finished with status 'done'
  Created wheel for nnunetv2: filename=nnunetv2-2.5.1-py3-none-any.whl size=264428 sha256=557efde55b579236d8846943f74854f469e1cd8c8a75e6a0268862e8821bab00
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\7b\85\af\51e5381b7cf9cc417ca071b9cd6e35afc59236a0ebb4462249
Successfully built nnunetv2
Installing collected packages: nnunetv2
Successfully installed nnunetv2-2.5.1
Collecting dynamic-network-architectures&lt;0.4,&gt;=0.3.1
  Downloading dynamic_network_architectures-0.3.1.tar.gz (20 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Building wheels for collected packages: dynamic-network-architectures
  Building wheel for dynamic-network-architectures (setup.py): started
  Building wheel for dynamic-network-architectures (setup.py): finished with status 'done'
  Created wheel for dynamic-network-architectures: filename=dynamic_network_architectures-0.3.1-py3-none-any.whl size=30056 sha256=5fa8fae7292a5f7ae3e656a4866d3a71262c51fd12ab6d0bb3fadbc79fd93286
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\ec\59\c1\e65ad8b5ac7df95651f913251875b4cc8275644e0e28e82c63
Successfully built dynamic-network-architectures
Installing collected packages: dynamic-network-architectures
Successfully installed dynamic-network-architectures-0.3.1
Collecting tqdm
  Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
     -------------------------------------- 57.7/57.7 kB 504.6 kB/s eta 0:00:00
Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
   ---------------------------------------- 78.5/78.5 kB 2.2 MB/s eta 0:00:00
Installing collected packages: tqdm
Successfully installed tqdm-4.67.1
Collecting colorama
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: colorama
Successfully installed colorama-0.4.6
Collecting dicom2nifti
  Downloading dicom2nifti-2.5.1-py3-none-any.whl.metadata (1.3 kB)
Downloading dicom2nifti-2.5.1-py3-none-any.whl (43 kB)
   ---------------------------------------- 43.6/43.6 kB 710.8 kB/s eta 0:00:00
Installing collected packages: dicom2nifti
Successfully installed dicom2nifti-2.5.1
Collecting nibabel
  Downloading nibabel-5.3.2-py3-none-any.whl.metadata (9.1 kB)
Downloading nibabel-5.3.2-py3-none-any.whl (3.3 MB)
   ---------------------------------------- 3.3/3.3 MB 5.5 MB/s eta 0:00:00
Installing collected packages: nibabel
Successfully installed nibabel-5.3.2
Collecting importlib-resources&gt;=5.12
  Downloading importlib_resources-6.4.5-py3-none-any.whl.metadata (4.0 kB)
Downloading importlib_resources-6.4.5-py3-none-any.whl (36 kB)
Installing collected packages: importlib-resources
Successfully installed importlib-resources-6.4.5
Collecting zipp&gt;=3.1.0
  Downloading zipp-3.21.0-py3-none-any.whl.metadata (3.7 kB)
Downloading zipp-3.21.0-py3-none-any.whl (9.6 kB)
Installing collected packages: zipp
Successfully installed zipp-3.21.0
Collecting python-gdcm
  Downloading python_gdcm-3.0.24.1-cp39-cp39-win_amd64.whl.metadata (3.8 kB)
Downloading python_gdcm-3.0.24.1-cp39-cp39-win_amd64.whl (28.9 MB)
   ---------------------------------------- 28.9/28.9 MB 7.3 MB/s eta 0:00:00
Installing collected packages: python-gdcm
Successfully installed python-gdcm-3.0.24.1
Collecting batchgenerators&gt;=0.25
  Downloading batchgenerators-0.25.1.tar.gz (76 kB)
     -------------------------------------- 77.0/77.0 kB 855.5 kB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Building wheels for collected packages: batchgenerators
  Building wheel for batchgenerators (setup.py): started
  Building wheel for batchgenerators (setup.py): finished with status 'done'
  Created wheel for batchgenerators: filename=batchgenerators-0.25.1-py3-none-any.whl size=93102 sha256=7fa22821f6ad387b26dca74114bb8ee5ec32751344b282bc631f14e1c3fe884f
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\97\8d\b9\3a9435d619b6a4bcd98f8cb8b324da29b6173555bb80860bdd
Successfully built batchgenerators
Installing collected packages: batchgenerators
Successfully installed batchgenerators-0.25.1
Collecting scikit-image
  Downloading scikit_image-0.24.0-cp39-cp39-win_amd64.whl.metadata (14 kB)
Downloading scikit_image-0.24.0-cp39-cp39-win_amd64.whl (12.9 MB)
   ---------------------------------------- 12.9/12.9 MB 5.1 MB/s eta 0:00:00
Installing collected packages: scikit-image
Successfully installed scikit-image-0.24.0
Collecting networkx&gt;=2.8
  Downloading networkx-3.2.1-py3-none-any.whl.metadata (5.2 kB)
Downloading networkx-3.2.1-py3-none-any.whl (1.6 MB)
   ---------------------------------------- 1.6/1.6 MB 5.2 MB/s eta 0:00:00
Installing collected packages: networkx
Successfully installed networkx-3.2.1
Collecting imageio&gt;=2.33
  Downloading imageio-2.36.1-py3-none-any.whl.metadata (5.2 kB)
Downloading imageio-2.36.1-py3-none-any.whl (315 kB)
   ---------------------------------------- 315.4/315.4 kB 2.2 MB/s eta 0:00:00
Installing collected packages: imageio
Successfully installed imageio-2.36.1
Collecting tifffile&gt;=2022.8.12
  Downloading tifffile-2024.8.30-py3-none-any.whl.metadata (31 kB)
Downloading tifffile-2024.8.30-py3-none-any.whl (227 kB)
   ---------------------------------------- 227.3/227.3 kB 2.8 MB/s eta 0:00:00
Installing collected packages: tifffile
Successfully installed tifffile-2024.8.30
Collecting lazy-loader&gt;=0.4
  Downloading lazy_loader-0.4-py3-none-any.whl.metadata (7.6 kB)
Downloading lazy_loader-0.4-py3-none-any.whl (12 kB)
Installing collected packages: lazy-loader
Successfully installed lazy-loader-0.4
Collecting scikit-learn
  Downloading scikit_learn-1.6.0-cp39-cp39-win_amd64.whl.metadata (15 kB)
Downloading scikit_learn-1.6.0-cp39-cp39-win_amd64.whl (11.1 MB)
   ---------------------------------------- 11.1/11.1 MB 7.7 MB/s eta 0:00:00
Installing collected packages: scikit-learn
Successfully installed scikit-learn-1.6.0
Collecting joblib&gt;=1.2.0
  Downloading joblib-1.4.2-py3-none-any.whl.metadata (5.4 kB)
Downloading joblib-1.4.2-py3-none-any.whl (301 kB)
   ---------------------------------------- 301.8/301.8 kB 1.7 MB/s eta 0:00:00
Installing collected packages: joblib
Successfully installed joblib-1.4.2
Collecting threadpoolctl&gt;=3.1.0
  Downloading threadpoolctl-3.5.0-py3-none-any.whl.metadata (13 kB)
Downloading threadpoolctl-3.5.0-py3-none-any.whl (18 kB)
Installing collected packages: threadpoolctl
Successfully installed threadpoolctl-3.5.0
Collecting future
  Downloading future-1.0.0-py3-none-any.whl.metadata (4.0 kB)
Downloading future-1.0.0-py3-none-any.whl (491 kB)
   -------------------------------------- 491.3/491.3 kB 962.2 kB/s eta 0:00:00
Installing collected packages: future
Successfully installed future-1.0.0
Collecting pandas
  Downloading pandas-2.2.3-cp39-cp39-win_amd64.whl.metadata (19 kB)
Downloading pandas-2.2.3-cp39-cp39-win_amd64.whl (11.6 MB)
   ---------------------------------------- 11.6/11.6 MB 6.2 MB/s eta 0:00:00
Installing collected packages: pandas
Successfully installed pandas-2.2.3
Collecting pytz&gt;=2020.1
  Downloading pytz-2024.2-py2.py3-none-any.whl.metadata (22 kB)
Downloading pytz-2024.2-py2.py3-none-any.whl (508 kB)
   ---------------------------------------- 508.0/508.0 kB 3.2 MB/s eta 0:00:00
Installing collected packages: pytz
Successfully installed pytz-2024.2
Collecting tzdata&gt;=2022.7
  Downloading tzdata-2024.2-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading tzdata-2024.2-py2.py3-none-any.whl (346 kB)
   ---------------------------------------- 346.6/346.6 kB 2.2 MB/s eta 0:00:00
Installing collected packages: tzdata
Successfully installed tzdata-2024.2
Collecting unittest2
  Downloading unittest2-1.1.0-py2.py3-none-any.whl.metadata (15 kB)
Downloading unittest2-1.1.0-py2.py3-none-any.whl (96 kB)
   ---------------------------------------- 96.4/96.4 kB 1.4 MB/s eta 0:00:00
Installing collected packages: unittest2
Successfully installed unittest2-1.1.0
Collecting argparse
  Downloading argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
Downloading argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Installing collected packages: argparse
Successfully installed argparse-1.4.0
Collecting traceback2
  Downloading traceback2-1.4.0-py2.py3-none-any.whl.metadata (1.5 kB)
Downloading traceback2-1.4.0-py2.py3-none-any.whl (16 kB)
Installing collected packages: traceback2
Successfully installed traceback2-1.4.0
Collecting linecache2
  Downloading linecache2-1.0.0-py2.py3-none-any.whl.metadata (1000 bytes)
Downloading linecache2-1.0.0-py2.py3-none-any.whl (12 kB)
Installing collected packages: linecache2
Successfully installed linecache2-1.0.0
Collecting graphviz
  Downloading graphviz-0.20.3-py3-none-any.whl.metadata (12 kB)
Downloading graphviz-0.20.3-py3-none-any.whl (47 kB)
   ---------------------------------------- 47.1/47.1 kB 784.8 kB/s eta 0:00:00
Installing collected packages: graphviz
Successfully installed graphviz-0.20.3
Collecting matplotlib
  Downloading matplotlib-3.9.4-cp39-cp39-win_amd64.whl.metadata (11 kB)
Downloading matplotlib-3.9.4-cp39-cp39-win_amd64.whl (7.8 MB)
   ---------------------------------------- 7.8/7.8 MB 5.1 MB/s eta 0:00:00
Installing collected packages: matplotlib
Successfully installed matplotlib-3.9.4
Collecting contourpy&gt;=1.0.1
  Downloading contourpy-1.3.0-cp39-cp39-win_amd64.whl.metadata (5.4 kB)
Downloading contourpy-1.3.0-cp39-cp39-win_amd64.whl (211 kB)
   ---------------------------------------- 211.8/211.8 kB 1.3 MB/s eta 0:00:00
Installing collected packages: contourpy
Successfully installed contourpy-1.3.0
Collecting cycler&gt;=0.10
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Installing collected packages: cycler
Successfully installed cycler-0.12.1
Collecting fonttools&gt;=4.22.0
  Downloading fonttools-4.55.3-cp39-cp39-win_amd64.whl.metadata (168 kB)
     -------------------------------------- 168.5/168.5 kB 1.3 MB/s eta 0:00:00
Downloading fonttools-4.55.3-cp39-cp39-win_amd64.whl (2.2 MB)
   ---------------------------------------- 2.2/2.2 MB 7.8 MB/s eta 0:00:00
Installing collected packages: fonttools
Successfully installed fonttools-4.55.3
Collecting kiwisolver&gt;=1.3.1
  Downloading kiwisolver-1.4.7-cp39-cp39-win_amd64.whl.metadata (6.4 kB)
Downloading kiwisolver-1.4.7-cp39-cp39-win_amd64.whl (55 kB)
   ---------------------------------------- 55.8/55.8 kB 723.9 kB/s eta 0:00:00
Installing collected packages: kiwisolver
Successfully installed kiwisolver-1.4.7
Collecting seaborn
  Downloading seaborn-0.13.2-py3-none-any.whl.metadata (5.4 kB)
Downloading seaborn-0.13.2-py3-none-any.whl (294 kB)
   ---------------------------------------- 294.9/294.9 kB 2.0 MB/s eta 0:00:00
Installing collected packages: seaborn
Successfully installed seaborn-0.13.2
Collecting imagecodecs
  Downloading imagecodecs-2024.12.30-1-cp39-cp39-win_amd64.whl.metadata (19 kB)
Downloading imagecodecs-2024.12.30-1-cp39-cp39-win_amd64.whl (28.9 MB)
   ---------------------------------------- 28.9/28.9 MB 6.2 MB/s eta 0:00:00
Installing collected packages: imagecodecs
Successfully installed imagecodecs-2024.12.30
Collecting yacs
  Downloading yacs-0.1.8-py3-none-any.whl.metadata (639 bytes)
Downloading yacs-0.1.8-py3-none-any.whl (14 kB)
Installing collected packages: yacs
Successfully installed yacs-0.1.8
Collecting PyYAML
  Downloading PyYAML-6.0.2-cp39-cp39-win_amd64.whl.metadata (2.1 kB)
Downloading PyYAML-6.0.2-cp39-cp39-win_amd64.whl (162 kB)
   ---------------------------------------- 162.3/162.3 kB 1.2 MB/s eta 0:00:00
Installing collected packages: PyYAML
Successfully installed PyYAML-6.0.2
Collecting batchgeneratorsv2&gt;=0.2
  Downloading batchgeneratorsv2-0.2.1.tar.gz (34 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: batchgeneratorsv2
  Building wheel for batchgeneratorsv2 (pyproject.toml): started
  Building wheel for batchgeneratorsv2 (pyproject.toml): finished with status 'done'
  Created wheel for batchgeneratorsv2: filename=batchgeneratorsv2-0.2.1-py3-none-any.whl size=45216 sha256=c96d79d541dec23011b7579b7316308b08850017ece1a5a1dd0a91958be7f5a2
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\8c\29\14\3fdf4a97638724355746fb142b55db6868f1c0f1698af26ebd
Successfully built batchgeneratorsv2
Installing collected packages: batchgeneratorsv2
Successfully installed batchgeneratorsv2-0.2.1
Collecting fft-conv-pytorch
  Downloading fft_conv_pytorch-1.2.0-py3-none-any.whl.metadata (2.8 kB)
Downloading fft_conv_pytorch-1.2.0-py3-none-any.whl (6.8 kB)
Installing collected packages: fft-conv-pytorch
Successfully installed fft-conv-pytorch-1.2.0
Collecting einops
  Downloading einops-0.8.0-py3-none-any.whl.metadata (12 kB)
Downloading einops-0.8.0-py3-none-any.whl (43 kB)
   ---------------------------------------- 43.2/43.2 kB 1.0 MB/s eta 0:00:00
Installing collected packages: einops
Successfully installed einops-0.8.0
Collecting light-the-torch&gt;=0.5
  Downloading light_the_torch-0.8.0-py3-none-any.whl.metadata (9.3 kB)
Requirement already satisfied: pip&lt;24.4,&gt;=22.3 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from light-the-torch&gt;=0.5) (24.0)
Downloading light_the_torch-0.8.0-py3-none-any.whl (14 kB)
Installing collected packages: light-the-torch
Successfully installed light-the-torch-0.8.0
Collecting torch&gt;=2.1.2
  Downloading https://download.pytorch.org/whl/cu124/torch-2.5.1%2Bcu124-cp39-cp39-win_amd64.whl (2510.7 MB)
     ---------------------------------------- 2.5/2.5 GB 2.0 MB/s eta 0:00:00
Collecting torchvision
  Downloading https://download.pytorch.org/whl/cu124/torchvision-0.20.1%2Bcu124-cp39-cp39-win_amd64.whl (6.1 MB)
     ---------------------------------------- 6.1/6.1 MB 14.0 MB/s eta 0:00:00
Collecting filelock (from torch&gt;=2.1.2)
  Downloading https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl (11 kB)
Requirement already satisfied: typing-extensions&gt;=4.8.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch&gt;=2.1.2) (4.12.1)
Requirement already satisfied: networkx in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch&gt;=2.1.2) (3.2.1)
Collecting jinja2 (from torch&gt;=2.1.2)
  Downloading jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting fsspec (from torch&gt;=2.1.2)
  Downloading https://download.pytorch.org/whl/fsspec-2024.2.0-py3-none-any.whl (170 kB)
     -------------------------------------- 170.9/170.9 kB 5.2 MB/s eta 0:00:00
Collecting sympy==1.13.1 (from torch&gt;=2.1.2)
  Downloading https://download.pytorch.org/whl/sympy-1.13.1-py3-none-any.whl (6.2 MB)
     ---------------------------------------- 6.2/6.2 MB 18.0 MB/s eta 0:00:00
Collecting mpmath&lt;1.4,&gt;=1.1.0 (from sympy==1.13.1-&gt;torch&gt;=2.1.2)
  Downloading https://download.pytorch.org/whl/mpmath-1.3.0-py3-none-any.whl (536 kB)
     ------------------------------------- 536.2/536.2 kB 17.0 MB/s eta 0:00:00
Requirement already satisfied: numpy in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torchvision) (1.26.4)
Requirement already satisfied: pillow!=8.3.*,&gt;=5.3.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torchvision) (10.3.0)
Collecting MarkupSafe&gt;=2.0 (from jinja2-&gt;torch&gt;=2.1.2)
  Downloading MarkupSafe-3.0.2-cp39-cp39-win_amd64.whl.metadata (4.1 kB)
Downloading jinja2-3.1.5-py3-none-any.whl (134 kB)
   ---------------------------------------- 134.6/134.6 kB 1.6 MB/s eta 0:00:00
Downloading MarkupSafe-3.0.2-cp39-cp39-win_amd64.whl (15 kB)
Installing collected packages: mpmath, sympy, MarkupSafe, fsspec, filelock, jinja2, torch, torchvision
Successfully installed MarkupSafe-3.0.2 filelock-3.13.1 fsspec-2024.2.0 jinja2-3.1.5 mpmath-1.3.0 sympy-1.13.1 torch-2.5.1+cu124 torchvision-0.20.1+cu124
Collecting acvl_utils==0.2
  Downloading acvl_utils-0.2.tar.gz (18 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: numpy in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (1.26.4)
Requirement already satisfied: batchgenerators in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (0.25.1)
Requirement already satisfied: torch in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (2.5.1+cu124)
Requirement already satisfied: SimpleITK in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (2.4.0rc2.dev213)
Requirement already satisfied: scikit-image in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (0.24.0)
Collecting connected-components-3d (from acvl_utils==0.2)
  Downloading connected_components_3d-3.22.0-cp39-cp39-win_amd64.whl.metadata (32 kB)
Requirement already satisfied: pillow&gt;=7.1.2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (10.3.0)
Requirement already satisfied: scipy in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.13.1)
Requirement already satisfied: scikit-learn in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.6.0)
Requirement already satisfied: future in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.0.0)
Requirement already satisfied: pandas in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (2.2.3)
Requirement already satisfied: unittest2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.1.0)
Requirement already satisfied: threadpoolctl in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (3.5.0)
Requirement already satisfied: networkx&gt;=2.8 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (3.2.1)
Requirement already satisfied: imageio&gt;=2.33 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (2.36.1)
Requirement already satisfied: tifffile&gt;=2022.8.12 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (2024.8.30)
Requirement already satisfied: packaging&gt;=21 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (24.0)
Requirement already satisfied: lazy-loader&gt;=0.4 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (0.4)
Requirement already satisfied: filelock in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (3.13.1)
Requirement already satisfied: typing-extensions&gt;=4.8.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (4.12.1)
Requirement already satisfied: jinja2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (3.1.5)
Requirement already satisfied: fsspec in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (2024.2.0)
Requirement already satisfied: sympy==1.13.1 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (1.13.1)
Requirement already satisfied: mpmath&lt;1.4,&gt;=1.1.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from sympy==1.13.1-&gt;torch-&gt;acvl_utils==0.2) (1.3.0)
Requirement already satisfied: MarkupSafe&gt;=2.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from jinja2-&gt;torch-&gt;acvl_utils==0.2) (3.0.2)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2024.2)
Requirement already satisfied: tzdata&gt;=2022.7 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2024.2)
Requirement already satisfied: joblib&gt;=1.2.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-learn-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.4.2)
Collecting argparse (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2)
  Using cached argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: six&gt;=1.4 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.16.0)
Requirement already satisfied: traceback2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.4.0)
Requirement already satisfied: linecache2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from traceback2-&gt;unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.0.0)
Downloading connected_components_3d-3.22.0-cp39-cp39-win_amd64.whl (545 kB)
   -------------------------------------- 545.5/545.5 kB 978.5 kB/s eta 0:00:00
Using cached argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Building wheels for collected packages: acvl_utils
  Building wheel for acvl_utils (setup.py): started
  Building wheel for acvl_utils (setup.py): finished with status 'done'
  Created wheel for acvl_utils: filename=acvl_utils-0.2-py3-none-any.whl size=22450 sha256=4dd58631f62b974d173a462023400c9d5b970cc13535e2723716f15d424e3f5b
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\db\79\df\6ffb48299bba36fd2fc5d14dc8ae7d1caa3416aa7e96d605b7
Successfully built acvl_utils
Installing collected packages: argparse, connected-components-3d, acvl_utils
Successfully installed acvl_utils-0.2 argparse-1.4.0 connected-components-3d-3.22.0
```
&lt;/details&gt;

## Testing with SlicerTotalSegmentator
I have also tested this in the context of [SlicerTotalSegmentator](https://github.com/lassoan/SlicerTotalSegmentator) . I have issued https://github.com/lassoan/SlicerTotalSegmentator/pull/67 to switch SlicerTotalSegmentator to also use SlicerNNUnet extension to avoid this situation again where SlicerTotalSegmentator got fixes that SlicerNNUNet did not get. I used a fresh install of Slicer 5.7.0-2024-12-31 with a cleared out system pip cache so that all downloads would be fresh.

![image](https://github.com/user-attachments/assets/aa47c1a1-ea49-491f-a6ea-929d8b51aaa1)


&lt;details&gt;
  &lt;summary&gt;SlicerTotalSegmentator python console output click here&lt;/summary&gt;

```python
Python 3.9.10 (main, Dec 31 2024, 23:19:20) [MSC v.1939 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
Collecting pandas
  Downloading pandas-2.2.3-cp39-cp39-win_amd64.whl.metadata (19 kB)
Requirement already satisfied: numpy&gt;=1.22.4 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from pandas) (1.26.4)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from pandas) (2.9.0.post0)
Collecting pytz&gt;=2020.1 (from pandas)
  Downloading pytz-2024.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata&gt;=2022.7 (from pandas)
  Downloading tzdata-2024.2-py2.py3-none-any.whl.metadata (1.4 kB)
Requirement already satisfied: six&gt;=1.5 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from python-dateutil&gt;=2.8.2-&gt;pandas) (1.16.0)
Downloading pandas-2.2.3-cp39-cp39-win_amd64.whl (11.6 MB)
   ---------------------------------------- 11.6/11.6 MB 6.5 MB/s eta 0:00:00
Downloading pytz-2024.2-py2.py3-none-any.whl (508 kB)
   ---------------------------------------- 508.0/508.0 kB 8.0 MB/s eta 0:00:00
Downloading tzdata-2024.2-py2.py3-none-any.whl (346 kB)
   ---------------------------------------- 346.6/346.6 kB 2.0 MB/s eta 0:00:00
Installing collected packages: pytz, tzdata, pandas
Successfully installed pandas-2.2.3 pytz-2024.2 tzdata-2024.2
Collecting light-the-torch&gt;=0.5
  Downloading light_the_torch-0.8.0-py3-none-any.whl.metadata (9.3 kB)
Requirement already satisfied: pip&lt;24.4,&gt;=22.3 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from light-the-torch&gt;=0.5) (24.0)
Downloading light_the_torch-0.8.0-py3-none-any.whl (14 kB)
Installing collected packages: light-the-torch
Successfully installed light-the-torch-0.8.0
Collecting torch&gt;=2.0.0
  Downloading https://download.pytorch.org/whl/cu124/torch-2.5.1%2Bcu124-cp39-cp39-win_amd64.whl (2510.7 MB)
     ---------------------------------------- 2.5/2.5 GB 1.4 MB/s eta 0:00:00
Collecting torchvision
  Downloading https://download.pytorch.org/whl/cu124/torchvision-0.20.1%2Bcu124-cp39-cp39-win_amd64.whl (6.1 MB)
     ---------------------------------------- 6.1/6.1 MB 16.4 MB/s eta 0:00:00
Collecting filelock (from torch&gt;=2.0.0)
  Downloading https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl (11 kB)
Requirement already satisfied: typing-extensions&gt;=4.8.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch&gt;=2.0.0) (4.12.1)
Collecting networkx (from torch&gt;=2.0.0)
  Downloading https://download.pytorch.org/whl/networkx-3.2.1-py3-none-any.whl (1.6 MB)
     ---------------------------------------- 1.6/1.6 MB 17.6 MB/s eta 0:00:00
Collecting jinja2 (from torch&gt;=2.0.0)
  Downloading jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting fsspec (from torch&gt;=2.0.0)
  Downloading https://download.pytorch.org/whl/fsspec-2024.2.0-py3-none-any.whl (170 kB)
     ------------------------------------- 170.9/170.9 kB 10.0 MB/s eta 0:00:00
Collecting sympy==1.13.1 (from torch&gt;=2.0.0)
  Downloading https://download.pytorch.org/whl/sympy-1.13.1-py3-none-any.whl (6.2 MB)
     ---------------------------------------- 6.2/6.2 MB 18.8 MB/s eta 0:00:00
Collecting mpmath&lt;1.4,&gt;=1.1.0 (from sympy==1.13.1-&gt;torch&gt;=2.0.0)
  Downloading https://download.pytorch.org/whl/mpmath-1.3.0-py3-none-any.whl (536 kB)
     ------------------------------------- 536.2/536.2 kB 17.0 MB/s eta 0:00:00
Requirement already satisfied: numpy in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torchvision) (1.26.4)
Requirement already satisfied: pillow!=8.3.*,&gt;=5.3.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torchvision) (10.3.0)
Collecting MarkupSafe&gt;=2.0 (from jinja2-&gt;torch&gt;=2.0.0)
  Downloading MarkupSafe-3.0.2-cp39-cp39-win_amd64.whl.metadata (4.1 kB)
Downloading jinja2-3.1.5-py3-none-any.whl (134 kB)
   ---------------------------------------- 134.6/134.6 kB 1.6 MB/s eta 0:00:00
Downloading MarkupSafe-3.0.2-cp39-cp39-win_amd64.whl (15 kB)
Installing collected packages: mpmath, sympy, networkx, MarkupSafe, fsspec, filelock, jinja2, torch, torchvision
Successfully installed MarkupSafe-3.0.2 filelock-3.13.1 fsspec-2024.2.0 jinja2-3.1.5 mpmath-1.3.0 networkx-3.2.1 sympy-1.13.1 torch-2.5.1+cu124 torchvision-0.20.1+cu124
Collecting nnunetv2&gt;=2.2.1
  Downloading nnunetv2-2.5.1.tar.gz (196 kB)
     -------------------------------------- 197.0/197.0 kB 1.5 MB/s eta 0:00:00
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: nnunetv2
  Building wheel for nnunetv2 (pyproject.toml): started
  Building wheel for nnunetv2 (pyproject.toml): finished with status 'done'
  Created wheel for nnunetv2: filename=nnunetv2-2.5.1-py3-none-any.whl size=264428 sha256=2ad70af904a73190ecb38046a84d569b352f8421d6ca8b1a94ad512667b946c7
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\7b\85\af\51e5381b7cf9cc417ca071b9cd6e35afc59236a0ebb4462249
Successfully built nnunetv2
Installing collected packages: nnunetv2
Successfully installed nnunetv2-2.5.1
Collecting dynamic-network-architectures&lt;0.4,&gt;=0.3.1
  Downloading dynamic_network_architectures-0.3.1.tar.gz (20 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Building wheels for collected packages: dynamic-network-architectures
  Building wheel for dynamic-network-architectures (setup.py): started
  Building wheel for dynamic-network-architectures (setup.py): finished with status 'done'
  Created wheel for dynamic-network-architectures: filename=dynamic_network_architectures-0.3.1-py3-none-any.whl size=30056 sha256=8d7546a50ebdfbade048f7fcc67b577fd5b25971518e75e949b378afda3f6fc1
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\ec\59\c1\e65ad8b5ac7df95651f913251875b4cc8275644e0e28e82c63
Successfully built dynamic-network-architectures
Installing collected packages: dynamic-network-architectures
Successfully installed dynamic-network-architectures-0.3.1
Collecting tqdm
  Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
     -------------------------------------- 57.7/57.7 kB 435.2 kB/s eta 0:00:00
Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
   ---------------------------------------- 78.5/78.5 kB 2.2 MB/s eta 0:00:00
Installing collected packages: tqdm
Successfully installed tqdm-4.67.1
Collecting colorama
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: colorama
Successfully installed colorama-0.4.6
Collecting dicom2nifti
  Downloading dicom2nifti-2.5.1-py3-none-any.whl.metadata (1.3 kB)
Downloading dicom2nifti-2.5.1-py3-none-any.whl (43 kB)
   ---------------------------------------- 43.6/43.6 kB 710.8 kB/s eta 0:00:00
Installing collected packages: dicom2nifti
Successfully installed dicom2nifti-2.5.1
Collecting nibabel
  Downloading nibabel-5.3.2-py3-none-any.whl.metadata (9.1 kB)
Downloading nibabel-5.3.2-py3-none-any.whl (3.3 MB)
   ---------------------------------------- 3.3/3.3 MB 5.7 MB/s eta 0:00:00
Installing collected packages: nibabel
Successfully installed nibabel-5.3.2
Collecting importlib-resources&gt;=5.12
  Downloading importlib_resources-6.4.5-py3-none-any.whl.metadata (4.0 kB)
Downloading importlib_resources-6.4.5-py3-none-any.whl (36 kB)
Installing collected packages: importlib-resources
Successfully installed importlib-resources-6.4.5
Collecting zipp&gt;=3.1.0
  Downloading zipp-3.21.0-py3-none-any.whl.metadata (3.7 kB)
Downloading zipp-3.21.0-py3-none-any.whl (9.6 kB)
Installing collected packages: zipp
Successfully installed zipp-3.21.0
Collecting python-gdcm
  Downloading python_gdcm-3.0.24.1-cp39-cp39-win_amd64.whl.metadata (3.8 kB)
Downloading python_gdcm-3.0.24.1-cp39-cp39-win_amd64.whl (28.9 MB)
   ---------------------------------------- 28.9/28.9 MB 4.8 MB/s eta 0:00:00
Installing collected packages: python-gdcm
Successfully installed python-gdcm-3.0.24.1
Collecting batchgenerators&gt;=0.25
  Downloading batchgenerators-0.25.1.tar.gz (76 kB)
     -------------------------------------- 77.0/77.0 kB 717.5 kB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Building wheels for collected packages: batchgenerators
  Building wheel for batchgenerators (setup.py): started
  Building wheel for batchgenerators (setup.py): finished with status 'done'
  Created wheel for batchgenerators: filename=batchgenerators-0.25.1-py3-none-any.whl size=93102 sha256=ef464be755e76bb5c5f81ec906759fcf230d0aecd0aaa1c655e8072c0a965788
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\97\8d\b9\3a9435d619b6a4bcd98f8cb8b324da29b6173555bb80860bdd
Successfully built batchgenerators
Installing collected packages: batchgenerators
Successfully installed batchgenerators-0.25.1
Collecting scikit-image
  Downloading scikit_image-0.24.0-cp39-cp39-win_amd64.whl.metadata (14 kB)
Downloading scikit_image-0.24.0-cp39-cp39-win_amd64.whl (12.9 MB)
   ---------------------------------------- 12.9/12.9 MB 5.3 MB/s eta 0:00:00
Installing collected packages: scikit-image
Successfully installed scikit-image-0.24.0
Collecting imageio&gt;=2.33
  Downloading imageio-2.36.1-py3-none-any.whl.metadata (5.2 kB)
Downloading imageio-2.36.1-py3-none-any.whl (315 kB)
   ---------------------------------------- 315.4/315.4 kB 2.4 MB/s eta 0:00:00
Installing collected packages: imageio
Successfully installed imageio-2.36.1
Collecting tifffile&gt;=2022.8.12
  Downloading tifffile-2024.8.30-py3-none-any.whl.metadata (31 kB)
Downloading tifffile-2024.8.30-py3-none-any.whl (227 kB)
   ---------------------------------------- 227.3/227.3 kB 3.5 MB/s eta 0:00:00
Installing collected packages: tifffile
Successfully installed tifffile-2024.8.30
Collecting lazy-loader&gt;=0.4
  Downloading lazy_loader-0.4-py3-none-any.whl.metadata (7.6 kB)
Downloading lazy_loader-0.4-py3-none-any.whl (12 kB)
Installing collected packages: lazy-loader
Successfully installed lazy-loader-0.4
Collecting scikit-learn
  Downloading scikit_learn-1.6.0-cp39-cp39-win_amd64.whl.metadata (15 kB)
Downloading scikit_learn-1.6.0-cp39-cp39-win_amd64.whl (11.1 MB)
   ---------------------------------------- 11.1/11.1 MB 6.2 MB/s eta 0:00:00
Installing collected packages: scikit-learn
Successfully installed scikit-learn-1.6.0
Collecting joblib&gt;=1.2.0
  Downloading joblib-1.4.2-py3-none-any.whl.metadata (5.4 kB)
Downloading joblib-1.4.2-py3-none-any.whl (301 kB)
   ---------------------------------------- 301.8/301.8 kB 1.6 MB/s eta 0:00:00
Installing collected packages: joblib
Successfully installed joblib-1.4.2
Collecting threadpoolctl&gt;=3.1.0
  Downloading threadpoolctl-3.5.0-py3-none-any.whl.metadata (13 kB)
Downloading threadpoolctl-3.5.0-py3-none-any.whl (18 kB)
Installing collected packages: threadpoolctl
Successfully installed threadpoolctl-3.5.0
Collecting future
  Downloading future-1.0.0-py3-none-any.whl.metadata (4.0 kB)
Downloading future-1.0.0-py3-none-any.whl (491 kB)
   ---------------------------------------- 491.3/491.3 kB 2.8 MB/s eta 0:00:00
Installing collected packages: future
Successfully installed future-1.0.0
Collecting unittest2
  Downloading unittest2-1.1.0-py2.py3-none-any.whl.metadata (15 kB)
Downloading unittest2-1.1.0-py2.py3-none-any.whl (96 kB)
   ---------------------------------------- 96.4/96.4 kB 1.4 MB/s eta 0:00:00
Installing collected packages: unittest2
Successfully installed unittest2-1.1.0
Collecting argparse
  Downloading argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
Downloading argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Installing collected packages: argparse
Successfully installed argparse-1.4.0
Collecting traceback2
  Downloading traceback2-1.4.0-py2.py3-none-any.whl.metadata (1.5 kB)
Downloading traceback2-1.4.0-py2.py3-none-any.whl (16 kB)
Installing collected packages: traceback2
Successfully installed traceback2-1.4.0
Collecting linecache2
  Downloading linecache2-1.0.0-py2.py3-none-any.whl.metadata (1000 bytes)
Downloading linecache2-1.0.0-py2.py3-none-any.whl (12 kB)
Installing collected packages: linecache2
Successfully installed linecache2-1.0.0
Collecting graphviz
  Downloading graphviz-0.20.3-py3-none-any.whl.metadata (12 kB)
Downloading graphviz-0.20.3-py3-none-any.whl (47 kB)
   ---------------------------------------- 47.1/47.1 kB 784.8 kB/s eta 0:00:00
Installing collected packages: graphviz
Successfully installed graphviz-0.20.3
Collecting matplotlib
  Downloading matplotlib-3.9.4-cp39-cp39-win_amd64.whl.metadata (11 kB)
Downloading matplotlib-3.9.4-cp39-cp39-win_amd64.whl (7.8 MB)
   ---------------------------------------- 7.8/7.8 MB 4.5 MB/s eta 0:00:00
Installing collected packages: matplotlib
Successfully installed matplotlib-3.9.4
Collecting contourpy&gt;=1.0.1
  Downloading contourpy-1.3.0-cp39-cp39-win_amd64.whl.metadata (5.4 kB)
Downloading contourpy-1.3.0-cp39-cp39-win_amd64.whl (211 kB)
   ---------------------------------------- 211.8/211.8 kB 1.1 MB/s eta 0:00:00
Installing collected packages: contourpy
Successfully installed contourpy-1.3.0
Collecting cycler&gt;=0.10
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Installing collected packages: cycler
Successfully installed cycler-0.12.1
Collecting fonttools&gt;=4.22.0
  Downloading fonttools-4.55.3-cp39-cp39-win_amd64.whl.metadata (168 kB)
     -------------------------------------- 168.5/168.5 kB 2.6 MB/s eta 0:00:00
Downloading fonttools-4.55.3-cp39-cp39-win_amd64.whl (2.2 MB)
   ---------------------------------------- 2.2/2.2 MB 4.7 MB/s eta 0:00:00
Installing collected packages: fonttools
Successfully installed fonttools-4.55.3
Collecting kiwisolver&gt;=1.3.1
  Downloading kiwisolver-1.4.7-cp39-cp39-win_amd64.whl.metadata (6.4 kB)
Downloading kiwisolver-1.4.7-cp39-cp39-win_amd64.whl (55 kB)
   ---------------------------------------- 55.8/55.8 kB 723.9 kB/s eta 0:00:00
Installing collected packages: kiwisolver
Successfully installed kiwisolver-1.4.7
Collecting seaborn
  Downloading seaborn-0.13.2-py3-none-any.whl.metadata (5.4 kB)
Downloading seaborn-0.13.2-py3-none-any.whl (294 kB)
   ---------------------------------------- 294.9/294.9 kB 2.0 MB/s eta 0:00:00
Installing collected packages: seaborn
Successfully installed seaborn-0.13.2
Collecting imagecodecs
  Downloading imagecodecs-2024.12.30-1-cp39-cp39-win_amd64.whl.metadata (19 kB)
Downloading imagecodecs-2024.12.30-1-cp39-cp39-win_amd64.whl (28.9 MB)
   ---------------------------------------- 28.9/28.9 MB 5.5 MB/s eta 0:00:00
Installing collected packages: imagecodecs
Successfully installed imagecodecs-2024.12.30
Collecting yacs
  Downloading yacs-0.1.8-py3-none-any.whl.metadata (639 bytes)
Downloading yacs-0.1.8-py3-none-any.whl (14 kB)
Installing collected packages: yacs
Successfully installed yacs-0.1.8
Collecting PyYAML
  Downloading PyYAML-6.0.2-cp39-cp39-win_amd64.whl.metadata (2.1 kB)
Downloading PyYAML-6.0.2-cp39-cp39-win_amd64.whl (162 kB)
   ---------------------------------------- 162.3/162.3 kB 1.6 MB/s eta 0:00:00
Installing collected packages: PyYAML
Successfully installed PyYAML-6.0.2
Collecting batchgeneratorsv2&gt;=0.2
  Downloading batchgeneratorsv2-0.2.1.tar.gz (34 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: batchgeneratorsv2
  Building wheel for batchgeneratorsv2 (pyproject.toml): started
  Building wheel for batchgeneratorsv2 (pyproject.toml): finished with status 'done'
  Created wheel for batchgeneratorsv2: filename=batchgeneratorsv2-0.2.1-py3-none-any.whl size=45216 sha256=27475a00e9a4228188ad2a80b706c400c9d2bb41ba896ea4983e7fe54ad6b285
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\8c\29\14\3fdf4a97638724355746fb142b55db6868f1c0f1698af26ebd
Successfully built batchgeneratorsv2
Installing collected packages: batchgeneratorsv2
Successfully installed batchgeneratorsv2-0.2.1
Collecting fft-conv-pytorch
  Downloading fft_conv_pytorch-1.2.0-py3-none-any.whl.metadata (2.8 kB)
Downloading fft_conv_pytorch-1.2.0-py3-none-any.whl (6.8 kB)
Installing collected packages: fft-conv-pytorch
Successfully installed fft-conv-pytorch-1.2.0
Collecting einops
  Downloading einops-0.8.0-py3-none-any.whl.metadata (12 kB)
Downloading einops-0.8.0-py3-none-any.whl (43 kB)
   ---------------------------------------- 43.2/43.2 kB 701.8 kB/s eta 0:00:00
Installing collected packages: einops
Successfully installed einops-0.8.0
Collecting acvl_utils==0.2
  Downloading acvl_utils-0.2.tar.gz (18 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: numpy in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (1.26.4)
Requirement already satisfied: batchgenerators in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (0.25.1)
Requirement already satisfied: torch in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (2.5.1+cu124)
Requirement already satisfied: SimpleITK in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (2.4.0rc2.dev213)
Requirement already satisfied: scikit-image in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from acvl_utils==0.2) (0.24.0)
Collecting connected-components-3d (from acvl_utils==0.2)
  Downloading connected_components_3d-3.22.0-cp39-cp39-win_amd64.whl.metadata (32 kB)
Requirement already satisfied: pillow&gt;=7.1.2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (10.3.0)
Requirement already satisfied: scipy in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.13.1)
Requirement already satisfied: scikit-learn in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.6.0)
Requirement already satisfied: future in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.0.0)
Requirement already satisfied: pandas in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (2.2.3)
Requirement already satisfied: unittest2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.1.0)
Requirement already satisfied: threadpoolctl in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (3.5.0)
Requirement already satisfied: networkx&gt;=2.8 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (3.2.1)
Requirement already satisfied: imageio&gt;=2.33 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (2.36.1)
Requirement already satisfied: tifffile&gt;=2022.8.12 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (2024.8.30)
Requirement already satisfied: packaging&gt;=21 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (24.0)
Requirement already satisfied: lazy-loader&gt;=0.4 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (0.4)
Requirement already satisfied: filelock in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (3.13.1)
Requirement already satisfied: typing-extensions&gt;=4.8.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (4.12.1)
Requirement already satisfied: jinja2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (3.1.5)
Requirement already satisfied: fsspec in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (2024.2.0)
Requirement already satisfied: sympy==1.13.1 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (1.13.1)
Requirement already satisfied: mpmath&lt;1.4,&gt;=1.1.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from sympy==1.13.1-&gt;torch-&gt;acvl_utils==0.2) (1.3.0)
Requirement already satisfied: MarkupSafe&gt;=2.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from jinja2-&gt;torch-&gt;acvl_utils==0.2) (3.0.2)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2024.2)
Requirement already satisfied: tzdata&gt;=2022.7 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2024.2)
Requirement already satisfied: joblib&gt;=1.2.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from scikit-learn-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.4.2)
Collecting argparse (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2)
  Using cached argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: six&gt;=1.4 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.16.0)
Requirement already satisfied: traceback2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.4.0)
Requirement already satisfied: linecache2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from traceback2-&gt;unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.0.0)
Downloading connected_components_3d-3.22.0-cp39-cp39-win_amd64.whl (545 kB)
   ---------------------------------------- 545.5/545.5 kB 4.9 MB/s eta 0:00:00
Using cached argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Building wheels for collected packages: acvl_utils
  Building wheel for acvl_utils (setup.py): started
  Building wheel for acvl_utils (setup.py): finished with status 'done'
  Created wheel for acvl_utils: filename=acvl_utils-0.2-py3-none-any.whl size=22450 sha256=565173fa58e9c290bc076063b9a571d6180ba7ba9b545a89accc15ca6d731700
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\db\79\df\6ffb48299bba36fd2fc5d14dc8ae7d1caa3416aa7e96d605b7
Successfully built acvl_utils
Installing collected packages: argparse, connected-components-3d, acvl_utils
Successfully installed acvl_utils-0.2 argparse-1.4.0 connected-components-3d-3.22.0
Collecting https://github.com/wasserth/TotalSegmentator/archive/7274faac4673298d17b63a5a8335006f02e6d426.zip
  Downloading https://github.com/wasserth/TotalSegmentator/archive/7274faac4673298d17b63a5a8335006f02e6d426.zip
     / 8.3 MB 5.0 MB/s 0:00:01
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: TotalSegmentator
  Building wheel for TotalSegmentator (pyproject.toml): started
  Building wheel for TotalSegmentator (pyproject.toml): finished with status 'done'
  Created wheel for TotalSegmentator: filename=TotalSegmentator-2.4.0-py3-none-any.whl size=348319 sha256=d4b53e53e781f64db7518e79038ab07cd4dc3720572b612ce20068d3811b0560
  Stored in directory: C:\Users\butlej30383\AppData\Local\Temp\pip-ephem-wheel-cache-shop__u8\wheels\d8\41\ce\20b3efb2dd6cebf94e551445b85bf8412c77d640fe7bd41cbb
Successfully built TotalSegmentator
Installing collected packages: TotalSegmentator
Successfully installed TotalSegmentator-2.4.0
Requirement already satisfied: numpy&lt;2 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (1.26.4)
Requirement already satisfied: nibabel&gt;=2.3.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (5.3.2)
Requirement already satisfied: importlib-resources&gt;=5.12 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from nibabel&gt;=2.3.0) (6.4.5)
Requirement already satisfied: numpy&gt;=1.22 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from nibabel&gt;=2.3.0) (1.26.4)
Requirement already satisfied: packaging&gt;=20 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from nibabel&gt;=2.3.0) (24.0)
Requirement already satisfied: typing-extensions&gt;=4.6 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from nibabel&gt;=2.3.0) (4.12.1)
Requirement already satisfied: zipp&gt;=3.1.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from importlib-resources&gt;=5.12-&gt;nibabel&gt;=2.3.0) (3.21.0)
Requirement already satisfied: tqdm&gt;=4.45.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (4.67.1)
Requirement already satisfied: colorama in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from tqdm&gt;=4.45.0) (0.4.6)
Collecting p_tqdm
  Downloading p_tqdm-1.4.2.tar.gz (6.0 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: tqdm&gt;=4.45.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from p_tqdm) (4.67.1)
Collecting pathos&gt;=0.2.5 (from p_tqdm)
  Downloading pathos-0.3.3-py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: six&gt;=1.13.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from p_tqdm) (1.16.0)
Collecting ppft&gt;=1.7.6.9 (from pathos&gt;=0.2.5-&gt;p_tqdm)
  Downloading ppft-1.7.6.9-py3-none-any.whl.metadata (12 kB)
Collecting dill&gt;=0.3.9 (from pathos&gt;=0.2.5-&gt;p_tqdm)
  Downloading dill-0.3.9-py3-none-any.whl.metadata (10 kB)
Collecting pox&gt;=0.3.5 (from pathos&gt;=0.2.5-&gt;p_tqdm)
  Downloading pox-0.3.5-py3-none-any.whl.metadata (8.0 kB)
Collecting multiprocess&gt;=0.70.17 (from pathos&gt;=0.2.5-&gt;p_tqdm)
  Downloading multiprocess-0.70.17-py39-none-any.whl.metadata (7.2 kB)
Requirement already satisfied: colorama in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from tqdm&gt;=4.45.0-&gt;p_tqdm) (0.4.6)
Downloading pathos-0.3.3-py3-none-any.whl (82 kB)
   ---------------------------------------- 82.1/82.1 kB 2.3 MB/s eta 0:00:00
Downloading dill-0.3.9-py3-none-any.whl (119 kB)
   ---------------------------------------- 119.4/119.4 kB 7.3 MB/s eta 0:00:00
Downloading multiprocess-0.70.17-py39-none-any.whl (133 kB)
   ---------------------------------------- 133.4/133.4 kB 4.0 MB/s eta 0:00:00
Downloading pox-0.3.5-py3-none-any.whl (29 kB)
Downloading ppft-1.7.6.9-py3-none-any.whl (56 kB)
   ---------------------------------------- 56.8/56.8 kB 2.9 MB/s eta 0:00:00
Building wheels for collected packages: p_tqdm
  Building wheel for p_tqdm (setup.py): started
  Building wheel for p_tqdm (setup.py): finished with status 'done'
  Created wheel for p_tqdm: filename=p_tqdm-1.4.2-py3-none-any.whl size=5426 sha256=9d00808bc6b757918c57dd5b8b837d71eda38aff24337ede80b337a47e6fe134
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\c1\d1\fa\5b7790c4da9b335ab699bbb968084fc6faaf3187f3c16a908e
Successfully built p_tqdm
Installing collected packages: ppft, pox, dill, multiprocess, pathos, p_tqdm
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
totalsegmentator 2.4.0 requires pyarrow, which is not installed.
totalsegmentator 2.4.0 requires xvfbwrapper, which is not installed.
Successfully installed dill-0.3.9 multiprocess-0.70.17 p_tqdm-1.4.2 pathos-0.3.3 pox-0.3.5 ppft-1.7.6.9
Collecting xvfbwrapper
  Downloading xvfbwrapper-0.2.9.tar.gz (5.6 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Building wheels for collected packages: xvfbwrapper
  Building wheel for xvfbwrapper (setup.py): started
  Building wheel for xvfbwrapper (setup.py): finished with status 'done'
  Created wheel for xvfbwrapper: filename=xvfbwrapper-0.2.9-py3-none-any.whl size=5028 sha256=a4f52962b0dafc97ad74551b86c9da42d39ba63e9dea12a4a4c47261bbc25a88
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\aa\09\0e\c0fa4c721cfb0a003121597a24181add912b7488054d2311ad
Successfully built xvfbwrapper
Installing collected packages: xvfbwrapper
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
totalsegmentator 2.4.0 requires pyarrow, which is not installed.
Successfully installed xvfbwrapper-0.2.9
Requirement already satisfied: dicom2nifti in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (2.5.1)
Requirement already satisfied: nibabel in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from dicom2nifti) (5.3.2)
Requirement already satisfied: numpy in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from dicom2nifti) (1.26.4)
Requirement already satisfied: scipy in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from dicom2nifti) (1.13.1)
Requirement already satisfied: pydicom&gt;=2.2.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from dicom2nifti) (2.4.4)
Requirement already satisfied: python-gdcm in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from dicom2nifti) (3.0.24.1)
Requirement already satisfied: importlib-resources&gt;=5.12 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from nibabel-&gt;dicom2nifti) (6.4.5)
Requirement already satisfied: packaging&gt;=20 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from nibabel-&gt;dicom2nifti) (24.0)
Requirement already satisfied: typing-extensions&gt;=4.6 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from nibabel-&gt;dicom2nifti) (4.12.1)
Requirement already satisfied: zipp&gt;=3.1.0 in c:\users\butlej30383\appdata\local\slicer.org\slicer 5.7.0-2024-12-31\lib\python\lib\site-packages (from importlib-resources&gt;=5.12-&gt;nibabel-&gt;dicom2nifti) (3.21.0)
Collecting pyarrow
  Downloading pyarrow-18.1.0-cp39-cp39-win_amd64.whl.metadata (3.4 kB)
Downloading pyarrow-18.1.0-cp39-cp39-win_amd64.whl (25.3 MB)
   ---------------------------------------- 25.3/25.3 MB 6.0 MB/s eta 0:00:00
Installing collected packages: pyarrow
Successfully installed pyarrow-18.1.0
```
&lt;/details&gt;

cc: @lassoan @Thibault-Pelletier</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
