---
topic_id: 22235
title: "Skull Segmentation Issues No Erase Scissors Islands Function"
date: 2022-03-01
url: https://discourse.slicer.org/t/22235
---

# Skull segmentation issues (no Erase, Scissors, Islands functions working)

**Topic ID**: 22235
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/skull-segmentation-issues-no-erase-scissors-islands-functions-working/22235

---

## Post #1 by @Kevin_Wendo (2022-03-01 15:02 UTC)

<p>Dear All,<br>
I hope you are well.</p>
<p>I am looking for some help to achieve the segmentation of a skull based on CT data (CBCT) for dentistry purposes.<br>
For some reasons that I cannot explain, I am not able to get rid of the all the noises and some areas (vertebras, mandibla, ribs) through Islands, Erase or Scissors functions. Any attempt of modification trough any of those methods does not appear on my model. Even any change on the smoothing factor does not apply to it.<br>
Can anyone help with this ?<br>
Is there a possibility that a protection on the model and some data are missing from the CT data (CBCT) ?<br>
Thank you so much !<br>
Kevin<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63e18ba0d26c6ccc55a0748753cfa192fa6862e8.jpeg" data-download-href="/uploads/short-url/efAuTU08SxGIQQjdsfngddIk0pq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63e18ba0d26c6ccc55a0748753cfa192fa6862e8_2_690x431.jpeg" alt="image" data-base62-sha1="efAuTU08SxGIQQjdsfngddIk0pq" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63e18ba0d26c6ccc55a0748753cfa192fa6862e8_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63e18ba0d26c6ccc55a0748753cfa192fa6862e8_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63e18ba0d26c6ccc55a0748753cfa192fa6862e8_2_1380x862.jpeg 2x" data-dominant-color="9D9DAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1200 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-03-01 17:39 UTC)

<aside class="quote no-group" data-username="Kevin_Wendo" data-post="1" data-topic="22235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kevin_wendo/48/14507_2.png" class="avatar"> Kevin_Wendo:</div>
<blockquote>
<p>Erase or Scissors functions. Any attempt of modification trough any of those methods does not appear on my model. Even any change on the smoothing factor does not apply to it.</p>
</blockquote>
</aside>
<p>Use the default masking settings to make sure that masking does not interfere with your intended modifications:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c45033ab8d62ede60058356ae5dc56e0f960a5d4.png" data-download-href="/uploads/short-url/s0FpMwIBXtQbXeskyfc94T6xHpy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c45033ab8d62ede60058356ae5dc56e0f960a5d4.png" alt="image" data-base62-sha1="s0FpMwIBXtQbXeskyfc94T6xHpy" width="690" height="180" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">795×208 4.99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Kevin_Wendo (2022-03-02 11:00 UTC)

<p>It works perfectly !! Thank you so much <a class="mention" href="/u/lassoan">@lassoan</a>  !!! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @Kevin_Wendo (2022-03-03 08:32 UTC)

<p>Dear All,<br>
<a class="mention" href="/u/lassoan">@lassoan</a><br>
I come back to you because during the segmentation process, i am unable to erase some parts from my model. It is not possible for me to take off all the remaining teeth from the absent mandible. Both Scissors and Erase function do not work.  On the CT images, it shows like if they are within the Threshold range but no Threshold change modifies it.<br>
Can you help with that, please ? I would like to remove the lower teeth.</p>
<p>Thank you all !<br>
Kévin<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db2cb87bd9d214211f6dc31cd98e6e9ec1113b84.jpeg" data-download-href="/uploads/short-url/vgUnx17yWel5dJGIXEy3HrCJTEw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db2cb87bd9d214211f6dc31cd98e6e9ec1113b84_2_690x431.jpeg" alt="image" data-base62-sha1="vgUnx17yWel5dJGIXEy3HrCJTEw" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db2cb87bd9d214211f6dc31cd98e6e9ec1113b84_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db2cb87bd9d214211f6dc31cd98e6e9ec1113b84_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db2cb87bd9d214211f6dc31cd98e6e9ec1113b84_2_1380x862.jpeg 2x" data-dominant-color="A0A1AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1200 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @cpinter (2022-03-03 09:09 UTC)

<p>I again suspect the masking options. Make sure it is Everywhere and Overwrite all.</p>

---

## Post #6 by @Kevin_Wendo (2022-03-04 18:23 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="22235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>ns. Make sure it is Everywhere and Overwrite all.</p>
</blockquote>
</aside>
<p>Thank you for your answer.<br>
I checked the masking options and nothing changed. Could it be something else ?<br>
Thanks</p>

---

## Post #7 by @mikebind (2022-03-04 18:37 UTC)

