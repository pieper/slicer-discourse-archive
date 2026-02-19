---
topic_id: 26956
title: "Error While Installing Pytorch"
date: 2022-12-27
url: https://discourse.slicer.org/t/26956
---

# Error while installing pytorch

**Topic ID**: 26956
**Date**: 2022-12-27
**URL**: https://discourse.slicer.org/t/error-while-installing-pytorch/26956

---

## Post #1 by @Anish_Raj (2022-12-27 10:07 UTC)

<p>Hii,<br>
I am having trouble applying the module in slicer 5.2.1. When i press apply, it says pytorch will be installed using light-the-torch. After few seconds, i get the error: failed to compute results, no module named torch.<br>
Detailed error:<br>
Traceback (most recent call last):<br>
File “E:\apps\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “E:/apps/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 248, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “E:/apps/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 494, in setupPythonRequirements<br>
torch = torchLogic.installTorch(askConfirmation=True)<br>
File “E:/apps/Slicer 5.2.1/NA-MIC/Extensions-31317/PyTorch/lib/Slicer-5.2/qt-scripted-modules/PyTorchUtils.py”, line 188, in installTorch<br>
import torch<br>
ModuleNotFoundError: No module named ‘torch’</p>
<p>Please let me know what am i doing wrong.</p>

---

## Post #2 by @rbumm (2022-12-27 12:35 UTC)

<p>Could you please install the PyTorch extension</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9251659e70ff690dbe0bb4aa29a7d498ca5e1575.png" alt="image" data-base62-sha1="kSo6nkEZ8OJpfklja75RwY27qSh" width="278" height="388"></p>
<p>and restart Slicer ?</p>

---

## Post #3 by @Anish_Raj (2022-12-27 12:46 UTC)

<p>Thanks, but it is already installed and doesn’t make a difference <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @rbumm (2022-12-27 12:48 UTC)

<p>If you are on Windows, could you please try to install TotalSegmentator from the command line (cmd.exe):</p>
<pre><code class="lang-auto">"C:\Users\yourname\AppData\Local\NA-MIC\Slicer 5.2.1\bin/PythonSlicer.EXE" -m pip install git+https://github.com/wasserth/TotalSegmentator.git --no-deps
</code></pre>
<p>and post the results?</p>

---

## Post #5 by @lassoan (2022-12-27 15:07 UTC)

<p>I’ve made improvements to the PyTorch extension. Please update it using the Extensions Manager. You can then open PyTorch Utils module and first click Uninstall pytorch to remove any incomplete installs and then click Install pytorch to properly install it.</p>

---

## Post #6 by @Anish_Raj (2022-12-28 12:32 UTC)

<p>Thank you, reinstalling pytorch worked <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @zhuji423 (2023-02-17 07:51 UTC)

<p>Very useful. Thank you</p>

---

## Post #8 by @Nicolas_Larragueta (2024-04-14 21:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="26956">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>e PyTorch extension. Please update it using the Extensions Manager. You can then open PyTorch Utils module and first click Uninstall pytorch to remove any incomplete installs</p>
</blockquote>
</aside>
<p>Can I use a computer with more than one GPU with total segmentator? I have de same problem with te pytorch, but nothing works for me, I try uninstall, and re insatall again, but does not work., Thank you!</p>

---

## Post #9 by @lassoan (2024-04-15 15:28 UTC)

<p>It should be no problem at all. You should be able to install and use pytorch in Slicer’s Python environment the same way as any other Python requirements. If you work on a laptop with discrete NVIDIA GPU then make sure that in your NVIDIA settings Slicer executable (SlicerApp-real.exe) is assigned to use the high-performance GPU.</p>
<p>If you need further help please provide the full application log of a pytorch installation from scratch:</p>
<ul>
<li>install latest Slicer Preview Release into a new folder</li>
<li>start this newly installed Slicer</li>
<li>install pytorch extension, restart Slicer</li>
<li>install torch using the <code>PyTorch Utils</code> module, go to menu: Help / Report a bug, save the full application log into a file, upload that file somewhere (dropbox, onedrive, etc.) and post the link here</li>
</ul>

