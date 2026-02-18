# Slice viewer reset view and set intersection

**Topic ID**: 2436
**Date**: 2018-03-27
**URL**: https://discourse.slicer.org/t/slice-viewer-reset-view-and-set-intersection/2436

---

## Post #1 by @MancaZerovnik (2018-03-27 12:31 UTC)

<p>Hello,</p>
<p>I have two question regarding slice viewer (red, green, yellow):</p>
<ol>
<li>Is it possible to reset change in intensity which is made by mouse dragging to default values?</li>
<li>Is it possible to set slice intersections to clicked position?</li>
</ol>

---

## Post #2 by @lassoan (2018-03-27 15:04 UTC)

<p>Reset image intensity display window/level. Go to volumes module, below the color presets, change <code>Manual W/L</code> to <code>Auto W/L</code>. From Python script:</p>
<pre><code>vol=getNode('MRHead')
vol.GetDisplayNode().SetAutoWindowLevel(True)
</code></pre>
<p>To prevent accidentally changing W/L, you can click the “lock” button next to Window/Level label.</p>
<blockquote>
<p>Is it possible to set slice intersections to clicked position?</p>
</blockquote>
<p>Hold down <code>Shift</code> key while moving the mouse. No need to press any mouse button. Works in both slice and 3D views.</p>

---
