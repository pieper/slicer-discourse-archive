---
topic_id: 42118
title: "Importing Covariates With Load Gpa Pca Analysis From File"
date: 2025-03-14
url: https://discourse.slicer.org/t/42118
---

# Importing covariates with "Load GPA + PCA  Analysis from File"?

**Topic ID**: 42118
**Date**: 2025-03-14
**URL**: https://discourse.slicer.org/t/importing-covariates-with-load-gpa-pca-analysis-from-file/42118

---

## Post #1 by @christyhipsley (2025-03-14 00:41 UTC)

<p>Hi all. I used the geomorph2slicermorph2 command in the SlicerMorphR package to load the results of a gpa and pca with sliding landmarks from geomorph into 3D Slicer. I would like to use some of the visualisation options here, but I can’t figure out how to get a covariates file in under the GPA module of SlicerMorph. I tried putting one called covariates.csv into the same outputs folder from R, but Slicer does not seem to read it. Is there another way to put covariates in? The button to “Generate new covariate table template” is grayed out, and if I load a file under “Select covariates table”, nothing happens - for example, under the Explore Data/Results tab for PCA Scatter Plot Options, nothing is shown under Select factor.</p>
<p>Thank you for any help,<br>
Christy</p>

---

## Post #2 by @muratmaga (2025-03-14 01:05 UTC)

<p><a class="mention" href="/u/christyhipsley">@christyhipsley</a> currently it is not possible to use covariates in the way you are bringing data from geomorph. You can only make bivariate PC plots and/or interactive 3D visualizations.</p>
<p>We are working to create on something that will allow both bringing the covariates and results from GPA, but it will take sometime.</p>

---
