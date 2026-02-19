---
topic_id: 22782
title: "Fused Volume Rendered Images Do Not Rotate In Synchrony Seem"
date: 2022-03-31
url: https://discourse.slicer.org/t/22782
---

# Fused volume rendered images do not rotate in synchrony, seemingly don't reflect reality

**Topic ID**: 22782
**Date**: 2022-03-31
**URL**: https://discourse.slicer.org/t/fused-volume-rendered-images-do-not-rotate-in-synchrony-seemingly-dont-reflect-reality/22782

---

## Post #1 by @maxaerosat.co.za (2022-03-31 19:56 UTC)

<p>i managed to fuse a ct to a spect image and display the resultant fused image  as a 3d volume .<br>
however if i rotate the fused image it appears asif it does not reflect reality , asif they still behave as seperate volmes ,(do not move in sync) i have "closed the chain rings " but it still appears something is lacking ,<br>
ie - i know the spect focus is in the spine - so if the other volume(ct) has opacity set to 1 i should not see the spect focus in the spine  - looking from the front , or if i know it is on the right it should not show if i look from the left - would appreciate some assistance</p>

---

## Post #2 by @lassoan (2022-03-31 22:50 UTC)

<p>You need to use the experimental multi-volume rendering feature for this. It has some <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html#limitations">limitations</a>. If those limitations are unacceptable for you then you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one">combine your volumes into one</a> volume and then render it as a single volume.</p>

---
