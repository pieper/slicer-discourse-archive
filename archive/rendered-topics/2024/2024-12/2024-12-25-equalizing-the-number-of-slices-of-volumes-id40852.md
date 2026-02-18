# Equalizing the number of slices of volumes

**Topic ID**: 40852
**Date**: 2024-12-25
**URL**: https://discourse.slicer.org/t/equalizing-the-number-of-slices-of-volumes/40852

---

## Post #1 by @OmerAfsin (2024-12-25 20:31 UTC)

<p>Hi everyone,<br>
I have some issue with interpolation. I am working on a project which aims to automatic segmentation of Aorta and Pulmonary. I got 20 different volumes from hospital but these volumes consist of different number of slices. I have tried to make them same with interpolation techniques. I decided to fix them to 319 slices in Resample Scalar/Vector/DWI Volume module’s Linear interpolation with taking one of the volumes as reference. Volumes that less than 319 slices are okay, higher ones lost information as I expected but is there any way can I specify the region of interest so that data is not harmed?</p>
<p>1-205<br>
2-319<br>
3-338<br>
4-427<br>
5-393<br>
6-305<br>
7-273<br>
8-581<br>
9-310<br>
10-319<br>
11-319<br>
12-306<br>
13-408<br>
14-212<br>
15-345<br>
16-366<br>
17-363<br>
18-382<br>
19-382<br>
20-382<br>
These are the number of slices in each volume that I have. While trying interpolation techniques (not only Linear one) I choose the 2. volume as my reference. This issue so important for me and if you have any advise or comment please don’t hesitate to share.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8255aebc2269d26c5d07fc33bf5f637719e4059c.jpeg" data-download-href="/uploads/short-url/iAZE07u1zlXBgBGTNHFa9iRzJQo.jpeg?dl=1" title="Ekran görüntüsü 2024-12-25 232724" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8255aebc2269d26c5d07fc33bf5f637719e4059c_2_690x488.jpeg" alt="Ekran görüntüsü 2024-12-25 232724" data-base62-sha1="iAZE07u1zlXBgBGTNHFa9iRzJQo" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8255aebc2269d26c5d07fc33bf5f637719e4059c_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8255aebc2269d26c5d07fc33bf5f637719e4059c_2_1035x732.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8255aebc2269d26c5d07fc33bf5f637719e4059c.jpeg 2x" data-dominant-color="64636D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2024-12-25 232724</span><span class="informations">1222×866 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af91b9a9c96efcf48c9942ec6357d86eba53bd89.jpeg" data-download-href="/uploads/short-url/p39LSs72kewgitFIcf13pSJmNzH.jpeg?dl=1" title="Ekran görüntüsü 2024-12-25 232625" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af91b9a9c96efcf48c9942ec6357d86eba53bd89_2_690x486.jpeg" alt="Ekran görüntüsü 2024-12-25 232625" data-base62-sha1="p39LSs72kewgitFIcf13pSJmNzH" width="690" height="486" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af91b9a9c96efcf48c9942ec6357d86eba53bd89_2_690x486.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af91b9a9c96efcf48c9942ec6357d86eba53bd89_2_1035x729.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af91b9a9c96efcf48c9942ec6357d86eba53bd89.jpeg 2x" data-dominant-color="51515A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2024-12-25 232625</span><span class="informations">1222×861 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for your time.</p>

---

## Post #2 by @pieper (2024-12-27 01:35 UTC)

<p>Sounds like you are on a reasonable track, but you may also want to do a rigid registration first so you at least have the anatomy lined up before cropping and resampling.</p>
<p>But also, check out the lung segmentation tools (<a href="https://github.com/Slicer/SlicerLungCTAnalyzer" class="inline-onebox">GitHub - Slicer/SlicerLungCTAnalyzer: This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in lung CT.</a> and <a href="https://discourse.slicer.org/t/new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation/35680" class="inline-onebox">New extension: MONAI Auto3DSeg - raise the bar in AI medical image segmentation</a> for example) before investing too much time in new tools.</p>
<p>If there things missing from existing tools please report back here.</p>

---

## Post #3 by @OmerAfsin (2024-12-27 01:44 UTC)

<p>Thanks for your reply sir.<br>
I will search about rigid registration. If you can suggest any source I would be grateful.</p>

---

## Post #4 by @pieper (2024-12-27 01:49 UTC)

<p>As I said, check what already exists for chest vessel segmentation first.</p>
<p>But also read about registration: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>

---
