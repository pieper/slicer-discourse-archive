# CT to optical image registration

**Topic ID**: 514
**Date**: 2017-06-16
**URL**: https://discourse.slicer.org/t/ct-to-optical-image-registration/514

---

## Post #1 by @Niousha_Aflatouni (2017-06-16 02:28 UTC)

<p>Hi there,</p>
<p>I have 2 image sets: one is a high resolution CT from a small specimen with<br>
0.15, 0.15, 0.15 millimeter spacing in each of the X, Y and Z axis, the<br>
other one is an optical stack of the same specimen taken using a digital<br>
camera with the following spacing (mm) in x,y,and  z axis respectively:<br>
0.05, 0.05, 3. The photographed images are taken carefully so there is a<br>
corresponding CT slice for each optical image.</p>
<p>I would like to align the two image sets.</p>
<p>I’m using Slicer 4.6.2 and tried landmark registration but when I save the<br>
transformed image (hardened), and then open it, it doesn’t match with my<br>
fixed image!</p>
<p>Can you help me do the registration properly?</p>
<p>Thanks,<br>
Niousha</p>

---

## Post #2 by @lassoan (2017-06-16 03:30 UTC)

<p>Could you please try it with the latest nightly build?<br>
Could you attach a few screenshots of how the images look before registration, after registration, after hardening, and after reloading the hardened image?</p>

---

## Post #3 by @Niousha_Aflatouni (2017-06-17 01:46 UTC)

<p>Hi,</p>
<p>Please see attached for the images requested.<br>
Fixed image: optical (0.05, 0.05, 3 millimeter spacing)<br>
Moving image: Ex vivo ( 0.15, 0.15, 0.15 millimeter spacing )</p>
<p>P.S. The CT images were reoriented using Inveon software prior to<br>
registration( before reorientation image not included).</p>
<p>Thanks,<br>
Niousha</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f51fd5143aad09036db15bbf3cd31a2f4c562f38.png" data-download-href="/uploads/short-url/yYtbcJUQWvPUQhLnIsi9fGWhjwk.png?dl=1" title="1.Before registration Shown in ITKSnap.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f51fd5143aad09036db15bbf3cd31a2f4c562f38_2_501x500.png" data-base62-sha1="yYtbcJUQWvPUQhLnIsi9fGWhjwk" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f51fd5143aad09036db15bbf3cd31a2f4c562f38_2_501x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f51fd5143aad09036db15bbf3cd31a2f4c562f38.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f51fd5143aad09036db15bbf3cd31a2f4c562f38.png 2x" data-dominant-color="756161"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1.Before registration Shown in ITKSnap.png</span><span class="informations">685×683 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e5be58016c034e4a83a91f6839c3546b163aad9d.jpg" data-download-href="/uploads/short-url/wMp9k4sc7W5J1K1VZZwfWu9kqoR.jpg?dl=1" title="2.After alignment in 3DSlicer.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e5be58016c034e4a83a91f6839c3546b163aad9d_2_643x500.jpg" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e5be58016c034e4a83a91f6839c3546b163aad9d_2_643x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e5be58016c034e4a83a91f6839c3546b163aad9d_2_964x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e5be58016c034e4a83a91f6839c3546b163aad9d_2_1286x1000.jpg 2x" data-dominant-color="282A2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2.After alignment in 3DSlicer.jpg</span><span class="informations">1329×1033 267 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62fd9f76104ece085d6f12bef515e7a1d4b910e5.png" data-download-href="/uploads/short-url/e7IaX2T512JfDfhlwMBKSSApQbP.png?dl=1" title="3. Reloading in ITKSnap after alignment before hardening.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/62fd9f76104ece085d6f12bef515e7a1d4b910e5_2_505x500.png" data-base62-sha1="e7IaX2T512JfDfhlwMBKSSApQbP" width="505" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/62fd9f76104ece085d6f12bef515e7a1d4b910e5_2_505x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62fd9f76104ece085d6f12bef515e7a1d4b910e5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62fd9f76104ece085d6f12bef515e7a1d4b910e5.png 2x" data-dominant-color="254226"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3. Reloading in ITKSnap after alignment before hardening.png</span><span class="informations">687×679 50 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/340341278e681deed777a7935861e7dd7b42134c.png" data-download-href="/uploads/short-url/7q7NFSNQoKmW56l2ljrn5oy7O7G.png?dl=1" title="4.After Hardening.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/340341278e681deed777a7935861e7dd7b42134c_2_501x500.png" data-base62-sha1="7q7NFSNQoKmW56l2ljrn5oy7O7G" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/340341278e681deed777a7935861e7dd7b42134c_2_501x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/340341278e681deed777a7935861e7dd7b42134c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/340341278e681deed777a7935861e7dd7b42134c.png 2x" data-dominant-color="584175"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4.After Hardening.png</span><span class="informations">679×677 62.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/448b2c1bd0e03895495656cdba5cc3358c44a9cf.png" data-download-href="/uploads/short-url/9MmDSIw0iQ2lqc6ltn9oAeYw0QT.png?dl=1" title="5.After Resampling.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/448b2c1bd0e03895495656cdba5cc3358c44a9cf_2_510x500.png" data-base62-sha1="9MmDSIw0iQ2lqc6ltn9oAeYw0QT" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/448b2c1bd0e03895495656cdba5cc3358c44a9cf_2_510x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/448b2c1bd0e03895495656cdba5cc3358c44a9cf.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/448b2c1bd0e03895495656cdba5cc3358c44a9cf.png 2x" data-dominant-color="723629"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5.After Resampling.png</span><span class="informations">697×683 48.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2017-06-18 18:43 UTC)

