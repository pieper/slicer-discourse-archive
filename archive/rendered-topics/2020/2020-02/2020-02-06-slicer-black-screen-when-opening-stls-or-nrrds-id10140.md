---
topic_id: 10140
title: "Slicer Black Screen When Opening Stls Or Nrrds"
date: 2020-02-06
url: https://discourse.slicer.org/t/10140
---

# Slicer - black screen when opening stls or nrrds

**Topic ID**: 10140
**Date**: 2020-02-06
**URL**: https://discourse.slicer.org/t/slicer-black-screen-when-opening-stls-or-nrrds/10140

---

## Post #1 by @Mikolaj (2020-02-06 14:57 UTC)

<p>Hi!<br>
I’m having problem with Slicer. When importing stl or nrrd (drag’n drop or import) the programme shows only black screens. Literally nothing happens.<br>
Another thing is that I don’t know how to install sequences extension.</p>

---

## Post #2 by @Mikolaj (2020-02-06 16:04 UTC)

<p>Installing done <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"> But nrrd problem stayed.</p>

---

## Post #3 by @pieper (2020-02-06 17:54 UTC)

<p>Sounds like this kind of issue:</p>
<aside class="quote quote-modified" data-post="9" data-topic="1574">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/soheil_sabet/48/4231_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/black-screen-after-downloading-slicer/1574/9">Black screen after downloading Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi. I use a 64bit Windows 10 Enterprise version. I tried both 4.10 and 4.11 versions but still have the same problem and at start up I see only 4 black rectenangles. <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d587d0de2c4651a0264b2ad26f200cc68a7d3c9a.png" data-download-href="/uploads/short-url/usYGuHXidDElUeGOj8bGInWT12i.png?dl=1" title="Slicer%20Problem" rel="noopener nofollow ugc">[Slicer%20Problem]</a>
  </blockquote>
</aside>

<aside class="quote" data-post="4" data-topic="6902">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/why-i-have-black-screen/6902/4">Why I have black screen?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for the additional information. If you update graphics card drivers to the latest version and/or upgrade the operating system to Windows10 then there may be a chance that Slicer will work on that computer.
  </blockquote>
</aside>


---

## Post #4 by @Mikolaj (2020-02-06 20:16 UTC)

<p>Installed newest drivers for nvidia mx250. It’s a laptop (MSI PS42 8RA).</p>
<p>Nothing’s changed <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>
<p>Tried with samples from embodi3d as well as with official slicer samples.</p>
<p>As for the guy who had 4 black rectangles - I see 3 with 4th being the pink cube.</p>
<p>Dicoms work fine.</p>

---

## Post #5 by @lassoan (2020-02-07 16:37 UTC)

<aside class="quote no-group" data-username="Mikolaj" data-post="4" data-topic="10140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c89c15/48.png" class="avatar"> Mikolaj:</div>
<blockquote>
<p>As for the guy who had 4 black rectangles - I see 3 with 4th being the pink cube.</p>
</blockquote>
</aside>
<p>This means that it is probably not an OpenGL issue then.</p>
<p>STL files only supposed to show up in the 3D view by default. Click in the 3D view and click the small rectangle icon to center the view to the scene content. You may also hit <kbd>r</kbd> key to reset zoom.</p>
<p>nrrd files should show up in slice views. You can go to Volumes module to check if the file was loaded correctly (has reasonable dimensions and range of values).</p>

---

## Post #6 by @lassoan (2020-02-08 18:44 UTC)

<p>I received the images from <a class="mention" href="/u/mikolaj">@Mikolaj</a> and they were all loaded without issues. The two nrrds and models are all at different locations - you need to click the center field of view to make sure they show up in the selected view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7302e1c78dc4cc7b459d2b466d6959d79c6a3a9.jpeg" data-download-href="/uploads/short-url/wZbwj8QLuaBgXWat1kAWfqmK5K1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7302e1c78dc4cc7b459d2b466d6959d79c6a3a9_2_690x441.jpeg" alt="image" data-base62-sha1="wZbwj8QLuaBgXWat1kAWfqmK5K1" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7302e1c78dc4cc7b459d2b466d6959d79c6a3a9_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7302e1c78dc4cc7b459d2b466d6959d79c6a3a9_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7302e1c78dc4cc7b459d2b466d6959d79c6a3a9_2_1380x882.jpeg 2x" data-dominant-color="A6A6AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 449 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @Mikolaj (2020-02-08 20:22 UTC)

