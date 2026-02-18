# Custom‐fitting Surgical Guides on Slicer

**Topic ID**: 14270
**Date**: 2020-10-27
**URL**: https://discourse.slicer.org/t/custom-fitting-surgical-guides-on-slicer/14270

---

## Post #1 by @mau_igna_06 (2020-10-27 17:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd704cc562b694a13d24db3078565e574c1e85a8.png" data-download-href="/uploads/short-url/tjotW2ipv52KWtJkxVAWIWtHG3e.png?dl=1" title="Captura" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd704cc562b694a13d24db3078565e574c1e85a8_2_662x500.png" alt="Captura" data-base62-sha1="tjotW2ipv52KWtJkxVAWIWtHG3e" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd704cc562b694a13d24db3078565e574c1e85a8_2_662x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd704cc562b694a13d24db3078565e574c1e85a8_2_993x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd704cc562b694a13d24db3078565e574c1e85a8.png 2x" data-dominant-color="D0D0D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura</span><span class="informations">1097×828 430 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is a question for the experts on python scripting here on the Slicer’s forum: Considering the osteotomy planes are already positioned like in picture A. Is it possible to develop on Slicer custom-fitting surgical guides such as the ones shown in pictures B and C?</p>

---

## Post #2 by @mau_igna_06 (2020-10-25 17:36 UTC)

<p>Thank you Andras for such a complete answer. It is great. I have read a paper that compared osteotomies of free-hand surgery, patient specific surgical guides (PSSG) and navigation systems and said that osteotomies with PSSG were the most accurate. In addition to that they don’t need navigation hardware and can be made with a desktop 3d printer in biocompatible PLA and esterilized with EtO or Gamma rays. Another question for you is: Is it possible to develop PSSG on Slicer?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66c403a6ca81b25b793f77724ea35bb10a4b16de.jpeg" data-download-href="/uploads/short-url/eF6EXnElXSzmkuTDsFgifT4v4zI.jpeg?dl=1" title="Captura.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66c403a6ca81b25b793f77724ea35bb10a4b16de_2_662x500.jpeg" alt="Captura.PNG" data-base62-sha1="eF6EXnElXSzmkuTDsFgifT4v4zI" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66c403a6ca81b25b793f77724ea35bb10a4b16de_2_662x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66c403a6ca81b25b793f77724ea35bb10a4b16de_2_993x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66c403a6ca81b25b793f77724ea35bb10a4b16de.jpeg 2x" data-dominant-color="D0D0D0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura.PNG</span><span class="informations">1097×828 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2020-10-28 04:11 UTC)

<p>Yes, Slicer contains everything you need to create patient-specific surgical guides. You can segment the anatomy using segment editor module and combine with other pieces and add cuts using segment editor and dynamic modeler modules. Once the user completed segmentation and marking up the models, the remaining steps can be automated using Python scripting.</p>

---

## Post #4 by @manjula (2020-10-28 21:49 UTC)

<p>Dear Prof <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I guess the question was</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="14270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>and combine with other pieces</p>
</blockquote>
</aside>
<p>whether we could create these “other pieces” i.e the guides within the 3D Slicer. Which would be great.</p>
<p>In commercial software like Materialise, we use the Materialise proplan-cmf for segmentation and planning (in 3D slicer it would be work done by the the segment editor + dynamic modeler) and then the  Materialise 3-matic to design the guides. So I guess the question is whether can we use 3D slicer to do the part done by a software equivalent to 3Matic as well.</p>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> you can use if you have not already using  As opensource options like Blender and FreeCAD  to design the guide. (you can import the planned segments in to them in STL or as OBJ or PLY ). Blender is not ideal for 3D printing.</p>
<p>Also i have tried to create some guides with the segment editor of 3D slicer using the tools already available. You can do something with that too. Main advantage of doing it within the slicer segment editor is that you will get a ready to 3D print stl with no non-manifold edges and intersect faces. (  i guess it has to do with the segment editor works ? )</p>

---

## Post #5 by @lassoan (2020-10-28 23:44 UTC)

<aside class="quote no-group" data-username="manjula" data-post="4" data-topic="14270">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>So I guess the question is whether can we use 3D slicer to do the part done by a software equivalent to 3Matic as well.</p>
</blockquote>
</aside>
<p>Probably 3-matic has a number of features that Slicer does not have, but most likely you only need a few. If you tell what features exactly would you need then we can tell if it is already doable in Slicer and if not then how hard it would be to implement. Slicer relies on very powerful libraries, such as VTK and ITK and we can easily pull in any Python packages, so there are a lot of features that could be easily added to Slicer.</p>

---