<p>Could you attach a few screenshots of how the images look <strong>in 3D Slicer!!!</strong> before registration, after registration, after hardening, and after reloading the hardened image? Many software make mistakes when importing images (ignore image orientation, etc), so we have to make sure the registration is correct within 3D Slicer, and if it is, then you can report the errors to developers of other software packages that you use. By the way, as you might have realized, Slicer can provide registration and visualization features that fulfills most users needs; so probably you can simplify your life by doing all processing in Slicer.</p>

---

## Post #5 by @Niousha_Aflatouni (2017-06-19 21:23 UTC)

<p>Hi Andras,</p>
<p>I tried the latest version and also tried <em>not to center</em> the images this<br>
time, and it worked (previously the images were centered before<br>
registration). So I got good alignments when I set the fixed and moving<br>
image as follows:<br>
Fixed image: optical (0.05, 0.05, 3 millimeter spacing)<br>
Moving image: Ex vivo ( 0.15, 0.15, 0.15 millimeter spacing )</p>
<p>But the problem for now is to do the reverse registration. In other words,<br>
I’m interested in doing the registration in such a way that my optical<br>
images are moving and my CT ex vivo images are fixed (the spacing is the<br>
same as indicated above). When doing that it shows me good overlap but I<br>
can’t save the hardened image. Please see the Error message attached; I<br>
also attached a few screen shots of before and after the alignment. I also<br>
included a screen shot of after hardening. But I don’t have an image after<br>
reloading the hardened image, because, as I explained, the hardened image<br>
couldn’t be saved. But I included the message generated after trying to<br>
save it. Based on your knowledge, how would I be able to perform such<br>
registration in Slicer?</p>
<p>I also noticed in our last email conversation you suggested that Slicer can<br>
work for most of the analysis and visualization. So my question is can I<br>
calculate the registration errors based on measures of Mutual Information<br>
and Target Registration Error using this software? If yes, can you please<br>
provide some help on how this is done?</p>
<p>Thank you,<br>
Niousha</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53c1ea1a9c1a6dd90941cf40f5899e016e601d6a.png" data-download-href="/uploads/short-url/bWX5zuVq8GCuliweBJbDKZGqaW6.png?dl=1" title="3. After hardening.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/53c1ea1a9c1a6dd90941cf40f5899e016e601d6a_2_689x337.png" data-base62-sha1="bWX5zuVq8GCuliweBJbDKZGqaW6" width="689" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/53c1ea1a9c1a6dd90941cf40f5899e016e601d6a_2_689x337.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/53c1ea1a9c1a6dd90941cf40f5899e016e601d6a_2_1033x505.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53c1ea1a9c1a6dd90941cf40f5899e016e601d6a.png 2x" data-dominant-color="3B3E42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3. After hardening.png</span><span class="informations">1206×590 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77e435570dd14c649f05351a8f65c75bd1af9512.png" data-download-href="/uploads/short-url/h6BKH45F3HJ5DOtsb17U6Dkpao2.png?dl=1" title="4. Error message.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77e435570dd14c649f05351a8f65c75bd1af9512.png" data-base62-sha1="h6BKH45F3HJ5DOtsb17U6Dkpao2" width="690" height="455" data-dominant-color="212020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4. Error message.png</span><span class="informations">841×555 55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0f03f836733be977cff96f13a626579582ec29.png" data-download-href="/uploads/short-url/40dxsMCYJFJUODeyQzMk4tZEKmJ.png?dl=1" title="1. Before registeration_images aren't centered-optical to exvivo.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1c0f03f836733be977cff96f13a626579582ec29_2_690x398.png" data-base62-sha1="40dxsMCYJFJUODeyQzMk4tZEKmJ" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1c0f03f836733be977cff96f13a626579582ec29_2_690x398.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1c0f03f836733be977cff96f13a626579582ec29_2_1035x597.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0f03f836733be977cff96f13a626579582ec29.png 2x" data-dominant-color="5F6368"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1. Before registeration_images aren't centered-optical to exvivo.png</span><span class="informations">1187×685 354 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62794f26427e6928af8a9bbb67653a1051ee9026.png" data-download-href="/uploads/short-url/e38H8IY65h1dpJfiJ7eWK5dAq0K.png?dl=1" title="2. Optical to exvivo_after alignment.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/62794f26427e6928af8a9bbb67653a1051ee9026_2_690x391.png" data-base62-sha1="e38H8IY65h1dpJfiJ7eWK5dAq0K" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/62794f26427e6928af8a9bbb67653a1051ee9026_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/62794f26427e6928af8a9bbb67653a1051ee9026_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62794f26427e6928af8a9bbb67653a1051ee9026.png 2x" data-dominant-color="464649"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2. Optical to exvivo_after alignment.png</span><span class="informations">1199×681 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2017-06-20 00:48 UTC)

