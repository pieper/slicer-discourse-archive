---
topic_id: 35180
title: "Default Terminology Entry In Application Settings"
date: 2024-03-30
url: https://discourse.slicer.org/t/35180
---

# Default terminology entry in Application Settings

**Topic ID**: 35180
**Date**: 2024-03-30
**URL**: https://discourse.slicer.org/t/default-terminology-entry-in-application-settings/35180

---

## Post #1 by @muratmaga (2024-03-30 17:27 UTC)

<p>Through this <a href="https://discourse.slicer.org/t/locking-a-segment-for-edits/35156/10">thread</a>, I just noticed that it is possible to set the default terminology entry through application settings. But when I go there and choose my terminology, select button grays out (and it stay grayed out for every other entry in the dropdown, including slicer’s defaults segmentation terminology).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddd18095225c9ed9957d06610943bf30448c359e.jpeg" data-download-href="/uploads/short-url/vEinpcGIIymDB9B4SPCknv52am2.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddd18095225c9ed9957d06610943bf30448c359e_2_632x500.jpeg" alt="image" data-base62-sha1="vEinpcGIIymDB9B4SPCknv52am2" width="632" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddd18095225c9ed9957d06610943bf30448c359e_2_632x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddd18095225c9ed9957d06610943bf30448c359e_2_948x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddd18095225c9ed9957d06610943bf30448c359e_2_1264x1000.jpeg 2x" data-dominant-color="E3E3E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1334×1054 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is in 5.6.1</p>

---

## Post #2 by @chir.set (2024-03-30 17:45 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="35180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>select button grays out</p>
</blockquote>
</aside>
<p>Found that it grays out whenever an item in the left list has been unselected; and remains gray even if all the items are selected again.</p>

---

## Post #3 by @lassoan (2024-03-30 19:06 UTC)

<p>If you choose a property then the “Select” button becomes enabled and you can click on it to accept the selection.</p>

---

## Post #4 by @chir.set (2024-03-30 19:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="35180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>then the “Select” button becomes enabled</p>
</blockquote>
</aside>
<p>Yes indeed, it was too obvious <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @muratmaga (2024-03-30 23:13 UTC)

<p>I might have misunderstood what this selection achieves. I want to make the custom terminology i installed as the default terminology to be used. I thought thats what the selection achieves.<br>
I dont need to select a term.</p>

---

## Post #6 by @lassoan (2024-03-31 02:20 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="35180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I might have misunderstood what this selection achieves. I want to make the custom terminology i installed as the default terminology to be used. I thought thats what the selection achieves.</p>
</blockquote>
</aside>
<p>That’s exactly what this does.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="35180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I dont need to select a term.</p>
</blockquote>
</aside>
<p>You have to select a complete term, because this will be used in the Segment Editor by default for new segments if you don’t select anything else.</p>

---

## Post #7 by @SoYoung_Lim (2024-04-15 03:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc65e47fdb40e9d4f547935a57d5ae4b417395c2.png" data-download-href="/uploads/short-url/A0OCPQlsUi2CrBqL1jRHL1tGiMW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc65e47fdb40e9d4f547935a57d5ae4b417395c2.png" alt="image" data-base62-sha1="A0OCPQlsUi2CrBqL1jRHL1tGiMW" width="690" height="396" data-dominant-color="3D3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">764×439 8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hi, I was trying to apply custom terminology by default when I added the segmentation layer, but it failed, though I changed the preference setting as the image above. Can anyone tell me the point that I misunderstood the process?</p>

---

## Post #8 by @lassoan (2024-04-21 12:37 UTC)

<p>I’ve tested this and it works well.</p>
<p>Color for segments with default terminology is automatically generated (to avoid using the same color for all segments). Maybe this was what you did not expect?</p>
<p>If a module registers the terminology dynamically then the terminology entry is not available at startup and you will get a warning message. Maybe you find this message misleading? The setting is still used, so you can ignore the warning. To fix it, you can make your module copy the terminology file to the application settings folder or you add the file manually using the “add file” buttons in the terminology selector:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d495fd5da0ada315cbab218f6c12bc455baa7443.png" data-download-href="/uploads/short-url/ukCzF5PRo2QpttZ6GMVMyOoyMEz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d495fd5da0ada315cbab218f6c12bc455baa7443_2_690x480.png" alt="image" data-base62-sha1="ukCzF5PRo2QpttZ6GMVMyOoyMEz" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d495fd5da0ada315cbab218f6c12bc455baa7443_2_690x480.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d495fd5da0ada315cbab218f6c12bc455baa7443_2_1035x720.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d495fd5da0ada315cbab218f6c12bc455baa7443_2_1380x960.png 2x" data-dominant-color="404852"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1847×1287 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>User-defined terminology files are stored in the <code>Terminologies</code> subfolder in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">application settings folder</a>. On Windows, it is something like this: <code>c:\Users\YourUserName\AppData\Roaming\slicer.org\Terminologies</code>. You can get this folder name by calling <code>slicer.modules.terminologies.logic().GetUserContextsPath()</code>.</p>

---

## Post #9 by @SoYoung_Lim (2024-04-22 07:16 UTC)

<p>Thank you for the reply!</p>

---
