---
topic_id: 26715
title: "Totalsegmentator Error At First Run Command Pip Install Git"
date: 2022-12-13
url: https://discourse.slicer.org/t/26715
---

# TotalSegmentator error at first run: "Command ‘pip’, ‘install’, ‘git+https://github.com/wasserth/TotalSegmentator.git’, ‘–no-deps’]’ returned non-zero exit status"

**Topic ID**: 26715
**Date**: 2022-12-13
**URL**: https://discourse.slicer.org/t/totalsegmentator-error-at-first-run-command-pip-install-git-https-github-com-wasserth-totalsegmentator-git-no-deps-returned-non-zero-exit-status/26715

---

## Post #1 by @miuwells (2022-12-13 15:44 UTC)

<p>Hi all, I have just tried the extension and it gives me error, I copy the log for help, I have tried to update Pytorch and it also gives me error.</p>
<p>I think the extension is amazing the amount of elements that can be segmented, congratulations to all the team.</p>
<p>LOG:</p>
<p>Failed to compute results.</p>
<p>Command ‘[‘C:/Users/er_de/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘git+https://github.com/wasserth/TotalSegmentator.git’, ‘–no-deps’]’ returned non-zero exit status 1.</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\er_de\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/er_de/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 248, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “C:/Users/er_de/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 532, in setupPythonRequirements<br>
slicer.util.pip_install(totalSegmentatorPackage + " --no-deps" + (" --upgrade" if upgrade else “”))<br>
File “C:\Users\er_de\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3571, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\er_de\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3533, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\er_de\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3502, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/er_de/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘git+https://github.com/wasserth/TotalSegmentator.git’, ‘–no-deps’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @lassoan (2022-12-13 15:50 UTC)

<p>It might have been just a temporary problem. Please try to restart Slicer and run the segmentation again. If it still reports issues then you may get more information about the problem by installing TotalSegmentator from the Windows terminal:</p>
<p><code>"C:\Users\er_de\AppData\Local\NA-MIC\Slicer 5.2.1\bin/PythonSlicer.EXE" -m pip install git+https://github.com/wasserth/TotalSegmentator.git --no-deps</code></p>

---

## Post #3 by @tsehrhardt (2022-12-13 15:56 UTC)

<p>I’m having the same issue. I get the error message, but it also shows that the TotalSegmentator Python package is installing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57dfd8d2cd33f6e6d3f5254dd22f801ea3b95428.png" data-download-href="/uploads/short-url/cxn837ft98vBHPR0CNwuVhVJWkw.png?dl=1" title="2022-12-13_10-55-10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57dfd8d2cd33f6e6d3f5254dd22f801ea3b95428_2_662x500.png" alt="2022-12-13_10-55-10" data-base62-sha1="cxn837ft98vBHPR0CNwuVhVJWkw" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57dfd8d2cd33f6e6d3f5254dd22f801ea3b95428_2_662x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57dfd8d2cd33f6e6d3f5254dd22f801ea3b95428_2_993x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57dfd8d2cd33f6e6d3f5254dd22f801ea3b95428_2_1324x1000.png 2x" data-dominant-color="C3C3CD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-12-13_10-55-10</span><span class="informations">2124×1602 420 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2022-12-13 16:02 UTC)

<p><a class="mention" href="/u/tsehrhardt">@tsehrhardt</a> Please do the same - restart Slicer and try again, and if you see the error again then run the install command from the Windows terminal</p>
<p><code>"c:\users\starb\appdata\local\na-mic\Slicer 5.2.1\bin\PythonSlicer.exe" -m pip install git+https://github.com/wasserth/TotalSegmentator.git --no-deps</code></p>

---

## Post #5 by @tsehrhardt (2022-12-13 16:15 UTC)

<p>Got this:</p>
<pre><code class="lang-auto">ERROR: Error [WinError 2] The system cannot find the file specified while executing command git clone -q https://github.com/wasserth/TotalSegmentator.git 'C:\Users\starb\AppData\Local\Temp\pip-req-build-2aahpc_y'
ERROR: Cannot find command 'git' - do you have 'git' installed and in your PATH?
</code></pre>
<p>I also just when straight to the git for Total Segmentator to install it as a standalone and got the following:</p>
<pre><code class="lang-auto">ERROR: Cannot install totalsegmentator==1.2, totalsegmentator==1.3 and totalsegmentator==1.4.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    totalsegmentator 1.4.0 depends on SimpleITK==2.0.2
    totalsegmentator 1.3 depends on SimpleITK==2.0.2
    totalsegmentator 1.2 depends on SimpleITK==2.0.2

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
</code></pre>

---

## Post #6 by @lassoan (2022-12-13 16:22 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="5" data-topic="26715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p><code>Cannot find command 'git' - do you have 'git' installed and in your PATH?</code></p>
</blockquote>
</aside>
<p>This may be the issue. Could you please <a href="https://git-scm.com/downloads">install git</a> and retry?</p>
<aside class="quote no-group" data-username="tsehrhardt" data-post="5" data-topic="26715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<pre><code class="lang-auto">ERROR: Cannot install totalsegmentator==1.2, totalsegmentator==1.3 and totalsegmentator==1.4.0 because these package versions have conflicting dependencies.
</code></pre>
</blockquote>
</aside>
<p>This is normal, TotalSegmentator must first be installed without dependencies (<code>--no-deps</code>), because of a <a href="https://github.com/wasserth/TotalSegmentator/issues/32">SimpleITK bug</a>. The extension implements a special technique to work around the limitation.</p>

---

## Post #7 by @tsehrhardt (2022-12-13 16:29 UTC)

<p>That helped. It went one step further but then gave me this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc90a6bf0735f4a87faf4e2a53d899bf0ffc6511.png" data-download-href="/uploads/short-url/vtcXmYXPzsx8omWDkkCIJmJt6Dv.png?dl=1" title="2022-12-13_11-28-26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc90a6bf0735f4a87faf4e2a53d899bf0ffc6511.png" alt="2022-12-13_11-28-26" data-base62-sha1="vtcXmYXPzsx8omWDkkCIJmJt6Dv" width="690" height="241" data-dominant-color="E9E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-12-13_11-28-26</span><span class="informations">1002×350 21.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and this:</p>
<pre><code class="lang-auto">Processing started

Writing input file to C:/Users/starb/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-13_11+27+45.797/total-segmentator-input.nii

Creating segmentations with TotalSegmentator AI...

Total Segmentator arguments: ['-i', 'C:/Users/starb/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-13_11+27+45.797/total-segmentator-input.nii', '-o', 'C:/Users/starb/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-13_11+27+45.797/segmentation', '--ml', '--task', 'total', '--fast']

File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator", line 10, in &lt;module&gt;

ModuleNotFoundError: No module named 'nibabel'
</code></pre>

---

## Post #8 by @miuwells (2022-12-13 16:45 UTC)

<p>It works for me. I installed GIT and now it works perfectly.<br>
Thank you very much for your help.</p>

---

## Post #9 by @lassoan (2022-12-13 16:51 UTC)

<p>This looks great, the main problem was solved. You now need to install the extension properly. If “Upgrade” in Advanced section does not work then probably the simplest is to reinstall Slicer and TotalSegmentator.</p>
<p>I’ll see if I can avoid the git installation to make the installation simpler.</p>

---

## Post #10 by @tsehrhardt (2022-12-13 17:25 UTC)

<p>It’s working now. Thank you!</p>

---

## Post #11 by @lassoan (2022-12-13 19:56 UTC)

<p>Thanks for the feedbacks. I’ve added automatic detection of git and now a more meaningful message is displayed if it is not found. I’ve also implemented automatic installation of git on Windows to make the setup a bit easier.</p>

---

## Post #12 by @lassoan (2022-12-15 19:56 UTC)

<p>3 posts were split to a new topic: <a href="/t/totalsegmentator-error-at-first-run-command-python-scripts-totalsegmentator-returned-non-zero-exit-status-120/26755">TotalSegmentator error at first run: Command …Python\Scripts\TotalSegmentator… returned non-zero exit status 120</a></p>

---

## Post #13 by @Knoch (2022-12-19 07:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>-m pip install git+https://github.com/wasserth/TotalSegmentator.git --no-deps</p>
</blockquote>
</aside>
<p>Hi Lassoan,</p>
<p>can you please help me, already installed the extention for the TotalSegementator, but now the slicer is not responding now, try to restart the program, and always not responding.</p>
<p>using the GPU 3070. there no error message, since its says successfully installed the extention, installed the git, etc.</p>
<p>thank you.</p>

---

## Post #14 by @rbumm (2022-12-19 09:03 UTC)

<p>Could you describe in more detail what happens exactly?</p>
<p>Please use the CTChest demo data for a test.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbca799241a9e5101e9c8e9b8c8001fdacde4b7e.png" alt="image" data-base62-sha1="zVrE1pKnVnPTYRiWL0CxvLi7QCO" width="567" height="392"></p>
<p>Select the TotalSegmentator extension and press “Apply”.<br>
Do you see any progress messages in the textbox?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86cb0f4224c2c3ca2a4f96b956ea5ae55bbeee46.png" data-download-href="/uploads/short-url/jer27AJitshrFlUKJ7jaTQ9QuUe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86cb0f4224c2c3ca2a4f96b956ea5ae55bbeee46_2_625x500.png" alt="image" data-base62-sha1="jer27AJitshrFlUKJ7jaTQ9QuUe" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86cb0f4224c2c3ca2a4f96b956ea5ae55bbeee46_2_625x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86cb0f4224c2c3ca2a4f96b956ea5ae55bbeee46.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86cb0f4224c2c3ca2a4f96b956ea5ae55bbeee46.png 2x" data-dominant-color="D1CFCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">840×672 35.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @Knoch (2023-01-03 02:58 UTC)

<p>Hi Rudolf,</p>
<p>thank you for the reply, i just come from my holiday so just open the forum.</p>
<p>yes, i do have press the apply, and nothing happen until the error message <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Traceback (most recent call last):<br>
File “C:\Users\ACER\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 715, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 624, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\ACER\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/ACER/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_09+44+38.651/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/ACER/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_09+44+38.651/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>
<p>any suggestion regarding this?</p>

---

## Post #16 by @lassoan (2023-01-03 03:01 UTC)

<p>Does clicking on “Upgrade” button in Advanced section and restarting Slicer fixes the issue?</p>
<p>Do you have a GPU? How much GPU RAM does it have?</p>

---

## Post #17 by @Knoch (2023-01-03 03:17 UTC)

<p>ITry to un-install the pytorch and reinstall, restarts the slicer, and now is working, but only the “fast” mode. for the non fast mode, its still got the same error.</p>
<p>Yes, I am Using Acer Predator with GPU RTX 3070 with 8GB RAM.</p>

---

## Post #18 by @lassoan (2023-01-03 03:25 UTC)

<p>Do you use CPU or GPU pytorch?</p>
<p>Does your computer have multiple graphics card (e.g., Intel integrated graphics + NVIDIA discrete GPU)? Have you configured your NVIDIA settings to make Slicer use the GPU?</p>
<p>Do you have problems with any of the Slicer sample data sets?</p>
<p>Could you copy here the output in the textbox below the Apply button when you run with “Fast” checkbox disabled?</p>

---

## Post #19 by @Knoch (2023-01-03 04:21 UTC)

<p>i dont have the option for the GPU, where can I install this? the option is only CPU, Automatic, and Cu80 until Cu112</p>
<p>this is the error message for the Fast Disabled using the sample data set CTChest:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\ACER\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 715, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 624, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\ACER\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/ACER/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_11+15+30.020/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/ACER/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_11+15+30.020/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>

---

## Post #20 by @Knoch (2023-01-03 04:37 UTC)

<p>this is my Pytorch status</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c3b2013e7582c14ad95d16a49ea9e809eddd65d.png" data-download-href="/uploads/short-url/6jhGpB78DGBlPCqc8Q5vlBnrwFT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c3b2013e7582c14ad95d16a49ea9e809eddd65d_2_690x473.png" alt="image" data-base62-sha1="6jhGpB78DGBlPCqc8Q5vlBnrwFT" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c3b2013e7582c14ad95d16a49ea9e809eddd65d_2_690x473.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c3b2013e7582c14ad95d16a49ea9e809eddd65d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c3b2013e7582c14ad95d16a49ea9e809eddd65d.png 2x" data-dominant-color="393938"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">745×511 49.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @lassoan (2023-01-03 06:29 UTC)

<p>It seems that you have an old driver and CUDA version installed, which may cause incompatibility issues.</p>
<p>Please install the <a href="https://pytorch.org/get-started/locally/">latest CUDA version that pytorch supports</a> - currently CUDA 11.6 or 11.7 - and then <a href="https://github.com/lassoan/SlicerTotalSegmentator/#segmentation-fails-while-predicting">uninstall and install pytorch</a>.</p>

---

## Post #22 by @Knoch (2023-01-03 07:13 UTC)

<p>Already update the drivers, but still got the error message:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9748b9ee276fcc3979a27b23975f60a04a29ac6.png" alt="image" data-base62-sha1="v1Hj7E2F0BpSTN1RzZtLdiPURkG" width="440" height="312"></p>
<p>the message:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\ACER\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 715, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 624, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/ACER/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\ACER\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/ACER/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_14+12+33.314/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/ACER/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_14+12+33.314/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>

---

## Post #23 by @lassoan (2023-01-03 07:17 UTC)

<p>How much memory your GPU has? Do you have issues with all data sets or just some of them?</p>
<p>Probably the best is if you remove Slicer and reinstall it. All the experimentation with installing various pytorch versions may have messed things up.</p>

---

## Post #24 by @rbumm (2023-01-03 08:41 UTC)

<p>On my borderline laptop, I get a “less than 7 GB” warning for a “total” TotalSegmentator run with the CTChest sample dataset.</p>
<p>If I select “No” (no FAST mode) → </p>
<p>Processing completed in 226.51 seconds</p>
<p>System Settings:</p>
<p>NVIDIA System Information report created on: 01/03/2023 09:17:56<br>
System name: LAPTOP-xxxxxxxxxx</p>
<p>[Display]<br>
Operating System:	Windows 10 Home, 64-bit<br>
DirectX version:	12.0<br>
GPU processor:		NVIDIA GeForce GTX 1060<br>
Driver version:		526.98<br>
Driver Type:		DCH<br>
Direct3D feature level:	12_1<br>
CUDA Cores:		1280<br>
Core clock:		1404 MHz<br>
Memory data rate:	8.01 Gbps<br>
Memory interface:	192-bit<br>
Memory bandwidth:	192.19 GB/s<br>
Total available graphics memory:	14278 MB<br>
Dedicated video memory:	6144 MB GDDR5<br>
System video memory:	0 MB<br>
Shared system memory:	8134 MB<br>
Video BIOS version:	86.06.3A.00.0F<br>
IRQ:			Not used<br>
Bus:			PCI Express x16 Gen3<br>
Device Id:		10DE 1C20 114E1025<br>
Part Number:		2914 0030</p>
<p>Could you post your system information? See NVIDIA Control Panel → System Information</p>

---

## Post #25 by @pixellett (2023-01-03 09:29 UTC)

<p>I am having the same issue with “returned non-zero exit status 120”</p>
<p>I have a clean install of Slicer 5.2.1.  Am running with 128Gigs RAM and a 3090Ti with 24Gigs.<br>
PyTorch is 1.13.1+cu117</p>
<p>I have noticed that the file that is saved in the …/fold_0 folder during processing is only called model_final_checkpoint.model - it does not have the .pkl extension as well - not sure if that is the issue?</p>
<p><strong>TotalSegmentator window:</strong><br>
Processing started<br>
Writing input file to C:/Users/282745H/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_17+18+42.605/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/282745H/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_17+18+42.605/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/282745H/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_17+18+42.605/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
Traceback (most recent call last):<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 201, in <br>
main()<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 179, in main<br>
seg = nnUNet_predict_image(args.input, args.output, task_id, model=model, folds=folds,<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 232, in nnUNet_predict_image<br>
nnUNet_predict(tmp_dir, tmp_dir, task_id, model, folds, trainer, tta)<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 106, in nnUNet_predict<br>
predict_from_folder(model_folder_name, dir_in, dir_out, folds, save_npz, num_threads_preprocessing,<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\inference\predict.py”, line 668, in predict_from_folder<br>
return predict_cases_fastest(model, list_of_lists[part_id::num_parts], output_files[part_id::num_parts], folds,<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\inference\predict.py”, line 468, in predict_cases_fastest<br>
trainer, params = load_model_and_checkpoint_files(model, folds, mixed_precision=mixed_precision, checkpoint_name=checkpoint_name)<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\training\model_restore.py”, line 140, in load_model_and_checkpoint_files<br>
trainer = restore_model(join(folds[0], “%s.model.pkl” % checkpoint_name), fp16=mixed_precision)<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\training\model_restore.py”, line 56, in restore_model<br>
info = load_pickle(pkl_file)<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\batchgenerators\utilities\file_and_folder_operations.py”, line 49, in load_pickle<br>
with open(file, mode) as f:<br>
<strong>FileNotFoundError: [Errno 2] No such file or directory: ‘C:\Users\282745H\.totalsegmentator\nnunet\results\nnUNet\3d_fullres\Task256_TotalSegmentator_3mm_1139subj\nnUNetTrainerV2_ep8000_nomirror__nnUNetPlansv2.1\fold_0\model_final_checkpoint.model.pkl’</strong><br>
<strong>Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x000002BC5A99A730&gt;</strong><br>
<strong>AttributeError: ‘DummyFile’ object has no attribute ‘flush’</strong><br>
<strong>Using ‘fast’ option: resampling to lower resolution (3mm)</strong><br>
Resampling…<br>
Resampled in 0.88s<br>
Predicting…</p>
<p><strong>Small popup error window:</strong><br>
Traceback (most recent call last):<br>
File “C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/282745H/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/282745H/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 715, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/282745H/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 624, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/282745H/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\282745H\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/282745H/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_17+18+42.605/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/282745H/AppData/Local/Temp/Slicer/__SlicerTemp__2023-01-03_17+18+42.605/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>

---

## Post #26 by @Knoch (2023-01-03 09:38 UTC)

<p>Already re-install my slicer, instal totalsegmentator and the pytorch again, but the same result</p>
<p>This is my system information:</p>
<p>NVIDIA System Information report created on: 01/03/2023 16:36:34<br>
System name: PREDATOR</p>
<p>[Display]<br>
Operating System:	Windows 10 Home Single Language, 64-bit<br>
DirectX version:	12.0<br>
GPU processor:		NVIDIA GeForce RTX 3070 Laptop GPU<br>
Driver version:		527.56<br>
Driver Type:		DCH<br>
Direct3D feature level:	12_1<br>
CUDA Cores:		5120<br>
Resizable BAR		Yes<br>
Max-Q Technologies	3rd Gen<br>
Dynamic Boost 2.0	Yes<br>
WhisperMode 2.0		Yes<br>
Advanced Optimus	No<br>
Maximum Graphics Power	100 W<br>
Core clock:		1290 MHz<br>
Memory data rate:	12.00 Gbps<br>
Memory interface:	256-bit<br>
Memory bandwidth:	384.06 GB/s<br>
Total available graphics memory:	16299 MB<br>
Dedicated video memory:	8192 MB GDDR6<br>
System video memory:	0 MB<br>
Shared system memory:	8107 MB<br>
Video BIOS version:	94.04.2B.40.2B<br>
IRQ:			Not used<br>
Bus:			PCI Express x16 Gen3<br>
Device Id:		10DE 249D 14421025<br>
Part Number:		4735 0010</p>

---

## Post #27 by @rbumm (2023-01-03 09:57 UTC)

<p>Sorry for the errors, hope we can fix them. The two systems indicated above should definitely be capable of doing complete TotalSegmentator GPU runs.</p>
<p>Please understand that the 3D Slicer extension is a wrapper of the TotalSegmentator AI tool.<br>
Have you tried something simple as running Slicer in Admin mode?</p>
<p>You could also install TotalSegmentator in a local Python installation and run it from the command line, which is what we did before implementing the tool wrapper in 3D Slicer.</p>

---

## Post #28 by @rbumm (2023-01-03 11:44 UTC)

<p>Could you uninstall PyTorch completely with the PyTorch extension.<br>
Use the restart option and repeat until you get a uninstall success message.<br>
Then paste</p>
<pre><code class="lang-auto">slicer.util.pip_install("torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117")
</code></pre>
<p>it into the Python Interactor and press return and wait until it is installed.</p>

---

## Post #29 by @lassoan (2023-01-03 15:04 UTC)

<aside class="quote no-group quote-modified" data-username="pixellett" data-post="25" data-topic="26715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pixellett/48/17897_2.png" class="avatar"> pixellett:</div>
<blockquote>
<p>FileNotFoundError: [Errno 2] No such file or directory: ‘C:\Users\282745H.totalsegmentator\nnunet\results\nnUNet\3d_fullres\Task256_TotalSegmentator_3mm_1139subj\nnUNetTrainerV2_ep8000_nomirror__nnUNetPlansv2.1\fold_0\model_final_checkpoint.model.pkl’</p>
</blockquote>
</aside>
<p>This looks like a real error. Maybe the model download have been interrupted. Please remove the entire <code>.totalsegmentator</code> folder and retry.</p>
<aside class="quote no-group" data-username="Knoch" data-post="26" data-topic="26715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/4491bb/48.png" class="avatar"> Knoch:</div>
<blockquote>
<p>NVIDIA GeForce RTX 3070 Laptop GPU</p>
</blockquote>
</aside>
<p>Laptop with Optimus technology (switchable integrated graphics/discrete GPU) are always problematic. As a quick test, disable Optimus (choose to always use the GPU for all software) and see if it fixes the issue. If you still get some error then you can contact me in a private message to set up a call with screen sharing so that I can have a closer look.</p>

---

## Post #30 by @pixellett (2023-01-04 02:12 UTC)

<p>Thank you so much for the response <a class="mention" href="/u/lassoan">@lassoan</a>!  Deleting the .totalsegmentator folder is the only thing I hadn’t thought of, all is now working perfectly.  You are an absolute legend!</p>

---

## Post #31 by @rbumm (2023-01-05 12:42 UTC)

<p>Experienced the same “status 120” error on a fresh AWS EC2 instance today after installation of PyTorch via the extension and running TotalSegmentator.</p>
<p>It happened upon the first run.<br>
Restarted Slicer and “Upgraded” once which resolved the error.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/044b283461c46f70b261f71cfc52aacf0dca043f.png" alt="image" data-base62-sha1="BYVQTY78xWyOhoB8mVcn3MtpdZ" width="575" height="134"></p>
<p>Is your problem solved by now?</p>

---

## Post #32 by @lassoan (2023-01-06 16:43 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> This is very useful information. I’ve updated TotalSegmentator extension following <a href="https://github.com/wasserth/TotalSegmentator/issues/32">fixes in the Python package</a>. We don’t need the SimpleITK installation hack and git installation anymore. Could you try if Slicer-5.2.1 installation with latest TotalSegmentator still runs into status 120 on a fresh EC2 instance?</p>

---

## Post #33 by @rbumm (2023-01-06 17:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Sure. Would I need to fork the extension or just install it from the extension manager?</p>

---

## Post #34 by @lassoan (2023-01-06 17:04 UTC)

<p>Just install Slicer-5.2.1 from scratch and install TotalSegmentator extension from the Extensions Manager.</p>

---

## Post #35 by @rbumm (2023-01-06 18:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Now it works.  On the fresh EC2 instance (g5.xlarge), PyTorch installs completely from the extension and recognizes the new NVIDIA  A10G drivers.</p>
<p>TotalSegmentator installs upon the first run, but takes a while to complete:<br>
Processing completed in 558.95 seconds</p>
<p>The second run:<br>
Processing completed in 110.23 seconds</p>

---

## Post #36 by @lassoan (2023-01-06 18:42 UTC)

<p>Awesome! Thanks for testing.</p>
<p>First run takes long time because the model weight files (about 1.6GB) have to be downloaded. If this delay causes a problem (slow, unreliable, etc) then we found have a look at where the files are hosted and if adding mirrors would make sense.</p>

---

## Post #37 by @Omar_El-Taji (2023-04-30 03:17 UTC)

<p>Hi I am having a similar problem.  I have m2 MacBook. I have tried all the above including updating PyTorch/total seg as well as downloading git. I have also changed from GPU to CPU in edit-application setting–&gt; volume rendering–&gt;VTK CPU (from GPU). I am using sample data. It works for the MRI head. but when I use on CTAP or CT liver or even my own DICOM CT Chest it brings up error messages.</p>
<p>This is my error message<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 2973, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/Applications/Slicer.app/Contents/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 799, in process<br>
self.logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 692, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/9l/6p4fv9qs1gb_22w9xm8_fm2r0000gn/T/Slicer-omarel-taji/__SlicerTemp__2023-04-30_02+17+21.212/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/9l/6p4fv9qs1gb_22w9xm8_fm2r0000gn/T/Slicer-omarel-taji/__SlicerTemp__2023-04-30_02+17+21.212/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>Thanks</p>

---

## Post #38 by @rbumm (2023-05-01 13:03 UTC)

<p>Please start all over again.</p>
<p>It would be great if you could read the <a href="https://github.com/lassoan/SlicerTotalSegmentator#troubleshooting">troubleshooting section</a> of the TotalSegmentator extension in the beginning.</p>
<ul>
<li>Uninstall 3D Slicer and delete the installation directory.</li>
<li>Install 3D Slicer stable in a new directory.</li>
<li>Install the Pytorch extension.</li>
<li>In the Pytorch extension, select CPU support just for a test.</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2db06282a1196c2ca884a26f647b7cf540ee7bef.png" alt="image" data-base62-sha1="6wbo6PtFEfzGWPLcusW3avMq6XZ" width="386" height="414"></p>
<ul>
<li>Install Pytorch.</li>
<li>Restart 3D Slicer.</li>
<li>Install the Totalsegmentator extension.</li>
<li>Load the CT Chest dataset</li>
<li>Run TotalSegmentator (will take longer because of using CPU).</li>
</ul>
<p>If not working, please post the results of the log and/or complete content of progress window here.<br>
We will handle GPU support later, probably by someone who has an M2 Macbook at hand. Not sure GPU support works in this case.</p>

---

## Post #39 by @sain (2023-05-09 09:28 UTC)

<p>I am having a similar problem too.</p>
<p>I installed pytorch module and totalsegmentator in extensions manager，and installed NVIDIA CUDA11.8 and GIT.<br>
But there was still some errors when running the program.Need help to solve this，thx！</p>
<p>Here are the error infos。</p>
<p>first try:<br>
Traceback (most recent call last):<br>
File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 255, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 660, in setupPythonRequirements<br>
slicer.util.pip_install(self.totalSegmentatorPythonPackageDownloadUrl)<br>
File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 3578, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 3540, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 3509, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command '<a href="https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip'%5D'" rel="noopener nofollow ugc">‘C:/Users/sain/Desktop/3DSilcer/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, '[https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip’]’</a> returned non-zero exit status 1.</p>
<p>second try：<br>
Traceback (most recent call last):<br>
File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 255, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 660, in setupPythonRequirements<br>
slicer.util.pip_install(self.totalSegmentatorPythonPackageDownloadUrl)<br>
File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 3578, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 3540, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 3509, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command '<a href="https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip'%5D'" rel="noopener nofollow ugc">‘C:/Users/sain/Desktop/3DSilcer/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, '[https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip’]’</a> returned non-zero exit status 2.</p>

---

## Post #40 by @lassoan (2023-05-09 10:48 UTC)

<p>Could you try with the latest Slicer Preview Release?</p>

---

## Post #41 by @sain (2023-05-10 01:43 UTC)

<p>Thank you for your reply!<br>
When i try with Slicer 5.3.0,there is new error.How can I solve this problem?thx！<br>
Here are the error infos。</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\bin\Python\slicer\util.py”, line 2973, in tryWithErrorDisplay</p>
<p>yield</p>
<p>File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.3.0/slicer.org/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton</p>
<p>self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),</p>
<p>File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.3.0/slicer.org/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 799, in process</p>
<p>self.logProcessOutput(proc)</p>
<p>File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.3.0/slicer.org/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 692, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[‘C:/Users/sain/Desktop/3DSilcer/Slicer 5.3.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/sain/AppData/Local/Temp/Slicer/__SlicerTemp__2023-05-10_09+14+18.597/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/sain/AppData/Local/Temp/Slicer/__SlicerTemp__2023-05-10_09+14+18.597/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>

---

## Post #42 by @lassoan (2023-05-10 01:48 UTC)

<p>What is the pytorch and NVIDIA driver version displayed in Pytorch Utils module?</p>
<p>Could you try to run the segmentation again and copy here all the output that you can find the the application log (menu: Help / Report a bug)?</p>

---

## Post #43 by @sain (2023-05-10 02:07 UTC)

<p>PyTorch:installed version 2.0.1+cu118<br>
NVIDIA driver:installed version 531.14</p>
<p>I try to run the segmentation again and  here are all the output。</p>
<p>Processing started</p>
<p>Writing input file to C:/Users/sain/AppData/Local/Temp/Slicer/__SlicerTemp__2023-05-10_10+01+57.716/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘C:/Users/sain/AppData/Local/Temp/Slicer/__SlicerTemp__2023-05-10_10+01+57.716/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/sain/AppData/Local/Temp/Slicer/__SlicerTemp__2023-05-10_10+01+57.716/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" class="inline-onebox" rel="noopener nofollow ugc">[2208.05868] TotalSegmentator: robust segmentation of 104 anatomical structures in CT images</a></p>
<p>Using ‘fast’ option: resampling to lower resolution (3mm)</p>
<p>Downloading pretrained weights for Task 256 (~230MB) …</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\urllib3\connection.py”, line 174, in _new_conn</p>
<p>conn = connection.create_connection(</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\urllib3\util\connection.py”, line 72, in create_connection</p>
<p>for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\socket.py”, line 954, in getaddrinfo</p>
<p>for res in _socket.getaddrinfo(host, port, family, type, proto, flags):</p>
<p>socket.gaierror: [Errno 11004] getaddrinfo failed</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 703, in urlopen</p>
<p>httplib_response = self._make_request(</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 386, in _make_request</p>
<p>self._validate_conn(conn)</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 1042, in _validate_conn</p>
<p>conn.connect()</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\urllib3\connection.py”, line 358, in connect</p>
<p>self.sock = conn = self._new_conn()</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\urllib3\connection.py”, line 186, in _new_conn</p>
<p>raise NewConnectionError(</p>
<p>urllib3.exceptions.NewConnectionError: &lt;urllib3.connection.HTTPSConnection object at 0x000002D3ADC85D90&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\requests\adapters.py”, line 489, in send</p>
<p>resp = conn.urlopen(</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 787, in urlopen</p>
<p>retries = retries.increment(</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\urllib3\util\retry.py”, line 592, in increment</p>
<p>raise MaxRetryError(_pool, url, error or ResponseError(cause))</p>
<p>urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host=‘<a href="http://zenodo.org" rel="noopener nofollow ugc">zenodo.org</a>’, port=443): Max retries exceeded with url: /record/6802052/files/Task256_TotalSegmentator_3mm_1139subj.zip?download=1 (Caused by NewConnectionError(‘&lt;urllib3.connection.HTTPSConnection object at 0x000002D3ADC85D90&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed’))</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Scripts\TotalSegmentator”, line 93, in </p>
<p>main()</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Scripts\TotalSegmentator”, line 86, in main</p>
<p>totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 157, in totalsegmentator</p>
<p>download_pretrained_weights(task_id)</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 183, in download_pretrained_weights</p>
<p>download_url_and_unpack(WEIGHTS_URL, config_dir)</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 69, in download_url_and_unpack</p>
<p>raise e</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 55, in download_url_and_unpack</p>
<p>with requests.get(url, stream=True) as r:</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\requests\api.py”, line 73, in get</p>
<p>return request(“get”, url, params=params, **kwargs)</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\requests\api.py”, line 59, in request</p>
<p>return session.request(method=method, url=url, **kwargs)</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\requests\sessions.py”, line 587, in request</p>
<p>resp = self.send(prep, **send_kwargs)</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\requests\sessions.py”, line 701, in send</p>
<p>r = adapter.send(request, **kwargs)</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Lib\site-packages\requests\adapters.py”, line 565, in send</p>
<p>raise ConnectionError(e, request=request)</p>
<p>requests.exceptions.ConnectionError: HTTPSConnectionPool(host=‘<a href="http://zenodo.org" rel="noopener nofollow ugc">zenodo.org</a>’, port=443): Max retries exceeded with url: /record/6802052/files/Task256_TotalSegmentator_3mm_1139subj.zip?download=1 (Caused by NewConnectionError(‘&lt;urllib3.connection.HTTPSConnection object at 0x000002D3ADC85D90&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed’))</p>
<p>Failed to compute results.</p>
<p>Command ‘[‘C:/Users/sain/Desktop/3DSilcer/Slicer 5.3.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/sain/AppData/Local/Temp/Slicer/__SlicerTemp__2023-05-10_10+01+57.716/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/sain/AppData/Local/Temp/Slicer/__SlicerTemp__2023-05-10_10+01+57.716/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\bin\Python\slicer\util.py”, line 2973, in tryWithErrorDisplay</p>
<p>yield</p>
<p>File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.3.0/slicer.org/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton</p>
<p>self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),</p>
<p>File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.3.0/slicer.org/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 799, in process</p>
<p>self.logProcessOutput(proc)</p>
<p>File “C:/Users/sain/Desktop/3DSilcer/Slicer 5.3.0/slicer.org/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 692, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[‘C:/Users/sain/Desktop/3DSilcer/Slicer 5.3.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\sain\Desktop\3DSilcer\Slicer 5.3.0\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/sain/AppData/Local/Temp/Slicer/__SlicerTemp__2023-05-10_10+01+57.716/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/sain/AppData/Local/Temp/Slicer/__SlicerTemp__2023-05-10_10+01+57.716/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>

---

## Post #44 by @lassoan (2023-05-10 02:42 UTC)

<aside class="quote no-group" data-username="sain" data-post="43" data-topic="26715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ccd318/48.png" class="avatar"> sain:</div>
<blockquote>
<p>socket.gaierror: [Errno 11004] getaddrinfo failed</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
</blockquote>
</aside>
<p>This indicates that TotalSegmentator could not download the segmentation model weights from the internet. You are either not connected to the internet or firewall/proxy server prevents you from accessing the server.</p>
<p>You can either fix your internet connection (you may need to use VPN if you are in China, etc.) or download the model weights manually (see for example <a href="https://github.com/wasserth/TotalSegmentator/issues/93" class="inline-onebox">Run TotalSegmentator error · Issue #93 · wasserth/TotalSegmentator · GitHub</a> and <a href="https://github.com/wasserth/TotalSegmentator/issues/60" class="inline-onebox">Use pre-downloaded weights in containerised implementation · Issue #60 · wasserth/TotalSegmentator · GitHub</a>).</p>

---

## Post #45 by @sain (2023-05-10 03:40 UTC)

<p>I download the model weights and paste files to the 3d_fullres folder.<br>
It’s working now. Thank you!</p>

---
