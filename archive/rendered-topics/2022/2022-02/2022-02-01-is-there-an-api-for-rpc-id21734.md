---
topic_id: 21734
title: "Is There An Api For Rpc"
date: 2022-02-01
url: https://discourse.slicer.org/t/21734
---

# Is there an API for RPC?

**Topic ID**: 21734
**Date**: 2022-02-01
**URL**: https://discourse.slicer.org/t/is-there-an-api-for-rpc/21734

---

## Post #1 by @swirlsky (2022-02-01 14:19 UTC)

<p>I’m wondering if there’s a way to instruct slicer from a remote application to load e.g. a DICOM Study or do other operations.</p>
<p>Like OsiriX has one: <a href="http://www.osirix-viewer.com/HIS-Integration.pdf" rel="noopener nofollow ugc">http://www.osirix-viewer.com/HIS-Integration.pdf</a></p>

---

## Post #2 by @pieper (2022-02-01 21:37 UTC)

<p>We don’t have an exact analog to that but for a while I’ve been working on <a href="https://github.com/pieper/SlicerWeb">SlicerWeb</a> to embed a web server that exposes slicer functionality as a service.  Basically you can define routes in the server and map them to python code to make Slicer do whatever you want.  I’ve been working to get it in the core <a href="https://github.com/Slicer/Slicer/pull/5999">in this PR</a> but it needs more work.</p>

---

## Post #3 by @lassoan (2022-02-02 03:21 UTC)

<p>In addition to SlicerWeb’s REST API, you can also use custom URL handlers (for example, to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#launch-slicer-directly-from-a-web-browser">load a data set from the web browser</a>), and for high-efficiency real-time data transfer (for example real time streaming of tool positions coming from surgical navigation systems to Slicer) you can use <a href="http://openigtlink.org/">OpenIGTLink</a>.</p>
<p><a class="mention" href="/u/swirlsky">@swirlsky</a> can you tell a bit more about your use case? What is your overall goal and what actions would you like Slicer to perform?</p>

---

## Post #4 by @swirlsky (2022-02-02 07:04 UTC)

<p>Thank you for your quick replies. My goal is to instruct Slicer from a web app to load a DICOM study from a PACS. As I understand, after I’ve configured a DICOM connection in Slicer, I could use the <code>slicer:</code> custom URL protocol to achieve this. I will give it a try. For a more sophisticated controlling from the browser, SlicerWeb sounds really promising.</p>

---

## Post #5 by @lassoan (2022-02-02 13:29 UTC)

<p>Yes, custom URL is the way to go for that, it is already set up with Kheops:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="60_hzSlptWY" data-video-title="Using 3D Slicer with cloud DICOMweb databases" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=60_hzSlptWY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/60_hzSlptWY/maxresdefault.jpg" title="Using 3D Slicer with cloud DICOMweb databases" width="" height="">
  </a>
</div>


---
