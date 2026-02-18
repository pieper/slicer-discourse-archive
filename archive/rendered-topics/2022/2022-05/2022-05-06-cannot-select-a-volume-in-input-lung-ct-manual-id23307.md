# Cannot select a volume in Input lung CT manual 

**Topic ID**: 23307
**Date**: 2022-05-06
**URL**: https://discourse.slicer.org/t/cannot-select-a-volume-in-input-lung-ct-manual/23307

---

## Post #1 by @zhongheng (2022-05-06 12:50 UTC)

<p>Dear Sir,<br>
Thank you for your excellent package for processing lung image; However, when I loaded a series of lung CT in .tiff format, I follow the instruction for “Lung CT Analyzer”. I found I cannot select a volume (i.e. when I click on the tool bar, there is no dropdown list). The same problem occurs for the “lung CT segmenter” module. Can you give me some hints to solve this problem? <a class="mention" href="/u/rbumm">@rbumm</a></p>

---

## Post #2 by @rbumm (2022-05-06 13:03 UTC)

<p>Which version of 3D Slicer and Lung CT Analyzer are you using?</p>
<p>You should maybe</p>
<p>(1) Restart Slicer<br>
(2) download the ChestCT dataset in the “Sample Data” module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3856cfd6f5c027180198db7a2948304896c4be71.png" data-download-href="/uploads/short-url/82oJnwGalLm0nNCwmL2DYral11n.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3856cfd6f5c027180198db7a2948304896c4be71_2_334x500.png" alt="image" data-base62-sha1="82oJnwGalLm0nNCwmL2DYral11n" width="334" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3856cfd6f5c027180198db7a2948304896c4be71_2_334x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3856cfd6f5c027180198db7a2948304896c4be71.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3856cfd6f5c027180198db7a2948304896c4be71.png 2x" data-dominant-color="C6C3C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">410×612 77.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(3) switch to the Lung CT Segmenter extension, you should be able to select CTChest in “Input Volume” dropdown list:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73663abfcd7d4a4110e7b1d7d5ce2a4191abb763.png" alt="image" data-base62-sha1="gsRVXgm8UZP2odfEBxvPBEZ6A5Z" width="493" height="289"></p>
<p>(4) perform the segmentation process with the demo dataset.</p>
<p>Let us know whether you can do (1) to (4).</p>
<p>As soon as you are familiar with the process restart Slicer. Try to load your local CT data as a DICOM dataset. You would need to export the CT from your PACS in DICOM format (as if you would have to burn it on a CD). Then redo the segmentation process.</p>

---

## Post #3 by @bagginstyrone (2022-05-13 11:38 UTC)

<p>Thank you so much <a class="mention" href="/u/rbumm">@rbumm</a>. Your instructions are working.</p>

---
