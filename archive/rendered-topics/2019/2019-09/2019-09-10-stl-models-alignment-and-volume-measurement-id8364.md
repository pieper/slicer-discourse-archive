# STL models - Alignment and Volume measurement

**Topic ID**: 8364
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/stl-models-alignment-and-volume-measurement/8364

---

## Post #1 by @manjula (2019-09-10 14:01 UTC)

<p>Hi,</p>
<p>Our Input - 2 STL surface scan models  (PreOp and Post Op) - from the 3Shape surface scanner.</p>
<p>We have two problems.</p>
<ol>
<li>
<p>Need to accurately align the pre and post op surface scans ? (they have fixed landmarks)</p>
</li>
<li>
<p>Need to measure the change of volume in the region of interest ? ( the volume of bone resorption)</p>
</li>
</ol>
<p>So far, we have install CMF registration and,</p>
<p>as you can see from the pictures the alignment with CMF surface registration is not accurate enough.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b21e83b01606bbf24344a6705dad93c0af5537b.png" alt="PreOperative" data-base62-sha1="1AtTFyYS3J4HzOPmd1UwJZGGoFZ" width="690" height="485"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dfd655d9175ff97f94b98986013de29a921c1a6.jpeg" data-download-href="/uploads/short-url/1ZL6xmFVrjiW5xSe8aNpfh8Yrem.jpeg?dl=1" title="SuperImposed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dfd655d9175ff97f94b98986013de29a921c1a6_2_690x485.jpeg" alt="SuperImposed" data-base62-sha1="1ZL6xmFVrjiW5xSe8aNpfh8Yrem" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dfd655d9175ff97f94b98986013de29a921c1a6_2_690x485.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dfd655d9175ff97f94b98986013de29a921c1a6_2_1035x727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dfd655d9175ff97f94b98986013de29a921c1a6.jpeg 2x" data-dominant-color="9491BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SuperImposed</span><span class="informations">1160×816 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We need to improve the accuracy of the alignment and we are unable to do it so far.</p>
<p>Can someone help us with accurate alignment/superimposition of the two scans ?</p>
<p>Next we need to measure the change in the bone volumes in the circled region. That is the difference of bone volume in preoperative and postoperative scans.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809.jpeg" data-download-href="/uploads/short-url/mf3VrCUemmTI25kMqFuZLAQHLrr.jpeg?dl=1" title="Volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809_2_608x500.jpeg" alt="Volume" data-base62-sha1="mf3VrCUemmTI25kMqFuZLAQHLrr" width="608" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809_2_608x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809_2_912x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809_2_1216x1000.jpeg 2x" data-dominant-color="867E7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Volume</span><span class="informations">1279×1051 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this can be done in 3d Slicer ?</p>
<p>Looking forward to hearing from you all.</p>
<p>Thanks</p>

---

## Post #2 by @timeanddoctor (2019-09-14 04:36 UTC)

<p>yes.<br>
You can use the “fiducial registration” and modeltomodel…<br>
…</p>

---

## Post #3 by @Juicy (2019-09-16 07:58 UTC)

<p>Have you seen this? <a href="https://www.youtube.com/watch?v=hsZrjNsXZbs" rel="nofollow noopener">Registration Video</a></p>
<p>Perhaps you could try ROI registration around those small tube looking bits which seem to be common to both models. To be honest with some models I just cant get automatic registration to work well enough. With a bit of time I can get a better result using manual registration of the two models.</p>
<p>You can manually move one model around using the “Transforms” module. It helps to make the models visible in the slice view which you can do under the “Models” module. Remember that the rotation seems to always be about the origin or 0,0,0 coordinate in the 3d space. So it helps a lot if your model is centered over the origin (0,0,0) point before you start moving it. Click local coordinate button in the transforms module to keep the rotation point around the centre of the model as you move it around.</p>
<p>Im not sure about the volume measurement part</p>

---

## Post #4 by @manjula (2019-09-16 08:06 UTC)

