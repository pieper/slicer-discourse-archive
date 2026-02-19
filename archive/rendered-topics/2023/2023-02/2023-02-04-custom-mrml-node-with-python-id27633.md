---
topic_id: 27633
title: "Custom Mrml Node With Python"
date: 2023-02-04
url: https://discourse.slicer.org/t/27633
---

# Custom MRML Node with Python

**Topic ID**: 27633
**Date**: 2023-02-04
**URL**: https://discourse.slicer.org/t/custom-mrml-node-with-python/27633

---

## Post #1 by @kleingeo (2023-02-04 16:57 UTC)

<p>Is there a way to define a custom MRML node that can be used with a module developed with the python backend?</p>

---

## Post #2 by @cpinter (2023-02-09 10:05 UTC)

<p>As far as I know it is not possible to subclass C++ classes in Python. What we do in cases like yours is that we use <code>vtkMRMLScriptedModuleNode</code>, a generic class for Python modules, set the module name accordingly, and use its attributes to store data (instead of properties you’d define in a C++ class).</p>
<p>Also it may help looking into this:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/main/Base/Python/slicer/parameterNodeWrapper">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/main/Base/Python/slicer/parameterNodeWrapper" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/main/Base/Python/slicer/parameterNodeWrapper" target="_blank" rel="noopener">Slicer/Base/Python/slicer/parameterNodeWrapper at main · Slicer/Slicer</a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/main/Base/Python/slicer/parameterNodeWrapper" target="_blank" rel="noopener">main/Base/Python/slicer/parameterNodeWrapper</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @kleingeo (2023-02-09 16:48 UTC)

<p>I am using the <code>vtkMRMLScriptedModuleNode</code> to build a module. I am loading/creating multiple <code>vtkMRMLMarkupsFiducialNodes</code>, but I also need to track other information per node. The current implementation of <code>parameterNodeWrapper</code> does not integrate well with the current <code>vtkMRMLNodes</code>.</p>
<p>Another option is to connect the different <code>qt</code> objects that track the information directly to the <code>vtkMRMLMarkupsFiducialNodes</code>, which seems cumbersome if possible.</p>

---

## Post #4 by @cpinter (2023-02-10 09:56 UTC)

<p>It would help if you described your use case in mode detail.</p>
<aside class="quote no-group" data-username="kleingeo" data-post="3" data-topic="27633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kleingeo/48/6772_2.png" class="avatar"> kleingeo:</div>
<blockquote>
<p>also need to track other information per node</p>
</blockquote>
</aside>
<p>You can add attributes in the nodes themselves.</p>

---

## Post #5 by @kleingeo (2023-02-13 16:07 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="27633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>It would help if you described your use case in mode detail.</p>
</blockquote>
</aside>
<p>I have a python module where many <code>vtkMRMLMarkupsFiducialNodes</code> are loaded and created and features need to be tracked. What I would like to do is define a new class for the <code>vtkMRMLMarkupsFiducialNodes</code> where the features I care about are defined as parameters of the object. The idea is for a user to use radio buttons to change which feature from a few options, so I would also like to have this class have better integration with the radio buttons themselves so when different <code>vtkMRMLMarkupsFiducialNodes</code> are chosen the radio button selection moves with them.</p>

---

## Post #6 by @cpinter (2023-02-13 18:13 UTC)

<p>Based on this vague description it still seems a good idea to use the Attributes of the nodes you need to store properties for.</p>
<p>If you insist you can subclass nodes in C++.</p>

---
