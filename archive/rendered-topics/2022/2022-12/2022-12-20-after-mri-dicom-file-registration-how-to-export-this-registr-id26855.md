---
topic_id: 26855
title: "After Mri Dicom File Registration How To Export This Registr"
date: 2022-12-20
url: https://discourse.slicer.org/t/26855
---

# After MRI Dicom file registration ... How to export this registration file in DICOM format

**Topic ID**: 26855
**Date**: 2022-12-20
**URL**: https://discourse.slicer.org/t/after-mri-dicom-file-registration-how-to-export-this-registration-file-in-dicom-format/26855

---

## Post #1 by @mahmoud (2022-12-20 17:35 UTC)

<p>Hello <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=12" title=":wave:" class="emoji" alt=":wave:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=12" title=":wave:" class="emoji" alt=":wave:" loading="lazy" width="20" height="20"><br>
Please, can help me to how export DICOM format after the two mri sequence Images registration.</p>
<p>I mean in my question<br>
I want to get Dicom new registration images separately from move and fix image …to help with the clinical process</p>

---

## Post #2 by @lassoan (2022-12-20 18:40 UTC)

<p>DICOM spatial registration object export is provided by SlicerRT extension. It supports both rigid and deformable transforms.</p>
<p>You can right-click on the transform in <code>Data</code> module, verify that the export type is <code>REG...</code> and choose <code>Export to DICOM</code> then click Export.</p>
<p>If <code>REG...</code> export type is not offered then the registration tool that you used did not set the fixed and moving image reference. You can do this by copying these few lines into the Python console (update the node names according to actual volume and transform node names in your scene):</p>
<pre><code class="lang-python">transform = getNode('Transform')
fixedVolume = getNode('MRBrainTumor1')
movingVolume = getNode('MRBrainTumor2')
transform.SetNodeReferenceID(transform.GetMovingNodeReferenceRole(), movingVolume.GetID())
transform.SetNodeReferenceID(transform.GetFixedNodeReferenceRole(), fixedVolume.GetID())
</code></pre>
<p>All this is a bit clunky, but the need for DICOM spatial registration object so rarely comes up that we did not spend much time making this feature more convenient.</p>

---
