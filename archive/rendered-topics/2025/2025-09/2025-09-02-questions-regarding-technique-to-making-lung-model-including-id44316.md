---
topic_id: 44316
title: "Questions Regarding Technique To Making Lung Model Including"
date: 2025-09-02
url: https://discourse.slicer.org/t/44316
---

# Questions regarding technique to making lung model including an comparison

**Topic ID**: 44316
**Date**: 2025-09-02
**URL**: https://discourse.slicer.org/t/questions-regarding-technique-to-making-lung-model-including-an-comparison/44316

---

## Post #1 by @jamesgyh (2025-09-02 13:40 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3887d9334b551e3731d09120387bec5abe92f051.jpeg" data-download-href="/uploads/short-url/845N7xhs2duP8O6UPJJk82qOLEl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3887d9334b551e3731d09120387bec5abe92f051_2_551x500.jpeg" alt="image" data-base62-sha1="845N7xhs2duP8O6UPJJk82qOLEl" width="551" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3887d9334b551e3731d09120387bec5abe92f051_2_551x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3887d9334b551e3731d09120387bec5abe92f051_2_826x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3887d9334b551e3731d09120387bec5abe92f051_2_1102x1000.jpeg 2x" data-dominant-color="88797B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1147×1039 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>here is the model from Stanford. According to them, they use 3d Slicer to build such a detailed bronchi model. However, what I build for now is like this which is roughly one level bronchi smaller than the standford model. May I kindly ask what extensions are needed or what technique is needed to build a model like the previous one, containing that level of bronchi?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30da461582b867f886115febe4c81e24772c8d47.jpeg" data-download-href="/uploads/short-url/6YazdgDK4fynZuenxXo8KrQX9n9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30da461582b867f886115febe4c81e24772c8d47_2_601x500.jpeg" alt="image" data-base62-sha1="6YazdgDK4fynZuenxXo8KrQX9n9" width="601" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30da461582b867f886115febe4c81e24772c8d47_2_601x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30da461582b867f886115febe4c81e24772c8d47_2_901x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30da461582b867f886115febe4c81e24772c8d47.jpeg 2x" data-dominant-color="4C4D84"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1069×889 87.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Esteban_Barreiro (2025-09-03 14:00 UTC)

<p>Hi!<br>
It looks like your model has a great percentage of Surface Smoothing.</p>

---

## Post #3 by @jamesgyh (2025-09-04 08:36 UTC)

<p>Thank you so much, I assume it is not only smoothing, but as the Stanford one reaches fifth</p>
<p>generation of bronchi. Mine only stops at the fourth generation. Is that something due to thickness of the slides?</p>

---

## Post #4 by @eNable_Polska (2025-09-05 06:37 UTC)

<p>Try the “lung segmentator” plugin and select the airways and AI, it should give a better result.</p>

---
