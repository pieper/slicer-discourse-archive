# New extension: ModalityConverter - bringing AI medical image-to-image translation to 3D Slicer

**Topic ID**: 44405
**Date**: 2025-09-09
**URL**: https://discourse.slicer.org/t/new-extension-modalityconverter-bringing-ai-medical-image-to-image-translation-to-3d-slicer/44405

---

## Post #1 by @ciro.raggio (2025-09-09 13:14 UTC)

<p><strong>ModalityConverter</strong> is officially available in the 3D Slicer Extensions Index, under the Image Synthesis category (from version 5.9.0)!</p>
<p>The extension makes medical image-to-image translation AI models freely and easily accessible in 3D Slicer. It already includes 3 ready-to-use models for brain T1w MRI-to-CT translation, recently introduced in the <a href="https://doi.org/10.1016/j.compbiomed.2025.110160" rel="noopener nofollow ugc">FedSynthCT-Brain</a> article.</p>
<p>We are looking forward to community contributions — if you would like to integrate new models for other modalities (MRI-MRI, CBCT-CT, PET-CT), please propose them via the <a href="https://github.com/ciroraggio/SlicerModalityConverter" rel="noopener nofollow ugc">GitHub repository</a>!</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/pushpin.png?v=14" title=":pushpin:" class="emoji" alt=":pushpin:" loading="lazy" width="20" height="20"> Useful links:</p>
<ul>
<li><img src="https://emoji.discourse-cdn.com/twitter/open_book.png?v=14" title=":open_book:" class="emoji" alt=":open_book:" loading="lazy" width="20" height="20"> <a href="https://github.com/ciroraggio/SlicerModalityConverter#how-to-use" rel="noopener nofollow ugc">How to use the extension</a></li>
<li><img src="https://emoji.discourse-cdn.com/twitter/gear.png?v=14" title=":gear:" class="emoji" alt=":gear:" loading="lazy" width="20" height="20"> <a href="https://github.com/ciroraggio/SlicerModalityConverter#how-to-integrate-a-custom-model" rel="noopener nofollow ugc">How to integrate a custom model</a></li>
<li><img src="https://emoji.discourse-cdn.com/twitter/handshake.png?v=14" title=":handshake:" class="emoji" alt=":handshake:" loading="lazy" width="20" height="20"> <a href="https://github.com/ciroraggio/SlicerModalityConverter#how-to-contribute" rel="noopener nofollow ugc">How to contribute</a></li>
</ul>
<p>Example of synthetic CT generation from the Slicer MRHead sample:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf6bb918fb5ef3181fbffaddf746ba13280097a.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da70502169f02d7451fd72c13c6638060cf09893.jpeg" data-video-base62-sha1="sXv4qo1nauILsnfnWweBkCm3NMe.mp4">
  </div><p></p>

---

## Post #2 by @Mohammed_Alshakhas1 (2025-09-09 13:36 UTC)

<p>Are you saying we can synthesize ct from MRI ?</p>
<p>Is it applicable to all MRis ? Like Tmj mri</p>
<p>How accurate is  it  ?</p>

---

## Post #3 by @ciro.raggio (2025-09-09 14:49 UTC)

<blockquote>
<p>Are you saying we can synthesize ct from MRI ?</p>
</blockquote>
<p>Yes, this has been possible for a few years—not only from MRI, but also from CBCT and PET <sup class="footnote-ref"><a href="#footnote-128320-1" id="footnote-ref-128320-1">[1]</a></sup>, <sup class="footnote-ref"><a href="#footnote-128320-2" id="footnote-ref-128320-2">[2]</a></sup>, <sup class="footnote-ref"><a href="#footnote-128320-3" id="footnote-ref-128320-3">[3]</a></sup>.</p>
<blockquote>
<p>Is it applicable to all MRis ? Like Tmj mri</p>
</blockquote>
<p>Currently, the extension includes 3 models from the FedSynthCT-Brain study <sup class="footnote-ref"><a href="#footnote-128320-4" id="footnote-ref-128320-4">[4]</a></sup>, which can generate synthetic CTs from T1w brain MRIs.</p>
<p>New models would need to be trained specifically for other regions, such as the TMJ. We hope to include new models with community contributions in the future.</p>
<blockquote>
<p>How accurate is it ?</p>
</blockquote>
<p>Accuracy depends on several factors, especially the quality and amount of training data. Deep learning models generally demonstrated satisfactory performance for image translation tasks.</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-128320-1" class="footnote-item"><p>Spadea, M. F. et al., Deep learning based synthetic-CT generation in radiotherapy and PET: A review, Medical Physics, Volume 48, 2021, <a href="https://doi.org/10.1002/mp.15150" rel="noopener nofollow ugc">https://doi.org/10.1002/mp.15150</a> <a href="#footnote-ref-128320-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-128320-2" class="footnote-item"><p>Sanuwani D. et al., Deep learning based synthesis of MRI, CT and PET: Review and analysis, Medical Image Analysis, Volume 92, 2024, <a href="https://doi.org/10.1016/j.media.2023.103046" class="inline-onebox" rel="noopener nofollow ugc">Redirecting</a> <a href="#footnote-ref-128320-2" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-128320-3" class="footnote-item"><p>Bahloul, M. A. et al., Advancements in synthetic CT generation from MRI: A review of techniques, and trends in radiation therapy planning, Journal of Applied Clinical Medical Physics, 2024, <a href="https://doi.org/10.1002/acm2.14499" rel="noopener nofollow ugc">https://doi.org/10.1002/acm2.14499</a> <a href="#footnote-ref-128320-3" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-128320-4" class="footnote-item"><p>Raggio C. B. et al., FedSynthCT-Brain: A federated learning framework for multi-institutional brain MRI-to-CT synthesis, Computers in Biology and Medicine, Volume 192, Part A, 2025, <a href="https://doi.org/10.1016/j.compbiomed.2025.110160" class="inline-onebox" rel="noopener nofollow ugc">Redirecting</a> <a href="#footnote-ref-128320-4" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #4 by @rbumm (2025-09-09 16:25 UTC)

