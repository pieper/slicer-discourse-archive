# Inverted slice view scrolling direction

**Topic ID**: 16977
**Date**: 2021-04-07
**URL**: https://discourse.slicer.org/t/inverted-slice-view-scrolling-direction/16977

---

## Post #1 by @chir.set (2021-04-07 08:30 UTC)

<p>Hi,</p>
<p>Using 4.13.0-2021-04-02 r29808 / 49642b0 / VTK8 on Linux.</p>
<p>Scrolling a slice view occurs in the opposite direction since this build.</p>
<p>Usually, the mouse wheel would scroll a view I&gt;S when scrolling the wheel up, same for keyboard arrow key. It’s just reversed now.</p>
<p>Is it a new feature or does it need a fix ?</p>
<p>Regards.</p>

---

## Post #2 by @jamesobutler (2021-04-07 12:45 UTC)

<p>Specifically between which two commits do you find scrolling behavior to have been changed?</p>

---

## Post #3 by @chir.set (2021-04-07 12:55 UTC)

<p>4.13.0-2021-03-20 r29789 / 233d7ac / VTK8 scrolls normally.<br>
4.13.0-2021-04-02 r29808 / 49642b0 / VTK8 scrolls inversely.</p>

---

## Post #4 by @chir.set (2021-04-07 12:58 UTC)

<p>Could it be related to the addition of ‘radiology’ and ‘neurology’ viewpoint ?</p>
<p>patient right is screen left<br>
patient right is screen right</p>
<p>combobox in settings.</p>

---

## Post #5 by @jamesobutler (2021-04-07 14:25 UTC)

<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a> who had been discussing the view orientation changes in <a href="https://github.com/Slicer/Slicer/pull/5536" class="inline-onebox" rel="noopener nofollow ugc">ENH: Make default slice view orientations configurable by lassoan · Pull Request #5536 · Slicer/Slicer · GitHub</a>.</p>
<p>Neither of the two new view orientation options (patient right is screen left (default)/patient right is screen right) match the scrolling behavior of the previous unconfigurable Slicer behavior.</p>

---

## Post #6 by @pieper (2021-04-07 15:00 UTC)

<p>Thanks for the report and tracking down the likely issue.  Let’s see what <a class="mention" href="/u/lassoan">@lassoan</a> thinks and we can make the appropriate fix.  I would vote for restoring the old behavior by default.</p>

---

## Post #7 by @lassoan (2021-04-07 15:43 UTC)

<p>The old default SliceToRAS coordinate systems were left-handed for no particular reason. We use right-handed coordinate system everywhere else. Using left-handed slice coordinate system turns models inside out and can introduce other small inconsistencies when we transform objects to the slice plane, so I would consider it as an undesirable behavior.</p>
<details>
<summary>
Comparison of left/right-handedness of coordinate systems between preview and stable release</summary>
<p>Using Slicer-4.11.20110226: two left handed, one right-handed</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; np.linalg.det(arrayFromVTKMatrix(getNode('vtkMRMLSliceNodeRed').GetSliceToRAS()))
-1.0
&gt;&gt;&gt; np.linalg.det(arrayFromVTKMatrix(getNode('vtkMRMLSliceNodeGreen').GetSliceToRAS()))
1.0
&gt;&gt;&gt; np.linalg.det(arrayFromVTKMatrix(getNode('vtkMRMLSliceNodeYellow').GetSliceToRAS()))
-1.0
</code></pre>
<p>Using Slicer-4.11.20110327: all right-handed</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; np.linalg.det(arrayFromVTKMatrix(getNode('vtkMRMLSliceNodeRed').GetSliceToRAS()))
1.0
&gt;&gt;&gt; np.linalg.det(arrayFromVTKMatrix(getNode('vtkMRMLSliceNodeGreen').GetSliceToRAS()))
1.0
&gt;&gt;&gt; np.linalg.det(arrayFromVTKMatrix(getNode('vtkMRMLSliceNodeYellow').GetSliceToRAS()))
1.0
</code></pre>
</details>
<p>With the new slice axis directions, the arrow buttons work more intuitively with the default 3D orientation, too:</p>
<p>Slicer-4.11.20110226:</p>
<ul>
<li>red: arrow right moves the slice up → as expected</li>
<li>green: arrow right moves the slice backward  → I would not expect this</li>
<li>yellow: arrow right moves the slice left → inconsistent</li>
</ul>
<p>Slicer-4.11.20110327:</p>
<ul>
<li>red: arrow right moves the slice up → as expected</li>
<li>green: arrow right moves the slice forward → as expected</li>
<li>yellow: arrow right moves the slice right → as expected</li>
</ul>
<p>So, overall, the new behavior is more consistent at all levels, expect it is different from the old behavior.</p>
<p>I just read the top post and indeed behavior of the mouse wheel is opposite of what is expected, I’ll invert that.</p>

---

## Post #8 by @chir.set (2021-04-07 16:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="16977">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>indeed behavior of the mouse wheel is opposite of what is expected, I’ll invert that.</p>
</blockquote>
</aside>
<p>Great, that’s the major change.</p>
<p>Currently :<br>
Red slice view : arrow up moves the slice down<br>
It’s troubling also.</p>

---

## Post #9 by @pieper (2021-04-07 17:03 UTC)

<p>The old behavior of the arrow keys in the slice views was that right arrow always went the in the RAS directions (right arrow on a sagittal went to patient right, right arrow on coronal went anterior, right arrow on an an axial went superior).  Now axial and sagittal are reversed from that, which probably is something everyone could get used to, but it seem illogical to me.</p>

---

## Post #10 by @lassoan (2021-04-08 18:45 UTC)

<p>Arrow/scrolling directions are reverted now (<a href="https://github.com/Slicer/Slicer/commit/87d3eb53bdf8915e5e995fd6619237a33866a44c" class="inline-onebox">BUG: Restore slice increment/decrement direction in slice views · Slicer/Slicer@87d3eb5 · GitHub</a>).</p>

---
