# Issue when build an extension

**Topic ID**: 30695
**Date**: 2023-07-20
**URL**: https://discourse.slicer.org/t/issue-when-build-an-extension/30695

---

## Post #1 by @haphantran (2023-07-20 03:21 UTC)

<p>Hi all,<br>
We’re trying to build the extension and publish it to extension Manager.<br>
It’s a Python base extension and I’m following the steps in this link for Windows.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#windows" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a><br>
I’m having trouble understand this step:<br>
<code>* Specify </code>Slicer_DIR<code>by replacing</code>Slicer_DIR-NOTFOUND<code>by the Slicer inner-build folder (for example</code>c:/D/SD/Slicer-build<code>).</code><br>
I think it is required to build Slicer from source code, but in another part of the doc, we have this:</p>
<pre><code class="lang-auto">If developing modules in Python only, then it is not necessary to build the extension.
</code></pre>
<p>So do I need to build Slicer from source code?<br>
I was trying to do it but couldn’t find the link to download and setup qt correctly.<br>
Please help on this topic.<br>
Thank you!!!</p>

---

## Post #2 by @pieper (2023-07-20 13:02 UTC)

<p>As I recall, you need to have a fully built local Slicer in order to package an extension for redistribution, but if you are just developing and only using python you don’t need that step.  If your are going to submit to the slicer extension index then packaging will happen on the Slicer factory machine build trees.</p>

---

## Post #3 by @lassoan (2023-07-20 13:28 UTC)

<aside class="quote no-group quote-modified" data-username="haphantran" data-post="1" data-topic="30695">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/haphantran/48/18446_2.png" class="avatar"> haphantran:</div>
<blockquote>
<blockquote>
<p><code>If developing modules in Python only, then it is not necessary to build the extension.</code></p>
</blockquote>
</blockquote>
</aside>
<p>This note is in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension">Build an extension section</a> of the documentation and means that you can <em>develop, use, and test</em> Python modules without building anything. However, if you want to build and extension package, you still need to built Slicer, as the packaging infrastructure relies on having a complete build tree of Slicer.</p>
<p>I agree that it would be nice to have a way to create packages of Python-only extensions. Feel free to submit a feature request for this (by creating a new topic in the <a href="https://discourse.slicer.org/c/support/feature-requests/9">Feature requests</a> category) and as more people vote on it, it will get higher on the priority list.</p>

---

## Post #4 by @haphantran (2023-07-21 04:15 UTC)

<p>Thank you for the answer. I’m trying to download Qt 5.15.2 but not sure which one I should download from this list. Can you comment on that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16af12c9660d0195475e56ef0011bd2560e8f3e7.png" data-download-href="/uploads/short-url/3eFB2cTQEgWq3y3Bgf33GdKNTT1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16af12c9660d0195475e56ef0011bd2560e8f3e7_2_690x469.png" alt="image" data-base62-sha1="3eFB2cTQEgWq3y3Bgf33GdKNTT1" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16af12c9660d0195475e56ef0011bd2560e8f3e7_2_690x469.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16af12c9660d0195475e56ef0011bd2560e8f3e7_2_1035x703.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16af12c9660d0195475e56ef0011bd2560e8f3e7.png 2x" data-dominant-color="EEEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1238×843 67.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @jcfr (2023-07-21 04:32 UTC)

<p>Based on the screenshot, it looks you are on a web page regarding embedded linux, instead I suggest you do the following:</p>
<ol>
<li>Go to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html" class="inline-onebox">Build Instructions — 3D Slicer documentation</a></li>
<li>Click on the <code>Install prerequisites</code> or <code>Prerequisites</code> corresponding to your platform</li>
<li>Click on the link related to Qt</li>
</ol>

---

## Post #6 by @haphantran (2023-07-25 19:36 UTC)

<p>Thank you Jean.<br>
I followed the instruction on the link, for Qt, here is the screenshot. Slicer required Qt 5.15.2.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99ef4af026d8557a2123e5c4309b6b2f99d1d5a0.png" data-download-href="/uploads/short-url/lXLJAqd63rGW8tIDZquiE6Ixzl6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99ef4af026d8557a2123e5c4309b6b2f99d1d5a0_2_690x201.png" alt="image" data-base62-sha1="lXLJAqd63rGW8tIDZquiE6Ixzl6" width="690" height="201" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99ef4af026d8557a2123e5c4309b6b2f99d1d5a0_2_690x201.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99ef4af026d8557a2123e5c4309b6b2f99d1d5a0_2_1035x301.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99ef4af026d8557a2123e5c4309b6b2f99d1d5a0_2_1380x402.png 2x" data-dominant-color="242525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1471×430 73.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The link get me to Online Qt installer, which is currently Qt version 6 only.<br>
For offline installer, they only provided link for 5.14 and lower, as per this annoucement.<br>
<a href="https://download.qt.io/archive/qt/5.15/5.15.2/OFFLINE_README.txt" rel="noopener nofollow ugc">download.qt.io/archive/qt/5.15/5.15.2/OFFLINE_README.txt</a><br>
Do you or anyone have the offline installer for Qt 5.15?</p>

---

## Post #7 by @haphantran (2023-07-25 19:55 UTC)

<p>Correction from this post: The current online installer has 5.15 and Qt 6.xx. I will try this and update you guys if successful.</p>

---
