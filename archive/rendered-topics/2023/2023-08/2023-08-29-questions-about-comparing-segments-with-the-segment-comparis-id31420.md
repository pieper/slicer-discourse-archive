# Questions about comparing segments with the Segment Comparison module

**Topic ID**: 31420
**Date**: 2023-08-29
**URL**: https://discourse.slicer.org/t/questions-about-comparing-segments-with-the-segment-comparison-module/31420

---

## Post #1 by @shahrokh (2023-08-29 09:48 UTC)

<p>Hello<br>
Dear Developers and Users</p>
<p>Is it possible to compare the segment of a specific organ, e.g. liver, (from CT images) in two different patients?</p>
<p>Basically, is it reasonable to directly compare such segments (from two different patients) using the <strong>Segment Comparison</strong> module? Because the coordinate space of patients’ CT images seems to be different, it may not be correct to do this and maybe it is necessary, for example, to equalize the centers of the image space at firstly.</p>
<p>I investigated this by following the steps below.</p>
<p><strong>1-</strong> I once compared the liver segments of two patients, without doing anything, with <strong>Segment Comparison</strong> module. Their Dice coefficient was equal to <strong>zero</strong>.</p>
<p><strong>2-</strong> Once again, I first converted the segments of two patients into <em>labelMapVolume</em>. Then I converted both to <em>Volume</em> and used <strong>Center Volume</strong> option in <strong>Volume</strong> module. I re-segmented the resulting nodes with the <strong>Threshold</strong> filter in the <strong>Segment Editor</strong> module with lower and upper limits equal to 1. Finally, I calculated Dice Coefficient with <strong>Segment Comparison</strong> module. This coefficient was equal to 0.566832.</p>
<p>Based on this experience, I concluded that the spatial position of the two segments is dependent on the coordinate space of the initial CT images of the two patients, and this issue completely affects the value of the Dice coefficient.</p>
<p>Please guide me in understanding this difference.</p>
<p>My main question is this:<br>
How can I calculate the similarity of two segments without this dependency?</p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh.</p>

---

## Post #2 by @cpinter (2023-08-29 09:53 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="31420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>equalize the centers of the image space</p>
</blockquote>
</aside>
<p>I think what you need to do is proper registration of the two patients. You can read about this concept here <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>
<p>If you want to focus on just one organ, instead of trying to do a good global registration, you can use the Segment Registration module from the <a href="https://github.com/SlicerRt/SegmentRegistration">extension</a> that has the same name.</p>

---

## Post #3 by @shahrokh (2023-08-29 12:12 UTC)

