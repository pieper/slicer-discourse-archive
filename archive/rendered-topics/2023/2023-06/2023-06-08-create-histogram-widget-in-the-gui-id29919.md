---
topic_id: 29919
title: "Create Histogram Widget In The Gui"
date: 2023-06-08
url: https://discourse.slicer.org/t/29919
---

# Create histogram widget in the GUI

**Topic ID**: 29919
**Date**: 2023-06-08
**URL**: https://discourse.slicer.org/t/create-histogram-widget-in-the-gui/29919

---

## Post #1 by @tux (2023-06-08 13:54 UTC)

<p>Os : Ubuntu 20.04.6<br>
Slicer version : 5.2.2</p>
<p>Hello !<br>
I am currently searching how to create an histogram but as a widget inside my module GUI like the one in the volume module :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5d57d5d2547ec64c472ede0ccd15592c91686a0.png" data-download-href="/uploads/short-url/nF2binU77SkKpEmHqko7um87q6Y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5d57d5d2547ec64c472ede0ccd15592c91686a0_2_690x176.png" alt="image" data-base62-sha1="nF2binU77SkKpEmHqko7um87q6Y" width="690" height="176" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5d57d5d2547ec64c472ede0ccd15592c91686a0_2_690x176.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5d57d5d2547ec64c472ede0ccd15592c91686a0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5d57d5d2547ec64c472ede0ccd15592c91686a0.png 2x" data-dominant-color="C0C7CC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">791×202 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I already have one in the “visualisation page” (i don’t know how is this called) like this :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9bac5a65c5a2590071dcba0b9e6c15832373db4.png" data-download-href="/uploads/short-url/qv2ul34Fdri1W8d2YJHZqAjVdeQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9bac5a65c5a2590071dcba0b9e6c15832373db4_2_690x372.png" alt="image" data-base62-sha1="qv2ul34Fdri1W8d2YJHZqAjVdeQ" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9bac5a65c5a2590071dcba0b9e6c15832373db4_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9bac5a65c5a2590071dcba0b9e6c15832373db4_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9bac5a65c5a2590071dcba0b9e6c15832373db4.png 2x" data-dominant-color="5E5E5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1070×577 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>so i already have the code to create the histogram with numpy.<br>
I tried to look at the code of the Volume module but i don’t know anything about c++ so i couldn’t find what i want.<br>
Can someone hellp me to know if it’s at least possible to create this widget with python ? And if so, how could i do ?<br>
Thank you !</p>

---

## Post #2 by @tux (2023-06-09 09:32 UTC)

<p>hi again !<br>
I found the widget that is used in the volume module (the <code>ctkTransferFunctionView</code>) and i understood that i need to draw inside it with QPainter but i can’t find how to draw.<br>
I think i almost got it with <code>widget.paintEvent()</code> and a event i created myself, but here is the error i got :</p>
<pre><code class="lang-auto">[Qt] QWidget::paintEngine: Should no longer be called
[Qt] QPainter::begin: Paint device returned engine == 0, type: 1
[Qt] QPainter::setRenderHint: Painter must be active to set rendering hints
[Qt] QPainter::setRenderHint: Painter must be active to set rendering hints
[Qt] QPainter::setWorldTransform: Painter not active
[Qt] QPainter::worldTransform: Painter not active
[Qt] QPainter::save: Painter not active
[Qt] QPainter::restore: Unbalanced save/restore
[Qt] QPainter::setWorldTransform: Painter not active
[Qt] QPainter::end: Painter not active, aborted
</code></pre>
<p>And i can’t set the painter active no matter what i do</p>

---

## Post #3 by @pieper (2023-06-09 13:37 UTC)

<p>It looks like you are on the right track.  The CTK widget could no doubt be improved to make it more flexible.  It would be good if you could look at how it’s implemented and propose changes to make it work better for what you have in mind.</p>

---

## Post #4 by @tux (2023-06-09 14:12 UTC)

<p>I can’t find the source code of the function <code>paintEvent()</code> but from what i understand, i think the problem come from an “recent” update where now you need to use the <code>beginNativePainting()</code> and <code>endNativePainting()</code> instead of the old ones <code>begin()</code> and <code>end()</code>.<br>
But as already said, i don’t know c++ and the source code is probably in this language since i tried a <code>grep -ri 'paintEvent'</code> in the <code>/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2</code> folder to see where the source code could be, and every file returned were <code>*.so</code> .</p>

---

## Post #5 by @pieper (2023-06-09 14:21 UTC)

<p>Yes, the Qt/CTK code is C++ so if you want to reuse or extend then you will need to learn C++ (if your goal is to develop code it’s good to know C++ so you understand how things work and what can and can’t be done in which languages)</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/commontk/CTK/tree/master/Libs/Widgets">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/commontk/CTK/tree/master/Libs/Widgets" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/commontk/CTK/tree/master/Libs/Widgets" target="_blank" rel="noopener">CTK/Libs/Widgets at master · commontk/CTK</a></h3>

  <p><a href="https://github.com/commontk/CTK/tree/master/Libs/Widgets" target="_blank" rel="noopener">master/Libs/Widgets</a></p>

  <p><span class="label1">A set of common support code for medical imaging, surgical navigation, and related purposes.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you want to avoid all that, you could just implement a fresh widget in python that does exactly what you need.  You can still use the Qt paint methods.  Something like this;</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1082-L1107">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1082-L1107" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1082-L1107" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1082-L1107</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1082" style="counter-reset: li-counter 1081 ;">
          <li>imageWidth = 128
</li>
          <li>imageHeight = 32
</li>
          <li>timeImage = qt.QImage(imageWidth, imageHeight, qt.QImage().Format_ARGB32)
</li>
          <li>timeImage.fill(0)
</li>
          <li>
</li>
          <li># a painter to use for various jobs
</li>
          <li>painter = qt.QPainter()
</li>
          <li>
</li>
          <li># draw a border around the pixmap
</li>
          <li>painter.begin(timeImage)
</li>
          <li>pen = qt.QPen()
</li>
          <li>color = qt.QColor(color)
</li>
          <li>color.setAlphaF(0.8)
</li>
          <li>pen.setColor(color)
</li>
          <li>pen.setWidth(5)
</li>
          <li>pen.setStyle(3)  # dotted line (Qt::DotLine)
</li>
          <li>painter.setPen(pen)
</li>
          <li>rect = qt.QRect(1, 1, imageWidth - 2, imageHeight - 2)
</li>
          <li>painter.drawRect(rect)
</li>
          <li>color = qt.QColor("#333")
</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1082-L1107" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