<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="5" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>tried not to center the images</p>
</blockquote>
</aside>
<p>Never center images if you need proper alignment. If centering is enabled then it forces Slicer to ignore image origin information that is stored in the image header.</p>
<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="5" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>to do the reverse registration</p>
</blockquote>
</aside>
<p>Slicer can compute the inverse of any transformation (linear, bspline, thin-plate spline, displacement field; or any combination of these in any order, with/without inversion in each component) by a single click. Go to Transforms module and click <code>Invert</code> button in <code>Edit</code> section. You can then align the fixed image to the moving image by applying the inverse transform to the fixed image.</p>
<p>In Slicer you can choose from a wide range of image registration methods: intensity-based, landmark-based, surface-based; with various metrics and transformations. For intensity-based registration with warping transform I would recommend to try these:</p>
<ul>
<li><a href="https://github.com/lassoan/SlicerElastix/blob/master/README.md">General registration (Elastix)</a>: available in the SlicerElastix extension. It is very robust and simple to use (requires much less parameter tuning than BRAINS).</li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/BRAINSFit">General registration (BRAINS)</a>: available in the Slicer core, by default uses mutual information. There are lots of examples and parameter sets in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary">registration case library</a>.</li>
</ul>
<p>Compute TRE: Mark landmarks in Fixed and Moving volume using <code>Markups</code> module. Apply computed transform to landmarks of Moving volume. Write a short script (2-3 lines of Python code) that compute distance between Fixed landmarks and transformed Moving landmarks.</p>

---

## Post #7 by @Niousha_Aflatouni (2017-06-21 20:26 UTC)

<p>Hi Andras,</p>
<p>I tried the inverse transform the way you explained and I can see the<br>
change in the image but I still have the same issue as before: the hardened<br>
image can not be saved and the same error message appears. I couldn’t<br>
figure out what the issue is. Any thoughts on that?</p>
<p>As for the intensity based registration, I’m more interested to know if<br>
there is any way that the registration can be quantified (not performed)<br>
based on  Mutual Information, which is an intensity measure?</p>
<p>Thank you,<br>
Niousha</p>

---

## Post #8 by @lassoan (2017-06-21 22:02 UTC)

<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="7" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>the hardened<br>
image can not be saved</p>
</blockquote>
</aside>
<p>Saving should be no problem, but maybe if it’s a color image there may be issues. Could you try if saving works if you convert the image to scalar (grayscale) volume (using Vector to scalar volume module)?</p>
<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="7" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>As for the intensity based registration, I’m more interested to know if<br>
there is any way that the registration can be quantified (not performed)<br>
based on  Mutual Information</p>
</blockquote>
</aside>
<p>Mutual information minimizes the entropy of the joint histogram. You can find the final value in the application log (the metric value should decrease in each iteration), but it’s not a metric of registration quality.</p>
<p>Registration is typically assessed using spatial error metrics. If you have ground truth landmark points then compute TRE. You may also compute Hausdorff distance using Segment Comparison module (between ground truth segmentation in the fixed image and segmentation in moving image transformed to fixed image coordinate system).</p>
<p>The only intensity-based metric that I’m aware of that might be somewhat applicable for assessing registration (or, more accurately, the effect of remaining registration error) is the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DoseComparison">module for comparison of dose volumes (in SlicerRT extension)</a>.</p>

