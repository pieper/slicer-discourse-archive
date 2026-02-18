# Volume rendering does not appear

**Topic ID**: 4303
**Date**: 2018-10-05
**URL**: https://discourse.slicer.org/t/volume-rendering-does-not-appear/4303

---

## Post #1 by @Carolina3D (2018-10-05 15:44 UTC)

<p>Operating system: Windows<br>
Slicer version:4.8.1<br>
Expected behavior: GIve me a volume redering picture<br>
Actual behavior: The program errors every time.</p>
<p>Do I have a to bad computer? HP Spectra Intel core i7 Geforce</p>

---

## Post #2 by @cpinter (2018-10-05 15:50 UTC)

<p>See <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/HardwareConfiguration">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/HardwareConfiguration</a></p>
<p>Can you please give us the exact type of the GPU in that laptop and the amount of RAM it has?</p>

---

## Post #3 by @Carolina3D (2018-10-05 16:22 UTC)

<p>Hi,<br>
Geforce GTX 1080 and 8 gb RAM.</p>

---

## Post #4 by @cpinter (2018-10-05 16:26 UTC)

<p>Definitely not too weak. Do you have issues with volume rendering?</p>

---

## Post #5 by @Carolina3D (2018-10-05 16:31 UTC)

<p>Yes, the program stops working when I ask for a volume renderaing and only give me a White Picture. Sometimes it works, but then computer begins to work so hard and slowly.</p>

---

## Post #6 by @cpinter (2018-10-05 16:36 UTC)

<p>Make sure GPU volume rendering is selected instead of the degfault CPU.</p>
<aside class="quote no-group" data-username="Carolina3D" data-post="5" data-topic="4303">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/9f8e36/48.png" class="avatar"> Carolina3D:</div>
<blockquote>
<p>program stops working when I ask for a volume renderaing and only give me a White Picture</p>
</blockquote>
</aside>
<p>Please elaborate on this. What steps do you exactly take after starting Slicer? What does it mean “stops working” and “white picture”?</p>

---

## Post #7 by @Carolina3D (2018-10-05 16:50 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/714e79dcedcab1c9e6afef18736e056553ad378d.jpeg" data-download-href="/uploads/short-url/gam5tk9eRDSv2QUZvT5rRmdEROd.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/714e79dcedcab1c9e6afef18736e056553ad378d_2_690x366.jpeg" alt="PNG" data-base62-sha1="gam5tk9eRDSv2QUZvT5rRmdEROd" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/714e79dcedcab1c9e6afef18736e056553ad378d_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/714e79dcedcab1c9e6afef18736e056553ad378d_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/714e79dcedcab1c9e6afef18736e056553ad378d_2_1380x732.jpeg 2x" data-dominant-color="747473"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">3680×1957 515 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> —the White Picture</p>
<p>I loading the dicom files- and the selects volume rendering in the menu. Klick on the Eye and the program Begins to work.<br>
Slowly I mean that the I can not do anything els with the computer and if I move the mouse it Begins to thinking and the program dosent answer at all and I need to turn the program off with the activity manager.</p>

---

## Post #8 by @brhoom (2018-10-05 16:53 UTC)

<p>Maybe the computer has two graphics card and the default working one is not the GTX?</p>
<p>Or maybe it is driver problem, what about other programs e.g 3D games do they work?</p>

---

## Post #9 by @muratmaga (2018-10-05 16:55 UTC)

<p>Is this a laptop? In any event, open the Nvidia control panel, navigate to the application settings to check the openGL rendering is done by the Geforce, not the integrated GPU…</p>

---

## Post #10 by @Carolina3D (2018-10-05 16:57 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="8" data-topic="4303" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Maybe the computer has two graphics card and the default working one is not the GTX?</p>
<p>Or maybe it is driver problem, what about other programs e.g 3D games do they work?</p>
</blockquote>
</aside>
<p>No it is only one graphic card on this computer. And I work i programs like inspier, meshmixer, spaceclaim, blender, fusion 360 and that work with any problems.</p>

---

## Post #11 by @Carolina3D (2018-10-05 17:00 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="4303" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Is this a laptop? In any event, open the Nvidia control panel, navigate to the application settings to check the openGL rendering is done by the Geforce, not the integrated GPU…</p>
</blockquote>
</aside>
<p>Yes it is a laptop. Ok I will check on that.</p>

---

## Post #12 by @jamesobutler (2018-10-05 17:01 UTC)

<p>As <a class="mention" href="/u/cpinter">@cpinter</a> suggested, make sure you are specifying the GPU rendering option. In the screenshot you posted it shows you are using “VTK CPU Ray Casting”.  Change this to the GPU option.</p>

---

## Post #13 by @brhoom (2018-10-05 17:18 UTC)

<blockquote>
<p>In the screenshot you posted it shows you are using “VTK CPU Ray Casting”. Change this to the GPU option.</p>
</blockquote>
<p>If nothing change, try the brain image from Slicer sample just to check if the problem is from Slicer not from the your image. If the brain image does not work try to remove slicer and re-install it. If it works, then maybe your image is very large, try to crop it to have a smaller image.</p>

---

## Post #14 by @Carolina3D (2018-10-05 17:19 UTC)

<p>Hi, yes I try that but that gives me only some shadows in the 3D window, even if I select ct-bone on the preset.</p>

---

## Post #15 by @Carolina3D (2018-10-05 17:20 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="13" data-topic="4303">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>If nothing change, try the brain image from Slicer sample just to check if the problem is from Slicer not from the your image. If the brain image does not work try to remove slicer and re-install it. If it works, then maybe your image is very large, try to crop it to have a smaller image.</p>
</blockquote>
</aside>
<p>Thanks, I will try that!</p>

---

## Post #16 by @lassoan (2018-10-05 17:27 UTC)

<p>If CPU volume rendering does not work then it means there is a problem with your data and so GPU volume rendering is not expected to work either.</p>
<p>Please also try with latest nightly version of Slicer. It supports many more GPUs than Slicer-4.8.1.</p>

---

## Post #17 by @rkikinis (2018-10-05 17:46 UTC)

<p>Hi</p>
<p>Can you also check the layout manager? What layout are you using?</p>
<p>Best</p>
<p>Ron</p>

---

## Post #18 by @Carolina3D (2018-10-05 18:30 UTC)

<p>Thanks, with the 3D slicer 4.9.0 all works fine so far.</p>

---
