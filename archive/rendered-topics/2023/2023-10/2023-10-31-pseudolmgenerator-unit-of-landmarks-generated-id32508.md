---
topic_id: 32508
title: "Pseudolmgenerator Unit Of Landmarks Generated"
date: 2023-10-31
url: https://discourse.slicer.org/t/32508
---

# PseudoLMGenerator - unit of Landmarks generated

**Topic ID**: 32508
**Date**: 2023-10-31
**URL**: https://discourse.slicer.org/t/pseudolmgenerator-unit-of-landmarks-generated/32508

---

## Post #1 by @Vignesh_Chakravarthy (2023-10-31 15:56 UTC)

<p>Hi Dr. Murat,</p>
<p>I am using PseudoLMGenerator to get landmarks on the prostate model (slicer 5.2.2). I am attaching the details of the model for reference (surface area and volume are calculated in mm2 and mm3 respectively). I have reduced the spacing tolerance to 0 to get more landmarks. Please clarify my two doubts.</p>
<ol>
<li>What is the unit of the landmarks generated? The distance between two points in the projectedLM. I believe it is mm in my case.</li>
<li>I am interested in obtaining more landmarks out of the model. But the maximum points I can obtain is 1852 even when the spacing tolerance is 0. Is there any way to get template with more points?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83736729e86dd77c52e7f7b3838c1460a3966c0c.jpeg" data-download-href="/uploads/short-url/iKRNuYk0e2VzkNxfkq9cORhjcmM.jpeg?dl=1" title="pseudolm_pros" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83736729e86dd77c52e7f7b3838c1460a3966c0c_2_690x362.jpeg" alt="pseudolm_pros" data-base62-sha1="iKRNuYk0e2VzkNxfkq9cORhjcmM" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83736729e86dd77c52e7f7b3838c1460a3966c0c_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83736729e86dd77c52e7f7b3838c1460a3966c0c_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83736729e86dd77c52e7f7b3838c1460a3966c0c_2_1380x724.jpeg 2x" data-dominant-color="B5AFB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pseudolm_pros</span><span class="informations">1917×1008 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1269861d1b714d9949db54c92404f67a2eeca16.jpeg" data-download-href="/uploads/short-url/mZBySTAyavddceh2q9dY8IZ6fEa.jpeg?dl=1" title="pros_details" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1269861d1b714d9949db54c92404f67a2eeca16_2_274x500.jpeg" alt="pros_details" data-base62-sha1="mZBySTAyavddceh2q9dY8IZ6fEa" width="274" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1269861d1b714d9949db54c92404f67a2eeca16_2_274x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1269861d1b714d9949db54c92404f67a2eeca16_2_411x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1269861d1b714d9949db54c92404f67a2eeca16_2_548x1000.jpeg 2x" data-dominant-color="F2F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pros_details</span><span class="informations">554×1009 65.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>Thanks,<br>
Vignesh</p>

---

## Post #2 by @smrolfe (2023-10-31 17:12 UTC)

<p><a class="mention" href="/u/vignesh_chakravarthy">@Vignesh_Chakravarthy</a> The spacing tolerance is specified as a percentage of the bounding box diagonal, rather than an absolute value.</p>
<p>The number of landmark points you can generate is limited by the number of points in your original mesh. It’s a little hard to see in your screenshot, but it looks like your prostate model has 1854 points. This is the best you can do with the tolerance set to 0. You are getting 1852 points, which is likely because the filter used in this step will automatically remove any coincident points and you likely had a couple in your model.</p>
<p>To generate more points, you can try useing the <code>Uniform remesh</code> tool in the <code>Surface Toolbox</code> module to oversample your model. Then run the PseudoLMGenerator on the new model.</p>

---

## Post #3 by @Vignesh_Chakravarthy (2023-10-31 17:28 UTC)

<p>Hi Sara,</p>
<p>Thanks for the clarification. Could you please let me know the unit of measurement between points in the generated template?</p>
<p>Regards,<br>
Vignesh</p>

---

## Post #4 by @smrolfe (2023-10-31 17:30 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="2" data-topic="32508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>To generate more points, you can try useing the <code>Uniform remesh</code> tool in the <code>Surface Toolbox</code> module to oversample your model. Then run the PseudoLMGenerator on the new model.</p>
</blockquote>
</aside>
<p>As an example of what’s possible, I’m attaching a screenshot of 552 points sampled on a model with 552 points, and a screenshot of 1513 points sampled on the surface of the same model after uniform remeshing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df34f8e5458095b2e5051d045b74750edb5d3a32.png" data-download-href="/uploads/short-url/vQzY2DJbZWhzewUuzzTQt1Wn4xs.png?dl=1" title="549" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df34f8e5458095b2e5051d045b74750edb5d3a32_2_690x474.png" alt="549" data-base62-sha1="vQzY2DJbZWhzewUuzzTQt1Wn4xs" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df34f8e5458095b2e5051d045b74750edb5d3a32_2_690x474.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df34f8e5458095b2e5051d045b74750edb5d3a32_2_1035x711.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df34f8e5458095b2e5051d045b74750edb5d3a32.png 2x" data-dominant-color="A89594"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">549</span><span class="informations">1276×878 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60456a476f0ec04453fcb55d99ba55c0d3e0cf2e.png" data-download-href="/uploads/short-url/dJEyCEee2jbX0xM5ioyQmZVVzci.png?dl=1" title="1513" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60456a476f0ec04453fcb55d99ba55c0d3e0cf2e_2_690x475.png" alt="1513" data-base62-sha1="dJEyCEee2jbX0xM5ioyQmZVVzci" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60456a476f0ec04453fcb55d99ba55c0d3e0cf2e_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60456a476f0ec04453fcb55d99ba55c0d3e0cf2e_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60456a476f0ec04453fcb55d99ba55c0d3e0cf2e.png 2x" data-dominant-color="A9A59D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1513</span><span class="informations">1278×881 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @smrolfe (2023-10-31 17:35 UTC)

<aside class="quote no-group" data-username="Vignesh_Chakravarthy" data-post="3" data-topic="32508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vignesh_chakravarthy/48/66674_2.png" class="avatar"> Vignesh_Chakravarthy:</div>
<blockquote>
<p>Could you please let me know the unit of measurement between points in the generated template?</p>
</blockquote>
</aside>
<p>The landmarks points are sampled from the model, so will be in the same units as the original. The enforced distance between the points is measured as a fraction of the bounding box diagonal.</p>

---

## Post #6 by @muratmaga (2023-10-31 17:58 UTC)

<aside class="quote no-group" data-username="Vignesh_Chakravarthy" data-post="3" data-topic="32508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vignesh_chakravarthy/48/66674_2.png" class="avatar"> Vignesh_Chakravarthy:</div>
<blockquote>
<p>nit of measurement between points in the generated template?</p>
</blockquote>
</aside>
<p>It is in the same units as your original data (in this case model).</p>

---

## Post #7 by @Vignesh_Chakravarthy (2023-10-31 19:31 UTC)

<p>Thanks Dr. Sara and Dr. Murat for your prompt responses. I can oversample the model using “surface Toolkit” and get desired number of landmarks with PseudoLMGenerator!</p>

---
