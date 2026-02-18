# Reuse of qMRMLTransformSliders to perform rotation transform in custom scriptable module

**Topic ID**: 31598
**Date**: 2023-09-07
**URL**: https://discourse.slicer.org/t/reuse-of-qmrmltransformsliders-to-perform-rotation-transform-in-custom-scriptable-module/31598

---

## Post #1 by @bruce (2023-09-07 03:54 UTC)

<p>In our custom module I’d like to include sliders to perform a rotation transform. <a href="https://discourse.slicer.org/t/how-to-do-custom-rotation-sliders-and-transformation-buttons-with-python/19747/1">This post</a> suggests reusing the slicer.qMRMLTransformSliders widget is the way to go but I can’t seem to access some of the properties from python. The setTypeOfTransform method is not available and If I try to set the TransformType property using Qt syntax I get an attribute error:</p>
<blockquote>
<p>t.TransformType = slicer.qMRMLTransformSliders.ROTATION<br>
Traceback (most recent call last):<br>
AttributeError: Enum ‘TransformType’ can not be overwritten on qMRMLTransformSliders object</p>
</blockquote>
<p>Nor can I access the minMaxVisible property to configure the widget manually.<br>
Maybe I’m going about this the wrong way? Any help would be appreciated.<br>
Thanks</p>

---

## Post #2 by @pieper (2023-09-07 11:45 UTC)

<p>Looks like you need to set <code>TypeOfTransform</code> to one of the <code>TransformType</code> values.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/4540594f5ff293cb387fd252e24e32be13e377c8/Libs/MRML/Widgets/qMRMLTransformSliders.h#L45-L46">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/4540594f5ff293cb387fd252e24e32be13e377c8/Libs/MRML/Widgets/qMRMLTransformSliders.h#L45-L46" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4540594f5ff293cb387fd252e24e32be13e377c8/Libs/MRML/Widgets/qMRMLTransformSliders.h#L45-L46" target="_blank" rel="noopener">Slicer/Slicer/blob/4540594f5ff293cb387fd252e24e32be13e377c8/Libs/MRML/Widgets/qMRMLTransformSliders.h#L45-L46</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="45" style="counter-reset: li-counter 44 ;">
          <li>Q_PROPERTY(TransformType TypeOfTransform READ typeOfTransform WRITE setTypeOfTransform)</li>
          <li>Q_ENUMS(TransformType)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><code>minMaxVisible</code> is available to me:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; t = slicer.qMRMLTransformSliders()
&gt;&gt;&gt; t.minMaxVisible
True
</code></pre>

---
