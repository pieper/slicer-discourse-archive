# ALPACA TPS warped model not showing

**Topic ID**: 34196
**Date**: 2024-02-07
**URL**: https://discourse.slicer.org/t/alpaca-tps-warped-model-not-showing/34196

---

## Post #1 by @ThomasVanParys (2024-02-07 22:44 UTC)

<p>Hello,<br>
I am looking to analyse shape variation of different human lungs. For this, I have generated a template lung with adequate surface landmark coverage which can be used for the ALPACA function. However, when I run ALPACA with the template lung, template source landmarks, and the new sample I want superimposed, neither the warped source model or the ALPACA initial landmarks is displayed. Has anyone else experienced this issue?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf079adfdaa7c750b50da059710db2f850f6c9f7.png" data-download-href="/uploads/short-url/rfVuph8pmABwIFOZmtEP4LipK19.png?dl=1" title="MicrosoftTeams-image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf079adfdaa7c750b50da059710db2f850f6c9f7_2_690x334.png" alt="MicrosoftTeams-image" data-base62-sha1="rfVuph8pmABwIFOZmtEP4LipK19" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf079adfdaa7c750b50da059710db2f850f6c9f7_2_690x334.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf079adfdaa7c750b50da059710db2f850f6c9f7_2_1035x501.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf079adfdaa7c750b50da059710db2f850f6c9f7_2_1380x668.png 2x" data-dominant-color="B6B0CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MicrosoftTeams-image</span><span class="informations">1851×898 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-02-07 23:56 UTC)

<p>Did turn on the visibility for the TPS deformed model (first screenshot)? Also what Slicer version are you using? This alpaca results are either incomplete or you are using an older version. Resultant files should be now nested under a folder in the Data module (second screenshot):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a6b0ee5040dbc7630d2562a50db9bb03f6d393b.png" data-download-href="/uploads/short-url/aCkHDPxuqZ76VxB7lKDaSmTGeFR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a6b0ee5040dbc7630d2562a50db9bb03f6d393b_2_628x500.png" alt="image" data-base62-sha1="aCkHDPxuqZ76VxB7lKDaSmTGeFR" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a6b0ee5040dbc7630d2562a50db9bb03f6d393b_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a6b0ee5040dbc7630d2562a50db9bb03f6d393b_2_942x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a6b0ee5040dbc7630d2562a50db9bb03f6d393b_2_1256x1000.png 2x" data-dominant-color="D4D9DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2120×1686 635 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cff220a78991c3e7144a9c208c9cb7c4ddad940b.png" data-download-href="/uploads/short-url/tFzAIIVNciAcstoqRFtBevpiYwX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cff220a78991c3e7144a9c208c9cb7c4ddad940b_2_609x499.png" alt="image" data-base62-sha1="tFzAIIVNciAcstoqRFtBevpiYwX" width="609" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cff220a78991c3e7144a9c208c9cb7c4ddad940b_2_609x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cff220a78991c3e7144a9c208c9cb7c4ddad940b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cff220a78991c3e7144a9c208c9cb7c4ddad940b.png 2x" data-dominant-color="EAE8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">836×686 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @ThomasVanParys (2024-02-08 12:31 UTC)

<p>Ok, this version is 5.6.1, and surprisingly, the ALPACA display settings are not able to be switched on. I have provided the two screenshots showing the issue on my end, but I am grateful for any more advice on this issue.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b5d2f82d8aae01a127737c01a0506ed9ff80fed.png" data-download-href="/uploads/short-url/aKHsuhmGFo4JLvkkmFqs2RdIs0J.png?dl=1" title="issue 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5d2f82d8aae01a127737c01a0506ed9ff80fed_2_690x371.png" alt="issue 1" data-base62-sha1="aKHsuhmGFo4JLvkkmFqs2RdIs0J" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5d2f82d8aae01a127737c01a0506ed9ff80fed_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5d2f82d8aae01a127737c01a0506ed9ff80fed_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5d2f82d8aae01a127737c01a0506ed9ff80fed_2_1380x742.png 2x" data-dominant-color="B3B5DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">issue 1</span><span class="informations">1600×862 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a52ef53f1cb5be48a949e66cfaa33c5c129144de.png" data-download-href="/uploads/short-url/nzho9RyDdkG9OfEnHuhNWHsg33U.png?dl=1" title="issue 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a52ef53f1cb5be48a949e66cfaa33c5c129144de_2_690x370.png" alt="issue 2" data-base62-sha1="nzho9RyDdkG9OfEnHuhNWHsg33U" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a52ef53f1cb5be48a949e66cfaa33c5c129144de_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a52ef53f1cb5be48a949e66cfaa33c5c129144de_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a52ef53f1cb5be48a949e66cfaa33c5c129144de_2_1380x740.png 2x" data-dominant-color="BFC2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">issue 2</span><span class="informations">1597×858 53.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-02-08 15:59 UTC)