## Post #6 by @manjula (2020-10-29 23:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="14270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you tell what features exactly would you need then we can tell if it is already doable in Slicer and if not then how hard it would be to implement</p>
</blockquote>
</aside>
<p>Dear Prof Lasso, Thank you for your quick answer.<br>
I have kind of worked out a workflow for this with 3D slicer and there are many other ways of doing the same thing as well. I have just use the sample data and fibular segmentation from some other case just to explain the case and please pardon the quality of my work as I simply did it for demonstration purposes only and it is not accurate.</p>
<ol>
<li>It would be great if we can give thickness to a cutting plane.</li>
</ol>
<p>(also to define the width and height of the plane, I know it can be done with the handles but it is really difficult to manipulate the points in 3D as it is very difficult to get the hang of it and it just behaves in unpredictable ways. )<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/902af2dab94902f79c490e74678b7c2894fe662e.png" data-download-href="/uploads/short-url/kzmLUEyccYjtRbizkVNe1elkzTw.png?dl=1" title="01.GivePlaneThickenss" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/902af2dab94902f79c490e74678b7c2894fe662e_2_690x388.png" alt="01.GivePlaneThickenss" data-base62-sha1="kzmLUEyccYjtRbizkVNe1elkzTw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/902af2dab94902f79c490e74678b7c2894fe662e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/902af2dab94902f79c490e74678b7c2894fe662e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/902af2dab94902f79c490e74678b7c2894fe662e_2_1380x776.png 2x" data-dominant-color="B7B5C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01.GivePlaneThickenss</span><span class="informations">1920×1080 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1972aea7d889af2638408b4a0147b92d2c8b3900.jpeg" data-download-href="/uploads/short-url/3D7DPaYdzZeMOMziAiHtvTDKUw0.jpeg?dl=1" title="Screenshot from 2020-10-29 22-20-34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1972aea7d889af2638408b4a0147b92d2c8b3900_2_690x388.jpeg" alt="Screenshot from 2020-10-29 22-20-34" data-base62-sha1="3D7DPaYdzZeMOMziAiHtvTDKUw0" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1972aea7d889af2638408b4a0147b92d2c8b3900_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1972aea7d889af2638408b4a0147b92d2c8b3900_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1972aea7d889af2638408b4a0147b92d2c8b3900_2_1380x776.jpeg 2x" data-dominant-color="C4C2AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-29 22-20-34</span><span class="informations">1920×1080 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>
<p>One the cutting planes are defined is there a way to translating the cutting planes to the fibular segment ?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97951797b3bea880e629cbde4a7b395d81558050.png" data-download-href="/uploads/short-url/lCXwDV65EHW75QknQ5DWVSHl3bi.png?dl=1" title="Screenshot from 2020-10-29 23-18-34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97951797b3bea880e629cbde4a7b395d81558050_2_690x490.png" alt="Screenshot from 2020-10-29 23-18-34" data-base62-sha1="lCXwDV65EHW75QknQ5DWVSHl3bi" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97951797b3bea880e629cbde4a7b395d81558050_2_690x490.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97951797b3bea880e629cbde4a7b395d81558050_2_1035x735.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97951797b3bea880e629cbde4a7b395d81558050.png 2x" data-dominant-color="9C92B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-29 23-18-34</span><span class="informations">1309×931 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> ’</p>
</li>
<li>
<p>Once surgical cuts are done how to construct the cutting guides inside the 3D Slicer ? Is there a way of extruding/pad the surface by defined amount ? (give thickness).  Rather than using the scissors to draw is it possible to use the markup to mark the area that we want to draw and then convert the area to a segment/model and give a thickness to that area ?</p>
</li>
</ol>
<p>As this will give excellent control</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c26d33301f086082eb7daf884c4a477b1f90188.png" data-download-href="/uploads/short-url/jZQ1JLD9hNOFUIoPtFtT0Jzi4Nq.png?dl=1" title="Screenshot from 2020-10-30 00-00-06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c26d33301f086082eb7daf884c4a477b1f90188_2_690x388.png" alt="Screenshot from 2020-10-30 00-00-06" data-base62-sha1="jZQ1JLD9hNOFUIoPtFtT0Jzi4Nq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c26d33301f086082eb7daf884c4a477b1f90188_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c26d33301f086082eb7daf884c4a477b1f90188_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c26d33301f086082eb7daf884c4a477b1f90188_2_1380x776.png 2x" data-dominant-color="B1ACC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-30 00-00-06</span><span class="informations">1920×1080 378 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For now something like this can be done with scissors but it is not elegant.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86157df5a123993a5bc69acf3456c8c72243cbe0.png" data-download-href="/uploads/short-url/j8a1HI8xGBacxHCyo5QD67mVLPi.png?dl=1" title="Screenshot from 2020-10-29 23-22-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86157df5a123993a5bc69acf3456c8c72243cbe0_2_657x499.png" alt="Screenshot from 2020-10-29 23-22-46" data-base62-sha1="j8a1HI8xGBacxHCyo5QD67mVLPi" width="657" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86157df5a123993a5bc69acf3456c8c72243cbe0_2_657x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86157df5a123993a5bc69acf3456c8c72243cbe0_2_985x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86157df5a123993a5bc69acf3456c8c72243cbe0.png 2x" data-dominant-color="988FB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-29 23-22-46</span><span class="informations">1148×873 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb753719dc657d5efa3360450f5d1d2dbf27d83a.png" data-download-href="/uploads/short-url/qKkq0q0814LbqOHbo1bgqtJkN9U.png?dl=1" title="Screenshot from 2020-10-29 23-21-08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb753719dc657d5efa3360450f5d1d2dbf27d83a_2_690x388.png" alt="Screenshot from 2020-10-29 23-21-08" data-base62-sha1="qKkq0q0814LbqOHbo1bgqtJkN9U" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb753719dc657d5efa3360450f5d1d2dbf27d83a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb753719dc657d5efa3360450f5d1d2dbf27d83a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb753719dc657d5efa3360450f5d1d2dbf27d83a_2_1380x776.png 2x" data-dominant-color="A3ABBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-29 23-21-08</span><span class="informations">1920×1080 449 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It above 3 can be done i think it would be possible to construct something like this with ease.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a52eba88dc2a341929cba61a744a78b298afa467.png" data-download-href="/uploads/short-url/nzgTH3gveDWublRsYaO446a06mr.png?dl=1" title="Screenshot from 2020-10-29 23-31-28" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a52eba88dc2a341929cba61a744a78b298afa467_2_690x499.png" alt="Screenshot from 2020-10-29 23-31-28" data-base62-sha1="nzgTH3gveDWublRsYaO446a06mr" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a52eba88dc2a341929cba61a744a78b298afa467_2_690x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a52eba88dc2a341929cba61a744a78b298afa467_2_1035x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a52eba88dc2a341929cba61a744a78b298afa467.png 2x" data-dominant-color="9B8FAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-29 23-31-28</span><span class="informations">1288×933 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>Also would it be possible to transform the cutting guide on to the fibuar and vice versa ?</li>
</ol>
<p>Thank you</p>

