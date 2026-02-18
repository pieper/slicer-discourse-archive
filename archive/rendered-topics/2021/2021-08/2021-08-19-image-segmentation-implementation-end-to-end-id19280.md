# Image segmentation implementation end to end

**Topic ID**: 19280
**Date**: 2021-08-19
**URL**: https://discourse.slicer.org/t/image-segmentation-implementation-end-to-end/19280

---

## Post #1 by @Aamir_Khan (2021-08-19 23:37 UTC)

<p>Hi. I have been trying to implement a deep learning based automatic segmentation for pelvic bone structure. I have a few questions:</p>
<ol>
<li>
<p>Is there some open source pelvic bone structure image segmentation dataset already implemented? (or some source where I can find data like these)</p>
</li>
<li>
<p>Roughly speaking, how much training data do I need to implement this segmentation procedure?</p>
</li>
<li>
<p>Roughly speaking, how long would the data preparation take?</p>
</li>
<li>
<p>Would we need specific trained model for specific type of patients? For example, one group of patient already has an implant placed and other group has no implants placed.</p>
</li>
<li>
<p>Roughly speaking, how much total time would be required to implement this procedure end to end? (weeks, months etc)</p>
</li>
<li>
<p>Can you suggest any good graphics card which could provide state of the art results?</p>
</li>
</ol>

---

## Post #2 by @pieper (2021-08-23 12:34 UTC)

<aside class="quote no-group" data-username="Aamir_Khan" data-post="1" data-topic="19280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aamir_khan/48/8627_2.png" class="avatar"> Aamir_Khan:</div>
<blockquote>
<p>Is there some open source pelvic bone structure image segmentation dataset already implemented? (or some source where I can find data like these)</p>
</blockquote>
</aside>
<p>I don’t think that exists - if you find one or create one be sure to report back!</p>
<p>The rest of your questions are pretty open-ended so it’s hard to give you any specifics.  It all depends on what kind of data you want to segment. High resolution CT would be best, but can you justify the radiation exposure and cost?  Are these patients who may have implants leading to metal artifacts in the scan?  How much accuracy do you need? These and many other details influence what segmentation approach you might take and how much data and time you will need to invest.  Best if you read up in the literature to see what other people have done and see how that compares to your case.</p>

---

## Post #3 by @lassoan (2021-08-23 15:41 UTC)

<p>Exact details depend on the specifics, as <a class="mention" href="/u/pieper">@pieper</a> explained, but some rough estimates:</p>
<aside class="quote no-group" data-username="Aamir_Khan" data-post="1" data-topic="19280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aamir_khan/48/8627_2.png" class="avatar"> Aamir_Khan:</div>
<blockquote>
<p>Is there some open source pelvic bone structure image segmentation dataset already implemented? (or some source where I can find data like these)</p>
</blockquote>
</aside>
<p>Hundreds of thousands of pelvic CTs are acquired every year for external beam radiation therapy treatment planning of prostate cancer. Bones are (roughly) segmented in probably most of them so, there is definitely lots of data sets out there. You “just” need to go out and get them. Of course, a CT acquired for radiation therapy treatment planning might not be perfect for planning musculoskeletal interventions, and if you don’t just need segment all the bones as one piece but also separate them then segmentation is not that trivial. So, depending on what exactly you need, it may or may not be easy to access lots of data. You can find freely usable, potentially segmented CTs on <a href="https://www.cancerimagingarchive.net/collections/">TCIA</a>. For example, Siewerdsen et al. used <a href="https://github.com/rhan93/Altas-of-Pelvis-Segmentation-and-Trajectory-Planning">40 CTs from TCIA to create a statistical model of left/right hip and sacrum</a>. You may find relevant data in various deep learning challenges or you can also contact authors that have data sets but did not share the publicly.</p>
<aside class="quote no-group" data-username="Aamir_Khan" data-post="1" data-topic="19280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aamir_khan/48/8627_2.png" class="avatar"> Aamir_Khan:</div>
<blockquote>
<p>Roughly speaking, how much training data do I need to implement this segmentation procedure?</p>
</blockquote>
</aside>
<p>You can segment bones on CTs pretty well, so if you use classic semiautomatic methods such as “Grow from seeds”, you don’t need to do any training. If you use classic statistical learning (e.g., statistical atlases) then a few dozens should suffice. If you use convolutional neural networks then probably you need a few hundred to get good confidence.</p>
<aside class="quote no-group" data-username="Aamir_Khan" data-post="1" data-topic="19280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aamir_khan/48/8627_2.png" class="avatar"> Aamir_Khan:</div>
<blockquote>
<p>Roughly speaking, how long would the data preparation take?</p>
</blockquote>
</aside>
<p>If you are experienced in this and you can get a suitable database then you may need just a few days. If you need to build the database from scratch and you have never segmented CTs, etc. then it may take 1-2 weeks for you to learn to segment from clinicians, figure out a good segmentation workflow using semi-automatic tools (grow from seeds, etc.). You can then probably segment 10-20 data sets per day.</p>
<p>You can try use <a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel</a> Slicer extension, which starts to train the neural network as you are segmenting each case and you might get useful preliminary segmentation which might speed up the segmentation. This concept has not been tested very widely, but on a relatively easy problem like this, it may work well.</p>
<aside class="quote no-group" data-username="Aamir_Khan" data-post="1" data-topic="19280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aamir_khan/48/8627_2.png" class="avatar"> Aamir_Khan:</div>
<blockquote>
<p>Roughly speaking, how much total time would be required to implement this procedure end to end? (weeks, months etc)</p>
</blockquote>
</aside>
<p>Finding a good network configuration and train and validate it takes probably a few weeks for someone who already completed a couple of projects like this. For a student who is completely new to the entire field it probably takes half a year.</p>
<aside class="quote no-group" data-username="Aamir_Khan" data-post="1" data-topic="19280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aamir_khan/48/8627_2.png" class="avatar"> Aamir_Khan:</div>
<blockquote>
<p>Can you suggest any good graphics card which could provide state of the art results?</p>
</blockquote>
</aside>
<p>It might save you some time if you don’t have to worry less about running out of GPU memory. So, I would recommend getting an NVidia RTC3090 with 24GB GPU RAM. Do to power and cooling requirements, it is not easy to just stick a card like this into an existing PC, so I would recommend to buy a gaming PC or a workstation that already comes with a card like this.</p>
<p>If you don’t want to invest into hardware or wait for a physical device to be shipped then you can rent virtual machines with GPUs from cloud providers. However, if you are experimenting a lot (doing lots of overnight training), then most likely you’ll end up paying more compared to buying your own hardware.</p>

---

## Post #4 by @Aamir_Khan (2021-08-25 11:52 UTC)

<p>Thanks a lot for your valuable suggestions.</p>

---
