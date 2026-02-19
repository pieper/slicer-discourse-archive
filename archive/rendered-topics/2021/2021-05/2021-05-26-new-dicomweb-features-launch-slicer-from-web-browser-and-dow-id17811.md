---
topic_id: 17811
title: "New Dicomweb Features Launch Slicer From Web Browser And Dow"
date: 2021-05-26
url: https://discourse.slicer.org/t/17811
---

# New DICOMweb features: launch Slicer from web browser and download/upload data sets to the cloud using DICOMweb

**Topic ID**: 17811
**Date**: 2021-05-26
**URL**: https://discourse.slicer.org/t/new-dicomweb-features-launch-slicer-from-web-browser-and-download-upload-data-sets-to-the-cloud-using-dicomweb/17811

---

## Post #1 by @lassoan (2021-05-26 14:45 UTC)

<p>Modern DICOM cloud storage services and applications increasingly use DICOMweb protocol instead of classic (DIMSE) DICOM networking. Three new features have been added to 3D Slicer to support cloud-based DICOM workflows.</p>
<p>The new features are demonstrated in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="60_hzSlptWY" data-video-title="Using 3D Slicer with cloud DICOMweb databases" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=60_hzSlptWY" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/60_hzSlptWY/maxresdefault.jpg" title="Using 3D Slicer with cloud DICOMweb databases" width="690" height="388">
  </a>
</div>

<h2><a name="p-60223-h-1-launch-3d-slicer-directly-from-the-web-browser-1" class="anchor" href="#p-60223-h-1-launch-3d-slicer-directly-from-the-web-browser-1" aria-label="Heading link"></a>1. Launch 3D Slicer directly from the web browser</h2>
<p>The application can be launched on a study selected in a DICOM browser. For example, <a href="https://kheops.online/">Kheops</a> DICOM cloud sharing platform has a View in 3D Slicer button:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7a36c06c3a093105e52208a1a7e5b9db3a5e5a7.jpeg" data-download-href="/uploads/short-url/nUZRMOIPok4tCVG8q8DKp8VZr9B.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a36c06c3a093105e52208a1a7e5b9db3a5e5a7_2_690x444.jpeg" alt="image" data-base62-sha1="nUZRMOIPok4tCVG8q8DKp8VZr9B" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a36c06c3a093105e52208a1a7e5b9db3a5e5a7_2_690x444.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a36c06c3a093105e52208a1a7e5b9db3a5e5a7_2_1035x666.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a36c06c3a093105e52208a1a7e5b9db3a5e5a7_2_1380x888.jpeg 2x" data-dominant-color="5D5E60"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2238×1442 471 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>3D Slicer is opened and download link and access code is passed to the application by opening a custom URL in the format: <code>slicer://viewer/?studyUID=...&amp;access_token=...&amp;dicomweb_endpoint=...&amp;dicomweb_uri_endpoint=...</code>.</p>
<p>The custom URL must be associated with 3D Slicer application. This association is created automatically when recent 3D Slicer Preview Release is installed on Windows and can be <a href="https://support.shotgunsoftware.com/hc/en-us/articles/219031308-Launching-Applications-Using-Custom-Browser-Protocols">registered manually on other platforms</a>.</p>
<h2><a name="p-60223-h-2-browse-and-download-content-from-dicomweb-databases-2" class="anchor" href="#p-60223-h-2-browse-and-download-content-from-dicomweb-databases-2" aria-label="Heading link"></a>2. Browse and download content from DICOMweb databases</h2>
<p>DICOMweb Browser module (in DICOMwebBrowser extension) has been added that allows connecting to any DICOMweb database (Kheops, DCM4CHEE, Orthanc, Google Cloud Healthcare API, <a href="https://github.com/dcmjs-org/dicomweb-server">DCM.js lightweight server</a>, etc), locally or on the cloud. The browser supports quick switching between servers, filtering, local caching of downloaded results.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c376b9f4fdf7eceb450c172f7271ce1e3daa7ff.jpeg" data-download-href="/uploads/short-url/d9MFe1OorrejPtL3vBfqH3Dq5c3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c376b9f4fdf7eceb450c172f7271ce1e3daa7ff_2_690x419.jpeg" alt="image" data-base62-sha1="d9MFe1OorrejPtL3vBfqH3Dq5c3" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c376b9f4fdf7eceb450c172f7271ce1e3daa7ff_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c376b9f4fdf7eceb450c172f7271ce1e3daa7ff_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c376b9f4fdf7eceb450c172f7271ce1e3daa7ff_2_1380x838.jpeg 2x" data-dominant-color="AEAAA7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1372 511 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-60223-h-3-upload-data-sets-from-3d-slicer-to-dicomweb-databases-3" class="anchor" href="#p-60223-h-3-upload-data-sets-from-3d-slicer-to-dicomweb-databases-3" aria-label="Heading link"></a>3. Upload data sets from 3D Slicer to DICOMweb databases</h2>
<p>The downloaded images, segmentations, or other data sets can be edited in 3D Slicer and then uploaded back to the web database to share it with others.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cd6d1053d02dabe78e05a2e88a3317a658b465e.png" data-download-href="/uploads/short-url/mnsJ6QQI7TOtkbJQHg6BWRI6H38.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cd6d1053d02dabe78e05a2e88a3317a658b465e_2_690x420.png" alt="image" data-base62-sha1="mnsJ6QQI7TOtkbJQHg6BWRI6H38" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cd6d1053d02dabe78e05a2e88a3317a658b465e_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cd6d1053d02dabe78e05a2e88a3317a658b465e_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cd6d1053d02dabe78e05a2e88a3317a658b465e_2_1380x840.png 2x" data-dominant-color="EEEBDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1375 326 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @KSC_IA (2023-02-11 17:34 UTC)

<p>Hello Dr Lasso.</p>
<p>The functionality offered with DICOMweb Browser is super interesting. We are running an Orthanc Research Server, but it’s gated by a username/password. Does it support entering username/password combinations?</p>
<p>I look forward to your reply.</p>

---

## Post #3 by @lassoan (2023-02-12 12:55 UTC)

<p>Probably you need to add authentication information to the request or its header. This is inplemented and tested for accessing Google Cloud Platform storage and Kheops - see around here: <a href="https://github.com/lassoan/SlicerDICOMwebBrowser/blob/dd7cd4a1535a246724f0580e2416cf33cbe1d0b9/DICOMwebBrowser/DICOMwebBrowser.py#L543" class="inline-onebox">SlicerDICOMwebBrowser/DICOMwebBrowser.py at dd7cd4a1535a246724f0580e2416cf33cbe1d0b9 · lassoan/SlicerDICOMwebBrowser · GitHub</a></p>
<p>You would probably need to modify the code around there to allow authentication with your server.</p>

---
