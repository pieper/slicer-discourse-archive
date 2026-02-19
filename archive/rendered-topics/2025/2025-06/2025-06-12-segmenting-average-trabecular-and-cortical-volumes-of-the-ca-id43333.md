---
topic_id: 43333
title: "Segmenting Average Trabecular And Cortical Volumes Of The Ca"
date: 2025-06-12
url: https://discourse.slicer.org/t/43333
---

# Segmenting average trabecular and cortical volumes of the calvaria

**Topic ID**: 43333
**Date**: 2025-06-12
**URL**: https://discourse.slicer.org/t/segmenting-average-trabecular-and-cortical-volumes-of-the-calvaria/43333

---

## Post #1 by @reettak (2025-06-12 18:57 UTC)

<p>Operating system: win 11<br>
Slicer version: 5.8.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I’ve found myself down a rabbit hole, and I’m looking for opinions/suggestions from more advanced users. Long story short, I would need to calculate the average trabecular and cortical bone densities of the calvaria from CT (and ZTE) images of quite many people, in order to calculate the skull density ratio. I have created the skull masks of the calvaria already, and now I’m battling what to do next. As direct thresholding cortical/trabecular does not seem accurate option, would some kind of clustering and/or bone texture analysis be suitable idea?</p>
<p>I’m not afraid some python scripts either, but I have to say I’m extremely lost in the option jungle, and I’m having hard time founding any examples and results people have gotten out of different options. I’ve tried this and that and read countles amounts of posts, but I would love to hear that has anyone actually managed to do such separation of the bone tissue types of the skull in a semi-okay manner. The resolution and image quality I have are okayish.</p>
<p>Me and my thesis would be extremely happy to hear your thoughts. Thank you for any suggestions!</p>

---

## Post #2 by @muratmaga (2025-06-12 19:23 UTC)

