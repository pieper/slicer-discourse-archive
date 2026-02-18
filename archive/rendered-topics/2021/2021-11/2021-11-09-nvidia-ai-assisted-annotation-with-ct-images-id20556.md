# Nvidia AI Assisted Annotation with CT images

**Topic ID**: 20556
**Date**: 2021-11-09
**URL**: https://discourse.slicer.org/t/nvidia-ai-assisted-annotation-with-ct-images/20556

---

## Post #1 by @TaraGh (2021-11-09 22:34 UTC)

<p>Hello, I have a problem in using Nvidia AI-Assisted Annotation for CT images of the head and neck. I want to segment organs at risk with this extension but if I run, I get errors like this images:<br>
(I’ have installed the 4.11 version of 3D slicer and in using this extension I select clara-pt-brain-mri-segmentation-t1c. I can’t find a model devoted to CT images)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2550d6fe295c32f01a62ebe6ba8e95c1427c568.jpeg" alt="photo_2021-11-10_01-53-28" data-base62-sha1="na3zBIEVEkZM6dMeSv52shmX1ZS" width="541" height="246"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/361f6bc6a2ef566cc331cd66df281702b4ad5c1b.png" alt="Annotation 2021-11-10 020335" data-base62-sha1="7IN6ml1QzJ3xtMxpk2QA1He6iWT" width="531" height="175"></p>
<p>I’m new to 3D slicer software, please guide me. does exist another solution in the AI-assisted method for my application?</p>

---

## Post #2 by @lassoan (2021-11-09 23:31 UTC)

<p>This model is trained on MRI images therefore it is expected to fail or return with error for CT images.</p>
<p>You can train your own models using <a href="https://github.com/Project-MONAI/MONAILabel#monai-label">MONAILabel extension</a>.</p>
<p>What structures would you like to segment?</p>

---

## Post #3 by @TaraGh (2021-11-10 08:05 UTC)

<p>Thank you a lot.<br>
I want to segment organs at risk from these CT images, such as left/right eye, lens, optic nerve, optic chiasm, pituitary … overall about 17 structures.</p>

---

## Post #4 by @lassoan (2021-11-10 19:03 UTC)

<p>I’m not aware of a publicly available model exist for such a comprehensive segmentation task, but you can ask the <a href="https://monai.io/community.html">MONAI community</a> if they know about something like this or get advice for how to create it yourself.</p>

---

## Post #5 by @TaraGh (2021-11-10 20:56 UTC)

<p>fine, I’ll do it.</p>
<p>Thanks for the helpful advice.</p>

---
