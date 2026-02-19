---
topic_id: 45999
title: "Transform Source To Target 3D Model"
date: 2026-01-30
url: https://discourse.slicer.org/t/45999
---

# Transform Source to Target 3D Model

**Topic ID**: 45999
**Date**: 2026-01-30
**URL**: https://discourse.slicer.org/t/transform-source-to-target-3d-model/45999

---

## Post #1 by @md.walten (2026-01-30 13:19 UTC)

<p>Hello</p>
<p>I am doing a research study with human bones where every bone has a little bit of different area das is marked and I would like to transform a source model exactly to a target bone so I can see the difference between the markings on the target model (.ply). The most important area for the overlap is the joint surface. I tried alpaca but the model ends up in a distorted model and does not look the same. Then I tried the IGT fiducial registration wizard with similarity, which comes very close, but the models are not exactly overlapped. What would be the best way to get a nice overlap of both models? I added 2 models with the markings which I want to overlap.</p>
<p>Thank you for your help</p>
<p>Manuel</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b520f3339d074517279e65ab40a2ae3bd636e05c.jpeg" data-download-href="/uploads/short-url/pQl14aCZ04q52J6l7BH4D2E6DVy.jpeg?dl=1" title="Bildschirmfoto 2026-01-29 um 21.46.13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b520f3339d074517279e65ab40a2ae3bd636e05c_2_412x500.jpeg" alt="Bildschirmfoto 2026-01-29 um 21.46.13" data-base62-sha1="pQl14aCZ04q52J6l7BH4D2E6DVy" width="412" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b520f3339d074517279e65ab40a2ae3bd636e05c_2_412x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b520f3339d074517279e65ab40a2ae3bd636e05c_2_618x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b520f3339d074517279e65ab40a2ae3bd636e05c.jpeg 2x" data-dominant-color="9D9FCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2026-01-29 um 21.46.13</span><span class="informations">822×996 77.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d32b7f1b10c9521e3ebc894025868a6cd40a1248.jpeg" data-download-href="/uploads/short-url/u85W6djZinTNWtOkkx3xVfeUtZe.jpeg?dl=1" title="Bildschirmfoto 2026-01-29 um 21.46.07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d32b7f1b10c9521e3ebc894025868a6cd40a1248_2_393x500.jpeg" alt="Bildschirmfoto 2026-01-29 um 21.46.07" data-base62-sha1="u85W6djZinTNWtOkkx3xVfeUtZe" width="393" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d32b7f1b10c9521e3ebc894025868a6cd40a1248_2_393x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d32b7f1b10c9521e3ebc894025868a6cd40a1248_2_589x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d32b7f1b10c9521e3ebc894025868a6cd40a1248_2_786x1000.jpeg 2x" data-dominant-color="A2A4D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2026-01-29 um 21.46.07</span><span class="informations">800×1016 80 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-01-30 17:57 UTC)

<aside class="quote no-group" data-username="md.walten" data-post="1" data-topic="45999">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a4c791/48.png" class="avatar"> md.walten:</div>
<blockquote>
<p>Then I tried the IGT fiducial registration wizard with similarity, which comes very close, but the models are not exactly overlapped.</p>
</blockquote>
</aside>
<p>Are these models the same (e.g., surgical treatment before and after), or two different bones? If latter, you need deformable registration to align them, similarity will make it close, but cannot account for small localized difference.</p>
<p>ALPACA is not a registration tool. Use FastModelAlign (in SlicerMorph), and enable deformable registration</p>

---

## Post #3 by @md.walten (2026-01-30 21:37 UTC)

<p>Hi Muratmaga</p>
<p>Thank you for your answer. yes these are 2 different bones. I tried Fastmodel along, but I do not find “enable deformable registration” in the module (see attachment). I use slicer 5.10.</p>
<p>Yesterday I tried the IGT first to align with similarity and then run alpaca. Then I got a pretty close match (attached).. The most important overlap has to be the joint surface which looks almost perfect now. However I am not sure if this is really the correct way to do it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddad3b617afeb353eeb5eac486af14b8f519c65e.png" data-download-href="/uploads/short-url/vD2Fszzkn7AMhUUUZDI0UCku3My.png?dl=1" title="Bildschirmfoto 2026-01-30 um 22.36.15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddad3b617afeb353eeb5eac486af14b8f519c65e_2_368x499.png" alt="Bildschirmfoto 2026-01-30 um 22.36.15" data-base62-sha1="vD2Fszzkn7AMhUUUZDI0UCku3My" width="368" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddad3b617afeb353eeb5eac486af14b8f519c65e_2_368x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddad3b617afeb353eeb5eac486af14b8f519c65e_2_552x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddad3b617afeb353eeb5eac486af14b8f519c65e_2_736x998.png 2x" data-dominant-color="2C2C2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2026-01-30 um 22.36.15</span><span class="informations">1288×1746 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2db854a5676d7ea7ac1029c21b53c6f65c6a75eb.jpeg" data-download-href="/uploads/short-url/6wspAFdPmUvUPeLZHHUmbD9ybXl.jpeg?dl=1" title="Bildschirmfoto 2026-01-30 um 22.35.43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2db854a5676d7ea7ac1029c21b53c6f65c6a75eb_2_467x499.jpeg" alt="Bildschirmfoto 2026-01-30 um 22.35.43" data-base62-sha1="6wspAFdPmUvUPeLZHHUmbD9ybXl" width="467" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2db854a5676d7ea7ac1029c21b53c6f65c6a75eb_2_467x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2db854a5676d7ea7ac1029c21b53c6f65c6a75eb_2_700x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2db854a5676d7ea7ac1029c21b53c6f65c6a75eb.jpeg 2x" data-dominant-color="767B97"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2026-01-30 um 22.35.43</span><span class="informations">910×974 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2026-01-30 21:48 UTC)

