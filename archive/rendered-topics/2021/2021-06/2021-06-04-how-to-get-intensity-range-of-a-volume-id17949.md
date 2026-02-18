# How to get intensity range of a volume?

**Topic ID**: 17949
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/how-to-get-intensity-range-of-a-volume/17949

---

## Post #1 by @Saima (2021-06-04 07:37 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="4457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"><a href="https://discourse.slicer.org/t/threshold-scalar-volume-to-labelmap/4457/1">Threshold scalar volume to labelmap</a></div>
<blockquote>
<p><code>volumeNo</code></p>
</blockquote>
</aside>
<p>how to get a scalar range value of a volume.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04b66b388a854ffd1f244b5bdbd3f88450e762a6.png" alt="image" data-base62-sha1="FGJUccgMfoAOWfKg5L4IRQwI1o" width="263" height="135"></p>

---

## Post #2 by @jamesobutler (2021-06-04 16:15 UTC)

<p>If you’re looking to get this range using Python, I searched the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">Script Repository</a> with the keywords “ScalarRange”. There is an example of get the scalar range in the following example:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded</a></p>

---
