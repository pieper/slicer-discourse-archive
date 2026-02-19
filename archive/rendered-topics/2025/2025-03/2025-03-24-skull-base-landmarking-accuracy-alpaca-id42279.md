---
topic_id: 42279
title: "Skull Base Landmarking Accuracy Alpaca"
date: 2025-03-24
url: https://discourse.slicer.org/t/42279
---

# Skull base landmarking accuracy ALPACA

**Topic ID**: 42279
**Date**: 2025-03-24
**URL**: https://discourse.slicer.org/t/skull-base-landmarking-accuracy-alpaca/42279

---

## Post #1 by @ThomasVanParys (2025-03-24 12:24 UTC)

<p>Hello,</p>
<p>I have created ~100 3D surface models of male and female human skulls from the NMDID. I aim to quantify sexual dimorphism in size and shape:</p>
<ul>
<li>For size, I have calculated Endocranial Volume (ECV, cm3).</li>
<li>For shape, I want to use a combination of fixed single Lm and semiLM patches at the basicranium.</li>
</ul>
<p>I need adequate landmarking coverage, but I only want landmarks that quantify variation at the basicranium. I am attempting to use the <em>SemiLMPatch</em> function, and will merge all landmarks (see photos below). The patches are as triangles, and struggles to stay projected at the surface: does anyone have any suggestions to make this easier?<br>
Does anyone have advice to maintain accuracy here, as I do not want to manually landmark each specimen, so <em>ALPACA</em> is being considered, but the landmark alignment seemed slightly ‘off’ during a first run with the template.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2fd5468774696f8764ac1fff7c9dc9f8c4e1a75.jpeg" data-download-href="/uploads/short-url/pxpKgeLwkPUsPrPOtozupJqFpJP.jpeg?dl=1" title="Screenshot 2025-03-22 141652" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2fd5468774696f8764ac1fff7c9dc9f8c4e1a75_2_690x224.jpeg" alt="Screenshot 2025-03-22 141652" data-base62-sha1="pxpKgeLwkPUsPrPOtozupJqFpJP" width="690" height="224" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2fd5468774696f8764ac1fff7c9dc9f8c4e1a75_2_690x224.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2fd5468774696f8764ac1fff7c9dc9f8c4e1a75_2_1035x336.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2fd5468774696f8764ac1fff7c9dc9f8c4e1a75_2_1380x448.jpeg 2x" data-dominant-color="CFCFA8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-22 141652</span><span class="informations">1912×621 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c9c3b4188b66b3c9678b7378c80fa63d3756fb4.png" data-download-href="/uploads/short-url/6mDJrWXh6zbYuHa0kPduP9ljug4.png?dl=1" title="Screenshot 2025-03-22 141625" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c9c3b4188b66b3c9678b7378c80fa63d3756fb4.png" alt="Screenshot 2025-03-22 141625" data-base62-sha1="6mDJrWXh6zbYuHa0kPduP9ljug4" width="638" height="500" data-dominant-color="A4A339"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-22 141625</span><span class="informations">760×595 304 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for the help. Tom.</p>

---

## Post #2 by @muratmaga (2025-03-24 16:00 UTC)

<p>I think you will find our new module PlaceLMGrid easier and more flexible than the SemiLMPatch functionality. See the tutorial here: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/GridBasedLandmarking" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/GridBasedLandmarking at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>Having said that you are trying to landmark a fairly complex area. Any method that involves projecting landmarks will have hard time avoiding those holes and crest etc. Also the landmarks on the basicranium tends to be quite adjacent.</p>
<p>If I were you, I would look into our new extension, Dense Correspondence Analysis, which is designed to tackle exactly situations like this.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/9877012cb1941ca6b7635ec726370eb4/SlicerMorph/SlicerDenseCorrespondenceAnalysis" class="thumbnail">

  <h3><a href="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerDenseCorrespondenceAnalysis: Dense Correspondence Analysis for Surfaces</a></h3>

    <p><span class="github-repo-description">Dense Correspondence Analysis for Surfaces</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>See the section on step-by-step landmarking (DeCaL module)</p>

---

## Post #3 by @ThomasVanParys (2025-03-24 20:02 UTC)

