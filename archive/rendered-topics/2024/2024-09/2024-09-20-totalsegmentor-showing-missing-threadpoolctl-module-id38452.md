# Totalsegmentor showing missing threadpoolctl module

**Topic ID**: 38452
**Date**: 2024-09-20
**URL**: https://discourse.slicer.org/t/totalsegmentor-showing-missing-threadpoolctl-module/38452

---

## Post #1 by @davidngqk88 (2024-09-20 05:27 UTC)

<p>hello community.</p>
<p>I have updated my slicer version to version 5.6.2 and that seems to have broken Total Segmentor. I am getting a failed to compute results with non-zero exit status 1 with the following logs.</p>
<p>it looks like a python module threadpoolctl is missing. My python is rudimentary, is there a way to install this manually and get total segmentor to reference it correctly?</p>
<pre><code class="lang-plaintext">Processing started
Writing input file to C:/Users/XXXX/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.122/total-segmentator-input.nii
Creating segmentations with TotalSegmentator AI...
Total Segmentator arguments: ['-i', 'C:/Users/david/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.122/total-segmentator-input.nii', '-o', 'C:/Users/XXXX/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.122/segmentation', '--ml', '--task', 'headneck_bones_vessels']
Traceback (most recent call last):
  File "C:\3dslicer\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\3dslicer\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\3dslicer\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 7, in &lt;module&gt;
  File "C:\3dslicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 141, in main
    totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
  File "C:\3dslicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 127, in totalsegmentator
    from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars
  File "C:\3dslicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py", line 30, in &lt;module&gt;
    from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
  File "C:\3dslicer\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py", line 12, in &lt;module&gt;
    from batchgenerators.dataloading.multi_threaded_augmenter import MultiThreadedAugmenter
  File "C:\3dslicer\Slicer 5.6.2\lib\Python\Lib\site-packages\batchgenerators\dataloading\multi_threaded_augmenter.py", line 26, in &lt;module&gt;
    from threadpoolctl import threadpool_limits
ModuleNotFoundError: No module named 'threadpoolctl'
</code></pre>
<p>Python Console:</p>
<pre><code class="lang-plaintext">[Qt] libpng warning: iCCP: known incorrect sRGB profile
[Qt] When loading module  "ParticlesDisplay" , the dependency "TractographyDisplay" failed to be loaded.
[Python] Irregular volume geometry detected (maximum error of 0.00119431 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.
[Python] Failed to compute results.
[Python] Command '['C:/3dslicer/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\3dslicer\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/XXXX/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.122/total-segmentator-input.nii', '-o', 'C:/Users/david/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.122/segmentation', '--ml', '--task', 'headneck_bones_vessels']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/3dslicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/3dslicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1001, in process
    self.processVolume(inputFile, inputVolume,
  File "C:/3dslicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1075, in processVolume
    self.logProcessOutput(proc)
  File "C:/3dslicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 847, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/3dslicer/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\3dslicer\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/XXXX/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.122/total-segmentator-input.nii', '-o', 'C:/Users/david/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.122/segmentation', '--ml', '--task', 'headneck_bones_vessels']' returned non-zero exit status 1.


Error Detail:
Traceback (most recent call last):
  File "C:\3dslicer\Slicer 5.6.2\bin\Python\slicer\util.py", line 3255, in tryWithErrorDisplay
    yield
  File "C:/3dslicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/3dslicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1001, in process
    self.processVolume(inputFile, inputVolume,
  File "C:/3dslicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1075, in processVolume
    self.logProcessOutput(proc)
  File "C:/3dslicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 847, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/3dslicer/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\3dslicer\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/david/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.122/total-segmentator-input.nii', '-o', 'C:/Users/david/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.122/segmentation', '--ml', '--task', 'headneck_bones_vessels']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @lassoan (2024-09-20 05:30 UTC)

<p>It seems that your installation was incomplete (is it possible that you were low in disk space or interrupted the installation?). You can try to fix this by executing <code>pip_install('threadpoolctl')</code> in Slicer’s Python console. If that is not enough then you can try <code>Force reinstall</code> button in <code>Advanced</code> section. If you still experience issues then probably the simplest solution is to reinstall Slicer from scratch (remove the <code>C:/3dslicer/Slicer 5.6.2</code> folder and install Slicer and TotalSegmentator extension again).</p>

---
