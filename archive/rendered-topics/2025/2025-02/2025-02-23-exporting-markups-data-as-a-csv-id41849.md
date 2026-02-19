---
topic_id: 41849
title: "Exporting Markups Data As A Csv"
date: 2025-02-23
url: https://discourse.slicer.org/t/41849
---

# Exporting markups data as a csv 

**Topic ID**: 41849
**Date**: 2025-02-23
**URL**: https://discourse.slicer.org/t/exporting-markups-data-as-a-csv/41849

---

## Post #1 by @evergarden (2025-02-23 14:12 UTC)

<p>I’m having issues exporting data as a csv, I created all the markups and nodes I wanted to collected and couldn’t seem to export any of the data as a csv successfully. I would often get csv’s with random numbers or incomplete cells. I also am using two separate modules (Biomech and Morph) to collect volume data and general length data so I also wanted to know if there was an easier way to export all of the data onto 1 csv?</p>
<p>Thanks! :3</p>

---

## Post #2 by @muratmaga (2025-02-23 20:00 UTC)

<aside class="quote no-group" data-username="evergarden" data-post="1" data-topic="41849">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evergarden/48/79535_2.png" class="avatar"> evergarden:</div>
<blockquote>
<p>couldn’t seem to export any of the data as a csv successfully. I</p>
</blockquote>
</aside>
<p>Did you try the Markup modules import/export tab? It allows you export the markups as a table inside slicer, which then you can save as a csv file.<br>
Also you can copy and paste control points from the control points table to Excel.</p>
<aside class="quote no-group" data-username="evergarden" data-post="1" data-topic="41849">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evergarden/48/79535_2.png" class="avatar"> evergarden:</div>
<blockquote>
<p>I would often get csv’s with random numbers or incomplete cells.</p>
</blockquote>
</aside>
<p>That doesn’t sound right. How are you exporting these CSV files?</p>
<aside class="quote no-group" data-username="evergarden" data-post="1" data-topic="41849">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evergarden/48/79535_2.png" class="avatar"> evergarden:</div>
<blockquote>
<p>I also wanted to know if there was an easier way to export all of the data onto 1 csv?</p>
</blockquote>
</aside>
<p>You can use the MergeMarkup module in SlicerMorph to merge all your markup nodes into a single markup object, which then you can use the export mechanism to save it as a csv file (or copy/paste to excel)</p>

---

## Post #3 by @evergarden (2025-03-07 22:45 UTC)

<p>Hello!</p>
<p>Thank you for your help, I was able to export the data but instead of the Description (like the name of the line and the length/angle etc.) I only get the points back from Slicer.</p>
<p>I was wondering if there is a way to get the Descriptions for the nodes from Slicer instead of the points.</p>

---

## Post #4 by @muratmaga (2025-03-08 01:43 UTC)

<aside class="quote no-group" data-username="evergarden" data-post="3" data-topic="41849">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/evergarden/48/79535_2.png" class="avatar"> evergarden:</div>
<blockquote>
<p>I was able to export the data but instead of the Description (like the name of the line and the length/angle etc.) I</p>
</blockquote>
</aside>
<p>It is not clear what method you used to export the csv file from Markups. For me, if I use the import/export option in the Markups module, descriptions are correctly included. See the control points, and compare to the export csv file:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8060f2c090f00d94ac5a1d9e893bab88a743aa4a.png" data-download-href="/uploads/short-url/ijGPgyj0Da34oC2PqMsBM0HZqYi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8060f2c090f00d94ac5a1d9e893bab88a743aa4a.png" alt="image" data-base62-sha1="ijGPgyj0Da34oC2PqMsBM0HZqYi" width="487" height="385"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">487×385 35.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/906fe45e094e25d8e0a3b5f0e6ba52221c93546a.png" data-download-href="/uploads/short-url/kBKtY6m59ZXgbDHNI2xVMQP1YdI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/906fe45e094e25d8e0a3b5f0e6ba52221c93546a.png" alt="image" data-base62-sha1="kBKtY6m59ZXgbDHNI2xVMQP1YdI" width="633" height="200"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">633×200 15.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @evergarden (2025-03-10 17:00 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7645d4e3a2bdd99e35c4b5f7cfbcd4394dc01c3f.png" data-download-href="/uploads/short-url/gShXd6DwlaYlBPc8aIPiz6MnD5B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7645d4e3a2bdd99e35c4b5f7cfbcd4394dc01c3f.png" alt="image" data-base62-sha1="gShXd6DwlaYlBPc8aIPiz6MnD5B" width="434" height="253"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">434×253 11.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
So here is what my Markup looks like, I was wondering if there was a way to get the names of the Nodes and Descriptions.</p>
<p>Thank you so much and sorry for any confusion, no one else in our lab knows how to use Slicer and we are all self-taught</p>

---

## Post #6 by @evergarden (2025-03-10 17:07 UTC)

<p>And then here is the CSV that I can get from the all the merged markups.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fed04dd897bcc959fc53e84ddc548d0aba72f01.png" data-download-href="/uploads/short-url/6PYfCDPycv4ALp55aCFsiS06yEV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fed04dd897bcc959fc53e84ddc548d0aba72f01.png" alt="image" data-base62-sha1="6PYfCDPycv4ALp55aCFsiS06yEV" width="415" height="500" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">625×753 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2025-03-10 18:30 UTC)

<p>So that description in your first screenshot comes from measurement. But the description field in the exported csv file comes from the description field of the individual control points (highlighted in the red). If you entered something there in your original markups, the exported csv should have description field also populated.</p>
<p>I am not sure if there is a way to include the description field from the markup object (the one highlighted in blue). It is confusing that both of them are called description, but they are not the same things.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e911a66fff99a8d1babf26a7604c34b1f560e2fd.png" data-download-href="/uploads/short-url/xfP45eOwaaboR9piMxNhPrqIIWx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e911a66fff99a8d1babf26a7604c34b1f560e2fd_2_375x500.png" alt="image" data-base62-sha1="xfP45eOwaaboR9piMxNhPrqIIWx" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e911a66fff99a8d1babf26a7604c34b1f560e2fd_2_375x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e911a66fff99a8d1babf26a7604c34b1f560e2fd_2_562x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e911a66fff99a8d1babf26a7604c34b1f560e2fd_2_750x1000.png 2x" data-dominant-color="D0CFD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">820×1092 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
