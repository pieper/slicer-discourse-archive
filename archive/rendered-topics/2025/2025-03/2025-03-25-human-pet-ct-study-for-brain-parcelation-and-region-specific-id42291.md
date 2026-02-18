# Human PET/CT Study for Brain Parcelation and Region-Specific PET Quantification

**Topic ID**: 42291
**Date**: 2025-03-25
**URL**: https://discourse.slicer.org/t/human-pet-ct-study-for-brain-parcelation-and-region-specific-pet-quantification/42291

---

## Post #1 by @Rafael_Pineda (2025-03-25 12:40 UTC)

<p>We are reaching out from the Physiology Department at the University of Córdoba (Spain) to seek guidance or suggestions on processing head PET/CT studies using 3D Slicer.</p>
<p>Attached below are some images showing the output when opening a folder with 3D Slicer.</p>
<p>After reviewing the available information, it appears that performing a Brain Parcellation of different brain areas would be an ideal approach. This would allow for the independent quantification of the PET signal within these regions.</p>
<p>Once these data are obtained, team members will analyze the data matrices to identify specific changes across different brain areas throughout the study. These changes will also be correlated with biochemical data and/or the final classification of subjects (patients with mild cognitive impairment) after the study.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9238429a1e7dee29d1746708950d9249e9f4ef28.png" data-download-href="/uploads/short-url/kRwflvEXyxNSU6Hz99rOGO4JmrK.png?dl=1" title="image003" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9238429a1e7dee29d1746708950d9249e9f4ef28.png" alt="image003" data-base62-sha1="kRwflvEXyxNSU6Hz99rOGO4JmrK" width="432" height="198"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image003</span><span class="informations">432×198 40.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f7e1cb6846e8c4ea1c9f4dd7fd22fa553d2ffdf.png" data-download-href="/uploads/short-url/2d3m4TNfdDZbI1phEwYyCraDb4P.png?dl=1" title="image002" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f7e1cb6846e8c4ea1c9f4dd7fd22fa553d2ffdf.png" alt="image002" data-base62-sha1="2d3m4TNfdDZbI1phEwYyCraDb4P" width="432" height="194"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image002</span><span class="informations">432×194 26.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-03-25 14:53 UTC)

<p>We don’t have it integrated directly with Slicer, but you can use SynthSeg and generally it gives very reasonable results.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSeg">
  <header class="source">

      <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSeg" target="_blank" rel="noopener">surfer.nmr.mgh.harvard.edu</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSeg" target="_blank" rel="noopener">SynthSeg - Free Surfer Wiki</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Rafael_Pineda (2025-03-25 15:08 UTC)

<p>Thank you very much Steve for your response, but SynthSeg is designed for MRI, right? Our anatomical image is a CT.</p>

---

## Post #4 by @Fernando (2025-03-25 16:48 UTC)

<p>From the link shared by <a class="mention" href="/u/pieper">@pieper</a>:</p>
<blockquote>
<p><strong>Processing CT scans</strong></p>
<p>Regarding CT scans: SynthSR does a decent job with CT ! The only caveat is that the dynamic range of CT is very different to that of MRI, so they need to be clipped to [0, 80] Hounsfield units. You can use the --ct flag to do this, as long as your image volume is in Hounsfield units. If not, you will have to clip to the Hounsfield equivalent yourself (and not use --ct).</p>
</blockquote>

---

## Post #5 by @Rafael_Pineda (2025-03-25 16:58 UTC)

<p>Thank you very much, Fernando, for your response. Please ignore the email I just sent you :-). Although I was trying to do something with 3D Slicer, since I feel more comfortable having worked with it before.</p>

---

## Post #6 by @pieper (2025-03-25 17:06 UTC)

<p>We have several examples of segmentation models that have been integrated with Slicer but not SynthSeg.  In theory it should be possible to follow existing examples and plug it in, but someone with the right experience would need to go through the process.  It would be great if someone has the bandwidth and wants to take this on (an AI coding buddy might be able to help).</p>

---

## Post #7 by @Rafael_Pineda (2025-03-26 08:52 UTC)

