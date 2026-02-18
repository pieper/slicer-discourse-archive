# How to find the image match between the external reference with the annotations and the sequence in 3DSlicer?

**Topic ID**: 18145
**Date**: 2021-06-15
**URL**: https://discourse.slicer.org/t/how-to-find-the-image-match-between-the-external-reference-with-the-annotations-and-the-sequence-in-3dslicer/18145

---

## Post #1 by @Mostafa2020 (2021-06-15 16:12 UTC)

<p>Hi All,</p>
<p>I have annotation files that contain a box surrounding the tumor. In order to do the segmentation process in 3D Slicer and extract features, I am going to find the exact match between the annotation file and the same image in 3D Slicer. I wondered if there is a way to match the annotation image (surrounding box) with the coordinates that 3Dslicer gives about the position of the image in the sequence.</p>
<p>Thank you in advance.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee34db0973ef03dfc63a0fac87dfa21e814712b7.jpeg" data-download-href="/uploads/short-url/xZgSB0y1sI4xD510TNbJQomz4k7.jpeg?dl=1" title="Screen Shot 2021-06-15 at 12.01.54 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee34db0973ef03dfc63a0fac87dfa21e814712b7_2_690x283.jpeg" alt="Screen Shot 2021-06-15 at 12.01.54 PM" data-base62-sha1="xZgSB0y1sI4xD510TNbJQomz4k7" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee34db0973ef03dfc63a0fac87dfa21e814712b7_2_690x283.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee34db0973ef03dfc63a0fac87dfa21e814712b7_2_1035x424.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee34db0973ef03dfc63a0fac87dfa21e814712b7_2_1380x566.jpeg 2x" data-dominant-color="8C8B8B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-15 at 12.01.54 PM</span><span class="informations">2880×1185 602 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-06-17 01:58 UTC)

<p>Yes, sure, it should be no problem. What software did you use to specify the boxes? What is the format of the annotation files? Can you copy the content of an example annotation file here?</p>

---

## Post #3 by @Mostafa2020 (2021-06-17 03:15 UTC)

<p>Hi Andras, The image annotations are saved as XML files in PASCAL VOC format and Python code is written to visualize the annotation boxes on top of the DICOM images. The following is the content of one of the annotation files for the first patient. Totally, there are 20 annotation files for the first patient, and I am going to find a way to match the annotation image (surrounding box) with the coordinates that 3D Slicer gives about the position of the image in the sequence.</p>
<blockquote></blockquote>
<div class="md-table">
<table>
<thead>
<tr>
<th>/<span class="mention">@verified</span></th>
<th>no</th>
</tr>
</thead>
<tbody>
<tr>
<td>/filename</td>
<td>Unknow</td>
</tr>
<tr>
<td>/folder</td>
<td>Unknow</td>
</tr>
<tr>
<td>/object/bndbox/xmax</td>
<td>360</td>
</tr>
<tr>
<td>/object/bndbox/xmin</td>
<td>278</td>
</tr>
<tr>
<td>/object/bndbox/ymax</td>
<td>394</td>
</tr>
<tr>
<td>/object/bndbox/ymin</td>
<td>308</td>
</tr>
<tr>
<td>/object/Difficult</td>
<td>0</td>
</tr>
<tr>
<td>/object/name</td>
<td>A</td>
</tr>
<tr>
<td>/object/pose</td>
<td>Unspecified</td>
</tr>
<tr>
<td>/object/truncated</td>
<td>0</td>
</tr>
<tr>
<td>/path</td>
<td>Unknow</td>
</tr>
<tr>
<td>/segmented</td>
<td>0</td>
</tr>
<tr>
<td>/size/depth</td>
<td>1</td>
</tr>
<tr>
<td>/size/height</td>
<td>512</td>
</tr>
<tr>
<td>/size/width</td>
<td>512</td>
</tr>
<tr>
<td>/source</td>
<td>Unknow</td>
</tr>
<tr>
<td>/source/database</td>
<td>Unknown</td>
</tr>
</tbody>
</table>
</div><p>Thanks for your help.</p>

---

## Post #4 by @lassoan (2021-06-17 03:51 UTC)

<p>Probably the simplest is to write a short Python script that creates fills a numpy array with these ROI rectangles (you can use numpy indexing to fill a rectangular region with a value), then save the numpy array into a nrrd file using pynrrd.</p>
<p>Make sure the set origin, spacing, and axis directions of the nrrd file according to the DICOM file’s geometry. If you are not sure how to get this information then you can import the DICOM series into Slicer, save as nrrd, and use the same header.</p>

---

## Post #5 by @Mostafa2020 (2021-06-17 03:57 UTC)

<p>Great!! Would you please tell me if there is an example of Python code, which you mentioned, that I can use as a reference?</p>

---

## Post #6 by @lassoan (2021-06-17 04:04 UTC)

<p>You don’t need anything fancy, just create a numpy array using <code>data=np.zeros([512,512,512])</code>, fill each rectangle by numpy array indexing, such as <code>data[10:20, 30:40, 45]=1</code> and write the resulting file nrrd as shown <a href="https://pynrrd.readthedocs.io/en/latest/user-guide.html#example-reading-and-writing-nrrd-files-with-c-order-indexing">here</a>.</p>
<p>If you save the file with <code>.label.nrrd</code> file extension then Slicer will load it by default as a labelmap volume and if you use <code>.seg.nrrd</code> then Slicer will load it as a segmentation by default.</p>

---

## Post #7 by @Mostafa2020 (2021-06-17 05:00 UTC)

<p>Awesome!! Thanks so much. I will try it.</p>

---