<p>Thank you very much Csaba for your guidances.<br>
As you suggested, I first used the <strong>Segment Registration</strong> module to register the segments.<br>
Assume that the input data includes the following:</p>
<p>Patient 07:<br>
CT07.nii (Information: 128x128x108, 3.912x3.912x5.000 mm)<br>
SegpCT07.seg.nrrd</p>
<p>Patient 45:<br>
CT45.nii (Information: 512x512x127, 0.978x0.978x5.000 mm)<br>
SegpCT45.seg.nrrd</p>
<p>The input data to 3DSlicer is shown in the figure below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ef80367dd7e8b166f25a368add50e24f904ba69.png" data-download-href="/uploads/short-url/6Hvkrl4yWIlR7vdrqoSSJpo57EB.png?dl=1" title="s01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef80367dd7e8b166f25a368add50e24f904ba69_2_690x437.png" alt="s01" data-base62-sha1="6Hvkrl4yWIlR7vdrqoSSJpo57EB" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef80367dd7e8b166f25a368add50e24f904ba69_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef80367dd7e8b166f25a368add50e24f904ba69_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ef80367dd7e8b166f25a368add50e24f904ba69.png 2x" data-dominant-color="9D9D9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">s01</span><span class="informations">1124×713 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The input data to the <strong>Segment Registration</strong> module is shown in the figure below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2918a6aec0cd2dfc4f7910be98214a63159e0d06.png" data-download-href="/uploads/short-url/5Ryof8DsTYRgf2jyQY6yJi6m7hs.png?dl=1" title="s2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2918a6aec0cd2dfc4f7910be98214a63159e0d06_2_584x499.png" alt="s2" data-base62-sha1="5Ryof8DsTYRgf2jyQY6yJi6m7hs" width="584" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2918a6aec0cd2dfc4f7910be98214a63159e0d06_2_584x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2918a6aec0cd2dfc4f7910be98214a63159e0d06.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2918a6aec0cd2dfc4f7910be98214a63159e0d06.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">s2</span><span class="informations">621×531 50.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Click on <strong>Perform Registration</strong> to start the process. In this registration, the <strong>Rigid</strong> option is <strong>disabled</strong> (I do not want the geometry of the segment to change in any way, then I must select Rigid option). The result is shown in the figure below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60c748b4474f5a3b42bd61a9652f1701e688bb5e.png" data-download-href="/uploads/short-url/dO8NFGeoGRw5PpFxM6Vr4XNB8Sy.png?dl=1" title="s3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60c748b4474f5a3b42bd61a9652f1701e688bb5e_2_690x438.png" alt="s3" data-base62-sha1="dO8NFGeoGRw5PpFxM6Vr4XNB8Sy" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60c748b4474f5a3b42bd61a9652f1701e688bb5e_2_690x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60c748b4474f5a3b42bd61a9652f1701e688bb5e_2_1035x657.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60c748b4474f5a3b42bd61a9652f1701e688bb5e.png 2x" data-dominant-color="A4A2A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">s3</span><span class="informations">1373×873 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As mentioned above, I just want the registration to be done via <strong>Rigid Transform</strong> only. So the <strong>Rigid</strong> option was selected and <strong>Perform Registration</strong> was done again. <strong>Is this correct?</strong></p>
<p>As you can see In the picture before the picture above, the <strong>Rigid</strong> option is disabled and this <strong>Rigid</strong> option is enabled for me after completing the previous step. The result of this step and the resulting outputs are shown in the following figure:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b54fb30b6b4d072c16e42d1627e53a8a9401c60.png" data-download-href="/uploads/short-url/6bkBmx8DCkwaEkPceKXAdEMFl4s.png?dl=1" title="s4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b54fb30b6b4d072c16e42d1627e53a8a9401c60_2_690x438.png" alt="s4" data-base62-sha1="6bkBmx8DCkwaEkPceKXAdEMFl4s" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b54fb30b6b4d072c16e42d1627e53a8a9401c60_2_690x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b54fb30b6b4d072c16e42d1627e53a8a9401c60_2_1035x657.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b54fb30b6b4d072c16e42d1627e53a8a9401c60.png 2x" data-dominant-color="A1A2A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">s4</span><span class="informations">1373×873 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now I will segment two nodes named <em>Fixed_Structure_Padded_1-Cropped</em> and <em>Moving_Structure_Padded_1-Cropped</em>.</p>
<p>The result is shown in the figure below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63d4c12ef91552c5d5a926b5578d6e2d0667553b.png" data-download-href="/uploads/short-url/ef95QiT8Ltkw69J6RcPxXW2PRfZ.png?dl=1" title="s5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63d4c12ef91552c5d5a926b5578d6e2d0667553b_2_690x306.png" alt="s5" data-base62-sha1="ef95QiT8Ltkw69J6RcPxXW2PRfZ" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63d4c12ef91552c5d5a926b5578d6e2d0667553b_2_690x306.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63d4c12ef91552c5d5a926b5578d6e2d0667553b_2_1035x459.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63d4c12ef91552c5d5a926b5578d6e2d0667553b.png 2x" data-dominant-color="A5A4A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">s5</span><span class="informations">1131×503 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the last step, the <strong>Segment Comparison</strong> module was used with the following settings and output.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63e725a1f7376314af7d2fdc42939a0cf4445e0d.png" data-download-href="/uploads/short-url/efMuZ0Uc9P8p8FqPIAyZFikooDX.png?dl=1" title="s6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63e725a1f7376314af7d2fdc42939a0cf4445e0d_2_419x500.png" alt="s6" data-base62-sha1="efMuZ0Uc9P8p8FqPIAyZFikooDX" width="419" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63e725a1f7376314af7d2fdc42939a0cf4445e0d_2_419x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63e725a1f7376314af7d2fdc42939a0cf4445e0d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63e725a1f7376314af7d2fdc42939a0cf4445e0d.png 2x" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">s6</span><span class="informations">620×739 85.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you think these steps are correct, specially selecting the <strong>Rigid</strong> option in the second use of the <strong>Segment Registration</strong> module?</p>
<p>If the above steps are correct, how can I do the last step via command line? In other words, can the <strong>Segment Comparison</strong> module be executed through the command line?<br>
The reason for this requirement is that my data is relatively large and doing these steps through the GUI is time-consuming.</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #4 by @cpinter (2023-08-29 13:40 UTC)

<p>It seems correct to me. When you change the type of registration from deformable to rigid, it is only a visualization thing, meaning that the deformable registration is simply not applied. So no need to do the perform registration step again.</p>

---

## Post #5 by @shahrokh (2023-08-29 15:44 UTC)

<p>Thanks a lot Csaba for your reply.</p>
<p>Please guide me regarding my last question.<br>
As mentioned in my message, how can I do two steps including as  at first <strong>Segment Registration</strong> and then  <strong>Segment Comparison</strong> modules in command line of terminal.<br>
As mentioned, I have a lot of data of images for which I have to calculate the dice coefficient in pairs. It would be nice to be able to do these steps (two modules) in the command line.</p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh.</p>

---

## Post #6 by @Young_Wang (2023-12-13 23:08 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="3" data-topic="31420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Segment Comparison</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/shahrokh">@shahrokh</a>, hi there. which version did you use? I’m using 5.6 and I can’t seem to find this <strong>Segment Registration</strong> module anymore.</p>

---