<p>Dear Timeandddoctor,</p>
<p>Thank you so much for your suggestion.</p>
<p>Are you suggesting the fiducial registration in the CMF surface registration model ?</p>
<p>Also can you point me to how to get the colour map for model to model distance module ?</p>
<p>Kind regards</p>
<p>Manjula</p>

---

## Post #5 by @lassoan (2019-09-17 00:29 UTC)

<p>If you can accurately identify landmark points then you may use Fiducial registration wizard module (in SlicerIGT extension) to register based manually placed landmarks. See U-12 <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorial</a> for step-by-step instructions.</p>

---

## Post #6 by @manjula (2019-09-17 10:56 UTC)

<p>Dear Prof Lasso,<br>
I used the as you suggested but this is my results and went through the tutorial as well. I can’t figure out  , how to get it to transformed. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef13654e402ff63028bb6df88000abf27c14df7a.png" data-download-href="/uploads/short-url/y6XFzJFvtreRK01I1tvEkwQV2ZQ.png?dl=1" title="IGTExt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef13654e402ff63028bb6df88000abf27c14df7a_2_690x426.png" alt="IGTExt" data-base62-sha1="y6XFzJFvtreRK01I1tvEkwQV2ZQ" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef13654e402ff63028bb6df88000abf27c14df7a_2_690x426.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef13654e402ff63028bb6df88000abf27c14df7a_2_1035x639.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef13654e402ff63028bb6df88000abf27c14df7a_2_1380x852.png 2x" data-dominant-color="7A7C9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IGTExt</span><span class="informations">1914×1182 391 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What i am doing wrong ?</p>

---

## Post #7 by @lassoan (2019-09-17 13:00 UTC)

<p>Registration result is a transform (not a transformed model node). You can apply this transform to models, markups, images, etc. to align them.</p>
<p>An easy way to preview transformation result and apply it to the model is to choose the moving model node in “Preview transform” section and click “Apply”.</p>

---

## Post #8 by @manjula (2019-09-17 14:19 UTC)

<p>I think i have better results now even though i have to perfect it. It comes with a error code.</p>
<p>Is it because of the geometry of the fixed landmarks we have ?  (Do i need to select point matching method to manual ?) What is s RMS error ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8398b22f75bb41c31a408abb7b3e382f8559c92.png" data-download-href="/uploads/short-url/qhJ8JNMwAVBmG35QmvTPQj4qDuy.png?dl=1" title="Screenshot%20from%202019-09-17%2016-09-13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8398b22f75bb41c31a408abb7b3e382f8559c92_2_690x417.png" alt="Screenshot%20from%202019-09-17%2016-09-13" data-base62-sha1="qhJ8JNMwAVBmG35QmvTPQj4qDuy" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8398b22f75bb41c31a408abb7b3e382f8559c92_2_690x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8398b22f75bb41c31a408abb7b3e382f8559c92_2_1035x625.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8398b22f75bb41c31a408abb7b3e382f8559c92_2_1380x834.png 2x" data-dominant-color="746F8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202019-09-17%2016-09-13</span><span class="informations">1917×1160 642 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also suppose i make this to a good alignment and then how can i save this aligned model to compare this in model to model distance module ?</p>
<p>Thanks</p>

---

## Post #9 by @lassoan (2019-09-17 14:39 UTC)

<aside class="quote no-group" data-username="manjula" data-post="8" data-topic="8364">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>It comes with a error code.</p>
</blockquote>
</aside>
<p>It seems that your point pattern is not unique enough for the automatic point matching to work reliably. Disable automatic point matching and instead make sure you mark corresponding points in the same order.</p>
<aside class="quote no-group" data-username="manjula" data-post="8" data-topic="8364">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>What is s RMS error ?</p>
</blockquote>
</aside>
<p>It is the root mean square of the residual error after fitting the landmark points. It characterizes how well the points can be aligned by the chosen transformation. Lower values are better.</p>

---

## Post #10 by @manjula (2019-09-19 09:34 UTC)

<p>Thank you very much for your great assistance.  I am at the moment trying to perfect the alignment on my samples trying different configurations.</p>
<p>I will soon comeback with my results and problems.</p>

