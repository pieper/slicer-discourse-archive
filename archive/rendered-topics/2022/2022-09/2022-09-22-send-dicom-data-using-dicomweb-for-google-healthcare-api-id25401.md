---
topic_id: 25401
title: "Send Dicom Data Using Dicomweb For Google Healthcare Api"
date: 2022-09-22
url: https://discourse.slicer.org/t/25401
---

# Send DICOM data using DICOMWeb for Google Healthcare API

**Topic ID**: 25401
**Date**: 2022-09-22
**URL**: https://discourse.slicer.org/t/send-dicom-data-using-dicomweb-for-google-healthcare-api/25401

---

## Post #1 by @DeepaKrishnaswamy (2022-09-22 16:40 UTC)

<p>Hi,</p>
<p>I am trying to use the option ‘Send to DICOM server’ for a series in the DICOM database, (using the latest version of Slicer - 5.1.0-2022-09-20). I’m using the DICOMweb protocol and the destination address is a Google Healthcare DICOM datastore that I have already created and populated with some data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f839bdf3c9bbfe48d6d75e0814bcf65d791620ad.png" data-download-href="/uploads/short-url/zpU7HXitsAo6kgsThWFDxLUpOyh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f839bdf3c9bbfe48d6d75e0814bcf65d791620ad.png" alt="image" data-base62-sha1="zpU7HXitsAo6kgsThWFDxLUpOyh" width="690" height="100" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1199×175 7.75 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when I use the ‘Send to DICOM server’, I get the following 404 Client Error:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fab1697e97c21dc993fbb3022c31ba0ed66c67b.png" alt="image" data-base62-sha1="4w9m6jlPBhtVDOib1PflX8B6ITp" width="499" height="133"></p>
<p>I checked that I can access the data in this DICOM datastore using the DICOMwebBrowser. However, I noticed that in the ‘send’ function in DICOMLib\DICOMProcesses.py, there is no authorization for the Google Healthcare API (though I see kheops). Perhaps I am looking in the wrong place, or have the incorrect URL, so any insight would be appreciated.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2022-09-22 17:28 UTC)

<p>Hi Deepa - Yes, I believe the google healthcare DICOMweb is only implemented as part of the SlicerDICOMwebBrowser extension, and that only handles downloads and not uploads currently.</p>
<p>You would need to add something like these lines from the extension into the Send code.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerDICOMwebBrowser/blob/main/DICOMwebBrowser/DICOMwebBrowser.py#L543-L545">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerDICOMwebBrowser/blob/main/DICOMwebBrowser/DICOMwebBrowser.py#L543-L545" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerDICOMwebBrowser/blob/main/DICOMwebBrowser/DICOMwebBrowser.py#L543-L545" target="_blank" rel="noopener">lassoan/SlicerDICOMwebBrowser/blob/main/DICOMwebBrowser/DICOMwebBrowser.py#L543-L545</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="543" style="counter-reset: li-counter 542 ;">
          <li>if "googleapis.com" in self.serverUrl:</li>
          <li>  # Google Healthcare API</li>
          <li>  headers["Authorization"] = f"Bearer {GoogleCloudPlatform().token()}"</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It makes me think we should move all the DICOMweb code into the core and refactor a bit to allow Kheops and GCP authentication support to be plugins to a generic interface.  It’s not a lot of code.</p>

---
