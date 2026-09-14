---
topic_id: 48151
title: "An Extension for colon tumor detection/localization on CT scan in 3D Slicer?"
date: 2026-09-13
url: https://discourse.slicer.org/t/48151
last_bumped: 2026-09-14T05:23:06.475Z
---

# An Extension for colon tumor detection/localization on CT scan in 3D Slicer?

**Topic ID**: 48151
**Date**: 2026-09-13
**URL**: https://discourse.slicer.org/t/an-extension-for-colon-tumor-detection-localization-on-ct-scan-in-3d-slicer/48151

---

## Post #1 by @qn_Huynh (2026-09-13 16:21 UTC)

<p>An Extension for colon tumor detection/localization on CT scan in 3D Slicer</p>
<p><strong>I am very interested in the project developed by Xu and colleagues, entitled “An Open-Source Implementation of Colon CAD in 3D Slicer.” The article is available here: <a href="https://doi.org/10.1117/12.844370" class="inline-onebox-loading" rel="noopener nofollow ugc">https://doi.org/10.1117/12.844370</a></strong></p>
<p><strong>I am currently working on my master’s thesis in a related field, focusing on the application of artificial intelligence to CT scans for detecting primary colorectal tumors. However, I have been unable to locate the source code or download the extension from the website referenced in the original article:</strong></p>
<p><strong><a href="http://www2.wfubmc.edu/ctc/download/" class="inline-onebox-loading" rel="noopener nofollow ugc">http://www2.wfubmc.edu/ctc/download/</a></strong></p>
<p><strong>Does anyone know where the source code for this 3D Slicer extension can be obtained? Alternatively, are there any similar open-source or free extensions or plug-ins currently available for 3D Slicer that could be used for colon CAD or the detection of colorectal tumors on CT images?</strong></p>
<p><strong>Original article:</strong></p>
<p><strong>Haiyong Xu, H. Donald Gage, and Pete Santago, “An open source implementation of colon CAD in 3D Slicer,” <em>Proceedings of SPIE 7624, Medical Imaging 2010: Computer-Aided Diagnosis</em>, 762421 (9 March 2010).</strong></p>
<p><strong>Referenced download link:<br>
<a href="http://www2.wfubmc.edu/ctc/download/" class="inline-onebox-loading" rel="noopener nofollow ugc">http://www2.wfubmc.edu/ctc/download/</a></strong></p>
<p><strong>Slicer Community Work List:<br>
<a href="https://www.slicer.org/wiki/Main_Page/SlicerCommunity/2005-2010" class="inline-onebox-loading" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Main_Page/SlicerCommunity/2005-2010</a></strong></p>

---

## Post #2 by @lassoan (2026-09-14 04:40 UTC)

<p>This paper was published 16 years ago. Most likely the module is no longer relevant. I would recommend to review papers that are published in the past 3-4 years.</p>

---

## Post #3 by @qn_Huynh (2026-09-14 05:11 UTC)

<p>I have already researched plenty of recent papers and found out that, although numerous models and modules are available, most are provided primarily as code on GitHub and require a Python environment such as Anaconda, which I am not very familiar with in usage. However, I have not yet found a model or module integrated into 3D Slicer for this purpose—for example, lesion detection and liver segmentation similar to those offered by TotalSegmentator.</p>
<p>Hopefully, an extension for 3D Slicer that supports these applications will become available soon.</p>

---

## Post #4 by @lassoan (2026-09-14 05:23 UTC)

<p>You can tell any state-of-the-art coding agent to create a 3D Slicer extension from a github repository. I’ve tried it several times in the past few months and it always worked. Make sure to let the agent connect to Slicer (I usually point to <a href="https://gist.github.com/lassoan/b2e83a928c8d59a65b3ecd7cff527d4e">this page</a>) and iterate on the module until everything works well.</p>
<p>Installing dependencies may need some guidance (e.g., use Slicer’s pytorch extension to install pytorch, skip unnecessary dependencies and relax some package requirements), but this only becomes important when you submit to the Slicer Extensions Index. Anaconda should not be needed.</p>

---
