---
topic_id: 23820
title: "Canine Skull Stripping"
date: 2022-06-10
url: https://discourse.slicer.org/t/23820
---

# Canine skull stripping

**Topic ID**: 23820
**Date**: 2022-06-10
**URL**: https://discourse.slicer.org/t/canine-skull-stripping/23820

---

## Post #1 by @Josefa_Garcia (2022-06-10 18:45 UTC)

<p>Hi, I am trying to do this with MRI images of the canine brain, I’ve provided an atlas volume and mask volume of an atlas I’ve found on internet, but the algorithm is not working, It selects the entire image and not just the brain, Idk if I’m doing something wrong or just doesn’t work, if you could help me I’d really appreciate it. Thanks!</p>

---

## Post #2 by @mau_igna_06 (2022-06-10 18:52 UTC)

<p>Dear Andras<br>
Is the SwissSkullStripper extension working these days?</p>

---

## Post #3 by @Josefa_Garcia (2022-06-10 18:55 UTC)

<p>if not, what are you using for skull stripping in large samples?</p>

---

## Post #4 by @mau_igna_06 (2022-06-10 22:08 UTC)

<p>Sorry I’m not an expert on this extensions but other core devs could tell you.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> hope you dom’t mind I tag you</p>

---

## Post #5 by @lassoan (2022-06-11 01:20 UTC)

<p>SwissSkullStripper extension may be usable for this. If it did not work for me then the best would be if you could share the images that you used.</p>
<p>Alternatively, you can bring this problem as a project to the upcoming <a href="https://discourse.slicer.org/t/na-mic-project-week-next-project-week-37-preparation-meeting-tuesday-june-14th/23816">Slicer Project Week</a>.</p>

---

## Post #6 by @Josefa_Garcia (2022-06-11 16:53 UTC)

<p>Hi, Thanks for your help, I’ve attached the link with the files I’m using. (MRI study, template and brain mask).</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1z1--SNKfUEqIpZwVJp6YTOjL8eJR8t2W/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1z1--SNKfUEqIpZwVJp6YTOjL8eJR8t2W/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1z1--SNKfUEqIpZwVJp6YTOjL8eJR8t2W/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1z1--SNKfUEqIpZwVJp6YTOjL8eJR8t2W/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Canine-braintumor.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2022-06-11 20:04 UTC)

<p>You have shared 8 brain MRIs and a an atlas mask. There was no atlas image - MRI image corresponding to the atlas mask, so I could not try SwissSkullStripper.</p>
<p>Also note that the atlas mask you provided was so different from all the brain images that most likely it would not be usable. I would recommend to manually segment the brain on one of your MRI images and use them as atlas image and mask for stripping the skull from other similar images.</p>

---

## Post #8 by @Josefa_Garcia (2022-06-12 22:26 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="23820">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>MRI image corresponding to the atlas mask, so I could not try SwissSkullStripper.</p>
</blockquote>
</aside>
<p>I’ll try that, thank you</p>

---
