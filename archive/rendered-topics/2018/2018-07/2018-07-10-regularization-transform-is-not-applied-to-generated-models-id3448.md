---
topic_id: 3448
title: "Regularization Transform Is Not Applied To Generated Models"
date: 2018-07-10
url: https://discourse.slicer.org/t/3448
---

# Regularization transform is not applied to generated models

**Topic ID**: 3448
**Date**: 2018-07-10
**URL**: https://discourse.slicer.org/t/regularization-transform-is-not-applied-to-generated-models/3448

---

## Post #1 by @lukebo (2018-07-10 14:52 UTC)

<p>Hi everybody,<br>
I have CT data which was obtained with a somehow tilted gantry and also with two different slice thicknesses within one series.</p>
<p>During the examination of the series in the DICOM-Browser, Slicer notes, that there are irregularities in the slice thickness and that transforms will be applied.</p>
<p>When I enter the models module, a warning appears several times: “Geometry of master and merge model volumes do not match. Transform mismatch”.</p>
<p>I used “Apply regularization transform” in the DICOM Settings and tried several Dicom Reader approaches. Using DCMTK and the activated transform, the views in the red, yellow and green box look good, at least visually. However, when I now try to create a model, let’s say bone from some HU to some higher HU, the model looks distorted. Slicer seems to apply the thickness of the first half of the volume also to the other half which then looks compressed in the z direction.<br>
Am I too stupid or is this a general problem? What am I doing wrong?<br>
Thanks for your help.</p>

---

## Post #2 by @lassoan (2018-07-10 15:09 UTC)

<p>It seems that you try to use the legacy Editor module. Please use Segment Editor module instead and the error should not occur.</p>
<p>Probably you’ve done it already, but just in case, check that you’ve enabled application of regularization transform (menu: Edit / Application settings / DICOM / Acquisition geometry regularization =&gt; apply regularization transform).</p>
<p>I would also recommend to go to Transforms module and harden the acquisition transform on your volume - it resamples the volume on a regularly spaced grid, avoiding all complications that may be caused by non-uniform spacing (you may need a recent Slicer nightly build for this to work well).</p>

---

## Post #3 by @lukebo (2018-07-11 06:49 UTC)

<p>Thank you so much Andreas,<br>
this almost solves the problem.<br>
Let me ask a probably easy follow up question: I press the “+ Add” button. Then i press “Threshold” and set the threshold to eg 200 - Max HU. The slices in the red, yellow and green box look good and everything is correctly marked. Then i hit “Apply”. Now, only the lower half of my volume (with higher slice density) is selected/colored and when i click “show 3d”, only the lower half of the model is rendered.<br>
There is only one master volume available.</p>
<p>(I now use DCMTK and the apply transform option in the segment editor. I did not try the transforms-module so far, as i need some deeper stufy of the manual first.)</p>
<p>Thank you very much for you help!</p>

---

## Post #4 by @lassoan (2018-07-12 02:59 UTC)

<aside class="quote no-group" data-username="lukebo" data-post="3" data-topic="3448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/fbc32d/48.png" class="avatar"> lukebo:</div>
<blockquote>
<p>Then i hit “Apply”. Now, only the lower half of my volume (with higher slice density) is selected/colored and when i click “show 3d”, only the lower half of the model is rendered.</p>
</blockquote>
</aside>
<p>It seems that Segment editor does not fully support editing non-linearly transformed volume (it does not compute the extent properly). For now, the simplest would be to harden the acquisition transform on the volume before you start segmentation.</p>

---

## Post #5 by @lukebo (2018-07-12 06:23 UTC)

<p>Thanks Andras for your support. I will try the transform.<br>
Best regards!</p>

---

## Post #6 by @lukebo (2018-10-17 14:10 UTC)

<p>Works perfectly! Thanks!!!</p>

---

## Post #7 by @DonaldHume (2019-05-29 22:58 UTC)

