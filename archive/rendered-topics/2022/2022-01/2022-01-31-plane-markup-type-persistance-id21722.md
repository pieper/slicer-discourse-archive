---
topic_id: 21722
title: "Plane Markup Type Persistance"
date: 2022-01-31
url: https://discourse.slicer.org/t/21722
---

# Plane markup type persistance

**Topic ID**: 21722
**Date**: 2022-01-31
**URL**: https://discourse.slicer.org/t/plane-markup-type-persistance/21722

---

## Post #1 by @smrolfe (2022-01-31 22:35 UTC)

<p>Is it possible to make the plane markup type persistent, or to change the default type? I usually use the 3-point placement method, but am needing to change this for each plane, even when in persistent placement mode.</p>

---

## Post #2 by @lassoan (2022-02-01 02:34 UTC)

<p>You can register a default vtkMRMLMarkupsPlaneNode in the scene and set the plane type to anything that you prefer. You can do this in the application startup script.</p>
<p>If you find that you or users wants to set this often, then you could add an “Advanced” section in “Plane settings” with a “Save to defaults” and “Reset to defaults” buttons.</p>

---