<aside class="quote no-group" data-username="reettak" data-post="1" data-topic="43333">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/reettak/48/80405_2.png" class="avatar"> reettak:</div>
<blockquote>
<p>calculate the average trabecular and cortical bone densities of the calvaria from CT (and ZTE) images of quite many people</p>
</blockquote>
</aside>
<p>I don’t work on bone morphometrics, so take it with a grain of salt.</p>
<p>Assuming your CT scans are not high enough resolution to see Tb, I am not sure this is something you can measure easily or even possible. Intensity only segmentation will not be sufficient (because you can’t distinguish a low intensities sufficiently clear. It can be a thin cortical bone showing partial volume effect, vs indeed part of Tb.</p>
<p>What did you find in the literature?</p>
<p>Also, what is ZTE?</p>

---

## Post #3 by @reettak (2025-06-13 08:08 UTC)

<p>Hi Murat,</p>
<p>The CT voxel sice is 0.5x0.5x0.5 so not great but not terrible, but partial volume effect is an issue here for sure. ZTE (zero echo time mri) is quite noivel MRI sequence that provides CT-like (but intensity based) images where bone structures are nicely visible, " Zero TE MRI for Craniofacial Bone Imaging" paper has some images. It’s not as good as CT, but the scans in my dataset are luckily quite nice.</p>
<p>Literature covers this topic quite well, but I’m having hard time finding anything that would be explained precisely enough for me to actually figure out what has been used.</p>
<p>Some examples about trabecular/cortical bone segmentation done in order to calculate the SDR which I eventually need: This group used a Matlab erosion algortihm, I don’t know if something similar would be available in slicer. Their dataset was a bit nicer as their patients had low SDR (=greater difference in the densities). The sdr calculation I’m using is similar to eq. 2 there : <a href="https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.612940/full" class="inline-onebox" rel="noopener nofollow ugc">Frontiers | The Distribution of Skull Score and Skull Density Ratio in Tremor Patients for MR-Guided Focused Ultrasound Thalamotomy</a></p>
<p>This group did similar thig with morphological operators (ie, connected components, opening and closing) and thresholding, also for zte images: <a href="https://onlinelibrary.wiley.com/doi/full/10.1002/jmri.26746" rel="noopener nofollow ugc">https://onlinelibrary.wiley.com/doi/full/10.1002/jmri.26746</a></p>
<p>This group also had threhoding approach (Otsu, histograms) with bunch of things I’m not too familiar with: <a href="https://iopscience.iop.org/article/10.1088/1361-6560/ab12f7/meta" class="inline-onebox" rel="noopener nofollow ugc">Radware Bot Manager Captcha</a></p>
<p>Many sources just mention that the SDR was calculated via segmentation and the basic ratio was taken, so I hope it would mean that it could be possible. Honestly, at this point anything that could create even slightly possible results is better than nothing, luckily this ain’t a PhD.</p>

---

## Post #4 by @muratmaga (2025-06-13 15:04 UTC)

<aside class="quote no-group" data-username="reettak" data-post="3" data-topic="43333">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/reettak/48/80405_2.png" class="avatar"> reettak:</div>
<blockquote>
<p>Many sources just mention that the SDR was calculated via segmentation and the basic ratio was taken, so I hope it would mean that it could be possible. Honestly, at this point anything that could create even slightly possible results is better than nothing, luckily this ain’t a PhD.</p>
</blockquote>
</aside>
<p>Well I am still not convinced that even 0.5mm is sufficient (since the Tb thickness is on the order 0.02-0.1 mm), but if people in the field is claiming that it is doable, I am not going to argue.</p>
<p>All of those functions you mentioned is available in the Slicer segment editor for you to try. However, if you can get your hands on some of these datasets (i.e., you have skulls partition into cortical and Tb), and you tryust their results, a more meaningful approach would be to train a deep-learning network to classify the bones for you.</p>
<p>Alternatively, you can try to do that manually using NNinteractive focusing on regions you know anatomically that Tb is present and see if you can manually segment to do the same without solely relying on intensities.</p>

---

## Post #5 by @reettak (2025-06-14 17:02 UTC)

<p>Thanks! Yeah I for sure agree that this seems like an impossible task to do even remotely correctly. I will for sure try the  NNinteractive option, as I have already tried all other thinkable options regarding this approach in the past two months.</p>
<p>I also thought about alternative approach to calculate the SDR, and it gave me an idea to try the intensity based method in <a href="https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.612940/full" class="inline-onebox" rel="noopener nofollow ugc">Frontiers | The Distribution of Skull Score and Skull Density Ratio in Tremor Patients for MR-Guided Focused Ultrasound Thalamotomy</a> paper (Eq. 1). I already found that Slicer can plot the intensity plot along one line with the LineProfile option. Thus, does anyone know if it’s technically possible to build a model that could measure  intensities along like 500 lines at the same time, but from different parts of the skull? This way I could extract the min and max intensities along each line and use the eq2. Here’s a not-so-fancy picture of what I’m hoping to achieve, but in 3D and with hundreds of skull points and by not needing to place each line manually (don’t mind the skull model itself, it’s a phantom, not a skull):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b4bc7bdfb3798db9c72e9c86c247530374c7fd9.png" data-download-href="/uploads/short-url/m9OmIdeFIGEdH1D9L1Z6Do909Tj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b4bc7bdfb3798db9c72e9c86c247530374c7fd9.png" alt="image" data-base62-sha1="m9OmIdeFIGEdH1D9L1Z6Do909Tj" width="611" height="251"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">611×251 19.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.</p>
<p>I’m new to slicer and it seems that either this is not possible to build a model like this with multiple lines at the same time or then I’m unable to find the correct search words for such thing.</p>

---

## Post #6 by @muratmaga (2025-06-14 20:57 UTC)

<aside class="quote no-group" data-username="reettak" data-post="5" data-topic="43333">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/reettak/48/80405_2.png" class="avatar"> reettak:</div>
<blockquote>
<p>I’m new to slicer and it seems that either this is not possible to build a model like this with multiple lines at the same time or then I’m unable to find the correct search words for such thing.</p>
</blockquote>
</aside>
<p>Did you checkout the script repository for Markups examples? I think it contains everything you need to do what propose to do:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#adding-control-points-programmatically">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#adding-control-points-programmatically" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#adding-control-points-programmatically" target="_blank" rel="noopener nofollow ugc">Script repository — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
