# What does this part of code mean? python slicer

**Topic ID**: 14876
**Date**: 2020-12-04
**URL**: https://discourse.slicer.org/t/what-does-this-part-of-code-mean-python-slicer/14876

---

## Post #1 by @NoobForSlicer (2020-12-04 05:18 UTC)

<p>Can someone explain to me what does this part of code does:</p>
<p>imagenode.SetOrigin(tuple(list([0,0,translation])))</p>
<p>what does imagenode.setorigin does?</p>
<h1>Create image node</h1>
<pre><code>    start = time.time()
    imagenode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
    imagenodeID = shNode.GetItemByDataNode(imagenode)
    shNode.SetItemName(imagenodeID, nodename)
    imagenode.CreateDefaultDisplayNodes()
    slicer.util.updateVolumeFromArray(imagenode, finalimage)
    if success: # apply transform
        imagenode.SetAndObserveTransformNodeID(transformationNode.GetID())
    imagenode.SetOrigin(tuple(list([0,0,translation])))
    end = time.time()
    logging.info(f"image node created in {human_time(end-start)}")
    slicer.app.processEvents()</code></pre>

---
