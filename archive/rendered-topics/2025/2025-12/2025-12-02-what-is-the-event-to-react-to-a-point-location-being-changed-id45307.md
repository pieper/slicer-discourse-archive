---
topic_id: 45307
title: "What Is The Event To React To A Point Location Being Changed"
date: 2025-12-02
url: https://discourse.slicer.org/t/45307
---

# What is the event to react to a point location being changed in a MarkupsNode/MarkupsLineNode?

**Topic ID**: 45307
**Date**: 2025-12-02
**URL**: https://discourse.slicer.org/t/what-is-the-event-to-react-to-a-point-location-being-changed-in-a-markupsnode-markupslinenode/45307

---

## Post #1 by @Victor_Wayne (2025-12-02 06:34 UTC)

<p>Hi,</p>
<p>To react to a point location being changed in a MarkupsLineNode I’ve been using PointModifiedEvent and I am calling one function whenever the location of a point changes. However my callback function is being called even when a MarkupsLine’s point is <strong>hidden</strong>. I don’t want that since my callback function is a bit compute intensive. So what is the event for listening just to a point being modified in a vtkMRMLMarkupsLineNode?</p>
<p>I checked the documentation and couldn’t find one. Do I have no other way than to cache the point location and compare them?</p>
<p>Thanks for your help in advance.</p>

---

## Post #2 by @mau_igna_06 (2025-12-02 15:33 UTC)

<p>Did you try something like this:</p>
<pre data-code-wrap="python"><code class="lang-python">def setVisibility(node, visible):
  node.GetDisplayNode().SetVisibility(visible)
  if visible:
    node.DisableModifiedEventOff()
  else:
    node.DisableModifiedEventOn()
</code></pre>

---

## Post #3 by @Victor_Wayne (2025-12-04 08:55 UTC)

<p>I am not hiding the line point using code. When I hide one of the endpoints of the line using the eye icon in the Markups extension this pointModifiedEvent Triggers.</p>

---

## Post #5 by @Victor_Wayne (2025-12-04 10:34 UTC)

<p>I am not hiding the line point using code. When I hide one of the endpoints of the line using the eye icon in the Markups extension this pointModifiedEvent Triggers.</p>
<p>I need my callback function to be called when one of the control point is modified using the GUI of the Markups module. But not when the point is hidden using the eye icon using the Markups extension</p>

---
