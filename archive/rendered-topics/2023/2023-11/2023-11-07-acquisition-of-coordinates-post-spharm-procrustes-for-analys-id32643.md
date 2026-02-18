# Acquisition of coordinates post SPHARM/Procrustes for analysis

**Topic ID**: 32643
**Date**: 2023-11-07
**URL**: https://discourse.slicer.org/t/acquisition-of-coordinates-post-spharm-procrustes-for-analysis/32643

---

## Post #1 by @Hoai-Nam_Bui (2023-11-07 15:41 UTC)

<p>Good morning!</p>
<p>I have a dataset of 51 different vertebrae I am analyzing for shape variation. I’ve utilized the population analysis module to export the PCA data in the json format and acquired the first two PCs from the table in the Data Module. However, I am unable to figure out what my PC values are in the json (or they do not seem to match up) with the Population analysis PC values.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e596fa8dc0483319922325357204b8efccd8f9.png" data-download-href="/uploads/short-url/1pybQjexs6AvAzbciHpAo1EuXj3.png?dl=1" title="Screenshot 2023-11-07 at 10.39.36 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e596fa8dc0483319922325357204b8efccd8f9_2_690x334.png" alt="Screenshot 2023-11-07 at 10.39.36 AM" data-base62-sha1="1pybQjexs6AvAzbciHpAo1EuXj3" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e596fa8dc0483319922325357204b8efccd8f9_2_690x334.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e596fa8dc0483319922325357204b8efccd8f9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e596fa8dc0483319922325357204b8efccd8f9.png 2x" data-dominant-color="EFF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-07 at 10.39.36 AM</span><span class="informations">737×357 51.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have attempted to also export the coordinates from my aligned vtk’s using the python interactor into an array and run the analysis through geomorph in Rstudio. I am also acquiring PC results very different from the Population analysis results.</p>
<p>First, I am wondering what the workflow is for acquiring PC values in the Population Analysis module. Second, I’d like to be able to acquire the coordinates of my vtk’s after SPHARM-PDM and Procrustes registration to be able to conduct further statistical analysis in R rather than in Slicer itself. I may also be missing something big, I’d love to have a second opinion!</p>
<p>Thanks so much.</p>

---
