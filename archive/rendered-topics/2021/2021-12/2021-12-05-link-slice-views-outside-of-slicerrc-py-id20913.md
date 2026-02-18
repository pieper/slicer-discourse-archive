# Link slice views outside of slicerrc.py

**Topic ID**: 20913
**Date**: 2021-12-05
**URL**: https://discourse.slicer.org/t/link-slice-views-outside-of-slicerrc-py/20913

---

## Post #1 by @koeglfryderyk (2021-12-05 07:35 UTC)

<p>I’m writing an extension and I would like that it automatically links the slice views. I know I can add it to .slicerrc.py, and this works, however, I wouldn’t want to ‘ship’ a custom .slicerrc.py together with my extension.</p>
<p>I tried to take the code from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-all-slice-views-linked-by-default" rel="noopener nofollow ugc">Set all slice views linked by default</a>, put it in a function <code>linkViews()</code> in my MyExtension.py and add it to the the <code>__init__()</code> of <code>class MyExtension(ScriptedLoadableModule)</code> similarily to the sample data:<br>
<code>slicer.app.connect("startupCompleted()", linkViews)</code></p>
<p>However, this doesn’t work - it doesn’t throw any error - the code gets executed (if I add a print() it prints to the console) but the views remain unlinked.</p>
<p>Can this be done as part of an extension?</p>

---

## Post #2 by @pieper (2021-12-05 17:19 UTC)

<p>This is probably a timing issue - the <code>startupCompleted</code> signal comes after the windows already exist, while the <code>slicerrc.py</code> is processed during command line processing where the windows must not have been set up yet.</p>
<p>Can you try calling <code>linkViews</code> directly in the <code>__init__()</code>?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/4960b400b3d7135a7b03f28a408358a650fc0a82/Base/QTApp/qSlicerApplicationHelper.txx#L221-L241">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/4960b400b3d7135a7b03f28a408358a650fc0a82/Base/QTApp/qSlicerApplicationHelper.txx#L221-L241" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4960b400b3d7135a7b03f28a408358a650fc0a82/Base/QTApp/qSlicerApplicationHelper.txx#L221-L241" target="_blank" rel="noopener">Slicer/Slicer/blob/4960b400b3d7135a7b03f28a408358a650fc0a82/Base/QTApp/qSlicerApplicationHelper.txx#L221-L241</a></h4>



  <pre class="onebox">    <code class="lang-txx">
      <ol class="start lines" start="221" style="counter-reset: li-counter 220 ;">
          <li>if (window)</li>
          <li>  {</li>
          <li>  QObject::connect(window.data(), SIGNAL(initialWindowShown()), &amp;app, SIGNAL(startupCompleted()));</li>
          <li>  }</li>
          <li>else</li>
          <li>  {</li>
          <li>  QTimer::singleShot(0, &amp;app, SIGNAL(startupCompleted()));</li>
          <li>  }</li>
          <li>
          </li>
<li>if (window)</li>
          <li>  {</li>
          <li>  if (splashScreen)</li>
          <li>    {</li>
          <li>    splashScreen-&gt;close();</li>
          <li>    }</li>
          <li>  window-&gt;setHomeModuleCurrent();</li>
          <li>  window-&gt;show();</li>
          <li>  }</li>
          <li>
          </li>
<li>// Process command line argument after the event loop is started</li>
          <li>QTimer::singleShot(0, &amp;app, SLOT(handleCommandLineArguments()));</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @koeglfryderyk (2021-12-06 16:13 UTC)

<p>Calling <code>linkViews</code> directly in the <code>__init__()</code> of <code>MyExtension(ScriptedLoadableModule)</code> doesn’t work.</p>
<p>However, it works when I call it in the <code>__init__()</code> of <code>MyExtensionWidget(ScriptedLoadableModuleWidget, VTKObservationMixin)</code> or <code>MyExtensionLogic(ScriptedLoadableModuleLogic)</code></p>

---