<p>Thank you for the advice.<br>
These are great modules, but there seems to be a small issue with the PlaceLMGrid projections on my own data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de4ac18b717568661efb8882c961b18d92cb7d83.jpeg" data-download-href="/uploads/short-url/vIua4FdeemwSVnLXmSbPrVTI2yf.jpeg?dl=1" title="GridIssue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de4ac18b717568661efb8882c961b18d92cb7d83_2_690x421.jpeg" alt="GridIssue" data-base62-sha1="vIua4FdeemwSVnLXmSbPrVTI2yf" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de4ac18b717568661efb8882c961b18d92cb7d83_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de4ac18b717568661efb8882c961b18d92cb7d83_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de4ac18b717568661efb8882c961b18d92cb7d83.jpeg 2x" data-dominant-color="B4A990"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GridIssue</span><span class="informations">1122×686 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(perhaps my parameters are wrong here?)</p>
<p>I am assuming I need to manually apply all models with fixed single Landmarks before the DeCaL procedure (creating the atlas etc)?<br>
Thank you so much for the assistance!</p>

---

## Post #4 by @muratmaga (2025-03-24 21:19 UTC)

<p>You have couple options. The simplest will be use the scissors tool in Dynamic model to crop out the section of the model you want to put landmarks on and then use the grid landmarks. That way you have less complexity to deal with.</p>
<p>If you do not want to do that, you can nudge the four corner points slightly and also play with the projection parameter in the advanced setting.</p>
<aside class="quote no-group" data-username="ThomasVanParys" data-post="3" data-topic="42279">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>I am assuming I need to manually apply all models with fixed single Landmarks before the DeCaL procedure (creating the atlas etc)?</p>
</blockquote>
</aside>
<p>If you already have manual landmarks for all the models, you are good to go with the DeCaL.</p>

---

## Post #5 by @ThomasVanParys (2025-03-27 19:48 UTC)

<p>Thank you. The DeCAL method is providing me with pseudo-landmarks for the entire skull model, is this somewhat diluting the shape analysis I specifically wanted at the skull base?</p>
<p>I performed a practice run on 4 NMDID segmented skulls. See the Lm and model data here. It didn’t generate an atlas model, but I will try it on my faster department computer tomorrow: <a href="https://drive.google.com/drive/folders/1yGXYLMEPK_R_TWymdOvB4WiCqxDAw_yu?usp=drive_link" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1yGXYLMEPK_R_TWymdOvB4WiCqxDAw_yu?usp=drive_link</a></p>
<p>Finally, I am assuming the new aligned Lm files from DeCAL are ready for GPA+PCA in SlicerMorph? Thank you!</p>

---

## Post #6 by @muratmaga (2025-03-27 22:21 UTC)

<aside class="quote no-group" data-username="ThomasVanParys" data-post="5" data-topic="42279">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>Thank you. The DeCAL method is providing me with pseudo-landmarks for the entire skull model, is this somewhat diluting the shape analysis I specifically wanted at the skull base?</p>
</blockquote>
</aside>
<p>You can subset the landmarks see: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/DeCAL#excluding-points-from-the-atlas" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/DeCAL at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #7 by @ThomasVanParys (2025-03-28 13:15 UTC)

<p>Thank you!<br>
Unfortunately the test run has failed and produced this atlas:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33b8d3b9229a93f75ad24db214184cda82ae8dec.jpeg" data-download-href="/uploads/short-url/7nyl9dwfinKNx318Icy35o4olhW.jpeg?dl=1" title="Atlas_failed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b8d3b9229a93f75ad24db214184cda82ae8dec_2_690x302.jpeg" alt="Atlas_failed" data-base62-sha1="7nyl9dwfinKNx318Icy35o4olhW" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b8d3b9229a93f75ad24db214184cda82ae8dec_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b8d3b9229a93f75ad24db214184cda82ae8dec_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b8d3b9229a93f75ad24db214184cda82ae8dec_2_1380x604.jpeg 2x" data-dominant-color="9B9CB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Atlas_failed</span><span class="informations">1920×843 87.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Please see my data used here: <a href="https://drive.google.com/drive/folders/1yGXYLMEPK_R_TWymdOvB4WiCqxDAw_yu?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">DeCAL_NMDID - Google Drive</a></p>
<p>If you have the time to advise me on what has gone wrong here, I would be extremely grateful. Tom.</p>

---

## Post #8 by @muratmaga (2025-03-28 13:36 UTC)

<p>That’s because you did not follow the same LM ordering in all your samples.<br>
To avoid that, I would suggest creating a LM template and then using in all your samples.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1500cd0d2b923c8b46256be3f84cc47b440453f.jpeg" data-download-href="/uploads/short-url/yqKzLo1jyoEs7C5kBvL9P0FWKXZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1500cd0d2b923c8b46256be3f84cc47b440453f_2_573x499.jpeg" alt="image" data-base62-sha1="yqKzLo1jyoEs7C5kBvL9P0FWKXZ" width="573" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1500cd0d2b923c8b46256be3f84cc47b440453f_2_573x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1500cd0d2b923c8b46256be3f84cc47b440453f_2_859x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1500cd0d2b923c8b46256be3f84cc47b440453f.jpeg 2x" data-dominant-color="9C9932"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1145×998 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @ThomasVanParys (2025-03-28 15:42 UTC)