<p>The only time I saw this happening when ALPACA stopped working in the middle due to an error. Can you share the log file (CTRL+0), better yet can you share those two models and the LMs.</p>

---

## Post #5 by @ThomasVanParys (2024-02-08 16:57 UTC)

<p>I’ve attached a google drive with the template model, template landmarks, target model, and log file for this stage:  <a href="https://drive.google.com/drive/folders/1SHq7x5Ea4qnyc-4Xl0PS9nb6gakRa_aA?usp=drive_link" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1SHq7x5Ea4qnyc-4Xl0PS9nb6gakRa_aA?usp=drive_link</a><br>
It is possible the template may need an extra ‘dummy patch’ for fully cover the lung, which can be removed at a later date. Once again, thank you for the assistance!</p>

---

## Post #6 by @muratmaga (2024-02-08 17:03 UTC)

<p>this is not publicly shared, it says I need access</p>

---

## Post #7 by @ThomasVanParys (2024-02-08 17:07 UTC)

<p>My apologies, the file should be available now.</p>

---

## Post #8 by @muratmaga (2024-02-08 17:57 UTC)

<p>ALPACA is failing at the end of the deformable registration (cpd), it is doing the rigid and scaling fine. We have to investigate this <a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/agporto">@agporto</a> can you take a look?</p>
<p>Independently, your models are generating these warnings when loaded into Slicer. I don’t know if this has anything to do with how they are created, or causing an issue. But there are lots of these warnings:</p>
<p><code>Generic Warning: In vtkMath.cxx, line 799 vtkMath::Jacobi: Error extracting eigenfunctions </code></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> is this a concern, or is it harmless? I am not seeing any other 3D models generating this warning when loaded into Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d19f8385cb3eb5f696f37fe36e1206a0e62f6382.jpeg" data-download-href="/uploads/short-url/tUpxYqLdszr7sJM5aCh0E4i7XBU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d19f8385cb3eb5f696f37fe36e1206a0e62f6382_2_430x500.jpeg" alt="image" data-base62-sha1="tUpxYqLdszr7sJM5aCh0E4i7XBU" width="430" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d19f8385cb3eb5f696f37fe36e1206a0e62f6382_2_430x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d19f8385cb3eb5f696f37fe36e1206a0e62f6382.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d19f8385cb3eb5f696f37fe36e1206a0e62f6382.jpeg 2x" data-dominant-color="928BC7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">535×621 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2024-02-09 02:15 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="34196">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Generic Warning: In vtkMath.cxx, line 799 vtkMath::Jacobi: Error extracting eigenfunctions</p>
</blockquote>
</aside>
<p>Do you get this message when applying a thin-plate spline transform?<br>
The error message probably indicates some error, for example the transformation may fold into itself (and therefore become non-invertible). But this may not necessarily cause any problem (for example, if you do not need the inverse transform in regions where it cannot be computed then you do not need to worry about it).</p>
<p>I would recommend to use tools in Transforms module’s Display section to verify the computed transform.</p>

---

## Post #10 by @muratmaga (2024-02-09 02:21 UTC)

<p>No, the warnings are generated while loading the sample lung models. Nothing to do with transforms or alpaca.</p>
<p>I havent seen these warnings with any other model load, so i was wondering if there is anything unique about the.</p>

---

## Post #11 by @ThomasVanParys (2024-02-09 09:49 UTC)

<p>For clarity, the template model was originally generated in Slicer but then cleaned with an automated routine using Rvcg/Morpho packages in R. I can send further codes and files if that will help with your investigation. Thank you again for the help.</p>

---

## Post #12 by @muratmaga (2024-02-09 13:44 UTC)

<p>There is something wrong with these models. Try alpaca with the model you exported directly from your slicer segmentation and see if it works.</p>

---

## Post #13 by @lassoan (2024-02-09 15:13 UTC)

<p>You can also try Surface Toolbox in Slicer to clean the model (maybe there are coincident points, incorrect normals, etc.).</p>

---

## Post #14 by @ThomasVanParys (2024-02-09 16:10 UTC)

<p>I am using this template to process 220 samples for a wider growth study on juvenile lung development, manually cleaning each model may be a challenge. <a class="mention" href="/u/muratmaga">@muratmaga</a> I have repeated the same ALPACA process for the right lung template with successful results, and I am now batch processing my entire dataset of right lungs. This means there is a specific issue with the left lung template model, but I can’t think of anything in my process which was different to the right lung template.<br>
Let me know what else you might need.</p>

---
