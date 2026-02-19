---
topic_id: 35594
title: "Appimage For Linux Systems"
date: 2024-04-18
url: https://discourse.slicer.org/t/35594
---

# Appimage - for linux systems

**Topic ID**: 35594
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/appimage-for-linux-systems/35594

---

## Post #1 by @Bob5 (2024-04-18 11:36 UTC)

<p>Hi! Building/installing 3dslicer on some linux systems is not easy, not fast, not fun.</p>
<p>Is it possible to provide appimage for download? Just like many of software do, freecad, cura slicer, kicad etc.</p>
<p>Thank You for Your help with this!</p>

---

## Post #2 by @jamesobutler (2024-04-18 14:29 UTC)

<p>Does the Linux binary provided at <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a> not fit your easy-to-use situation? Which distro of Linux are you using?</p>
<p>There has been some past discussion on Linux distribution to support networkless builds by way of Flatpaks. Do you have any thoughts as it relates to that method?</p>
<aside class="quote quote-modified" data-post="35" data-topic="16532">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/interest-to-create-flatpak-for-3d-slicer-have-issue-with-guisupportqtopengl-not-found/16532/35">Interest to create Flatpak for 3D Slicer, have issue with GUISupportQtOpenGL not found</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    From worse to better: 

AppImages: “fail in everything they set out to do” → Don’t use them.


Linux apps running everywhere → They don’t
Easy to install apps as in Windows or Mac → They are not.
Provide applications without the need to ‘get into a distribution’ or ‘build for a different distributions’ → Practically, you need to learn every distro and build one.


Snaps → Practically confined to Canonical ecosystems.



Still very limited to Ubuntu ecosystem (won’t deliver confinement in most Li…
  </blockquote>
</aside>


---

## Post #3 by @Bob5 (2024-04-18 23:40 UTC)

<p>Arch , from AUR 3dslicer-bin have sha256 mismatch so it fail to build.</p>
<p>I build it but it took like forever and sill got some problems (like it  dont want to load dicom module).</p>
<p>I will try once again with Your suggestions, thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Ps. Never get problems with appimages mentioned above on various linux systems and machines. They are updatable and easy to use. But maybe not so easy to properly make an appimage? Flatpacks would be a bad choice - I 100% agree.</p>

---
