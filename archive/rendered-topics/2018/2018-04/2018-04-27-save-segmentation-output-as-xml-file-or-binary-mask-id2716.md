# Save segmentation output as xml file or binary mask

**Topic ID**: 2716
**Date**: 2018-04-27
**URL**: https://discourse.slicer.org/t/save-segmentation-output-as-xml-file-or-binary-mask/2716

---

## Post #1 by @shikunyu8 (2018-04-27 04:01 UTC)

<p>Operating system: Windows 8<br>
Slicer version: 4.8.1<br>
Expected behavior: get segmentation output in xml, or just binary image format like jpg or png.<br>
Actual behavior: can’t figure out how to get correct format.</p>
<p>Hi,</p>
<p>I am very new to slicer, and my goal of using slicer is to create manual annotations on dicom files, then save those annotations as binary array(1 for segmented area, 0 for background) with exact same dimension with original image.  The purpose of saving these masks is for training neural nets.</p>
<p>However, I haven’t figured it out how to save these segmented areas. If someone can tell me how to do this or provide some tutorial links, that will be great.</p>
<p>Warmest Regard!<br>
Kunyu Shi</p>

---

## Post #2 by @lassoan (2018-04-27 04:06 UTC)

<p>Export segmentation to labelmap node in Segmentations module’s Export/Import section. To match the exported labelmap’s geometry with another volume’s choose a reference volume in Advanced section / Reference volume.</p>

---

## Post #3 by @Arcsecond (2019-02-06 00:04 UTC)

<p>I’m also looking to generate masks for neural nets, I see how I can follow the instructions you’ve given but I don’t see how I can get the output as a series of .jpgs or binary arrays. I’m not sure how to convert .nnrd and .ctbl into a series of images</p>

---

## Post #4 by @lassoan (2019-02-06 00:35 UTC)

<p>Most medical image deep learning toolkits can directly use the nrrd file that you save in Slicer. See for example <a href="http://www.niftynet.io" rel="nofollow noopener">http://www.niftynet.io</a>.</p>
<p>For initial testing, you can use Screen Capture module to export image slices as a series of png files.</p>

---

## Post #5 by @Arcsecond (2019-02-06 01:57 UTC)

<p>Preliminary inspection of niftynet shows it to be cool but I already have a pipeline in Keras so I’m not sure it would be worth the time to switch.</p>
<p>Thank you for the help! I will proceed via the screen capture module for now</p>

---
