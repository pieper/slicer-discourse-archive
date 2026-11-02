---
topic_id: 48653
title: "Help to Segment Small Intestine "
date: 2026-10-30
url: https://discourse.slicer.org/t/48653
last_bumped: 2026-11-01T19:26:05.607Z
---

# Help to Segment Small Intestine 

**Topic ID**: 48653
**Date**: 2026-10-30
**URL**: https://discourse.slicer.org/t/help-to-segment-small-intestine/48653

---

## Post #1 by @Randy_Peterson (2026-10-30 15:08 UTC)

<p>I am a Neuroendocrine cancer patient with a partial bowel obstruction in my small intestine. I have several CT scans of the area where the obstruction is located.  I want to create a 3-D model to aid in surgical planning to resolve the obstruction.  Doing this work myself is beyond my skill. I am looking for someone with the right skill and experience to create this model. Is there anyone here I could get help from? I’m willing to pay for that help.  Thanks in advance.  Email: <a href="mailto:Randypea@gmail.com">Randypea@gmail.com</a></p>

---

## Post #2 by @mau_igna_06 (2026-10-31 20:10 UTC)

<p>Learning to segment on Slicer a small structure as node manually should be quite easy. You can get other structures that are harder to segment using AI Slicer extensions. Then you can export the segmentation as 3D models.</p>
<p>How do you plan to help the doctor for the surgery by providing 3D models of your pathology?</p>

---

## Post #3 by @Randy_Peterson (2026-11-01 16:59 UTC)

<p>Thanks Mauro!</p>
<p>Having this model will help the surgeon, because it will give a more precise location of the area where there is an obstruction.  The radiologists have just said it’s somewhere in the small intestine. That covers a large area. I am also hopeful that a 3D model would give me an idea about the extent of the narrowing.</p>
<p>Have you had experience with doing this kind of segmenting?</p>

---

## Post #4 by @mau_igna_06 (2026-11-01 19:26 UTC)

<blockquote>
<p>The radiologists have just said it’s somewhere in the small intestine. That covers a large area.</p>
</blockquote>
<p>Indeed, what you say is true. Usually radiologists point out on which series and at what slice-number the lesion is, that should already help you, you can load and find the lesion on Slicer after that and start segmenting. Use as much AI segmentation as you can, you should find tutorials on youtube about Slicer AI Segmentation Extensions, how to install them and use them.</p>
<p>About recognizing bowel anatomy, I’d suggest you to take a anatomy study book like the ones doctors use for their training and make a deep dive into learning the abdomen (or pelvis if your lesion is more inferior). You should get advanced local anatomy knowledge putting around 2 weeks into it (or maybe less time using AIs to help you).</p>
<p>Try <a href="https://github.com/PerkLab/SlicerSandbox#slicey" rel="noopener nofollow ugc">Slicey</a>, it could help you use Slicer as a noobie user.</p>
<p>Surgical-planning-wise, you need to give your surgeon a measurable reference (or some other kind of actionable information otherwise all this work does not make sense). E.g. the mass is 4 cm inferior to the xyphoid process of the sternum and 6cm posterior; or 5cm to the left of the belly button and then 1cm superior, etc. Superficial bones are usually good reference sources.</p>
<p>I have myself have luck doing this for a health problem I had in the past so I think if you do the hard work it should pay-off</p>
<p>Good luck!<br>
Mauro</p>

---
