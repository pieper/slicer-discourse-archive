# About logic in Scissor tool

**Topic ID**: 29469
**Date**: 2023-05-15
**URL**: https://discourse.slicer.org/t/about-logic-in-scissor-tool/29469

---

## Post #1 by @phtran.dev (2023-05-15 04:59 UTC)

<p>Hi,<br>
I am trying to dig out Slicer code into my Application with free cut feature.<br>
I am debugging Free cut feature in Scissor tool. When I run to function : bool qSlicerSegmentEditorScissorsEffectPrivate::updateBrushStencil(qMRMLWidget* viewWidget),</p>
<pre><code class="lang-auto">  vtkOrientedImageData* modifierLabelmap = q-&gt;modifierLabelmap();
  if (!modifierLabelmap)
    {
    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": Invalid modifierLabelmap";
    return false;
    }
</code></pre>
<p>I do not know how the modifierLabelMap is initialized and when it’s being set . Could you please help to explain me logic as well as how can I get this value from python console ?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2023-05-16 04:47 UTC)

<p>We provide Slicer source code for free, and allow anyone to use it for any purpose. However, it is unlikely that any Slicer user or developer would devote time to explain how you can move Slicer features to other applications.</p>
<p>If you are not sure how to do this then you might consider learning how to customize and extend the Slicer application framework to make it do exactly what you need, instead of developing your application from scratch. You can customize the user interface any way you need; you can have a very simple GUI that contains only those features that your users need right now, and you can expose more features later as needed.</p>

---
