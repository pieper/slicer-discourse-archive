---
topic_id: 25761
title: "Export Of Sequenceregistration Output Save Each Individual T"
date: 2022-10-18
url: https://discourse.slicer.org/t/25761
---

# Export of SequenceRegistration output: save each individual transformed Model

**Topic ID**: 25761
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/export-of-sequenceregistration-output-save-each-individual-transformed-model/25761

---

## Post #1 by @scarpma (2022-10-18 15:45 UTC)

<p>Hello,</p>
<p>I run SequenceRegistration module on a 4d cardiac CT. As a result i have a sequence of transformations.</p>
<p>I apply the transformations to a segmentation node or to a surface model. How can I save these two as nrrd or VTK for each time instant of the result sequence of transformations ?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-10-19 05:28 UTC)

<p>See a code snippet that does this in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-nodes-warped-by-transform-sequence">script repository</a>.</p>

---

## Post #3 by @scarpma (2022-10-19 15:01 UTC)

<p>Wow, fantastic. Thank you very much !</p>

---