<p>Hi, I’m having similar issues to OP and was hoping someone might help me. I also have a scan with variable slice thickness through maybe 4 different regions of the scan. I was able to successfully regularize geometry upon read in. However when I begin to segment (and upon closer inspection of the RYG views) there are gaps in my volume as seen here <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/050fc62ffe5ba34086af309638b5419a0922436f.png" alt="2019-05-29_1656" data-base62-sha1="IMbmOGs0DwPZAil9nmBKDlm5DF" width="609" height="309"></p>
<p>I’m wondering if I also need to harden my series, but I can’t seem to figure out how to do that. When I go to the Transform tab everything is greyed out and not accessible. Any advice would be appreciated!</p>
<p>Thanks</p>

---

## Post #8 by @lassoan (2019-05-30 03:53 UTC)

<aside class="quote no-group" data-username="DonaldHume" data-post="7" data-topic="3448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/donaldhume/48/3846_2.png" class="avatar"> DonaldHume:</div>
<blockquote>
<p>When I go to the Transform tab everything is greyed out and not accessible.</p>
</blockquote>
</aside>
<p>You need to select the transform next to “Active Transform” label, then scroll down to “Apply transform” section. You can harden a transform with less clicks in Data module: double-click on the transform icon in the transforms column and choose “Harden transform”.</p>
<p>The screenshot above indicates that there might be something wrong with the frames. Maybe there are some extra frames in the sequence that don’t belong there (sometimes localizer images got mixed into the 3D series). Check slice positions in the <a href="https://discourse.slicer.org/t/how-to-adjust-the-distorted-image/817/44">DICOM browser’s metadata viewer</a>.</p>

---

## Post #9 by @DonaldHume (2019-05-30 17:48 UTC)

<p>Hi Andras, I believe you are correct:</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="3448" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe there are some extra frames in the sequence that don’t belong there (sometimes localizer images got mixed into the 3D series). Check slice positions in the <a href="https://discourse.slicer.org/t/how-to-adjust-the-distorted-image/817/44">DICOM browser’s metadata viewer</a>.</p>
</blockquote>
</aside>
<p>I’ve found that the sections of the scan with changing slice thickness sometimes have double frames (same location) and sometimes overlap in the transitional region … likely convoluting the linearization. Here’s an example I found:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Slice #</th>
<th>Location</th>
<th>Thickness</th>
</tr>
</thead>
<tbody>
<tr>
<td>60</td>
<td>-422.5</td>
<td>2.5</td>
</tr>
<tr>
<td>61</td>
<td>-420</td>
<td>2.5</td>
</tr>
<tr>
<td>62</td>
<td>-418.125</td>
<td>5</td>
</tr>
<tr>
<td>63</td>
<td>-417.5</td>
<td>2.5</td>
</tr>
<tr>
<td>64</td>
<td>-413.125</td>
<td>5</td>
</tr>
<tr>
<td>65</td>
<td>-408.125</td>
<td>5</td>
</tr>
</tbody>
</table>
</div><p>Is there a way for me to fix this in Slicer3D, so that I might then linearize it properly? I appreciate your feedback, thank you.</p>

---

## Post #10 by @lassoan (2019-05-30 17:54 UTC)

<p>Varying spacing is not an issue but if there are duplicate frames or highly non-parallel (e.g., orthogonal) planes then they should be removed. If they are separated based on acquisition time then you can split up the series (menu: Application settings / DICOM / Allow subseries loading by time -&gt; enable; in DICOM module: enable Advanced option, click Examine, and see if there is a subseries listed that is usable). If this does not work then you may need to manually delete the DICOM file before importing the DICOM folder into Slicer (and next time play with data export parameters in the CT scanner to prevent mixing in the extra slices in the volumetric acquisition).</p>

---

## Post #11 by @DonaldHume (2019-05-30 18:49 UTC)

<p>Thank you for the feedback; I’ll explore some of those suggestions.</p>

---
