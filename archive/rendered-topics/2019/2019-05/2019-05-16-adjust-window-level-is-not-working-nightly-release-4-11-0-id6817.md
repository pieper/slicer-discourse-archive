# Adjust Window Level is not working (nightly release 4.11.0)

**Topic ID**: 6817
**Date**: 2019-05-16
**URL**: https://discourse.slicer.org/t/adjust-window-level-is-not-working-nightly-release-4-11-0/6817

---

## Post #1 by @JoostJM (2019-05-16 14:22 UTC)

<p>In the latest nigthly release (13-05-2019, windows), adjusting window/level by left-click + dragging is not working anymore. It is still possible to adjust window/level through the Volumes module however.</p>
<p>Furthermore, when checking the interactorstyle, it shows that AdjustWindowLevelForeground and AdjustWindowLevelBackground are enabled.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; interactorStyle = slicer.app.layoutManager().sliceWidget('Red').sliceView().sliceViewInteractorStyle()
&gt;&gt;&gt; interactorStyle.GetActionEnabled(interactorStyle.AdjustWindowLevelForeground)
True
&gt;&gt;&gt; interactorStyle.GetActionEnabled(interactorStyle.AdjustWindowLevelBackground)
True
</code></pre>

---

## Post #2 by @cpinter (2019-05-16 14:43 UTC)

<p>HI Joost,</p>
<p>Mouse modes have recently changed. To window/level you need to switch to W/L mode by clicking on the button on the toolbar that is activated in this screenshot:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb0efdef9970062e2f46839e8477554354ad1b11.png" alt="image" data-base62-sha1="sYl2T2YCAe7nbjZcn0Ay7MRRX7b" width="133" height="49"></p>

---

## Post #3 by @JoostJM (2019-05-16 14:44 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Thanks! Is there a way to set the default to W/L adjustment on startup?</p>

---

## Post #4 by @cpinter (2019-05-16 14:51 UTC)

<p>You can put this in the slicerrc.py</p>
<pre><code>appLogic = slicer.app.applicationLogic()
interactionNode = appLogic.GetInteractionNode()
interactionNode.SetCurrentInteractionMode(slicer.vtkMRMLInteractionNode.AdjustWindowLevel)</code></pre>

---

## Post #5 by @lassoan (2019-05-16 14:52 UTC)

<p>See some more information about the feature here: <a href="https://discourse.slicer.org/t/feedback-requested-how-to-improve-mouse-interaction-in-views/6420" class="inline-onebox">Feedback requested: How to improve mouse interaction in views?</a></p>

---
