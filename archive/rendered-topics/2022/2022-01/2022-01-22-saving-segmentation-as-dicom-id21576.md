# Saving segmentation as DICOM

**Topic ID**: 21576
**Date**: 2022-01-22
**URL**: https://discourse.slicer.org/t/saving-segmentation-as-dicom/21576

---

## Post #1 by @WojtekL (2022-01-22 15:55 UTC)

<p>Hello Community,<br>
I’d like to save my segmentation shown on a picture below as a DICOM (.dcm) file instead of (.nrrd). Is there any way to do it?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/952ed417fc575ee7f700ebebc9b8f364715a6f8f.png" alt="image" data-base62-sha1="lhJtiXXyhl8iEeaunmCRoWqLFz9" width="535" height="336"></p>

---

## Post #2 by @cpinter (2022-01-22 18:32 UTC)

<p>See here <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html</a></p>

---

## Post #3 by @DIV (2022-01-25 10:46 UTC)

<p>I take it that the answer is, “Yes”.</p>
<p>From the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database" rel="noopener nofollow ugc">link</a>, the key step seems to be:<br>
“<em>Right-click on a data node in the data tree that will be converted to DICOM format.</em>”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be21dcb3415ad7f79196b9de2d5b192765596a2c.png" data-download-href="/uploads/short-url/r7ZgEA70BfMo7kjPm8hC6yjr0U4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be21dcb3415ad7f79196b9de2d5b192765596a2c.png" alt="image" data-base62-sha1="r7ZgEA70BfMo7kjPm8hC6yjr0U4" width="520" height="500" data-dominant-color="E2E6E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">545×524 30.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It seems to be designed to be applied to a <em>Segmentation</em>, rather than a <em>Segment</em>.</p>
<p>Initially I got the error, “Slicer data bundle export failed.  No file is found for any of the selected items.”<br>
The problem was not having installed the <code>QuantitativeReporting</code> extension, which is mentioned in the linked instructions, and its prerequisites.  (Do this from View &gt; Extensions Manager , and restart the application.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5fb64892834f18df6a5b5b6409a7f05759e7eb8.png" data-download-href="/uploads/short-url/z63AnaPWXsgrUYE6XrsZTKC61x6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5fb64892834f18df6a5b5b6409a7f05759e7eb8.png" alt="image" data-base62-sha1="z63AnaPWXsgrUYE6XrsZTKC61x6" width="527" height="500" data-dominant-color="EFF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">662×628 25.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>A further issue was that initially I couldn’t specify a path under “<code>Export to folder:</code>”.<br>
It turns out that there is a barely visible tick box to the left.  The low contrast meant that I either didn’t see it or else thought that it was deactivated just like all of the controls to the right of “<code>Export to folder:</code>”.</p>
<p>—DIV</p>

---

## Post #4 by @cpinter (2022-01-25 15:31 UTC)

<p>What DICOM modality you want to export it into?</p>

---

## Post #5 by @WojtekL (2022-02-04 22:36 UTC)

<p>Hello,<br>
thanks a lot for the answers as it has helped me already a lot.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> I would like to save it as the SEG modality, to be later able to display the slice with the corresponding mask. As I already know how to save it all as .dcm, now it is only that display part that causes me some troubles.</p>
<p>As I create the segmentations, they are all saved in one file, is there any way to save each segmentation in a different one?</p>
<p>Or maybe is there any way to corelate the slice of the segmentation with the slice of the study, like adding a tag for the segmentation with number of slice regarding the main study?</p>

---

## Post #6 by @cpinter (2022-02-07 14:06 UTC)

<p>What you do is saving the <em>whole scene</em> into a non-standard DICOM secondary capture that has the scene MRB file in its blob field. What you want instead is to export the segmentation to DICOM SEG. For that you need to install the <a href="https://qiicr.gitbook.io/quantitativereporting-guide/">Quantitative Reporting</a> extension.</p>

---

## Post #7 by @WojtekL (2022-02-07 14:19 UTC)

<p>Hello,</p>
<p>thank you for the answer. I do have the Quantitaive Reporting extension installed and I managed to succesfully export the segmentation to DICOM SEG.</p>
<p>After doing so, I only encountered the issue described in the following thread <a href="https://discourse.slicer.org/t/matching-segmentation-with-the-input-data/21817">https://discourse.slicer.org/t/matching-segmentation-with-the-input-data/21817</a></p>
<p>Do you know why a situation described in the thread above happens? <a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>Thank you</p>

---

## Post #8 by @koeglfryderyk (2022-03-02 16:02 UTC)

<p>I downloaded the latest preview release (version 4.13.0, revision 30669, built 2022-03-02, MacOS) but I cannot find the extension in the extension manager</p>
<p>(I can find and install it in the stable release (version 4.11.20210226, revision 29738, built 2021-02-28, MacOS)</p>

---
