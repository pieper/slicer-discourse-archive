---
topic_id: 16158
title: "Markups Creating A Single File Including Landmarks Fixed And"
date: 2021-02-23
url: https://discourse.slicer.org/t/16158
---

# Markups - Creating a SINGLE file including Landmarks (fixed) and Curves (semilandmarks) - problem while resampling

**Topic ID**: 16158
**Date**: 2021-02-23
**URL**: https://discourse.slicer.org/t/markups-creating-a-single-file-including-landmarks-fixed-and-curves-semilandmarks-problem-while-resampling/16158

---

## Post #1 by @mariev (2021-02-23 12:59 UTC)

<p>Hi all,</p>
<p>I would like to pose a serie of (fixed) landmarks on my model and in between those landmarks, curves (semilandmarks).</p>
<p>I can make a node for landmarks using ‘create fiducial markup’ and another node for curves using ‘create open curve markup’. To insert my landmarks into the curves I can copy paste the landmarks from the “fiducial markup node” into the  "open curve node ".</p>
<p>BUT when I use the “resample” option to get evenly-spaced points,  it will resample all my markups - landmarks and curve points - meaning that my landmarks will move - while I want them to be fixed - and that I will not have the same number of semilandmarks between the landmarks for different specimens, which makes the generate file (fcsv) not comparable between specimens.</p>
<p>The only solution I see is to create different nodes for different curves (and so resample them separately), but then I have to export them separately as well, and I want a single file per specimen.</p>
<p>Is there a way to fix the landmarks delimiting a curve, and resample the different curves separately? And to get a single file with all markups.</p>
<p>Thanks a lot for your help!</p>

---

## Post #2 by @lassoan (2021-02-23 14:41 UTC)

<p>We plan to add a right-click menu action that would allow exporting all markup nodes in a subject hierarchy folder into a single mrk.json file. Would this fulfill your needs?</p>

---

## Post #3 by @mariev (2021-02-23 14:47 UTC)

<p>Yes, if it’s possible to export several nodes into a single file (fcsv as well would be great), it should work for what I want to do…</p>
<p>Thanks,</p>

---

## Post #4 by @lassoan (2021-02-23 16:23 UTC)

<p>Can you copy here the content of a file (in json or csv format) that you would ideally like to see as an output of the export operation? Probably it can be generated with 5-10 lines of Python code.</p>

---

## Post #5 by @muratmaga (2021-02-23 17:58 UTC)

<aside class="quote no-group" data-username="mariev" data-post="1" data-topic="16158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/13edae/48.png" class="avatar"> mariev:</div>
<blockquote>
<p>The only solution I see is to create different nodes for different curves (and so resample them separately), but then I have to export them separately as well, and I want a single file per specimen.</p>
</blockquote>
</aside>
<p>Yes, only the first and last LM in a resampled curve is treated as a fixed. The other points are simply enabling you to draw the curve in the way you would like to draw. As you suggested, the solution is to create multiple curves, and resample them independetly. Remember you can also resample them as a new curve so that they don’t overwrite the original points.</p>
<p>Until the new feature <a class="mention" href="/u/lassoan">@lassoan</a> mentioned is available, you can choose to create a blank curve node, and copy and paste contents from individually resampled curves.</p>

---

