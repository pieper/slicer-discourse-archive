# Teeth Segmentation

**Topic ID**: 9775
**Date**: 2020-01-10
**URL**: https://discourse.slicer.org/t/teeth-segmentation/9775

---

## Post #1 by @manjula (2020-01-10 20:03 UTC)

<p>Is there a easier way of segmenting multiple  teeth easily like shown here from a CBCT ?</p>
<div class="youtube-onebox lazy-video-container" data-video-id="MFzFKGKx29Q" data-video-title="3D Tooth Segmentation Tool: How to segment many teeth easily" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=MFzFKGKx29Q" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/MFzFKGKx29Q/maxresdefault.jpg" title="3D Tooth Segmentation Tool: How to segment many teeth easily" width="" height="">
  </a>
</div>

<p>I tried thresholding and grow from seed, fill between slices and filling holes and applying smoothes.</p>
<p>While we can segment out single tooth after spending like 15 minutes on 1 teeth with good results  it is not easy to do this for all the teeth. Is there a easier way like as shown here in the youtube ?</p>
<p>Also if someone has done teeth segmenting from CBCT what is the normal work flow that worked the best for you ?</p>
<p>thanks</p>

---

## Post #2 by @manjula (2020-01-10 21:11 UTC)

<p>My end goal is to achieve this the easiest way !</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eedc4a66626ee7d3ad906e2ede36d0e912ed7254.jpeg" alt="eedc4a66626ee7d3ad906e2ede36d0e912ed7254" data-base62-sha1="y53BITyH7ZdDisjTnHd2pjlmR8g" width="599" height="468"></p>

---

## Post #3 by @lassoan (2020-01-10 22:22 UTC)

<p>The segmentation process in the video above looks very tedious. It should be possible to do it much more easily. If you have a good-quality CBCT to share then we could try various segmentation approaches. It should be also possible to train an AI model that would segment a tooth from a single click.</p>

---

## Post #4 by @manjula (2020-01-10 22:55 UTC)

<p>Thank you Prof <a class="mention" href="/u/lassoan">@lassoan</a> . That would be great. I will share a CBCT file and it is not very good but these are the ones we get.</p>
<p>It would be great if we can try various methods to get the best segmentation and perhaps the cook up the best recipe for the teeth  and also i am very much interested in AI model training but i would need help with AI training.</p>

---

## Post #5 by @lassoan (2020-01-11 17:22 UTC)

<p>There is no such thing as a perfect segmentation, it can only be good enough for a specific use. What is your use case? What would you like to segment on the image is exactly? What accuracy do you need? What is particularly important to be accurate and what parts are not that important?</p>

---

## Post #6 by @manjula (2020-01-11 20:51 UTC)

<p>We want to segment the roots of the teeth. We want to measure root resorption of teeth pre and post orthodontic treatment.  Not very happy with the apex part.</p>
<p>I tried with ITK-SNAP and at the apex it spills in to the adjacent bone and i think of course it is because of the quality of the CBCT but trying to get it to work the best.  And with slicer we will have to do teeth by teeth.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="IlFBkkJIIr0" data-video-title="dental" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=IlFBkkJIIr0" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/IlFBkkJIIr0/maxresdefault.jpg" title="dental" width="" height="">
  </a>
</div>

<p>We find it very particular difficult to segment out the root apexes of teeth.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0ddcbc7aa9d4bb836e3a8d59bd678d9d28c8d7c1.png" data-download-href="/uploads/short-url/1YD8cJ6GlTXAZfe7rlimw1Puq0V.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0ddcbc7aa9d4bb836e3a8d59bd678d9d28c8d7c1_2_689x240.png" alt="1" data-base62-sha1="1YD8cJ6GlTXAZfe7rlimw1Puq0V" width="689" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0ddcbc7aa9d4bb836e3a8d59bd678d9d28c8d7c1_2_689x240.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0ddcbc7aa9d4bb836e3a8d59bd678d9d28c8d7c1_2_1033x360.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0ddcbc7aa9d4bb836e3a8d59bd678d9d28c8d7c1.png 2x" data-dominant-color="5C5A54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1290×449 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @manjula (2020-01-12 19:20 UTC)

