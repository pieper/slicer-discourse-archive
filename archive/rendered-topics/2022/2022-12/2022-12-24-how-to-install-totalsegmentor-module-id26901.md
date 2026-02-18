# How To Install TotalSegmentor module

**Topic ID**: 26901
**Date**: 2022-12-24
**URL**: https://discourse.slicer.org/t/how-to-install-totalsegmentor-module/26901

---

## Post #1 by @akmal871026 (2022-12-24 03:18 UTC)

<p>Dear all,</p>
<p>I was plugin the TotalSegmentor extension. But got error.</p>
<p><strong>Failed to compute results.</strong></p>
<p><strong>Command ‘[‘C:/Users/Akmal/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘light_the_torch’, ‘install’, ‘torch’]’ returned non-zero exit status 1.</strong></p>
<p><strong>Traceback (most recent call last):</strong><br>
**  File “C:\Users\Akmal\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay**<br>
**    yield**<br>
**  File “C:/Users/Akmal/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 248, in onApplyButton**<br>
**    self.logic.setupPythonRequirements()**<br>
**  File “C:/Users/Akmal/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 494, in setupPythonRequirements**<br>
**    torch = torchLogic.installTorch(askConfirmation=True)**<br>
**  File “C:/Users/Akmal/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/PyTorch/lib/Slicer-5.2/qt-scripted-modules/PyTorchUtils.py”, line 180, in installTorch**<br>
**    slicer.util._executePythonModule(‘light_the_torch’, args)**<br>
**  File “C:\Users\Akmal\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3533, in _executePythonModule**<br>
**    logProcessOutput(proc)**<br>
**  File “C:\Users\Akmal\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3502, in logProcessOutput**<br>
**    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)**<br>
<strong>subprocess.CalledProcessError: Command ‘[‘C:/Users/Akmal/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘light_the_torch’, ‘install’, ‘torch’]’ returned non-zero exit status 1.</strong></p>

---

## Post #2 by @lassoan (2022-12-24 04:58 UTC)

<p>Thanks for reporting, it is due to a regression that I introduced a few days ago when I improved GPU detection. Update PyTorch extension tomorrow in the extensions manager and it should work well. Let me know if you run into any further issues.</p>

---

## Post #3 by @akmal871026 (2022-12-29 02:07 UTC)

<p>SOlve. Thank you sir.</p>

---