<p>Thank you all very much for the responses. Following some of <a class="mention" href="/u/lassoan">@lassoan</a> suggestions, we are using the <a href="https://discourse.slicer.org/t/new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation/35680">MONAIAuto3DSeg</a> extension and the AI model: “Brain and intracranial hemorrhage (ICrH)” for segment the main areas of the brain (images attached). However, it does not segment as we expected (would like); the main lobes are what we would like.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22daedc82683ef7c4dffedc5f2d35660cb306d7b.jpeg" data-download-href="/uploads/short-url/4YlhMHaebetdL9LUDTZPq9YxczV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22daedc82683ef7c4dffedc5f2d35660cb306d7b_2_690x368.jpeg" alt="image" data-base62-sha1="4YlhMHaebetdL9LUDTZPq9YxczV" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22daedc82683ef7c4dffedc5f2d35660cb306d7b_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22daedc82683ef7c4dffedc5f2d35660cb306d7b_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22daedc82683ef7c4dffedc5f2d35660cb306d7b_2_1380x736.jpeg 2x" data-dominant-color="9B99A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1655×885 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35377a91e7850a85d42936fbc0f73140bb34ce90.jpeg" data-download-href="/uploads/short-url/7AMasrHXLgEjb2ITXj0mIRBPg52.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35377a91e7850a85d42936fbc0f73140bb34ce90_2_480x500.jpeg" alt="image" data-base62-sha1="7AMasrHXLgEjb2ITXj0mIRBPg52" width="480" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35377a91e7850a85d42936fbc0f73140bb34ce90_2_480x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35377a91e7850a85d42936fbc0f73140bb34ce90.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35377a91e7850a85d42936fbc0f73140bb34ce90.jpeg 2x" data-dominant-color="EBEBEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">516×537 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecd54bc02dafe997b30014b7c1ed6c76b8dfe665.jpeg" data-download-href="/uploads/short-url/xN7FnqUZQ00MNhuZLlGtiv2sEyF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd54bc02dafe997b30014b7c1ed6c76b8dfe665_2_690x398.jpeg" alt="image" data-base62-sha1="xN7FnqUZQ00MNhuZLlGtiv2sEyF" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd54bc02dafe997b30014b7c1ed6c76b8dfe665_2_690x398.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd54bc02dafe997b30014b7c1ed6c76b8dfe665_2_1035x597.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd54bc02dafe997b30014b7c1ed6c76b8dfe665_2_1380x796.jpeg 2x" data-dominant-color="B2B1D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1547×894 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @diazandr3s (2025-03-26 13:22 UTC)

<p>Thanks for the update, <a class="mention" href="/u/rafael_pineda">@Rafael_Pineda</a>.</p>
<p>The Brain and intracranial hemorrhage (ICrH) model was trained for hemorrhage  analysis. We used corrected SynthSeg labels to train this model.</p>
<p>Would you be interested in collaborating to train a brain parcellation model using Auto3DSeg on CT images? We could also use SynthSeg labels as the GT.</p>

---

## Post #9 by @pieper (2025-03-26 13:36 UTC)

<p>Great idea <a class="mention" href="/u/diazandr3s">@diazandr3s</a> - training Auto3DSeg using SynthSeg ground truth would be very cool.  The resulting model would be more maintainable and easy to just drop into Slicer.</p>

---

## Post #10 by @Rafael_Pineda (2025-03-26 16:21 UTC)

<p>Thank you very much, Andres, for your message, but I believe my background is far from training models for 3D Slicer. We are happy to collaborate with anyone who can help us quantify PET specifically by large brain regions.</p>

---

## Post #11 by @diazandr3s (2025-04-02 04:48 UTC)

<p>I’m happy to help with the model training if you are open to collaborate on label preparation <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Let me know!</p>

---

## Post #12 by @Rafael_Pineda (2025-04-03 07:23 UTC)

<p>Thank you very much for your offer, I’m open to collaborating on label preparation.</p>

---

## Post #13 by @Rafael_Pineda (2025-05-07 09:59 UTC)

<p>An update on this:</p>
<ol>
<li>
<p>We are trying to use the BrainParcellation extension <a href="https://github.com/fepegar/SlicerParcellation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - fepegar/SlicerParcellation: 3D Slicer modules for brain segmentation using deep learning.</a> and the ROIs it generates to quantify the PET scan — see attached video.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63e64973545f31e46b34a19de369300d7023e4d2.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7354df8e47b7baab17a65551c86ac3e1166f1a9.jpeg" data-video-base62-sha1="efKEJzrVQLQTOl56cXo8Ktidgci.mp4">
  </div><p></p>
</li>
<li>
<p>We tried using Elastix <a href="https://github.com/lassoan/SlicerElastix" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerElastix: This extension makes available Elastix medical image registration toolkit (http://elastix.isi.uu.nl/) available in Slicer.</a> to register a reference atlas to the fixed PET volume. It looked promising, but we couldn’t make further progress.</p>
</li>
</ol>

---
