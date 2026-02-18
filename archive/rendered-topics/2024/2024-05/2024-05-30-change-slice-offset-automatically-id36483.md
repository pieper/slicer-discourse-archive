# Change slice offset automatically

**Topic ID**: 36483
**Date**: 2024-05-30
**URL**: https://discourse.slicer.org/t/change-slice-offset-automatically/36483

---

## Post #1 by @Xiaojie_Guo (2024-05-30 02:46 UTC)

<p>Hi, all<br>
I saw a script <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-slice-offset" rel="noopener nofollow ugc">here</a>, which could change the Red slice.</p>
<p>Suppose there is a CT data of 512 slices. I want to scroll from slice 0 to slice 511 automatically, is it possible to implement that using a python script?</p>
<p>Here is a try to move 2 times in Red slice, but the GUI is not updated immediately. I want to know how to update the GUI.</p>
<pre><code class="lang-auto">import time

layoutManager = slicer.app.layoutManager()

red = layoutManager.sliceWidget("Red")
redLogic = red.sliceLogic()

# Print current slice offset position
print(redLogic.GetSliceOffset())

# Change slice position
redLogic.SetSliceOffset(-400)
print('move first')
    
time.sleep(1.0)
    
redLogic.SetSliceOffset(-500)
print('move sceond')
</code></pre>

---

## Post #2 by @lassoan (2024-05-30 12:51 UTC)

<p>This looks good, but Slicer is an event-driven application, so you either need to force a redraw (<code>slicer.util.forceRenderAllViews()</code>) or pump the event loop (<code>slicer.app.processEvents()</code>) to immediately update the display after data modification.</p>
<p>See a complete implementation of <a href="https://github.com/Slicer/Slicer/blob/2e6f53f27386dddacbb690956b35396ba47a53a5/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1228-L1256">slicing through the scene and capturing each image</a> in Screen Capture module.</p>

---

## Post #3 by @Xiaojie_Guo (2024-05-31 01:54 UTC)

<p>The second choice is what I need. Thanks a lot.</p>

---
