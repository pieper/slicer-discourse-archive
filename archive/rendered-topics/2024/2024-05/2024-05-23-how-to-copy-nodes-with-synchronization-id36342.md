# How to Copy Nodes with Synchronization

**Topic ID**: 36342
**Date**: 2024-05-23
**URL**: https://discourse.slicer.org/t/how-to-copy-nodes-with-synchronization/36342

---

## Post #1 by @park (2024-05-23 09:07 UTC)

<p>Hello all,</p>
<p>I would like to apply gridTransform to a specific Slice View (panoramic view) to visualize the data, as shown in the image below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/685182f5e4368041a153dd15abee8741c4fe4142.png" data-download-href="/uploads/short-url/eSQigCVjMFqSJYQoi300PG5E7vk.png?dl=1" title="2D view" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/685182f5e4368041a153dd15abee8741c4fe4142_2_690x145.png" alt="2D view" data-base62-sha1="eSQigCVjMFqSJYQoi300PG5E7vk" width="690" height="145" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/685182f5e4368041a153dd15abee8741c4fe4142_2_690x145.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/685182f5e4368041a153dd15abee8741c4fe4142_2_1035x217.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/685182f5e4368041a153dd15abee8741c4fe4142.png 2x" data-dominant-color="838483"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2D view</span><span class="informations">1342×283 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I was advised that the easiest way to do this is to copy all the data, apply the Transform, and then visualize it.<br>
<a href="https://discourse.slicer.org/t/apply-transform-matirx-to-only-specific-2d-view/36273/3">https://discourse.slicer.org/t/apply-transform-matirx-to-only-specific-2d-view/36273/3</a></p>
<p>Therefore, I am seeking advice on how to copy the data.</p>
<p>When I have the original node A and the copied node A’, I want to ensure that any transformations (such as color, transparency, position, etc.) applied to node A are reflected in node A’ and vice versa.</p>
<p>This way, any modifications made in one view will be consistently reflected in both the transformed view and the non-transformed view.</p>
<p>The nodes to be copied include Volume, Model, Markup, and Transform. I also plan to create copies for any new nodes that are added.</p>
<p>Thank you for your assistance.</p>

---

## Post #2 by @pieper (2024-05-23 15:02 UTC)

<p>I don’t think there’s any code that does the specific operation currently, but it shouldn’t be too much work to make a kind of “dynamic clone” node.</p>
<p>Effectively you would just need to observe modify events from the source node and copy parameters to the cloned nodes when anything change, but filter out any changes you don’t have to have apply to the clone, like setting the transforms.  This same code could handle the shared bulk data (both nodes pointing to the same <code>vtkImageData</code> for example).</p>
<p>If this approach works and you find it useful  it would be great to consider making it a core feature somehow, or maybe part of an extension or just an example in the script repository.</p>

---

## Post #3 by @park (2024-05-28 01:22 UTC)

<p>Here is the codes I made.<br>
This synch A → A’ one way</p>
<pre><code class="lang-auto"># Get hierarchyNode
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
  
# Get info from origin node
nodeItem = shNode.GetItemByDataNode(node)
nodeName = node.GetName()

# Clone node
cloneItem = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, nodeItem)
clonedNode = shNode.GetItemDataNode(cloneItem)
clonedNode.SetName(nodeName+'Clone')
  
# Set clone data unber origin data 
shNode.CreateItem(nodeItem, clonedNode)

# Clone data synch 
def synchOriginToClone(unusedArg1=None, unusedArg2=None, unusedArg3=None):
    clonedNode.CopyContent(node)
    
node.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, synchOriginToClone)
node.AddObserver(slicer.vtkMRMLTransformNode.TransformModifiedEvent, synchOriginToClone)
</code></pre>

---