## Post #6 by @mariev (2021-03-19 10:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16158">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>t-click menu action that would allow exporting all markup nodes in a subject</p>
</blockquote>
</aside>
<p>Dear Dr Lasso,</p>
<p>When I apply the solution suggested by <a class="mention" href="/u/muratmaga">@muratmaga</a>, to create different nodes for different curves and copy paste each one of them into a new blank curve node that I can export, I get the fcsv file here below. But I had to manually delete redundant landmarks : in node1, I have lmk1- 8semilmks - lmk2 and in node2 I have lmk2 - 8 semilmk - lmk3.<br>
I have to place lmk2 in both nodes to get evenly spaced point between the two fixed lmks in each case.</p>
<p>It is of course feasible like that, and having a  right-click menu action allowing exporting all markup nodes in a subject hierarchy folder into a single file would avoid the last step of copy paste all separate node into another single blank node.</p>
<p>The ideal for what I want to do would be to be able to directly place fixed landmarks (fiducial markups) and open curves into the same node, so I don’t have to delete redundant lmks AND I have a single file including all markups from 1 specimen.<br>
and then have an option to export data from multiple specimens into a single file (.dta or .pts ?).<br>
That would be ideal, but I can get to this result manually (just requires more clicking and format conversion…)</p>
<p>Thanks a lot for your help with this!<br>
Best regards,</p>
<h1><a name="p-56590-markups-fiducial-file-version-411-1" class="anchor" href="#p-56590-markups-fiducial-file-version-411-1" aria-label="Heading link"></a>Markups fiducial file version = 4.11</h1>
<h1><a name="p-56590-coordinatesystem-lps-2" class="anchor" href="#p-56590-coordinatesystem-lps-2" aria-label="Heading link"></a>CoordinateSystem = LPS</h1>
<h1><a name="p-56590-columns-idxyzowoxoyozvissellocklabeldescassociatednodeid-3" class="anchor" href="#p-56590-columns-idxyzowoxoyozvissellocklabeldescassociatednodeid-3" aria-label="Heading link"></a>columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID</h1>
<p>1,3.1665592193603516,3.600550413131714,4.49215030670166,0,0,0,1,1,1,1,lmk-1,<br>
2,3.200083017349243,3.611091375350952,4.4122419357299805,0,0,0,1,1,1,1,<br>
3,3.245849132537842,3.6081860065460205,4.338837146759033,0,0,0,1,1,1,1,C0-1,<br>
4,3.3022565841674805,3.5931780338287354,4.274499416351318,0,0,0,1,1,1,1,<br>
2,3.3729569911956787,3.5815329551696777,4.224930286407471,0,0,0,1,1,1,1,<br>
6,3.427863359451294,3.547471761703491,4.163037300109863,0,0,0,1,1,1,1,C0-2,<br>
7,3.495396375656128,3.522686243057251,4.114658355712891,0,0,0,1,1,1,1,<br>
8,3.5646512508392334,3.4949839115142822,4.070284843444824,0,0,0,1,1,1,1,C0-3,<br>
9,3.6365785598754883,3.4671223163604736,4.029834270477295,0,0,0,1,1,1,1,<br>
10,3.7150931358337402,3.4446561336517334,4.000028610229492,0,0,0,1,1,1,1,lmk-2,<br>
2,3.8455679416656494,3.573317766189575,3.9720921516418457,0,0,0,1,1,1,0,C1-2,<br>
3,3.9041731357574463,3.7461397647857666,3.958988666534424,0,0,0,1,1,1,0,C1-3,<br>
4,3.9525156021118164,3.924328327178955,3.955364465713501,0,0,0,1,1,1,0,<br>
5,4.007574081420898,4.101275444030762,3.961444139480591,0,0,0,1,1,1,0,C1-4,<br>
6,4.07861852645874,4.269351005554199,3.9274699687957764,0,0,0,1,1,1,0,<br>
3,4.184473514556885,4.371997833251953,3.812854290008545,0,0,0,1,1,1,0,C1-5,<br>
8,4.280713081359863,4.443325519561768,3.674037456512451,0,0,0,1,1,1,0,<br>
9,4.3735127449035645,4.509683132171631,3.525798797607422,0,0,0,1,1,1,0,C1-6,<br>
10,4.4661455154418945,4.637211322784424,3.4207212924957275,0,0,0,1,1,1,0,lmk-3,</p>

---

## Post #7 by @muratmaga (2021-03-19 13:48 UTC)

<aside class="quote no-group" data-username="mariev" data-post="6" data-topic="16158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/13edae/48.png" class="avatar"> mariev:</div>
<blockquote>
<p>It is of course feasible like that, and having a right-click menu action allowing exporting all markup nodes in a subject hierarchy folder into a single file would avoid the last step of copy paste all separate node into another single blank node.</p>
</blockquote>
</aside>
<p>This will not remove the redundant LMs from the export. Redundancy is coming from the workflow, not from copy/paste or merging. If you want to create a curve between, say, three anatomical LMs, and merge them, LM2 (or any of the points in the middle) will be still be redundant (as last LM point on the first curve and as the first LM point in the second curve).</p>
<p>People haven’t used the curve function to generate semiLMs and we haven’t thought about making something more than curve generation. A custom function to stitch them into a single curve into in the given order shouldn’t be too difficult. <a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---

## Post #8 by @muratmaga (2021-03-26 15:21 UTC)

<aside class="quote no-group" data-username="mariev" data-post="6" data-topic="16158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/13edae/48.png" class="avatar"> mariev:</div>
<blockquote>
<p>The ideal for what I want to do would be to be able to directly place fixed landmarks (fiducial markups) and open curves into the same node, so I don’t have to delete redundant lmks AND I have a single file including all markups from 1 specimen.</p>
</blockquote>
</aside>
<p>This feature is now available in SlicerMorph. It is called MergeMarkups. You want to use the MergeCurves tab. If your curves are meant to be continuous (e.g., green and pink pair), check the continuous option, which when merging will remove the first LM of the second (and all subsequent) curves selected. If curves are separate, but they belong the same specimen and you want to store them in the same file for analytical reasons, uncheck the continuous option (default setting).</p>
<p>GIve it a try, and let us know how it works for you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07d2f6afe134ac6c5eae6b36edec1c31884581ba.png" data-download-href="/uploads/short-url/17dkrCIELAd2wzXRzmmX3Y15WFY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07d2f6afe134ac6c5eae6b36edec1c31884581ba_2_690x349.png" alt="image" data-base62-sha1="17dkrCIELAd2wzXRzmmX3Y15WFY" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07d2f6afe134ac6c5eae6b36edec1c31884581ba_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07d2f6afe134ac6c5eae6b36edec1c31884581ba.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07d2f6afe134ac6c5eae6b36edec1c31884581ba.png 2x" data-dominant-color="CDD3E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">980×497 41.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @smrolfe (2021-03-27 19:00 UTC)

<p>I’ve added a tutorial on the new MergeMarkups module in SlicerMorph, check it out <a href="https://github.com/SlicerMorph/Tutorials/blob/main/MergeMarkups.md" rel="noopener nofollow ugc">here</a>!</p>

---
