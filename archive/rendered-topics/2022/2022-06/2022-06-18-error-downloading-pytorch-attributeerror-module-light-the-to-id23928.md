# Error downloading pytorch: "AttributeError: module ‘light_the_torch’ has no attribute ‘find_links’"

**Topic ID**: 23928
**Date**: 2022-06-18
**URL**: https://discourse.slicer.org/t/error-downloading-pytorch-attributeerror-module-light-the-torch-has-no-attribute-find-links/23928

---

## Post #1 by @hourglassnam (2022-06-18 15:01 UTC)

<p>Hello,<br>
I want to download PyTorch to use TorchIO for the data augmentation process.<br>
I installed TorchIO and PyTorch Utils, but when I tried to install PyTorch using PyTorch Utils it gave me an attribution error.<br>
I tried the installation on 3D slicer version 4.13.0 and 5.1.0 using my window10 computer, but nothing worked.<br>
I tested installation on a different computer, which worked fine and confused me even more.<br>
I got the following message.<br>
Could you please give me some advice?<br>
Thank you very much.</p>
<blockquote>
<p>Importing torch…<br>
Querying light-the-torch for torch wheel…<br>
Requirement already satisfied: light-the-torch in c:\users\njy95\appdata\local\na-mic\slicer 5.1.0-2022-06-14\lib\python\lib\site-packages (0.4.0)<br>
Requirement already satisfied: pip!=22.0,!=22.0.1,!=22.0.2,&lt;22.2,&gt;=22.0 in c:\users\njy95\appdata\local\na-mic\slicer 5.1.0-2022-06-14\lib\python\lib\site-packages (from light-the-torch) (22.0.3)<br>
WARNING: You are using pip version 22.0.3; however, version 22.1.2 is available.<br>
You should consider upgrading via the ‘C:\Users\njy95\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-14\bin\python-real.exe -m pip install --upgrade pip’ command.<br>
Traceback (most recent call last):<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 5.1.0-2022-06-14/NA-MIC/Extensions-31027/PyTorch/lib/Slicer-5.1/qt-scripted-modules/PyTorchUtils.py”, line 40, in onInstallTorch<br>
torch = PyTorchUtilsLogic().torch<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 5.1.0-2022-06-14/NA-MIC/Extensions-31027/PyTorch/lib/Slicer-5.1/qt-scripted-modules/PyTorchUtils.py”, line 55, in torch<br>
self._torch = self.importTorch()<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 5.1.0-2022-06-14/NA-MIC/Extensions-31027/PyTorch/lib/Slicer-5.1/qt-scripted-modules/PyTorchUtils.py”, line 80, in importTorch<br>
torch = self.installTorch()<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 5.1.0-2022-06-14/NA-MIC/Extensions-31027/PyTorch/lib/Slicer-5.1/qt-scripted-modules/PyTorchUtils.py”, line 99, in installTorch<br>
slicer.util.pip_install(self.wheelURL)<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 5.1.0-2022-06-14/NA-MIC/Extensions-31027/PyTorch/lib/Slicer-5.1/qt-scripted-modules/PyTorchUtils.py”, line 63, in wheelURL<br>
self._wheel = self.getTorchUrl()<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 5.1.0-2022-06-14/NA-MIC/Extensions-31027/PyTorch/lib/Slicer-5.1/qt-scripted-modules/PyTorchUtils.py”, line 114, in getTorchUrl<br>
wheelUrl = ltt.find_links([‘torch’])[0]<br>
AttributeError: module ‘light_the_torch’ has no attribute ‘find_links’</p>
</blockquote>

---

## Post #2 by @jamesobutler (2022-06-18 16:35 UTC)

<p><a class="mention" href="/u/fernando">@Fernando</a> recently pushed <a href="https://github.com/fepegar/SlicerPyTorch/commit/b1f33d6527509a607576e544cf225a67bcabe437" class="inline-onebox" rel="noopener nofollow ugc">Add upper bound for light-the-torch requirement · fepegar/SlicerPyTorch@b1f33d6 · GitHub</a> to address this issue by using a 2020 version of <code>pip</code> instead of the newer 2022 version of <code>pip</code> included by default in Slicer. You will be able to update the PyTorch Slicer extension tomorrow to get this latest versions or you can directly install PyTorch with the method in the linked commit.</p>

---

## Post #3 by @hourglassnam (2022-06-18 17:05 UTC)

<p>Thank you so much for your help!<br>
I was able to install pytorch with the link you provided!! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
