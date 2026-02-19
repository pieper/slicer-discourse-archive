---
topic_id: 37547
title: "Totalsegmentator Use Error"
date: 2024-07-24
url: https://discourse.slicer.org/t/37547
---

# TotalSegmentator use Error

**Topic ID**: 37547
**Date**: 2024-07-24
**URL**: https://discourse.slicer.org/t/totalsegmentator-use-error/37547

---

## Post #1 by @AnasKRG (2024-07-24 15:16 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.6.2<br>
Expected behavior: Auto segmentation<br>
Actual behavior: when I click apply, it shows me this command:<br>
“Command ‘[‘D:/3d slicer/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘D:\3d slicer\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/Sa E1/AppData/Local/Temp/Slicer/__SlicerTemp__2024-07-24_17+26+03.989/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Sa E1/AppData/Local/Temp/Slicer/__SlicerTemp__2024-07-24_17+26+03.989/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.”<br>
I reinstalled the program, and this command still shows, what should I do?</p>

---

## Post #2 by @lassoan (2024-07-24 15:17 UTC)

<p>Please follow troubleshooting instructions <a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#troubleshooting">here</a>.</p>

---

## Post #3 by @AnasKRG (2024-07-25 07:38 UTC)

<p>I tried the solution provided in the Documentation, but nothing changed, I tried reinstallation for pyTorch module, it always shows me that there’s a failure in installation because of running Python programs in the background, I restarted the whole Laptop and tried again, it stops progressing at this moment<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/beba034aa9f00f808a1c2b7ae7d903923af4790c.png" data-download-href="/uploads/short-url/rdffvmNgR3MxjNr6qj3vFkvv2wc.png?dl=1" title="image_2024-07-25_10-35-21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beba034aa9f00f808a1c2b7ae7d903923af4790c_2_690x369.png" alt="image_2024-07-25_10-35-21" data-base62-sha1="rdffvmNgR3MxjNr6qj3vFkvv2wc" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beba034aa9f00f808a1c2b7ae7d903923af4790c_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beba034aa9f00f808a1c2b7ae7d903923af4790c_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beba034aa9f00f808a1c2b7ae7d903923af4790c_2_1380x738.png 2x" data-dominant-color="454345"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_2024-07-25_10-35-21</span><span class="informations">1920×1029 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
please if you can guide me with a better solution</p>

---

## Post #4 by @lassoan (2024-07-25 07:51 UTC)

<p>Please provide the full application log (menu; Help / Report a bug) and the content if the textbox below the Apply button.</p>
<p>Size of pytorch is several GB, so you have a very slow internet connnection then download may take hours. You may also need up to 20GB of free disk space during installation.</p>

---

## Post #5 by @AnasKRG (2024-07-25 08:11 UTC)

<p>Thanks for responding, I’ll change my internet connection to faster one, I’ll keep you updated</p>

---

## Post #6 by @AnasKRG (2024-07-25 08:56 UTC)

<p><em><strong>The full log content:</strong></em></p>
<pre><code class="lang-auto">[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - Session start time .......: 20240725_110150
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19045, Code Page 65001) - 64-bit
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - Memory ...................: 8099 MB physical, 12451 MB virtual
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 4 logical processors
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - Application path .........: D:/3d slicer/Slicer 5.6.2/bin
[DEBUG][Qt] 25.07.2024 11:01:50 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/TorchIO/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules
[DEBUG][Python] 25.07.2024 11:01:57 [Python] (D:\3d slicer\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 25.07.2024 11:01:57 [Python] (D:\3d slicer\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 25.07.2024 11:01:57 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 25.07.2024 11:02:01 [] (unknown:0) - Switch to module:  "SampleData"
[DEBUG][Python] 25.07.2024 11:02:11 [Python] (D:/3d slicer/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Verifying checksum
[DEBUG][Python] 25.07.2024 11:02:12 [Python] (D:/3d slicer/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - File already exists and checksum is OK - reusing it.
[DEBUG][Python] 25.07.2024 11:02:12 [Python] (D:/3d slicer/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Requesting load CTACardio from C:/Users/Sa E1/AppData/Local/slicer.org/Slicer/cache/SlicerIO/CTA-cardio.nrrd ...
[DEBUG][Qt] 25.07.2024 11:02:13 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/Sa E1/AppData/Local/slicer.org/Slicer/cache/SlicerIO/CTA-cardio.nrrd" "[1.23s]"
[DEBUG][Python] 25.07.2024 11:02:13 [Python] (D:/3d slicer/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Load finished
[DEBUG][Qt] 25.07.2024 11:02:18 [] (unknown:0) - Switch to module:  "TotalSegmentator"
[INFO][Stream] 25.07.2024 11:02:33 [] (unknown:0) - Requirement already satisfied: pillow&lt;10.1 in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (10.0.1)
[INFO][Python] 25.07.2024 11:02:35 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - PyTorch Python package is required. Installing... (it may take several minutes)
[INFO][Python] 25.07.2024 11:02:35 [Python] (D:\3d slicer\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - PyTorch will be downloaded and installed using light-the-torch (ltt install torch&gt;=1.12 torchvision). The process might take some minutes.
[INFO][Python] 25.07.2024 11:02:44 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:213) - Installation of PyTorch aborted by user
[CRITICAL][Stream] 25.07.2024 11:02:44 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 25.07.2024 11:02:44 [] (unknown:0) -   File "D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 274, in onApplyButton
[CRITICAL][Stream] 25.07.2024 11:02:44 [] (unknown:0) -     self.logic.setupPythonRequirements()
[CRITICAL][Stream] 25.07.2024 11:02:44 [] (unknown:0) -   File "D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 723, in setupPythonRequirements
[CRITICAL][Stream] 25.07.2024 11:02:44 [] (unknown:0) -     raise ValueError('PyTorch extension needs to be installed to use this module.')
[CRITICAL][Stream] 25.07.2024 11:02:44 [] (unknown:0) - ValueError: PyTorch extension needs to be installed to use this module.
[INFO][Python] 25.07.2024 11:02:44 [Python] (D:\3d slicer\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Application is required to complete installation of required Python packages.
Press OK to restart.
[DEBUG][Qt] 25.07.2024 11:04:04 [] (unknown:0) - Python console user input: git clone https://github.com/git/git
[CRITICAL][Stream] 25.07.2024 11:04:04 [] (unknown:0) -   File "&lt;console&gt;", line 1
[CRITICAL][Stream] 25.07.2024 11:04:04 [] (unknown:0) -     git clone https://github.com/git/git
[CRITICAL][Stream] 25.07.2024 11:04:04 [] (unknown:0) -         ^
[CRITICAL][Stream] 25.07.2024 11:04:04 [] (unknown:0) - SyntaxError: invalid syntax
[DEBUG][Qt] 25.07.2024 11:04:21 [] (unknown:0) - Python console user input: git clone https://github.com/git/git
[CRITICAL][Stream] 25.07.2024 11:04:21 [] (unknown:0) -   File "&lt;console&gt;", line 1
[CRITICAL][Stream] 25.07.2024 11:04:21 [] (unknown:0) -     git clone https://github.com/git/git
[CRITICAL][Stream] 25.07.2024 11:04:21 [] (unknown:0) -         ^
[CRITICAL][Stream] 25.07.2024 11:04:21 [] (unknown:0) - SyntaxError: invalid syntax
[DEBUG][Qt] 25.07.2024 11:04:45 [] (unknown:0) - Python console user input: clear
[CRITICAL][Stream] 25.07.2024 11:04:45 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 25.07.2024 11:04:45 [] (unknown:0) -   File "&lt;console&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 25.07.2024 11:04:45 [] (unknown:0) - NameError: name 'clear' is not defined
[DEBUG][Qt] 25.07.2024 11:05:15 [] (unknown:0) - Python console user input: git clone https://github.com/git/git
[CRITICAL][Stream] 25.07.2024 11:05:15 [] (unknown:0) -   File "&lt;console&gt;", line 1
[CRITICAL][Stream] 25.07.2024 11:05:15 [] (unknown:0) -     git clone https://github.com/git/git
[CRITICAL][Stream] 25.07.2024 11:05:15 [] (unknown:0) -         ^
[CRITICAL][Stream] 25.07.2024 11:05:15 [] (unknown:0) - SyntaxError: invalid syntax
[INFO][Stream] 25.07.2024 11:05:27 [] (unknown:0) - Requirement already satisfied: pillow&lt;10.1 in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (10.0.1)
[INFO][Python] 25.07.2024 11:05:27 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - PyTorch Python package is required. Installing... (it may take several minutes)
[INFO][Python] 25.07.2024 11:05:27 [Python] (D:\3d slicer\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - PyTorch will be downloaded and installed using light-the-torch (ltt install torch&gt;=1.12 torchvision). The process might take some minutes.
[INFO][Python] 25.07.2024 11:05:30 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:216) - Install PyTorch using light-the-torch with arguments: ['install', 'torch&gt;=1.12', 'torchvision']
[DEBUG][Python] 25.07.2024 11:05:30 [Python] (D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\pip\_internal\vcs\versioncontrol.py:225) - Registered VCS backend: bzr
[DEBUG][Python] 25.07.2024 11:05:30 [Python] (D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\pip\_internal\vcs\versioncontrol.py:225) - Registered VCS backend: git
[DEBUG][Python] 25.07.2024 11:05:30 [Python] (D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\pip\_internal\vcs\versioncontrol.py:225) - Registered VCS backend: hg
[DEBUG][Python] 25.07.2024 11:05:30 [Python] (D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\pip\_internal\vcs\versioncontrol.py:225) - Registered VCS backend: svn
[INFO][Stream] 25.07.2024 11:05:33 [] (unknown:0) - Collecting torch&gt;=1.12
[INFO][Stream] 25.07.2024 11:05:35 [] (unknown:0) -   Downloading https://download.pytorch.org/whl/cpu/torch-2.4.0%2Bcpu-cp39-cp39-win_amd64.whl (200.3 MB)
[INFO][Stream] 25.07.2024 11:19:33 [] (unknown:0) -      ------------------------------------ 200.3/200.3 MB 337.1 kB/s eta 0:00:00
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) - Collecting torchvision
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) -   Using cached https://download.pytorch.org/whl/cpu/torchvision-0.9.1%2Bcpu-cp39-cp39-win_amd64.whl (845 kB)
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) - Requirement already satisfied: filelock in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from torch&gt;=1.12) (3.15.4)
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) - Requirement already satisfied: typing-extensions&gt;=4.8.0 in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from torch&gt;=1.12) (4.8.0)
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) - Requirement already satisfied: sympy in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from torch&gt;=1.12) (1.13.1)
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) - Requirement already satisfied: networkx in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from torch&gt;=1.12) (3.2.1)
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) - Requirement already satisfied: jinja2 in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from torch&gt;=1.12) (3.1.4)
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) - Requirement already satisfied: fsspec in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from torch&gt;=1.12) (2024.6.1)
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) - Requirement already satisfied: numpy in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from torchvision) (1.26.1)
[INFO][Stream] 25.07.2024 11:19:41 [] (unknown:0) - INFO: pip is looking at multiple versions of torchvision to determine which version is compatible with other requirements. This could take a while.
[INFO][Stream] 25.07.2024 11:19:42 [] (unknown:0) -   Using cached https://download.pytorch.org/whl/cpu/torchvision-0.9.0%2Bcpu-cp39-cp39-win_amd64.whl (845 kB)
[INFO][Stream] 25.07.2024 11:19:43 [] (unknown:0) -   Using cached https://download.pytorch.org/whl/cpu/torchvision-0.8.2%2Bcpu-cp39-cp39-win_amd64.whl (804 kB)
[INFO][Stream] 25.07.2024 11:19:44 [] (unknown:0) -   Using cached https://download.pytorch.org/whl/torchvision-0.2.0-py2.py3-none-any.whl (48 kB)
[INFO][Stream] 25.07.2024 11:19:44 [] (unknown:0) - Requirement already satisfied: pillow&gt;=4.1.1 in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from torchvision) (10.0.1)
[INFO][Stream] 25.07.2024 11:19:44 [] (unknown:0) - Requirement already satisfied: six in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from torchvision) (1.16.0)
[INFO][Stream] 25.07.2024 11:19:44 [] (unknown:0) - Requirement already satisfied: MarkupSafe&gt;=2.0 in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from jinja2-&gt;torch&gt;=1.12) (2.1.5)
[INFO][Stream] 25.07.2024 11:19:44 [] (unknown:0) - Requirement already satisfied: mpmath&lt;1.4,&gt;=1.1.0 in d:\3d slicer\slicer 5.6.2\lib\python\lib\site-packages (from sympy-&gt;torch&gt;=1.12) (1.3.0)
[INFO][Stream] 25.07.2024 11:19:45 [] (unknown:0) - Installing collected packages: torch, torchvision
[INFO][Stream] 25.07.2024 11:20:20 [] (unknown:0) -   WARNING: The scripts convert-caffe2-to-onnx.exe, convert-onnx-to-caffe2.exe and torchrun.exe are installed in 'D:\3d slicer\Slicer 5.6.2\lib\Python\Scripts' which is not on PATH.
[INFO][Stream] 25.07.2024 11:20:20 [] (unknown:0) -   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
[INFO][Stream] 25.07.2024 11:20:21 [] (unknown:0) - Successfully installed torch-2.4.0+cpu torchvision-0.2.0
[INFO][Python] 25.07.2024 11:20:30 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:226) - PyTorch 2.4.0+cpu installed successfully.
[INFO][Python] 25.07.2024 11:20:30 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Processing started
[INFO][Python] 25.07.2024 11:20:30 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Writing input file to D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/total-segmentator-input.nii
[INFO][Python] 25.07.2024 11:20:31 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Creating segmentations with TotalSegmentator AI...
[INFO][Python] 25.07.2024 11:20:31 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Total Segmentator arguments: ['-i', 'D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/total-segmentator-input.nii', '-o', 'D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/segmentation', '--ml', '--task', 'total', '--fast']
[INFO][Python] 25.07.2024 11:20:36 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - Traceback (most recent call last):
[INFO][Python] 25.07.2024 11:20:36 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
[INFO][Python] 25.07.2024 11:20:36 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     return _run_code(code, main_globals, None,
[INFO][Python] 25.07.2024 11:20:36 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 87, in _run_code
[INFO][Python] 25.07.2024 11:20:36 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     exec(code, run_globals)
[INFO][Python] 25.07.2024 11:20:37 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "D:\3d slicer\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 4, in &lt;module&gt;
[INFO][Python] 25.07.2024 11:20:37 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 6, in &lt;module&gt;
[INFO][Python] 25.07.2024 11:20:37 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     from totalsegmentator.python_api import totalsegmentator, validate_device_type_api
[INFO][Python] 25.07.2024 11:20:37 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 13, in &lt;module&gt;
[INFO][Python] 25.07.2024 11:20:37 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     from totalsegmentator.statistics import get_basic_statistics, get_radiomics_features_for_entire_dir
[INFO][Python] 25.07.2024 11:20:37 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -   File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\statistics.py", line 13, in &lt;module&gt;
[INFO][Python] 25.07.2024 11:20:37 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) -     from p_tqdm import p_map
[INFO][Python] 25.07.2024 11:20:37 [Python] (D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:565) - ModuleNotFoundError: No module named 'p_tqdm'
[ERROR][Python] 25.07.2024 11:20:37 [Python] (D:\3d slicer\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Failed to compute results.

Command '['D:/3d slicer/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'D:\\3d slicer\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/total-segmentator-input.nii', '-o', 'D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/segmentation', '--ml', '--task', 'total', '--fast']' returned non-zero exit status 1.
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) -   File "D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 298, in onApplyButton
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) -     self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) -   File "D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 971, in process
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) -     self.processVolume(inputFile, inputVolume,
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) -   File "D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1045, in processVolume
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) -     self.logProcessOutput(proc)
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) -   File "D:/3d slicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 817, in logProcessOutput
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 25.07.2024 11:49:04 [] (unknown:0) - subprocess.CalledProcessError: Command '['D:/3d slicer/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'D:\\3d slicer\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/total-segmentator-input.nii', '-o', 'D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/segmentation', '--ml', '--task', 'total', '--fast']' returned non-zero exit status 1.
</code></pre>
<p><em><strong>The textbox under Apply button content:</strong></em></p>
<pre><code class="lang-auto">PyTorch Python package is required. Installing... (it may take several minutes)
Processing started
Writing input file to D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/total-segmentator-input.nii
Creating segmentations with TotalSegmentator AI...
Total Segmentator arguments: ['-i', 'D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/total-segmentator-input.nii', '-o', 'D:/3d slicer/Temporary/__SlicerTemp__2024-07-25_11+20+30.506/segmentation', '--ml', '--task', 'total', '--fast']
Traceback (most recent call last):
  File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "D:\3d slicer\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 4, in &lt;module&gt;
  File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 6, in &lt;module&gt;
    from totalsegmentator.python_api import totalsegmentator, validate_device_type_api
  File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 13, in &lt;module&gt;
    from totalsegmentator.statistics import get_basic_statistics, get_radiomics_features_for_entire_dir
  File "D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\statistics.py", line 13, in &lt;module&gt;
    from p_tqdm import p_map
