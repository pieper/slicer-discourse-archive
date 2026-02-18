# BoneTexture extension Attribute error

**Topic ID**: 32863
**Date**: 2023-11-16
**URL**: https://discourse.slicer.org/t/bonetexture-extension-attribute-error/32863

---

## Post #1 by @thangngoc89 (2023-11-16 16:00 UTC)

<p>I encountered an error with BoneTexture module, it’s probably because it wasn’t updated with the latest code changes from 3D Slicer.</p>
<p>As soon as I load the BoneTexture module, an error was thrown in the console and none of the function would work.</p>
<pre><code class="lang-auto">Traceback (most recent call last):

File "/Applications/Slicer.app/Contents/Extensions-31938/BoneTextureExtension/lib/Slicer-5.4/qt-scripted-modules/BoneTexture.py", line 155, in setup

self.vectorToScalarVolumeConversionWidget = VectorToScalarVolume.VectorToScalarVolumeConversionMethodWidget()

AttributeError: module 'VectorToScalarVolume' has no attribute 'VectorToScalarVolumeConversionMethodWidget'
</code></pre>
<p>I’ve looked around the commit history of Slicer and <code>VectorToScalarVolumeConversionMethodWidget</code> was removed in <a href="https://github.com/Slicer/Slicer/commit/41adaa558f44e2cbe5d06053fd7b79b473e431e0#diff-9644ea9d931812f2dca3ce5c4ed35b5e15dc1518ea63de8b3967908a324d8379L162" rel="noopener nofollow ugc">this commit in 2022</a></p>
<p>I’ve tested this on Windows, MacOS (M2) and Linux, it’s throwing the same error.<br>
I’ve tested this multiple stable releases from latest preview (5.5.0-2023-11-14) to 5.0.2.<br>
The last working 3D Slicer version for this extension is 5.0.3.</p>

---

## Post #2 by @pieper (2023-11-16 18:55 UTC)

<p>You can report this at the BoneTexture repository:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Kitware/BoneTextureExtension/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Kitware/BoneTextureExtension/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/90e65d9cbce8e079a4c259295eb4efc6ef3580f37b9fbbc018d396e2c13d99f3/Kitware/BoneTextureExtension" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Kitware/BoneTextureExtension/issues" target="_blank" rel="noopener">Issues · Kitware/BoneTextureExtension</a></h3>

  <p>Slicer extensions for computing feature maps of N-Dimensional images using well-known texture analysis methods. - Issues · Kitware/BoneTextureExtension</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Even better, maybe you an propose a fix.</p>

---

## Post #3 by @thangngoc89 (2023-11-16 19:18 UTC)

<p>Thank you for your reply. I’ve tried to take a look at the code but due to my unfamiliarity with Slicer’s internals, I have no ideas how to fix it or where to even start. I will create an issue in the extension’s issues tracker</p>

---
