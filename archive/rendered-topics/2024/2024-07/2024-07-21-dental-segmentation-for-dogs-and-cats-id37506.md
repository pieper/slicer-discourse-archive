# Dental segmentation for dogs and cats

**Topic ID**: 37506
**Date**: 2024-07-21
**URL**: https://discourse.slicer.org/t/dental-segmentation-for-dogs-and-cats/37506

---

## Post #1 by @Charlie_Tewson (2024-07-21 15:05 UTC)

<p>Hi</p>
<p>This tool looks extremely useful, thank you for your work on it. I am a veterinary dentist interested in the applications for dogs and cats. I tried running it on a dog skull CT and it only managed to identify a few teeth. Out of curiosity, is it likely to be a lot of work to adapt this model to a completely different dental formula and skull shape?</p>
<p>Kind regards<br>
Charlie Tewson<br>
Veterinary Dentistry Resident</p>

---

## Post #2 by @Gauthier (2024-07-22 11:29 UTC)

<p>Dear Charlie</p>
<p>Thank you for your interest. Such an adaptation would probably require a fair amount of properly annotated data (manually corrected segmentations) of dogs &amp; cats CT, in order to train a model dedicated to this task.</p>
<p>It’s quite difficult to tell you how many scans would be necessary, depending on the difficulty of the task (metal artifacts? highly variable anatomy? different CT protocols? …). To give you an idea, we have trained our model with 470 CT/CBCT scans but some papers show great results with less scans, while other use more data…</p>
<p>Best<br>
Gauthier</p>

---

## Post #3 by @Charlie_Tewson (2024-07-23 14:54 UTC)

<p>Dear Gauthier</p>
<p>Thank you for the information. The anatomy would be extremely variable for different skull types for different breeds, particularly compared to how similar human skulls are! This might be an interesting project in the future, but it is beyond my availability at the moment to fully manually segment and train a model :). Perhaps if another Veterinary Dental Resident is reading this and wants a research project…</p>
<p>Kind regards<br>
Charlie Tewson</p>

---

## Post #4 by @lassoan (2024-07-23 16:39 UTC)

<p>FYI, if somebody wants to do this work, data set that could be used for training is already available. Images of Hundreds of canine (and a handful of other animal) skulls are shared with permissive (CC-BY) license in this <a href="https://www.nature.com/articles/s41597-024-03572-x">recent paper by Czeibert et al. (2024)</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf87dc7d3ace47bc128ccc16ace58538f6624d92.jpeg" data-download-href="/uploads/short-url/rkmhfR25myfOqtkwxb76e0y9U9I.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf87dc7d3ace47bc128ccc16ace58538f6624d92_2_690x357.jpeg" alt="image" data-base62-sha1="rkmhfR25myfOqtkwxb76e0y9U9I" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf87dc7d3ace47bc128ccc16ace58538f6624d92_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf87dc7d3ace47bc128ccc16ace58538f6624d92.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf87dc7d3ace47bc128ccc16ace58538f6624d92.jpeg 2x" data-dominant-color="413731"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">734×380 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @mau_igna_06 (2024-07-23 18:08 UTC)

<p>If I understood correctly those CTs are from “dog” skulls that are not surrounded by soft-tissue. Would that affect the trained model inferences for alive “dogs”?</p>

---

## Post #6 by @lassoan (2024-07-23 18:12 UTC)

<p>Soft tissues can be largely removed by simple global thresholding, so the data set should be usable for training bone and teeth segmentation.</p>

---

## Post #7 by @mau_igna_06 (2024-07-23 18:17 UTC)

<p>Do you mean I could do the same for fibula CTs from a bone bank?</p>

---

## Post #8 by @lassoan (2024-07-23 18:21 UTC)

<p>Probably yes, especially if you are only interested in bone (not cartilage, supplying blood vessels, etc.).</p>

---

## Post #9 by @Charlie_Tewson (2024-07-23 19:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="37506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>r training bone and teeth seg</p>
</blockquote>
</aside>
<p>That is a super useful paper! Thank you.</p>
<p>Thoughts on the use of skulls (without soft tissue) for data training in live patients: The periodontal ligament will likely have been disturbed by the processing when the skull was created (sometimes the teeth need to be superglued back in), which might slightly affect a computer model’s training, but perhaps not…</p>

---
