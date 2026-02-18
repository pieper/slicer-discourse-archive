# Do I need to re-download the sample data every time I reopen 3D Slicer and use the SlicerLiver extension?

**Topic ID**: 41841
**Date**: 2025-02-23
**URL**: https://discourse.slicer.org/t/do-i-need-to-re-download-the-sample-data-every-time-i-reopen-3d-slicer-and-use-the-slicerliver-extension/41841

---

## Post #1 by @feiyu (2025-02-23 04:29 UTC)

<p><strong>After downloading and installing the slicerliver extension, in order to test the extension, when loading LiverVolume and LiverSementation data from the sample data module, it took too long to load. I guess it was a network transmission problem. I couldn’t get the data from the cloud. Is there any other way to get the data so that I can load it locally?</strong></p>
<p><strong>Do I need to re-download the sample data every time I reopen 3D Slicer and use the SlicerLiver extension?</strong></p>

---

## Post #2 by @feiyu (2025-02-23 04:52 UTC)

<p>he latest version of SlicerLiver has been downloaded, but when loading LiverVolume, the message “File already exists in cache but checksum is different - re-downloading it” appears. However, the download takes a long time and eventually results in an error. How can this issue be resolved?</p>

---

## Post #3 by @pieper (2025-02-23 16:06 UTC)

<p>It sounds like the checksum is incorrect, perhaps in the extension source code.   You could doublecheck and suggest a change to the SlicerLiver maintainers.  By design the SampleData should be read from the cache and not redownloaded.</p>

---

## Post #4 by @RafaelPalomar (2025-02-24 09:10 UTC)

<p><a class="mention" href="/u/feiyu">@feiyu</a>, I can’t reproduce this behavior. Data load works correctly on my end with Slicer-5.8.0 (GNU/Linux). Maybe your data was corrupted on the first download. That could be a reason for checksum failure. You could delete your cached data and try again. You can also download the data manually  form <a href="https://github.com/ALive-research/ALiveResearchTestingData/releases/tag/SHA256" class="inline-onebox" rel="noopener nofollow ugc">Release SHA256 · ALive-research/ALiveResearchTestingData · GitHub</a> (you will have to rename the files when you download them as their name is a hash)</p>

---

## Post #5 by @feiyu (2025-02-26 10:42 UTC)

<p>Thank you to all the experts for your replies. I tried clearing the cache and persisted with the download for an hour, finally succeeding. It failed no less than 10 times during the process, but fortunately, it worked out in the end.</p>

---