---

## Post #10 by @Nicolas_Larragueta (2024-04-16 00:02 UTC)

<p>Hi! I downloaded the last version, and installed Total Segmentator., but when I want to apply for segmentations, try to download pytorch and fails. Here the log <a href="https://drive.google.com/file/d/1ZUMbQOJD3sLEI4ZK4TnGLJ1WlO7pzxpW/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">Slicer_5.7.0-2024-04-12_32805_20240415_204438_406.log - Google Drive</a><br>
Thank you in advance!</p>

---

## Post #11 by @Nicolas_Larragueta (2024-04-17 19:53 UTC)

<p>I could already install pytorch by adding time in the default timeout:</p>
<p><code>slicer.util.pip_install('--default-timeout=100 torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121')</code></p>
<p>I have pytorch installed but still cant use Totalsegmentator. It downloads model for task 294, and when its done the installation cant be done and errors appears:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\ProgramData\slicer.org\Slicer 5.7.0-2024-04-12\bin\Python\slicer\util.py", line 3295, in tryWithErrorDisplay
    yield
  File "C:/ProgramData/slicer.org/Slicer 5.7.0-2024-04-12/slicer.org/Extensions-32805/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py", line 292, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/ProgramData/slicer.org/Slicer 5.7.0-2024-04-12/slicer.org/Extensions-32805/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py", line 975, in process
    self.logProcessOutput(proc)
  File "C:/ProgramData/slicer.org/Slicer 5.7.0-2024-04-12/slicer.org/Extensions-32805/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py", line 795, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/ProgramData/slicer.org/Slicer 5.7.0-2024-04-12/bin/../bin\\PythonSlicer.EXE', 'C:\\ProgramData\\slicer.org\\Slicer 5.7.0-2024-04-12\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Familia Larragueta/AppData/Local/Temp/Slicer/__SlicerTemp__2024-04-17_16+11+21.925/total-segmentator-input.nii', '-o', 'C:/Users/Familia Larragueta/AppData/Local/Temp/Slicer/__SlicerTemp__2024-04-17_16+11+21.925/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
</code></pre>
<p>Thank you!!!</p>

---

## Post #12 by @lassoan (2024-04-18 00:01 UTC)

<p>You may find more information in the process output. Check both the text window in the TotalSegmentator module and the Slicer application log.</p>

---

## Post #13 by @LukasR (2024-09-15 18:12 UTC)

<p>Greetings,</p>
<p>I’m using the current latest stable version Slicer 5.6.2. I have quite the similar issue mentioned above. During the use of an extension MONAI Auto3DSeg when I press apply It says:<br>
PyTorch will be downloaded and installed using light-the-torch (ltt install torch&gt;=1.12 torchvision)</p>
<p>After some time an error occurs:<br>
Failed to install required dependencies. No module named ‘torch’</p>
<p>Error details:<br>
Traceback (most recent call last):<br>
File “D:\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “D:/Slicer 5.6.2/slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules/MONAIAuto3DSeg.py”, line 505, in onApply<br>
self.logic.setupPythonRequirements()<br>
File “D:/Slicer 5.6.2/slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules/MONAIAuto3DSeg.py”, line 1062, in setupPythonRequirements<br>
torch = torchLogic.installTorch(askConfirmation=True, torchVersionRequirement = f"&gt;={minimumTorchVersion}")<br>
File “D:/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 225, in installTorch<br>
import torch<br>
ModuleNotFoundError: No module named ‘torch’</p>
<p>I’ve already tried to reinstall slicer from the scratch, reinstall extensions PyTorch and MONAI Auto3DSeg from the extenions manager, change computation backened to CPU and I also have more than 20gb of free space on the disk. None of these possibilities solved the problem.</p>
<p>I’ll be very grateful for your help.</p>

