---
topic_id: 37839
title: "Distance Calculation Between Two Model Nodes"
date: 2024-08-12
url: https://discourse.slicer.org/t/37839
---

# Distance Calculation Between Two Model Nodes

**Topic ID**: 37839
**Date**: 2024-08-12
**URL**: https://discourse.slicer.org/t/distance-calculation-between-two-model-nodes/37839

---

## Post #1 by @park (2024-08-12 09:00 UTC)

<p>Hello,</p>
<p>I have two model nodes: one that moves based on a transform handle and another that is fixed. I want to find the shortest distance between these two model nodes.</p>
<p>I’ve implemented this functionality with the code below, but I’d like to improve its speed (it seems that copying the nodes is taking a significant amount of time).</p>
<p>Could you provide some advice on optimizing this functionality?</p>
<pre><code class="lang-auto">def compute_closest_distance_between_models(event, caller, modelA, modelB):
    
    polyDataA = modelA.GetPolyData()   
    transformNode = modelB.GetParentTransformNode()
    
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    nodeItem = shNode.GetItemByDataNode(modelB)
    copyItem = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, nodeItem)
    modelBCopy = shNode.GetItemDataNode(copyItem)
    
    modelBCopy.SetAndObserveTransformNodeID(transformNode.GetID())
    slicer.vtkSlicerTransformLogic().hardenTransform(modelBCopy)
    polyDataB = modelBCopy.GetPolyData()
    
    distanceFilter = vtk.vtkImplicitPolyDataDistance()
    distanceFilter.SetInput(polyDataB)
    
    closestDistance = float('inf')
    
    for i in range(polyDataA.GetNumberOfPoints()):
        point = polyDataA.GetPoint(i)
        distance = distanceFilter.EvaluateFunction(point)
        if distance &lt; closestDistance:
            closestDistance = distance
    
    slicer.mrmlScene.RemoveNode(modelBCopy)
    print(closestDistance)
    return closestDistance
</code></pre>

---

## Post #2 by @pieper (2024-08-12 20:33 UTC)

<p>You could do this same loop in C++ and it would be faster.  But if you have a labelmap version of the model (i.e. it comes from a segment or is easy to convert to one) you could make a distance transform volume from that.  Then you should also be able to get the point coordinates of the other model as a numpy array, convert them to IJK, extract the distances from the volume with a vectorized indexing operation and then find the min of the resulting array.</p>

---

## Post #3 by @park (2024-08-13 12:11 UTC)

<p>Thank you very much. Converting to a segment and then performing the calculations seems like a very good approach.</p>

---
