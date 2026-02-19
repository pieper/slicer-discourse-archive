---
topic_id: 17677
title: "Scripted Loadable Modules Accessing Eachothers Logic"
date: 2021-05-18
url: https://discourse.slicer.org/t/17677
---

# Scripted Loadable Modules Accessing Eachother's Logic

**Topic ID**: 17677
**Date**: 2021-05-18
**URL**: https://discourse.slicer.org/t/scripted-loadable-modules-accessing-eachothers-logic/17677

---

## Post #1 by @nathanbmnt (2021-05-18 14:42 UTC)

<p>Hello,<br>
I have multiple scripted loadable modules (python) where I need modules to access each other’s logic.</p>
<p>In the setup() method of Module 1’s ScriptedLoadableModuleWidget there is the line<br>
<code>self.logic = Module1Logic()</code></p>
<p>Now in my Module 2, if I want to access Module 1’s logic, do I import the class and instantiate it every time I want to use the logic? Like:</p>
<blockquote>
<p>from Module1 import Module1Logic<br>
logic = Module1Logic()<br>
logic.myMethod()</p>
</blockquote>
<p>Or do I access the singleton logic object stored in Module1Widget like:</p>
<blockquote>
<p>logic = slicer.modules.module1.widgetRepresentation().self().logic<br>
logic.myMethod()</p>
</blockquote>
<p>When accessing logic from a C++ module a singleton is accessed every time.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d1228b870e677c83ccce4e61635f8d5e198d79f.png" alt="image" data-base62-sha1="49aKDGn4bejYf9eKtherXmkA6J1" width="479" height="66"></p>
<p>Furthermore, if I have a ScriptedLoadableModule with <em>no</em> widget class, how should I access its logic?</p>

---

## Post #2 by @lassoan (2021-05-19 03:53 UTC)

<p>These questions and other essential techniques are explained in <a href="https://github.com/PerkLab/PerkLabBootcamp/raw/master/Doc/day3_2_SlicerProgramming.pptx">PerkLab bootcamp Slicer programming tutorial</a>.</p>

---

## Post #3 by @nathanbmnt (2021-05-19 13:45 UTC)

<p>I’ve read through the powerpoint and it says a logic reference is myWidget.logic, but the powerpoint doesn’t specify if this is just how the myWidget class accesses logic, or if that is how other modules should access the logic as well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9425a5115a8dabff7c71428984ba875ce7c4259.png" data-download-href="/uploads/short-url/uZXLOTDXNeEB6dXv8AjID2iDwXD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9425a5115a8dabff7c71428984ba875ce7c4259.png" alt="image" data-base62-sha1="uZXLOTDXNeEB6dXv8AjID2iDwXD" width="678" height="500" data-dominant-color="EFEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1084×799 42.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This slide says logic <em>may</em> be instantiated many times, does this mean it should be instantiated in other modules?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/277bd64529af3b6818614856e3e2e12b2b7515e7.png" data-download-href="/uploads/short-url/5DhWkKiiDIBmlIGkVEwjm7jIy1N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/277bd64529af3b6818614856e3e2e12b2b7515e7.png" alt="image" data-base62-sha1="5DhWkKiiDIBmlIGkVEwjm7jIy1N" width="690" height="319" data-dominant-color="D6D6D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1159×536 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-05-19 14:55 UTC)

<aside class="quote no-group" data-username="nathanbmnt" data-post="3" data-topic="17677">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/a9adbd/48.png" class="avatar"> nathanbmnt:</div>
<blockquote>
<p>the powerpoint doesn’t specify if this is just how the myWidget class accesses logic</p>
</blockquote>
</aside>
<p>This is included in the standard scripted module template (created by Extension Wizard):</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/7b60eed09c2cef6358e2f67935623e8a90b28cb1/Utilities/Templates/Modules/Scripted/TemplateKey.py#L122-L124">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/7b60eed09c2cef6358e2f67935623e8a90b28cb1/Utilities/Templates/Modules/Scripted/TemplateKey.py#L122-L124" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/7b60eed09c2cef6358e2f67935623e8a90b28cb1/Utilities/Templates/Modules/Scripted/TemplateKey.py#L122-L124" target="_blank" rel="noopener">Slicer/Slicer/blob/7b60eed09c2cef6358e2f67935623e8a90b28cb1/Utilities/Templates/Modules/Scripted/TemplateKey.py#L122-L124</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="122" style="counter-reset: li-counter 121 ;">
          <li># Create logic class. Logic implements all computations that should be possible to run</li>
          <li># in batch mode, without a graphical user interface.</li>
          <li>self.logic = TemplateKeyLogic()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="nathanbmnt" data-post="3" data-topic="17677">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/a9adbd/48.png" class="avatar"> nathanbmnt:</div>
<blockquote>
<p>if that is how other modules should access the logic as well</p>
</blockquote>
</aside>
<p>For loadable and CLI modules the logic is instantiated at application startup. You can access them as shown in the slide you referenced above. For scripted modules, optimal choice depends on the module. If the the scripted module logic is active (e.g., continuously observe the scene and act on scene or node changes automatically) then you need to access the existing module logic (typically via the module object). However, in most cases the module logic is just passive (it is just a collection of functions, does not do any observations) and in these cases you can instantiate another logic class and use that, as it is done for example here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/moselhy/SlicerSequenceRegistration/blob/a6b0409b8e25a4f60eb4a459fea39f53273f1f92/SequenceRegistration/SequenceRegistration.py#L490-L491">
  <header class="source">

      <a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/a6b0409b8e25a4f60eb4a459fea39f53273f1f92/SequenceRegistration/SequenceRegistration.py#L490-L491" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/a6b0409b8e25a4f60eb4a459fea39f53273f1f92/SequenceRegistration/SequenceRegistration.py#L490-L491" target="_blank" rel="noopener">moselhy/SlicerSequenceRegistration/blob/a6b0409b8e25a4f60eb4a459fea39f53273f1f92/SequenceRegistration/SequenceRegistration.py#L490-L491</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="490" style="counter-reset: li-counter 489 ;">
          <li>import Elastix
</li>
          <li>self.elastixLogic = Elastix.ElastixLogic()
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