<p>Might you have a model in the scene in addition to the segmentation?  Segmentation tools will edit the current segment, but will have no effect on a model.  Sometimes a model has the exact same appearance in the 3D view as a segment (usually because you generated the model by exporting it from the segmentation, so it matches perfectly in color and location), but would hide any subtractive editing.  The segment would be edited, but you would see no change in the 3D view because the changes are behind the opaque surface of the model.</p>

---

## Post #8 by @rbumm (2022-03-04 19:39 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="7" data-topic="22235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Might you have a model in the scene in addition to the segmentation?</p>
</blockquote>
</aside>
<p>Would support that. Please have a look in “Data”<br>
, maybe post the “Data” content of that scene. There must be something in the scene that overlays your editing.</p>

---

## Post #9 by @Kevin_Wendo (2022-03-08 10:51 UTC)

<p>Thank you <a class="mention" href="/u/rbumm">@rbumm</a> <a class="mention" href="/u/mikebind">@mikebind</a><br>
Here is the “Data” content. I have tried to (un)mask different segments and i am still unable to erase the mandible teeth.<br>
Thank you so much for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7a415155ce8442c593b81ab8611795ef4ee6da1.jpeg" data-download-href="/uploads/short-url/zkJtLezWlu4I5cyk9u35JALKvCN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7a415155ce8442c593b81ab8611795ef4ee6da1_2_690x431.jpeg" alt="image" data-base62-sha1="zkJtLezWlu4I5cyk9u35JALKvCN" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7a415155ce8442c593b81ab8611795ef4ee6da1_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7a415155ce8442c593b81ab8611795ef4ee6da1_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7a415155ce8442c593b81ab8611795ef4ee6da1_2_1380x862.jpeg 2x" data-dominant-color="9D9DA8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1200 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @mikebind (2022-03-08 18:23 UTC)

<p>It appears that you have three segmentations which are all named “Segmentation”.  I would suggest changing the names of each of them to be distinct (you can do this by double clicking on the name in the Data module and entering a new name).  One possible source of your problem is that you have been editing only one of the segmentations, and looking for effects on the other one, which is unaffected by edits to the first.  In the Segment Editor module, make sure the segmentation you are editing is the same as the one you are viewing. It would also help you keep track of things if you change the color of each segment by double-clicking on the color square and selecting a new color.  That will help to clarify which elements you are currently viewing and editing.</p>

---

## Post #11 by @rbumm (2022-03-09 18:48 UTC)

<p>Correct Mike.</p>
<p><a class="mention" href="/u/kevin_wendo">@Kevin_Wendo</a> in the image you provide</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0c041f2a85e6d37b2f7171f285eed89559f3712.jpeg" data-download-href="/uploads/short-url/tMHdSB3LD4NSlgdKbaB0tH0n4MW.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0c041f2a85e6d37b2f7171f285eed89559f3712_2_689x398.jpeg" alt="image" data-base62-sha1="tMHdSB3LD4NSlgdKbaB0tH0n4MW" width="689" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0c041f2a85e6d37b2f7171f285eed89559f3712_2_689x398.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0c041f2a85e6d37b2f7171f285eed89559f3712_2_1033x597.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0c041f2a85e6d37b2f7171f285eed89559f3712.jpeg 2x" data-dominant-color="9E9EAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1374×793 79.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>you are actually viewing the segmentation that is marked with red arrows here. See also both marked eye symbols, they indicate what is visible in the scene.  Change the name of that “Segmentation” (double click on it to rename)  to “Segmentation_final”. Then select “Segmentation_final” in the Segment Editor and make your desired changes.</p>

---

## Post #12 by @Kevin_Wendo (2022-03-14 07:52 UTC)

<p>Dear All,<br>
Thank you for your recommandations, it worked I was able to erase the areas i needed too!.<br>
Quick question : I switched the “Editable area” to “Inside segments” and it worked too, can you explain me why ?<br>
Thank you very much for your support!</p>

---

## Post #13 by @mikebind (2022-03-14 18:33 UTC)

<p>The masking settings control where segment editing tools are allowed to make changes.  If you choose to have the “Editable area” be “Inside segments” then the selected editing tool will only be able to make changes to voxels which are already inside existing segments. This works fine for subtractive tools like the “Eraser” because it only makes sense to erase parts of existing segments.  On the other hand, if you only had one existing segment and you tried to add to it using the Paint tool, but had the editable area as “Inside segments”, it would be impossible to paint new areas to add because all voxels outside of your single existing segment are outside your “editable area”.</p>

---

## Post #14 by @Kevin_Wendo (2022-03-14 20:36 UTC)

<p>Alright Thank you very much  Mike ! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