<p>Also is there a way to measure the volume difference between at a ROI from two CT scans from two time points ?</p>
<p>For example CBCT - Time 01 (Pre OP)  and CBCT time 02 ( PostOp) will be registered and then measure the area of bone resoprtion in a ROI with out segmenting ?</p>
<p>So the segmentation problem will not come ?</p>

---

## Post #8 by @manjula (2020-01-14 14:27 UTC)

<p>Dear Prof Lasso, I have crop the volume of one of the cases that i would like to segment.</p>
<p>However i find it extremely difficult to segment out the teeth from the mandible. We want to be able to segment out selected teeth from the mandible.</p>
<p>I have shared the link to the data with you. If you have time can you help us with this in finding a better way to segment the teeth ?  We need accurate segmentation of roots of the teeth.</p>

---

## Post #9 by @lassoan (2020-01-14 15:41 UTC)

<aside class="quote no-group" data-username="manjula" data-post="8" data-topic="9775">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>I have shared the link to the data with you. If you have time can you help us with this in finding a better way to segment the teeth ? We need accurate segmentation of roots of the teeth.</p>
</blockquote>
</aside>
<p>I’ve checked this and found that all teeth can be quite quickly and accurately segmented  at once by the following steps:</p>
<ol>
<li>Set editable intensity range from about 1880 to maximum using Threshold effect, “Use for masking”</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abe1ef3a4fba2bd6e1fb12fb93e2a6240cd88b9f.jpeg" data-download-href="/uploads/short-url/owxI0DZMnPEQGISQGHiaT4vgpY3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abe1ef3a4fba2bd6e1fb12fb93e2a6240cd88b9f_2_690x438.jpeg" alt="image" data-base62-sha1="owxI0DZMnPEQGISQGHiaT4vgpY3" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abe1ef3a4fba2bd6e1fb12fb93e2a6240cd88b9f_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abe1ef3a4fba2bd6e1fb12fb93e2a6240cd88b9f_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abe1ef3a4fba2bd6e1fb12fb93e2a6240cd88b9f_2_1380x876.jpeg 2x" data-dominant-color="AFAEB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1696×1078 381 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>Using “Paint” effect, painta few strokes in the mandible and each tooth with different segment. You need to experiment to find what is the minimum amount that you need to paint and where, but probably it is enough to paint one stroke that goes down to the tip of the root (it is easy to do, as we are in threshold paint mode, so cannot paint outside the tooth) and add seeds where the tooth is in contact with another tooth. You can add seeds later, but updates in watershed transform take time, so it is better to provide enough seeds on the first try.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9941c6214c574f1dfc9e89ba5ff7d8ee6ef49d10.jpeg" data-download-href="/uploads/short-url/lRLYkeRyumUwtRNLl9raW8AAe0U.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9941c6214c574f1dfc9e89ba5ff7d8ee6ef49d10_2_690x438.jpeg" alt="image" data-base62-sha1="lRLYkeRyumUwtRNLl9raW8AAe0U" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9941c6214c574f1dfc9e89ba5ff7d8ee6ef49d10_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9941c6214c574f1dfc9e89ba5ff7d8ee6ef49d10_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9941c6214c574f1dfc9e89ba5ff7d8ee6ef49d10_2_1380x876.jpeg 2x" data-dominant-color="ADADB2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1696×1078 359 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Use “Watershed” effect (provided by SegmentEditorExtraEffects extension) with object scale = 0.2, then click Initialize and Show 3D</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fb7c08ca11fdf462ec9d43766a3fb0c7ef7a172.jpeg" data-download-href="/uploads/short-url/kvnXR7eOY0l5nTwmiZXiJKEPF9U.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fb7c08ca11fdf462ec9d43766a3fb0c7ef7a172_2_690x438.jpeg" alt="image" data-base62-sha1="kvnXR7eOY0l5nTwmiZXiJKEPF9U" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fb7c08ca11fdf462ec9d43766a3fb0c7ef7a172_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fb7c08ca11fdf462ec9d43766a3fb0c7ef7a172_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fb7c08ca11fdf462ec9d43766a3fb0c7ef7a172_2_1380x876.jpeg 2x" data-dominant-color="AEABB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1696×1078 410 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>Add more seeds as needed. If you find that your initial seeds did not give correct results then add more seeds. For example, if boundary between two teeth are not in the correct place then paint on both sides at the boundary with the correct color. If you get better with initial placement of the seeds then this should not be necessary. When results look good, go back to Watershed effect and click “Apply”.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d85d49aa9b96ac74e0844f209211c706e55ffb6.jpeg" data-download-href="/uploads/short-url/b3NuJx3H9E4K9rpfgou1Xj3NDYa.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d85d49aa9b96ac74e0844f209211c706e55ffb6_2_690x438.jpeg" alt="image" data-base62-sha1="b3NuJx3H9E4K9rpfgou1Xj3NDYa" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d85d49aa9b96ac74e0844f209211c706e55ffb6_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d85d49aa9b96ac74e0844f209211c706e55ffb6_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d85d49aa9b96ac74e0844f209211c706e55ffb6_2_1380x876.jpeg 2x" data-dominant-color="ABA9B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1696×1078 403 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="5">
<li>Touch up the segmentation. Near very dense areas (typically when crown of two teeth are in contact), blooming artifact may occur in the CT, resulting in connection between teeth. Probably the easiest to cut off those connective pieces using Scissors effect in 3D view.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b80b193aa09338fe49f4a694e9ee3acfa3444a34.jpeg" data-download-href="/uploads/short-url/qg7DfD0tgruwTbRSlAca8JJfBg8.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b80b193aa09338fe49f4a694e9ee3acfa3444a34_2_690x336.jpeg" alt="image" data-base62-sha1="qg7DfD0tgruwTbRSlAca8JJfBg8" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b80b193aa09338fe49f4a694e9ee3acfa3444a34_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b80b193aa09338fe49f4a694e9ee3acfa3444a34.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b80b193aa09338fe49f4a694e9ee3acfa3444a34.jpeg 2x" data-dominant-color="9182BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">926×452 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Notes:</p>
<ul>
<li>This workflow segments all teeth at once and it takes 10 minutes for me, but if complete a number of cases then I would expect it would go down to about 5 minutes.</li>
<li>You can make Watershed updates faster and more accurate if you crop the volume to the minimum necessary size and enable “isotropic spacing” option.</li>
</ul>
<aside class="quote no-group" data-username="manjula" data-post="7" data-topic="9775">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Also is there a way to measure the volume difference between at a ROI from two CT scans from two time points ? For example CBCT - Time 01 (Pre OP) and CBCT time 02 ( PostOp) will be registered and then measure the area of bone resoprtion in a ROI with out segmenting ?</p>
</blockquote>
</aside>
<p>You might be able to segment one image and then compute segmentation on the other image by warping the segmentation based on the transformation that you computed using registration (e.g., using SlicerElastix). However, probably it is more accurate if you rigidly register the images and, copy the complete segmentation from the first image to the second, shrink all the segments using Margin effect and use those as input for Watershed effect. This may or may not be faster than doing the segmentation from scratch. You need to practice and see which one is faster and easier.</p>

