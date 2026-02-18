# Finding coordinates for plane-line intersection

**Topic ID**: 28813
**Date**: 2023-04-08
**URL**: https://discourse.slicer.org/t/finding-coordinates-for-plane-line-intersection/28813

---

## Post #1 by @esomjai (2023-04-08 22:57 UTC)

<p>I was wondering if there’s s script I could use to get the coordinates of my intersection point where my plane and line meet.<br>
I would like to use this coordinate later on for angle measurements as my project involves angles measured against a plane defined by interlandmark lines.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66ce8811cc56b67e084db9d03b22b8d83d198f7c.png" data-download-href="/uploads/short-url/eFtc0Hi6LScJBwsNQUhxEGOoToM.png?dl=1" title="Screenshot 2023-04-09 at 00.52.46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66ce8811cc56b67e084db9d03b22b8d83d198f7c.png" alt="Screenshot 2023-04-09 at 00.52.46" data-base62-sha1="eFtc0Hi6LScJBwsNQUhxEGOoToM" width="541" height="500" data-dominant-color="9392C8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-09 at 00.52.46</span><span class="informations">585×540 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-04-09 01:44 UTC)

<p>Bing chat question: “generate python code that can compute intersection point of a line and plane in 3D”</p>
<p>Answer:</p>
<pre><code class="lang-python"># Define a line by its direction vector and a point on it
line_dir = [1, 2, 3] # direction vector of the line
line_pt = [0, 0, 0] # a point on the line

# Define a plane by its normal vector and a point on it
plane_norm = [4, 5, 6] # normal vector of the plane
plane_pt = [1, 1, 1] # a point on the plane

# Compute the dot product of the line direction and the plane normal
dot_prod = sum([a*b for a,b in zip(line_dir, plane_norm)])

# Check if the dot product is zero, which means the line is parallel to the plane
if dot_prod == 0:
    print("The line is parallel to the plane. No intersection point.")
else:
    # Compute the parameter t that gives the intersection point
    t = sum([(a-b)*c for a,b,c in zip(plane_pt, line_pt, plane_norm)]) / dot_prod

    # Compute the intersection point by plugging t into the line equation
    inter_pt = [a + b*t for a,b in zip(line_pt, line_dir)]

    # Print the intersection point
    print("The intersection point is", inter_pt)
</code></pre>
<p>The complete solution (setting the inputs from markupnodes and writing the result to a markup node:</p>
<pre><code class="lang-python"># Get inputs from nodes
lineNode = getNode('L')
planeNode = getNode('P')
# Create output node
intersectionPointNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', "Intersection")

import numpy as np

# Define a line by its direction vector and a point on it
line_dir = np.array(lineNode.GetLineStartPositionWorld())-np.array(lineNode.GetLineEndPositionWorld())
line_dir /= np.linalg.norm(line_dir)
line_pt = lineNode.GetLineStartPositionWorld()

# Define a plane by its normal vector and a point on it
plane_norm = planeNode.GetNormalWorld()
plane_pt = planeNode.GetOriginWorld()

###

# Compute the dot product of the line direction and the plane normal
dot_prod = sum([a*b for a,b in zip(line_dir, plane_norm)])

# Check if the dot product is zero, which means the line is parallel to the plane
if dot_prod == 0:
    print("The line is parallel to the plane. No intersection point.")
else:
    # Compute the parameter t that gives the intersection point
    t = sum([(a-b)*c for a,b,c in zip(plane_pt, line_pt, plane_norm)]) / dot_prod

    # Compute the intersection point by plugging t into the line equation
    inter_pt = [a + b*t for a,b in zip(line_pt, line_dir)]

    # Print the intersection point
    print("The intersection point is", inter_pt)

###

# Save result into the output node
intersectionPointNode.AddControlPointWorld(inter_pt)
</code></pre>

---

## Post #3 by @esomjai (2023-04-09 16:52 UTC)

<p>Absolute lifesaver! Thank you!</p>

---
