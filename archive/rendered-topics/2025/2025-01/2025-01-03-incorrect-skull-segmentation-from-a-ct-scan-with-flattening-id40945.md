# Incorrect skull segmentation from a CT scan, with flattening distortion

**Topic ID**: 40945
**Date**: 2025-01-03
**URL**: https://discourse.slicer.org/t/incorrect-skull-segmentation-from-a-ct-scan-with-flattening-distortion/40945

---

## Post #1 by @JuMaLe (2025-01-03 17:32 UTC)

<p>Hello!<br>
I obtained this serie, which lacks information about slice thickness, and I obtained the following flattened segmentation. What could be the issues? What metadata information could allow me to anticipate this outcome? Is it possible to obtain a correct segmentation from the same series?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac6bb709a05979745dd4df451ddf5a923888de48.png" data-download-href="/uploads/short-url/oBiTZYHce7HKu55wuhXsuHFTsIU.png?dl=1" title="consutla 3dlslicer forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac6bb709a05979745dd4df451ddf5a923888de48_2_690x461.png" alt="consutla 3dlslicer forum" data-base62-sha1="oBiTZYHce7HKu55wuhXsuHFTsIU" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac6bb709a05979745dd4df451ddf5a923888de48_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac6bb709a05979745dd4df451ddf5a923888de48.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac6bb709a05979745dd4df451ddf5a923888de48.png 2x" data-dominant-color="464849"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">consutla 3dlslicer forum</span><span class="informations">829×554 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks again!</p>

---

## Post #2 by @pieper (2025-01-03 17:45 UTC)

<p>It looks like you have scans of a study that was printed on film, so you’ll need to figure out what the right spacing is (perhaps you can tell from some of the text or maybe you know it from somewhere else).  You can set the spacings in the Volume Information portion of the Volumes module.</p>

---
