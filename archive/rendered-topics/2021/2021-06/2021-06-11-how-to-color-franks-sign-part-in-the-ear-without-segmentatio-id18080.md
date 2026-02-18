# How to color Frank's sign part in the ear without segmentation

**Topic ID**: 18080
**Date**: 2021-06-11
**URL**: https://discourse.slicer.org/t/how-to-color-franks-sign-part-in-the-ear-without-segmentation/18080

---

## Post #1 by @abhijeet2410 (2021-06-11 14:44 UTC)

<p>Hello Everyone,</p>
<p>For my project, I need to color some part of ear in niffi images. Over that I am going to apply segementatio so that while training deep learning model, machine can easily understand which part must be  segementated based on colorful part of ear. How can I color the specific part without segementation?</p>

---

## Post #2 by @mikebind (2021-06-11 17:07 UTC)

<p>This approach does not make sense to me.  If you mark the part you want segmented with color and then train a deep learning model to segment that area, you will just be training it to segment out colored areas, which will be useless for images which have not already been colored.  Furthermore, the creation of the colored area, however you achieve it, is a type of segmentation, where the created segment corresponds to the colored area, so I’m not sure why you say you want to achieve this “without segmentation”.  In addition, for your training (assuming the learning is supervised) you will need correct segmentations for your deep learning model to compare its results to and learn from, so in this way you also can not possibly achieve your goal without segmentation.</p>

---

## Post #3 by @abhijeet2410 (2021-06-11 17:16 UTC)

<p>Hello Sir,</p>
<p>Greetings!!</p>
<p>Thank you very much for your reply. Even after doing segementation of very small part (frank sign) in entire 3 D Brain Niffti image, it does not predicted accurate segementation properly for test data after learning 3 D Unet model. I saw some brain image dataset. They color or increase the intensity of tumar part too maximize the results. I am planning to follow the same way. Can you suggest me how I color or increase intensity of frank sign on ear or any alterative you can suggest?.</p>

---

## Post #4 by @mikebind (2021-06-11 18:03 UTC)

<p>I am not an expert in deep learning approaches, but might it make sense to crop your volume so that the area of interest makes up a larger fraction of the total volume?  You could crop volumes a smaller block containing just the ear, train to find Frank’s sign within those volumes, and then if that is successful you could separately train another model to crop whole head volumes down to ear-containing subvolumes.  The final pipeline would then use the cropping network to generate a subvolume containing each ear, and then use the Frank’s sign finding network to identify whether the sign is present in that ear.  If you have enough examples of cases where the sign is present and not present, you might even be able to get away with training the ear subvolume classifier to just produce a yes/no answer about the presence of the sign without segmenting the sign itself.  Even if you would rather generate a segmentation in the end, I suspect that restricting the volume that you are sending to the model to focus on a smaller area of interest will be helpful.</p>

---

## Post #5 by @twloehfelm (2021-06-11 18:04 UTC)

<p>The ear lobe is such a small percentage of the overall volume of a 3D brain MRI that I suspect part of the problem is signal:noise for the specific training task. You might have more success splitting the work up into a few steps - train an ear segmentation and then try to limit your Frank sign algorithm to the presegmented ears. This is an approach that we take pretty regularly in segmentation problems in the abdomen - first segment the kidney, then train to characterize the renal lesion.</p>
<p>There may be other parts of the image (carotids and intracranial vessels) that contain useful information for your task which you’d be loosing with this approach, but it would help if your primary task is to isolate the earlobe.</p>

---

## Post #6 by @lassoan (2021-06-11 19:30 UTC)

<p>Yes, most probably if you let a network make decision based on the entire head MRI as input, then the network would pick up many other signs of cardiovascular disease or aging from various parts of the image and not from a small crease in the earlobe, cutting out a small ROI around the earlobe will certainly fix this.</p>
<p>Note that head MRI images are often acquired with a head coil, and noise reduction headphones, which may squish or deform the ear. Another issue is that the earlobe is often not completely visible in MRI scans. You might have better luck with CT scans, but even there you may have head immobilizers that deform the ear. Due to all these issues, it may be simpler to generate volume renderings of the ears and let a human decide in a few seconds if there is a crease in the ear or not, rather than spending several days or weeks to train a network. You can probably manually classify hundreds of images per hour, so in 1-2 days you can complete thousands of classifications. To set up a neural network to achieve the same performance and validate that its performance is comparable to a human would take at least several weeks. Therefore using “AI” for this task would just slow you down and distract you from answering the clinical question.</p>

---

## Post #7 by @abhijeet2410 (2021-06-14 04:56 UTC)

<p>Thank you very much for your response. I followed your approach but the<br>
results are not good. Now, I am focusing on pre segmented ear only (So that<br>
AI correctly predicts the frank sign part). My question is how do I color<br>
the frank sign part in the ear without segmentation?</p>
<p>Since, I am not focusing on 2 D image but 3 D brain Image. Therefore, there<br>
is no question of cropping it.</p>
<p>Can anyone please share a youtube link? I am beniger, I need youtube videos<br>
to understand it carefully.</p>

---

## Post #8 by @lassoan (2021-06-16 21:02 UTC)

<aside class="quote no-group" data-username="abhijeet2410" data-post="7" data-topic="18080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/abhijeet2410/48/11196_2.png" class="avatar"> abhijeet2410:</div>
<blockquote>
<p>My question is how do I color<br>
the frank sign part in the ear without segmentation?</p>
</blockquote>
</aside>
<p>Coloring and segmentation mean the same thing. If by coloring you mean volume rendering then you can check out the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded">examples in the script repository</a>.</p>
<aside class="quote no-group" data-username="abhijeet2410" data-post="7" data-topic="18080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/abhijeet2410/48/11196_2.png" class="avatar"> abhijeet2410:</div>
<blockquote>
<p>Since, I am not focusing on 2 D image but 3 D brain Image. Therefore, there<br>
is no question of cropping it.</p>
</blockquote>
</aside>
<p>In Slicer, you can crop 2D images as easily as 3D images.</p>
<aside class="quote no-group" data-username="abhijeet2410" data-post="7" data-topic="18080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/abhijeet2410/48/11196_2.png" class="avatar"> abhijeet2410:</div>
<blockquote>
<p>Can anyone please share a youtube link? I am beniger, I need youtube videos<br>
to understand it carefully.</p>
</blockquote>
</aside>
<p>You can find lots of training material on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training">training page</a>, and there are many videos on the <a href="https://www.youtube.com/user/PerkLabResearch/videos">PerkLab’s channel</a> and you can also find lots of additional videos by searching on google and youtube.</p>

---
