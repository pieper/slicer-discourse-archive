# How to match two dose distributions (TPS and Monte Carlo results) and CT images automatically (editing metadata tags)?

**Topic ID**: 8074
**Date**: 2019-08-18
**URL**: https://discourse.slicer.org/t/how-to-match-two-dose-distributions-tps-and-monte-carlo-results-and-ct-images-automatically-editing-metadata-tags/8074

---

## Post #1 by @shahrokh (2019-08-18 12:44 UTC)

<p>Hi Dears 3DSlicer developers and users</p>
<p>My ultimate goal is to perform the <strong>Gamma analysis</strong> between two absorbed dose distributions using “Dose Comparison” module. These are the absorbed dose distributions obtained from calculations in the <em>Monte Carlo simulation</em> (<em>PRIMO code, in text format</em>) and <em>Treatment Planning System</em> (<em>ISOgray in DICOM RT-Dose format</em>).</p>
<p>It should be noted that the output file (absorbed dose distribution) of PRIMO code is in Text format. At firstly, it is converted to the Volume node using Python Interactor and then the Dose Volume node .</p>
<p>The specifics of these data are as follows.</p>
<blockquote>
<p><strong>CT</strong>:</p>
<p>Image Dimensions: 512 x 512 x 89</p>
<p>Image Spacing: 0.962891mm x 0.962891mm x 5.000000mm</p>
</blockquote>
<blockquote>
<p><strong>dose TPS</strong>:</p>
<p>Image Dimensions: 62 x 46 x 88</p>
<p>Image Spacing: 5mm x 5mm x 5mm</p>
</blockquote>
<blockquote>
<p><strong>dose PRIMO</strong>:</p>
<p>Image Dimensions: 256 x 256 x 89</p>
<p>Image Spacing: 1.925782mm x 1.925782mm x 5.000000mm</p>
</blockquote>
<p>The following figure is a demonstration of the current situation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/502cff95f7fde9069d8376ad48ae1af2f5798f28.jpeg" data-download-href="/uploads/short-url/brgBAkn9cnW0yBaWPqBLM0oZPCg.jpeg?dl=1" title="Screenshot%20from%202019-08-18%2016-57-39" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/502cff95f7fde9069d8376ad48ae1af2f5798f28_2_690x431.jpeg" alt="Screenshot%20from%202019-08-18%2016-57-39" data-base62-sha1="brgBAkn9cnW0yBaWPqBLM0oZPCg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/502cff95f7fde9069d8376ad48ae1af2f5798f28_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/502cff95f7fde9069d8376ad48ae1af2f5798f28_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/502cff95f7fde9069d8376ad48ae1af2f5798f28_2_1380x862.jpeg 2x" data-dominant-color="8A655E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202019-08-18%2016-57-39</span><span class="informations">1440×900 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>In the first step</strong>, I want to match the two absorbed dose distributions and CT images with together. After doing it, I want to normalize them.</p>
<p>I <strong>do not</strong> want to use <em>manual transform methods</em> to do this (this method is subjective).</p>
<p>I noticed in the following link that this may be possible to do matching (2 dose distribution and CT images) through editing metadata tags.</p>
<p><strong>Title</strong>: VTK - Users - Matching CT and RT dose coordinates<br>
<strong>Address</strong>: <a>http://vtk.1045678.n5.nabble.com/Matching-CT-and-RT-dose-coordinates-td3397428.html</a></p>
<p>As mentioned Scott Johnson in this link that “<em>If the FrameOfReferenceUIDs of the CT and the RT dose are the same, they both exist in the same coordinate system, if they don’t, you will have to register the dose to the CT somehow</em>”, Is this my understanding right?<br>
I think this is possible because as shown in the figure above, the images are physically the same size.<br>
In the other words, is it possible to match two absorbed dose distributions through the Metadata tags?</p>
<p>OR</p>
<p>Can I match this data (Dose volume node of the PRIMO absorbed dose distribution) by <strong>Export to DICOM…</strong> (in 3DSlicer) and then adding some tags (such as FrameOfReferenceUID) to DICOM files with software such as <strong>DVTK</strong> or <strong>DicomBrowser</strong> and finally loading it with <strong>DICOM Browser</strong> module in 3DSlicer?</p>
<p>I am waiting for your guidance.<br>
Please guide me.</p>

---

## Post #2 by @lassoan (2019-08-18 13:43 UTC)

<p>I don’t think you should manually register the dose volumes. It would not make sense, since this would not be an option if you computed the dose for a patient CT either.</p>
<p>Computed dose volumes must be spatially aligned with the CT volumes (therefore with each other, if you use the same CT) without any registration. If they don’t then it is a software bug that must be fixed.</p>

---