<p>Installed new 4.11 slicer - makes no difference <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=9" title=":confused:" class="emoji" alt=":confused:"> Center or not, it just doesn’t load the files.</p>
<p>Checked on my friends 'kintosh - all works well there, and according to your instruction - one of the objects was waaaay out of the box <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #8 by @Mikolaj (2020-02-08 20:38 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75c71d359ea1eca1e131ebd8a2ea0e42050e1eb8.png" data-download-href="/uploads/short-url/gNUsLK4Rzy8DfAuGUvlhjwAEJbq.png?dl=1" title="slicer problem 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75c71d359ea1eca1e131ebd8a2ea0e42050e1eb8_2_690x388.png" alt="slicer problem 1" data-base62-sha1="gNUsLK4Rzy8DfAuGUvlhjwAEJbq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75c71d359ea1eca1e131ebd8a2ea0e42050e1eb8_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75c71d359ea1eca1e131ebd8a2ea0e42050e1eb8_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75c71d359ea1eca1e131ebd8a2ea0e42050e1eb8_2_1380x776.png 2x" data-dominant-color="A5A5A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer problem 1</span><span class="informations">1920×1080 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c6e4466dc5789957e5e0b6e69d9b56ff14f402c.png" data-download-href="/uploads/short-url/hKLs4dz4ypKJk2Q42xT10bTgnjC.png?dl=1" title="slicer problem 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c6e4466dc5789957e5e0b6e69d9b56ff14f402c_2_690x388.png" alt="slicer problem 2" data-base62-sha1="hKLs4dz4ypKJk2Q42xT10bTgnjC" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c6e4466dc5789957e5e0b6e69d9b56ff14f402c_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c6e4466dc5789957e5e0b6e69d9b56ff14f402c_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c6e4466dc5789957e5e0b6e69d9b56ff14f402c_2_1380x776.png 2x" data-dominant-color="C9C9C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer problem 2</span><span class="informations">1920×1080 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3dfc76703e91a2747d6476ee94889d6925f154a.png" data-download-href="/uploads/short-url/rWMy9tJcsyyiksNmGsufSNZNr2W.png?dl=1" title="slicer problem 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3dfc76703e91a2747d6476ee94889d6925f154a_2_690x388.png" alt="slicer problem 3" data-base62-sha1="rWMy9tJcsyyiksNmGsufSNZNr2W" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3dfc76703e91a2747d6476ee94889d6925f154a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3dfc76703e91a2747d6476ee94889d6925f154a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3dfc76703e91a2747d6476ee94889d6925f154a_2_1380x776.png 2x" data-dominant-color="A6A6A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer problem 3</span><span class="informations">1920×1080 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d7174d799a069df23f2a528fd689fa5670e7668.png" data-download-href="/uploads/short-url/msO2BRxVsNeQrVUgR7yI790Rf4Y.png?dl=1" title="slicer problem 4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d7174d799a069df23f2a528fd689fa5670e7668_2_690x388.png" alt="slicer problem 4" data-base62-sha1="msO2BRxVsNeQrVUgR7yI790Rf4Y" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d7174d799a069df23f2a528fd689fa5670e7668_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d7174d799a069df23f2a528fd689fa5670e7668_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d7174d799a069df23f2a528fd689fa5670e7668_2_1380x776.png 2x" data-dominant-color="67676F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer problem 4</span><span class="informations">1920×1080 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2020-02-08 21:09 UTC)

<p>Oh, I see your screenshots now. Files cannot be loaded from folders that contain special characters. ASCII maybe Latin1 characters are safe, but many Polish characters are not. Rename the parent folders or move your files to a different directory. I’ve <a href="https://issues.slicer.org/view.php?id=4723">submitted an issue</a> to improve Slicer in this (at least display a meaningful error message).</p>

---

## Post #10 by @Mikolaj (2020-02-10 16:21 UTC)

<p>Thanks Andras!<br>
That solved the problem :D. Main user name also had special characters so… only main directory</p>
<p>Big Thanks!</p>

---