<p>Re-landmarking in sequence with the template has worked, and I have managed to generate multiple pseudo-landmarks at the skull base, instead of the entire skull vault:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c9b153e03ab91f464950a6365e5f3f0410488d4.jpeg" data-download-href="/uploads/short-url/mloKrGjTrG3nxxR4tKZuICRvXuc.jpeg?dl=1" title="Basicranium2_pseudolandmarks" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c9b153e03ab91f464950a6365e5f3f0410488d4_2_690x445.jpeg" alt="Basicranium2_pseudolandmarks" data-base62-sha1="mloKrGjTrG3nxxR4tKZuICRvXuc" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c9b153e03ab91f464950a6365e5f3f0410488d4_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c9b153e03ab91f464950a6365e5f3f0410488d4_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c9b153e03ab91f464950a6365e5f3f0410488d4_2_1380x890.jpeg 2x" data-dominant-color="A0A397"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Basicranium2_pseudolandmarks</span><span class="informations">1920×1239 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The final <code>Run subsetting</code> stage appears to be failing however, as I can’t see the new landmarks saved in the output_directory.<br>
I have &gt;100 skulls to landmark before <code>DeCAL</code>, but will use <code>ALPACA</code> and adjust accordingly. Then I will merge the fixed single and pseudo-landmarks together and run GPA/PCA? This has been extremely grateful Murat, thank you!</p>

---

## Post #10 by @muratmaga (2025-03-28 16:58 UTC)

<p>I would not use</p>
<aside class="quote no-group" data-username="ThomasVanParys" data-post="9" data-topic="42279">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>The final <code>Run subsetting</code> stage appears to be failing however, as I can’t see the new landmarks saved in the output_directory.</p>
</blockquote>
</aside>
<p>I can’t replicate this on my end. If you can share your data, I can take a look.</p>
<aside class="quote no-group" data-username="ThomasVanParys" data-post="9" data-topic="42279">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>have &gt;100 skulls to landmark before <code>DeCAL</code>, but will use <code>ALPACA</code> and adjust accordingly.</p>
</blockquote>
</aside>
<p>I would not use ALPACA in this context. The main goal of DeCA is to create reliable correspondences, and ALPACA has no constraints on that. You can use ALPACA to transfer manual landmarks to your remaining skulls, but you should review them carefully before you feed them into DeCA.</p>

---

## Post #11 by @ThomasVanParys (2025-03-28 19:48 UTC)

<p>Here is the output from DeCAL ran today: <a href="https://drive.google.com/drive/folders/1j5CVbQxn2nexbFOKGBhRg5Ken_LwJwY1?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">2025_03-28_14_20_26 - Google Drive</a></p>
<p>That sounds great, I will use ALPACA for the fixed manual landmarks and then adjust them accordingly before DeCAL. Thank you!</p>

---

## Post #12 by @muratmaga (2025-03-28 20:14 UTC)

<aside class="quote no-group" data-username="ThomasVanParys" data-post="9" data-topic="42279">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>The final <code>Run subsetting</code> stage appears to be failing however, as I can’t see the new landmarks saved in the output_directory.</p>
</blockquote>
</aside>
<p>I am not sure I understand the issue. The subsetted landmarks are saved in the folder you shared. There are 32 LMs in each of them. Isn’t that’s what you wanted?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bafca9f4c98cad2d6976360ea0df047bf4fcd4a.png" data-download-href="/uploads/short-url/jVIZZJe3DIWK6MQCx5IhSCRSv7Y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bafca9f4c98cad2d6976360ea0df047bf4fcd4a_2_689x252.png" alt="image" data-base62-sha1="jVIZZJe3DIWK6MQCx5IhSCRSv7Y" width="689" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bafca9f4c98cad2d6976360ea0df047bf4fcd4a_2_689x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bafca9f4c98cad2d6976360ea0df047bf4fcd4a_2_1033x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bafca9f4c98cad2d6976360ea0df047bf4fcd4a_2_1378x504.png 2x" data-dominant-color="EFF3F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2388×874 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @ThomasVanParys (2025-03-28 21:46 UTC)

<p>My apologies, they were in my DeCAL_output file. I now have .json files for both fixed single landmarks (32, which are present) and for the subsetted pseudo-landmarks for each model generated from DeCAL. I will then merge fixed and pseudo-landmarks for each model. Thank you Murat.</p>

---
