---
topic_id: 3529
title: "Saving Transformed Label Map For Radiomics Analysis"
date: 2018-07-20
url: https://discourse.slicer.org/t/3529
---

# Saving transformed label map for radiomics analysis

**Topic ID**: 3529
**Date**: 2018-07-20
**URL**: https://discourse.slicer.org/t/saving-transformed-label-map-for-radiomics-analysis/3529

---

## Post #1 by @xuec (2018-07-20 03:31 UTC)

<p>Operating system: MacOs 10.13<br>
Slicer version: 4.8.1</p>
<p>Hi,</p>
<p>So I had a label map (which was made by drawing ROI in the editor module–&gt; call it LabelMap1), which then I transformed it using transform module then apply it using the Resample Image module to produced a transformed labelmap (call it Labelmap2).<br>
I chose the output as Labelmap volume hoping that it will just work like previously when I use them in Radiomics (standalone).</p>
<p>However, I am not sure why if I put in the LabelMap2 as mask to the Radiomics, it just did not give any results, but when I enter the LabelMap1 (drawn from editor module) to the Radiomics, it works just fine.</p>
<p>Is there any difference in the output or way to export it? I would really appreciate any hints or any help on this. Thank you very much in advance!</p>

---

## Post #2 by @lassoan (2018-07-20 03:58 UTC)

<aside class="quote no-group quote-modified" data-username="xuec" data-post="1" data-topic="3529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xuec/48/77755_2.png" class="avatar"> xuec:</div>
<blockquote>
<p>it saved as a volume rather than label map</p>
</blockquote>
</aside>
<p>Scalar and labelmap volumes are saved exactly the same way. When you load a volume, you can specify in “Add data” dialog to load the volume is a labelmap; or you can change the volume type later (in Volumes module).</p>

---

## Post #3 by @xuec (2018-07-20 04:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="3529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>When you load a volume, you can specify in “Add data” dialog to load the volume is a labelmap; or you can change the volume type later (in Volumes module).</p>
</blockquote>
</aside>
<p>Thank you very much for the fast response.<br>
I know that we could do this, however, if we load the labelmap1 (the one that drawn in editor module), slicer will directly know that it is a labelmap, however, the labelmap2 (the one I transformed and saved as labelmap), slicer will directly load it as volumes rather than labelmap. Because I run the radiomics outside slicer, so I cannot change the volume type later on. So, I was just wondering if I could just save it with the same settings as the Labelmap1 with just some transformations.</p>
<p>I am sorry if the questions might not be too clear, please let me know if I need to explain more. Thank you. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2018-07-20 04:55 UTC)

<aside class="quote no-group" data-username="xuec" data-post="3" data-topic="3529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xuec/48/77755_2.png" class="avatar"> xuec:</div>
<blockquote>
<p>slicer will directly know that it is a labelmap, however, the labelmap2 (the one I transformed and saved as labelmap)</p>
</blockquote>
</aside>
<p>There may be some heuristics that try to set the default loading format correctly (e.g., if the filename ends with “-label” then loads it as labelmap by default), but scalar and labelmap volumes are otherwise saved exactly the same way.</p>
<aside class="quote no-group" data-username="xuec" data-post="3" data-topic="3529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xuec/48/77755_2.png" class="avatar"> xuec:</div>
<blockquote>
<p>I run the radiomics outside slicer</p>
</blockquote>
</aside>
<p>Do you compute radiomics features using Slicer, but from command-line (without using graphical user interface)? Or a completely different software?</p>

---

## Post #5 by @xuec (2018-07-20 05:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="3529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you compute radiomics features using Slicer, but from command-line (without using graphical user interface)? Or a completely different software?</p>
</blockquote>
</aside>
<p>yepp… I compute the radiomics not using Slicer, but use Mac Terminal.</p>

---

## Post #6 by @xuec (2018-07-20 08:12 UTC)

<p>Hi,<br>
I just try to run it to radiomics in slicer, it doesn’t seem to work too. It did not give any output (such as table).</p>
<p>I am very confused, what I did is just transform (which is translate the mask to the right side), however, it ended up not being able to run in radiomics.</p>
<p>Any tips in solving this problem please? Thank you</p>

---

## Post #7 by @JoostJM (2018-08-07 09:51 UTC)

<p>Which package are you using? SlicerRadiomics / PyRadiomics?<br>
Can you share an (anonymized) copy of the image and the labelmap that is not working?</p>

---
