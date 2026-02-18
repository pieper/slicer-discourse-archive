# Set visibility of fiducials inside an ROI?

**Topic ID**: 16300
**Date**: 2021-03-02
**URL**: https://discourse.slicer.org/t/set-visibility-of-fiducials-inside-an-roi/16300

---

## Post #1 by @hherhold (2021-03-02 01:31 UTC)

<p>I’d like to be able to make an ROI and hide all the markup fiducials inside of it. Is there a way to get the RAS bounds of an ROI? <code>GetRASBounds()</code> is returning <code>[1e+299, -1e+299, 1e+299, -1e+299, 1e+299, -1e+299]</code>, but <code>GetBoundsROI()</code> returns reasonable-looking values (but not in RAS coordinates). Do I need to do something to it to get it to set the RAS bounds? And do I need RAS coordinates to then loop through the MarkupsFiducialNode, setting visibility?</p>
<p>(Does this make sense?)</p>
<p>Thanks!!!</p>
<p>-Hollister</p>

---

## Post #2 by @muratmaga (2021-03-02 01:38 UTC)

<p>FYI If you don’t need to do this programmatically, SlicerMorph’s MarkupEditor does something similar (at least lets you select points within a curve) via <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/MarkupEditor" rel="noopener nofollow ugc">MarkupEditor</a></p>

---

## Post #3 by @hherhold (2021-03-02 02:29 UTC)

<p>Oh, that’s most excellent! That’s actually a lot easier than making an ROI (for my workflow).</p>
<p>Thanks, Murat! Hope you’re doing well.</p>
<p>-Hollister</p>

---

## Post #4 by @hherhold (2021-03-03 13:28 UTC)

<p>Hmm, I’m a little confused by what “selected” means and how that is set in code and in the control points list. Here’s my code to toggle visibility for selected control points:</p>
<pre><code>def hh_toggle_visibility_selected_fiducials():
    mod = slicer.util.getModule("Markups")
    ml = mod.logic()
    n = slicer.util.getNode(ml.GetActiveListID())
    num_control_points = n.GetNumberOfControlPoints()
    for i in range(num_control_points):
      visible = n.GetNthFiducialVisibility(i)
      selected = n.GetNthFiducialSelected()
      if selected:
        n.SetNthFiducialVisibility(i, not visible)
</code></pre>
<p>If I use the button in the control points to select all, then run my code, it toggles the visibility just fine. But if I pick a few points by hand, using the check boxes, or use the select points by curve, as <a class="mention" href="/u/muratmaga">@muratmaga</a> mentioned, the above code has no effect. I’ve compared what I’m doing to the C++ in <code>vtkSlicerMarkupsLogic</code> and I can’t see any meaningful differences… Is there something obvious I’m missing?</p>
<p>Thanks!</p>

---

## Post #5 by @lassoan (2021-03-03 13:41 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="16300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p><code>n.GetNthFiducialSelected()</code></p>
</blockquote>
</aside>
<p>This is a syntax error. The code will have no effect because it just stops.</p>
<p>Have you connected using PyCharm debugger? Recent versions are quote buggy and may cause you not to see error messages in the Slicer console in certain circumstances.</p>

---

## Post #6 by @hherhold (2021-03-03 13:47 UTC)

<p>GAAAH that’s totally embarrassing. Works perfectly now.</p>
<p>I do not use PyCharm - I either use VS Code when working inside the Slicer codebase or just Emacs when tweaking my .slicerrc.py file, where this function is. (My Emacs setup has no checking or code completion. Maybe it’s time to rethink that…)</p>
<p>THANKS!!</p>

---