---

## Post #9 by @Niousha_Aflatouni (2017-06-29 20:45 UTC)

<p>Hi Andras,</p>
<p>Thanks for the info. After many trials, I realized that the images should<br>
be cropped and turned into gray scale both in 3D Slicer, and if those are<br>
initially done in MATLAB then they won’t work in 3D Slicer.</p>
<p>I also found a feature in 3D Slicer called Metric Test, that seems to<br>
enable us to calculate MMI and MSE. There was however no documentation for<br>
this feature that I could find. I was wondering is this something that I<br>
can reliably use for calculating the MI? I used two identical images with<br>
exact overlap. For that I used different histogram bin numbers that ranged<br>
from 50 to 1000. Then the MI values I got ranged from -0.925 to -1.79812. I<br>
was wondering how can one interpret these numbers, also what is the<br>
suggested histogram bin number to use?</p>
<p>Thanks,<br>
Niousha</p>

---

## Post #10 by @lassoan (2017-06-30 13:42 UTC)

<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="9" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>if those are<br>
initially done in MATLAB then they won’t work in 3D Slicer</p>
</blockquote>
</aside>
<p>What do you mean? What do you expect to happen and what happens?</p>

---

## Post #11 by @lassoan (2017-06-30 13:53 UTC)

<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="9" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>There was however no documentation for<br>
this feature that I could find</p>
</blockquote>
</aside>
<p>I think the only help is in the tooltips. Let us know if anything is unclear.</p>
<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="9" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>I was wondering is this something that I<br>
can reliably use for calculating the MI</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="9" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>I was wondering how can one interpret these numbers</p>
</blockquote>
</aside>
<p>It is the metric that is minimized during registration. Read about the metric in journal papers, such as <a href="https://www.researchgate.net/publication/222899257_BRAINSFIT_Mutual_information_registrations_of_whole-brain_3D_Images_using_the_insight_toolkit">https://www.researchgate.net/publication/222899257_BRAINSFIT_Mutual_information_registrations_of_whole-brain_3D_Images_using_the_insight_toolkit</a>.</p>
<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="9" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>what is the<br>
suggested histogram bin number to use?</p>
</blockquote>
</aside>
<p>Usually registration is not very sensitive to the number of bins. You can probably use the default value or slightly change it and see if it makes results better. See more details of mutual information metric in journal papers.</p>

---

## Post #12 by @Niousha_Aflatouni (2017-07-10 19:30 UTC)

<p>Hi Andras,</p>
<p>Thanks for your previous answers. I had some questions about the Metric<br>
Test to calculate MI; I’m interested in obtaining the MI value of a<br>
specific region from the images rather than the entire image sets. I<br>
understand that this normally can be done using Masking but I couldn’t find<br>
a place where we can input the masked images in addition to the fixed and<br>
moving image. Is this something that can be done when running the Metric<br>
Test for MI? If not, what are the alternatives?</p>
<p>Thanks,<br>
Niousha</p>

---

## Post #13 by @lassoan (2017-07-11 14:39 UTC)

<p>You have two options:</p>
<ul>
<li>Option A: Extend the Metric Test module to accept mask images. You need to build Slicer from source code and be somewhat familiar with C++ programming (so that you can find out where to add the masking option).</li>
<li>Option B: Create a simple scripted module that computes the metric at different positions. You can check out SimpleITK examples for registration <a href="https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks/tree/master/Python">here</a> (for example, a <a href="https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks/blob/master/Python/63_Registration_Initialization.ipynb">registration initialization example</a>)</li>
</ul>

---

## Post #14 by @Niousha_Aflatouni (2017-07-11 20:03 UTC)

<p>Hi Andras,</p>
<p>Can you provide some instructions on how to access the source code? I<br>
followed the instructions provided in here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CHECKOUT_slicer_source_files" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CHECKOUT_slicer_source_files</a><br>
but it wasn’t clear to me what should be done next and how to access the<br>
(i.e. Metric Test’s )source code from there?</p>
<p>I’m really new to this so your helps are really appreciated.</p>
<p>Thanks,<br>
Niousha</p>

---

## Post #15 by @lassoan (2017-07-11 20:21 UTC)

<p>After build is complete, you’ll see the source files (in c:\D\S4D\BRAINSTools\BRAINSFit\PerformMetricTest.cxx).</p>