---

## Post #11 by @manjula (2019-09-20 21:33 UTC)

<p>Finally i think i have good alignment following the method Prof Lasso suggested. Many thanks for the wonderful help.</p>
<p>For my benefit can you all please comment which image is better aligned ? A1 or B1. One is using the 3D Slicer and other one a commercial product.</p>
<p><strong>A1</strong>  <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25c9d68859fc6c93649adfb69a9e2264d508fcec.jpeg" alt="A1" data-base62-sha1="5oi6luFq0H15Occ5MII2Tigy2Ha" width="420" height="439"></p>
<p><strong>B1</strong>   <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab5b108ec108abdf074b900a6573eaedfd07f8a7.jpeg" data-download-href="/uploads/short-url/orSKF4rWklpXTHhJFEPJkyYAV3F.jpeg?dl=1" title="B1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab5b108ec108abdf074b900a6573eaedfd07f8a7_2_486x500.jpeg" alt="B1" data-base62-sha1="orSKF4rWklpXTHhJFEPJkyYAV3F" width="486" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab5b108ec108abdf074b900a6573eaedfd07f8a7_2_486x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab5b108ec108abdf074b900a6573eaedfd07f8a7_2_729x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab5b108ec108abdf074b900a6573eaedfd07f8a7.jpeg 2x" data-dominant-color="7B9BB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">B1</span><span class="informations">732×752 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>According to the opinion of the guys here which you think is better aligned ?</p>
<p>And my second problem is to measure the difference in Volume ? (this is the old photo but the idea remains the same to ilustrate where exactly i want the volume difference in )</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec67096a272fd591d435e20db6d4009aa5824626.png" alt="2aa220b72b9c97e2200b5a4e8df0855cb24f0b5b_2_608x500%20(1)" data-base62-sha1="xJjraPhbaxrQTN41odAEB4OV3oO" width="608" height="500"></p>
<p>Also i want to create a colour map like this one using 3D Slicer. (this was not created with the 3D Slicer)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3132fac34bfc761a80cd5ab20fac5a0c598379c9.jpeg" alt="colourmap" data-base62-sha1="71eCoh09GcdFqehwidW2k5WVXvz" width="419" height="500"></p>
<p>I tried the <a href="https://www.youtube.com/watch?v=FCCa2A77fV8" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=FCCa2A77fV8</a>  but i cannot find the 3Derror metric plugin in my slicer as shown in the video here.  So i dont’ know how to proceed.</p>
<p>Looking for the help again by anyone who is interested.</p>
<p>Thanks</p>

---

## Post #12 by @lassoan (2019-09-21 14:50 UTC)

<p>Alignment is hard to assess in 3D view. It is more visible in slice views.</p>
<p>You can meause volumes by importing the model nodes to a segmentation node and then use segment statistics module.</p>

---

## Post #13 by @manjula (2019-09-21 17:13 UTC)

<p>Thank you again.</p>
<p>I figured out how to asses it in slice views.</p>
<p>But may i please know how to import model nodes to a segmentation node ?</p>
<p>Also how to get the color map ? (The colour map i posted is not created using 3D Slicer. )</p>

---

## Post #14 by @lassoan (2019-09-23 21:09 UTC)

<aside class="quote no-group" data-username="manjula" data-post="13" data-topic="8364">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>But may i please know how to import model nodes to a segmentation node ?</p>
</blockquote>
</aside>
<p>Using Segmentations module Import section.</p>
<aside class="quote no-group" data-username="manjula" data-post="13" data-topic="8364">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>how to get the color map ?</p>
</blockquote>
</aside>
<p>You can comoute distances between modules using Model to model distance extension.</p>

---

## Post #15 by @manjula (2019-09-10 14:18 UTC)

