---
topic_id: 25335
title: "Automation Monailabel Functionality"
date: 2022-09-19
url: https://discourse.slicer.org/t/25335
---

# Automation MONAILabel functionality

**Topic ID**: 25335
**Date**: 2022-09-19
**URL**: https://discourse.slicer.org/t/automation-monailabel-functionality/25335

---

## Post #1 by @lukasvanderstricht (2022-09-19 10:55 UTC)

<p>Hi everyone</p>
<p>I am using MONAILabel to train models to automatically segment certain body parts on MRI/CT images.<br>
The training went well and I have a decent model. I am interested in volumetric properties of the segmentation I have made with <em>Automatic segmentation</em>.<br>
With the help of some existing blog posts and such, I have already succeeded in writing a <code>Python</code> script to generate a table with the <code>SegmentStatistics</code> module and save it locally as a <code>.csv</code> file.  I would however want to automate this process even further and include in my script the step where I press <em>Run</em> for the automatic segmentation in MONAILabel. I am looking for how I can translate this step to <code>Python</code> code, similar to <a href="https://discourse.slicer.org/t/using-segmentstatistics-module-in-python-script/2140">this</a>.</p>
<p>I found the <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/plugins/slicer/MONAILabel/MONAILabel.py" rel="noopener nofollow ugc">source code</a> for this module, and I suspect that the function I’m looking for is <code>onClickSegmentation</code> on <a href="https://github.com/Project-MONAI/MONAILabel/blob/df9de94ff8b668d896e5aed902338811a0aca281/plugins/slicer/MONAILabel/MONAILabel.py#L1446" rel="noopener nofollow ugc">line 1446</a>. The only problem is that I don’t know how to invoke this function in a <code>Python</code> script.</p>
<p>Thanks in advance!</p>
<p>Lukas</p>

---
