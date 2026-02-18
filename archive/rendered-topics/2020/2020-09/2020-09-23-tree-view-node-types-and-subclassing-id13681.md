# Tree view node types and subclassing

**Topic ID**: 13681
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/tree-view-node-types-and-subclassing/13681

---

## Post #1 by @giovform (2020-09-23 20:12 UTC)

<p>Hello, I am modifying the Data module (copying the widget contents to a new module and calling it another name), and would like to only show some scalar volumes on it’s tree view. For that, I could use instead of this:</p>
<pre><code>subjectHierarchyTreeView.nodeTypes = ["vtkMRMLScalarVolumeNode"]
</code></pre>
<p>, something like this:</p>
<pre><code>subjectHierarchyTreeView.nodeTypes = ["vtkMRMLScalarVolumeSubclassNode"]
</code></pre>
<p>I tried to subclass the vtkMRMLScalarVolumeNode:</p>
<pre><code>class vtkMRMLScalarVolumeSubclassNode(slicer.vtkMRMLScalarVolumeNode):

    @staticmethod
    def GetClassName():
        return "vtkMRMLScalarVolumeSubclassNode"
</code></pre>
<p>and succeed in using it as a scalar volume, but it still maintains the original ClassName as show in the Data module “Node information”:</p>
<pre><code>ClassName: vtkMRMLScalarVolumeNode
</code></pre>
<p>I don’t even know if is the right way to create a new node type, but it’s what I came with for now. I would be grateful for any clarifications on how to create subtypes of nodes.</p>

---

## Post #2 by @lassoan (2020-09-24 00:05 UTC)

<p>You cannot override the class name of a C++ class in Python.</p>
<p>The subject hierarchy selector will have filtering capabilities based on attribute values, by until then you need to use workarounds.</p>
<p>For example you can choose to show nodes in a certain branch. Or use qMRMLNodeComboBox, as it can filter nodes by custom attributes.</p>

---