---

## Post #14 by @muratmaga (2024-09-15 18:16 UTC)

<p>You can try to install the PyTorch extension and run it yourself to get more diagnostic information about why Torch is not being installed).</p>
<p>Just choose auto the method…</p>
<p>If it work, go ahead and reinstall the auto3Dseg one more time.</p>

---

## Post #15 by @LukasR (2024-09-15 18:57 UTC)

<p>I tried to install PyTorch directly in the module and it shows error:<br>
Failed to install PyTorch. Some PyTorch files may be in use or corrupted. Please restart the application, uninstall PyTorch, and try installing again.<br>
No module named ‘torch’</p>
<p>Error details:<br>
Traceback (most recent call last):<br>
File “D:\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “D:/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 78, in onInstallTorch<br>
torch = self.logic.installTorch(askConfirmation, None if automaticBackend else backend, torchVersionRequirement, torchvisionVersionRequirement)<br>
File “D:/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 225, in installTorch<br>
import torch<br>
ModuleNotFoundError: No module named ‘torch’</p>

---

## Post #16 by @lassoan (2024-09-15 19:45 UTC)

<p>Please restart the application, uninstall PyTorch, and try installing again. If you still experience any problems then copy here the application log of the session in that you tried to install pytorch.</p>

---

## Post #17 by @LukasR (2024-09-15 21:01 UTC)

