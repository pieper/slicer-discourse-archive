---
topic_id: 44496
title: "I Want To Creat A Qmrmlnodecombobox To Choose One Of Fiducia"
date: 2025-09-16
url: https://discourse.slicer.org/t/44496
---

# I want to creat a qMRMLNodeCombobox to choose one of fiducial node

**Topic ID**: 44496
**Date**: 2025-09-16
**URL**: https://discourse.slicer.org/t/i-want-to-creat-a-qmrmlnodecombobox-to-choose-one-of-fiducial-node/44496

---

## Post #1 by @zhutouzjq (2025-09-16 12:49 UTC)

<p>I know this question may be stupid, but it has been already struggling me for several days.</p>
<p>as you see, there is a fiducial node in the CTA image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/642850957d4a297a1dcd8cd9e437f48f9cc2f819.png" data-download-href="/uploads/short-url/ei27vn9Hca407oFkkMEY8ZojoTv.png?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/642850957d4a297a1dcd8cd9e437f48f9cc2f819.png" alt="无标题" data-base62-sha1="ei27vn9Hca407oFkkMEY8ZojoTv" width="255" height="205"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">255×205 16.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and I  created a standard intial extension, insert a label called ‘lowerpoint’ and a qMRMLNodeCombobox.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f3b7ea089ab0f062f010c8813078deb6c1e760.png" data-download-href="/uploads/short-url/qfjxz5R1IxuU6x4b7FaxGMPd1ra.png?dl=1" title="无标题-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f3b7ea089ab0f062f010c8813078deb6c1e760.png" alt="无标题-1" data-base62-sha1="qfjxz5R1IxuU6x4b7FaxGMPd1ra" width="652" height="382"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题-1</span><span class="informations">652×382 4.37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to use this qMRMLNodeCombobox to choose the fiducial node, but the combobox is gray and can’t to interact with mouse. So, how can I use the combobox to choose the fiducial node?</p>

---

## Post #2 by @jamesobutler (2025-09-16 12:59 UTC)

<p>I suspect the qMRMLNodeComboBox doesn’t yet have the mrmlScene set for it. MRML widgets are grey like that when this is the case.</p>
<pre><code class="lang-auto">node_combobox.setMRMLScene(slicer.mrmlScene)
</code></pre>

---

## Post #3 by @zhutouzjq (2025-09-17 00:54 UTC)

<p>sincerely thank you for your anwser. Magic, with only one line of code, this problem is just sovled. Magic</p>

---

## Post #4 by @cpinter (2025-09-17 11:32 UTC)

<p>If you created the UI with Qt designer, I think the step that you missed was making the connection between the parent widget’s <code>mrmlSceneChanged</code> signal and the combobox’ <code>setMRMLScene</code> function. You can do it by switching to Edit Signals/Slots mode (F4). Normally if we create a UI in designer, we do that instead of adding this line in the code (that way there is no question about when to call it exactly).</p>

---

## Post #5 by @zhutouzjq (2025-09-18 01:26 UTC)

<p>yes，these operation in Qt is same to add a line of code.</p>
<p>for example, to activate the qMRMLNodeCombobox in the extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8a9634ee8ef08def2a3669600f368c28641b503.png" data-download-href="/uploads/short-url/o437S8oY8zMxrZ1YxW48h8ySQan.png?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8a9634ee8ef08def2a3669600f368c28641b503.png" alt="无标题" data-base62-sha1="o437S8oY8zMxrZ1YxW48h8ySQan" width="370" height="411"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">370×411 3.76 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i first change the nodetype of the new qMRMLNodeCombobox</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cbc7031f1affdffce94642eb5786bdff1a58cd6.png" data-download-href="/uploads/short-url/k50zwwyQAe8SV2DqKAwu0dPV1oW.png?dl=1" title="无标题-3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cbc7031f1affdffce94642eb5786bdff1a58cd6.png" alt="无标题-3" data-base62-sha1="k50zwwyQAe8SV2DqKAwu0dPV1oW" width="498" height="226"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题-3</span><span class="informations">498×226 4.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then press F4 as you say</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfd1c54386a30e8f250369a41a606d193aec77b9.png" data-download-href="/uploads/short-url/vVZUfwNXli8A3t5Sgd8MGnxH9SF.png?dl=1" title="无标题-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfd1c54386a30e8f250369a41a606d193aec77b9.png" alt="无标题-1" data-base62-sha1="vVZUfwNXli8A3t5Sgd8MGnxH9SF" width="373" height="418"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题-1</span><span class="informations">373×418 5.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>finally link the edge of widget to this qMRMLNodeCombobox, and choose this option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/effbaf5f4b9cb92f048b46242b73a72dda139e05.png" data-download-href="/uploads/short-url/yeZlAlz56dS3jrzetdbyKJkr0YR.png?dl=1" title="无标题-2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/effbaf5f4b9cb92f048b46242b73a72dda139e05.png" alt="无标题-2" data-base62-sha1="yeZlAlz56dS3jrzetdbyKJkr0YR" width="690" height="289" data-dominant-color="E1E4E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题-2</span><span class="informations">971×408 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>after reloading, the qMRMLNodeCombobox called upperpoint can also choose the fiducial points in markups.</p>

---