<aside class="quote no-group" data-username="md.walten" data-post="3" data-topic="45999">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a4c791/48.png" class="avatar"> md.walten:</div>
<blockquote>
<p>astmodel along, but I do not find “enable deformable registration” in the module (see attachment). I use slicer 5.10.</p>
</blockquote>
</aside>
<p>Sorry I should have specified. You need to use the current preview, it is a new feature being tested, so it is not in the stable.</p>

---

## Post #5 by @md.walten (2026-02-02 20:18 UTC)

<p>Thanks for the tip, i found it!  but the fastmodelalignement with deformation did not the best job, and the new model looks quiet deformed and not identical to the target model.. at the moment the best way was igt similarity followed by alpaca, but i am not sure if this is methodological correct for future scientific publication in a medical journal..</p>

---

## Post #6 by @muratmaga (2026-02-02 21:53 UTC)

<aside class="quote no-group" data-username="md.walten" data-post="5" data-topic="45999">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a4c791/48.png" class="avatar"> md.walten:</div>
<blockquote>
<p>gt similarity followed by alpaca</p>
</blockquote>
</aside>
<p>Interesting, FastModelAlign, (including deformable registeration) uses the same library as ALPACA. So it is surprising you get different results. Did you do its rigid registration before hand?</p>

---

## Post #7 by @md.walten (2026-02-03 21:07 UTC)

<p>You are right, I did not do rigid registration first.. So now I did a registration with option of scaling and rigid and then I did another registration only with deformable registration and I think the result looks like I had in my mind. I attached the two models and when they are overlapped.</p>
<p>I hope the reviewer will be okay with this technique <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=15" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20">  I will write the methods sth. like that:</p>
<p>“Surface models were registered using the FastModelAlign module in 3D Slicer (v5.11.0 preview). After point-cloud subsampling, global scaling and rigid alignment were performed. Non-rigid registration was subsequently applied using a CPD-based deformation framework, and the resulting deformation field was interpolated onto the original surface mesh for downstream analyses.”</p>
<p>What do you think?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/813d849b8072f687e1d565f73298e5add04d043a.jpeg" data-download-href="/uploads/short-url/irjovSzGt9O2bgF2QOes0Ty53l0.jpeg?dl=1" title="Bildschirmfoto 2026-02-03 um 21.53.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813d849b8072f687e1d565f73298e5add04d043a_2_690x364.jpeg" alt="Bildschirmfoto 2026-02-03 um 21.53.23" data-base62-sha1="irjovSzGt9O2bgF2QOes0Ty53l0" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813d849b8072f687e1d565f73298e5add04d043a_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813d849b8072f687e1d565f73298e5add04d043a_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813d849b8072f687e1d565f73298e5add04d043a_2_1380x728.jpeg 2x" data-dominant-color="A9A9B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2026-02-03 um 21.53.23</span><span class="informations">1808×956 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e838b324e7da58073f788209add5c509f30e96f6.jpeg" data-download-href="/uploads/short-url/x8kfCaRL6qMshAScnY4V5G9dTXE.jpeg?dl=1" title="Bildschirmfoto 2026-02-03 um 21.50.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e838b324e7da58073f788209add5c509f30e96f6_2_499x499.jpeg" alt="Bildschirmfoto 2026-02-03 um 21.50.27" data-base62-sha1="x8kfCaRL6qMshAScnY4V5G9dTXE" width="499" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e838b324e7da58073f788209add5c509f30e96f6_2_499x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e838b324e7da58073f788209add5c509f30e96f6_2_748x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e838b324e7da58073f788209add5c509f30e96f6_2_998x998.jpeg 2x" data-dominant-color="AAAAB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2026-02-03 um 21.50.27</span><span class="informations">1420×1420 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @muratmaga (2026-02-03 22:52 UTC)

<p>Your description is accurate and sufficient, but things  depends on what you are trying to achieve and what reviewers want to see.</p>

---