---

## Post #10 by @manjula (2020-01-14 19:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="9775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>1880 to maximum using Threshold effect, “Use for masking”</p>
</blockquote>
</aside>
<p>Dear Prof Lasso,</p>
<p>Thank you for your kind help. I will try with this to master this. !</p>

---

## Post #11 by @Reham_Hassan (2020-11-13 20:03 UTC)

<p>Hi,</p>
<p>whenever i try to use the method u described by using thresholding and paint then the watershed tool i end up with the teeth partially embedded in the bone, i would also want to know how can i further extract the pulp space after segmenting teeth</p>
<p>im attaching a screen shot of my final result</p>
<p>would really appreciate your help <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/625b675a92c1f7579897c9db69afe613e59a7351.jpeg" data-download-href="/uploads/short-url/e26CFrcDEAtxslVKFUr4CDLKAnf.jpeg?dl=1" title="Screen Shot 2020-11-13 at 9.53.14 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/625b675a92c1f7579897c9db69afe613e59a7351_2_690x431.jpeg" alt="Screen Shot 2020-11-13 at 9.53.14 PM" data-base62-sha1="e26CFrcDEAtxslVKFUr4CDLKAnf" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/625b675a92c1f7579897c9db69afe613e59a7351_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/625b675a92c1f7579897c9db69afe613e59a7351_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/625b675a92c1f7579897c9db69afe613e59a7351_2_1380x862.jpeg 2x" data-dominant-color="C8C9DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-11-13 at 9.53.14 PM</span><span class="informations">2560×1600 384 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @juangdiosa (2020-11-13 21:15 UTC)