<p>Hi,</p>
<p>Our Input - 2 STL surface scan models  (PreOp and Post Op) - from the 3Shape surface scanner.</p>
<p>We have two problems.</p>
<ol>
<li>
<p>Need to accurately align the pre and post op surface scans ? (they have fixed landmarks)</p>
</li>
<li>
<p>Need to measure the change of volume in the region of interest ? ( the volume of bone resorption)</p>
</li>
</ol>
<p>So far, we have install CMF registration and,</p>
<p>as you can see from the pictures the alignment with CMF surface registration is not accurate enough.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b21e83b01606bbf24344a6705dad93c0af5537b.png" alt="PreOperative" data-base62-sha1="1AtTFyYS3J4HzOPmd1UwJZGGoFZ" width="690" height="485"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dfd655d9175ff97f94b98986013de29a921c1a6.jpeg" data-download-href="/uploads/short-url/1ZL6xmFVrjiW5xSe8aNpfh8Yrem.jpeg?dl=1" title="SuperImposed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dfd655d9175ff97f94b98986013de29a921c1a6_2_690x485.jpeg" alt="SuperImposed" data-base62-sha1="1ZL6xmFVrjiW5xSe8aNpfh8Yrem" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dfd655d9175ff97f94b98986013de29a921c1a6_2_690x485.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dfd655d9175ff97f94b98986013de29a921c1a6_2_1035x727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dfd655d9175ff97f94b98986013de29a921c1a6.jpeg 2x" data-dominant-color="9491BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SuperImposed</span><span class="informations">1160×816 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We need to improve the accuracy of the alignment and we are unable to do it so far.</p>
<p>Can someone help us with accurate alignment/superimposition of the two scans ?</p>
<p>Next we need to measure the change in the bone volumes in the circled region. That is the difference of bone volume in preoperative and postoperative scans.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809.jpeg" data-download-href="/uploads/short-url/mf3VrCUemmTI25kMqFuZLAQHLrr.jpeg?dl=1" title="Volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809_2_608x500.jpeg" alt="Volume" data-base62-sha1="mf3VrCUemmTI25kMqFuZLAQHLrr" width="608" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809_2_608x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809_2_912x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9be3bbff36435aa9258599e0989fd95dcb183809_2_1216x1000.jpeg 2x" data-dominant-color="867E7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Volume</span><span class="informations">1279×1051 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this can be done in 3d Slicer ?</p>
<p>Looking forward to hearing from you all.</p>
<p>Thanks</p>

---

## Post #16 by @lassoan (2020-02-28 16:35 UTC)

<p>We talked a lot about registration. Summary:</p>
<ul>
<li>Current surface-to-surface methods require cutting off non-common surfaces, which will be much easier with the new surface cutting module that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is working on (that will allow cutting with plane widgets and surface curves).</li>
<li>There is also the option of doing landmark registration.</li>
<li>Integration of more robust surface matching algorithm from OpenCV could allow surface matching without the need to cut off non-common surfaces - this should not be too much work, but would require dedicated funding (or maybe you may ask SlicerCMF developers if it is potentially in the scope of their project).</li>
</ul>
<p>Volume measurement: You need to register the surfaces, then close them (for example, cut off excess parts, thicken it using vtkLinearExtrusionFilter, then cut off the back side). We did this for surface-scan based volumetric fat resorption monitoring after breast lipofilling (see details in this <a href="https://qspace.library.queensu.ca/handle/1974/26146">thesis</a> and implementation in this <a href="https://github.com/PerkLab/BreastReconstruction">repository</a>). It would be not too hard to adapt this to dental scans, but probably would require dedicated project. SlicerCMF and others, such as <a class="mention" href="/u/cpinter">@cpinter</a> might be potentially interested in collaborating or could help out if you can secure some funding.</p>

---

## Post #17 by @sfglio (2023-08-26 21:32 UTC)

<p>Are there <strong>any updates on this topic</strong>?</p>
<p>Volume measurement between two intraoral or breast STL files which are generally not closed need manual adjustments to close the surface…<br>
In the thesis provided an extrusion of the surface was performed. Wouldn’t bridging (joining) the two surfaces provide the same results in case you have multiple follow up scans e.g. to measure postop swelling and would like to detect the % reduction over time?</p>

---
