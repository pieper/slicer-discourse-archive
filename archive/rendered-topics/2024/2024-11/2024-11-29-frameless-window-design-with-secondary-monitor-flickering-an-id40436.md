# Frameless Window Design with Secondary Monitor Flickering and Performance Degradation

**Topic ID**: 40436
**Date**: 2024-11-29
**URL**: https://discourse.slicer.org/t/frameless-window-design-with-secondary-monitor-flickering-and-performance-degradation/40436

---

## Post #1 by @park (2024-11-29 09:03 UTC)

<p>Hi all!</p>
<p>I am currently working on implementing a frameless window design for my application and rebuilding the functionalities provided by the native frame. The primary reasons for this approach are:</p>
<ul>
<li>To ensure consistent window design across operating systems.</li>
<li>To maximize the available size of the MainWindow.</li>
</ul>
<p>Below is the code snippet I am using for this purpose:</p>
<pre><code class="lang-auto">mainWindow = slicer.util.mainWindow()
flags = mainWindow.windowFlags()
newFlags = (flags | qt.Qt.FramelessWindowHint | qt.Qt.WindowStaysOnTopHint)
mainWindow.setWindowFlags(newFlags)
mainWindow.hide()
mainWindow.show()
</code></pre>
<p>This implementation works as expected on the primary monitor. However, when the application is moved to a secondary monitor, I encounter two issues:</p>
<ul>
<li>Noticeable flickering of the window.</li>
<li>Significant performance degradation.</li>
</ul>
<p>I would appreciate any insights into the potential cause of these issues or suggestions for resolving them.</p>
<p>Thank you in advance for your help!</p>

---
