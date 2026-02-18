# Extract preprocessed image and mask from Pyradiomics

**Topic ID**: 22654
**Date**: 2022-03-23
**URL**: https://discourse.slicer.org/t/extract-preprocessed-image-and-mask-from-pyradiomics/22654

---

## Post #1 by @JonasB (2022-03-23 14:32 UTC)

<p>Dear community,</p>
<p>I was wondering if it is possible to extract the images and masks on which the feature calculation is based with Pyradiomics in command-line batch mode. I would like to make some comparisons on different mask validation, image discretization, and normalization procedures.</p>
<p>Best,<br>
Jonas</p>

---

## Post #2 by @JoostJM (2022-03-25 07:12 UTC)

<p>Hello Jonas,</p>
<p>Currently, it is not possible to do so directly from the commandline. Still, PyRadiomcis is built fairly modular, so it shouldn’t be to much of a hassle to use the pre-processing functions directly.</p>
<p>Image pre-processing (e.g. normalization, resampling and application of filters) is all defined in <code>imageoperations.py</code>. Every functions accepts a <code>**kwargs</code> argument dict, which contains all configuration from the <code>setting</code> section in the parameter file (it doesn’t matter if there are settings in the dict that are intended for other functions, it just takes out those that are needed).</p>
<p>Image discretization is just as easy, but works on the numpy array extracted from the image. The function you’re looking for is <code>imageoperations.binImage</code>, which accepts the <code>image_array</code>, an optional <code>mask_array</code> and the <code>**kwargs</code> settings. In case the mask array (boolean array) is provided, the discretization is based only on the pixels inside the ROI (PyRadiomics default). If omitted, the entire image is discretized. Be aware that the selection of the label is done elsewhere, the mask array should have boolean datatype indicating only the active ROI.</p>
<p>Hope this helps.</p>
<p>Regards,</p>
<p>Joost</p>

---

## Post #3 by @JonasB (2022-03-25 15:49 UTC)

<p>Thank you very much <a class="mention" href="/u/joostjm">@JoostJM</a>.<br>
Does that mean I need to integrate this into my code or apply imageoperations.py from command line?</p>
<p>Best,<br>
Jonas</p>

---

## Post #4 by @JoostJM (2022-03-26 11:50 UTC)

<p>Hello <a class="mention" href="/u/jonasb">@JonasB</a>,</p>
<p>To test this, you’d need to integrate it into your own python script. The PyRadiomics commandline does not expose that functionality.</p>
<p>Regards,</p>
<p>Joost</p>

---

## Post #5 by @JonasB (2022-10-06 09:50 UTC)

<p>Hi <a class="mention" href="/u/joostjm">@JoostJM</a> ,</p>
<p>thanks for your answers.<br>
I managed to transform the images.<br>
I was wondering, since the functions (such as imageoperations.getLoGImage) take the image and the segmentations but only output the transformed img could the segmentation (the region of interest) be effected by the transformation?<br>
Or in other words do we need to refine the mask for transformed images (might be that the borders of the segmentation from the original image do not fit 100% on the transformed image)?</p>
<p>Best regards,<br>
Jonas</p>

---
