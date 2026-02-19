---
topic_id: 28435
title: "Markups Saved With Scalar Visibility On Produce Warning When"
date: 2023-03-17
url: https://discourse.slicer.org/t/28435
---

# Markups saved with Scalar Visibility ON produce warning when loading

**Topic ID**: 28435
**Date**: 2023-03-17
**URL**: https://discourse.slicer.org/t/markups-saved-with-scalar-visibility-on-produce-warning-when-loading/28435

---

## Post #1 by @keri (2023-03-17 20:33 UTC)

<p>Hi,</p>
<p>Let’s suppose in Markups module we have set Active Scalars (PedigreeId for example) and Scalar Visibility to ON.<br>
Then we save the scene.<br>
Finally we load the scene and we can see the following warning:</p>
<pre><code class="lang-auto">[VTK] Warning: In /work/Preview/Slicer-0/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsDisplayNode.cxx, line 926
[VTK] vtkMRMLMarkupsDisplayNode (0x66db9d0): UpdateAssignedAttribute() failed: assign markupsNode before calling this method.
</code></pre>
<p>Somewhere at loading step we are trying to call <code>vtkMRMLMarkupsDisplayNode::SetScalarVisibility</code> before Markups Node is set.</p>
<p>As a result Markups is not colored after the loading.</p>
<p>Slicer 5.3.0-2023-03-16 r31679 / 106cff2</p>

---
