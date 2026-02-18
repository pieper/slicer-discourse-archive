# Anatomical brain segmentation

**Topic ID**: 17778
**Date**: 2021-05-24
**URL**: https://discourse.slicer.org/t/anatomical-brain-segmentation/17778

---

## Post #1 by @Miglius_Mikalauskas (2021-05-24 22:49 UTC)

<p>Hi. Is there a way to automatically segment human brain in mri by anatomical structures?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffd1c82cd89d67b40536d73046d4fe3e514dd577.jpeg" data-download-href="/uploads/short-url/Av5d3SlgIKm9tK6Cmqf9n5Zqu9N.jpeg?dl=1" title="smegenu anatomija" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffd1c82cd89d67b40536d73046d4fe3e514dd577_2_690x334.jpeg" alt="smegenu anatomija" data-base62-sha1="Av5d3SlgIKm9tK6Cmqf9n5Zqu9N" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffd1c82cd89d67b40536d73046d4fe3e514dd577_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffd1c82cd89d67b40536d73046d4fe3e514dd577_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffd1c82cd89d67b40536d73046d4fe3e514dd577_2_1380x668.jpeg 2x" data-dominant-color="898999"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">smegenu anatomija</span><span class="informations">1415×685 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
So that i could automatically see the human brain segmented by either lobes (frontal, temporal etc) or by gyri?<br>
The photo is from a video in youtube.</p>

---

## Post #2 by @pieper (2021-05-25 11:34 UTC)

<p>We usually suggest you use freesurfer for that:<br>
<a href="https://surfer.nmr.mgh.harvard.edu/" class="onebox" target="_blank" rel="noopener">https://surfer.nmr.mgh.harvard.edu/</a></p>

---

## Post #3 by @lassoan (2021-05-25 11:54 UTC)

<p>You may also try more modern and faster methods, such as <a href="https://www.sciencedirect.com/science/article/pii/S1053811920304985">FastSurfer</a>. Let us know which one you end up using.</p>

---

## Post #4 by @Miglius_Mikalauskas (2021-05-25 12:17 UTC)

<p>Thank you for your answers. I have tried running FreeSurfer in linux on VirtualBox, but failed. Never heard of FastSurfer. The problem is that I only have access to microsoft windows. Therefore i was wondering whether there is a method suitable for plain microsoft windows.</p>

---

## Post #5 by @lassoan (2021-05-26 17:05 UTC)

<p>FastSurfer and other modern brain segmentation tools should run fine on any operating systems (because the deep learning frameworks support all operating systems). If FastSurfer does not work well enough for you  then you need to do some web searching, there are several other upcoming competitors.</p>

---

## Post #6 by @dokay1 (2022-07-21 15:49 UTC)

<p>Depending on the level of detail you need the SAMSEG module of FreeSurfer7+ can do a volume based brain segmentation in 5-10 minutes. It generates WM, GM, basal ganglia, ventricles, etc, and has a pretty high tolerance for surface defects or mass lesions.</p>

---
