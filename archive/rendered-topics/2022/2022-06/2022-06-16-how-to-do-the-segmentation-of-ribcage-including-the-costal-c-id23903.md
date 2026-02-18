# How to do the segmentation of ribcage including the Costal cartilage? 

**Topic ID**: 23903
**Date**: 2022-06-16
**URL**: https://discourse.slicer.org/t/how-to-do-the-segmentation-of-ribcage-including-the-costal-cartilage/23903

---

## Post #1 by @Monkeyking123 (2022-06-16 13:28 UTC)

<p>Hi everyone<br>
It is my first time using 3D slicer along with its tools, mainly for learning the segmentations of ribcages, and heart structures with the aforementioned tools and those in the extensive section(i.e Nvidia AIAA, wrap solidify and logical operator)</p>
<p>Our teacher told us 2 ways:</p>
<ol>
<li>
<p>Crop volume - Threshold - Segment editor (Scissors, Island, smoothing etc) then export files</p>
</li>
<li>
<p>Go to logical operators first and invert and apply. (Cancel bypass marking)<br>
Go to “Wrap solidify” - "Largest cavities, split cavities to about 10 mm) and create a new segment<br>
Go back to logical operators to invert back<br>
Go to Nvidia AIAA to find and delete the livers, spleen, tumors etc from the ribcage<br>
Do the rest of the segmenting as the 1st method</p>
</li>
</ol>
<p>I have tried both methods but got stuck since the requested ribcage is a perfect model</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bb134c826f705f5487aca31e0534b8d79fa6364.jpeg" data-download-href="/uploads/short-url/d596XFTeFeuUzqnt7ey3Nxsdr48.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb134c826f705f5487aca31e0534b8d79fa6364_2_230x500.jpeg" alt="image" data-base62-sha1="d596XFTeFeuUzqnt7ey3Nxsdr48" width="230" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb134c826f705f5487aca31e0534b8d79fa6364_2_230x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb134c826f705f5487aca31e0534b8d79fa6364_2_345x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb134c826f705f5487aca31e0534b8d79fa6364_2_460x1000.jpeg 2x" data-dominant-color="636D71"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1125×2436 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But, the ribcage that I segmented lacks the cartilage and the “Island” section seems to become<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1c014386ee698ba6f004bd1cccaec292b8534e0.png" data-download-href="/uploads/short-url/wd4XpfjHYQ2HN1JilFLoib4lJXG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1c014386ee698ba6f004bd1cccaec292b8534e0_2_508x500.png" alt="image" data-base62-sha1="wd4XpfjHYQ2HN1JilFLoib4lJXG" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1c014386ee698ba6f004bd1cccaec292b8534e0_2_508x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1c014386ee698ba6f004bd1cccaec292b8534e0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1c014386ee698ba6f004bd1cccaec292b8534e0.png 2x" data-dominant-color="9A9ECA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">569×559 64.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7c3c4caa43c4867017bb72f83eb298b0af34e2f.jpeg" data-download-href="/uploads/short-url/svcrQzHQyQBQZryuIAS8xLrKt0r.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7c3c4caa43c4867017bb72f83eb298b0af34e2f_2_594x499.jpeg" alt="image" data-base62-sha1="svcrQzHQyQBQZryuIAS8xLrKt0r" width="594" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7c3c4caa43c4867017bb72f83eb298b0af34e2f_2_594x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7c3c4caa43c4867017bb72f83eb298b0af34e2f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7c3c4caa43c4867017bb72f83eb298b0af34e2f.jpeg 2x" data-dominant-color="8997AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">723×608 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Question:</p>
<ol>
<li>What is the best way to do a model of the ribcage and are there places to be aware of</li>
<li>Is there an automatic ribcage segmentation tool or is that the 2 method that was mentioned above e</li>
<li>What steps might be missing in the ribcaged that was tried?</li>
</ol>
<p>Thank you for the help and tips!</p>

---

## Post #2 by @mau_igna_06 (2022-06-16 13:46 UTC)

<p>Did you try localThreshold on segmentEditor extra effects? And the some scissors maybe?</p>

---

## Post #3 by @Monkeyking123 (2022-06-16 15:55 UTC)

<p>What’s the difference between the Normal Threshold and localThreshold?</p>

---

## Post #4 by @mau_igna_06 (2022-06-16 16:02 UTC)

<p>LocalThreshold uses a combination of threshold and region growing</p>

---

## Post #5 by @Monkeyking123 (2022-06-16 19:40 UTC)

<p>Hi!<br>
I have a question on the process of Ribcage segmentation.<br>
Given the picture below(haven’t completed yet), there are some gaps in the ribs (Left side) as seen which are attached to the sternum</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f50a184134d181a6e52a3219a54f5abfe9c3f155.png" data-download-href="/uploads/short-url/yXIBHJuXnFTB5wYYAsmqtTt5wIB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f50a184134d181a6e52a3219a54f5abfe9c3f155_2_499x500.png" alt="image" data-base62-sha1="yXIBHJuXnFTB5wYYAsmqtTt5wIB" width="499" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f50a184134d181a6e52a3219a54f5abfe9c3f155_2_499x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f50a184134d181a6e52a3219a54f5abfe9c3f155.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f50a184134d181a6e52a3219a54f5abfe9c3f155.png 2x" data-dominant-color="9198B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">569×570 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2e4cd62e49784795154959701193c7e1fc09947.jpeg" alt="image" data-base62-sha1="pwzcaUgQqAwekQynnUDhurzyJfN" width="617" height="494"></p>
<p>Question:</p>
<ol>
<li>Are there tools that can be used to fill in the gaps of the ribs (Extensions etc) and how should I do it</li>
<li>I was trying to see if Nvidia AIAA can work to segment out the liver and tumors but it shows an error message so I want to ask if there is a way to finetune the ribcage to this</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a6049fd9b026375ae8dcd7460e1547cb8de54ef.png" alt="image" data-base62-sha1="1tN4wzQb8vX2iIv9KQLVcqdg4X5" width="445" height="339"></p>
<p>Thanks very much!</p>

