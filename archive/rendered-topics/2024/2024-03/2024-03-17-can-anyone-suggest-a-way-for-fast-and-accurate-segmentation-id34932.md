# Can anyone suggest a way for fast and accurate segmentation of teeth in CBCT volumes?

**Topic ID**: 34932
**Date**: 2024-03-17
**URL**: https://discourse.slicer.org/t/can-anyone-suggest-a-way-for-fast-and-accurate-segmentation-of-teeth-in-cbct-volumes/34932

---

## Post #1 by @Sourav_Bose (2024-03-17 00:04 UTC)

<p>I have been trying to do the segmentation of teeth using fill between slices in the  CBCTs.<br>
I tried a few different techniques mentioned in the forum but I am unable to add seeds on the margins of the tooth. So there is spillage of the the label in the adjacent bone and tooth, when I am using Watershed.</p>
<p>Kindly help me with this!</p>

---

## Post #2 by @mau_igna_06 (2024-03-17 00:11 UTC)

<p>You can try <a href="https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools#slicer-automated-dental-tools" rel="noopener nofollow ugc">Slicer Automated Dental Tools Extension</a> if you have a decent graphics card</p>

---

## Post #3 by @Sourav_Bose (2024-03-17 06:23 UTC)

<p>I want to create individual segment for each tooth. Without the adjacent bone (maxilla and mandible).<br>
I have run the extension suggested by you, but it comes with the bony structures</p>

---

## Post #4 by @lassoan (2024-04-10 06:18 UTC)

<p>You can use <a href="https://github.com/gaudot/SlicerDentalSegmentator">DentalSegmentator extension</a> to get the teeth.</p>
<p>                    <a href="https://raw.githubusercontent.com/gaudot/SlicerDentalSegmentator/main/Screenshots/1.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/gaudot/SlicerDentalSegmentator/main/Screenshots/1.png" width="690" height="431">
          </a>

</p>
<p>                    <a href="https://raw.githubusercontent.com/gaudot/SlicerDentalSegmentator/main/Screenshots/dentalsegmentator_example.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/gaudot/SlicerDentalSegmentator/main/Screenshots/dentalsegmentator_example.png" width="690" height="499">
          </a>

</p>
<p>The upper and lower teeth are already separated and you can split the individual teeth using semi-automatic tools in Segment Editor (Islands effect and Scissors).</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> may have more experience in automatic separation of teeth from each other.</p>

---

## Post #5 by @cpinter (2024-04-10 08:55 UTC)

<p>We have a MONAI Label based model pair for segmenting the teeth but unfortunately it’s proprietary. We are in the process of deciding what could be shared publically (mentioning <a class="mention" href="/u/diazandr3s">@diazandr3s</a> and <a class="mention" href="/u/palkod">@PalkoD</a> here as well).</p>

---

## Post #6 by @Sourav_Bose (2024-04-10 13:01 UTC)

<p>Thank you Prof.<br>
But I am unable to add the extension in my Mac from the extension manager or manually as mentioned in the page.<br>
What could be a possible way out?</p>

---

## Post #7 by @lassoan (2024-04-10 19:20 UTC)

<p>You can use <a href="https://github.com/KitwareMedical/SlicerNNUnet">nnUnet extension</a> today (follow instructions in the tutorial) or you can use DentalSegmentator from tomorrow. It will be released in the latest Slicer Preview Release (that you download tomorrow or later).</p>

---

## Post #8 by @dimnsk (2024-05-16 17:39 UTC)

<p>is there any news on your models?<br>
can I see them in public?</p>

---

## Post #9 by @r_dientes (2024-10-21 17:27 UTC)

<p>Hello!<br>
I’m starting to segment and I wanted to know if there was a tool or extension to separately segment enamel, dentin and pulp canal. Or if not some advice or tip that I should follow. Thank you!</p>

---

## Post #11 by @lassoan (2024-10-21 18:48 UTC)

<p>DentalSegmentator Slicer extension can segment teeth. There is no Slicer extension yet for for segmenting an individual tooth or parts of it, but it is just a matter of time.</p>
<p>Please search the web for any public data sets and pre-trained models (there are many of them) and if you find one that seem to match what you need and it uses a permissive license then let us know and we’ll help making it conveniently available in Slicer as an extension.</p>

---

## Post #12 by @r_dientes (2024-10-21 19:27 UTC)

<p>Thanks for your comments!<br>
My doubt arises from my still little experience and that I have Micro-CT images that are quite heavy for my computer. For this reason, I need to lower the quality of the images but then be able to distinguish the structures well to be able to segment. Any recommendations? I leave you a screenshot of my work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0.jpeg" data-download-href="/uploads/short-url/h5IlKdhm0yDsO8WtXJCCy6Mpeb6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0_2_690x366.jpeg" alt="image" data-base62-sha1="h5IlKdhm0yDsO8WtXJCCy6Mpeb6" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0_2_1380x732.jpeg 2x" data-dominant-color="8F8F94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1020 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2024-10-21 20:12 UTC)

<p>Tooth segmentation on non-clinical images is an entirely different story. MicroCT has a magnitude finer resolution and its image quality can be much better due to that there are no dose concerns and there is less scattering. Any models that are trained for tooth segmentation in clinical CBCT will not work on high-resolution microCT and vice versa, so if you want to discuss microCT tooth segmentation further then please create a new forum topic for it.</p>

---
