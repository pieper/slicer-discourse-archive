# Cortical vs Trabecular Bone Segmentation

**Topic ID**: 13406
**Date**: 2020-09-09
**URL**: https://discourse.slicer.org/t/cortical-vs-trabecular-bone-segmentation/13406

---

## Post #1 by @Shreya_Chakraborty (2020-09-09 18:51 UTC)

<p>Hi<br>
I am relatively new to 3DSlicer and have been finding the software extremely useful! This might seem like a stupid question, but is there a way to differentiate cortical and trabecular bones from CT scans? The easiest one I could think of was Thresholding, but is it the most accurate I can get with the software?</p>

---

## Post #2 by @lassoan (2020-09-09 19:40 UTC)

<p>It depends on what is the voxel size (also known as spacing, or resolution) of your images. You can directly see the actual bone structure on a microCT but you only get average bone density on an average clinical CT.</p>

---

## Post #3 by @muratmaga (2020-09-09 22:18 UTC)

<p>I might be off, but I think <a class="mention" href="/u/shreya_chakraborty">@Shreya_Chakraborty</a> wants to know if it is somehow possible to select only Tb but not  cortical with a method like threshold. As far as I know, there is not a density difference in the mineral that make up Tb vs cortical bone. So in terms of attenuation, they have probably very similar values. While higher resolution will let you see the microstructure more clearly, I am not sure if it will help isolating Tb and cortical bone, particularly in areas where they (e.g., epiphysis) where they gradually blend into each other.</p>
<p>I am also curious, It would be good to hear from people who does bone morphometrics regularly (i don’t).</p>

---

## Post #4 by @pieper (2020-09-10 00:12 UTC)

<p>You might be able to threshold the outputs of one of these texture metrics to do the segmentation.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/BoneTextureExtension" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/BoneTextureExtension</a></p>

---

## Post #5 by @Shreya_Chakraborty (2020-09-10 00:37 UTC)

<p>I am not working with microCT unfortunately but with clinical CT. As <a class="mention" href="/u/muratmaga">@muratmaga</a> pointed out, I can probably do a very rough thresholding but it does not give me an accurate segmentation. Although the HU values seem to have a fair difference as per Wikipedia, I don’t think a naive thresholding is an elegant solution.</p>

---

## Post #6 by @lassoan (2020-09-10 01:46 UTC)

<p>Thresholding is a clear, reproducible tool for clinical CTs, as trabecular bone ends up showing up with lower intensity voxel values due to partial volume effect (because in trabecular bone, ratio of high-density bone and lower-density cavities is lower). You may even apply slight blurring to make ensure sufficient averaging.</p>
<p>Texture features (and various radiomics features in general) may be more sensitive and may be able to distinguish between more tissue types. However, results may depend on implementation of the features and various imaging parameters.</p>
<p>Of course the “state-of-the-art” solution nowadays would be to ask experts to manually/semi-automatically segment a few hundred (or thousand?) images and use the results to train a neural network. The network would figure out what features (intensity, texture, etc.) can be used for distinguishing the different bone types and how.</p>

---