---

## Post #6 by @lassoan (2022-06-17 18:44 UTC)

<p>Segmentation of ribs is usually an easy task, so even simple thresholding may suffice, but depending on what you need exactly, you may need to use additional tools.</p>
<p>What is your end goal? Visualization, quantification (what do you want to measure?), 3D printing (is it OK if the cancellous region inside the bones are hollow)? Do you need separate the ribs from each other or from vertebrae? Are there contrasted vessels in your CT images?</p>

---

## Post #7 by @Monkeyking123 (2022-06-17 19:09 UTC)

<p>Using the aforementioned models for 3D printing<br>
We need to keep the ribcage structure as following<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7ad1f9567843d5d1e55fbe0d66324e62b285db3.jpeg" data-download-href="/uploads/short-url/uLXzpW6FkoMZU9OUwVS8APCS2Xh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7ad1f9567843d5d1e55fbe0d66324e62b285db3_2_609x500.jpeg" alt="image" data-base62-sha1="uLXzpW6FkoMZU9OUwVS8APCS2Xh" width="609" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7ad1f9567843d5d1e55fbe0d66324e62b285db3_2_609x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7ad1f9567843d5d1e55fbe0d66324e62b285db3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7ad1f9567843d5d1e55fbe0d66324e62b285db3.jpeg 2x" data-dominant-color="D8E3D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">736×604 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bb134c826f705f5487aca31e0534b8d79fa6364.jpeg" data-download-href="/uploads/short-url/d596XFTeFeuUzqnt7ey3Nxsdr48.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb134c826f705f5487aca31e0534b8d79fa6364_2_230x500.jpeg" alt="image" data-base62-sha1="d596XFTeFeuUzqnt7ey3Nxsdr48" width="230" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb134c826f705f5487aca31e0534b8d79fa6364_2_230x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb134c826f705f5487aca31e0534b8d79fa6364_2_345x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb134c826f705f5487aca31e0534b8d79fa6364_2_460x1000.jpeg 2x" data-dominant-color="636D71"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1125×2436 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>*I was trying to use</p>
<ol>
<li>Logical Operators first to invert(Cancel bypass marking)</li>
<li>Warp Solidify and create a new segment by largest cavity</li>
<li>Allow bypass marking in Logical Operators and inverting back</li>
<li>NVidia AIAA to cancel out the liver, spleen, tumors etc</li>
<li>Then the Islands, smoothing etc</li>
</ol>
<p>But there are a few problems to solve:</p>
<p>(a) Accidentally cutting parts of the ribcage but the redo button can’t be pressed(can’t redo after a certain number)<br>
(b) Too much other elements other than the ribcage and using the “Island” function sometimes deletes the entire Ribcage<br>
(c) Slicer automatically shuts off when using Nvidia and gives this message when reopening:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13374d6081382dad4535c2639e634983ffc8b153.png" data-download-href="/uploads/short-url/2JZyv4AaWy8yaTkeEAmCOiW4WUr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13374d6081382dad4535c2639e634983ffc8b153_2_690x393.png" alt="image" data-base62-sha1="2JZyv4AaWy8yaTkeEAmCOiW4WUr" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13374d6081382dad4535c2639e634983ffc8b153_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13374d6081382dad4535c2639e634983ffc8b153_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13374d6081382dad4535c2639e634983ffc8b153_2_1380x786.png 2x" data-dominant-color="78767B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1728×985 98.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks!</p>

---

## Post #8 by @lassoan (2022-06-17 19:30 UTC)

<aside class="quote no-group" data-username="Monkeyking123" data-post="7" data-topic="23903">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/monkeyking123/48/15663_2.png" class="avatar"> Monkeyking123:</div>
<blockquote>
<p>NVidia AIAA to cancel out the liver, spleen, tumors etc</p>
</blockquote>
</aside>
<p>Do you need to segment any other structures than ribs, cartilage, and sternum? Do you need to separate the ribs from vertebrae?</p>
<p>How many segmentations do you need to do? Are there any time limits on the maximum segmentation time? Does the method have to be fully automatic? Are all the images acquired using the same imaging protocol?</p>
<p>What is the goal with 3D printing? Would like to create a phantom? 3D printing an entire ribcage requires special printer and/or splitting the model into several pieces. tThis is both time-consuming and expensive. It is much easier and cheaper to buy a ready-made phantom (e.g., from <a href="https://www.sawbones.com/">sawbones</a>) and get a CT scan of it.</p>

---

## Post #9 by @rbumm (2022-06-17 20:54 UTC)

<aside class="quote no-group" data-username="Monkeyking123" data-post="7" data-topic="23903">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/monkeyking123/48/15663_2.png" class="avatar"> Monkeyking123:</div>
<blockquote>
<p>NVidia AIAA to cancel out the liver, spleen, tumors etc</p>
</blockquote>
</aside>
<p>Please note that developers of NVIDIA-AIAA have changed their focus on working on MONAILabel so you can not expect to find ready to use solution for your task in NVIDIA-AIAA. It would probably make more sense from a mid-term perspective to use MONAILabel for that specific task.</p>

---
