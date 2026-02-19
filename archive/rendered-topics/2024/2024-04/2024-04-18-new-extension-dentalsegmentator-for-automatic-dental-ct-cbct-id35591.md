---
topic_id: 35591
title: "New Extension Dentalsegmentator For Automatic Dental Ct Cbct"
date: 2024-04-18
url: https://discourse.slicer.org/t/35591
---

# New extension: DentalSegmentator for automatic dental CT & CBCT segmentation

**Topic ID**: 35591
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/new-extension-dentalsegmentator-for-automatic-dental-ct-cbct-segmentation/35591

---

## Post #1 by @Gauthier (2024-04-18 11:31 UTC)

<p>Dear All,</p>
<p>We are glad to announce the availability of <strong>DentalSegmentator</strong>, <a href="https://github.com/gaudot/SlicerDentalSegmentator" rel="noopener nofollow ugc">a new 3D Slicer extension for automatic segmentation of dental CT and CBCT scans</a>. It is now available in the latest Slicer 5.7.0 preview release.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31a016c36678715d2a934dd4a2673430e005a8bc.jpeg" data-download-href="/uploads/short-url/750nRRkZGfY7oEkYjuYMZ2zSXSY.jpeg?dl=1" title="Fig4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31a016c36678715d2a934dd4a2673430e005a8bc_2_690x431.jpeg" alt="Fig4" data-base62-sha1="750nRRkZGfY7oEkYjuYMZ2zSXSY" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31a016c36678715d2a934dd4a2673430e005a8bc_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31a016c36678715d2a934dd4a2673430e005a8bc_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31a016c36678715d2a934dd4a2673430e005a8bc_2_1380x862.jpeg 2x" data-dominant-color="BEBBB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig4</span><span class="informations">1920×1202 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This tool is based on a nnU-Net model trained and evaluated on more than 700 CT and CBCT scans. <strong>It has been shown to be robust in most situations</strong>, even in the presence of metallic artefacts or varying field of views.</p>
<p>It generates the <strong>following segmentations</strong> :</p>
<ul>
<li>Maxilla &amp; Upper Skull</li>
<li>Mandible</li>
<li>Upper Teeth</li>
<li>Lower Teeth</li>
<li>Mandibular canal</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2569828df311674a764d62a37486d035e3ee28dd.jpeg" data-download-href="/uploads/short-url/5kXIFzDWIwQoGkjlyaVQYvy73bv.jpeg?dl=1" title="dentalsegmentator_example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2569828df311674a764d62a37486d035e3ee28dd_2_517x374.jpeg" alt="dentalsegmentator_example" data-base62-sha1="5kXIFzDWIwQoGkjlyaVQYvy73bv" width="517" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2569828df311674a764d62a37486d035e3ee28dd_2_517x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2569828df311674a764d62a37486d035e3ee28dd_2_775x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2569828df311674a764d62a37486d035e3ee28dd.jpeg 2x" data-dominant-color="D6CEC6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dentalsegmentator_example</span><span class="informations">850×615 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Segment editor</strong> tools and <strong>model export</strong> features are directly available in the module. The extension does not require a GPU, but a CUDA-capable GPU is needed for fast results (around 1-2 minutes).</p>
<p>Install tutorial and demonstration video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="BEG-XhjjiaY" data-video-title="DentalSegmentator 3D Slicer extension" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=BEG-XhjjiaY" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/BEG-XhjjiaY/maxresdefault.jpg" title="DentalSegmentator 3D Slicer extension" width="690" height="388">
  </a>
</div>

<p>If you use DentalSegmentator for your work, please cite our paper and nnU-Net:</p>
<blockquote>
<p>Dot G, Chaurasia A, Dubois G, et al. DentalSegmentator: robust deep learning-based CBCT image segmentation. Published online March 18, 2024:2024.03.18.24304458. doi:<a href="https://doi.org/10.1101/2024.03.18.24304458" rel="noopener nofollow ugc">10.1101/2024.03.18.24304458</a></p>
</blockquote>
<blockquote>
<p>Isensee F, Jaeger PF, Kohl SAA, Petersen J, Maier-Hein KH. nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nat Methods. 2021;18(2):203-211. doi:<a href="https://doi.org/10.1038/s41592-020-01008-z" rel="noopener nofollow ugc">10.1038/s41592-020-01008-z</a></p>
</blockquote>
<p>The module was developed by T. Pelletier and R. Fenioux (Kitware SAS); financed by the FFO (Fédération Française d’Orthodontie) and the Fondation des Gueules Cassées.</p>

---

## Post #2 by @lassoan (2024-04-24 01:23 UTC)

<p>5 posts were split to a new topic: <a href="/t/dentalsegmentator-extension-is-not-working/35697">DentalSegmentator extension is not working</a></p>

---

## Post #3 by @lassoan (2024-06-10 13:20 UTC)

<p>3 posts were split to a new topic: <a href="/t/dentalsegmentator-version-of-2024-04-22-fails-to-load-segmentation-result/36682">DentalSegmentator version of 2024-04-22 fails to load segmentation result</a></p>

---

## Post #6 by @lassoan (2024-06-17 19:18 UTC)

<p>A post was merged into an existing topic: <a href="/t/dentalsegmentator-fails-with-runtimeerror-invalid-nnunet-configuration-model-folder-is-missing-the-following-folds/35697/8">DentalSegmentator fails with “RuntimeError: Invalid nnUNet configuration. Model folder is missing the following folds”</a></p>

---

## Post #7 by @lassoan (2024-06-10 13:21 UTC)

<p>2 posts were split to a new topic: <a href="/t/dentalsegmentator-inaccuracies-separating-cortical-bone-and-teeth/36683">DentalSegmentator inaccuracies separating cortical bone and teeth</a></p>

