# Error while installing Extension Pytorch utils 

**Topic ID**: 33261
**Date**: 2023-12-06
**URL**: https://discourse.slicer.org/t/error-while-installing-extension-pytorch-utils/33261

---

## Post #1 by @Novak_xu (2023-12-06 18:00 UTC)

<p>Hello, dear repositories<br>
I am having trouble installing Pytorch utils in slicer 5.6.0. When I click the botton “install PyTorch”, it says pytorch will be installed using light-the-torch. After few minutes, I get the error:  <code>ModuleNotFoundError: No module named 'torch'</code>.</p>
<p><strong>Detailed error:</strong></p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\Users\jaxni\AppData\Local\slicer.org\Slicer 5.6.0\bin\Python\slicer\util.py", line 3252, in tryWithErrorDisplay
    yield
  File "C:/Users/jaxni/AppData/Local/slicer.org/Slicer 5.6.0/slicer.org/Extensions-32390/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py", line 78, in onInstallTorch
    torch = self.logic.installTorch(askConfirmation, None if automaticBackend else backend, torchVersionRequirement, torchvisionVersionRequirement)
  File "C:/Users/jaxni/AppData/Local/slicer.org/Slicer 5.6.0/slicer.org/Extensions-32390/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py", line 225, in installTorch
    import torch
ModuleNotFoundError: No module named 'torch'
</code></pre>
<p>To use the TotalSegamentor, I need to install this Pytorch utils.<br>
<strong>Meanwhile, I tried to uninstall pytorch and uninstall the extension  Pytorch utils, then install. The Error happened again. I also uninstall the 5.6.0 Slicer, did not use.</strong></p>
<p><strong>I also went the Pytorch utils Github Home Page, use the python Console to install (Follow the guide in the READE.md). Similar Error happened.</strong></p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 2, in &lt;module&gt;
  File "C:/Users/jaxni/AppData/Local/slicer.org/Slicer 5.6.0/slicer.org/Extensions-32390/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py", line 154, in torch
    self._torch = self.importTorch()
  File "C:/Users/jaxni/AppData/Local/slicer.org/Slicer 5.6.0/slicer.org/Extensions-32390/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py", line 186, in importTorch
    torch = self.installTorch()
  File "C:/Users/jaxni/AppData/Local/slicer.org/Slicer 5.6.0/slicer.org/Extensions-32390/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py", line 225, in installTorch
    import torch
ModuleNotFoundError: No module named 'torch'
</code></pre>
<p>Please let me know  “Am I doing the wrong flow path?” and How I solve this Error?</p>
<p>Thank you for your time, I truly appreciate your support.</p>

---

## Post #2 by @lassoan (2023-12-06 18:02 UTC)

<p>PyTorch may need about 20GB free disk space during installation. I would recommend to delete your <code>C:/Users/jaxni/AppData/Local/slicer.org/Slicer 5.6.0</code> folder, reinstall Slicer from scratch, and make sure you have 20GB+ disk space and solid network connection.</p>

---
