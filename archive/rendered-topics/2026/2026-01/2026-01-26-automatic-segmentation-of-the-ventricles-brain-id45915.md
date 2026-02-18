# Automatic segmentation of the ventricles (brain)

**Topic ID**: 45915
**Date**: 2026-01-26
**URL**: https://discourse.slicer.org/t/automatic-segmentation-of-the-ventricles-brain/45915

---

## Post #1 by @Preetham_Dange (2026-01-26 10:34 UTC)

<p>Hello everyone,</p>
<p>I am currently working on hydrocephalus . I wanted to automatically segment the ventricles (brain) and use the volume statistics for research purposes. I tried MONAI Auto3Dseg and nnUnet but I couldn’t find any specific module for ventricles . Can anyone please help me with this</p>
<p>Thanks in advance</p>
<p>Regards,</p>
<p>Preetham S.D.</p>
<p>Fellow in pediatric neurosurgery, Amrita institute, Kochi,India</p>

---

## Post #2 by @muratmaga (2026-01-27 01:50 UTC)

<p>I don’t think there is any model specific to the ventricles, but are probably many brain segmentation models that do provide ventricles as part of the output.</p>
<p>Having said that, I highly encourage you to try the [NNInteractive extension](<a href="https://github.com/coendevente/SlicerNNInteractive" class="inline-onebox" rel="noopener nofollow ugc">GitHub - coendevente/SlicerNNInteractive: A 3D Slicer extension for efficient segmentation with nnInteractive.</a>). It is very simple prompt based AI-segmentation tool. It will probably work very well in your case.</p>

---

## Post #3 by @drnoorfatima (2026-02-17 09:35 UTC)

<p>Hi Preetham,</p>
<p>Great research focus, ventricular segmentation in hydrocephalus is a genuinely tricky problem because the enlarged, irregular ventricles fall outside the training distribution of most standard models including the ones you’ve tried. That’s not a user error, it’s a fundamental limitation of those pipelines for this pathology.</p>
<p>Getting volumetric statistics that are accurate and reproducible enough for research purposes requires a more targeted approach.</p>
<p>I work with medical image segmentation and have a clinical background in neurology, so this kind of problem is something I can help with properly. DM me and we can talk through your data and what you need.</p>

---

## Post #4 by @Preetham_Dange (2026-02-17 15:36 UTC)

<p>Thanks for your suggestion Muratmaga. I tried NNinteractive. I couldn’t get it working as it required me to do a lot in the terminal. I am a non technical person and have zero coding knowledge. Thanks again for the help.</p>

---

## Post #5 by @Preetham_Dange (2026-02-17 15:37 UTC)

<p>Thanks lollypoppink, I will DM you</p>

---
