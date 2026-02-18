# Bone Mineral Density (BMD) measurement method

**Topic ID**: 11010
**Date**: 2020-04-06
**URL**: https://discourse.slicer.org/t/bone-mineral-density-bmd-measurement-method/11010

---

## Post #1 by @manjula (2020-04-06 08:23 UTC)

<p>I have been told a method of calculating BMD from micro CT data using a proprietary software and i am wondering about the accuracy of the method and replicating it with the 3D Slicer.</p>
<p>The way it was done in the software was,<br>
we use 3 phantoms of know density, water and 0.25 and 0.75   and the mean hounsfield values  was</p>
<p>water 0 = -575.936<br>
0.25 = 1142.4<br>
0.75 = 3267.8</p>
<p>so the equation was<br>
X =(y+11.708)/4381.1</p>
<p>so i try to do this the same with the 3D Slicer,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c3777513cdaa0fb9ae449f088c19bbba892b311.jpeg" data-download-href="/uploads/short-url/1K4z2yqzj2RgOJYybXK8kAARDCF.jpeg?dl=1" title="Screenshot from 2020-04-06 10-07-50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c3777513cdaa0fb9ae449f088c19bbba892b311_2_690x318.jpeg" alt="Screenshot from 2020-04-06 10-07-50" data-base62-sha1="1K4z2yqzj2RgOJYybXK8kAARDCF" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c3777513cdaa0fb9ae449f088c19bbba892b311_2_690x318.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c3777513cdaa0fb9ae449f088c19bbba892b311_2_1035x477.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c3777513cdaa0fb9ae449f088c19bbba892b311_2_1380x636.jpeg 2x" data-dominant-color="3B3937"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-04-06 10-07-50</span><span class="informations">1886×870 445 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c17c0b4d0d29e7cd9ef449a6f4340e20163061.png" data-download-href="/uploads/short-url/kWgfsKXKSHMCupBxYgjuUPwIyU9.png?dl=1" title="Screenshot from 2020-04-06 10-08-55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c17c0b4d0d29e7cd9ef449a6f4340e20163061_2_690x93.png" alt="Screenshot from 2020-04-06 10-08-55" data-base62-sha1="kWgfsKXKSHMCupBxYgjuUPwIyU9" width="690" height="93" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c17c0b4d0d29e7cd9ef449a6f4340e20163061_2_690x93.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c17c0b4d0d29e7cd9ef449a6f4340e20163061_2_1035x139.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c17c0b4d0d29e7cd9ef449a6f4340e20163061_2_1380x186.png 2x" data-dominant-color="ECEAE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-04-06 10-08-55</span><span class="informations">1461×198 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>so my problem is,</p>
<ol>
<li>
<p>in the segment  statistics module, the value that come as the mean in the scalar volume statistics, is it the mean hounsfield  ?</p>
</li>
<li>
<p>Is the method of trying to arrive at BMD in this way is accurate ?</p>
</li>
<li>
<p>What is the reason for the slight difference in the mean values between the 3D Slicer and the other program ?</p>
</li>
</ol>
<p>thank you.</p>

---

## Post #2 by @lassoan (2020-04-06 14:10 UTC)

<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="11010">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>in the segment statistics module, the value that come as the mean in the scalar volume statistics, is it the mean hounsfield ?</p>
</blockquote>
</aside>
<p>You get results in the same unit as the input image. In case of a calibrated CT, it is Hounsfield unit. In case of a non-calibrated system, it can be anything.</p>
<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="11010">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Is the method of trying to arrive at BMD in this way is accurate ?</p>
</blockquote>
</aside>
<p>3 measurement points are very few. At least for initial exploration, I would add at least 5-10 points, just to have an idea about shape and amount of noise in the curve. It is highly unlikely that the calibration curve would be a line, so fitting a line to 3 points is a potential source of error.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/GelDosimetry">GelDosimetry extension</a> contains an automatic image intensity calibration and evaluation workflow that should be directly usable. <a class="mention" href="/u/cpinter">@cpinter</a> do you have any advice?</p>
<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="11010">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>What is the reason for the slight difference in the mean values between the 3D Slicer and the other program ?</p>
</blockquote>
</aside>
<p>There could be many reasons, but I don’t know what that software does. Is that software open-source? Do they describe somewhere what they do?</p>
<p>How much is the difference? If it’s small then it may be due to forcing the calibration curve to be a line.</p>

