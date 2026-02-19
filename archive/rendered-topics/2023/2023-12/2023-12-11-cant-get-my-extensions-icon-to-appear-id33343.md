---
topic_id: 33343
title: "Cant Get My Extensions Icon To Appear"
date: 2023-12-11
url: https://discourse.slicer.org/t/33343
---

# Can't get my extension's icon to appear

**Topic ID**: 33343
**Date**: 2023-12-11
**URL**: https://discourse.slicer.org/t/cant-get-my-extensions-icon-to-appear/33343

---

## Post #1 by @Justin_Kirby (2023-12-11 18:26 UTC)

<p>I’ve tried editing the following files to specify the location of the icon for TCIABrowser, but Slicer still shows the default puzzle icon in the menus:</p>
<ul>
<li><a href="https://github.com/Slicer/ExtensionsIndex/blob/main/TCIABrowser.s4ext" rel="noopener nofollow ugc">https://github.com/Slicer/ExtensionsIndex/blob/main/TCIABrowser.s4ext</a></li>
<li><a href="https://github.com/QIICR/TCIABrowser/blob/master/TCIABrowser/CMakeLists.txt" rel="noopener nofollow ugc">https://github.com/QIICR/TCIABrowser/blob/master/TCIABrowser/CMakeLists.txt</a></li>
<li><a href="https://github.com/QIICR/TCIABrowser/blob/master/CMakeLists.txt" rel="noopener nofollow ugc">https://github.com/QIICR/TCIABrowser/blob/master/CMakeLists.txt</a></li>
</ul>
<p>Interestingly the icon and screenshots do appear properly in the Extension Manager.  Any suggestions?</p>

---

## Post #2 by @jcfr (2023-12-11 19:18 UTC)

<p>Looking at both the <code>Stable</code> and <code>Preview</code> versions of the uploaded extension, we can can confirm the icon is showing up as expected:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Stable</th>
<th>Preview</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4156126f06b92e7938a988b6bd11b5239a3fe947.png" data-download-href="/uploads/short-url/9jZrwKk4Mp8ACqpGxIOEy0J8Laf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4156126f06b92e7938a988b6bd11b5239a3fe947_2_690x390.png" alt="image" data-base62-sha1="9jZrwKk4Mp8ACqpGxIOEy0J8Laf" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4156126f06b92e7938a988b6bd11b5239a3fe947_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4156126f06b92e7938a988b6bd11b5239a3fe947_2_1035x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4156126f06b92e7938a988b6bd11b5239a3fe947_2_1380x780.png 2x" data-dominant-color="EAEAED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1655×937 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/115f2b25948bd7245fd0f0d6539e13e263d11bfc.png" data-download-href="/uploads/short-url/2tG0UlCDF8tVdyODdHgjO0DB3Uo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/115f2b25948bd7245fd0f0d6539e13e263d11bfc_2_690x419.png" alt="image" data-base62-sha1="2tG0UlCDF8tVdyODdHgjO0DB3Uo" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/115f2b25948bd7245fd0f0d6539e13e263d11bfc_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/115f2b25948bd7245fd0f0d6539e13e263d11bfc_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/115f2b25948bd7245fd0f0d6539e13e263d11bfc_2_1380x838.png 2x" data-dominant-color="E6E7EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1587×964 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
</tr>
</tbody>
</table>
</div>

---

## Post #3 by @Justin_Kirby (2023-12-11 20:34 UTC)

<p>Yes, I also see it working in the Extension Manager.  The problem is inside the main GUI of Slicer if you navigate to it in the Module menu:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcda07c1edc3b1e412f8cb0f8306086da4c75e75.png" data-download-href="/uploads/short-url/A4PrV2vjOfeWz4yBYizwe7BBx4N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcda07c1edc3b1e412f8cb0f8306086da4c75e75_2_604x500.png" alt="image" data-base62-sha1="A4PrV2vjOfeWz4yBYizwe7BBx4N" width="604" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcda07c1edc3b1e412f8cb0f8306086da4c75e75_2_604x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcda07c1edc3b1e412f8cb0f8306086da4c75e75_2_906x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcda07c1edc3b1e412f8cb0f8306086da4c75e75_2_1208x1000.png 2x" data-dominant-color="C3C1C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1669×1381 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2023-12-11 20:36 UTC)

<p>Hi <a class="mention" href="/u/justin_kirby">@Justin_Kirby</a> -</p>
<p>You need to include an icon in your repo and refer to it from the cmakelists for your module.  Like this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/CMakeLists.txt#L11">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/CMakeLists.txt#L11" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/CMakeLists.txt#L11" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/master/Animator/CMakeLists.txt#L11</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>#-----------------------------------------------------------------------------</li>
          <li>set(MODULE_NAME Animator)</li>
          <li></li>
          <li>#-----------------------------------------------------------------------------</li>
          <li>set(MODULE_PYTHON_SCRIPTS</li>
          <li>  ${MODULE_NAME}.py</li>
          <li>  AnimatorLib/TransformAction.py</li>
          <li>  )</li>
          <li></li>
          <li>set(MODULE_PYTHON_RESOURCES</li>
          <li class="selected">  Resources/Icons/${MODULE_NAME}.png</li>
          <li>  )</li>
          <li></li>
          <li>#-----------------------------------------------------------------------------</li>
          <li>slicerMacroBuildScriptedModule(</li>
          <li>  NAME ${MODULE_NAME}</li>
          <li>  SCRIPTS ${MODULE_PYTHON_SCRIPTS}</li>
          <li>  RESOURCES ${MODULE_PYTHON_RESOURCES}</li>
          <li>  WITH_GENERIC_TESTS</li>
          <li>  )</li>
          <li>#-----------------------------------------------------------------------------</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Pointing to this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Resources/Icons/Animator.png">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Resources/Icons/Animator.png" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Resources/Icons/Animator.png" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/master/Animator/Resources/Icons/Animator.png</a></h4>


  This file is binary. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Resources/Icons/Animator.png" target="_blank" rel="noopener">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @jcfr (2023-12-11 20:48 UTC)

<p><a class="mention" href="/u/justin_kirby">@Justin_Kirby</a>  It turns that that the call to the <code>ScriptedLoadableModule</code> base class was missing.</p>
<p>See <a href="https://github.com/QIICR/TCIABrowser/pull/65" class="inline-onebox">BUG: Ensure module icon is set by calling ScriptedLoadableModule construtor by jcfr · Pull Request #65 · QIICR/TCIABrowser · GitHub</a></p>

---

## Post #6 by @jcfr (2023-12-11 21:22 UTC)

<p>And this one is further simplifying by removing functionality provided by the <code>ScriptedLoadableModuleWidget</code> base class.</p>
<p>See <a href="https://github.com/QIICR/TCIABrowser/pull/67" class="inline-onebox">Fix integration with scripted loadable module widget base class by jcfr · Pull Request #67 · QIICR/TCIABrowser · GitHub</a></p>

---

## Post #7 by @Justin_Kirby (2023-12-18 13:57 UTC)

<p>Thanks for your help! It’s working properly in 5.6.1 now.</p>

---
