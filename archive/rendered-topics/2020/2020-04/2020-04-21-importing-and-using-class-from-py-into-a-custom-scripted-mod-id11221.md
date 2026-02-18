# Importing and using class from .py into a custom scripted module

**Topic ID**: 11221
**Date**: 2020-04-21
**URL**: https://discourse.slicer.org/t/importing-and-using-class-from-py-into-a-custom-scripted-module/11221

---

## Post #1 by @laura.gelcano (2020-04-21 09:21 UTC)

<p>Hello,</p>
<p>I am using Slicer 4.11.0 on a Windows 10 computer and developing a Python scripted module.</p>
<p>I want to import a class (TripleMRNet from TripleMRNet.py) from my scripted module, so that I can use it in the module. This TripleMRNet.py is in the same directory as the scripted module.</p>
<p>I have tried to import the class directly in the Python Console and it runs well:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8b5d298dbb8dc2f16da4d5e70d84414ac722e54.jpeg" data-download-href="/uploads/short-url/qm1phw3zbD8Cg0HTlX93jC45dqY.jpeg?dl=1" title="load_fromPythonIterator" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8b5d298dbb8dc2f16da4d5e70d84414ac722e54_2_608x500.jpeg" alt="load_fromPythonIterator" data-base62-sha1="qm1phw3zbD8Cg0HTlX93jC45dqY" width="608" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8b5d298dbb8dc2f16da4d5e70d84414ac722e54_2_608x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8b5d298dbb8dc2f16da4d5e70d84414ac722e54.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8b5d298dbb8dc2f16da4d5e70d84414ac722e54.jpeg 2x" data-dominant-color="F2F3EF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">load_fromPythonIterator</span><span class="informations">621×510 74.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, when I tried to use it in my scripted module I get the following error:<br>
AttributeError: Can’t get attribute ‘TripleMRNet’ on &lt;module ‘<strong>main</strong>’ (built-in)&gt;</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b48e2d930538ae18454f657dcd5e29e23a1d7629.jpeg" alt="load_fromScriptedModule" data-base62-sha1="pLgyHsFLgQ39do7bL5y3U2koMQh" width="607" height="189"></p>
<p>Any help is appreciated.</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2020-04-21 15:34 UTC)

<aside class="quote no-group" data-username="laura.gelcano" data-post="1" data-topic="11221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/c77e96/48.png" class="avatar"> laura.gelcano:</div>
<blockquote>
<p>This TripleMRNet.py is in the same directory as the scripted module.</p>
</blockquote>
</aside>
<p>Slicer expects all .py files in a scripted module folder to be Slicer module, so you need to put all additional files into regular <a href="https://realpython.com/python-modules-packages/#python-packages">Python packages</a> in subfolders. See <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/ExtensionWizard">Extension wizard module</a> and its ExtensionWizardLib package as an example.</p>
<p>The only complication is that you need to implement dynamic reloading of custom packages, if you want to reload your module without restarting Slicer. See this post for details: <a href="https://discourse.slicer.org/t/python-scripted-module-development-reload-feature-for-multiple-files/6363/4" class="inline-onebox">Python scripted module development reload feature for multiple files - #4 by lassoan</a></p>

---

## Post #3 by @laura.gelcano (2020-04-22 10:56 UTC)

<p>Thank you so much, now it works perfectly.</p>

---
