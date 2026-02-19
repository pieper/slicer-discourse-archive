---
topic_id: 11264
title: "Question About Cervical Spine Tool"
date: 2020-04-23
url: https://discourse.slicer.org/t/11264
---

# Question about cervical spine tool

**Topic ID**: 11264
**Date**: 2020-04-23
**URL**: https://discourse.slicer.org/t/question-about-cervical-spine-tool/11264

---

## Post #1 by @yf025 (2020-04-23 09:17 UTC)

<p>I can not find any results（like segments or lables） after locating c1-7 and press run（it takes about several seconds），is there anyone who have experience in this tool，please tell me how to use this tool，thx！！<br>
ps：I put the location fiducials in spinal canal for each c vertebra</p>

---

## Post #2 by @yf025 (2020-04-27 02:35 UTC)

<p>anyone who can help me？</p>

---

## Post #3 by @muratmaga (2020-04-27 03:58 UTC)

<p>I haven’t used the tool, so I can’t tell why it is not working. But from their own github description and as well as the video on youtube, it seems to do a very rough job anyways. You can probably do better manual segmentations of cervicals using the effects in the segment editor directly. This is probably a good starting place:<br>
</p><div class="lazyYT" data-youtube-id="Uht6Fwtr9hE" data-youtube-title="How to segment multiple vertebrae in spine CT for 3D printing" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #4 by @brhoom (2020-10-20 19:33 UTC)

<p>Sorry for the late reply, I missed this post somehow.</p>
<blockquote>
<p>I can not find any results（like segments or lables） after locating c1-7 and press run（it takes about several seconds），is there anyone who have experience in this tool，please tell me how to use this tool，thx！！<br>
ps：I put the location fiducials in spinal canal for each c vertebra</p>
</blockquote>
<p>It is always good to add the error message from the python console and check the output folder in your_home/VisSimTools/output. You can also try the vertebra tool which segments one vertebra. We are planning to add an updated version with more and improved features in the upcoming weeks.</p>
<blockquote>
<p>But from their own github description and as well as the video on youtube, it seems to do a very rough job anyways. You can probably do better manual segmentations of cervicals using the effects in the segment editor directly. This is probably a good starting place:</p>
</blockquote>
<p>Correct, I already mentioned it gives an approximation so it is not a very accurate segmentation but it has the advantages of getting separated vertebrae in a very short time (the result in the above video has connected vertebrae).</p>

---
