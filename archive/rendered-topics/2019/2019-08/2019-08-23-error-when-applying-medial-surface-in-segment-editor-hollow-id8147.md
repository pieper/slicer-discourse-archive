# Error when applying Medial surface in Segment Editor hollow effect (with possible fix)

**Topic ID**: 8147
**Date**: 2019-08-23
**URL**: https://discourse.slicer.org/t/error-when-applying-medial-surface-in-segment-editor-hollow-effect-with-possible-fix/8147

---

## Post #1 by @hherhold (2019-08-23 15:13 UTC)

<p>I get an error when applying medial surface in hollow effect. The offending line is in SegmentEditorHollowEffect.py, line 157:</p>
<pre><code>  kernelSizePixel = [int(kernelSizePixel[0],2), int(kernelSizePixel[1],2), int(kernelSizePixel[2],2)]
</code></pre>
<p>The int(…,2) specifies base 2, which doesn’t make sense.</p>
<p>I think this should read:</p>
<pre><code>  kernelSizePixel = [int(kernelSizePixel[0]/2), int(kernelSizePixel[1]/2), int(kernelSizePixel[2]/2)]
</code></pre>
<p>I’m happy to submit a pull request if this looks correct.</p>
<p>Thanks,</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2019-08-23 15:20 UTC)

<p>Yes, please send a pull request. The change has been made by the automatic Python2-&gt;Python3 converter script.</p>

---

## Post #3 by @hherhold (2019-08-23 15:39 UTC)

<p>Done. Thanks!</p>
<p>-Hollister</p>

---

## Post #4 by @lassoan (2019-08-23 15:41 UTC)

<p>I don’t see a pull request here (checked it here <a href="https://github.com/Slicer/Slicer/pulls" rel="nofollow noopener">https://github.com/Slicer/Slicer/pulls</a>).</p>

---
