# Unable to load CT Files

**Topic ID**: 26219
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/unable-to-load-ct-files/26219

---

## Post #1 by @cepehde (2022-11-14 03:47 UTC)

<p>Operating system: Windows 10<br>
Slicer version:5.0.3<br>
Expected behavior:  Load CT files<br>
Actual behavior:  Error about data base</p>
<p>Have not had issues over the last couple of years loading CT scans.  Received error message below and thought was the particular study.   Tried other studies that have worked in past and now getting this message.</p>
<p>Getting following message:</p>
<p>“Could not create a DICOM database with default settings.  Please create a new database or update the existing incompatible database using options in DICOM browser”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3414e6b75f1ef0aab40f79980eb8e40e6f381d6e.png" data-download-href="/uploads/short-url/7qJBLArl9I056DC4b3tdW1y4DsG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3414e6b75f1ef0aab40f79980eb8e40e6f381d6e_2_690x388.png" alt="image" data-base62-sha1="7qJBLArl9I056DC4b3tdW1y4DsG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3414e6b75f1ef0aab40f79980eb8e40e6f381d6e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3414e6b75f1ef0aab40f79980eb8e40e6f381d6e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3414e6b75f1ef0aab40f79980eb8e40e6f381d6e_2_1380x776.png 2x" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-11-14 15:59 UTC)

<p>The yellow box in the upper right is saying it can’t create files in your <code>G\</code> drive, but your file browser indicates that’s a DVD.  Use the button to select a writable location.</p>

---

## Post #3 by @lassoan (2022-11-14 18:06 UTC)

<p>Probably the source of confusion is the difference between these folders:</p>
<ul>
<li>DICOM database location: a writeable folder where essential metadata about inspected DICOM folders are stored - this must be somewhere on a local disk (e.g., in your user or Documents folder). You need to select this the first time you load DICOM images by clicking on <code>Select database folder</code> in the box highlighted in yellow.</li>
<li>Folder containing DICOM files you want to load: these can be anywhere, on a read-only and/or remove drive. You select this when you click on <code>Import DICOM files</code> button or drag-and-drop a folder to the application window.</li>
</ul>

---

## Post #4 by @cepehde (2022-11-15 12:26 UTC)

<p>Thank you for the help ! Solved my problem.</p>
<p>Collin</p>

---
