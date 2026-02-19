---
topic_id: 27725
title: "Labeloverlay Image Saved As Dicom Series"
date: 2023-02-09
url: https://discourse.slicer.org/t/27725
---

# LabelOverlay Image saved as DICOM series

**Topic ID**: 27725
**Date**: 2023-02-09
**URL**: https://discourse.slicer.org/t/labeloverlay-image-saved-as-dicom-series/27725

---

## Post #1 by @Franciska (2023-02-09 17:33 UTC)

<p>Hi!</p>
<p>I have a DICOM series, and with the segmentations I create a LabelOverlay Image. When I write it out as a DICOM series, I modified the following datatags in the created image, to get an RGB image.:</p>
<pre><code class="lang-auto">  image_slice.SetMetaData("0028|0002", str(3)) #Samples per Pixel Attribute
  image_slice.SetMetaData("0028|0004", "RGB")
</code></pre>
<p>The LabelOverlay is saved as DICOM series, but Slicer is not able to load it, it gives the following ERROR: Could not load: prediction as a Scalar Volume.<br>
When I check one pixel of the LabelOverlay Image it is in fact not a scalar, but (255,255,255). I though setting the samples per pixel attribute to 3 will fix this.<br>
What tag should I modify to be able to load the LabelOverlay DICOM series into slicer?</p>

---

## Post #2 by @Franciska (2023-02-13 14:52 UTC)

<p>The slices one-by-one are loaded properly, and look good in Slicer. If I drag the whole Series into the DICOM database it looks like one Serie, with several slices. The DICOM metadata looks good, (modality is set to “OT”, SOPInstance UID, InstanceNumber,ImagePositionPatient and Instance CreationTime are different to each slice, the other attributes are the same for all).</p>
<p>All in all, the DICOM slices seems to be good, however, Slicer can’t load them in together, as a Serie.</p>
<p>These attributes are fixed for all slice to be the same as in the original DICOM serie:</p>
<pre><code>        "0010|0010",  # Patient Name
        "0010|0020",  # Patient ID    
        "0020|0011",  # Series Number
        "0010|0030",  # Patient Birth Date
        "0020|000d",  # Study Instance UID, for machine consumption
        "0020|0010",  # Study ID, for human consumption
        "0008|0020",  # Study Date
        "0008|0030",  # Study Time
        "0008|0050",  # Accession Number
        "0008|1030",  # Study Description
</code></pre>

---

## Post #3 by @pieper (2023-02-13 16:35 UTC)

<p>Hi - it’s not clear to me how you are creating these label overlay images - i.e. what software is used and what how you expect to use them.  But it sounds like you want segmentation objects and would be able to use the code and methods described <a href="https://github.com/QIICR/dcmqi">in the DCMQI project</a>.</p>

---

## Post #4 by @Franciska (2023-02-13 16:47 UTC)

<p>Hi! Sorry I really wasn’t clear enough. I am generating these images with SimpleITK. I also posted my problem (and my script) in the <a href="https://discourse.itk.org/t/saving-labeloverlay-image-as-dicom-series/5689/6" rel="noopener nofollow ugc">simpleitk forum</a>.</p>
<p>I want to use this to be able to visualize several segmentations on the CT scan, in the same DICOM Series file. (without opening several files together.) It works perfectly if I save my results in a nii.gz format, but unfortunately it is a requierment to save them as a DICOM series.</p>

---

## Post #5 by @pieper (2023-02-13 17:13 UTC)

<p>Ah, okay, yes, that helps.  The DCMQI code should let you do this in a straightforward way.  You can create a set of segments with appropriate labels and colors.  The code can take your nii.gz file as input and you can use a json file to specify the metadata.</p>

---

## Post #6 by @Franciska (2023-02-14 08:38 UTC)

<p>Thanks, I’ll take a look at it!</p>

---

## Post #7 by @Franciska (2023-02-14 11:56 UTC)

<p>I also uploaded example files <a href="https://easyupload.io/m/gpj0qm" rel="noopener nofollow ugc">here</a>.<br>
NLST_56831_result contains the DICOM series, that gives<br>
<code> ERROR: Could not load: prediction as a Scalar Volume</code><br>
while it can load the slices individually perfectly fine.</p>

---

## Post #8 by @Franciska (2023-02-14 15:43 UTC)

<p>And the other weird thing is that when I drag the directory into Slicer, and it asks me to select a reader, if I select Any Data instead of Load directory into DICOM database, it loads it!</p>

---

## Post #9 by @pieper (2023-02-14 20:59 UTC)

<p>You’ll need to read through the DCMQI documentation that I linked above to learn about how dicom segmentation objects are created.  Once you do this, and you have the Quantitative Reporting extension installed in Slicer then you can work with these data formats directly.</p>
<p>If you are still having trouble, you could join the Imaging Data Commons (IDC) office hours described <a href="https://discourse.canceridc.dev/t/idc-may-2022-release-idc-community-office-hours/276">at this post</a>.  The IDC has examples for encoding segmentation results in dicom.</p>

---
