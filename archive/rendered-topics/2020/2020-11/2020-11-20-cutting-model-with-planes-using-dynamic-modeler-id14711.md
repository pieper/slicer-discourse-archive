---
topic_id: 14711
title: "Cutting Model With Planes Using Dynamic Modeler"
date: 2020-11-20
url: https://discourse.slicer.org/t/14711
---

# Cutting model with planes using dynamic modeler

**Topic ID**: 14711
**Date**: 2020-11-20
**URL**: https://discourse.slicer.org/t/cutting-model-with-planes-using-dynamic-modeler/14711

---

## Post #1 by @Tomek (2020-11-20 15:21 UTC)

<p>I am relatively new to slicer beginning to test out the features to use in my research project. So far I was able to get by with information I found in this forum or the wiki. But I got to a point that I am stuck. My goal is to divide a 3D model of periatrial fat into regions with regard to the adjacent left atrial wall by drawing planes and calculate the partial volumes.</p>
<p>Operating system: Win 10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: cutting a 3D Model with multiple planes through the dynamic modeler feature to create separate model parts.<br>
Actual behavior: nothing seems to be happening after selecting model node and plane nodes; trying different parameter and output node options.<br>
This is how it looks:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68aee887c52b58d9b1978e5f0afaa08a22e2597f.png" data-download-href="/uploads/short-url/eW4ozi3yPHiVpEqoITtXilxkohN.png?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68aee887c52b58d9b1978e5f0afaa08a22e2597f_2_690x353.png" alt="Screenshot_1" data-base62-sha1="eW4ozi3yPHiVpEqoITtXilxkohN" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68aee887c52b58d9b1978e5f0afaa08a22e2597f_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68aee887c52b58d9b1978e5f0afaa08a22e2597f_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68aee887c52b58d9b1978e5f0afaa08a22e2597f.png 2x" data-dominant-color="9898BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1331×681 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would really appreciate any help in this regard to point out any things I am missing.</p>

---

## Post #2 by @muratmaga (2020-11-20 15:44 UTC)

<p>By default Dynamic modeler is giving the output as the same color as the original model. So it might be working fine and you might not be noticing anything until you actually go to Data module and check the output and change the colors.</p>
<p>Right after the apply the cut,  it looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a1caeb5af30b708cc6ec2356adee67e0738350a.jpeg" data-download-href="/uploads/short-url/hqfHBpF6mb9dZIDyJOUnaaAaErM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a1caeb5af30b708cc6ec2356adee67e0738350a_2_577x500.jpeg" alt="image" data-base62-sha1="hqfHBpF6mb9dZIDyJOUnaaAaErM" width="577" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a1caeb5af30b708cc6ec2356adee67e0738350a_2_577x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a1caeb5af30b708cc6ec2356adee67e0738350a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a1caeb5af30b708cc6ec2356adee67e0738350a.jpeg 2x" data-dominant-color="94939C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">720×623 84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
But when I set the colors of different cuts, i can see them (you can see the original model bleeding through the cuts as yellow):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5abea32c4e2edbf8b4974389b97af2d1c423e495.jpeg" data-download-href="/uploads/short-url/cWLpuaHjTsk1oUavWT1UlE0H9qZ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5abea32c4e2edbf8b4974389b97af2d1c423e495_2_690x328.jpeg" alt="image" data-base62-sha1="cWLpuaHjTsk1oUavWT1UlE0H9qZ" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5abea32c4e2edbf8b4974389b97af2d1c423e495_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5abea32c4e2edbf8b4974389b97af2d1c423e495_2_1035x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5abea32c4e2edbf8b4974389b97af2d1c423e495_2_1380x656.jpeg 2x" data-dominant-color="5D6072"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1726×822 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Tomek (2020-11-20 16:02 UTC)

