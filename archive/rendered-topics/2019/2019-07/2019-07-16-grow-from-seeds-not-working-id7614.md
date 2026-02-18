# Grow From Seeds Not Working

**Topic ID**: 7614
**Date**: 2019-07-16
**URL**: https://discourse.slicer.org/t/grow-from-seeds-not-working/7614

---

## Post #1 by @Tyrus (2019-07-16 16:17 UTC)

<p>Hi everyone,</p>
<p>I have a question about the “Grow from seeds” effect in Segment Editor. I have been using it pretty seamlessly in the past, but this morning when I tried to use it, its effect is to remove everything I have painted. Furthermore, I even tried to paint within this effect hoping for function to auto-update - as it normally does - however there was no effect of using the paint function.</p>
<p>Attached are two screenshots depicting the problem. After initializing the “Grow from seeds”, the painted colours become more dull, implying that they will be, and are, removed when the effect is applied, and the result is a blank slate after I click “Apply”.</p>
<p>I was having trouble with crashing this morning so I downloaded the 4.11.0 version (28391) but the problem with “Grow from seeds” is occurred on both this version and the 4.10.2 version (28257).</p>
<p>Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/600864053beb63bfa22f53e00c11635c06b02b08.jpeg" data-download-href="/uploads/short-url/dHxOtEp7Z5YlPX5EO1VxuST5yJi.jpeg?dl=1" title="Grow%20From%20Seeds%20Not%20Working%201%20of%202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/600864053beb63bfa22f53e00c11635c06b02b08_2_690x387.jpeg" alt="Grow%20From%20Seeds%20Not%20Working%201%20of%202" data-base62-sha1="dHxOtEp7Z5YlPX5EO1VxuST5yJi" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/600864053beb63bfa22f53e00c11635c06b02b08_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/600864053beb63bfa22f53e00c11635c06b02b08_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/600864053beb63bfa22f53e00c11635c06b02b08_2_1380x774.jpeg 2x" data-dominant-color="898B93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Grow%20From%20Seeds%20Not%20Working%201%20of%202</span><span class="informations">1919×1079 377 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-07-16 16:22 UTC)

<p>It is hard to guess from this much information, but you can try these:</p>
<ul>
<li>Make sure “Masking” settings are set to default (Editable area: Everywhere; Editable intensity range: unchecked; Overwrite other segments: All segments).</li>
<li>Make sure that other auto-complete effects (Fill intersection between slices, Watershed) are not active</li>
</ul>

---

## Post #3 by @Tyrus (2019-07-16 17:29 UTC)

<p>Thanks for the quick reply!</p>
<p>I double-checked these settings and they were set just as you mentioned. I gathered it would be a bit of a guessing game with the limited information. I can provide additional details if necessary, but I am not sure what else would be helpful. I was more wondering if this was a recurring issue that had an easy fix.</p>
<p>I’ll let you know if I have a breakthrough.</p>

---

## Post #4 by @lassoan (2019-07-16 20:51 UTC)

<p>Is there any warning or error in the application log?</p>
<p>Can you share the scene file?</p>
<p>You can try creating a new scene and load just the volume and segmentation files and see if things get back to normal then.</p>

---

## Post #5 by @Tyrus (2019-07-17 17:42 UTC)

<p>From what I can tell, there is no error in the application log.</p>
<p>A bit of a strange progression: I had temporarily given up on that file and just decided to move on. I started another one, periodically making sure my “Grow from seeds” function worked, which it did. Anyway, after not attempting the “Grow from seeds” following a substantial amount of painting, I was done and ready to get my 3D model. Upon initializing the “Grow from seeds”, the exact same thing happened - it wanted to remove everything!</p>
<p>After trying a handful of things to no avail, I created a new scene and loaded the volume and segmentation files (as you suggested), and it worked. This confused me, as I was pretty sure I tried this with the other file yesterday. Sure enough I tried again with the other file and it did <em>not</em> work with this one.</p>
<p>In regards to sharing the scene file, did you want me to share it here? I was under the impression that I could only share jpg, jpeg, png, and gif files.</p>
<p>I hope this is not some dumb mistake on my part - or maybe it would be more convenient if it was. As always, I appreciate the help.</p>

---

## Post #6 by @lassoan (2019-07-17 17:53 UTC)

<aside class="quote no-group" data-username="Tyrus" data-post="5" data-topic="7614">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/8c91f0/48.png" class="avatar"> Tyrus:</div>
<blockquote>
<p>In regards to sharing the scene file, did you want me to share it here?</p>
</blockquote>
</aside>
<p>You can upload to dropbox/onedrive/gdrive and post the link here.</p>

---

## Post #7 by @Tyrus (2019-07-17 19:18 UTC)

<p>Thank you! My apologies, it’s my first time here.</p>
<p>Here is the link:<br>
<a href="https://queensuca-my.sharepoint.com/:f:/g/personal/15tneg_queensu_ca/ErdWWmE2OOhAgkOXbSf8RGMBrkDoCTZoFQKehv-YUsa68Q?email=tyrusgibson%40gmail.com&amp;e=yUow9b" class="onebox" target="_blank" rel="nofollow noopener">https://queensuca-my.sharepoint.com/:f:/g/personal/15tneg_queensu_ca/ErdWWmE2OOhAgkOXbSf8RGMBrkDoCTZoFQKehv-YUsa68Q?email=tyrusgibson%40gmail.com&amp;e=yUow9b</a></p>

---

## Post #8 by @lassoan (2019-07-18 02:12 UTC)

<p>It asked for a verification code. Please either send the verification code or allow access without verification.</p>

---

## Post #9 by @Tyrus (2019-07-18 12:49 UTC)

<p>Thanks so much for you patience, Andras. Here’s a Dropbox link, this should work a lot better:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/sh/29fmc42bjr8o5le/AACQQyMYSIAcQa2-ASNeAcnna?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/sh/29fmc42bjr8o5le/AACQQyMYSIAcQa2-ASNeAcnna?dl=0" target="_blank" rel="nofollow noopener">3D Slicer #13</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #10 by @lassoan (2019-08-11 12:10 UTC)

<p>Sorry, it took me a while to get to this. I’ve checked the scene that you shared and interestingly there was a 0.000003 difference in image origin position (due to numerical inaccuracy? saving of values to file?), which tripped a geometry consistency check.</p>
<p>I’ve fixed the check now, so Grow from seeds should work correctly in Slicer Preview Release downloaded tomorrow or later.</p>
<p>Thanks again for reporting the issue, it was very helpful.</p>

---
