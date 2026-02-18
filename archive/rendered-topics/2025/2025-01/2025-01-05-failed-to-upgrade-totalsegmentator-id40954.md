# Failed to upgrade TotalSegmentator

**Topic ID**: 40954
**Date**: 2025-01-05
**URL**: https://discourse.slicer.org/t/failed-to-upgrade-totalsegmentator/40954

---

## Post #1 by @Young (2025-01-05 03:37 UTC)

<p>I installed the TotalSegmentator extension using 3Dslicer version 5.6.2. The first time I used it, I was unable to update TotalSegmentator when installing the python package. The following is the error code displayed. How can I solve this problem</p>
<p>[Python] Failed to upgrade TotalSegmentator</p>
<p>[Python] Command ‘[‘C:/Users/Young/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘black;extra’, ‘==’, ‘dev’]’ returned non-zero exit status 2.</p>
<p>Traceback (most recent call last):</p>
<p>File “C:/Users/Young/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 319, in onPackageUpgrade</p>
<p>self.logic.setupPythonRequirements(upgrade=True)</p>
<p>File “C:/Users/Young/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 819, in setupPythonRequirements</p>
<p>self.pipInstallSelective(‘nnunetv2’, nnunetRequirement, packagesToSkip)</p>
<p>File “C:/Users/Young/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 706, in pipInstallSelective</p>
<p>slicer.util.pip_install(requirement)</p>
<p>File “C:\Users\Young\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3887, in pip_install</p>
<p>_executePythonModule(“pip”, args)</p>
<p>File “C:\Users\Young\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3848, in _executePythonModule</p>
<p>logProcessOutput(proc)</p>
<p>File “C:\Users\Young\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3814, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[‘C:/Users/Young/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘black;extra’, ‘==’, ‘dev’]’ returned non-zero exit status 2.</p>

---
