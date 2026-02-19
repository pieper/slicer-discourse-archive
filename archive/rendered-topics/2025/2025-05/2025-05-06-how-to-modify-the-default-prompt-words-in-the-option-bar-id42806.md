---
topic_id: 42806
title: "How To Modify The Default Prompt Words In The Option Bar"
date: 2025-05-06
url: https://discourse.slicer.org/t/42806
---

# How to modify the default prompt words in the option bar

**Topic ID**: 42806
**Date**: 2025-05-06
**URL**: https://discourse.slicer.org/t/how-to-modify-the-default-prompt-words-in-the-option-bar/42806

---

## Post #1 by @slicer365 (2025-05-06 05:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d66ebf8ff945a1ef2016796648736daf22f11086.png" data-download-href="/uploads/short-url/uAXsg4zCQrnbnDcT9r2liYbvZT8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d66ebf8ff945a1ef2016796648736daf22f11086.png" alt="image" data-base62-sha1="uAXsg4zCQrnbnDcT9r2liYbvZT8" width="503" height="224"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">503×224 4.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I know that these contents may be determined by the underlying code of the program, such as “Select a Node”, “Select a Model”, and so on. Sometimes I need to design a slicer module, for example, in other languages, but there is no way to modify these default display prompt words. Is there a better way? I don’t plan to compile the entire source code.</p>
<p>Thank you very much !</p>

---

## Post #2 by @jamesobutler (2025-05-06 11:58 UTC)

<p>I would suggest reviewing the following extension which makes Slicer available in other languages than the default English.</p>
<aside class="quote quote-modified" data-post="1" data-topic="24421">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicerlanguagepacks-new-extension-for-translating-user-interface-of-slicer-to-various-languages/24421">SlicerLanguagePacks: New extension for translating user interface of Slicer to various languages</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We added a new extension that allows translators to see the translation results immediately. It can download and install nightly translations with a single click. It can also install latest translations that are downloaded from Crowdin website. 
See <a href="https://github.com/Slicer/SlicerLanguagePacks#how-to-use" rel="noopener nofollow ugc">setup and usage instructions on the extension’s website</a>. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8a9f91e78ccddca78f5b131061a6b29952dee1.png" data-download-href="/uploads/short-url/1MWJbgSVNR3mTBdKPCqPwJFkYSd.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
Currently, it requires downloading and installing the Qt toolkit, which is not very convenient (it can take 10-15 minutes). In the near future we will remove this requirement - see d…
  </blockquote>
</aside>


---
