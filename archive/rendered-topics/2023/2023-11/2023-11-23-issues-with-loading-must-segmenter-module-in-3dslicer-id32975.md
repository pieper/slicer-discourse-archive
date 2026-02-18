# Issues with Loading MUST-Segmenter Module in 3DSlicer

**Topic ID**: 32975
**Date**: 2023-11-23
**URL**: https://discourse.slicer.org/t/issues-with-loading-must-segmenter-module-in-3dslicer/32975

---

## Post #1 by @cyufu (2023-11-23 10:10 UTC)

<p>windows 11，Version: 5.4<br>
Hello，<br>
“The 3DSlicer software displays the message ‘MUST-segmenter requires the ‘PyTorch’ Python package. Click OK to install it now.’ when loading the MUST-Segmenter module.”</p>
<pre><code class="lang-auto">ERROR: Could not find a version that satisfies the requirement torch (from versions: none)
ERROR: No matching distribution found for torch

[notice] A new release of pip is available: 23.1.2 -&gt; 23.3.1
[notice] To update, run: python-real.exe -m pip install --upgrade pip
Traceback (most recent call last):
  File "C:/ProgramData/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/PET-MUST-Segmenter/lib/Slicer-5.4/qt-scripted-modules/MUSTsegmenter.py", line 314, in checkRequirements
    from torch.nn import Conv3d
ModuleNotFoundError: No module named 'torch'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/ProgramData/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/PET-MUST-Segmenter/lib/Slicer-5.4/qt-scripted-modules/MUSTsegmenter.py", line 56, in setup
    self.segmentationLogic = MUSTsegmenterLogic()
  File "C:/ProgramData/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/PET-MUST-Segmenter/lib/Slicer-5.4/qt-scripted-modules/MUSTsegmenter.py", line 292, in __init__
    self.checkRequirements()
  File "C:/ProgramData/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/PET-MUST-Segmenter/lib/Slicer-5.4/qt-scripted-modules/MUSTsegmenter.py", line 321, in checkRequirements
    slicer.util.pip_install('torch')
  File "C:\ProgramData\slicer.org\Slicer 5.4.0\bin\Python\slicer\util.py", line 3759, in pip_install
    _executePythonModule('pip', args)
  File "C:\ProgramData\slicer.org\Slicer 5.4.0\bin\Python\slicer\util.py", line 3721, in _executePythonModule
    logProcessOutput(proc)
  File "C:\ProgramData\slicer.org\Slicer 5.4.0\bin\Python\slicer\util.py", line 3690, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/ProgramData/slicer.org/Slicer 5.4.0/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'torch']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/ProgramData/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/PET-MUST-Segmenter/lib/Slicer-5.4/qt-scripted-modules/MUSTsegmenter.py", line 81, in enter
    self.initializeParameterNode()
  File "C:/ProgramData/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/PET-MUST-Segmenter/lib/Slicer-5.4/qt-scripted-modules/MUSTsegmenter.py", line 99, in initializeParameterNode
    self.setParameterNode(self.segmentationLogic.getParameterNode())
AttributeError: 'NoneType' object has no attribute 'getParameterNode'


</code></pre>
<p>After clicking OK, as shown in the following image, there is a segmentation error and the cursor turns into a spinning circle continuously</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7d83a34803a6b6aa6aedc79d961a8328649bd90.jpeg" data-download-href="/uploads/short-url/uNrV6QCugGN1NgL7uVnUtTF1duM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7d83a34803a6b6aa6aedc79d961a8328649bd90_2_565x499.jpeg" alt="image" data-base62-sha1="uNrV6QCugGN1NgL7uVnUtTF1duM" width="565" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7d83a34803a6b6aa6aedc79d961a8328649bd90_2_565x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7d83a34803a6b6aa6aedc79d961a8328649bd90_2_847x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7d83a34803a6b6aa6aedc79d961a8328649bd90_2_1130x998.jpeg 2x" data-dominant-color="9B9999"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1313×1160 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be greatly appreciated. Thank you!</p>

---

## Post #2 by @cyufu (2023-11-23 11:10 UTC)

<p>pip_install(‘torch -i <a href="https://pypi.tuna.tsinghua.edu.cn/simple" rel="noopener nofollow ugc">https://pypi.tuna.tsinghua.edu.cn/simple</a>’)</p>

---
