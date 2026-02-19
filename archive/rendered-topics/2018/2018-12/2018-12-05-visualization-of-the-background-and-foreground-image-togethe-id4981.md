---
topic_id: 4981
title: "Visualization Of The Background And Foreground Image Togethe"
date: 2018-12-05
url: https://discourse.slicer.org/t/4981
---

# Visualization of the background and foreground image together

**Topic ID**: 4981
**Date**: 2018-12-05
**URL**: https://discourse.slicer.org/t/visualization-of-the-background-and-foreground-image-together/4981

---

## Post #1 by @alireza (2018-12-05 22:59 UTC)

<p>Hi<br>
Is there a way to view background and foreground images both at full opacity in one view?</p>
<p>Thanks</p>

---

## Post #2 by @cpinter (2018-12-05 23:12 UTC)

<p>If foreground is at full opacity then it will obscure everything underneath. The only way to see them on equal opacity is at 50-50.</p>
<p>Is your problem that it becomes darker that way? You can change the blending mode:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1ad04e4508037369305786c4ea5251424b7d1b1.png" alt="image" data-base62-sha1="n4fyZPN3z5hC7u3SiDaSBVbAWxr" width="406" height="194"></p>

---

## Post #3 by @alireza (2018-12-05 23:17 UTC)

<p>Thank you Csaba,<br>
Here are my two images, I don’t think i have the obscuring problem as you stated. The images are from IXI public dataset</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7d828cd15fbc961aa4619e8f12379fab81ece17.jpeg" data-download-href="/uploads/short-url/svU8qBAsnMXKmQs12qr8EhGDuqb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7d828cd15fbc961aa4619e8f12379fab81ece17_2_675x500.jpeg" alt="image" data-base62-sha1="svU8qBAsnMXKmQs12qr8EhGDuqb" width="675" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7d828cd15fbc961aa4619e8f12379fab81ece17_2_675x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7d828cd15fbc961aa4619e8f12379fab81ece17.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7d828cd15fbc961aa4619e8f12379fab81ece17.jpeg 2x" data-dominant-color="0A2A00"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">797×590 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My red image is kind of edges of the green image, and when I put the opacity at 50-50 the green image becomes dark.</p>
<p>I tried making a model from my red image and view the cross section of it on the green image but not quite exactly what I’m looking for.</p>
<p>I played with blending mode, and I think “ADD” option address my question to some extent</p>
<p>thank you</p>

---

## Post #4 by @cpinter (2018-12-06 00:02 UTC)

<aside class="quote no-group" data-username="alireza" data-post="3" data-topic="4981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alireza/48/67173_2.png" class="avatar"> alireza:</div>
<blockquote>
<p>I don’t think i have the obscuring problem</p>
</blockquote>
</aside>
<p>It’s not a problem, it is the way things are. Whatever you have in the background if you show the foreground at full opacity, the only thing you’ll see will be the foreground.</p>
<p>You can also play with the threshold function on the Volumes module. If you set the threshold so that the low values (the blackish regions) are not visible than that 50% black won’t darken the background.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abcfc26e5e46570d40eb75e5974fbaaf0f7b59e2.png" alt="image" data-base62-sha1="ovULKk31gnUnSVaCIGmyvb65kJk" width="535" height="56"></p>

---

## Post #5 by @lassoan (2018-12-06 05:17 UTC)

