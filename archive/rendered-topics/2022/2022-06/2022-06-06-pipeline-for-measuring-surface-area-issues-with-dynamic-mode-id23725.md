# Pipeline for measuring surface area & issues with dynamic modeller

**Topic ID**: 23725
**Date**: 2022-06-06
**URL**: https://discourse.slicer.org/t/pipeline-for-measuring-surface-area-issues-with-dynamic-modeller/23725

---

## Post #1 by @sridhar (2022-06-06 08:55 UTC)

<p>Hello,</p>
<p>I was hoping someone could provide me feedback on the pipeline I am developing for measuring the eye surface area of insects (from microCT scans) and figure out the specific issue I am having when performing surface cut using Dynamic Modeller. As of now, I think this could be the pipeline (I am using Slicer ver 5.0.2 on imac):</p>
<ol>
<li>Convert .tiff stacks to .nrrd in ImageJ and specify the voxel size (this step might not be necessary)</li>
<li>Import .nrrd file and segment out the whole head in the Segment Editor (thresholding works fine)</li>
<li>Convert this segment to model (data module → right click on the segment → export visible segment to model)</li>
<li>Create a close curve from the Markups module and place the points to demarcate the outline of the eye (resample points if needed). Here I chose the following options in the curve settings tab (curve type= shortest distance on the surface, constrain to model= model I just created, cost function=inverse squared)</li>
<li>Then open Dynamic Modeller and chose curve cut.</li>
<li>I will then find the surface area in the Models module</li>
</ol>
<p>Firstly, please let me know if there are any shortcuts to speed up the analyses (I have close to 400 scans to measure). Secondly, you can see that the placement of the curve is misplaced when seen in 2D slices but looks alright on the 3D model. And thirdly, the surface cut is not extracting the actual demarcated curve but is extracting something else (red blotch seen in the 3D view image). I am wondering why this is happening. Any inputs will be very helpful and thank you very much in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15b54bb663e4411b7aca172a2080b83f38e2e318.jpeg" data-download-href="/uploads/short-url/362rYyeOVftyWNvQEGVm8IJNEvK.jpeg?dl=1" title="butterfly head" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15b54bb663e4411b7aca172a2080b83f38e2e318_2_690x443.jpeg" alt="butterfly head" data-base62-sha1="362rYyeOVftyWNvQEGVm8IJNEvK" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15b54bb663e4411b7aca172a2080b83f38e2e318_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15b54bb663e4411b7aca172a2080b83f38e2e318_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15b54bb663e4411b7aca172a2080b83f38e2e318_2_1380x886.jpeg 2x" data-dominant-color="505358"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">butterfly head</span><span class="informations">1920×1233 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43df69c3d4b7734a1292e84a53d112b65a741fb9.png" data-download-href="/uploads/short-url/9GqEmlqjd0HNIotwsaH78B5uNE5.png?dl=1" title="surface cut gone wrong" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43df69c3d4b7734a1292e84a53d112b65a741fb9_2_690x436.png" alt="surface cut gone wrong" data-base62-sha1="9GqEmlqjd0HNIotwsaH78B5uNE5" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43df69c3d4b7734a1292e84a53d112b65a741fb9_2_690x436.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43df69c3d4b7734a1292e84a53d112b65a741fb9_2_1035x654.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43df69c3d4b7734a1292e84a53d112b65a741fb9_2_1380x872.png 2x" data-dominant-color="9B9DD3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">surface cut gone wrong</span><span class="informations">3556×2252 72.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
