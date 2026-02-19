---
topic_id: 18217
title: "Annotation Screenshot"
date: 2021-06-18
url: https://discourse.slicer.org/t/18217
---

# Annotation Screenshot

**Topic ID**: 18217
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/annotation-screenshot/18217

---

## Post #1 by @Loc_Tran (2021-06-18 18:26 UTC)

<p>Hello,</p>
<p>I followed the tutorial on <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#screen-capture" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> to write a python program to take a screenshot. However, The resolution of the screenshot is not very good. I notice that on Annotation Screenshot window we can change Scale Factor to obtain a higher resolution image. I was wondering is there any way we can do that programmatically.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2021-06-18 18:34 UTC)

<p>The ScaleFactor on the Annotation Screenshot wasn’t a very reliable method (some renderings didn’t work correctly).  You should have better luck if you make the target widget the size you want the capture to be.  Here’s an example:</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L912-L921" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L912-L921" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L912-L921</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="912" style="counter-reset: li-counter 911 ;">
          <li># set up the threeDWidget at the correct render size</li>
          <li>layoutManager = slicer.app.layoutManager()</li>
          <li>oldLayout = layoutManager.layout</li>
          <li>threeDWidget = layoutManager.threeDWidget(0)</li>
          <li>threeDWidget.setParent(None)</li>
          <li>threeDWidget.show()</li>
          <li>geometry = threeDWidget.geometry</li>
          <li>size =  self.sizes[self.sizeSelector.currentText]</li>
          <li>threeDWidget.threeDController().visible = False</li>
          <li>threeDWidget.setGeometry(geometry.x(), geometry.y(), size["width"], size["height"])</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Loc_Tran (2021-06-18 21:41 UTC)

<p>Thank you for your answer. I will try that.</p>

---
