# How to Align a vtk Cylinder to a Known Vector

**Topic ID**: 35880
**Date**: 2024-05-02
**URL**: https://discourse.slicer.org/t/how-to-align-a-vtk-cylinder-to-a-known-vector/35880

---

## Post #1 by @Teresa_Marotta (2024-05-02 18:31 UTC)

<p>Hi all, I’m looking to create a model of a cylinder and orient it along a known vector using python. More specifically, I have two control points, but I want to create a line that goes between them but extends past the control points along the same direction.</p>
<p>Any help with this is greatly appreciated.</p>

---

## Post #2 by @rfenioux (2024-05-03 07:57 UTC)

<p>I think the simplest way to achieve that would be the following:</p>
<ul>
<li>retrieve the  existing control points as numpy arrays</li>
<li>using those, compute the two endpoints of your desired line</li>
<li>create a markupsLineNode with these new points as control points</li>
<li>hide the label text and the new control points to only show the line</li>
</ul>
<p>To do all that, I recommend looking at the examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">script repository</a> and/or search for previous answers in the discourse.</p>

---

## Post #3 by @mikebind (2024-05-03 16:15 UTC)

<p>Here is some rough but working code which I wrote a long time ago when I was trying to learn to do something similar that does almost exactly what you want. The only thing missing is calculating the extensions you want, which could be calculated in a pre-step, or modified into the function below.</p>
<pre><code class="lang-auto">def makeCylinderModelNode(
    endpoint1, endpoint2, radiusMm=0.25, numberOfSides=20
):
    """Make a cylinder surface, transform it so that the center of one end is endpoint1, and the other
    is centered on endpoint2"""
    import numpy as np

    center = np.add(endpoint1, endpoint2) / 2.0
    height = np.linalg.norm(np.subtract(endpoint2, endpoint1))
    direction = np.subtract(endpoint2, endpoint1)
    print(
        "Center: (%0.2f, %0.2f, %0.2f)\nHeight: %0.2f\nDirection: (%0.2f, %0.2f, %0.2f)"
        % (*center, height, *direction)
    )
    #
    cyl = vtk.vtkCylinderSource()
    cyl.SetRadius(radiusMm)
    cyl.SetResolution(numberOfSides)
    cyl.SetHeight(height)
    cyl.Update()  # don't know if this is necessary
    #
    initial_axis = [0, 1, 0]
    #
    # Create transform for it
    # The initial axis direction is anterior/posterior (0,1,0) in RAS, we want to rotate that so that it
    # points along the vector represented in "direction"
    # Can determine this by finding the cross product, and angle from dot product
    axis = np.cross(initial_axis, direction)
    angle_deg = 180 / np.pi * np.arccos(np.dot(initial_axis, direction) / (np.linalg.norm(initial_axis) * np.linalg.norm(direction)))
    
    #
    print("Axis: (%0.2f, %0.2f, %0.2f)\nAngle: %0.2f deg" % (*axis, angle_deg))
    #
    vtkTform = vtk.vtkTransform()
    vtkTform.Translate(center)
    vtkTform.RotateWXYZ(angle_deg, axis)
    vtkTform.Modified()  # don't know if this is necessary
    #
    # Create filter
    vtkTformFilter = vtk.vtkTransformFilter()
    vtkTformFilter.SetInputData(cyl.GetOutput())
    vtkTformFilter.SetTransform(vtkTform)
    vtkTformFilter.Update()  # don't know if this is necessary
    #
    # Create model node and connect it to the transformed cylinder
    model_node = slicer.modules.models.logic().AddModel(vtkTformFilter.GetOutput())
    return model_node
</code></pre>

---

## Post #4 by @chir.set (2024-05-03 19:01 UTC)

<p>You may also draw a cylinder using the ExtraMarkups extension.</p>
<p>Then you may set the control points defining the axis of the cylinder using python since you know the coordinates of your 2 control points. Next ajust the radius.</p>
<p>You may finally calculate the coordinates of a point beyond the line defined by your pair of control points using vtkMath::GetPointAlongLine(). Then draw a line as suggested <a href="https://discourse.slicer.org/t/how-to-align-a-vtk-cylinder-to-a-known-vector/35880/2">here</a>.</p>

---
