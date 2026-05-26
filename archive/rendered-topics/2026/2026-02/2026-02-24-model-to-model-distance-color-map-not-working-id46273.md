---
topic_id: 46273
title: "Model to Model Distance Color Map Not working"
date: 2026-02-24
url: https://discourse.slicer.org/t/46273
last_bumped: 2026-02-26T10:59:09.175Z
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

## Post #2 by @drnoorfatima (2026-02-25 09:39 UTC)

<p>Hi!</p>
<p>I can see exactly where the workflow is breaking down, the transform is being applied to the wrong model at step 5, which is why your model-to-model distance isn’t working. The registration logic needs a small but specific correction and your color map comparison will work perfectly.</p>
<p>I work in medical imaging research with a focus on surgical outcome analysis. This is actually a really elegant application for cleft outcome measurement.</p>
<p>Happy to help get this working, feel free to DM me to discuss further.</p>
<p>Noor</p>

---

## Post #3 by @Nacole (2026-02-25 18:46 UTC)

<p>Hi Noor! Thank you so much for the reply and I appreciate the compliment. I would love to figure out how to get this working. I’m not sure how to DM on this interface, but if you know how and prefer to speak there please send a message!</p>

---

## Post #5 by @drnoorfatima (2026-02-26 10:59 UTC)

<p>Hi Nacole,<br>
I sent you a dm.<br>
Also you can reach me here: <a href="mailto:noorfatimacheema249@gmail.com">noorfatimacheema249@gmail.com</a></p>

---
