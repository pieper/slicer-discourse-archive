---
topic_id: 31175
title: "Alpaca Tps Transform Matrix"
date: 2023-08-16
url: https://discourse.slicer.org/t/31175
---

# ALPACA - TPS Transform Matrix

**Topic ID**: 31175
**Date**: 2023-08-16
**URL**: https://discourse.slicer.org/t/alpaca-tps-transform-matrix/31175

---

## Post #1 by @Vignesh_Chakravarthy (2023-08-16 15:42 UTC)

<p>Hi,</p>
<p>It would be really helpful if the ALPACA module can also provide TPS transform matrix as output after running the module (similar to rigid transformation matrix). It will provide more insights on understanding the deformation vector field. Please let me know the changes needs to be incorporated to get “TPS transform matrix” as output after running ALPACA module.</p>
<p>Regards,<br>
Vignesh</p>

---

## Post #2 by @muratmaga (2023-08-16 16:41 UTC)

<p><a class="mention" href="/u/vignesh_chakravarthy">@Vignesh_Chakravarthy</a> ALPACA is not a registration tool, and to transfer landmarks from one model to the next. That TPS transform is only approximate and the whole purpose is to provide a fast visualization of where the landmarks will be. See this long thread about it. <a href="https://discourse.slicer.org/t/increasing-alpaca-non-rigid-alignment/28906/13">Increasing ALPACA Non-Rigid Alignment - Support - 3D Slicer Community</a></p>
<p>If your goal is to do the model registration, use FastModelAlign, however, we don’t currently have deformable registration implemented in it. It is not much work, but we don’t have time or people right now.</p>

---

## Post #3 by @Vignesh_Chakravarthy (2023-08-16 17:29 UTC)

<p>Hi Murat,</p>
<p>Thank you very much for your immediate response.</p>
<p>Regards,<br>
Vignesh</p>

---
