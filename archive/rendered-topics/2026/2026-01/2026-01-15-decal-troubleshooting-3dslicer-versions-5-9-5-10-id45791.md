# DeCAL troubleshooting (3DSlicer versions 5.9 & 5.10)

**Topic ID**: 45791
**Date**: 2026-01-15
**URL**: https://discourse.slicer.org/t/decal-troubleshooting-3dslicer-versions-5-9-5-10/45791

---

## Post #1 by @katrust (2026-01-15 20:46 UTC)

<p>I have been using the DeCAL extension via SlicerMorph since it’s earliest versions, and I have produced DeCAL output of evenly spaced semi-landmarks across all the models in my sample (in my case, these models are several segmented fossil teeth). I have taken painstakingly arduous manual segmentation efforts to also ensure that there is no internal morphology inside the teeth (i.e., fossilized dentin) that would affect the DeCAL surface semi-landmarking.</p>
<p>In the latest versions of 3DSlicer, 5.10 and 5.9, I have tried to re-run the same analyses that I produced last year (February and March 2025), and the DeCAL output is nothing like the original DeCAL output from earlier runs. 3D Slicer versions 5.10 and 5.9 have produced uneven semi-landmarks across the same sample of models and fixed landmarks (see attached screenshots comparing the DeCAL semi-LM output for the same dataset)</p>
<p>Has anyone else run into this issue? I first experienced this issue when I went to add additional fossil specimens to my original dataset. I first thought this was an issue with my additional specimens, so I decided to re-run the original analysis without any new data on versions 5.10 and 5.9.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8febcd41f6c462ee154c5488d5ad1f10b4fc51d.jpeg" data-download-href="/uploads/short-url/xfaxQFC460GZlFkZbBMP00fuAoZ.jpeg?dl=1" title="Screenshot 2026-01-13 at 12.56.58 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8febcd41f6c462ee154c5488d5ad1f10b4fc51d_2_577x500.jpeg" alt="Screenshot 2026-01-13 at 12.56.58 PM" data-base62-sha1="xfaxQFC460GZlFkZbBMP00fuAoZ" width="577" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8febcd41f6c462ee154c5488d5ad1f10b4fc51d_2_577x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8febcd41f6c462ee154c5488d5ad1f10b4fc51d_2_865x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8febcd41f6c462ee154c5488d5ad1f10b4fc51d_2_1154x1000.jpeg 2x" data-dominant-color="C5C6D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-01-13 at 12.56.58 PM</span><span class="informations">1347×1166 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcdce1700f69d6d560243a9b44ea9468d5b83602.jpeg" data-download-href="/uploads/short-url/A4VyxsjSMf44xqpRd0ZPJXz0yVs.jpeg?dl=1" title="Screenshot 2026-01-13 at 1.02.23 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdce1700f69d6d560243a9b44ea9468d5b83602_2_575x500.jpeg" alt="Screenshot 2026-01-13 at 1.02.23 PM" data-base62-sha1="A4VyxsjSMf44xqpRd0ZPJXz0yVs" width="575" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdce1700f69d6d560243a9b44ea9468d5b83602_2_575x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdce1700f69d6d560243a9b44ea9468d5b83602_2_862x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdce1700f69d6d560243a9b44ea9468d5b83602_2_1150x1000.jpeg 2x" data-dominant-color="C5C6DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-01-13 at 1.02.23 PM</span><span class="informations">1349×1172 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-01-15 21:09 UTC)

<p>Are these the same specimens? It is hard to tell from the screenshots? The from August 8 looks fairly smooth to me, are  you saying that it is not?</p>
<p>If your older slicer is giving you good results, can you try running the new dataset with that? DeCaL hasn’t seen any significant changes since last august (we added some file checks and a new landmark symmetry specification) but those are mostly UI changes and cosmetic in a sense.</p>

---

## Post #3 by @muratmaga (2026-01-15 21:26 UTC)

<p>I did look into some, there are some VTK changes (which we use for creating downsampled point cloud for our semi-landmarks). It is possible that library version changes in Slicer 5.8 from 5.9/5.10 specifically to <code>vtkCleanPolyData</code> might have an impact on the outcome. I don’t have time to investigate further.</p>
<p>What you can do is to go back to the versions that produced good results for you, rerun your original data and your new data to confirm that it still produces good results (that is, changes are not related to the new data you have added to the analysis. New data may have their own problems, perhaps surfaces are not as smooth).  That will confirm that it is a VTK change related problem that we have to investigate.</p>

---

## Post #4 by @katrust (2026-01-20 19:39 UTC)

<p>Thanks Murat, I was able to replicate my results in v5.8. Based on the successful replication, I think it could be related to the VTK changes you mentioned.</p>

---

## Post #5 by @muratmaga (2026-01-20 22:34 UTC)

<p>OK I will try to see what might have changed between the VTK versions that might affect the functionality (when I have the bandwidth).</p>

---
