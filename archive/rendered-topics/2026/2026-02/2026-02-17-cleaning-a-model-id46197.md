# Cleaning a model

**Topic ID**: 46197
**Date**: 2026-02-17
**URL**: https://discourse.slicer.org/t/cleaning-a-model/46197

---

## Post #1 by @kvzwaag (2026-02-17 22:39 UTC)

<p>Hello!  New user here, just getting my feet wet.  I’m help an head and neck surgeon friend with some modeling to see if it can be used for surgical planning.  I’m trying to isolate the mandible, and I’ve gotten close but I can’t get rid of the areas in red.  The snipping tool isn’t working and if I try to add those areas to background it removes areas from the entire mandible.  I’d appreciate any input, thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51b33cb7af6eecd2f57050d0715f1556537a0934.jpeg" data-download-href="/uploads/short-url/bEKGItjQsSNfKAfvTfHgjU4mlmY.jpeg?dl=1" title="Screenshot 2026-02-17 160303" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51b33cb7af6eecd2f57050d0715f1556537a0934_2_690x384.jpeg" alt="Screenshot 2026-02-17 160303" data-base62-sha1="bEKGItjQsSNfKAfvTfHgjU4mlmY" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51b33cb7af6eecd2f57050d0715f1556537a0934_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51b33cb7af6eecd2f57050d0715f1556537a0934_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51b33cb7af6eecd2f57050d0715f1556537a0934.jpeg 2x" data-dominant-color="969591"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-02-17 160303</span><span class="informations">1367×762 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-02-17 23:03 UTC)

<p>you can definitely use the scissors tool for that.  Or if you are ambitious you could try using the nnInteractive extension, which is very powerful for this kind of segmentation task.</p>

---

## Post #3 by @mau_igna_06 (2026-02-18 16:00 UTC)

<p>If you are planning a fibula flap mandible reconstruction consider using <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" rel="noopener nofollow ugc">BoneReconstructionPlanner</a></p>

---