<p>Hi Reham Hassan</p>
<p>The thresholding is highly depended to the patient and equipment. In my experience I have found values around 700 to 1400 units are good range to have teeth without include too much around bone tissues . I suggest you increase the number of slices the much as possible to have a better segmentation results [you can do it in crop module, when you create the ROI], also use island tool to remove undesired structures and help to reduce the time need it to use paint an erase tools.</p>
<p>If you used threshold tool to include mainly the teeth structure, you will have the pulp region. You can extract the pulp using creating a new segment and the boolean operations or using grow from seed tool too. Another strategy is to export the tooth stl and in Meshlab remove the enamel and dentine structure, inside you will have the pulp.</p>
<p>I hope this suggestions help you</p>
<p>Regards</p>
<p>Juan G. Diosa</p>

---

## Post #13 by @Reham_Hassan (2020-11-14 10:12 UTC)

<p>thank you for your reply <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
the maximum threshold range of the volume im using is 253<br>
i have tried different ranges to select only teeth, uploading a screenshot of the threshold range im using, do u have a better suggestion</p>
<p>also i have cropped the skull partially to include the teeth i want, could u please mark on the other screenshot, what do u mean by increasing the number of the slices</p>
<p>i really appreciate your help<br>
and the time u took to reply to my inquiry</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/049af6fe5856e2888cdfad488edd4b094fdf438a.jpeg" data-download-href="/uploads/short-url/EJV4iMe7LavrrBiYsRpovVsUT8.jpeg?dl=1" title="Screen Shot 2020-11-14 at 11.50.13 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/049af6fe5856e2888cdfad488edd4b094fdf438a_2_690x431.jpeg" alt="Screen Shot 2020-11-14 at 11.50.13 AM" data-base62-sha1="EJV4iMe7LavrrBiYsRpovVsUT8" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/049af6fe5856e2888cdfad488edd4b094fdf438a_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/049af6fe5856e2888cdfad488edd4b094fdf438a_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/049af6fe5856e2888cdfad488edd4b094fdf438a_2_1380x862.jpeg 2x" data-dominant-color="757574"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-11-14 at 11.50.13 AM</span><span class="informations">2560×1600 301 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fb6fb130f84b5985715524ff8df6dc175acd0fe.jpeg" data-download-href="/uploads/short-url/kvmjobysZFbU8YJaR6OtiqMfOVw.jpeg?dl=1" title="Screen Shot 2020-11-14 at 12.07.28 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fb6fb130f84b5985715524ff8df6dc175acd0fe_2_690x431.jpeg" alt="Screen Shot 2020-11-14 at 12.07.28 PM" data-base62-sha1="kvmjobysZFbU8YJaR6OtiqMfOVw" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fb6fb130f84b5985715524ff8df6dc175acd0fe_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fb6fb130f84b5985715524ff8df6dc175acd0fe_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fb6fb130f84b5985715524ff8df6dc175acd0fe_2_1380x862.jpeg 2x" data-dominant-color="94949B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-11-14 at 12.07.28 PM</span><span class="informations">2560×1600 436 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @juangdiosa (2020-11-18 13:27 UTC)

