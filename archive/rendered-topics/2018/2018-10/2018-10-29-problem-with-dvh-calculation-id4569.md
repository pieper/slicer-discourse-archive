---
topic_id: 4569
title: "Problem With Dvh Calculation"
date: 2018-10-29
url: https://discourse.slicer.org/t/4569
---

# Problem With DVH Calculation

**Topic ID**: 4569
**Date**: 2018-10-29
**URL**: https://discourse.slicer.org/t/problem-with-dvh-calculation/4569

---

## Post #1 by @MeryMB (2018-10-29 11:45 UTC)

<p>Hi Dear 3DSlicerc Developer and User</p>
<p>I want to re-calculate DVH for TPS Plan with 3D Slicer.<br>
I export CT, RTDose and RTStruct from ISOgray TPS and use them as input files for 3D Slicer for DVH calculation.<br>
Based on the software, it should not be hard but when I calculate it I encounter a strange problem…<br>
The 3DSlicer DVH has the same shape in contrast with TPS DVH but the dose per volume are not the same.<br>
for example: I have 41 cGy for  95% of volume in TPS but 3D Slicer show 35.0 for the same volume!!!<br>
I attached both DVH to the message to make it more clear.</p>
<p>I wonder if someone encounter to such problem before?<br>
I will be thankful if someone have suggestion for me…</p>
<p>Best Regards<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3709501ecbeea8e148ca9d9fd08249e416ee11b.jpeg" data-download-href="/uploads/short-url/uatX2k1gHfUSajCvghmrj7TTUJZ.jpeg?dl=1" title="IMG_56621" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3709501ecbeea8e148ca9d9fd08249e416ee11b_2_666x500.jpeg" alt="IMG_56621" data-base62-sha1="uatX2k1gHfUSajCvghmrj7TTUJZ" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3709501ecbeea8e148ca9d9fd08249e416ee11b_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3709501ecbeea8e148ca9d9fd08249e416ee11b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3709501ecbeea8e148ca9d9fd08249e416ee11b.jpeg 2x" data-dominant-color="AEA59A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_56621</span><span class="informations">816×612 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2018-10-29 14:00 UTC)

<p>Can you please try with <a href="https://download.slicer.org/">4.10</a>? A few DVH-related fixes have been made since 4.8.1.</p>

---

## Post #3 by @lassoan (2018-10-29 14:24 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I’m wondering what oversampling factor would be used for the CTV. The data set looks very unusual in that the whole upper body is imaged and contoured - maybe the huge region of interest causes DVH computation to be performed at relatively low resolution?</p>

---

## Post #4 by @cpinter (2018-10-29 16:31 UTC)

<p>The oversampling factor is a constant 2 by default, so the resolution should be fine.</p>

---

## Post #5 by @lassoan (2018-10-29 17:02 UTC)

<p>I suspect that dose gradient is high at the CTV surface, therefore minor numerical differences in how a 3D region-of-interest is computed from planar contours and how that region is used for integrating dose values can cause significant difference in the DVH.</p>
<p>When comparing DVHs, both volume and dose differences must be considered (see dose comparison module in Slicer). 41cGy volume computed by Slicer/ISOgray differs by approximately 5%. This value is not small, but may be inevitable in case of an ill-conditioned problem. It would be interesting to test this data set in a few other RT planning software to see how much the CTV’s DVH varies.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> At some point, we added heuristics to not oversample large structures. Maybe the CTV (it seems to be the entire breast) exceeds the size limit?</p>
<p><a class="mention" href="/u/merymb">@MeryMB</a> What is the volume spacing of the CT volume and the dose volume? (you can find the values in Volumes module / Volume information section). Could you please also post a screenshot with the dose volume overlaid with segments (especially the CTV) to see how steep the dose gradient is at the segment boundary? Even better, could you share the data set? Could you compute the DVH in other software (CERR, Pinnacle, etc)?</p>

---

## Post #6 by @cpinter (2018-10-29 18:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="4569">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>At some point, we added heuristics to not oversample large structures. Maybe the CTV (it seems to be the entire breast) exceeds the size limit?</p>
</blockquote>
</aside>
<p>That heuristics is only enabled if the “A/O” (automatic oversampling) checkbox is checked in the DVH module next to the dose volume selector. By default is off, and so there is a constant oversampling of 2.</p>
<p><a class="mention" href="/u/merymb">@MeryMB</a></p>
<ol>
<li>By turning A/O on, the resolution of the CTV will probably increase.</li>
<li>You can also manually increase the resolution in the Segment Editor module. Select the segmentation, the dose volume as master volume, click the small box icon next to the master selector, and after choosing the dose volume as source geometry, choose oversampling factor of 4.</li>
</ol>
<p>Can you calculate DVHs after trying both?</p>

---

