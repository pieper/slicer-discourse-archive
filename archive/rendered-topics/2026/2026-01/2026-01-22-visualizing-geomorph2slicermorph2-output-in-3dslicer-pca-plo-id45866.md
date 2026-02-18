# Visualizing geomorph2slicermorph2 output in 3DSlicer: PCA plot differences?

**Topic ID**: 45866
**Date**: 2026-01-22
**URL**: https://discourse.slicer.org/t/visualizing-geomorph2slicermorph2-output-in-3dslicer-pca-plot-differences/45866

---

## Post #1 by @katrust (2026-01-22 15:41 UTC)

<p>I am concerned about some differences I am seeing in my PCA scatterplot in 3DSlicer after having produced GPA and PCA results to slide semi-LMs in the geomorph R package.</p>
<p>As a very coarse way to sanity checking myself, I uploaded my geomorph output to 3DSlicer to better visualize which specimens fall where in the morphospace (a very convenient feature in SlicerMorph). As you can see in the Geomorph R PCA plot, a datapoint with a factor of stage  “2” and colored pink is positioned in the lower right quadrant at the intersection of .02 on PC1 and close to -.06 on PC2.</p>
<p>When I uploaded this geomorph output into 3Dslicer to see which specimen this is, I went to search for that specific data point and I can’t seem to locate it in the morphospace where my Geomorph R plotted it along PC1 and PC2.</p>
<p>Now, as I compare the plots, I am concerned about the overall differences in these scatterplots. Of course scaling differences between plots can alter the visualization of the data, but as I compare the plots, I don’t think that’s the case. Am I missing something here?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/252f08b09aad0e38f82a8716ce0e31279a8f9a36.png" data-download-href="/uploads/short-url/5iWr2DaM355YweRslPhViNWrpFY.png?dl=1" title="Screenshot 2026-01-20 at 1.48.26 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/252f08b09aad0e38f82a8716ce0e31279a8f9a36_2_435x500.png" alt="Screenshot 2026-01-20 at 1.48.26 PM" data-base62-sha1="5iWr2DaM355YweRslPhViNWrpFY" width="435" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/252f08b09aad0e38f82a8716ce0e31279a8f9a36_2_435x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/252f08b09aad0e38f82a8716ce0e31279a8f9a36_2_652x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/252f08b09aad0e38f82a8716ce0e31279a8f9a36.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-01-20 at 1.48.26 PM</span><span class="informations">723×831 25.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5999f77817291ebac63f01614308116b430ad5df.png" data-download-href="/uploads/short-url/cMEmKz13gRwfYCZKEAZbIOIJ6tF.png?dl=1" title="Screenshot 2026-01-20 at 1.51.59 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5999f77817291ebac63f01614308116b430ad5df_2_690x411.png" alt="Screenshot 2026-01-20 at 1.51.59 PM" data-base62-sha1="cMEmKz13gRwfYCZKEAZbIOIJ6tF" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5999f77817291ebac63f01614308116b430ad5df_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5999f77817291ebac63f01614308116b430ad5df_2_1035x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5999f77817291ebac63f01614308116b430ad5df_2_1380x822.png 2x" data-dominant-color="F2F4F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-01-20 at 1.51.59 PM</span><span class="informations">1717×1023 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-01-22 16:37 UTC)

<p>As far as I can tell the sign of PC2 has changes between those two plots. PC signs are arbitrary, so I wouldn’t be concerned about those. But if you want to be sure, you can just run a correlation of the values between geomorph and slicermorph. I suspect it will come as -1.</p>

---
