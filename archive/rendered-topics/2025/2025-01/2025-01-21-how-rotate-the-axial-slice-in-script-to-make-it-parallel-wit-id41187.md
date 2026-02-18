# How rotate the axial slice in script to make it parallel with the plane across 3 specified points?

**Topic ID**: 41187
**Date**: 2025-01-21
**URL**: https://discourse.slicer.org/t/how-rotate-the-axial-slice-in-script-to-make-it-parallel-with-the-plane-across-3-specified-points/41187

---

## Post #1 by @SummerZ2020 (2025-01-21 09:37 UTC)

<p>Operating system:windows<br>
Slicer version:5.6.2<br>
Expected behavior: After running script in slicer, the crossline in the slice window is rotated.<br>
Actual behavior: no any rotated happened.<br>
The script is:</p>
<pre><code class="lang-auto"># 
        markup_node = slicer.vtkMRMLMarkupsFiducialNode()
        markup_node.SetName("MyPoints")
        slicer.mrmlScene.AddNode(markup_node)

        # 
        print('le',points['le'])
        fiducial_index  = markup_node.AddControlPoint(-1*points['le'][0][0], -1*points['le'][0][1], points['le'][0][2])
        markup_node.SetNthControlPointLabel(fiducial_index, 'le')
        fiducial_index = markup_node.AddControlPoint(-1*points['re'][0][0], -1*points['re'][0][1], points['re'][0][2])
        markup_node.SetNthControlPointLabel(fiducial_index, 're')
        fiducial_index = markup_node.AddControlPoint(-1*points['oo'][0][0], -1*points['oo'][0][1], points['oo'][0][2])
        markup_node.SetNthControlPointLabel(fiducial_index, 'oo')

        # 
        slicer.app.applicationLogic().GetSelectionNode().SetReferenceActivePlaceNodeID(markup_node.GetID())
        slicer.app.applicationLogic().PropagateVolumeSelection(0)

           #
        p0 = np.array(points['le'][0])
        p1 = np.array(points['re'][0])
        p2 = np.array(points['oo'][0])

        # 
        v1 = p1 - p0
        v2 = p2 - p0

        # 
        normal = np.cross(v1, v2)
        normal = normal / np.linalg.norm(normal)  # 归一化

        # 
        #
        z_axis = normal
        x_axis = v1 / np.linalg.norm(v1)
        y_axis = np.cross(z_axis, x_axis)
        y_axis = y_axis / np.linalg.norm(y_axis)
        x_axis = np.cross(y_axis, z_axis)

        #
        transform_matrix = np.eye(4)
        transform_matrix[:3, 0] = x_axis
        transform_matrix[:3, 1] = y_axis
        transform_matrix[:3, 2] = z_axis
        transform_matrix[:3, 3] = p0

        # 
        print(f'Transform Matrix:\n{transform_matrix}')

        #
        slice_node = slicer.util.getNode('vtkMRMLSliceNodeRed')
        slice_node.GetSliceToRAS().DeepCopy(slicer.util.vtkMatrixFromArray(transform_matrix))
        slice_node.UpdateMatrices()

        # 
        slicer.app.applicationLogic().FitSliceToAll()

     
        print('Slice to RAS Transformed Matrix:')
        print(slice_node.GetSliceToRAS())
</code></pre>

---

## Post #2 by @chir.set (2025-01-21 10:00 UTC)

<p>You may get some insight <a href="https://gitlab.com/chir-set/RcHacks7/-/blob/900664b75fca04210a065f1324d7fae0214eb559/12-ResliceToAxis.py.txt#L64" rel="noopener nofollow ugc">here</a> and <a href="https://gitlab.com/chir-set/RcHacks7/-/blob/900664b75fca04210a065f1324d7fae0214eb559/00-Lib.py.txt#L125" rel="noopener nofollow ugc">here</a>.</p>

---