## Post #7 by @MeryMB (2018-10-31 08:31 UTC)

<p>Hi Dear Csaba Pinter</p>
<p>I tried with the new version of 3D Slicer (4.10.0).<br>
As you suggested I should turn on A/O or increase the resolution in the Segment Editor module. it works.<br>
But I encounter another problem again. when I draw the DVH with this version, the dose axis is not correct. it should be between 0 to 52 Gy but it increase to 250-260 Gy and when scroll on the DVH graph, it only show the percentage of volume, not dose!!!  I attached the screenshot of the new DVH with new version.</p>
<p>Best Regards<br>
Mery</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51fe07845441920ca1d163dfb92a64ab39fae83b.png" data-download-href="/uploads/short-url/bHkVGRIRYepvSaVCocsa3JIQ6bV.png?dl=1" title="Screenshot%20from%202018-10-31%2010-52-51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51fe07845441920ca1d163dfb92a64ab39fae83b_2_690x324.png" alt="Screenshot%20from%202018-10-31%2010-52-51" data-base62-sha1="bHkVGRIRYepvSaVCocsa3JIQ6bV" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51fe07845441920ca1d163dfb92a64ab39fae83b_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51fe07845441920ca1d163dfb92a64ab39fae83b_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51fe07845441920ca1d163dfb92a64ab39fae83b_2_1380x648.png 2x" data-dominant-color="979890"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-10-31%2010-52-51</span><span class="informations">2044×961 355 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @cpinter (2018-10-31 10:52 UTC)

<p>Thanks for the update!</p>
<p>When you say automatic oversampling works it means that the difference between your TPS and Slicer’s DVH is gone and they are almost the same?</p>
<p>The difference between dose values might be a side effect of my recent refactoring of DVH plotting. Can you please go to the volumes module, select the dose, and send me the scalar range (min,max)? In the meantime I’ll check this out myself.</p>
<aside class="quote no-group" data-username="MeryMB" data-post="7" data-topic="4569">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f19dbf/48.png" class="avatar"> MeryMB:</div>
<blockquote>
<p>when scroll on the DVH graph, it only show the percentage of volume, not dose</p>
</blockquote>
</aside>
<p>Can you please elaborate? I’m not sure if I understand what does scrolling on the graph means.</p>
<p>One last question. I see that your dataset is a very nice breast phantom one. Would it be possible to share it with us for future testing and demonstration purposes? Thank you!</p>

---

## Post #9 by @MeryMB (2018-10-31 12:30 UTC)

<p>Hi Dear Csaba Pinter</p>
<p>Thanks for your answering my questions.</p>
<p>I dont know how should I check that they are the same or not “When you say automatic oversampling works it means that the difference between your TPS and Slicer’s DVH is gone and they are almost the same?”<br>
but when I turn on the O/A, the DVH become correct and the problem will solve. it dont show correctly on the grapg but when you export it as a file the data which extracted, is ok!!</p>
<p>I attached the volume information of dose so you can check what you want.</p>
<p>For Scorlling the mouse I mean when I move the mouse sign on the graph. When I move the mouse on the graph, I only see the volume percentage not with the dose. because in the previous version or in TPS you see both of them (the volume and the dose) .</p>
<p>For breast phantom, it is only the CT DICOM of our Rando Phantom which we did it in our department. I should get permission from department but I think no problem for that. I will inform you.</p>
<p>Best<br>
Mery</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d066bb246fd1407c49a25f06f297290f9ee3c89.png" data-download-href="/uploads/short-url/k7z4VXZvFUwze85KUAZf3kucm3T.png?dl=1" title="Screenshot%20from%202018-10-31%2015-45-48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d066bb246fd1407c49a25f06f297290f9ee3c89_2_690x324.png" alt="Screenshot%20from%202018-10-31%2015-45-48" data-base62-sha1="k7z4VXZvFUwze85KUAZf3kucm3T" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d066bb246fd1407c49a25f06f297290f9ee3c89_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d066bb246fd1407c49a25f06f297290f9ee3c89_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d066bb246fd1407c49a25f06f297290f9ee3c89_2_1380x648.png 2x" data-dominant-color="999991"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-10-31%2015-45-48</span><span class="informations">2044×961 355 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2018-10-31 12:44 UTC)

<p>You need to change the plot type from “line” to “scatter” (for line type, X axis is always the element index).</p>

---

## Post #11 by @cpinter (2018-10-31 13:01 UTC)

<p>Thank you both for the replies! I’ll change it to scatter plot to fix the X axis labels, and will try to fix the popup so that both the V and D values are shown.</p>

---

## Post #12 by @cpinter (2018-10-31 13:20 UTC)

<p>Done, both issues should be fixed if you update the extension tomorrow. Thanks for reporting the issues!</p>

---
