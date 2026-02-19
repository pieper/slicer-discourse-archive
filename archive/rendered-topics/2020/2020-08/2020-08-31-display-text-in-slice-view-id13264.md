---
topic_id: 13264
title: "Display Text In Slice View"
date: 2020-08-31
url: https://discourse.slicer.org/t/13264
---

# Display Text in Slice view

**Topic ID**: 13264
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/display-text-in-slice-view/13264

---

## Post #1 by @DavidCai1246 (2020-08-31 19:42 UTC)

<p>I’m would like to display unique text in the slice view for each slice.</p>
<p>I’m currently trying to use the python script to display text in slice view:</p>
<pre><code>view=slicer.app.layoutManager().threeDWidget(0).threeDView()
# Set text to "Something"
view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,"Something")
# Set color to red
view.cornerAnnotation().GetTextProperty().SetColor(1,0,0)
# Update the view
view.forceRender()
</code></pre>
<p>However nothing shows up, do I have to enable something?</p>
<p>Another question I have is would this script display the same text for all the slices? So if I scroll through the slices it would be the same text? How can I display unique text for each slice?</p>

---

## Post #2 by @lassoan (2020-08-31 20:05 UTC)

<p>The code above works well for me - displays text in 3D view as expected.</p>
<p>To display text in slice views, replace the first line by this line:</p>
<pre><code>view = slicer.app.layoutManager().sliceWidget("Red").sliceView()
</code></pre>
<p>You may consider hiding slice view annotations, to prevent them from overwriting the text you place there. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Hide_slice_view_annotations_.28DataProbe.29">example</a>.</p>

---

## Post #3 by @DavidCai1246 (2020-08-31 20:18 UTC)

<p>thank you very much! it displays for me now</p>

---

## Post #4 by @DavidCai1246 (2020-08-31 21:00 UTC)

<p>Sorry one more question I have is, can I change the font size of the text? like make it bigger?</p>

---

## Post #5 by @lassoan (2020-08-31 21:17 UTC)

<p>Yes, sure, see how the text is scaled by DataProbe:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/77d4268cd3659d452d8e5a7748cd20f456771b48/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L451-L453" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/77d4268cd3659d452d8e5a7748cd20f456771b48/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L451-L453" target="_blank" rel="noopener">Slicer/Slicer/blob/77d4268cd3659d452d8e5a7748cd20f456771b48/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L451-L453</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="451" style="counter-reset: li-counter 450 ;">
<li>cornerAnnotation.SetMaximumFontSize(self.fontSize)</li>
<li>cornerAnnotation.SetMinimumFontSize(self.fontSize)</li>
<li>cornerAnnotation.SetNonlinearFontScaleFactor(1)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @DavidCai1246 (2020-08-31 21:17 UTC)

<p>thank you very much!!</p>

---
