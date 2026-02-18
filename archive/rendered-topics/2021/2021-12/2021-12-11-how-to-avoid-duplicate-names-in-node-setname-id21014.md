# How to avoid duplicate names in node.SetName()?

**Topic ID**: 21014
**Date**: 2021-12-11
**URL**: https://discourse.slicer.org/t/how-to-avoid-duplicate-names-in-node-setname/21014

---

## Post #1 by @jumbojing (2021-12-11 02:44 UTC)

<p>如何避免node.SetName()重名呢?<br>
比如,当重名时会自动添加数字,“N”,“N1”…</p>
<blockquote>
<p>How to avoid duplicate names in node.SetName()?<br>
For example, when the name is the same, the number will be automatically added, “N”, “N1”…</p>
</blockquote>

---

## Post #2 by @jumbojing (2021-12-11 02:53 UTC)

<p>解决了:</p>
<pre><code class="lang-auto">node.SetName(slicer.mrmlScene.GetUniqueNameByString("N"))
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8912972cabb8e4303d811ab1352ac59d69b0ef4.png" data-download-href="/uploads/short-url/zsVq4SBG8UyPEXCD7113i6MQVPm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8912972cabb8e4303d811ab1352ac59d69b0ef4.png" alt="image" data-base62-sha1="zsVq4SBG8UyPEXCD7113i6MQVPm" width="690" height="221" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">763×245 29.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