<p>Restarting the application and reinstalling PyTorch didnt help. There’s the full application log of the error session you asked:</p>
<p>[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20240915_225204<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19045, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16343 MB physical, 16343 MB virtual<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/bin<br>
[DEBUG][Qt] 15.09.2024 22:52:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules</a><br>
[DEBUG][Python] 15.09.2024 22:52:08 [Python] (C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 15.09.2024 22:52:08 [Python] (C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 15.09.2024 22:52:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 15.09.2024 22:52:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SampleData”<br>
[DEBUG][Python] 15.09.2024 22:52:18 [Python] (C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Verifying checksum<br>
[DEBUG][Python] 15.09.2024 22:52:18 [Python] (C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - File already exists and checksum is OK - reusing it.<br>
[DEBUG][Python] 15.09.2024 22:52:18 [Python] (C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Requesting load CTChest from C:/Users/12345/AppData/Local/slicer.org/Slicer/cache/SlicerIO/CT-chest.nrrd …<br>
[DEBUG][Qt] 15.09.2024 22:52:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/12345/AppData/Local/slicer.org/Slicer/cache/SlicerIO/CT-chest.nrrd” “[0.72s]”<br>
[DEBUG][Python] 15.09.2024 22:52:19 [Python] (C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Load finished<br>
[DEBUG][Qt] 15.09.2024 22:52:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “MONAIAuto3DSeg”<br>
[INFO][Python] 15.09.2024 22:52:34 [Python] (C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules/MONAIAuto3DSeg.py:1036) - Initializing PyTorch…<br>
[INFO][Python] 15.09.2024 22:52:34 [Python] (C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules/MONAIAuto3DSeg.py:1036) - PyTorch Python package is required. Installing… (it may take several minutes)<br>
[INFO][Python] 15.09.2024 22:52:34 [Python] (C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - PyTorch will be downloaded and installed using light-the-torch (ltt install torch&gt;=1.12 torchvision). The process might take some minutes.<br>
[INFO][Python] 15.09.2024 22:52:36 [Python] (C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:216) - Install PyTorch using light-the-torch with arguments: [‘install’, ‘torch&gt;=1.12’, ‘torchvision’]<br>
[INFO][Stream] 15.09.2024 22:52:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Collecting light-the-torch&gt;=0.5<br>
[INFO][Stream] 15.09.2024 22:52:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Using cached light_the_torch-0.7.5-py3-none-any.whl.metadata (9.5 kB)<br>
[INFO][Stream] 15.09.2024 22:52:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Collecting pip&lt;23.3,&gt;=22.3 (from light-the-torch&gt;=0.5)<br>
[INFO][Stream] 15.09.2024 22:52:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Using cached pip-23.2.1-py3-none-any.whl.metadata (4.2 kB)<br>
[INFO][Stream] 15.09.2024 22:52:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Using cached light_the_torch-0.7.5-py3-none-any.whl (14 kB)<br>
[INFO][Stream] 15.09.2024 22:52:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Using cached pip-23.2.1-py3-none-any.whl (2.1 MB)<br>
[INFO][Stream] 15.09.2024 22:52:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Installing collected packages: pip, light-the-torch<br>
[INFO][Stream] 15.09.2024 22:52:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Attempting uninstall: pip<br>
[INFO][Stream] 15.09.2024 22:52:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     Found existing installation: pip 23.3<br>
[INFO][Stream] 15.09.2024 22:52:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     Uninstalling pip-23.3:<br>
[INFO][Stream] 15.09.2024 22:52:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -       Successfully uninstalled pip-23.3<br>
[INFO][Stream] 15.09.2024 22:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   WARNING: The scripts pip.exe, pip3.9.exe and pip3.exe are installed in ‘C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts’ which is not on PATH.<br>
[INFO][Stream] 15.09.2024 22:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.<br>
[INFO][Stream] 15.09.2024 22:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   WARNING: The script ltt.exe is installed in ‘C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts’ which is not on PATH.<br>
[INFO][Stream] 15.09.2024 22:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.<br>
[INFO][Stream] 15.09.2024 22:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Successfully installed light-the-torch-0.7.5 pip-23.2.1<br>
[DEBUG][Python] 15.09.2024 22:52:48 [Python] (C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\vcs\versioncontrol.py:225) - Registered VCS backend: bzr<br>
[DEBUG][Python] 15.09.2024 22:52:48 [Python] (C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\vcs\versioncontrol.py:225) - Registered VCS backend: git<br>
[DEBUG][Python] 15.09.2024 22:52:48 [Python] (C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\vcs\versioncontrol.py:225) - Registered VCS backend: hg<br>
[DEBUG][Python] 15.09.2024 22:52:48 [Python] (C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\vcs\versioncontrol.py:225) - Registered VCS backend: svn<br>
[INFO][Stream] 15.09.2024 22:53:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Collecting torch&gt;=1.12<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ERROR: Exception:<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\cli\base_command.py”, line 180, in exc_logging_wrapper<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     status = run_func(*args)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\cli\req_command.py”, line 248, in wrapper<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     return func(self, options, args)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\commands\install.py”, line 377, in run<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     requirement_set = resolver.resolve(<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\light_the_torch_utils.py”, line 103, in new<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     output = fn(*args, **kwargs)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\resolution\resolvelib\resolver.py”, line 92, in resolve<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     result = self._result = resolver.resolve(<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\resolvelib\resolvers.py”, line 546, in resolve<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     state = resolution.resolve(requirements, max_rounds=max_rounds)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\resolvelib\resolvers.py”, line 397, in resolve<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self._add_to_criteria(self.state.criteria, r, parent=None)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\resolvelib\resolvers.py”, line 173, in _add_to_criteria<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     if not criterion.candidates:<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\resolvelib\structs.py”, line 156, in <strong>bool</strong><br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     return bool(self._sequence)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\resolution\resolvelib\found_candidates.py”, line 155, in <strong>bool</strong><br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     return any(self)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\resolution\resolvelib\found_candidates.py”, line 143, in <br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     return (c for c in iterator if id(c) not in self._incompatible_ids)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\resolution\resolvelib\found_candidates.py”, line 47, in _iter_built<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     candidate = func()<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\resolution\resolvelib\factory.py”, line 206, in _make_candidate_from_link<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self._link_candidate_cache[link] = LinkCandidate(<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\resolution\resolvelib\candidates.py”, line 293, in <strong>init</strong><br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     super().<strong>init</strong>(<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\resolution\resolvelib\candidates.py”, line 156, in <strong>init</strong><br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.dist = self._prepare()<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\resolution\resolvelib\candidates.py”, line 225, in _prepare<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     dist = self._prepare_distribution()<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\resolution\resolvelib\candidates.py”, line 304, in _prepare_distribution<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     return preparer.prepare_linked_requirement(self._ireq, parallel_builds=True)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\operations\prepare.py”, line 538, in prepare_linked_requirement<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     return self._prepare_linked_requirement(req, parallel_builds)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\operations\prepare.py”, line 609, in _prepare_linked_requirement<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     local_file = unpack_url(<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\operations\prepare.py”, line 166, in unpack_url<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     file = get_http_url(<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\operations\prepare.py”, line 107, in get_http_url<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     from_path, content_type = download(link, temp_dir.path)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\network\download.py”, line 134, in <strong>call</strong><br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     resp = _http_get_download(self._session, link)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\network\download.py”, line 117, in _http_get_download<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     resp = session.get(target_url, headers=HEADERS, stream=True)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\requests\sessions.py”, line 602, in get<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     return self.request(“GET”, url, **kwargs)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_internal\network\session.py”, line 519, in request<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     return super().request(method, url, *args, **kwargs)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\requests\sessions.py”, line 589, in request<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     resp = self.send(prep, **send_kwargs)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\requests\sessions.py”, line 703, in send<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     r = adapter.send(request, **kwargs)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\cachecontrol\adapter.py”, line 48, in send<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     cached_response = self.controller.cached_request(request)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\cachecontrol\controller.py”, line 155, in cached_request<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     resp = self.serializer.loads(request, cache_data, body_file)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\cachecontrol\serialize.py”, line 95, in loads<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     return getattr(self, “_loads_v{}”.format(ver))(request, data, body_file)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\cachecontrol\serialize.py”, line 186, in _loads_v4<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     cached = msgpack.loads(data, raw=False)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\msgpack\fallback.py”, line 125, in unpackb<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     ret = unpacker._unpack()<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\msgpack\fallback.py”, line 590, in _unpack<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     ret[key] = self._unpack(EX_CONSTRUCT)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\msgpack\fallback.py”, line 590, in _unpack<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     ret[key] = self._unpack(EX_CONSTRUCT)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\msgpack\fallback.py”, line 544, in _unpack<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     typ, n, obj = self._read_header()<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\msgpack\fallback.py”, line 486, in _read_header<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     obj = self._read(n)<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\msgpack\fallback.py”, line 403, in _read<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     ret = self._buffer[i : i + n]<br>
[INFO][Stream] 15.09.2024 22:53:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - MemoryError<br>
[ERROR][Python] 15.09.2024 22:53:03 [Python] (C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Failed to install required dependencies.</p>
<p>No module named ‘torch’<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules/MONAIAuto3DSeg.py”, line 494, in onApplyButton<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.onApply()<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules/MONAIAuto3DSeg.py”, line 505, in onApply<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.logic.setupPythonRequirements()<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules/MONAIAuto3DSeg.py”, line 1062, in setupPythonRequirements<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     torch = torchLogic.installTorch(askConfirmation=True, torchVersionRequirement = f"&gt;={minimumTorchVersion}")<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/12345/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 225, in installTorch<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     import torch<br>
[CRITICAL][Stream] 15.09.2024 22:53:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ModuleNotFoundError: No module named ‘torch’</p>

---

## Post #18 by @lassoan (2024-09-16 01:13 UTC)

<p>Thanks, thia was very useful. This shows the exact cause of the error:</p>
<aside class="quote no-group" data-username="LukasR" data-post="17" data-topic="26956">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/d78d45/48.png" class="avatar"> LukasR:</div>
<blockquote>
<p>File “C:\Users\12345\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pip_vendor\msgpack\fallback.py”, line 403, in _read<br>
[INFO][Stream] 15.09.2024 22:53:02 (unknown:0) - ret = self._buffer[i : i + n]<br>
[INFO][Stream] 15.09.2024 22:53:02 (unknown:0) - MemoryError</p>
</blockquote>
</aside>
<p>So, you have ran out of memory RAM while unpacking pytorch. It means that your computer has very low amount of available memory, because it has small physical RAM (such as 8GB or less) and there is not enough free disk space either (and so the operating system does not want to allocate more virtual memory). You need to fix this not just for the installation but becaues you will need to have at least about 16GB memory space (physical+virtual memory) for the automatic segmentation, too.</p>
<p>Solution: If you are running some applications that use lots of memory (e.g., you have a web browser with 50 tabs open) then close them and try again. If you still get MemoryError then increase the virtual memory size. You can achieve that by freeing up lots of disk space (then Windows will allocate some of the free disk space as virtual memory) or manually <a href="https://www.windowscentral.com/software-apps/windows-11/how-to-manage-virtual-memory-on-windows-11">allocate more virtual memory in your Windows system settings</a> (I would recommend at least 30GB).</p>

---

## Post #19 by @LukasR (2024-09-16 08:40 UTC)

<p>You were absolutely right with that solution sir. Freeing up more disk space and simultaneously allocating more virtual memory than were the original preset values in Windows system settings finally allowed to install PyTorch Utils (Torch and TorchVision) successfully. Extension MONAI Auto3DSeg is now working flawlessly.</p>
<p>Thank you very much for your help, time and patience</p>

---

## Post #21 by @lassoan (2025-07-29 23:29 UTC)

<p>You need to install pytorch. TotalSegmentator should do it automatically, but it makes sense to install manually because it is easier to see any errors.</p>
<p>TotalSegmentator will need SlicerNNUnet extension. It seems that you have rejected its installation when it was offered (or uninstalled it), so you need to install it again.</p>
<p>If you want to use CUDA then on Windows you need to install the appropriate drivers with CUDA support.</p>
<p>What CPU model and GPU do you have? How much free disk space you have?</p>

---

## Post #23 by @muratmaga (2025-07-30 15:53 UTC)

<p>What happens when you choose the CPU as the computation backend, and then click install PyTorch?</p>
<p>You don’t seem to have a NVIDIA gpu, so CUDA part is moot.</p>
<p>Also know that with CPU-only torch, NNInteractive and deep-learnign tools will work slow. The main speed up comes from fast GPUs (which you don’t seem to have in your system).</p>

---

## Post #26 by @lassoan (2025-08-05 13:19 UTC)

<aside class="quote no-group" data-username="ooo" data-post="22" data-topic="26956">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/898d66/48.png" class="avatar"> ooo:</div>
<blockquote>
<p>Intel(R) Core ™ i5 - 10500 CPU @ 3.1 GHz</p>
</blockquote>
</aside>
<p>ThisCPU model was released 5 years ago and it wad not high-end even then, so it is expected that you run into difficulties when you want to use it for CPU-only inference. How much RAM do you have?</p>
<p>Your Python environment is quite messy by now, so I would recommend to remove the entire Slicer installation folder and install Slicee-5.8.1, install only PyTorch extension, and then use it to install a CPU-only pytorch. If you encounter any errors, copy here the content of the Python console and the Slicer application log (menu: Help / Report a bug).</p>

---

## Post #28 by @muratmaga (2025-08-08 15:21 UTC)

<p>You have a long series of SSL errors meaning necessary packages is failing to download on this connection. This happens sometimes when institutions use their own unsigned certificates or have strict firewalls. If thats the case you will have to work with your IT department to resolve the case.</p>
<p>The easiest way to test this is to use a public network and see if things out.</p>

---
