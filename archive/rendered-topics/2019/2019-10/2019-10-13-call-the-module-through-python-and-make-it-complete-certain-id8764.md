---
topic_id: 8764
title: "Call The Module Through Python And Make It Complete Certain"
date: 2019-10-13
url: https://discourse.slicer.org/t/8764
---

# Call the module through Python and make it complete certain work or modify some of the default values in the module

**Topic ID**: 8764
**Date**: 2019-10-13
**URL**: https://discourse.slicer.org/t/call-the-module-through-python-and-make-it-complete-certain-work-or-modify-some-of-the-default-values-in-the-module/8764

---

## Post #1 by @yulaomao (2019-10-13 03:29 UTC)

<p>Hi,<br>
I want to call the module through Python and make it complete certain work or modify some of the default values in the module.<br>
For example, in “volume rendering” module, “preset” is set to "CT - bones ".<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16893f6d4ae7ad0a98f55259ae26ebb50b27200c.png" data-download-href="/uploads/short-url/3dmyuvfhlJSbE9ZhPJjyvBIypVa.png?dl=1" title="L%7D%60(K6%40E63ZW3)~C2N4PP)J" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16893f6d4ae7ad0a98f55259ae26ebb50b27200c.png" alt="L%7D%60(K6%40E63ZW3)~C2N4PP)J" data-base62-sha1="3dmyuvfhlJSbE9ZhPJjyvBIypVa" width="601" height="500" data-dominant-color="F6F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">L%7D%60(K6%40E63ZW3)~C2N4PP)J</span><span class="informations">652×542 23.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-10-13 03:33 UTC)

<p>See in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_volume_rendering_automatically_when_a_volume_is_loaded" rel="nofollow noopener">example in the script repository</a> how to show volume rendering with a certain preset.</p>

---

## Post #3 by @yulaomao (2019-10-13 04:08 UTC)

<p>Thank you for your reply. I really don’t know about it and I don’t have much time to study. May I ask if you can tell me who can help me complete the series of tasks I need? I can pay a certain salary. Thanks very much.</p>

---

## Post #4 by @lassoan (2019-10-13 11:17 UTC)

<p>You just need to copy-paste a few lines from example that you can find at the link that I gave. I copy the code here:</p>
<pre data-code-wrap="python"><code class="lang-python">import SampleData
volumeNode = SampleData.SampleDataLogic().downloadMRHead()

volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName('MR-Default'))
displayNode.SetVisibility(True)
</code></pre>
<aside class="quote no-group" data-username="yulaomao" data-post="3" data-topic="8764">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yulaomao/48/78556_2.png" class="avatar"> yulaomao:</div>
<blockquote>
<p>you can tell me who can help me complete the series of tasks I need? I can pay a certain salary</p>
</blockquote>
</aside>
<p>You can <a href="https://discourse.slicer.org/c/announcements/jobs">post here to offer a job</a> or contact <a href="https://www.slicer.org/wiki/CommercialUse#Commercial_Partners">Slicer commercial partners</a>.</p>

---