<p>Grayscale images are alpha-blended, you see the average of two volumes, which means a darker image will darken the rendered output (unless you choose “Add” compositing option). Labelmap images are rendered as an opaque or semi-transparent overlay and so “background” region will not affect the rendered output.</p>
<p>Make sure you to click “labelmap” in the “Add data” window when you load labelmap/binary image (or if you already loaded as scalar volume, convert it to labelmap in Volumes module / Volume information section).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef4bf28fea307cdb7dc75379c8e92af1efa5aa00.jpeg" data-download-href="/uploads/short-url/y8UPB4e2KVnHUWwqXqKYxrv1HY4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef4bf28fea307cdb7dc75379c8e92af1efa5aa00_2_690x196.jpeg" alt="image" data-base62-sha1="y8UPB4e2KVnHUWwqXqKYxrv1HY4" width="690" height="196" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef4bf28fea307cdb7dc75379c8e92af1efa5aa00_2_690x196.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef4bf28fea307cdb7dc75379c8e92af1efa5aa00_2_1035x294.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef4bf28fea307cdb7dc75379c8e92af1efa5aa00_2_1380x392.jpeg 2x" data-dominant-color="847A75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3256×929 731 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Tommaso_Di_Noto (2019-07-10 12:45 UTC)

<p>Thanks a lot for the tip <a class="mention" href="/u/lassoan">@lassoan</a>!</p>
<p>I didn’t know about the “labelmap” tick when loading data.</p>
<p>Quick question: when should we then use Background + Foregroung and when should we instead use Background + Labelmap?</p>
<p>Also, small suggestion: wouldn’t it be possible to enlarge the “Add data into the scene” window, maybe with the “Show Options” tick automatically ticked, so that one also sees the different loading modalities? For instance, I had never seen the “labelmap” tick just because the window was small.</p>
<p>Of course it’s just a suggestion and you probably set it this way for other good reasons <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #7 by @Tommaso_Di_Noto (2019-07-11 09:59 UTC)

<p>Also, two more (probably trivial) questions:</p>
<ol>
<li>
<p>how can I change the color of the LabelMap?</p>
</li>
<li>
<p>which is the quickest way to find in <a>https://github.com/Slicer</a> the corresponding part of the “Add data into the scene” window? I was curious to see how you implemented that.</p>
</li>
</ol>
<p>Thank you very much again!</p>

---

## Post #8 by @pieper (2019-07-11 15:01 UTC)

<p>1 -   you can change the color map using the Volumes module</p>
<p>2 - the code is big and complicated, but one way to find your way around is to use the search feature of github to look for a term from the UI.  <a href="https://github.com/Slicer/Slicer/search?q=%22Add+data+into%22&amp;unscoped_q=%22Add+data+into%22" rel="nofollow noopener">So if you search for “Add data into”</a> you find that class qSlicerDataDialog and you can look at the corresponding code.</p>

---

## Post #9 by @koeglfryderyk (2021-10-22 06:46 UTC)

<p>Hi, I have a related question. I want to overlay US images onto MRI images. The problem is that the empty (black) part of the US images obscures the MRI image. It looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/798f1dbfec50ed5f94c7f507e29247592eaa8889.jpeg" data-download-href="/uploads/short-url/hlmoJIoCxWJ1tigRheTzXMZD76x.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/798f1dbfec50ed5f94c7f507e29247592eaa8889_2_690x479.jpeg" alt="image" data-base62-sha1="hlmoJIoCxWJ1tigRheTzXMZD76x" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/798f1dbfec50ed5f94c7f507e29247592eaa8889_2_690x479.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/798f1dbfec50ed5f94c7f507e29247592eaa8889_2_1035x718.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/798f1dbfec50ed5f94c7f507e29247592eaa8889_2_1380x958.jpeg 2x" data-dominant-color="868692"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2659×1849 519 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there a way to deal with this issue? For example by making black foreground pixels transparent?</p>
<p>(I know I can choose ‘Add’ as the blending option, but this is not what I’m trying to achieve as it changes the appearance of the foreground)</p>
<p>Thanks for your help in advance</p>

---

## Post #10 by @jamesobutler (2021-10-22 11:42 UTC)

<p>Using the Volumes module, set the lower threshold value to 1 for your volume. Then all the 0 black pixels will be removed from the overlay display.</p>

---

## Post #11 by @lassoan (2021-10-22 14:03 UTC)

<p>For MRI/US fusion it is also common to change the color map of the US to green. You can choose the color map in Volumes module.</p>

---
