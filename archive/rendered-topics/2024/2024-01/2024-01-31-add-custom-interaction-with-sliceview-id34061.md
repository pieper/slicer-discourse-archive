# Add custom interaction with sliceview

**Topic ID**: 34061
**Date**: 2024-01-31
**URL**: https://discourse.slicer.org/t/add-custom-interaction-with-sliceview/34061

---

## Post #1 by @keri (2024-01-31 10:42 UTC)

<p>Hi,</p>
<p>There are two ways to zoom slice view:</p>
<ol>
<li>hold right mouse btn adn drag</li>
<li>hold <code>ctrl</code> key and use wheel</li>
</ol>
<p>I’m going to implement the interaction that changes FOV independently by vertical and horizontal dimensions when user holds <code>ctrl</code> and drag mouse with right button mouse pressed.</p>
<p>Is there a way to do that inside custom displayable manager or do I have to modify <code>vtkMRMLSliceViewInteractorStyle</code>?</p>

---

## Post #2 by @keri (2024-02-01 16:20 UTC)

<p>This can be done with custom displayable manager’s methods:</p>
<pre><code class="lang-auto">public:
  virtual bool CanProcessInteractionEvent(vtkMRMLInteractionEventData* eventData, double &amp;closestDistance2) override;
  virtual bool ProcessInteractionEvent(vtkMRMLInteractionEventData* eventData) override;
</code></pre>
<p><code>eventData</code> contains all the necessary information about hotkeys and mouse pisition.</p>
<p>And sliceview zooming implementation example can be found in <code>vtkMRMLSliceIntersectionWidget::ProcessZoomSlice</code></p>

---
