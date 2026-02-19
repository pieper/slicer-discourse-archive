---
topic_id: 3305
title: "Dashboard Errors Midas Upload Failed"
date: 2018-06-26
url: https://discourse.slicer.org/t/3305
---

# Dashboard errors: midas upload failed

**Topic ID**: 3305
**Date**: 2018-06-26
**URL**: https://discourse.slicer.org/t/dashboard-errors-midas-upload-failed/3305

---

## Post #1 by @fedorov (2018-06-26 15:25 UTC)

<p>Uploads for some of the extensions for Mac are failing today with the error below. Can one of the dashboard maintainers look into this? Seems like a configuration issue.</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1304988" class="onebox" target="_blank" rel="noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1304988</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26372110b44b8a8c44d75b9038a7680e7648e099.png" data-download-href="/uploads/short-url/5s4fY3M4ntIbIBxt5WGP786u1Zv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26372110b44b8a8c44d75b9038a7680e7648e099_2_690x262.png" alt="image" data-base62-sha1="5s4fY3M4ntIbIBxt5WGP786u1Zv" width="690" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26372110b44b8a8c44d75b9038a7680e7648e099_2_690x262.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26372110b44b8a8c44d75b9038a7680e7648e099_2_1035x393.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26372110b44b8a8c44d75b9038a7680e7648e099.png 2x" data-dominant-color="ECEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1250×476 43.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sam_Horvath (2018-06-26 16:00 UTC)

<p>Will look into this. From a quick check of the dashboard, it is failing to authenticate to the MIDAS server.</p>

---

## Post #3 by @Sam_Horvath (2018-06-26 17:18 UTC)

<p>I suspect that this might have been some intermittent network issue on the side of the server.  All of the extensions use the same auth details to upload, and it failed in a few cases, while all the others went fine.</p>
<p>The failures are clustered towards the beginning of the nightly build, but are not contiguous (some uploads succeeded between failures)</p>

---

## Post #4 by @Sam_Horvath (2018-06-27 14:03 UTC)

<p>Just a heads up, there are no mac preview builds today, looking into it.</p>

---

## Post #5 by @Sam_Horvath (2018-06-27 18:48 UTC)

<p>Connection errors that broke last night’s mac build were caused by a firewall upgrade.  Fixed now.  Not sure if the previous extension upload errors are related.</p>

---

## Post #6 by @fedorov (2018-06-27 19:17 UTC)

<p>Thanks!</p>
<p>Sounds like we need a test to test the test server! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=5" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
