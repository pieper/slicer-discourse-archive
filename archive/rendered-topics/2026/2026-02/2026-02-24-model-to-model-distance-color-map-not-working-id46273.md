---
topic_id: 46273
title: "Model To Model Distance Color Map Not Working"
date: 2026-02-24
url: https://discourse.slicer.org/t/46273
---

# Model to Model Distance Color Map Not working

**Topic ID**: 46273
**Date**: 2026-02-24
**URL**: https://discourse.slicer.org/t/model-to-model-distance-color-map-not-working/46273

---

## Post #1 by @Nacole (2026-02-24 13:23 UTC)

<p>Hi there, I am hoping to get some help with an issue. My goal is calculate the post op changes after bone grafting to the alveolus in cleft patients. I am having this issue.</p>
<ol>
<li>Import Pre op DICOMs–&gt; dental segmentor –&gt; Maxilla and Upper Teeth selected –&gt; Merge Models –&gt; export to VTK, STL and PLY (save all on desktop)</li>
<li>Repeat steps for post op DICOM</li>
<li>Now I have 2 VTKs that I can “register” to align the two</li>
<li>Surface registration –&gt; Fixed Pre Op, Movable Post Op, Output Transform (create new Transform as S.Registration) –&gt; Compute</li>
<li>Click undo, then select the output model I want to apply the transform to (fixed pre op), fort output transform the selection is none</li>
<li>Then overlayed model is displaced and I save the color map</li>
<li>Then I go to model-to-model distance</li>
<li>From here the overlayed map is not shown, only either the pre or post op model which I cannot calculate any difference between.</li>
</ol>
<p>I followed this link for the surface registration (<a href="https://www.youtube.com/watch?v=hsZrjNsXZbs" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=hsZrjNsXZbs</a>)</p>
<p>What am I doing wrong? Is there a way I can just upload the 2 VTK files from step 3 and go straight to model-to-model calculation?</p>
<p>Thanks!</p>

---
