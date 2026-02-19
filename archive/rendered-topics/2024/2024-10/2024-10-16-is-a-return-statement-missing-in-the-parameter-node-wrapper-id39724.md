---
topic_id: 39724
title: "Is A Return Statement Missing In The Parameter Node Wrapper"
date: 2024-10-16
url: https://discourse.slicer.org/t/39724
---

# Is a return statement missing in the parameter node wrapper?

**Topic ID**: 39724
**Date**: 2024-10-16
**URL**: https://discourse.slicer.org/t/is-a-return-statement-missing-in-the-parameter-node-wrapper/39724

---

## Post #1 by @chir.set (2024-10-16 13:46 UTC)

<p>In python modules created using the Extension wizard, <em>_parameterNodeGuiTag</em> is always <em>None</em> on inspection. I’m wondering if this <a href="https://github.com/Slicer/Slicer/blob/ba3a9fdc04c9f4fc47cad331f9160b6d7a0beded/Base/Python/slicer/parameterNodeWrapper/wrapper.py#L253" rel="noopener nofollow ugc">line</a> should return a value. Thanks for developers’ opinion.</p>

---

## Post #2 by @chir.set (2024-10-16 15:51 UTC)

<p>I am referring to <a href="https://github.com/Slicer/Slicer/blob/ba3a9fdc04c9f4fc47cad331f9160b6d7a0beded/Utilities/Templates/Modules/Scripted/TemplateKey.py#L143" rel="noopener nofollow ugc">this</a> declaration in the scripted module template.</p>

---
