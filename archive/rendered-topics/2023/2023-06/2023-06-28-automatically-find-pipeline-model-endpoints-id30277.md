# Automatically find pipeline model endpoints

**Topic ID**: 30277
**Date**: 2023-06-28
**URL**: https://discourse.slicer.org/t/automatically-find-pipeline-model-endpoints/30277

---

## Post #1 by @yangxw (2023-06-28 11:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1745f02f4f878c71d92762b763cabfd48f2c1a7f.png" data-download-href="/uploads/short-url/3jSP4znLpYfsJgFn49fjHHnMudh.png?dl=1" title="微信图片_20230628185315" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1745f02f4f878c71d92762b763cabfd48f2c1a7f_2_638x500.png" alt="微信图片_20230628185315" data-base62-sha1="3jSP4znLpYfsJgFn49fjHHnMudh" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1745f02f4f878c71d92762b763cabfd48f2c1a7f_2_638x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1745f02f4f878c71d92762b763cabfd48f2c1a7f_2_957x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1745f02f4f878c71d92762b763cabfd48f2c1a7f.png 2x" data-dominant-color="B6B7D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20230628185315</span><span class="informations">1001×784 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
About the automatic extraction of endpoints as shown in the figure, how to implement it in code, I want to use this endpoint to extract the centerline of VMTK。<br>
I checked the source code of the VMTK-slicer extension package and found that it calls a lot of slicer methods. My intention was to load an STL pipeline with code that automatically gets the endpoints and later extracts the model centerline</p>

---
