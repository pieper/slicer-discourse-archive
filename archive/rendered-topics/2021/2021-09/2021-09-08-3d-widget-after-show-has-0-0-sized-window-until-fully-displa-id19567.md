---
topic_id: 19567
title: "3D Widget After Show Has 0 0 Sized Window Until Fully Displa"
date: 2021-09-08
url: https://discourse.slicer.org/t/19567
---

# 3D Widget after show() has (0,0)-sized window until fully displayed

**Topic ID**: 19567
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/3d-widget-after-show-has-0-0-sized-window-until-fully-displayed/19567

---

## Post #1 by @atracsys-sbt (2021-09-08 12:34 UTC)

<p>Hi,<br>
In order to make a custom camera reset in a 3D widget (qMRMLThreeDWidget), I need to access the vtkRenderWindow size after the call for the widget to show().<br>
However, I noticed that the window size was (0,0) if performed shortly after the show(), likely due to the window not being fully rendered yet.<br>
I tried and failed with the following attempts:</p>
<pre><code class="lang-auto">widget.show()
widget.threeDView().renderWindow().WaitForCompletion()
size = widget.threeDView().renderWindow().GetSize() # sill is (0,0)
</code></pre>
<p>and</p>
<pre><code class="lang-auto">widget.show()
while not widget.visible:
  pass
size = widget.threeDView().renderWindow().GetSize() # sill is (0,0)
</code></pre>
<p>Is there a way to get the size only once the 3D widget is done rendering ? Perhaps with through a connect to a signal or an observer for an event ?<br>
Thanks for any help</p>

---

## Post #2 by @pieper (2021-09-08 12:37 UTC)

<p>You could try either <code>slicer.app.processEvents()</code> or use a <code>QTimer.singleShot</code> so the event loop has had a chance to run.</p>

---

## Post #3 by @atracsys-sbt (2021-09-08 12:43 UTC)

<p><code>slicer.app.processEvents()</code> worked, thanks !</p>

---