ModuleNotFoundError: No module named 'p_tqdm'
</code></pre>

---

## Post #7 by @AnasKRG (2024-07-26 00:35 UTC)

<p>I found this module should be installed, I think, in the same path provided:</p>
<p>File “D:\3d slicer\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\statistics.py”, line 13, in <br>
from p_tqdm import p_map<br>
ModuleNotFoundError: No module named ‘p_tqdm’</p>
<p>Could you please guide me to install it manually?</p>

---

## Post #8 by @lassoan (2024-07-26 04:50 UTC)

<p>Tqdm is a simple process reporting Python package that is installed as part of nnunet. The fact that you dont have it installed,why nnunet is already installed indicates that your nnunet installation was incomplete. Nnunet installation was not included in the log file you provided, so I dont know what went wrong with it.</p>
<p>You can pip install tqdm manually in Slicer’s Python console (<code>pip_install("tqdm")</code>). If you find that then some other dependencies are missed then probably the easiest is to force reinstall the Python dependencies using the button in the advanced section.</p>

---

## Post #9 by @AnasKRG (2024-07-26 11:44 UTC)

<p>I’m very Greatfull for your help, Thank you very much for continuing supporting us in this particular error<br>
It successfully worked finally after I disabled my Windows antivirus and Apps &amp; Web antivirus … I noticed when I forces reinstallation of Python Packages it Stops when downloading the Lib (p_tqdm) and shows an error that I already showed you above, when I tried every solution i saw here or in documentation nothing changes, but when I opened Python Console and entered</p>
<blockquote>
<p>pip_install(“p_tqdm”)</p>
</blockquote>
<p>it shows me that Windows antivirus disabled this download for suspecting of a virus in the Console, so I disabled the antivirus and it worked very well, as shown:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/066f0e21193a63c605e088d0343b88fa6833f245.png" data-download-href="/uploads/short-url/UUNzbmMKxfC85K9LK8Y1RcAoYt.png?dl=1" title="IMG_20240726_144357_922" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/066f0e21193a63c605e088d0343b88fa6833f245_2_690x366.png" alt="IMG_20240726_144357_922" data-base62-sha1="UUNzbmMKxfC85K9LK8Y1RcAoYt" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/066f0e21193a63c605e088d0343b88fa6833f245_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/066f0e21193a63c605e088d0343b88fa6833f245_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/066f0e21193a63c605e088d0343b88fa6833f245_2_1380x732.png 2x" data-dominant-color="464446"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20240726_144357_922</span><span class="informations">1920×1021 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
