# Slice intersection source code

**Topic ID**: 3024
**Date**: 2018-05-30
**URL**: https://discourse.slicer.org/t/slice-intersection-source-code/3024

---

## Post #1 by @Ricardo_Mesquita (2018-05-30 18:43 UTC)

<p>Hi all,<br>
i would like to know if there is some possibility to control slice intersections manually ,i.e, without mouse control. I intend to set a 3D position  (x,y,z) and then the slice intersection cursor automatically goes to the correspondent XY position in the axial, sagital and coronal planes.<br>
Moreover, is there any source code regarding the slice intersection functionality?<br>
Thanks for your attention!</p>

---

## Post #2 by @gleman (2018-05-30 20:11 UTC)

<p>Not sure what you mean, but does this help?  You can turn on the intersection visibility and move the slice views around programatically  (turn on slices is in the wiki):</p>
<pre><code>def turn_on_slice_intersections():
    viewNodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLSliceCompositeNode')
    viewNodes.UnRegister(slicer.mrmlScene)
    viewNodes.InitTraversal()
    viewNode = viewNodes.GetNextItemAsObject()
    while viewNode:
        viewNode.SetSliceIntersectionVisibility(1)
        viewNode = viewNodes.GetNextItemAsObject()

view_to_color = {'axial':'Red','coronal':'Green','sagittal':'Yellow'}

def get_current_slice(view):
    lm = slicer.app.layoutManager()
    color = lm.sliceWidget(view_to_color[view])
    colorLogic = color.sliceLogic()
    return colorLogic.GetSliceOffset() 
    
def set_current_slice(view, new_level):
    lm = slicer.app.layoutManager()
    color = lm.sliceWidget(view_to_color[view])
    colorLogic = color.sliceLogic()
    colorLogic.SetSliceOffset(new_level)
    return True</code></pre>

---

## Post #3 by @leochan2009 (2018-05-30 21:17 UTC)

<p>I used to make the slice node go through a point. Hope it will help</p>
<p>def updateSliceViewBasedOnPoints(self, pos):<br>
redSliceNode = slicer.mrmlScene.GetNodeByID(“vtkMRMLSliceNodeRed”)<br>
matrixRedOri = redSliceNode.GetSliceToRAS()<br>
matrixRedOri.SetElement(0, 3, pos[0])<br>
matrixRedOri.SetElement(1, 3, pos[1])<br>
matrixRedOri.SetElement(2, 3, pos[2])<br>
redSliceNode.UpdateMatrices()</p>

---

## Post #4 by @Nicole_Aucoin (2018-05-30 21:53 UTC)

<p>Once you have the slice node you can call:</p>
<blockquote>
<p>redSliceNode.JumpSliceByOffsetting(pos[0], pos[1], pos[2])</p>
</blockquote>
<p>or you can use JumpSliceByCentering.</p>
<p>If you’re already using fiducials, you can use the Markups module logic to do this for all slices by calling JumpSlicesToLocation,</p>

---
