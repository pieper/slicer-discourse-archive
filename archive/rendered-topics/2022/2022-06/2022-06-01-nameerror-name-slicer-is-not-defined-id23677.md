# NameError: name 'slicer' is not defined

**Topic ID**: 23677
**Date**: 2022-06-01
**URL**: https://discourse.slicer.org/t/nameerror-name-slicer-is-not-defined/23677

---

## Post #1 by @sunshine (2022-06-01 19:36 UTC)

<p>Windows 10, Slicer 5.0.2, jupyter server 5.0</p>
<p>NameError: name ‘slicer’ is not defined</p>
<p>Please refer to this screenshot:       <a href="https://ibb.co/pdtfLX2" class="inline-onebox" rel="noopener nofollow ugc">Capture — ImgBB</a></p>
<p>In the cmd history, we can see that the scene file is loaded successfully, however, I always failed to call the slicer.util.getNode command.</p>
<p>This code works well in version Slicer 4.13, and the error appears in version 5.02.</p>

---

## Post #2 by @Nicolas_Larragueta (2024-04-13 13:11 UTC)

<p>could you resolve it?</p>

---

## Post #3 by @lassoan (2024-04-13 15:46 UTC)

<p>You can add <code>import slicer</code> to the line before to avoid this issue.</p>

---
