# When creating a extension using Slicer5.9, I've found that the only available type options are "default" and "superbuild".

**Topic ID**: 42963
**Date**: 2025-05-16
**URL**: https://discourse.slicer.org/t/when-creating-a-extension-using-slicer5-9-ive-found-that-the-only-available-type-options-are-default-and-superbuild/42963

---

## Post #1 by @zhaokaien (2025-05-16 12:45 UTC)

<p>I have successfully built Slicer using the 5.9 source code. However, when I use the generated Slicer application and try to create an extension, in the Extension Wizard interface, I only see two options for “Type” when creating a new extension, as shown in the image below. Could you please help me understand what’s happening and how to resolve this? env is:window11<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7fb635083ef41a2e605febb706c9bc9fcabe816.png" data-download-href="/uploads/short-url/x6cTikQFBNlJC4oQz6M1M1G2uUu.png?dl=1" title="微信图片_20250516183200" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7fb635083ef41a2e605febb706c9bc9fcabe816_2_690x357.png" alt="微信图片_20250516183200" data-base62-sha1="x6cTikQFBNlJC4oQz6M1M1G2uUu" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7fb635083ef41a2e605febb706c9bc9fcabe816_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7fb635083ef41a2e605febb706c9bc9fcabe816_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7fb635083ef41a2e605febb706c9bc9fcabe816.png 2x" data-dominant-color="BBBAC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20250516183200</span><span class="informations">1355×702 62.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-05-16 12:48 UTC)

<p>If you are not sure about then choose <code>default</code>. The other option is for advanced use, when you build an extension that fetches and builds C++ libraries from external repositories.</p>

---

## Post #3 by @zhaokaien (2025-05-18 01:43 UTC)

<p>Thank you for your guidance. It’s not that I’m unsure about the two options in the dropdown menu, but I’m confused about why there are only two options. In previous versions of others, this dropdown menu had many options, such as “scripted,” “loadable” etc. However, I don’t see these options here. I’m wondering if this is because I’m using a newer version (V5.9+) or if something is missing.</p>

---

## Post #4 by @lassoan (2025-05-18 02:02 UTC)

<p>The options you remember are still there. First you create an extension (default or superbuild) then you create modules (scripted, loadable, segment editor effect, cli, …).</p>

---

## Post #5 by @zhaokaien (2025-05-18 11:40 UTC)

<p>OK，thank you very much ,Iassoan！ <img src="https://emoji.discourse-cdn.com/twitter/grinning_face.png?v=14" title=":grinning_face:" class="emoji" alt=":grinning_face:" loading="lazy" width="20" height="20"></p>

---