---

## Post #7 by @lassoan (2020-10-30 04:27 UTC)

<p>What you describe are developments in the GUI to make the manual workflow easier to do. But probably it would be much easier to implement and way more convenient to use if plane placement would be mostly automated. Placing the planes from bone segmentation and some landmark points should be not be hard, using a small Python scripted module. You would then only need to make small adjustments, which would be easy to do, with the current widgets as they are.</p>
<p>I’m just curious, if commercial solutions already exist for this planning, what is the motivation for developing custom software for it? Do you have improvement ideas that you would like to try but the commercial software has a too rigid workflow?</p>

---

## Post #8 by @manjula (2020-10-30 09:30 UTC)

<p>Dear Prof <a class="mention" href="/u/lassoan">@lassoan</a>, thank you for the reply</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="14270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>implement and way more convenient to use if plane placement would be mostly automated.</p>
</blockquote>
</aside>
<p>As the first step can you please let me know how to put the planes to the mandible and translate that to the fibualr bone ?</p>
<p>Do you think is possible with the 3D slicer as it is without much development?  or at least transfer the plane as i mentioned earlier <a href="https://youtu.be/KYZlEP9mHvw?t=125" rel="noopener nofollow ugc">https://youtu.be/KYZlEP9mHvw?t=125</a> ?</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="14270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if commercial solutions already exist for this planning, what is the motivation for developing custom software fo</p>
</blockquote>
</aside>
<p>Due to 3 main reasons. 1. Most of the commercial software has limited functions  (i think that’s the idea ) so to make a whole package you have to purchase lots of modules. 2. These softwares (in my opinion only one for CMF surgery is worth it at any cost) is prohibitively expensive for developing countries. 3. I personally believe open source should be the way in medical services at least to address the mismatch of resources and to keep the cost of software/devices at manageable levels to emerging economies.</p>
<p>Also of course I have improvement ideas for the software that would improve the workflow. And it is hard to do with commercial software. ( I have inbox you some other details that cannot be or i thought inappropriate to be disclosed in public)</p>

---

## Post #9 by @lassoan (2020-10-30 13:29 UTC)

<aside class="quote no-group" data-username="manjula" data-post="8" data-topic="14270">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>As the first step can you please let me know how to put the planes to the mandible and translate that to the fibualr bone ?</p>
</blockquote>
</aside>
<p>I would define a curve on the mandible, each point defining a cutting position. Set Markups module / Curve settings / Curve type → Linear. Also define a centerline on the fibula using a Line markup. You can measure angles between the segments with a few lines of Python code and generate fibula cutting planes automatically (with a few dozens of lines of Python script). It would make sense to create a small scripted module for this, for ease of use, specifying of additional parameters (cutting plane angle adjustments, specification of cut thickness), and automatic updates of cutting planes and automatic display of cut-out fibula pieces in their planned position.</p>

