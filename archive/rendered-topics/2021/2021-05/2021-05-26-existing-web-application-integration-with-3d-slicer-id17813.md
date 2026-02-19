---
topic_id: 17813
title: "Existing Web Application Integration With 3D Slicer"
date: 2021-05-26
url: https://discourse.slicer.org/t/17813
---

# Existing Web application integration with 3D Slicer

**Topic ID**: 17813
**Date**: 2021-05-26
**URL**: https://discourse.slicer.org/t/existing-web-application-integration-with-3d-slicer/17813

---

## Post #1 by @klm-1992 (2021-05-26 16:18 UTC)

<p>I have an existing web application where we are able to search for images and display it in OHIF viewer. We have a new requirement where we need to integrate the 3D slicer viewer as well. Can I know how can I run it in the web browser and also have it customized to pass the images information so that it can display those images?</p>
<p>Any help would be appreciated. Thanks.</p>

---

## Post #2 by @lassoan (2021-05-26 16:21 UTC)

<p>This should be no problem at all. See this post for details: <a href="https://discourse.slicer.org/t/new-dicomweb-features-launch-slicer-from-web-browser-and-download-upload-data-sets-to-the-cloud-using-dicomweb/17811" class="inline-onebox">New DICOMweb features: launch Slicer from web browser and download/upload data sets to the cloud using DICOMweb</a></p>
<p><a class="mention" href="/u/pieper">@pieper</a> as far as I remember, you have already experimented with adding a Slicer launcher button in OHIF viewer (similar to the one in Kheops). Can you give some more details about it?</p>

---

## Post #3 by @klm-1992 (2021-05-26 16:32 UTC)

<p>Thanks for the quick reply. I need to launch 3D slicer in the browser in a new window itself from another custom web application - let’s say on the click of view button for Study 1. When this view button is clicked, it should open 3D slicer in the new browser window. In the previous link, I see it launched the 3D slicer locally from a web application. My aim is to view it in the browser itself and I should be able to pass the image’s metadata from my end. Any idea?</p>
<p>Also OHIF viewer has this slicer functionality? We have already integrated the OHIF viewer.</p>

---

## Post #4 by @lassoan (2021-05-26 16:39 UTC)

<p>You can either launch a locally installed Slicer (using a custom URL as shown in the linked post above) or a cloud-hosted Slicer (by spinning up a virtual machine or docker container, and instruct Slicer to load data from a URL using <a href="https://github.com/pieper/SlicerWeb">SlicerWeb</a>).</p>
<p>Launching a locally installed Slicer has the advantages that you offload computationally intensive tasks to the user computer (you don’t need to set up servers with strong graphics capabilities) and interactions will be very smooth. The disadvantages are that images must be transferred to the user computer (same way as for the OHIF viewer or other viewers that run locally) and that the user needs to download and install Slicer.</p>

---

## Post #5 by @pieper (2021-05-26 17:55 UTC)

<p><a class="mention" href="/u/klm-1992">@klm-1992</a> it sounds like you want something like what is shown in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="vTGQMDIqL9k" data-video-title="teamplay+Slicer 2017 02 10" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=vTGQMDIqL9k" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/vTGQMDIqL9k/maxresdefault.jpg" title="teamplay+Slicer 2017 02 10" width="" height="">
  </a>
</div>

<p>Here the Slicer instance is running in a <a href="https://github.com/pieper/SlicerDockers">docker instance</a> that is monitoring a database where job requests are placed.  The job request is basically just a json object with the urls and access tokens passed from the web app to Slicer so it can open the data selected in the web app.  This example used a Siemens commercial system dicom archive, but the same thing can be set up with DICOMweb stores (e.g. running on Google or elsewhere).</p>

---

## Post #6 by @klm-1992 (2021-05-27 06:00 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>. WIll check this out. Meanwhile any idea if you ever integrated slicer button with OHIF viewer?</p>

---

## Post #7 by @pieper (2021-05-27 18:37 UTC)

<p>The last time we had a chance to work on this together was a <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/OHIFSlicerBridge/">Project Week in Las Palmas</a> and I had a mostly working prototype that adds a tool button to OHIF that launches a containerized Slicer instance in Google Cloud.  I didn’t finish up passing the data reference to the Slicer instance, but this can be set so that Slicer can communicate with the same DICOMweb endpoint that OHIF uses.  Now that we have better DICOMweb support in Slicer it would be great to flesh this out, perhaps at the <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/">upcoming Project Week</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcb7c9a206f5fd5fc4404beb7bff516d5008b95c.jpeg" data-download-href="/uploads/short-url/vuyO0RIMYqEKSxGKdXyMXRaXCIQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dcb7c9a206f5fd5fc4404beb7bff516d5008b95c_2_690x390.jpeg" alt="image" data-base62-sha1="vuyO0RIMYqEKSxGKdXyMXRaXCIQ" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dcb7c9a206f5fd5fc4404beb7bff516d5008b95c_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dcb7c9a206f5fd5fc4404beb7bff516d5008b95c_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dcb7c9a206f5fd5fc4404beb7bff516d5008b95c_2_1380x780.jpeg 2x" data-dominant-color="A3A4A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2200×1246 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/pieper/658731a7ef77231711c651ec622a6432">
  <header class="source">

      <a href="https://gist.github.com/pieper/658731a7ef77231711c651ec622a6432" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/pieper/658731a7ef77231711c651ec622a6432" target="_blank" rel="noopener">https://gist.github.com/pieper/658731a7ef77231711c651ec622a6432</a></h4>

  <h5>Google VM launcher from OHIF</h5>
  <pre><code class="">&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;meta charset="utf-8" /&gt;

    &lt;meta
      name="description"
      content="Open Health Imaging Foundation DICOM Viewer"
    /&gt;
    &lt;meta</code></pre>
    This file has been truncated. <a href="https://gist.github.com/pieper/658731a7ef77231711c651ec622a6432" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @klm-1992 (2021-05-31 08:12 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> ,</p>
<p>Thanks for the update. Wanted to know more related to the example of siemens commercial system…Do you have any more idea related to this to whom we can reach out to so that we can clarify our doubts? I’m a bit unclear as to how are we passing the json object with the urls and access tokens from the UI or do you have any documentation link? Any help would be appreciated. Thanks!!</p>

---

## Post #9 by @pieper (2021-06-08 19:16 UTC)

<p>Hi <a class="mention" href="/u/klm-1992">@klm-1992</a> -</p>
<p>The Siemens prototype was based on their APIs at the time, which were internal and subject to change.  I believe though that they were moving towards standards-based APIs like DICOMweb.  Probably <a href="https://www.siemens-healthineers.com/digital-health-solutions/teamplay-digital-health-platform/teamplay-digital-health-platform-as-a-service">a site like this</a> would have good contact info to start with.</p>
<p>For that prototype it was a bit ad hoc.  I set up a dedicated database where the teamplay client could post requests (json documents containing credentials) that were tagged by userID which the slicer instances could claim if they were owned by that user.  A better design would be to allocate Slicer instances as needed but that hasn’t been fleshed out yet.  I’ll probably keep working on it as <a href="https://discourse.slicer.org/t/pw35-projects-list/17905/8">part of this project</a>.</p>

---