---

## Post #16 by @Niousha_Aflatouni (2017-07-26 15:24 UTC)

<p>Hi Andras,</p>
<p>Do we need to do any pre-processing step before we import images that are<br>
modified in MATLAB?</p>
<p>The problem is anytime I do some modification on my .jpg images in MATLAB<br>
(i.e rotation, gray scale, cropping), then those images will change in<br>
strange and unexpected ways when exported back to Slicer.</p>
<p>Thanks,<br>
Niousha</p>

---

## Post #17 by @lassoan (2017-07-26 17:11 UTC)

<p>Do you work with color images? 2D or 3D?</p>

---

## Post #18 by @Niousha_Aflatouni (2017-07-26 18:24 UTC)

<p>Hi Andras,</p>
<p>Yes, the images are colored, 2D initially. So what I do is I align them in<br>
MATLAB using control point registration, then save each individual modified<br>
2D image and then stack those in 3D Slicer. I then change the stack into<br>
gray scale in 3D Slicer.</p>
<p>Niousha</p>

---

## Post #19 by @lassoan (2017-07-28 21:35 UTC)

<blockquote>
<p>I align them in MATLAB using control point registration, then save each individual modified<br>
2D image and then stack those in 3D Slicer</p>
</blockquote>
<p>This should work. What problem do you see? If you just browse the aligned images in an image viewer, do they appear correctly, nicely aligned?</p>

---

## Post #20 by @Niousha_Aflatouni (2017-08-16 16:46 UTC)

<p>Hi Andras,</p>
<p>I kind of figured out what the problem was. I should have used imwrite to<br>
save the images properly to avoid this issue. But thanks for following up.<br>
I was wondering does slicer support combining multiple transforms that can<br>
be applied to an image? For example, consider having 4 images, (i.e. image<br>
1 to image 4),  with the ultimate goal of mapping image 4 such that it<br>
aligns with image 1, can we find a final transformation matrix in 3D Slicer<br>
such that when we apply that to image 4 we can match image 4 to image 1?<br>
Please note that we already have obtained  the transformation matrices<br>
between, image 2 and 1, image 3 and 2, and image 4 and 3.</p>
<p>Thanks,<br>
Niousha</p>

---

## Post #21 by @lassoan (2017-08-17 04:12 UTC)

<aside class="quote no-group" data-username="Niousha_Aflatouni" data-post="20" data-topic="514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c77e96/48.png" class="avatar"> Niousha_Aflatouni:</div>
<blockquote>
<p>I was wondering does slicer support combining multiple transforms that can be applied to an image</p>
</blockquote>
</aside>
<p>Yes, Slicer can concatenate any number and types of transforms (both linear and warping). You can build a transform tree by drag-and-dropping transforms and volumes in Data module / Transform hierarchy tab. Probably you’ll need something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/3795be2970f15371e2f7cf8ade7dfc7dd2e75985.png" data-download-href="/uploads/short-url/7VJ5axmj32HnidRmGrGmNgfx4u9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3795be2970f15371e2f7cf8ade7dfc7dd2e75985_2_384x500.png" alt="image" data-base62-sha1="7VJ5axmj32HnidRmGrGmNgfx4u9" width="384" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3795be2970f15371e2f7cf8ade7dfc7dd2e75985_2_384x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3795be2970f15371e2f7cf8ade7dfc7dd2e75985_2_576x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/3795be2970f15371e2f7cf8ade7dfc7dd2e75985.png 2x" data-dominant-color="F0F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">666×867 30.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @lassoan (2019-08-21 16:10 UTC)

<p>A post was split to a new topic: <a href="/t/inverting-elastix-transform/8123">Inverting Elastix transform</a></p>

---

## Post #23 by @HodaGH (2021-04-21 18:30 UTC)

<p>Hi Andras,</p>
<p>You mentioned briefly here <a href="https://discourse.slicer.org/t/ct-to-optical-image-registration/514/11" class="inline-onebox">CT to optical image registration - #11 by lassoan</a>  that the only help on metric test is in “Tooltips”. I can’t find it. Where is that?</p>

---

## Post #24 by @lassoan (2021-04-21 18:37 UTC)

<p>Tooltips are the small windows that are displayed when you keep your mouse steady over a widget:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e6315f3484388c50bb6f624c3a4da4eccf5969d.png" alt="image" data-base62-sha1="kjC5DV0a7XwxPJSQAxzHjX4dIpD" width="563" height="387"></p>

---
