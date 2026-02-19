---
topic_id: 189
title: "Merge Separate Images Into One Label"
date: 2017-04-25
url: https://discourse.slicer.org/t/189
---

# Merge separate images into one label

**Topic ID**: 189
**Date**: 2017-04-25
**URL**: https://discourse.slicer.org/t/merge-separate-images-into-one-label/189

---

## Post #1 by @Guido_Buezas (2017-04-25 18:42 UTC)

<p>Hi everyone</p>
<p>I have several series (6 rodents species) of microCTs, that I cannot save in DICOM format. I can only reconstruct the slices in TIFF, BMP, PNG format (I’m using NRecon software).<br>
When I load the series of each rodent, all images appear in separate master volumes. I tried to use Merge volume function, but they still appear as separate, I can’t merge separate volumes into one.<br>
What should I do? I want to use Slicer but with this problem is useless.</p>
<p>Kind regards</p>
<p>Guido</p>

---

## Post #2 by @muratmaga (2017-04-25 18:54 UTC)

<p>I use Slicer with datasets from Nrecon daily.</p>
<p>Make sure to uncheck “single file” option during data. See my blog for more detailed instructions using Slicer with image stacks<br>
<a href="https://blogs.uw.edu/maga/2017/04/11/a-worked-example-getting-and-visualizing-data-from-digimorph/" class="onebox" target="_blank" rel="nofollow noopener">https://blogs.uw.edu/maga/2017/04/11/a-worked-example-getting-and-visualizing-data-from-digimorph/</a></p>
<p>You can also convert your stack outside of Slicer to a 3D format (nifti or NRRD) and load it.<br>
M</p>

---
