# Hide mainWindow title bar

**Topic ID**: 35666
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/hide-mainwindow-title-bar/35666

---

## Post #1 by @park (2024-04-23 05:24 UTC)

<p>Hi all.</p>
<p>I would like to hide the title bar of the mainWindow (as shown in the figure below). Thus, I have tried the code below,  But the mainWindow itself closed.<br>
Could I get solution about this ?</p>
<pre><code class="lang-auto">flags = qt.Qt.FramelessWindowHint

main = slicer.util.mainWindow()
main.setWindowFlags(flags)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/753cd208187d66b69194b66628855a0dcc5b1cfc.png" alt="titlebar" data-base62-sha1="gJ8aCbTpngbW6zwDC1AidpzEP4E" width="325" height="198"></p>

---

## Post #2 by @pieper (2024-04-23 12:18 UTC)

<p>You might have to set the flag before the window is created.</p>
<p>Since this is basically just Qt, you could experiment with Qt examples and then port what you learn to the Slicer code.</p>

---

## Post #3 by @lassoan (2024-04-23 13:54 UTC)

<p>You can find the solution on the Qt forum:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://forum.qt.io/topic/60642/framelesswindowhint-fails-at-runtime-on-mainwindow/5">
  <header class="source">
      <img src="https://forum.qt.io/assets/uploads/system/favicon.ico?v=ifu3inlhqv8" class="site-icon" width="" height="">

      <a href="https://forum.qt.io/topic/60642/framelesswindowhint-fails-at-runtime-on-mainwindow/5" target="_blank" rel="noopener" title="06:01PM - 13 November 2015">Qt Forum – 13 Nov 15</a>
  </header>

  <article class="onebox-body">
    <img width="175" height="175" src="https://ddgobkiprc33d.cloudfront.net/bfdb2533-84e9-45a1-956a-106722433d3f.png" class="thumbnail onebox-avatar">

<h3><a href="https://forum.qt.io/topic/60642/framelesswindowhint-fails-at-runtime-on-mainwindow/5" target="_blank" rel="noopener">FramelessWindowHint fails at runtime on MainWindow</a></h3>

  <p>When I execute setWindowFlags(Qt::FramelessWindowHint) before the main window is shown this works, but if I try to execute after the main window is shown the window disappears from the screen and the task manager but is still running.  I have to kill...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto">main = slicer.util.mainWindow()
main.hide()
main.setWindowFlags(qt.Qt.FramelessWindowHint)
main.show()
</code></pre>

---

## Post #4 by @park (2024-04-23 15:58 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> .<br>
This is exactly what I wanted !</p>

---
