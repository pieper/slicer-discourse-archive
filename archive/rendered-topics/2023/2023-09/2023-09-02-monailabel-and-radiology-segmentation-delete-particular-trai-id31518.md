# Monailabel and radiology/segmentation delete particular training / model

**Topic ID**: 31518
**Date**: 2023-09-02
**URL**: https://discourse.slicer.org/t/monailabel-and-radiology-segmentation-delete-particular-training-model/31518

---

## Post #1 by @Ylim (2023-09-02 12:27 UTC)

<p>Sorry if I am asking a trivial question, is there any way of either deleting a prediction model OR delete 1 training data? in the process of training?</p>
<p>My command -<br>
!monailabel start_server --app apps/radiology --studies datasets/myMODEL --conf models segmentation</p>
<p>Thanks.</p>

---

## Post #2 by @Ylim (2023-09-04 08:05 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>can you please shed some light on this? thanks.</p>

---

## Post #3 by @diazandr3s (2023-09-04 11:13 UTC)

<p>Hi <a class="mention" href="/u/ylim">@Ylim</a>,</p>
<p>Please search in the folder <strong>datasets/myMODEL</strong> for the subfolder <strong>labels/final</strong>. There you can find all the labels you used for training. You can remove the annotation from there.</p>
<p>BTW, I’d suggest you post any question/comment related to MONAI Label directly in the discussions: <a href="https://github.com/Project-MONAI/MONAILabel/discussions" class="inline-onebox" rel="noopener nofollow ugc">Project-MONAI/MONAILabel · Discussions · GitHub</a></p>
<p>There you can also find more discussions that might help you.</p>
<p>Hope this helps,</p>

---

## Post #4 by @Ylim (2023-09-04 23:21 UTC)

<p>thanks <a class="mention" href="/u/diazandr3s">@diazandr3s</a> and <a class="mention" href="/u/rbumm">@rbumm</a> for the generous advice.<br>
<a class="mention" href="/u/diazandr3s">@diazandr3s</a>, i will take note of posting the monailabel questions in the github section.</p>
<p>thanks.</p>

---