---

## Post #3 by @manjula (2020-04-06 15:46 UTC)

<p>Thank you for your kind reply as always.</p>
<p>The one we used is <a href="https://medicine.temple.edu/sites/medicine/files/files/ct_analyzer.pdf" rel="noopener nofollow ugc">Burker</a>.</p>
<p>The method it describe was way too complex for me but the way it was done is very simple.</p>
<p>You segment out the 3 phantoms. then calculate the mean values.  ( i mean automatically it  is given just like in the segment statistics module)</p>
<p>Then we put the 3 values to the graph and calculate the equation for line with libreCalc,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/244a4c54a34bc5f1ce11502d889c0bff1c08151f.png" data-download-href="/uploads/short-url/5b2n43EZvH4j6L0Q7eFVx1PYz6L.png?dl=1" title="Screenshot from 2020-04-06 17-43-24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/244a4c54a34bc5f1ce11502d889c0bff1c08151f_2_690x287.png" alt="Screenshot from 2020-04-06 17-43-24" data-base62-sha1="5b2n43EZvH4j6L0Q7eFVx1PYz6L" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/244a4c54a34bc5f1ce11502d889c0bff1c08151f_2_690x287.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/244a4c54a34bc5f1ce11502d889c0bff1c08151f_2_1035x430.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/244a4c54a34bc5f1ce11502d889c0bff1c08151f_2_1380x574.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-04-06 17-43-24</span><span class="informations">1512×629 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So from the trend-line we can calculate the density of any know HU value.</p>
<p>As you can see the difference between 3D slicer and the burker is very small i guess…</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="11010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>3 measurement points are very few. At least for initial exploration, I would add at least 5-10 points, just to have an idea about shape and amount of noise in the curve. It is highly unlikely that the calibration curve would be a line, so fitting a line to 3 points is a potential source of error.</p>
</blockquote>
</aside>
<p>Do you mean we take few more segments from each the 3 phantoms or we should use more phantoms with different densities ???</p>

---

## Post #4 by @lassoan (2020-04-06 17:56 UTC)

<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="11010">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>The method it describe was way too complex for me but the way it was done is very simple.</p>
</blockquote>
</aside>
<p>GelDosimetry allows you to automatically compute the curve on many samples and also evaluates the error and how it is distributed in the image (error may be different in different regions of the phantom). These additional features may also mean more complexity - most importantly, you need a ground truth image of the phantom, which can come from a calibration CT scanner or you can construct it manually.</p>
<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="11010">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Do you mean we take few more segments from each the 3 phantoms or we should use more phantoms with different densities ???</p>
</blockquote>
</aside>
<p>I would recommend to use a phantom with 5-10 different densities to get an idea of the shape of the intensity calibration function. That will help you to decide if line fit is sufficient or you need a polynomial fit.</p>

---

## Post #5 by @cpinter (2020-04-07 13:20 UTC)

<p>The GelDosimetryAnalysis application is closely tailored to the gel dosimetry workflow, which includes one phantom for calibration, and one for the measurement. One calibration phantom is enough, because it measures the photon beam attenuation as a function of depth, and the measurement along the central line is matched with the percent depth dose curve which is given. So it is a quite different workflow then what is needed here. The FilmDosimetryAnalysis application is more similar, in that it manages a list of calibration images for each dose level, but it handles 2D images (film scans) and the workflow is quite fixed.</p>
<p>I think your method makes sense for the current scenario with three phantoms.</p>
<p>Most of the difference between the two programs is probably due to a different selection of calibration ROI. Since the regions contain a lot of noise, the size and position of the segments that you draw may change the values significantly.</p>
<p>Fitting a polynomial on the dat points is quite easy, see <a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysisLogic/GelDosimetryAnalysisLogic.py#L472">for example</a> the way it is done for gel dosimetry.</p>

---
