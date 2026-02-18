# How can give more than one segments different color in the same volume?

**Topic ID**: 23788
**Date**: 2022-06-09
**URL**: https://discourse.slicer.org/t/how-can-give-more-than-one-segments-different-color-in-the-same-volume/23788

---

## Post #1 by @MAXFAXSURGEON (2022-06-09 08:30 UTC)

<p>Dears in 3D Slicer support team,<br>
I want to know how could I color different regions with different  colors in the same model!<br>
As you can seen in this screenshot below:<br>
Want to color the fractured segments (small ones) with a different color than the whole mandible!<br>
Thank you so much for appreciated help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4719f80ff923efb0cbd9456ef15f82ab009cdeae.jpeg" data-download-href="/uploads/short-url/a8ZxoOIgQF5AhsOlTTzXF1G241M.jpeg?dl=1" title="2BE47661-DEC0-4931-A552-F63068FDD2AF" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4719f80ff923efb0cbd9456ef15f82ab009cdeae_2_666x500.jpeg" alt="2BE47661-DEC0-4931-A552-F63068FDD2AF" data-base62-sha1="a8ZxoOIgQF5AhsOlTTzXF1G241M" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4719f80ff923efb0cbd9456ef15f82ab009cdeae_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4719f80ff923efb0cbd9456ef15f82ab009cdeae_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4719f80ff923efb0cbd9456ef15f82ab009cdeae_2_1332x1000.jpeg 2x" data-dominant-color="81817E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2BE47661-DEC0-4931-A552-F63068FDD2AF</span><span class="informations">1920×1440 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mau_igna_06 (2022-06-09 08:57 UTC)

<p>If they are separated from the mandible you can use islands effect to add them to a new segment</p>

---

## Post #3 by @MAXFAXSURGEON (2022-06-09 10:44 UTC)

<p>Thank you, Can you please explain more and if there is a demo link would be great if shared! Thank you again</p>

---

## Post #4 by @mau_igna_06 (2022-06-09 10:45 UTC)

<p>Here you have</p><div class="youtube-onebox lazy-video-container" data-video-id="bCZZ2oxgWxQ" data-video-title="slicer Segment Editor Island Scissor" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=bCZZ2oxgWxQ" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/bCZZ2oxgWxQ/maxresdefault.jpg" title="slicer Segment Editor Island Scissor" width="" height="">
  </a>
</div>


---

## Post #5 by @MAXFAXSURGEON (2022-06-09 11:14 UTC)

<p>But this one dose not show to the end result! Do this mean by doing these steps I would have two different colored segments in the same model?</p>

---

## Post #6 by @mau_igna_06 (2022-06-09 11:23 UTC)

<p>If you want to have dofferent colors on the same model you should use color scalars<br>
For example: red=1,blue=2, and so on</p>
<p>You can explore the models module to know more about this</p>

---

## Post #7 by @muratmaga (2022-06-09 18:51 UTC)

<p>Please do not post screen captures with private information on them!</p>

---

## Post #8 by @MAXFAXSURGEON (2022-06-10 04:18 UTC)

<p>You are right, next time I will take care. Thank you for such great notice.</p>

---
