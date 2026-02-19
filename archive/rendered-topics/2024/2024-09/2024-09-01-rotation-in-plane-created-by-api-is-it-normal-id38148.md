---
topic_id: 38148
title: "Rotation In Plane Created By Api Is It Normal"
date: 2024-09-01
url: https://discourse.slicer.org/t/38148
---

# Rotation in plane created by API : is it normal?

**Topic ID**: 38148
**Date**: 2024-09-01
**URL**: https://discourse.slicer.org/t/rotation-in-plane-created-by-api-is-it-normal/38148

---

## Post #1 by @chir.set (2024-09-01 10:11 UTC)

<p>If a markups plane is created using the API, and its normal and origin are set to those of another plane interactively placed in a rotated 3D view, the plane created by API has an extra rotation.</p>
<pre><code class="lang-auto">interactivePlane = getNode("P")

# New plane on interactive plane : there is an additional rotation
apiPlane = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode")
apiPlane.AddControlPointWorld(interactivePlane.GetOriginWorld())
apiPlane.SetNormalWorld(interactivePlane.GetNormalWorld())

# New plane on api plane : there is no additional rotation
apiPlane2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode")
apiPlane2.AddControlPointWorld(apiPlane.GetOriginWorld())
apiPlane2.SetNormalWorld(apiPlane.GetNormalWorld())
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc25fcbb2c65e1e26a636508e7a02ddb43320739.png" alt="rotated_api_planes" data-base62-sha1="zYBI0y3p0BTaLjDP2IsIQ2y8Vbb" width="546" height="495"></p>
<p>Is this to be expected? If so, how should it be handled in user code to cancel this rotation?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2024-09-01 11:36 UTC)

<p>Yes, this is the expected behavior, because normal direction does not specify the orientation of a rectangle in 3D. You need to specify direction of all the axes if you care about the rotation around the normal vector.</p>

---
