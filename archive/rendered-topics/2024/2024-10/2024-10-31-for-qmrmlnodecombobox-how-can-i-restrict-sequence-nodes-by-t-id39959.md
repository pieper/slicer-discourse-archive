# For qMRMLNodeComboBox, how can I restrict Sequence nodes by type?

**Topic ID**: 39959
**Date**: 2024-10-31
**URL**: https://discourse.slicer.org/t/for-qmrmlnodecombobox-how-can-i-restrict-sequence-nodes-by-type/39959

---

## Post #1 by @mikebind (2024-10-31 17:43 UTC)

<p>I am working on a module to process a 4D data set.  It will need to take as inputs a sequence node of segmentations and a sequence node of tables.  Also present in the scene will be (possibly multple) sequence nodes of image volumes.  I want only sequence nodes holding segmentations to be allowed choices in the combobox for segmentations, and only sequence nodes holding tables to be allowed choices in the combobox for tables.  I don’t want the image sequences to be options in either place.  qMRMLNodeComboBox allows restriction by node type, but all sequences are of type vtkMRMLSequenceNode, so all sequences show up as options, even if they hold inappropriate data types.  Is there any way to filter or restrict further?</p>

---

## Post #2 by @chir.set (2024-10-31 19:28 UTC)

<p>You may add an attribute to your target nodes and to the selector. See <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/a4f318ee39b71085ef414b5efedd10c2da78d52d/ExtractCenterline/ExtractCenterline.py#L89" rel="noopener nofollow ugc">here</a> for an example.</p>

---

## Post #3 by @mikebind (2024-11-01 15:39 UTC)

<p>That’s perfect!  Thanks so much.</p>

---

## Post #4 by @mikebind (2024-11-01 20:18 UTC)

<p>In fact, vtkMRMLSequenceNode objects which have a data node type stored in them already have an attribute called “DataNodeClassName”, so all I needed to do was add this attribute to the selector like this:</p>
<p><code>self.ui.segmentationSequenceSelector.addAttribute("vtkMRMLSequenceNode", "DataNodeClassName", "vtkMRMLSegmentationNode")</code></p>
<p>Or like this for a sequence node holding tables:</p>
<p><code>self.ui.segmentationSequenceSelector.addAttribute( "vtkMRMLSequenceNode", "DataNodeClassName", "vtkMRMLTableNode")</code></p>
<p>Empty sequence nodes do not have this attribute set, but it can be set manually, or it is automatically set when the first data node is added to the sequence.</p>

---