<p>This is a great result!</p>

---

## Post #5 by @mohammed_alshakhas (2025-09-09 16:57 UTC)

<p>i hope there is serious consideration for TMJ MRI . i routinely request both images for patient and the ability to generate ct from mri would mean big for my patients</p>

---

## Post #6 by @mikebind (2025-09-10 15:21 UTC)

<p>Please be aware that image “translation” really means image synthesis.  The newly created image is the model’s best guess as to what the corresponding image in another modality would look like, based on what the given image looks like. For clinical use purposes, such synthetic images should be used only with extreme caution.  Clinically, imaging is typically acquired to look for the presence of ABNORMAL features.  Usually, image synthesis models will have seen predominantly, or sometimes only, NORMAL features.  So, when guessing what the translated image should look like, a well-trained model is likely to guess something that looks roughly normal, even if a clinical image in the target modality would clearly show abnormality.</p>
<p>If you typically acquire both a CT and an MRI to evaluate a condition, it is likely because there are distinct abnormal features which are best seen on each modality.   It is generally not safe to assume that an image translation would be able to generate the abnormality you are looking for based only on the image from the other modality.</p>

---

## Post #7 by @muratmaga (2025-09-10 16:04 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="6" data-topic="44405">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>. Clinically, imaging is typically acquired to look for the presence of ABNORMAL features. Usually, image synthesis models will have seen predominantly, or sometimes only, NORMAL features.</p>
</blockquote>
</aside>
<p>I don’t think this is meant to replace diagnostic imaging. One potential use I can think of is the study of normative population of growing children, where you can not justify exposing them to ionizing radiation (and repetitively if it is a longitudinal study) just for the sake of research data. MRI to CT would be costly but possible.</p>
<aside class="quote no-group" data-username="mikebind" data-post="6" data-topic="44405">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>sually, image synthesis models will have seen predominantly, or sometimes only, NORMAL features.</p>
</blockquote>
</aside>
<p>I am not familiar with this, but I think it depends on the how the model is trained. In MR, the bone is dark, but it is still there as a void. So if you have an abnormality, depending on how it is shaped, it is likely going to affect the shape of the void is as well. So if the model is learning how to convert the void to CT from the existing CT (as opposed to learning what a normal CT looks like), then it should reconstruct the abnormality to some extend. Of course it cannot reconstruct what’s going on inside the bone accurately.</p>
<p>I still don’t think you can replace the diagnostic data with synthetic ones, particularly for treatment planning, but I see quite a potential for growing kids when the care team orders evaluation exams for surgery followups. Kids with craniofacial conditions would get 3-4 CTs, and even potential to replace a couple is a welcome prospect.</p>

---

## Post #8 by @mikebind (2025-09-10 17:21 UTC)

<p>Don’t get me wrong, these models are both very cool and very useful for many purposes, and it is fabulous that this new extension is making them easily usable in Slicer!  I just wanted to inject a note of caution that would be seen by clinicians who may be less familiar with the technology and who might assume that a translated image is more or less equivalent to an acquired image, making the extra diagnostic acquisition unnecessary. There may be use cases where that will likely be OK (like bone shape from void shape on MR as you suggest), but there are also use cases where that will likely not be OK, and clinicians (and researchers) need to consider and test carefully for whatever application they are considering.</p>

---

## Post #9 by @mohammed_alshakhas (2025-09-11 03:15 UTC)

<p>The thing is that MRI captures all information needed . So I would think that a very good model would be able to 80ish percent accurate . If that is correct , it would be good enough.</p>
<p>The two great things is that I can use it as way to visualize bone morphology not quality . Quality is already being seen in MRi . But 3d shape is illusive , required bit of imagination and lots of experience to guess from mri .</p>
<p>The second is that bone will be perfectly registered on MRi . And that has big potential for me . Not sure what but I’m thinking it might be diagnostically significant</p>
<p>a would also hope that someone can work on MRI ct registration .</p>

---

## Post #10 by @manjula (2025-09-11 13:12 UTC)

<p>Nice Work. Thank you</p>

---
