---
topic_id: 40341
title: "Copy Images From An Icon Near Reset Images"
date: 2024-11-23
url: https://discourse.slicer.org/t/40341
---

# Copy images from an icon near reset images

**Topic ID**: 40341
**Date**: 2024-11-23
**URL**: https://discourse.slicer.org/t/copy-images-from-an-icon-near-reset-images/40341

---

## Post #1 by @mohammed_alshakhas (2024-11-23 10:23 UTC)

<p>would be great if i can copy an image from an icon instead of right click and navigation to copy .<br>
i do lots of copying for case studies .<br>
if for example a copy image icon is put near the slice bar where the reset view and maximize view it would be more efficient than right click menu</p>

---

## Post #2 by @pieper (2024-11-23 13:49 UTC)

<p>I’m not sure that’s a very common operation for a lot of people, but if it’s common for you, then one option is to add a keyboard shortcut in your .slicerrc.py.</p>

---

## Post #3 by @mohammed_alshakhas (2024-11-23 14:11 UTC)

<p>i guess you are right , is the resource to help doing it ?</p>

---

## Post #4 by @pieper (2024-11-23 14:19 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts</a></p>
<p>And then this code would need to be converted to Python:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/50612e7ca2e5a26858029a93f23005d7e1fc082b/Modules/Loadable/SubjectHierarchy/Widgets/qSlicerSubjectHierarchyViewContextMenuPlugin.cxx#L493-L503">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/50612e7ca2e5a26858029a93f23005d7e1fc082b/Modules/Loadable/SubjectHierarchy/Widgets/qSlicerSubjectHierarchyViewContextMenuPlugin.cxx#L493-L503" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/50612e7ca2e5a26858029a93f23005d7e1fc082b/Modules/Loadable/SubjectHierarchy/Widgets/qSlicerSubjectHierarchyViewContextMenuPlugin.cxx#L493-L503" target="_blank" rel="noopener">Slicer/Slicer/blob/50612e7ca2e5a26858029a93f23005d7e1fc082b/Modules/Loadable/SubjectHierarchy/Widgets/qSlicerSubjectHierarchyViewContextMenuPlugin.cxx#L493-L503</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="493" style="counter-reset: li-counter 492 ;">
          <li>// Grab image</li>
          <li>QImage screenshot = ctk::grabVTKWidget(widget);</li>
          <li></li>
          <li>// Copy to clipboard</li>
          <li>QClipboard* clipboard = QApplication::clipboard();</li>
          <li>if (!clipboard)</li>
          <li>{</li>
          <li>  qWarning() &lt;&lt; Q_FUNC_INFO &lt;&lt; " failed: cannot access the clipboard";</li>
          <li>  return;</li>
          <li>}</li>
          <li>clipboard-&gt;setImage(screenshot);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>As programming projects go this would be among the simplest.</p>

---

## Post #5 by @mohammed_alshakhas (2024-11-24 04:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/pieper">@pieper</a></p>
<p>in my opinion there is a real estate ( space ) that can be used for so many things to make usage faster and more efficient.</p>
<p>for examplae on right and left side of 3d view we can placed as custom /default transparent icon  on side of view .</p>
<p>for example it would way much  more efficient than going to volume module and toggle on and off.</p>
<p>saving and a specific view would be much better if choosen from an icon on the same view rather than doing it on save then selecting which one to save .</p>

---

## Post #6 by @lassoan (2024-11-24 22:04 UTC)

<p>There is space but we often get criticism for having too many buttons. If many other people voted on this feature then we would consider adding it though.</p>
<p>In the meantime, you can add this button yourself by writing a few lines of Python script to your .slicerrc.py.</p>

---

## Post #7 by @mohammed_alshakhas (2024-11-25 05:46 UTC)

<p>I think you also should consider optional transparent button on side .</p>

---