<p>Hi<br>
A good strategy to identify the proper threshold range is begging with high values and click in apply, then to reduce the min value  a little bit until you include what you want. Use the 3D representation to check if you have everything you need. I think the values you have now are to low because is including no related tissues. This video explain better what I am talking about at 2:20 min <a href="https://www.youtube.com/watch?v=Uht6Fwtr9hE&amp;t=261s" class="inline-onebox" rel="noopener nofollow ugc">How to segment multiple vertebrae in spine CT for 3D printing - YouTube</a></p>
<p>To increase the number of slices you have to modify the spacing scale using numbers below to 1, check the volume information to know the distance you in the file and what distance between slices you will have in the ROI. Check this video at 0:30 min to know how to do it</p><div class="youtube-onebox lazy-video-container" data-video-id="BJoIexIvtGo" data-video-title="Whole heart segmentation from cardiac CT in 10 minutes" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=BJoIexIvtGo" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/BJoIexIvtGo/maxresdefault.jpg" title="Whole heart segmentation from cardiac CT in 10 minutes" width="" height="">
  </a>
</div>

<p>Regards</p>

---

## Post #15 by @muratmaga (2020-11-18 17:59 UTC)

<aside class="quote no-group" data-username="Reham_Hassan" data-post="13" data-topic="9775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/reham_hassan/48/7824_2.png" class="avatar"> Reham_Hassan:</div>
<blockquote>
<p>i have tried different ranges to select only teeth, uploading a screenshot of the threshold range im using, do u have a better suggestion</p>
</blockquote>
</aside>
<p>Your displayed value range for threshold in the screenshot starts 103.22 ends at 140.92. Teeth is the most dense material in the skull. Their intensity values tend to be close to the maximum range. Your threshold range is picking up everything but the teeth. So try something like 140-255 to make sure you are including the upper end of the intensity range.</p>

---

## Post #16 by @lassoan (2020-11-18 18:28 UTC)

<aside class="quote no-group" data-username="Reham_Hassan" data-post="13" data-topic="9775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/reham_hassan/48/7824_2.png" class="avatar"> Reham_Hassan:</div>
<blockquote>
<p>the maximum threshold range of the volume im using is 253</p>
</blockquote>
</aside>
<p>This may indicate that the CT has been exported incorrectly (e.g., as a series of JPEG images). If intensity values in the image are in the range of 0-255 then it means that you will have more difficulty with differentiating tissue types as you would have with the properly exported images (which have about 10x larger dynamic range).</p>
<p>Where the images are from? How were they exported?</p>

---

## Post #17 by @HAFIZAL (2020-11-23 15:21 UTC)

<p>Hi there, I just want to share how I did tooth segmentation.<br>
I basically used  level tracing with paint and eraser to highlight which area I wanted especially for enamel and dentine.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91aaa70089a0be558e8710c566a0119d8ab4ca63.jpeg" data-download-href="/uploads/short-url/kMCQXw5Zjn248rrpUSWbaiiNj7d.jpeg?dl=1" title="Screenshot (385)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91aaa70089a0be558e8710c566a0119d8ab4ca63_2_690x387.jpeg" alt="Screenshot (385)" data-base62-sha1="kMCQXw5Zjn248rrpUSWbaiiNj7d" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91aaa70089a0be558e8710c566a0119d8ab4ca63_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91aaa70089a0be558e8710c566a0119d8ab4ca63_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91aaa70089a0be558e8710c566a0119d8ab4ca63.jpeg 2x" data-dominant-color="797A81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (385)</span><span class="informations">1366×768 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Next, I use fill between slices tool for root structure.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/034cfd3e02ba9b288bc8dda5a5ad9261c5c6d51b.jpeg" data-download-href="/uploads/short-url/tcnCPKRmmpp73m7Q8BppGMs1qH.jpeg?dl=1" title="Screenshot (387)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/034cfd3e02ba9b288bc8dda5a5ad9261c5c6d51b_2_690x387.jpeg" alt="Screenshot (387)" data-base62-sha1="tcnCPKRmmpp73m7Q8BppGMs1qH" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/034cfd3e02ba9b288bc8dda5a5ad9261c5c6d51b_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/034cfd3e02ba9b288bc8dda5a5ad9261c5c6d51b_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/034cfd3e02ba9b288bc8dda5a5ad9261c5c6d51b.jpeg 2x" data-dominant-color="707176"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (387)</span><span class="informations">1366×768 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Finally, I smooth it with smoothing tool. Here I use median mode with kernel size 1.00 mm size reduction.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0701ca873a0b8a05d8855a371501d1476af6c0c2.jpeg" data-download-href="/uploads/short-url/ZZb90tJdARRsojJstWEXAjgpa2.jpeg?dl=1" title="Screenshot (386)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0701ca873a0b8a05d8855a371501d1476af6c0c2_2_690x387.jpeg" alt="Screenshot (386)" data-base62-sha1="ZZb90tJdARRsojJstWEXAjgpa2" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0701ca873a0b8a05d8855a371501d1476af6c0c2_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0701ca873a0b8a05d8855a371501d1476af6c0c2_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0701ca873a0b8a05d8855a371501d1476af6c0c2.jpeg 2x" data-dominant-color="86868B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (386)</span><span class="informations">1366×768 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>thank you.</p>

