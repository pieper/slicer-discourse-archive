# How to get mouse curser position in 3D view?

**Topic ID**: 27456
**Date**: 2023-01-25
**URL**: https://discourse.slicer.org/t/how-to-get-mouse-curser-position-in-3d-view/27456

---

## Post #1 by @dsa934 (2023-01-25 06:08 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<pre><code class="lang-auto">
def test():

    # get crosshair 
    crosshairNode=slicer.util.getNode("Crosshair")

    pos = [0,0,0]

    crosshairNode.GetCursorPositionRAS(pos)

    print(pos)

    slicer.modules.markups.logic().AddControlPoint(pos[0], pos[1], pos[2])
</code></pre>
<p>This code works only in slicer view (R,Y,G), how do I make it work in 3d VIEW?</p>

---
