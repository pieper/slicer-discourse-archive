---
topic_id: 35145
title: "Slicer Looking Glass Extension Unavailable In Slicer 5 7 Rev"
date: 2024-03-27
url: https://discourse.slicer.org/t/35145
---

# Slicer Looking Glass extension unavailable in Slicer 5.7 revision 32785

**Topic ID**: 35145
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/slicer-looking-glass-extension-unavailable-in-slicer-5-7-revision-32785/35145

---

## Post #1 by @karthik_vandy (2024-03-27 22:37 UTC)

<p>We were looking to use the SlicerLookingGlass extension on Slicer3D but couldn’t find it in the extension manager. I have tried different keywords for search including “SlicerLookingGlass, Looking glass, Lookingglass, look, glass”. I have also looked through the full list of extensions in the manager to no avail.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac491728fafdcccda03a287d0f6942bef5c0b3e2.png" data-download-href="/uploads/short-url/oA6IFHhmnU9Mn3rG0PYv01AudJo.png?dl=1" title="Slicer_extensions" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac491728fafdcccda03a287d0f6942bef5c0b3e2_2_690x405.png" alt="Slicer_extensions" data-base62-sha1="oA6IFHhmnU9Mn3rG0PYv01AudJo" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac491728fafdcccda03a287d0f6942bef5c0b3e2_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac491728fafdcccda03a287d0f6942bef5c0b3e2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac491728fafdcccda03a287d0f6942bef5c0b3e2.png 2x" data-dominant-color="DFDBCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_extensions</span><span class="informations">1023×601 63.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Kindly do advise if I need to backdate my Slicer version to access the extension, if so, which latest preview release can I find the extension on? I have attempted download Windows, mac and linux machines. Could you please let us know of a solution?</p>

---

## Post #2 by @jamesobutler (2024-03-27 22:55 UTC)

<p>SlicerLookingGlass development has not kept up with updates to newer versions of VTK which it uses. You’re not alone in wondering about the status of this extension. See other post:</p>
<aside class="quote quote-modified" data-post="1" data-topic="33723">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicerlookingglass-plans/33723">SlicerLookingGlass plans</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all, 
I updated my development environment to the latest Slicer, and bumped into the issue that apparently the SlicerLookingGlass extension does not build anymore. 
I did some digging and it seems that the last time it was build successfully was the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2023-11-22&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=lookingglass" rel="noopener nofollow ugc">nightly of November 22</a>. 
The problem seems to be related to the event delegation improvements (<a href="https://github.com/Slicer/Slicer/commit/1cc3b2c62bf5d3836802d3aab4ce37feee6500f0" class="inline-onebox" rel="noopener nofollow ugc">ENH: Improve Event Delegation in qMRMLThreeDView and qMRMLSliceView · Slicer/Slicer@1cc3b2c · GitHub</a>), at least that is my guess. 
My question is whethe…
  </blockquote>
</aside>

<p>Currently with the latest Slicer stable (5.6.1) the SlicerLookingGlass extension is not building successfully across all platforms (Windows, macOS, Linux). See build details <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=LookingGlass" rel="noopener nofollow ugc">here</a>. These build errors are why SlicerLookingGlass cannot be found in the Extensions Manager.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> has been the primary developer of <a href="https://github.com/KitwareMedical/SlicerLookingGlass" rel="noopener nofollow ugc">SlicerLookingGlass</a> and may be able to respond about which version of Slicer was the extension last working. If he does not respond, you can write up an <a href="https://github.com/KitwareMedical/SlicerLookingGlass/issues/new" rel="noopener nofollow ugc">issue</a> in that repo to document the state of it not working with latest Slicer.</p>

---

## Post #3 by @Mark_Ryan (2024-08-01 12:44 UTC)

<p>I’ve had to keep a copy of version 5.2.2 to use the Looking Glass extension. Have the new Looking Glass Go and OLED 16-inch displays coming next week, so hopefully there is some kind of update forthcoming. Would also be interested to know if it is possible to export the “quilt” output to the display as a .hop file, so I can save the holograms for patient education purposes.</p>
<p>Have left a message on their GitHub repository but nothing yet. Last software update listed as 2 years ago.</p>

---

## Post #4 by @cpinter (2024-08-02 13:15 UTC)

<p>Based on the uncharacteristic silence about this particular topic, I assume there is some kind of legal issue that prevents Kitware from commenting about it altogether…</p>

---

## Post #5 by @Mark_Ryan (2024-08-02 17:23 UTC)

<p>I hope not. Messaged their sales division, since there isn’t much point in trying to convince my university to purchase one of the larger displays if it’s going to be such a struggle to look at medical images on it.</p>

---

## Post #6 by @Mark_Ryan (2024-08-04 19:14 UTC)

<p>Seems like there’s hope . . .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54a8f8afd5c32ca3e3219b2a6d59dad4f45a38cd.jpeg" data-download-href="/uploads/short-url/c4W7SJP8R80eiLxDyjDbqg8cwhf.jpeg?dl=1" title="1000008776" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54a8f8afd5c32ca3e3219b2a6d59dad4f45a38cd_2_690x124.jpeg" alt="1000008776" data-base62-sha1="c4W7SJP8R80eiLxDyjDbqg8cwhf" width="690" height="124" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54a8f8afd5c32ca3e3219b2a6d59dad4f45a38cd_2_690x124.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54a8f8afd5c32ca3e3219b2a6d59dad4f45a38cd_2_1035x186.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54a8f8afd5c32ca3e3219b2a6d59dad4f45a38cd_2_1380x248.jpeg 2x" data-dominant-color="3B3836"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000008776</span><span class="informations">1440×259 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
