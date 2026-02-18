# Having Trouble Extracting Ultrasound DICOM/Vol file from GE Voluson S8

**Topic ID**: 18218
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/having-trouble-extracting-ultrasound-dicom-vol-file-from-ge-voluson-s8/18218

---

## Post #1 by @d_roscoe_j (2021-06-18 18:52 UTC)

<p>I’m attempting to create a 3d model of a 3d ultrasound .dcm file that I’d asked a 3d sonographer to extract, (for 3d printing) but all that is appearing when uploading to slicer is a 2d image of the ultrasound (in .dcm format)</p>
<p>She is using a GE Voluson S8 machine for the task, and doesn’t know how to extract the volume file I am needing… any advice or instruction for what to ask/tell her?</p>
<p>Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16d57e16bd2be4eef3c798e1b4fd2907507ecf84.jpeg" data-download-href="/uploads/short-url/3fZUq1otv3JFOZ8CCYxEq6570vG.jpeg?dl=1" title="Screenshot 2021-06-18 13.48.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16d57e16bd2be4eef3c798e1b4fd2907507ecf84_2_690x372.jpeg" alt="Screenshot 2021-06-18 13.48.48" data-base62-sha1="3fZUq1otv3JFOZ8CCYxEq6570vG" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16d57e16bd2be4eef3c798e1b4fd2907507ecf84_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16d57e16bd2be4eef3c798e1b4fd2907507ecf84_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16d57e16bd2be4eef3c798e1b4fd2907507ecf84_2_1380x744.jpeg 2x" data-dominant-color="A5A5BA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-06-18 13.48.48</span><span class="informations">1930×1042 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Operating system: GE Voluson S8<br>
Slicer version: 4.11.20200930<br>
Expected behavior: Loading 3d Volume from .dcm file<br>
Actual behavior: Loading a 2d image from .dcm file</p>

---

## Post #2 by @lassoan (2021-06-18 20:40 UTC)

<p>GE 3D ultrasound machines only store a 2D screenshot in standard DICOM image field and use private fields for the 3D volume. You can use <a href="https://github.com/SlicerHeart/SlicerHeart#ge">SlicerHeart extension</a> to load the 3D information (it will require you to request the image decoder pack from GE, by filling out a web form).</p>

---

## Post #3 by @d_roscoe_j (2021-06-18 20:48 UTC)

<p>So I, as the person doing the slicing, can use the SlicerHeart extension (and the image decoder pack from GE) to load 3d information from these seemingly 2D .dcm files the woman who took the ultrasounds sent over?<br>
The files are all around 2000 KB, which seems low for having 3d vol information, but is that decoder pack a means of “reading between the lines” of the 2D screenshotted .dcm file to get the 3d volume?</p>
<p>Or is that decoder pack something SHE would need on her end to get the right information out of the machine to send over to me for slicing?</p>
<p>Just making sure I understand.<br>
Really appreciate your help! Thanks!</p>

---

## Post #4 by @lassoan (2021-06-18 21:12 UTC)

<p>You need to have the decoder (not the patient or the ultrasound technologist).</p>
<p>2000KB seems to be a bit small, but it may contain a smaller region or lower resolution image. Size of a single 3D ultrasound volume is typically 3-5MB.</p>

---

## Post #5 by @Roxxx (2023-02-10 10:19 UTC)

<p>I have the same output view as seen in the first post when using SlicerHeart.<br>
I could not find the image decoder pack from GE you mention. Do you happen to have a URL of the web form?</p>

---

## Post #6 by @Jeff_Beckman (2023-04-11 15:52 UTC)

<p>I’m in the same boat and may have found the solution.  There are directions including a link to the required web form on this page in the docs:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md" target="_blank" rel="noopener nofollow ugc">SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md</a></h4>


      <pre><code class="lang-md"># Importing DICOM files

While DICOM standard specifies how 3D and 4D (3D+t) ultrasound volumes can be stored in standard fields, most ultrasound manufacturers do not follow this standard. Typically, only 2D screenshots or 2D+t screen capture videos are stored in standard fields. 3D information is stored in private fields and proprietary algorithms are needed to interpret them.

## Open Image3D API

[Image3D API](https://github.com/MedicalUltrasound/Image3dAPI) can be used to read 3D ultrasound images from GE, Canon, Hitachi, Siemens, and Philips scanners. This API is only avaialble on Windows and a reader library must be obtained from the scanner's manufacturer and installed on the system (by registering the reader by running `regsvr32 (loaderlibraryname).dll` as an administrator). This API can provide access to all kinds of image data and ECG signal. File can be read by renaming it so that it ends with `.3dus` and drag-and-dropping to the Slicer application window. GE 3D ultrasound images can be also loaded using the DICOM module (then the files do not have to be renamed).

Example import of 4D ultrasound sequence and ECG imported from GE system:

![](Image3dApiExample.png)

Additional vendor-specific file reading options are described below.

## Philips

### Import Philips 4D cardiac images:

Philips machines save 3D/4D ultrasound data in private fields. Method to extract volumetric images from these fields is not publicly disclosed. However, Philips QLAB cardiac analysis software can export images to a DICOM format variant, which stores volumetric images in standard fields, which can be interpreted without proprietary methods. Unfortunately, these DICOM files are not fully DICOM compliant (required fields, such as SOP instance UID, patient name, ID, study instance UID, and series instance UID fields are missing), therefore they need to be fixed up before they can be imported into a DICOM database.

</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The GE section is about half way down.  I haven’t gotten a response from GE yet, fingers crossed.</p>

---

## Post #7 by @MartinNA (2023-06-16 21:36 UTC)

<p>Hi<br>
I have a similar problem, I have .vol files from a voluson S8 ultrasound, the doctor gave me the files via USB, when I pass them to slicer an error appears and that it cannot load them. I don’t know if anyone has had the same problem and how do I solve it.</p>

---
