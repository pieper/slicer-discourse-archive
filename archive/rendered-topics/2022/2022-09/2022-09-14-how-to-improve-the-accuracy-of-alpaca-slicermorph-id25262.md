# How to improve the accuracy of ALPACA @slicerMorph?

**Topic ID**: 25262
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/how-to-improve-the-accuracy-of-alpaca-slicermorph/25262

---

## Post #1 by @MrMarkus (2022-09-14 13:48 UTC)

<p>Hi,</p>
<p>the following experiment was performed in order to “validate” the accuracy of slicerMorph/ALPACA.</p>
<ul>
<li>
<p>2 skull samples were measured on CT</p>
</li>
<li>
<p>9 landmarks were manually placed on each of the two samples</p>
</li>
<li>
<p><strong>experiment <span class="hashtag">#1</span></strong> ALPACA:  sample_01 served as source, sample _02 served as target</p>
</li>
<li>
<p><strong>experiment <span class="hashtag">#2</span></strong> ALPACA:  sample_02 served as source, sample _01 served as target</p>
</li>
</ul>
<p>One landmark was “troublesome”.</p>
<p><em>In experiment <span class="hashtag">#1</span> the landmark <span class="hashtag">#3</span> was inaccurate.</em></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f26a2e914d6d8bba0abe25816275ebed4a2a57ac.jpeg" data-download-href="/uploads/short-url/yAv2zDNLq8YXS9lD76mUSDzO2i8.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f26a2e914d6d8bba0abe25816275ebed4a2a57ac_2_690x472.jpeg" alt="grafik" data-base62-sha1="yAv2zDNLq8YXS9lD76mUSDzO2i8" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f26a2e914d6d8bba0abe25816275ebed4a2a57ac_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f26a2e914d6d8bba0abe25816275ebed4a2a57ac_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f26a2e914d6d8bba0abe25816275ebed4a2a57ac.jpeg 2x" data-dominant-color="C5C6C8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1186×813 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><em>In experiment <span class="hashtag">#2</span> the landmark <span class="hashtag">#3</span> was “accurate”</em></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/784d50156347ff4356193a1ae558c93458d87e77.jpeg" data-download-href="/uploads/short-url/haeWbhRkU1BDyCNuqkRbGqy7CWH.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/784d50156347ff4356193a1ae558c93458d87e77_2_687x500.jpeg" alt="grafik" data-base62-sha1="haeWbhRkU1BDyCNuqkRbGqy7CWH" width="687" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/784d50156347ff4356193a1ae558c93458d87e77_2_687x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/784d50156347ff4356193a1ae558c93458d87e77_2_1030x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/784d50156347ff4356193a1ae558c93458d87e77.jpeg 2x" data-dominant-color="C1C2C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1120×815 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol>
<li>
<p>How the performance of this destinct landmark can be improved?</p>
</li>
<li>
<p>Why is the performance of ALPACA for the two experiments different in terms of placing the landmark <span class="hashtag">#3</span>?</p>
</li>
</ol>
<p>Is this the reason one should go for “Comparing semi-landmarking approaches for analyzing three-dimensional cranial morphology” (10.1002/ajpa.24214) ?</p>
<p>Thanks!</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2022-09-14 16:18 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="1" data-topic="25262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<ul>
<li>How the performance of this destinct landmark can be improved?</li>
<li>Why is the performance of ALPACA for the two experiments different in terms of placing the landmark <span class="hashtag-raw">#3</span>?</li>
</ul>
</blockquote>
</aside>
<p><span class="hashtag-raw">#2</span> is easier to answer. They are different because you swapped the sample that defines the points. The registration you obtain via ALPACA is not necessarily symmetric (has no claim to be so). So when you swap reference and target you will get a different result.</p>
<p><span class="hashtag-raw">#1</span> It is not easy to manipulate the parameters to improve the performance of a single landmark. That’s because the registration is a global optimization. You can try to adjust the alpha and beta parameters of the CPD deformable registration step (under advanced settings) and see if you can improve. Technical details are in this paper <a href="https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13689">https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13689</a> (see the sections 2.2). Be warned that the defaults settings are the best for mouse skulls that we were able to determine.</p>
<p>So both of these points illustrate the limit of using a single reference to automatically estimate LMs in new target. You can usually do a much better job if you can use multiple references. We have implemented the multi-template ALPACA  (MALPACA). The <a href="https://www.biorxiv.org/content/10.1101/2022.01.04.474967v1.article-metrics">preprint is out on biorxiv</a>. You can follow the steps there to obtain the prototype (we will incorporate it into SlicerMorph, once the paper is accepted).</p>
<aside class="quote no-group" data-username="MrMarkus" data-post="1" data-topic="25262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>Is this the reason one should go for “Comparing semi-landmarking approaches for analyzing three-dimensional cranial morphology” (10.1002/ajpa.24214) ?</p>
</blockquote>
</aside>
<p>Most semiLM approaches require presence of existing set of anatomical LMs to constrain their placement. If the anatomical landmarks are good, and the semiLM patches are created correctly, that paper shows that semiLM methods can be very good to estimate local shape differences. However, it requires more work (you need to create those anatomical landmarks first). SO there are many trades of between accuracy and analytical throughput based on sample sizes and the ultimate methodological choice depends on what you are comfortable with.</p>

---

## Post #3 by @MrMarkus (2022-09-15 11:26 UTC)

<p>Thanks!</p>
<p>Changing the CPD parameter worked in this case. alpha = 2, beta = 7.</p>
<p>I definitely will try the Mighty-ALPACA <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p>Best,<br>
Markus</p>

---

## Post #4 by @muratmaga (2022-09-15 15:10 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="3" data-topic="25262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>Changing the CPD parameter worked in this case. alpha = 2, beta = 7.</p>
</blockquote>
</aside>
<p>This is great, did the other points end up staying where they were supposed to be? In the current version of the ALPACA, you can quantify this, if you provide a the fixed set of landmarks on the target. This is an optional setup. If you do, ALPACA will report the RMSE (root mean squared error) between the estimated landmark position and your manual ones in a table. As you iterate over settings, new values are added to take, making the decision somewhat more quantitative then just visual.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c327a64e57a9e1cfa0c256311e4098ccb6098d24.png" alt="image" data-base62-sha1="rQq3s37RVV0H7gg3kx8yyABcuMs" width="601" height="237"></p>

---

## Post #5 by @MrMarkus (2022-09-19 15:00 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>,</p>
<p>thanks for this hint. Indeed, the by changing the beta = 7 the RMSE decreased.</p>
<p>I have noticed that in the ALPACA publication the skull was downsampled from 36 µm³ to 500 µm³.<br>
Do you recommend to do so and what would be the practical way using 3DSlicer?</p>
<p>Thanks.<br>
Markus</p>

---

## Post #6 by @muratmaga (2022-09-19 15:40 UTC)

<p>We have heavily downsampled sample data we provide for ALPACA, because we wanted datasets downloaded quickly so that people can use our tutorials.</p>
<p>The degree you want to decimate your model is up to you really. If you are deriving your model from microCT scans of sufficient resolution, you might be able to decimate the final model 80-90% without much loss of detail. But you have to do it yourself and see what’s acceptable.</p>

---