---

## Post #10 by @manjula (2020-10-31 13:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I have selected a case which is the simplest scenario for cutting guide generation.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="14270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>curve on the mandible, each point defining a cutting position.</p>
</blockquote>
</aside>
<p>I have done that</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="14270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>centerline on the fibula using a Line markup.</p>
</blockquote>
</aside>
<p>I have made the line but do it need to be a centerline ? or the way I have done it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f7403e6ceb292969c3a9e4450960bbc8c5740f7.png" data-download-href="/uploads/short-url/fTXyLqOyTRIpAXZgndl3YoF5MlV.png?dl=1" title="Screenshot from 2020-10-31 14-29-35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f7403e6ceb292969c3a9e4450960bbc8c5740f7_2_690x388.png" alt="Screenshot from 2020-10-31 14-29-35" data-base62-sha1="fTXyLqOyTRIpAXZgndl3YoF5MlV" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f7403e6ceb292969c3a9e4450960bbc8c5740f7_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f7403e6ceb292969c3a9e4450960bbc8c5740f7_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f7403e6ceb292969c3a9e4450960bbc8c5740f7_2_1380x776.png 2x" data-dominant-color="9A9CB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-31 14-29-35</span><span class="informations">1920×1080 357 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @drvarunagarwal (2020-11-20 17:09 UTC)

<p>Hi,</p>
<p>I have been following this thread with interest.</p>
<p>Can yu plese elaborate that how after marking up the 3D model, can one convert it into a guide and automate the process?</p>
<p>many thanks</p>

---

## Post #12 by @lassoan (2020-11-27 18:46 UTC)

<p>I’ve created repository for this project (<a href="https://github.com/lassoan/SlicerBoneReconstructionPlanner">https://github.com/lassoan/SlicerBoneReconstructionPlanner</a>). <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> will work on this in the next few months as his final project in engineering school.</p>

---

## Post #13 by @martig (2021-02-08 10:59 UTC)

<p>Hi,</p>
<p>I’m interested in this project. I tried it out a few days ago. I can see that it’s not quite ready yet.<br>
Is there any way I could contribute? Unfortunately I don’t have any python skills.</p>

---

## Post #14 by @manjula (2021-02-08 18:44 UTC)

<p>Hi Martig,</p>
<p>Yes, you and anyone else can contribute to the project in any way you wish/can.</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/lassoan/SlicerBoneReconstructionPlanner" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/307929?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/lassoan/SlicerBoneReconstructionPlanner" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerBoneReconstructionPlanner</a></h3>


  <p><span class="label1">3D Slicer module for planning mandible reconstruction surgery using fibula flap</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>best<br>
Manjula</p>

---

## Post #15 by @lassoan (2021-02-08 19:13 UTC)

<aside class="quote no-group" data-username="martig" data-post="13" data-topic="14270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/martig/48/4516_2.png" class="avatar"> martig:</div>
<blockquote>
<p>I tried it out a few days ago. I can see that it’s not quite ready yet.</p>
</blockquote>
</aside>
<p>Yes, the module is actively being worked on. The plan is to have automatic surgical bone cutting and placement guide generation in a few months.</p>
<p><a class="mention" href="/u/martig">@martig</a> Would you be interested to use this for mandibular reconstruction with fibula free flap? What is your expertise and how would you use the surgical guide designer? We have a conference call once in every couple of weeks, if you were interested to join then send your contact info in a private message to <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> and he will invite you to the next meeting.</p>

---

## Post #16 by @martig (2021-02-09 07:41 UTC)

<p>Yes, I would be interested in using for the mandibular reconstruction with fibula free flap. So far I have designed guides for one surgery with ProPlan CMF and for another using Blender. I have also designed guides for cranioplasty surgeries with Blender. It seems the new Dynamic Modeler extension is also quite useful for that.<br>
I will contact <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> .</p>

---

## Post #17 by @mau_igna_06 (2021-05-16 12:44 UTC)

<p>BoneReconstructionPlanner is now available in the Extensions Manager for Slicer latest preview release.</p>
<p>Here is a preview video:</p><div class="youtube-onebox lazy-video-container" data-video-id="wsr_g_1E_pw" data-video-title="Mandible reconstruction on Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=wsr_g_1E_pw" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/wsr_g_1E_pw/hqdefault.jpg" title="Mandible reconstruction on Slicer" width="" height="">
  </a>
</div>

<p>And the link to the project:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://repository-images.githubusercontent.com/316575529/fc6f0980-7e9e-11eb-9a53-5c1e41ae1245" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for...</a></h3>

  <p>3D Slicer module for planning mandible reconstruction surgery using fibula flap - GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for planning mandible reconstruction surgery u...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