<p>Thank you very much for your answer. You are right about the color behavior of the models. The models are generated in the Data section but changing colors does not yield a result as in your case, unfortunately.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b25da6057d87a5ff7d49606829af5298bafec2c.png" data-download-href="/uploads/short-url/1AClON9EoO5v17lcUEu6Now7IPq.png?dl=1" title="data view" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b25da6057d87a5ff7d49606829af5298bafec2c_2_690x345.png" alt="data view" data-base62-sha1="1AClON9EoO5v17lcUEu6Now7IPq" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b25da6057d87a5ff7d49606829af5298bafec2c_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b25da6057d87a5ff7d49606829af5298bafec2c_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b25da6057d87a5ff7d49606829af5298bafec2c_2_1380x690.png 2x" data-dominant-color="C1C2D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">data view</span><span class="informations">1922×962 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6c00b36fc8c6b4b4fbfa2e0f6ce26a506835b1b.png" data-download-href="/uploads/short-url/smdZrP8GMDQMmehcruwu9L3tSzx.png?dl=1" title="settings fat" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6c00b36fc8c6b4b4fbfa2e0f6ce26a506835b1b_2_690x318.png" alt="settings fat" data-base62-sha1="smdZrP8GMDQMmehcruwu9L3tSzx" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6c00b36fc8c6b4b4fbfa2e0f6ce26a506835b1b_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6c00b36fc8c6b4b4fbfa2e0f6ce26a506835b1b_2_1035x477.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6c00b36fc8c6b4b4fbfa2e0f6ce26a506835b1b_2_1380x636.png 2x" data-dominant-color="BDBED0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">settings fat</span><span class="informations">1928×890 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> .</p>

---

## Post #4 by @smrolfe (2020-11-20 17:37 UTC)

<p>Have you tried checking the properties of the output models (Model_2 and Model_3)? This might help narrow down the issue. In the Models menu under ‘Information’ you can check the number of points and cells.</p>

---

## Post #5 by @Tomek (2020-11-20 17:59 UTC)

<p>Thank you for your input. I checked the properties of my models, strangely the 3D Fat model I was using had no Information (blank fields) the same was true for the generated Model2, Model3.<br>
I loaded my fat model .vtk again (which than displayed properties values) and again used the dynamic modeler (trying all possible settings like union, intersection…) to generate the new models, with the same result (properties remain blank / models not visible)</p>

---

## Post #6 by @muratmaga (2020-11-20 18:30 UTC)

<p>You can check the log file (Ctrl + 0) to see if there are any errors generated by the module. Alternatively, try other modes of operation and see if it is unique to the difference mode.</p>

---

## Post #7 by @Tomek (2020-11-20 19:13 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="4" data-topic="14711" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>Have you tried checking the properties of the output models (Model_2 and Model_3)? This might help narrow down the issue. In the Models menu under ‘Information’ you can check the number of points and cells.</p>
</blockquote>
</aside>
<p>I found the problem with your help. I suppose the problem somehow was that my first model had a problem with the “properties being missing”. After loading it again, at first I did not delete my “plane cut”. But after going through the whole process again (loading .vtk model and creating new planes and a new “plane cut” in the dynamic modeler, it worked.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92596ae9eb290f82392c83f15204645c9043670d.jpeg" data-download-href="/uploads/short-url/kSFhNwLHcZ3xUQC8Nzza4jC9TD7.jpeg?dl=1" title="Screenshot done" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92596ae9eb290f82392c83f15204645c9043670d_2_344x196.jpeg" alt="Screenshot done" data-base62-sha1="kSFhNwLHcZ3xUQC8Nzza4jC9TD7" width="344" height="196" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92596ae9eb290f82392c83f15204645c9043670d_2_344x196.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92596ae9eb290f82392c83f15204645c9043670d_2_516x294.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92596ae9eb290f82392c83f15204645c9043670d_2_688x392.jpeg 2x" data-dominant-color="8F86B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot done</span><span class="informations">1196×681 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you both.</p>

---
