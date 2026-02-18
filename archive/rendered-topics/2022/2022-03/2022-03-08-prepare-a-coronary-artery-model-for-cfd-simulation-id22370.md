# Prepare a coronary artery model for CFD simulation.

**Topic ID**: 22370
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/prepare-a-coronary-artery-model-for-cfd-simulation/22370

---

## Post #1 by @Chengxi_Li (2022-03-08 15:02 UTC)

<p>Hi There,</p>
<p>I am trying to prepare a coronary model for CFD simulation which requires to cut the branches of coronary artery nicely. <strong>The aim is to get the model as shown below</strong>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4758e9211114e5ad1ba6ccdbf757e62e241455b8.jpeg" data-download-href="/uploads/short-url/abaodwhFKDsrciPhjNDwYFqfWEo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4758e9211114e5ad1ba6ccdbf757e62e241455b8_2_363x500.jpeg" alt="image" data-base62-sha1="abaodwhFKDsrciPhjNDwYFqfWEo" width="363" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4758e9211114e5ad1ba6ccdbf757e62e241455b8_2_363x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4758e9211114e5ad1ba6ccdbf757e62e241455b8_2_544x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4758e9211114e5ad1ba6ccdbf757e62e241455b8.jpeg 2x" data-dominant-color="4A5070"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">575×790 40.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can seen every branches have been clipped. When i try to do achieve this function in VMTK i used command line in Pype as:</p>
<p>vmtksurfacereader -ifile C:/Users/31860/Desktop/ModelProcessing/3-7/CoronaryArtery.stl  --pipe vmtkcenterlines  --pipe vmtkendpointextractor --pipe vmtkbranchclipper -ifile C:/Users/31860/Desktop/ModelProcessing/3-7/CoronaryArtery.stl  --pipe vmtksurfaceconnectivity -cleanoutput 1 --pipe vmtksurfacewriter --pipe vmtksurfacecapper -ofile C:/Users/31860/Desktop/ModelProcessing/3-7/CoronaryArtery_capped.vtp -interactive 0</p>
<p>I have selected source and target as shown below:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c2fe85aaf06af5709c5750bd88d92b9b1faeb9a.jpeg" alt="image" data-base62-sha1="hIBQzApxeJP6BHVei4pVLH9XEP8" width="648" height="409"></p>
<p><strong>The actural result is shown below:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a8e81d17f7cd0e5f7d63831c4ade6c576cf7749.jpeg" data-download-href="/uploads/short-url/cV6i7ZbzIYgUwCCs8GRoS3YeHpv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a8e81d17f7cd0e5f7d63831c4ade6c576cf7749_2_499x500.jpeg" alt="image" data-base62-sha1="cV6i7ZbzIYgUwCCs8GRoS3YeHpv" width="499" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a8e81d17f7cd0e5f7d63831c4ade6c576cf7749_2_499x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a8e81d17f7cd0e5f7d63831c4ade6c576cf7749_2_748x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a8e81d17f7cd0e5f7d63831c4ade6c576cf7749.jpeg 2x" data-dominant-color="4B516E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">763×764 40.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can see, the coronary branches are good but the aortic root is not cut correctly. Let me know how can i imporve. Many thanks!</p>
<p>For any one who wanna have a try at the model, please find link attrached.<br>
<a href="https://liveuclac-my.sharepoint.com/:u:/g/personal/ucemmly_ucl_ac_uk/EXZ8d20_3XhGhzLq-n3tjlgBxbwyL8i_vCaoVAJ3HgfH5w?e=wMneJi" rel="noopener nofollow ugc">CoronaryArtery.stl</a></p>
<p>Cheers,<br>
Chengxi</p>
<p>Operating system:Windows<br>
Slicer version:Slicer 4.11.20210226<br>
Expected behavior:Mentioned above<br>
Actual behavior:Mentioned above</p>

---