---

## Post #18 by @Reham_Hassan (2020-12-15 09:36 UTC)

<p>Thank you Dr Murat, i have tried this range you recommended (140-255) but ended up by selecting only enamel</p>

---

## Post #19 by @Reham_Hassan (2020-12-15 09:55 UTC)

<p>Hi,</p>
<p>yes i believe there must be a problem with the Micro CT images, because i tried every method mentioned here in trial to segment teeth, to some extent i have better results with segmenting the brain, sharing screenshots but have been totally failing with teeth<br>
i have been using the image stacks module of the slicerMorph<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82819e9c60c7184ce46429631d9e7a053bd7e1e3.jpeg" data-download-href="/uploads/short-url/iCvMlBxt1Gp2Iz8mwvfKrxukymD.jpeg?dl=1" title="Screen Shot 2020-12-10 at 9.12.23 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82819e9c60c7184ce46429631d9e7a053bd7e1e3_2_690x431.jpeg" alt="Screen Shot 2020-12-10 at 9.12.23 PM" data-base62-sha1="iCvMlBxt1Gp2Iz8mwvfKrxukymD" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82819e9c60c7184ce46429631d9e7a053bd7e1e3_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82819e9c60c7184ce46429631d9e7a053bd7e1e3_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82819e9c60c7184ce46429631d9e7a053bd7e1e3_2_1380x862.jpeg 2x" data-dominant-color="939399"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-12-10 at 9.12.23 PM</span><span class="informations">2560×1600 351 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #20 by @muratmaga (2020-12-15 17:37 UTC)

<aside class="quote no-group" data-username="Reham_Hassan" data-post="18" data-topic="9775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/reham_hassan/48/7824_2.png" class="avatar"> Reham_Hassan:</div>
<blockquote>
<p>recommended (140-255) but ended up by selecting only enamel</p>
</blockquote>
</aside>
<p>I only suggest looking at the screenshot. You may bring the lower end lower a bit, and see if it helps. But the issue as <a class="mention" href="/u/lassoan">@lassoan</a> said is that 8 bit data range doesn’t give you a lot to work with. The root of the tooth and the bone they are embedded in has similar densities so it is harder to find an intensity value that will pick only one but not the other. If you can get your scan reconstructed as 16 bit, this may help some. Alternatively to you can try to use the <code>Local Threshold</code> module so that the segmentation does so leak so much into the alveolar region (I think).</p>

---

## Post #21 by @lassoan (2020-12-15 20:22 UTC)

<aside class="quote no-group" data-username="Reham_Hassan" data-post="18" data-topic="9775" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/reham_hassan/48/7824_2.png" class="avatar"> Reham_Hassan:</div>
<blockquote>
<p>Thank you Dr Murat, i have tried this range you recommended (140-255) but ended up by selecting only enamel</p>
</blockquote>
</aside>
<p>Unlike clinical scanners, micro-CT scanners are often not calibrated (well), so you cannot rely on absolute image intensity ranges. Of course, density of bone and teeth depends on the individual and the imaging is never perfect (there is always some noise, blurring, partial volume effect, etc.), so if structures have similar intensity then you may not be able to segment based on only a global threshold. You may then need to use region-growing based approaches (e.g., Grow from seeds, Watershed), or just manually segment a few slices and interpolate between them using “Fill between slices” effect.</p>

---
