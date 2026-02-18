# Intersection lines not show up

**Topic ID**: 35851
**Date**: 2024-05-01
**URL**: https://discourse.slicer.org/t/intersection-lines-not-show-up/35851

---

## Post #1 by @Ben_Fong (2024-05-01 13:26 UTC)

<p>I am a novice user. I tried “basic + intersection” or “small basic + intersection”, the crosshair showed up, but the intersection did not, what should I do? Please help. Thanks. (Windows 10 &amp; Mac Sonoma, version 5.6.2).</p>

---

## Post #2 by @pieper (2024-05-01 18:58 UTC)

<p>Basic with intersection should look like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7acc7e9d0a2a95735835fce91881efe2e22842e5.png" alt="image" data-base62-sha1="hwknuX291ypTtNCmV6uMgstn2y9" width="164" height="92"></p>
<p>No intersection should look like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e4f5b670dbd4e8bac2e5b05864569de9dd9847f.png" alt="image" data-base62-sha1="4k8lrdtDdgkPZK9jKhDXtRDzr2v" width="119" height="83"></p>
<p>Small basic with intersection like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a8163b7e93bb67a71591f268741117b314c8eaa.png" alt="image" data-base62-sha1="8lyUmrC1qx7oPVPHcAN5N4APD4K" width="101" height="68"></p>
<p>Is that not what you see?</p>

---

## Post #4 by @Ben_Fong (2024-05-01 22:28 UTC)

<p>Thanks for yor information. Yes, it is, sorry that probably my terms are not correct. I want to see the cross reference lines in the images when I scroll through them. I could see it in the past year ago, but not now after update. What setting am I missed? Thanks.</p>

---

## Post #5 by @Ben_Fong (2024-05-01 22:36 UTC)

<p>I am looking for the cross reference lines that showing the real time position of the slice of the image in other views when I scroll. The crosshair is a mark that stays at one spot. The crosshair line function normal, but is not I want. Thanks.</p>

---

## Post #6 by @cpinter (2024-05-02 11:48 UTC)

<p>It seems to me that what you need are the slice intersections. There has been a rework around crosshairs and slice intersections, and now it has its own button and settings in the toolbar:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3039ea0d137413a848bb98b4193e1c5c7f53aee7.png" alt="image" data-base62-sha1="6SCZXmUlIDiuqoNevvNg7WhkpDx" width="386" height="201"></p>
<p>I think it would be a great community contribution if you could add a paragraph about this below this one:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#view-cross-reference" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#view-cross-reference</a><br>
Please let us know if you have an hour for this. We’re happy to provide you guidance. Thanks!</p>
<p>Of course also let me know if this is not what you needed.</p>

---

## Post #7 by @Ben_Fong (2024-05-02 12:12 UTC)

<p>Thanks for your information.<br>
I realized the problem.<br>
Yes, it is what I am looking for, but I just failed to activate it correctly.<br>
Instead of directly pressing on the button, I went to the sideway arrow button and clicked on the interaction, I thought it would activate the cross-reference at the same time, which is not. I got this wrong impression because if I choose an option for the nearby crosshair button, the crosshair is activated.<br>
Now I know that I simply need to press directly on the button to get the function, the “interaction” is the newly added function to the cross-reference line, clicking it does not activate the cross-reference function.<br>
Thanks a lot.</p>

---

## Post #8 by @Ben_Fong (2024-05-02 12:29 UTC)

<p>I just suggested to insert two lines (97 &amp; 98) to the document:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05981a1f66256a4b8f9b1ab58b38df145ed2fc02.jpeg" data-download-href="/uploads/short-url/NugoDqOD5BR8BgfcHRkBDZVyJI.jpeg?dl=1" title="2024-05-02_202704" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05981a1f66256a4b8f9b1ab58b38df145ed2fc02_2_689x88.jpeg" alt="2024-05-02_202704" data-base62-sha1="NugoDqOD5BR8BgfcHRkBDZVyJI" width="689" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05981a1f66256a4b8f9b1ab58b38df145ed2fc02_2_689x88.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05981a1f66256a4b8f9b1ab58b38df145ed2fc02_2_1033x132.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05981a1f66256a4b8f9b1ab58b38df145ed2fc02.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-05-02_202704</span><span class="informations">1283×164 46.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks.</p>

---

## Post #9 by @cpinter (2024-05-02 12:57 UTC)

<p>Thanks for the report! I think your suggestion for change would be a mistake, as that paragraph is about the Crosshair, and now we have a separate Slice intersections feature. We’ll need a new paragraph.</p>
<p>Edit: It may actually be okay, I did not consider it in depth, because, again, the most confusing part is that we don’t have it documented that there are two different functions now instead of one.</p>

---
