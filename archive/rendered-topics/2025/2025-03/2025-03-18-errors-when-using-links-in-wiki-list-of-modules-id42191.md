# Errors when using links in wiki list of modules

**Topic ID**: 42191
**Date**: 2025-03-18
**URL**: https://discourse.slicer.org/t/errors-when-using-links-in-wiki-list-of-modules/42191

---

## Post #1 by @robertf (2025-03-18 00:33 UTC)

<p>When I try to use some links at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Modules/</a>, I get the message</p>
<pre><code class="lang-auto">502 Bad Gateway
---
nginx
</code></pre>
<p>That has happened repeatedly for ResampleScalarVectorDWIVolume and ResampleDTIVolume, for example, but some links work correctly (e.g., AnglePlanes).</p>
<p>For ResampleDTIVolume I got the message</p>
<pre><code class="lang-auto">Internal error
Jump to: navigation, search
[17a0c848e45ece58783383c6] 2025-03-18 00:11:58: Fatal exception of type "Error"
</code></pre>

---

## Post #2 by @muratmaga (2025-03-18 03:38 UTC)

<p>Documentation has been moved to <a href="https://slicer.readthedocs.io" rel="noopener nofollow ugc">https://slicer.readthedocs.io</a> a while ago, but those hard coded URLs in module documentation are difficult to change:<br>
This is the link you should be using:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html" class="inline-onebox" rel="noopener nofollow ugc">Resample Scalar/Vector/DWI Volume — 3D Slicer documentation</a></p>

---

## Post #3 by @robertf (2025-03-19 00:38 UTC)

<p>Thank you for the pointer.<br>
I had found that documentation, but then I saw the message ‘This documentation is still a work in progress. Additional module documentation is available on the <a href="https://www.slicer.org/wiki/Documentation/Nightly" rel="noopener nofollow ugc">Slicer wiki</a>’, so I wasn’t sure which documentation I should be looking at.<br>
I was (am) also confused by the fact that some of the links on the wiki still work.<br>
Would it be feasible to put dummy pages in the wiki that link to the current documentation?</p>

---

## Post #4 by @muratmaga (2025-03-19 02:20 UTC)

<p>I think all those wiki pages should redirect to the readthedocs, and I think there was some discussion of that recently on the forum, though not sure when that can happen.</p>

---