---

## Post #9 by @lassoan (2024-06-10 13:22 UTC)

<p>A post was split to a new topic: <a href="/t/unicodedecodeerror-when-running-dentalsegmentator/36684">UnicodeDecodeError when running DentalSegmentator</a></p>

---

## Post #10 by @lassoan (2024-06-17 19:20 UTC)

<p>3 posts were merged into an existing topic: <a href="/t/cuda-issue-with-dentalsegmentator/36549/5">Cuda issue with dentalsegmentator</a></p>

---

## Post #13 by @lassoan (2024-06-17 19:22 UTC)

<p>3 posts were split to a new topic: <a href="/t/dentalsegmentator-for-condyle-segmentation/36847">DentalSegmentator for condyle segmentation?</a></p>

---

## Post #14 by @lassoan (2024-07-16 18:25 UTC)

<p>3 posts were split to a new topic: <a href="/t/dentalsegmentator-result-mesh-is-inverted/37408">DentalSegmentator result mesh is inverted</a></p>

---

## Post #15 by @lassoan (2024-07-22 21:43 UTC)

<p>2 posts were split to a new topic: <a href="/t/dental-segmentation-for-dogs-and-cats/37506">Dental segmentation for dogs and cats</a></p>

---

## Post #16 by @Marta_Fernandez (2024-08-26 16:32 UTC)

<p>Thank you very much for creating the module, but it doesn’t work. I have the latest version of the program installed, as well as all the required plugins. However, when I click ‘apply,’ it just keeps loading and doesn’t do anything. I’ve left it running for up to an hour, but nothing happens.</p>

---

## Post #17 by @Anderson_Fedel (2024-09-15 20:57 UTC)

<p>Awesome work. Congrats!<br>
I would like to know if it is possible to set parameters so we can run it on a 2gb NVIDIA laptop GPU.<br>
I run it on CPU just fine (it takes several minutes). But I ran out of memory when tried to run on CUDA.</p>

---

## Post #18 by @lassoan (2024-09-16 23:19 UTC)

<p>A GPU with 2GB RAM is only sufficient for some very lightweight visualization tasks, it is too small to be useful for 3D segmentation.</p>
<p>You can either upgrade to a stronger GPU (I would recommend minimum 12GB GPU RAM, but 24GB would be safer if you want to use it for a few years) or use your CPU.</p>

---

## Post #19 by @Anderson_Fedel (2024-09-17 12:07 UTC)

<p>Thank you very much for the clarification! I understood perfectly. My laptop’s GPU is not suitable for the task.</p>

---

## Post #20 by @lassoan (2024-10-01 13:56 UTC)

<p>A post was split to a new topic: <a href="/t/install-dentalsegmentator-from-behind-restrictive-firewall/39474">Install DentalSegmentator from behind restrictive firewall</a></p>

---

## Post #21 by @Haider_Amin (2025-02-02 20:06 UTC)

<p>HEY,<br>
thankyou for such a revolutionary initiative.<br>
i cant use the module even with all the instruction s. can anyone help?<br>
regards<br>
dr haider<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11dfc0c0ce30de59faa988f7c8349ee039c30f8c.jpeg" data-download-href="/uploads/short-url/2y7vl0rgADFQf0epjEfcidZ3Lly.jpeg?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11dfc0c0ce30de59faa988f7c8349ee039c30f8c_2_690x415.jpeg" alt="error" data-base62-sha1="2y7vl0rgADFQf0epjEfcidZ3Lly" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11dfc0c0ce30de59faa988f7c8349ee039c30f8c_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11dfc0c0ce30de59faa988f7c8349ee039c30f8c_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11dfc0c0ce30de59faa988f7c8349ee039c30f8c_2_1380x830.jpeg 2x" data-dominant-color="D3D2D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1920×1155 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @Haider_Amin (2025-02-02 20:09 UTC)

<p>how do i share logs?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddc3e07a6dbdcab8d7d62740920331a154d365ff.jpeg" data-download-href="/uploads/short-url/vDPbtZZFo6lVa4FHMpwUdLAgiaH.jpeg?dl=1" title="error 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddc3e07a6dbdcab8d7d62740920331a154d365ff_2_690x414.jpeg" alt="error 2" data-base62-sha1="vDPbtZZFo6lVa4FHMpwUdLAgiaH" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddc3e07a6dbdcab8d7d62740920331a154d365ff_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddc3e07a6dbdcab8d7d62740920331a154d365ff_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddc3e07a6dbdcab8d7d62740920331a154d365ff_2_1380x828.jpeg 2x" data-dominant-color="C2C3C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error 2</span><span class="informations">1920×1152 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @Rabab (2025-02-27 09:12 UTC)

<p>I have an issue with this tool “Dentalsegmentator” when I choose it from the menu, this massage “nnUNet is already installed (2.5.2) and compatible with requested version (nnunetv2).” appear and nothing happens in the software. The application keeps loading with no change. I really want help with this problem.</p>

---

## Post #24 by @amyers (2025-10-03 13:48 UTC)

<p>Hi, great work on the extension! Additional training data can be found here: <a href="https://ditto.ing.unimore.it/toothfairy/" class="inline-onebox" rel="noopener nofollow ugc">Dataset</a></p>

---

## Post #25 by @Romulo_Alfaro (2025-10-04 15:58 UTC)

<p>It’s a huge extension. I hope that at some point we can segment each tooth individually.</p>

---

## Post #26 by @Aleksandr_Rybakov (2026-02-09 16:20 UTC)

<p>I wish we could use UniversalLabDentalSegmentator model in this plugin.</p>

---
