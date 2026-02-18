# Mixing Modules, and Extensions

**Topic ID**: 7596
**Date**: 2019-07-15
**URL**: https://discourse.slicer.org/t/mixing-modules-and-extensions/7596

---

## Post #1 by @jazlynn21100 (2019-07-15 21:51 UTC)

<p>I’ve been digging on the internet for just over a week to try and figure out how to merge modules. From what I have found, it would seem like an extension is my best bet. However, my 3D slicer won’t load the extension catalogue, and I haven’t been able to load it in browser to scroll through either.</p>
<p>I’m doing a ‘segmentation’ using masks, and to complete it the way that we want it, we have to use 3 different modules (Editor/Model Maker/Models). The only issue is that my lab wants it to be automated, so they would just plug in the image files, and 3D slicer would run everything on its own using set parameters. I was wondering what the best way to go about this is!</p>
<p>Also if anyone knows why the extension catalogue is unavailable to me, I would love to know that information as well.</p>

---

## Post #2 by @pieper (2019-07-16 00:25 UTC)

<p>Hi -</p>
<p>A couple suggestions:</p>
<ul>
<li>
<p>you can update to use the Segment Editor (in the latest release) and use it in place of the Editor and ModelMaker steps. (<a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Segmentation" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Segmentation</a>)</p>
</li>
<li>
<p>to automate things in Slicer you can use python scripting, which is very powerful and not too hard to learn (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting</a>)</p>
</li>
</ul>
<p>As for the extension catalog it should be available.  Maybe these links will help you debug.</p>
<p><a href="https://discourse.slicer.org/t/trouble-with-extension-manager/2457">https://discourse.slicer.org/t/trouble-with-extension-manager/2457</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F</a></p>
<p>Hope that helps.</p>

---

## Post #3 by @jazlynn21100 (2019-07-16 16:55 UTC)

<p>Thank you! I’ll try this!</p>

---

## Post #4 by @lassoan (2019-07-18 02:23 UTC)

<p>A post was split to a new topic: <a href="/t/use-segment-editor-from-python/7648">Use segment editor from Python</a></p>

---

## Post #5 by @lassoan (2019-08-01 04:12 UTC)

<p>A post was split to a new topic: <a href="/t/segmentation-using-thresholding-using-python/7833">Segmentation using thresholding using Python</a></p>

---
