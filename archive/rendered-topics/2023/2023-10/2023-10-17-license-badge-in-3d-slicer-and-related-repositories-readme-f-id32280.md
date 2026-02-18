# License badge in 3D Slicer and related repositories `README` files

**Topic ID**: 32280
**Date**: 2023-10-17
**URL**: https://discourse.slicer.org/t/license-badge-in-3d-slicer-and-related-repositories-readme-files/32280

---

## Post #1 by @jhlegarreta (2023-10-17 19:12 UTC)

<p>Hi,</p>
<p>I was about to add a License badge to the <code>README</code> files of some of our 3D Slicer-related repositories that use exactly the same license as 3D Slicer, and was<br>
going to do the same for 3D Slicer as I see that the badge is not displayed.</p>
<p>However, some concerns were raised about the shield,<br>
<a href="https://img.shields.io/badge/License-BSD-green.svg" class="inline-onebox" rel="noopener nofollow ugc">License: BSD</a></p>
<p>as the 3D Slicer license text may be a customized version of BSD, so the shield, or maybe the “BSD” text itself, may not be appropriate.</p>
<p>What are the thoughts about this? Maybe a custom text in the shield<br>
(e.g. BSD style) would be faithful enough for the license type?</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-10-17 22:01 UTC)

<p>You can read some background here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#license" class="inline-onebox">About 3D Slicer — 3D Slicer documentation</a></p>

---

## Post #3 by @jcfr (2023-10-17 22:01 UTC)

<p>For context, you may be interested in reading the following.<br>
See <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#license">https://slicer.readthedocs.io/en/latest/user_guide/about.html#license</a></p>

---

## Post #4 by @jcfr (2023-10-17 22:04 UTC)

<p>To help with this, we discussed submitting the Slicer license so that it is added to the SPDX license list.</p>
<p>This should then allow us to move forward with having the license detected by GitHub, which in turn should allow to automatically generate a badge.</p>
<aside class="quote quote-modified" data-post="1" data-topic="28664">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/proposal-add-the-slicer-license-to-spdx-license-list/28664">Proposal: Add the Slicer license to SPDX license list</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    <a name="what-is-the-spdx-license-list-1" class="anchor" href="#what-is-the-spdx-license-list-1"></a>What is the SPDX License List ?

The SPDX License List is an integral part of the SPDX Specification. The SPDX License List itself is a list of commonly found licenses and exceptions used in free and open or collaborative software, data, hardware, or documentation. The SPDX License List includes a standardized short identifier, the full name, the license text, and a canonical permanent URL for each license and exception. 

See <a href="https://spdx.org/licenses/" class="inline-onebox">SPDX License List | Software Package Data Exchange (SPDX)</a> 
<a name="why-should-we-add-the-slicer-license-2" class="anchor" href="#why-should-we-add-the-slicer-license-2"></a>Why should…
  </blockquote>
</aside>


---

## Post #5 by @jhlegarreta (2023-10-18 15:13 UTC)

<p>OK. Thanks for the answers, Steve and JC. Have gone through the information in the links pointed. It has been informative.</p>
<p>Thanks for all this work, and thanks <a class="mention" href="/u/jcfr">@jcfr</a> for having submitted the request yesterday to the SPDX list</p>

---
