# How to use a python package in an extension?

**Topic ID**: 12736
**Date**: 2020-07-26
**URL**: https://discourse.slicer.org/t/how-to-use-a-python-package-in-an-extension/12736

---

## Post #1 by @nathanhillyer (2020-07-26 22:53 UTC)

<p>How do I import my python pip package into an extension, for example:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L9" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L9" target="_blank" rel="nofollow noopener">Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L9</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
<li>from __future__ import print_function</li>
<li>from itertools import chain</li>
<li>import json</li>
<li>import os</li>
<li>import vtk, qt, ctk, slicer, logging</li>
<li>import numpy</li>
<li>from slicer.ScriptedLoadableModule import *</li>
<li>import SimpleITK as sitk</li>
<li class="selected">from radiomics import getFeatureClasses</li>
<li>import sitkUtils</li>
<li>import traceback</li>
<li>
</li><li>
</li><li>#</li>
<li># SlicerRadiomics</li>
<li>#</li>
<li>
</li><li>class SlicerRadiomics(ScriptedLoadableModule):</li>
<li>  """Uses ScriptedLoadableModule base class, available at:</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Notice this extension is able to import a method from the radiomics library. How do I accomplish the same with my pip module on PyPi?</p>

---

## Post #2 by @jamesobutler (2020-07-26 23:18 UTC)

<p>I think these two posts will help you out! Which python package on PyPI are you looking to use in your extension?</p>
<p>Simplest (Really only recommended for packaged on PyPI that have wheels available):</p><aside class="quote" data-post="2" data-topic="10110">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/markasselin/48/5916_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/install-python-library-with-extension/10110/2">Install python library with extension</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi Paolo, 
You can use the following structure to do this right in the module. The first time the module is loaded the library will be automatically installed, and every successive time the import in the try block will succeed and the catch will not be executed. 
try:
    import library_name
except:
    slicer.util.pip_install('library_name')
    import library_name

Of course you can use other forms of the Python import lines as well, like 
from library_name import module_name
  </blockquote>
</aside>

<p>More involved, but gets the external python package at time of building the extension and then the files are packaged together when building the extension package file:</p><aside class="quote quote-modified" data-post="8" data-topic="10110">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/install-python-library-with-extension/10110/8">Install python library with extension</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Ciao <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a>, if your extension is in the extension manager, you can actually do it directly in the cmake (so they will be packed at compilation time on the kitware factory machines): 


add  python requirements in the superbuild: 
<a href="https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild.cmake#L28" rel="noopener nofollow ugc">https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild.cmake#L28</a> 
<a href="https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/slicerastro-requirements.txt" rel="noopener nofollow ugc">https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/slicerastro-requirements.txt</a> 
<a href="https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/External_python-slicerastro-requirements.cmake" rel="noopener nofollow ugc">https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/External_python-slicerastro-requirements.…</a>
  </blockquote>
</aside>


---

## Post #3 by @nathanhillyer (2020-07-27 23:48 UTC)

<p>Thanks James, the first method worked! I am using the collageradiomics python package.</p>

---
