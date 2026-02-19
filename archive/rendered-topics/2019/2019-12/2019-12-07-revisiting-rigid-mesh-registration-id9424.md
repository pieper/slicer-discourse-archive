---
topic_id: 9424
title: "Revisiting Rigid Mesh Registration"
date: 2019-12-07
url: https://discourse.slicer.org/t/9424
---

# Revisiting Rigid Mesh Registration

**Topic ID**: 9424
**Date**: 2019-12-07
**URL**: https://discourse.slicer.org/t/revisiting-rigid-mesh-registration/9424

---

## Post #1 by @manjula (2019-12-07 13:43 UTC)

<p>I first posted the problem few months back and Prof: Lassoan help me with it. Now i have had time to read about this topic and play around I would like to have a better understanding of the problem as i am not 100% happy with the results that i am getting with CMF surface registraion module and IGT fiducial registration wizard.  i am no mathematician or programmer and many parts of this will be copy pasted from other published work whici i read.</p>
<p><strong>Original Problem :</strong> We have a STL files from surface scans of bone from preop and post op with changes. We have initially put landmarks on the bone.</p>
<p>I have attached the sample data from our original scan. Blue is the pre op and the yellow is the post op.<br>
We need to align the two meshes perfectly so we can see the difference of bone volume. (model to model distance and shape population viewer.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d81e83981f21b8f597e0defc91364f20bcc941df.jpeg" data-download-href="/uploads/short-url/uPSvB4VptJtEGygBVUxgikjljoX.jpeg?dl=1" title="Screenshot from 2019-12-05 10-44-19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d81e83981f21b8f597e0defc91364f20bcc941df_2_690x431.jpeg" alt="Screenshot from 2019-12-05 10-44-19" data-base62-sha1="uPSvB4VptJtEGygBVUxgikjljoX" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d81e83981f21b8f597e0defc91364f20bcc941df_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d81e83981f21b8f597e0defc91364f20bcc941df_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d81e83981f21b8f597e0defc91364f20bcc941df_2_1380x862.jpeg 2x" data-dominant-color="ADBDCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-05 10-44-19</span><span class="informations">1920×1200 640 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>As i understand mathematical problem</strong></p>
<p>Given the coordinates of a set of points measured in two Cartesian coordinate systems (left, right) find the rigid transformation, T, between the two systems so that for corresponding points Pr , Pl we have:<br>
Pr = T(Pl )</p>
<p>From what i read on this,</p>
<ol>
<li>
<p>Pairing between points is <strong>known</strong> →  closed form <strong>(analytic) solutions.</strong></p>
</li>
<li>
<p>Pairing between points is <strong>unknown</strong>, → <strong>iterative solutions</strong> (require initialization and only guarantee  convergence to local optimum).</p>
</li>
</ol>
<p>And the advantages and disadvantages of the each method are,</p>
<p><strong>Analytic solution</strong></p>
<ul>
<li>requires pairing</li>
<li>sensitive to outliers</li>
<li>guarantees optimality</li>
<li>assumes noise is isotropic and IID (~N(0,))</li>
</ul>
<p><strong>Iterative solution</strong></p>
<ul>
<li>does not require a known pairing</li>
<li>sensitive to outliers</li>
<li>does not guarantee optimality</li>
<li>assumes noise is isotropic and IID (~N(0,))</li>
<li>requires initialization</li>
<li>requires use of spatial data structures to achieve reasonable running times on a reasonably large data set.</li>
</ul>
<p><strong>My Question 01</strong></p>
<p>CMF surface registration falls under ICP right ?</p>
<p><strong>My Question 02</strong></p>
<p>IGT Fiducial registration wizard → Is it ICP or Analytic solution ??? or a hybird ???</p>
<p><strong>My Experiment</strong></p>
<p>I made 3 stl models with Blender.<br>
Red and Green models are exact duplicates but with two locations. (2 origins)</p>
<p>Yellow models is also a exact duplicate but i distorted one part of the mesh and with as you can see different origin.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a91891e22c719b7e00cb5f5383fab98f99d7c90.png" data-download-href="/uploads/short-url/aDF8LFmlJ3ddEYxbw0eXwVyfYLS.png?dl=1" title="3 STL models" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a91891e22c719b7e00cb5f5383fab98f99d7c90_2_690x456.png" alt="3 STL models" data-base62-sha1="aDF8LFmlJ3ddEYxbw0eXwVyfYLS" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a91891e22c719b7e00cb5f5383fab98f99d7c90_2_690x456.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a91891e22c719b7e00cb5f5383fab98f99d7c90_2_1035x684.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a91891e22c719b7e00cb5f5383fab98f99d7c90.png 2x" data-dominant-color="9799BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3 STL models</span><span class="informations">1300×860 26.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I use CMF registriaon of Red and Green models. And the results are excellent.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1343ec8792217efa6636bcba4258601272f9ba9f.png" alt="ExactModelsSuperimposed" data-base62-sha1="2KqB5VBCHkQISBn141FypZN2erZ" width="514" height="425"></p>
<p>However when i use it to align the distorted model (yellow) it gives very very bad results. ( with max iterations 10000 and max landmarks 4000 )</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7eb6b261b898817d19c43df35e13550e2a235d49.png" data-download-href="/uploads/short-url/i4XApRrNwGxJtXAIJHEGhlxbanT.png?dl=1" title="CMFSurfaceRegistraopm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7eb6b261b898817d19c43df35e13550e2a235d49_2_690x456.png" alt="CMFSurfaceRegistraopm" data-base62-sha1="i4XApRrNwGxJtXAIJHEGhlxbanT" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7eb6b261b898817d19c43df35e13550e2a235d49_2_690x456.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7eb6b261b898817d19c43df35e13550e2a235d49_2_1035x684.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7eb6b261b898817d19c43df35e13550e2a235d49.png 2x" data-dominant-color="9D99C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CMFSurfaceRegistraopm</span><span class="informations">1300×860 40 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also i used IGT Fiducial registration with 4 landmarks and the results were not good but better than CMF registration. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/752f545ad2ad9dd3552319a8b60a35de3bd90502.png" data-download-href="/uploads/short-url/gIFgyxW6wgokZy1tB7xLCHLfACC.png?dl=1" title="IGT-Transformes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/752f545ad2ad9dd3552319a8b60a35de3bd90502_2_690x457.png" alt="IGT-Transformes" data-base62-sha1="gIFgyxW6wgokZy1tB7xLCHLfACC" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/752f545ad2ad9dd3552319a8b60a35de3bd90502_2_690x457.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/752f545ad2ad9dd3552319a8b60a35de3bd90502_2_1035x685.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/752f545ad2ad9dd3552319a8b60a35de3bd90502.png 2x" data-dominant-color="A198B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IGT-Transformes</span><span class="informations">1296×860 38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then i used the cloud compare on the same and even with the default settings it gives very good results.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed2d3ab6361b7d8df9fd3512c68630e71bd3ed02.png" data-download-href="/uploads/short-url/xQa3XH5SBpBHISRFwc49YH47UFc.png?dl=1" title="CloudCompareResults" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed2d3ab6361b7d8df9fd3512c68630e71bd3ed02_2_690x388.png" alt="CloudCompareResults" data-base62-sha1="xQa3XH5SBpBHISRFwc49YH47UFc" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed2d3ab6361b7d8df9fd3512c68630e71bd3ed02_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed2d3ab6361b7d8df9fd3512c68630e71bd3ed02_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed2d3ab6361b7d8df9fd3512c68630e71bd3ed02_2_1380x776.png 2x" data-dominant-color="66878A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CloudCompareResults</span><span class="informations">1920×1080 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So <strong>my question 3</strong></p>
<p>Why is 3D slicer ICP method in CMF registration module gives inferior results to cloudcompare ?</p>
<p>For my original study i did registration with IGT module with manual landmarks and the results were good as evident by the colour map.  we can see exact superimposition on the landmarks we fixed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/0697525d719ad73f897ab79e9de229de7e320a00.jpeg" data-download-href="/uploads/short-url/Wj4lF9xPwIIgMcMEbTd2ejOAY8.jpeg?dl=1" title="Screenshot from 2019-12-05 12-29-36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0697525d719ad73f897ab79e9de229de7e320a00_2_690x431.jpeg" alt="Screenshot from 2019-12-05 12-29-36" data-base62-sha1="Wj4lF9xPwIIgMcMEbTd2ejOAY8" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0697525d719ad73f897ab79e9de229de7e320a00_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0697525d719ad73f897ab79e9de229de7e320a00_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0697525d719ad73f897ab79e9de229de7e320a00_2_1380x862.jpeg 2x" data-dominant-color="93949F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-05 12-29-36</span><span class="informations">1920×1200 345 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But i could get the same results with the cloud compare too in which alignment was as above completely automated. ( I think with ICP registration - cloud compare fine alignment)</p>
<p>So <strong>Question 04</strong></p>
<p>Where is the problem with CMF registration module in comparison to cloud compare ? Why is it failing ? I edited the source file of CMF slicer module and tried it with 10000 landmarks and the results were the same albeit it was lot of computer power for my laptop - had to wait a long time !.</p>
<p><strong>Question 05</strong></p>
<p>In IGT Fiducial registration wizard is there any part which is automatic or done by a algorithm ? or is it s just transform or move the mesh landmarks we select on to each other without any kind of matching ?</p>
<p><strong>Question 06</strong><br>
Is there a remedy to improve this ? As  i prefer a fully automated system (without selecting landmarks) to align the models with better precision.</p>

---

## Post #2 by @lassoan (2019-12-07 15:08 UTC)

<p>Typically, you align surfaces approximately first (if they are not already aligned, either manually translating/rotating or using landmark registration), then perform surface-based registration (masking out or removing regions that should be ignored).</p>
<p>Landmark registration result can be solved without iterations and it gives the global optimum.</p>
<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="9424">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>CMF surface registration falls under ICP right ?</p>
</blockquote>
</aside>
<p>I haven’t used this module but it seems that it can do both landmark registration and surface registration (using ICP).</p>
<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="9424">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>IGT Fiducial registration wizard → Is it ICP or Analytic solution ??? or a hybird ???</p>
</blockquote>
</aside>
<p>Fiducial registration wizard performs landmark registration (non-iterative, global optimum solution). You can enable automatic point matching up to 7 landmark points.</p>
<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="9424">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Why is 3D slicer ICP method in CMF registration module gives inferior results to cloudcompare ?</p>
</blockquote>
</aside>
<p>You can get accurate alignment reliably:</p>
<ul>
<li>remove those regions from the moving surface that you want to be ignored (regions affected by the medical procedure)</li>
<li>perform initial alignment if surfaces are not aligned already; if orientation and region of interest approximately matches then automatic centroid-based alignment may be enough</li>
<li>register using ICP; it is important to choose the clipped surface as moving and the full surface as fixed surface</li>
</ul>

---

## Post #3 by @manjula (2019-12-07 15:19 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Many thanks again for taking the time.</p>
<p>I have a question  that came out of this ? I don’t know it is valid or just a stupid question.</p>
<p>Is ICP better than land mark registration ? or which one is superior or are they the same. ?</p>
<p>2nd. How do i remove the region that has changed before ICP registration and then add it back to the new location to calculate model to model distance ?  i can think of how to do this in dicom data with masking but these are stl files. How to do I do that ???</p>
<p>Thank you.</p>

---

## Post #4 by @lassoan (2019-12-08 14:42 UTC)

<p>Are there any more error details shown in the application log?</p>

---

## Post #5 by @manjula (2019-12-08 15:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>application log?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>These are the results I get with the cloud compare fine registration with RMS. As you can see when i look at the model to model distance and view it in shape population viewer with the same setting… our land marks show almost exact matches ( Green ) in the viewer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6032afd17d99626c43152c7376cc69a11673b5e9.png" data-download-href="/uploads/short-url/dJ0qQSmPcSRQ57o8qPCSm90nWm5.png?dl=1" title="Screenshot from 2019-12-08 13-16-08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6032afd17d99626c43152c7376cc69a11673b5e9_2_690x388.png" alt="Screenshot from 2019-12-08 13-16-08" data-base62-sha1="dJ0qQSmPcSRQ57o8qPCSm90nWm5" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6032afd17d99626c43152c7376cc69a11673b5e9_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6032afd17d99626c43152c7376cc69a11673b5e9_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6032afd17d99626c43152c7376cc69a11673b5e9_2_1380x776.png 2x" data-dominant-color="878F83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 13-16-08</span><span class="informations">1920×1080 483 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42bdc7101eb0a609528bd60a6c9461dcc1841c9e.png" data-download-href="/uploads/short-url/9wq6Nx92YFzxVh6MndqAZznlMdg.png?dl=1" title="Screenshot from 2019-12-08 13-15-52" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42bdc7101eb0a609528bd60a6c9461dcc1841c9e_2_690x388.png" alt="Screenshot from 2019-12-08 13-15-52" data-base62-sha1="9wq6Nx92YFzxVh6MndqAZznlMdg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42bdc7101eb0a609528bd60a6c9461dcc1841c9e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42bdc7101eb0a609528bd60a6c9461dcc1841c9e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42bdc7101eb0a609528bd60a6c9461dcc1841c9e_2_1380x776.png 2x" data-dominant-color="878F83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 13-15-52</span><span class="informations">1920×1080 491 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae13521e98b27443c7f8f6d26d1d439d2ebe8bc9.png" data-download-href="/uploads/short-url/oPWtpJCKn4LmyqmhdQJUVV1xdXz.png?dl=1" title="Screenshot from 2019-12-08 13-17-27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae13521e98b27443c7f8f6d26d1d439d2ebe8bc9_2_690x388.png" alt="Screenshot from 2019-12-08 13-17-27" data-base62-sha1="oPWtpJCKn4LmyqmhdQJUVV1xdXz" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae13521e98b27443c7f8f6d26d1d439d2ebe8bc9_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae13521e98b27443c7f8f6d26d1d439d2ebe8bc9_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae13521e98b27443c7f8f6d26d1d439d2ebe8bc9_2_1380x776.png 2x" data-dominant-color="636765"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 13-17-27</span><span class="informations">1920×1080 403 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4ba7e585f5ef56784afc255624a62e0a86899099.jpeg" data-download-href="/uploads/short-url/aNhwFVKze00WvU5cp7SfXz13xlD.jpeg?dl=1" title="Screenshot from 2019-12-08 13-22-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ba7e585f5ef56784afc255624a62e0a86899099_2_690x388.jpeg" alt="Screenshot from 2019-12-08 13-22-16" data-base62-sha1="aNhwFVKze00WvU5cp7SfXz13xlD" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ba7e585f5ef56784afc255624a62e0a86899099_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ba7e585f5ef56784afc255624a62e0a86899099_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ba7e585f5ef56784afc255624a62e0a86899099_2_1380x776.jpeg 2x" data-dominant-color="736E82"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 13-22-16</span><span class="informations">1920×1080 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I get almost same resutls with the cloud compare iteration method also. Again very good match on the landmarks we put in surgically.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cb0b07f8d90c83cc49ef26d419cf9081d2a4290.png" data-download-href="/uploads/short-url/hN3Le5epyknwLZGiiWK702mcnVC.png?dl=1" title="Screenshot from 2019-12-08 13-28-20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7cb0b07f8d90c83cc49ef26d419cf9081d2a4290_2_690x388.png" alt="Screenshot from 2019-12-08 13-28-20" data-base62-sha1="hN3Le5epyknwLZGiiWK702mcnVC" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7cb0b07f8d90c83cc49ef26d419cf9081d2a4290_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7cb0b07f8d90c83cc49ef26d419cf9081d2a4290_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7cb0b07f8d90c83cc49ef26d419cf9081d2a4290_2_1380x776.png 2x" data-dominant-color="909591"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 13-28-20</span><span class="informations">1920×1080 416 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f8e1c646f18e7bb0a9ce14627bf0a9b1e1fd3fa.png" data-download-href="/uploads/short-url/fURtalP1rySkW4iNWnGueIQD8Ey.png?dl=1" title="Screenshot from 2019-12-08 13-25-09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f8e1c646f18e7bb0a9ce14627bf0a9b1e1fd3fa_2_690x388.png" alt="Screenshot from 2019-12-08 13-25-09" data-base62-sha1="fURtalP1rySkW4iNWnGueIQD8Ey" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f8e1c646f18e7bb0a9ce14627bf0a9b1e1fd3fa_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f8e1c646f18e7bb0a9ce14627bf0a9b1e1fd3fa_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f8e1c646f18e7bb0a9ce14627bf0a9b1e1fd3fa_2_1380x776.png 2x" data-dominant-color="636765"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 13-25-09</span><span class="informations">1920×1080 405 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edfbb8109f67a3436ac8406929ea77daf2f38389.jpeg" data-download-href="/uploads/short-url/xXisTcLsgVzoD1NLtGPjLxfdzCx.jpeg?dl=1" title="Screenshot from 2019-12-08 13-27-29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edfbb8109f67a3436ac8406929ea77daf2f38389_2_690x388.jpeg" alt="Screenshot from 2019-12-08 13-27-29" data-base62-sha1="xXisTcLsgVzoD1NLtGPjLxfdzCx" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edfbb8109f67a3436ac8406929ea77daf2f38389_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edfbb8109f67a3436ac8406929ea77daf2f38389_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edfbb8109f67a3436ac8406929ea77daf2f38389_2_1380x776.jpeg 2x" data-dominant-color="726D83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 13-27-29</span><span class="informations">1920×1080 345 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However when i used the CMF surface registration results are like this, with not very good registration.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18888b8ec90f26173464b5c042a9e3b57e06f6cf.jpeg" data-download-href="/uploads/short-url/3v20mKUBwtKUh1sEw5GgaM29xwP.jpeg?dl=1" title="Screenshot from 2019-12-08 13-37-12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18888b8ec90f26173464b5c042a9e3b57e06f6cf_2_690x388.jpeg" alt="Screenshot from 2019-12-08 13-37-12" data-base62-sha1="3v20mKUBwtKUh1sEw5GgaM29xwP" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18888b8ec90f26173464b5c042a9e3b57e06f6cf_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18888b8ec90f26173464b5c042a9e3b57e06f6cf_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18888b8ec90f26173464b5c042a9e3b57e06f6cf_2_1380x776.jpeg 2x" data-dominant-color="766A83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 13-37-12</span><span class="informations">1920×1080 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I managed to get good results with IGT fiducial registration wizard but it was after lot of playing around with fiducial markers and changing ti manually until i could get very good alignment. This took lot of time to chaging the location of fiducials until it gave this result.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/166452ded916843979a1c21b17833ef6c42b2ffc.jpeg" data-download-href="/uploads/short-url/3c5rHVZc3Ukh9MxwjoSj8qSUlME.jpeg?dl=1" title="Screenshot from 2019-12-08 16-16-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/166452ded916843979a1c21b17833ef6c42b2ffc_2_690x388.jpeg" alt="Screenshot from 2019-12-08 16-16-46" data-base62-sha1="3c5rHVZc3Ukh9MxwjoSj8qSUlME" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/166452ded916843979a1c21b17833ef6c42b2ffc_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/166452ded916843979a1c21b17833ef6c42b2ffc_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/166452ded916843979a1c21b17833ef6c42b2ffc_2_1380x776.jpeg 2x" data-dominant-color="83808E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 16-16-46</span><span class="informations">1920×1080 373 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>**So my major Problem is ** why is cloud compare fine alignment gives better results in comparison to CMF surface registration ? Because as i read on both the module they use the ICP algorithms and why should it then give different results  ?</p>
<p>Today i installed nightly version because i wanted to try it with CMFreg ROI method since i did not knew how to do only to select the region of interest as you suggested in a stl file and  as for some reason in the stable version in my computer ROI registration was not marking the regions of interest for some reason.  So i tried with nightly version and it worked and gave excellent results with ease compared to IGT registration. But still cloud compares registration is fully automated as i do not need to select any points.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c66a44c196eaffdafe1bf370a2e16442937fca5a.png" data-download-href="/uploads/short-url/sjgdy1DBMJwGGD3i7LL98pnXAEy.png?dl=1" title="Screenshot from 2019-12-08 16-40-13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c66a44c196eaffdafe1bf370a2e16442937fca5a_2_690x388.png" alt="Screenshot from 2019-12-08 16-40-13" data-base62-sha1="sjgdy1DBMJwGGD3i7LL98pnXAEy" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c66a44c196eaffdafe1bf370a2e16442937fca5a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c66a44c196eaffdafe1bf370a2e16442937fca5a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c66a44c196eaffdafe1bf370a2e16442937fca5a_2_1380x776.png 2x" data-dominant-color="68777C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 16-40-13</span><span class="informations">1920×1080 336 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d98c7787af8ff4db3f195090acea0ec8de6c2bac.jpeg" data-download-href="/uploads/short-url/v2wyISHOUHOr1BqeosdISzKeVdi.jpeg?dl=1" title="Screenshot from 2019-12-08 16-40-06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d98c7787af8ff4db3f195090acea0ec8de6c2bac_2_690x388.jpeg" alt="Screenshot from 2019-12-08 16-40-06" data-base62-sha1="v2wyISHOUHOr1BqeosdISzKeVdi" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d98c7787af8ff4db3f195090acea0ec8de6c2bac_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d98c7787af8ff4db3f195090acea0ec8de6c2bac_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d98c7787af8ff4db3f195090acea0ec8de6c2bac_2_1380x776.jpeg 2x" data-dominant-color="736D83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2019-12-08 16-40-06</span><span class="informations">1920×1080 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So i am out of interest and also because almost all the research that we have planned or are currently been conducted involves registration i am very much interested in learning about this and for publication purposes i think it is much convenient to stick to one software (3D slicer) to do the registration and the model to model distance and colour mapping.</p>

---

## Post #6 by @lassoan (2019-12-09 05:15 UTC)

<aside class="quote no-group" data-username="manjula" data-post="5" data-topic="9424">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>why is cloud compare fine alignment gives better results in comparison to CMF surface registration</p>
</blockquote>
</aside>
<p>Maybe there is some heuristics in CloudCompare’s registration algorithms that make the registration ignore the modified parts of the surface.</p>
<p>Instead of relying on heuristics, it would be safer to explicitly restrict registration to only take into account neighborhood of landmarks. You can write a short Python script for this:</p>
<ul>
<li>compute distance from landmark points on the “moving” mesh: create a polydata from the landmark points and use that in <a href="https://vtk.org/doc/nightly/html/classvtkDistancePolyDataFilter.html">vtkDistancePolyDataFilter</a></li>
<li>clip “moving” mesh to only contain regions that are near landmark points (maximum distance should be approximate size of the landmark object, or maybe a bit larger) using <a href="https://vtk.org/doc/nightly/html/classvtkThreshold.html">vtkThreshold</a></li>
<li>register the two meshes approximately using landmark transform</li>
<li>refine registration by registering the clipped “moving” mesh to the “fixed” mesh (the other mesh, without any clipping) using surface registration</li>
</ul>
<p>Maybe CMFreg already supports something like this, but if not, then it should be quite easy to add there. Or, such a registration module could be added to SlicerMorph extension, too.</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> <a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---

## Post #7 by @manjula (2019-12-09 08:33 UTC)

<p>Dear Prof <a class="mention" href="/u/lassoan">@lassoan</a><br>
I started learning python but at the moment not capable of writing that script. But i am willing to try it if someone can help me with it when your time permits it.</p>
<p>we are happy with the results we get with the CMFreg ROI registration and we are going to analyse the data with it for now. But if we can get the surface registration to work with the python code i am willing to learn it.</p>

---

## Post #8 by @mau_igna_06 (2021-10-14 14:53 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>. I am thinking about developing this improved surface registration you were talking about. Although I would need a little bit more info.</p>
<p>A question, would the improved version work as well as this one?</p><div class="youtube-onebox lazy-video-container" data-video-id="WxaOFZPt6Ws" data-video-title="ICP in Blender Example" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=WxaOFZPt6Ws" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/WxaOFZPt6Ws/maxresdefault.jpg" title="ICP in Blender Example" width="" height="">
  </a>
</div>

<p>Would some kind of paint selection of cells of the mesh be possible using the segment editor or using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#select-cells-of-a-model-using-markups-fiducial-points" rel="noopener nofollow ugc">this script</a> as base? Would that improve usability?</p>
<p>This blender’s ICP is currently used in blender to plan deformity correction surgeries using the normal bone (contralateral) to guide the aligment of the to-be-aligned deformed bone pieces after the closing/opening wedge osteotomy. But they lack access to the ICP transform that results from the algorithm in blender. So they can’t plan kirchner wires on the corrected bone segments and transform them to the deformed original bone to create surgical guides for cut and aligment.</p>
<p>Related relevant post: <a href="https://discourse.slicer.org/t/robust-icp-alignment-tool/16107" class="inline-onebox">Robust ICP alignment tool</a></p>

---

## Post #9 by @mau_igna_06 (2021-10-17 20:00 UTC)

<p>Meanwhile I got the faces selection working:<br>
(copy it to a code editor for better display)</p>
<pre><code class="lang-auto">fiducialList = getNode('MarkupsFiducial')
appendFilter = vtk.vtkAppendPolyData()
for i in range(fiducialList.GetNumberOfControlPoints()):
    position = [0,0,0]
    fiducialList.GetNthControlPointPosition(i,position)
    sphere = vtk.vtkSphereSource()
    sphere.SetRadius(0.1)
    sphere.SetCenter(position)
    sphere.SetThetaResolution(5)
    sphere.SetPhiResolution(5)
    sphere.Update()
    appendFilter.AddInputData(sphere.GetOutput())

appendFilter.Update()

myModel = getNode('deformed_Right_tibia')

distanceFilter = vtk.vtkDistancePolyDataFilter()
distanceFilter.SetInputData(0, myModel.GetPolyData())
distanceFilter.SetInputData(1, appendFilter.GetOutput())
distanceFilter.SignedDistanceOff()
distanceFilter.Update()

myModel.SetAndObservePolyData(distanceFilter.GetOutput())
#Turn on distance scalars on Models module's properties

"""
Creating a points-only polydata doesn't work
points = vtk.vtkPoints()
vertsCellArray = vtk.vtkCellArray()
appendFilter = vtk.vtkAppendPolyData()
for i in range(fiducialList.GetNumberOfControlPoints()):
    position = [0,0,0]
    fiducialList.GetNthControlPointPosition(i,position)
    pointId = points.InsertNextPoint(position)
    vertsCellArray.InsertNextCell(1)
    vertsCellArray.InsertCellPoint(pointId)

polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetVerts(vertsCellArray)
polydata.Modified()

myModel = getNode('deformed_Right_tibia')

distanceFilter = vtk.vtkDistancePolyDataFilter()
distanceFilter.SetInputData(0, myModel.GetPolyData())
distanceFilter.SetInputData(1, polydata)
distanceFilter.SignedDistanceOff()
distanceFilter.Update()


myModel.SetAndObservePolyData(distanceFilter.GetOutput())
"""

thresholdFilter = vtk.vtkThreshold()
thresholdFilter.SetInputData(distanceFilter.GetOutput())
maximumDistanceToPointsmm = 15
thresholdFilter.ThresholdBetween(0, maximumDistanceToPointsmm)
thresholdFilter.SetInputArrayToProcess(0, 0, 0,
    vtk.vtkDataObject.FIELD_ASSOCIATION_CELLS,
    "Distance")
#thresholdFilter.SetInputArrayToProcess(0, 0, 0,
#   vtk.vtkDataObject.
#    FIELD_ASSOCIATION_POINTS, "Distance")
thresholdFilter.Update()
geometryFilter = vtk.vtkGeometryFilter()
geometryFilter.SetInputData(thresholdFilter.GetOutput())
geometryFilter.Update()
myModel2 = getNode('deformed_Right_tibia Copy')
myModel2.SetAndObservePolyData(geometryFilter.GetOutput())
</code></pre>
<p>Faces need to be well-shaped for it to work well I think. Here is an example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7dc5711e4024bcd1aaf68082b25c0c8c78e815b0.jpeg" data-download-href="/uploads/short-url/hWCHsRwleX8vUvfc8vuD5Lo9oSA.jpeg?dl=1" title="facesSelection" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dc5711e4024bcd1aaf68082b25c0c8c78e815b0_2_690x411.jpeg" alt="facesSelection" data-base62-sha1="hWCHsRwleX8vUvfc8vuD5Lo9oSA" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dc5711e4024bcd1aaf68082b25c0c8c78e815b0_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7dc5711e4024bcd1aaf68082b25c0c8c78e815b0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7dc5711e4024bcd1aaf68082b25c0c8c78e815b0.jpeg 2x" data-dominant-color="9A98AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">facesSelection</span><span class="informations">1025×612 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2021-10-17 23:49 UTC)

<p>Thanks for the update, this looks nice. Could you turn this into a Dynamic modeler tool? It should be fairly straightforward to implement and would make the feature conveniently available to end users.</p>
<p>We can already use curves and planes to define regions on surfaces, but sometimes using points is easier and can be more robust (especially if you simply add all points within a certain radius instead of marching on the surface). We could also make the output cropping optional: the end result could be the cropped model; or the original model storing selection in point/cell scalars.</p>

---

## Post #11 by @mau_igna_06 (2021-10-18 18:39 UTC)

<blockquote>
<p>Thanks for the update, this looks nice. Could you turn this into a Dynamic modeler tool? It should be fairly straightforward to implement and would make the feature conveniently available to end users.</p>
</blockquote>
<p>I’m doing it. I have done a full Slicer build. I have my DynamicModeler changes in my fork of the SlicerSurfaceToolbox how do I make the built Slicer load my DynamicModeler changes. I guess I have to change a variable of the superbuild to point to my repository. Or how do I do to build my new code of the SlicerSurfaceToolbox?</p>
<blockquote>
<p>or the original model storing selection in point/cell scalars.</p>
</blockquote>
<p>This is done in a script, I have to implement it yet in the new SelectionTool class of the Dynamic Modeler.</p>
<p>This is the script to have selection scalars:</p>
<pre><code class="lang-auto">maximumDistancemm = 30
cellScalars = myModel.GetMesh().GetCellData()
distanceArray = cellScalars.GetArray("Distance")
selectionArray = vtk.vtkIntArray()
selectionArray.SetName("Selection")
selectionArray.SetNumberOfValues(myModel.GetMesh().GetNumberOfCells())
for i in range(myModel.GetMesh().GetNumberOfCells()):
    if distanceArray.GetTuple1(i) &lt; maximumDistancemm:
        selectionArray.SetTuple1(i,1)
    else:
        selectionArray.SetTuple1(i,0)

cellScalars.AddArray(selectionArray)

# Set up coloring by selection array
myModel.GetDisplayNode().SetActiveScalar("Selection", vtk.vtkAssignAttribute.CELL_DATA)
myModel.GetDisplayNode().SetAndObserveColorNodeID("vtkMRMLColorTableNodeWarm1")
myModel.GetDisplayNode().SetScalarVisibility(True)
</code></pre>
<p>The script would be faster to execute if the selection-fiducials created just points polydata instead of small spheres. <a class="mention" href="/u/lassoan">@lassoan</a>  you can check the commented part of the first script I posted (more above this comment) to see if you can find out why this faster approach doesn’t work (there are no Distance arrays created for the model).</p>

---

## Post #12 by @mau_igna_06 (2021-10-19 11:01 UTC)

<p>Building Slicer (without changing the source code) with the VisualStudio GUI fails and gives like 500 errors, building it from the command line succeeds. Although I don’t like it building from the command line because it takes very long, not as much as a clean build, but like 70% of the time. Building from the GUI usually takes a lot once, but then it only rebuilds the changed files and it is a lot faster.</p>
<p>Now I changed ‘SuperBuild.cmake’ to point to my forked repository of the surfaceToolbox and changed the commit_tag to the last commit of the selectionToolFeatureBranch. And I’m doing a clean build from the command line. I think it should work.</p>
<p>How can I make Slicer compile faster from the command line? Why there is not match in compiling results using the command line and using the GUI of Visual Studio? (I followed the build instructions for windows)</p>
<p>Here is my branch if you want to check it out: <a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/SelectionToolFeature" class="inline-onebox" rel="noopener nofollow ugc">GitHub - mauigna06/SlicerSurfaceToolbox at SelectionToolFeature</a></p>

---

## Post #13 by @lassoan (2021-10-20 06:02 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="11" data-topic="9424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I guess I have to change a variable of the superbuild to point to my repository</p>
</blockquote>
</aside>
<p>You can, but you don’t have to. You can make changes locally, test everything, and send a pull request to the <a href="https://github.com/Slicer/SlicerSurfaceToolbox/">SurfaceToolbox repository</a> to get your changes integrated into Slicer.</p>
<p>Instead of using vtkDistancePolyDataFilter, you can <a href="https://vtk.org/doc/nightly/html/classvtkPointLocator.html#af102b01d784984fdf14fb8bc17293157">get the list of points within a certain radius using a fast point locator</a>.</p>
<p>You could also add an option to add points based on geodesic distance (distance along the surface) using <a href="https://www.vtkjournal.org/browse/publication/891">these filters</a>.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="12" data-topic="9424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Building Slicer (without changing the source code) with the VisualStudio GUI fails and gives like 500 errors</p>
</blockquote>
</aside>
<p>You must set the build type (debug/release) to the same that you used when you configured your project using the command line.</p>

---

## Post #14 by @mau_igna_06 (2021-10-20 11:04 UTC)

<blockquote>
<p>Instead of using vtkDistancePolyDataFilter, you can <a href="https://vtk.org/doc/nightly/html/classvtkPointLocator.html#af102b01d784984fdf14fb8bc17293157" rel="noopener nofollow ugc">get the list of points within a certain radius using a fast point locator </a>.</p>
</blockquote>
<p>Here is the faster (a lot faster) script for selection using what you suggested:</p>
<pre><code class="lang-auto">
fiducialList = getNode('MarkupsFiducial_2')
myModel = getNode('normalBone')

modelPolydata = vtk.vtkPolyData()
modelPolydata.ShallowCopy(myModel.GetPolyData());

# Initialize the locator
pointTree = vtk.vtkPointLocator();
pointTree.SetDataSet(modelPolydata);
pointTree.BuildLocator();

selectionArray = vtk.vtkIntArray()
selectionArray.SetName("Selection")
selectionArray.SetNumberOfValues(modelPolydata.GetNumberOfPoints())
selectionArray.Fill(0)

maximumDistanceToPointsmm = 5

for i in range(fiducialList.GetNumberOfControlPoints()):
    position = [0,0,0]
    fiducialList.GetNthControlPointPosition(i,position)
    result = vtk.vtkIdList()
    pointTree.FindPointsWithinRadius(maximumDistanceToPointsmm, position,
                                    result);
    
    for j in range(result.GetNumberOfIds()):
        point_ind = result.GetId(j);
        selectionArray.SetTuple1(point_ind, 1);


pointScalars = modelPolydata.GetPointData()
pointScalars.AddArray(selectionArray)

thresholdFilter = vtk.vtkThreshold()
thresholdFilter.SetInputData(modelPolydata)
thresholdFilter.ThresholdBetween(0.9, 1.1)
thresholdFilter.SetInputArrayToProcess(0, 0, 0,
    vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS,
    "Selection")
thresholdFilter.Update()
geometryFilter = vtk.vtkGeometryFilter()
geometryFilter.SetInputData(thresholdFilter.GetOutput())
geometryFilter.Update()

selectedNormalBoneDistal = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode','selectedNormalBone')
selectedNormalBoneDistal.CreateDefaultDisplayNodes()
displayNode = selectedNormalBoneDistal.GetDisplayNode()
displayNode.SetColor(0,0,1)
selectedNormalBoneDistal.SetAndObservePolyData(geometryFilter.GetOutput())
</code></pre>
<p>If you think the script is okey, I’ll update the selectionToolBranch.</p>
<p>I could filter selected points a little more by checking if the normal of the inside-sphere points (given by the pointLocator) has less than 90 degress with the normal of pointNearestToTheFiducial. That would avoid selection though the surface when radius of the sphere is big I think. What do you think about this?</p>
<p>I could try to make the geodesic distance option. With the change above do you think it will still be needed? Do you know if the geodesic-distace algorithm execution is fast? (if it takes as long as vtkDistancePolyDataFilter, it may not be worth it, or does it?)</p>

---

## Post #15 by @lassoan (2021-10-21 04:04 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="14" data-topic="9424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I could filter selected points a little more by checking if the normal of the inside-sphere points (given by the pointLocator) has less than 90 degress with the normal of pointNearestToTheFiducial.</p>
</blockquote>
</aside>
<p>That usually does not work very well (normals can be noisy, so the edge can be very rough and it is also hard to find a good angle threshold), so we can leave it for now.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="14" data-topic="9424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I could try to make the geodesic distance option. With the change above do you think it will still be needed? Do you know if the geodesic-distace algorithm execution is fast? (if it takes as long as vtkDistancePolyDataFilter, it may not be worth it, or does it?)</p>
</blockquote>
</aside>
<p>The geodesic distance filter may be faster. The speed may depend on the maximum distance - for small distances the propagation should stop earlier.</p>

---

## Post #16 by @mau_igna_06 (2021-10-22 11:14 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>. I added the geodesicDistance algorithm to the SelectionTool of the dynamicModeler (you can checkout my <a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/SelectionToolFeature" rel="noopener nofollow ugc">branch</a>). The code should be 95% okey in theory but I wasn’t able to try it because I’m having trouble compiling Slicer. It fails from Visual Studio GUI with 2 errors. Now I’m trying to build from the command line. I don’t know if it will work out. It takes a lot of time.</p>
<p>Meanwhile I was trying to compile the example of Geodesics and I cannot make it work. These are my commands:</p>
<pre><code class="lang-auto">cd GeodesicsOnMeshesRelease
"C:\Program Files\CMake\bin\cmake.exe" -G "Visual Studio 16 2019" -A x64 -DVTK_DIR:PATH=C:\D\S4R\VTK-build ..\GeodesicsOnMeshes
"C:\Program Files\CMake\bin\cmake.exe" --build . --config Release
</code></pre>
<p>If fails with this log:</p>
<pre><code class="lang-auto">Microsoft (R) Build Engine versión 16.9.0+5e4b48a27 para .NET Framework
Copyright (C) Microsoft Corporation. Todos los derechos reservados.

  Checking Build System
  Building Custom Rule C:/Users/mau_i/Downloads/SourceCode3_GeodesicsOnMeshes/GeodesicsOnMeshes/FastMarching/CMakeLists
  .txt
  GW_Config.cpp
  GW_Face.cpp
  GW_FaceIterator.cpp
  GW_Mesh.cpp
  GW_SmartCounter.cpp
  GW_Vertex.cpp
  GW_VertexIterator.cpp
  GW_GeodesicFace.cpp
  GW_GeodesicMesh.cpp
  GW_GeodesicPath.cpp
  GW_GeodesicPoint.cpp
  GW_GeodesicVertex.cpp
  GW_TriangularInterpolation_Linear.cpp
  GW_TriangularInterpolation_Quadratic.cpp
  GW_TriangularInterpolation_Cubic.cpp
  Generando código...
  MeshGeodesics.vcxproj -&gt; C:\Users\mau_i\Downloads\SourceCode3_GeodesicsOnMeshes\GeodesicsOnMeshesRelease\bin\Release\
  MeshGeodesics.lib
  Building Custom Rule C:/Users/mau_i/Downloads/SourceCode3_GeodesicsOnMeshes/GeodesicsOnMeshes/Source/CMakeLists.txt
  vtkPolyDataGeodesicDistance.cxx
C:\Users\mau_i\Downloads\SourceCode3_GeodesicsOnMeshes\GeodesicsOnMeshes\Source\vtkPolyDataGeodesicDistance.h(16,10): f
atal error C1083: No se puede abrir el archivo incluir: 'vtkPolyDataAlgorithm.h': No such file or directory [C:\Users\m
au_i\Downloads\SourceCode3_GeodesicsOnMeshes\GeodesicsOnMeshesRelease\Source\vtkMeshGeodesics.vcxproj]
  vtkFastMarchingGeodesicDistance.cxx
C:\Users\mau_i\Downloads\SourceCode3_GeodesicsOnMeshes\GeodesicsOnMeshes\Source\vtkPolyDataGeodesicDistance.h(16,10): f
atal error C1083: No se puede abrir el archivo incluir: 'vtkPolyDataAlgorithm.h': No such file or directory [C:\Users\m
au_i\Downloads\SourceCode3_GeodesicsOnMeshes\GeodesicsOnMeshesRelease\Source\vtkMeshGeodesics.vcxproj]
  vtkFastMarchingGeodesicPath.cxx
C:\Users\mau_i\Downloads\SourceCode3_GeodesicsOnMeshes\GeodesicsOnMeshes\Source\vtkFastMarchingGeodesicPath.h(40,10): f
atal error C1083: No se puede abrir el archivo incluir: 'vtkGeodesicPath.h': No such file or directory [C:\Users\mau_i\
Downloads\SourceCode3_GeodesicsOnMeshes\GeodesicsOnMeshesRelease\Source\vtkMeshGeodesics.vcxproj]
  vtkPolygonalSurfaceContourLineInterpolator2.cxx
C:\Users\mau_i\Downloads\SourceCode3_GeodesicsOnMeshes\GeodesicsOnMeshes\Source\vtkPolygonalSurfaceContourLineInterpola
tor2.h(48,10): fatal error C1083: No se puede abrir el archivo incluir: 'vtkPolyDataContourLineInterpolator.h': No such
 file or directory [C:\Users\mau_i\Downloads\SourceCode3_GeodesicsOnMeshes\GeodesicsOnMeshesRelease\Source\vtkMeshGeode
sics.vcxproj]
  Generando código...
</code></pre>
<p>Do you have any suggestions of how to make it work? (Maybe the error happens because I’m trying to build using VTK-build and I don’t know if it finished compiling in the Slicer superbuild, commandline is processing)</p>
<p>Also I don’t know what I have to do to make the Geodesics library compile inside the dynamicModeler (or how to make vtkFastMarchingGeodesicDistance findable for my SelectionTool)</p>

---

## Post #17 by @mau_igna_06 (2021-10-22 19:21 UTC)

<p>I could compile Slicer well from the command line. So now the next thing to do is to compile the new Dynamic Modeler and test it. But I don’t know how to add the vtkFastMarchingGeodesicDistance to the DynamicModeler logic, it has a folder full of dependencies. And I don’t know how to configure the CMake.</p>
<p>I tried to follow how <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/CombineModels/Logic" rel="noopener nofollow ugc">Combine Models</a> does it in its CMakeLists.txt but the Geodesics have a lot more dependencies.</p>
<p>I would like the geodesics filter to be available from the python interpreter also.</p>

---

## Post #18 by @mau_igna_06 (2021-10-26 18:41 UTC)

<p>Ok. I think I fixed most of the bugs. There is only one left:</p>
<pre><code class="lang-auto">Gravedad	Código	Descripción	Proyecto	Archivo	Línea	Estado suprimido
Error	LNK1181	no se puede abrir el archivo de entrada 'FastMarching.lib'	vtkSlicerDynamicModelerModuleLogic	C:\D\S4R\Slicer-build\E\SurfaceToolbox\DynamicModeler\Logic\LINK	1	

</code></pre>
<p><a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/SelectionToolFeature" rel="noopener nofollow ugc">Link to the code</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> maybe you can help with this</p>

---

## Post #19 by @mau_igna_06 (2021-10-27 13:24 UTC)

<p>All working. I submitted a pull-request <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/46" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #20 by @Ruida_Cheng (2025-03-07 08:47 UTC)

<p>For Rigid Mesh Registration, you have the code below. The deformed_Right_tibia, deformed_Right_tibia Copy,<br>
what’s the 3D model type, i.e., .ply file? I am new to 3D Slicer. For “MarkupFiducial”, how do I invoke it in 3D Slicer? Thanks.</p>
<p>fiducialList = getNode(‘MarkupsFiducial’)<br>
appendFilter = vtk.vtkAppendPolyData()<br>
for i in range(fiducialList.GetNumberOfControlPoints()):<br>
position = [0,0,0]<br>
fiducialList.GetNthControlPointPosition(i,position)<br>
sphere = vtk.vtkSphereSource()<br>
sphere.SetRadius(0.1)<br>
sphere.SetCenter(position)<br>
sphere.SetThetaResolution(5)<br>
sphere.SetPhiResolution(5)<br>
sphere.Update()<br>
appendFilter.AddInputData(sphere.GetOutput())</p>
<p>appendFilter.Update()</p>
<p>myModel = getNode(‘deformed_Right_tibia’)</p>
<p>distanceFilter = vtk.vtkDistancePolyDataFilter()<br>
distanceFilter.SetInputData(0, myModel.GetPolyData())<br>
distanceFilter.SetInputData(1, appendFilter.GetOutput())<br>
distanceFilter.SignedDistanceOff()<br>
distanceFilter.Update()</p>
<p>myModel.SetAndObservePolyData(distanceFilter.GetOutput())<br>
<a href="https://www.linkedin.com/feed/hashtag/?keywords=turn" rel="noopener nofollow ugc">hashtag#Turn</a> on distance scalars on Models module’s properties</p>
<p>“”"<br>
Creating a points-only polydata doesn’t work<br>
points = vtk.vtkPoints()<br>
vertsCellArray = vtk.vtkCellArray()<br>
appendFilter = vtk.vtkAppendPolyData()<br>
for i in range(fiducialList.GetNumberOfControlPoints()):<br>
position = [0,0,0]<br>
fiducialList.GetNthControlPointPosition(i,position)<br>
pointId = points.InsertNextPoint(position)<br>
vertsCellArray.InsertNextCell(1)<br>
vertsCellArray.InsertCellPoint(pointId)</p>
<p>polydata = vtk.vtkPolyData()<br>
polydata.SetPoints(points)<br>
polydata.SetVerts(vertsCellArray)<br>
polydata.Modified()</p>
<p>myModel = getNode(‘deformed_Right_tibia’)</p>
<p>distanceFilter = vtk.vtkDistancePolyDataFilter()<br>
distanceFilter.SetInputData(0, myModel.GetPolyData())<br>
distanceFilter.SetInputData(1, polydata)<br>
distanceFilter.SignedDistanceOff()<br>
distanceFilter.Update()</p>
<p>myModel.SetAndObservePolyData(distanceFilter.GetOutput())<br>
“”"</p>
<p>thresholdFilter = vtk.vtkThreshold()<br>
thresholdFilter.SetInputData(distanceFilter.GetOutput())<br>
maximumDistanceToPointsmm = 15<br>
thresholdFilter.ThresholdBetween(0, maximumDistanceToPointsmm)<br>
thresholdFilter.SetInputArrayToProcess(0, 0, 0,<br>
vtk.vtkDataObject.FIELD_ASSOCIATION_CELLS,<br>
“Distance”)<br>
<a href="https://www.linkedin.com/feed/hashtag/?keywords=thresholdfilter" rel="noopener nofollow ugc">hashtag#thresholdFilter</a>.SetInputArrayToProcess(0, 0, 0,</p>
<h1><a name="p-123188-vtkvtkdataobject-1" class="anchor" href="#p-123188-vtkvtkdataobject-1" aria-label="Heading link"></a>vtk.vtkDataObject.</h1>
<h1><a name="p-123188-field_association_points-distance-2" class="anchor" href="#p-123188-field_association_points-distance-2" aria-label="Heading link"></a>FIELD_ASSOCIATION_POINTS, “Distance”)</h1>
<p>thresholdFilter.Update()<br>
geometryFilter = vtk.vtkGeometryFilter()<br>
geometryFilter.SetInputData(thresholdFilter.GetOutput())<br>
geometryFilter.Update()<br>
myModel2 = getNode(‘deformed_Right_tibia Copy’)<br>
myModel2.SetAndObservePolyData(geometryFilter.GetOutput())</p>

---

## Post #21 by @mau_igna_06 (2025-03-11 12:48 UTC)

<p>Hi</p>
<blockquote>
<p>For “MarkupFiducial”, how do I invoke it in 3D Slicer?</p>
</blockquote>
<p>You can create a MarkupsFiducial using the Markups toolbar as explained <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#place-new-markups" rel="noopener nofollow ugc">here</a>. To create a markup points list, please press the button squared on the picture below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdc911b38170f837fc4ad702e49dce6572475dbc.png" data-download-href="/uploads/short-url/Ad5AuT4z4gmLy9Ff8wFiH1PXxSI.png?dl=1" title="Screenshot from 2025-03-11 09-47-24_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdc911b38170f837fc4ad702e49dce6572475dbc_2_690x390.png" alt="Screenshot from 2025-03-11 09-47-24_2" data-base62-sha1="Ad5AuT4z4gmLy9Ff8wFiH1PXxSI" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdc911b38170f837fc4ad702e49dce6572475dbc_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdc911b38170f837fc4ad702e49dce6572475dbc_2_1035x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdc911b38170f837fc4ad702e49dce6572475dbc_2_1380x780.png 2x" data-dominant-color="5A5961"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-03-11 09-47-24_2</span><span class="informations">2484×1405 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
