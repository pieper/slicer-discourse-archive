# Pyradiomics doesn't calculate features for all VOIs

**Topic ID**: 34454
**Date**: 2024-02-21
**URL**: https://discourse.slicer.org/t/pyradiomics-doesnt-calculate-features-for-all-vois/34454

---

## Post #1 by @Dhartez (2024-02-21 16:08 UTC)

<p>Hi all,</p>
<p>I am having a little issue with pyradiomics in Slicer. Briefly, this is to extract features from CNN generated segmentations of two brain structures (bilaterally, so 4 segmentations / VOIs in total) on MRI.</p>
<p>When I load the MRI volume and the segmentation file, it looks good, only the light blue VOI isn’t fully recognized as a segmentation it seems:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f.jpeg" data-download-href="/uploads/short-url/lzju9q29sTdAIBwrJ5pPFS36VlR.jpeg?dl=1" title="Screen1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f_2_690x298.jpeg" alt="Screen1" data-base62-sha1="lzju9q29sTdAIBwrJ5pPFS36VlR" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f_2_690x298.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f_2_1035x447.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f_2_1380x596.jpeg 2x" data-dominant-color="757477"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen1</span><span class="informations">1603×693 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I add it in the Segmentations module it looks fine:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3.jpeg" data-download-href="/uploads/short-url/58X4Tk7Wbb1Ts4kzPA3kmppox3R.jpeg?dl=1" title="Screen2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3_2_690x395.jpeg" alt="Screen2" data-base62-sha1="58X4Tk7Wbb1Ts4kzPA3kmppox3R" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3_2_1380x790.jpeg 2x" data-dominant-color="9E9FA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen2</span><span class="informations">1642×941 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when I run pyradiomics on it, features are only calculated for one of the four VOIs (the brown one):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/6205f08bcf3f0331d852c31b3385db5ebb750e2b.jpeg" data-download-href="/uploads/short-url/dZ9w64IHqV2cWG5RdJrL2i810ZJ.jpeg?dl=1" title="Screen3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6205f08bcf3f0331d852c31b3385db5ebb750e2b_2_690x402.jpeg" alt="Screen3" data-base62-sha1="dZ9w64IHqV2cWG5RdJrL2i810ZJ" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6205f08bcf3f0331d852c31b3385db5ebb750e2b_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6205f08bcf3f0331d852c31b3385db5ebb750e2b_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6205f08bcf3f0331d852c31b3385db5ebb750e2b_2_1380x804.jpeg 2x" data-dominant-color="ABAAAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen3</span><span class="informations">1899×1109 349 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any explanation for this? I am also adding the python console output and the volume and segmentation files in the folder below (all deidentified of course):</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://cloudius.meduniwien.ac.at/index.php/s/tRFmMXwUbacZE05">
  <header class="source">
      <img src="https://cloudius.meduniwien.ac.at/apps-external/theme-meduniwien/core/img/favicon.ico" class="site-icon" width="48" height="48">

      <a href="https://cloudius.meduniwien.ac.at/index.php/s/tRFmMXwUbacZE05" target="_blank" rel="noopener nofollow ugc">MedUni Wien ownCloud</a>
  </header>

  <article class="onebox-body">
    <img width="194" height="194" src="https://cloudius.meduniwien.ac.at/apps-external/theme-meduniwien/core/img/favicon-fb.png" class="thumbnail onebox-avatar">

<h3><a href="https://cloudius.meduniwien.ac.at/index.php/s/tRFmMXwUbacZE05" target="_blank" rel="noopener nofollow ugc">MedUni Wien ownCloud - Cloud Dienst auf Servern der MedUni Wien.</a></h3>

  <p>Files wird öffentlich geteilt</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Many thanks for your help!</p>
<p>P.S.: It works fine with a set of manual segmentations, so I assume it’s not directly a pyradiomics issue, but must have something to do with the segmentation.</p>

---
