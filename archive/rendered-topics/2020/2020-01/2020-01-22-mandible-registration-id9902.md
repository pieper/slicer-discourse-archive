# Mandible registration

**Topic ID**: 9902
**Date**: 2020-01-22
**URL**: https://discourse.slicer.org/t/mandible-registration/9902

---

## Post #1 by @Lexus_H (2020-01-22 02:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2531ed8880e91ddff8f4c41289e406ca78c1e514.jpeg" data-download-href="/uploads/short-url/5j2DsaVg2NqZCcYV2YmGPSc0Sag.jpeg?dl=1" title="color map but no defects shown" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2531ed8880e91ddff8f4c41289e406ca78c1e514_2_690x431.jpeg" alt="color map but no defects shown" data-base62-sha1="5j2DsaVg2NqZCcYV2YmGPSc0Sag" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2531ed8880e91ddff8f4c41289e406ca78c1e514_2_690x431.jpeg,  1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2531ed8880e91ddff8f4c41289e406ca78c1e514_2_1380x862.jpeg 2x" data-dominant-color="9E989C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">color map but no defects shown</span><span class="informations">3360×2100 800 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am using dry mandible so predefect and postdefect periodontal bone changes can be superimposed then the difference can be detected in color map.  I have converted CBCT dicom files to gipl then manual approximation then segment using ITK then surface register in stl then harden it using transform then model to model but I still get the color map with only one color(no post periodontal bone defect is shown)<br>
Please let me know if you know what I am doing wrong.</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a></p>

---

## Post #2 by @manjula (2020-01-22 19:11 UTC)

<p>Hi,</p>
<p>The workflow i use which works is,</p>
<ol>
<li>
<p>Import DICOM data</p>
</li>
<li>
<p>registration can be done of the two DICOM image sets with General registration.</p>
</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="cS1l1izbBqk" data-video-title="image registration in 3d slicer, using general registration" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cS1l1izbBqk" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cS1l1izbBqk/maxresdefault.jpg" title="image registration in 3d slicer, using general registration" width="" height="">
  </a>
</div>

<p>or you can go to segmentation editor first and then do the segmentation and make the segments and do the registration,</p>
<p>or</p>
<p>use ITK if you reallywant to segment in that one and import the STL and register the models with</p>
<p>IGT fiducial registration wizard or   CMF registration → surface registration or ROI</p>
<p>I don’t know which way to register is the most accurate will be but we can see the accuracy of the registration once we have the color maps.</p>
<ol start="3">
<li>
<p>Use model to model distance module to measure the difference</p>
</li>
<li>
<p>Load it in the shape population viewer (signed distance)</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1d92c96b8443d3c4f6cabf71ada7886f4a44868.png" data-download-href="/uploads/short-url/n5Maj7OMWlx2Uuizrz1hsHNPAlG.png?dl=1" title="Screenshot from 2020-01-22 20-08-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1d92c96b8443d3c4f6cabf71ada7886f4a44868_2_690x330.png" alt="Screenshot from 2020-01-22 20-08-16" data-base62-sha1="n5Maj7OMWlx2Uuizrz1hsHNPAlG" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1d92c96b8443d3c4f6cabf71ada7886f4a44868_2_690x330.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1d92c96b8443d3c4f6cabf71ada7886f4a44868_2_1035x495.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1d92c96b8443d3c4f6cabf71ada7886f4a44868.png 2x" data-dominant-color="555356"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-01-22 20-08-16</span><span class="informations">1333×639 71.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>you will have to figure out the color map values to make a meaningful conclusion in a case like yours as you are dealing with difficult and highly subjective segmentation.</p>

---

## Post #3 by @Lexus_H (2020-01-24 01:55 UTC)

<p>Thanks for your input.</p>
<p>Does that mean I can just use 3d slicer 4.1 and do all registration and segmentation?</p>
<p>In other words, just foollow step 1 to 4 without using segment editor nor ITK nor CMF?</p>
<p>Please let me know.</p>
<p>Thanks,</p>
<p>ERin</p>

---

## Post #4 by @manjula (2020-01-24 08:00 UTC)

<p>yes you can use just the 3D Slicer for everything you want to do and the workflow will be very less complicated.</p>

---

## Post #5 by @bpaniagua (2020-01-27 13:29 UTC)

<p>Hi <a class="mention" href="/u/erin_hong">@erin_hong</a> and <a class="mention" href="/u/manjula">@manjula</a></p>
<p>I agree with Manjula that the first step here is to see a bit more of what type of distances you have computed. Take into account that the color mapping in SPV by default will happen by setting your highest value in your distances to the color in your colorbar on the right and the lowest to the other end of the colorbar.</p>
<p>Could you please look at the attributes/ranges tab in SPV and see what is your min and max value in the distance map you have calculated, and let us know?</p>
<p>Thanks,<br>
Bea</p>

---

## Post #6 by @Lexus_H (2020-01-28 15:07 UTC)

<p>Please see two screenshots with values for attributes/ranges.</p>
<p>Thanks,</p>
<p>Erin</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e9733bc50aee8675bd57c42ec78cdf6fc800eb5.png" data-download-href="/uploads/short-url/fMktbw1HIPXaRI7KM7exawEJW73.png?dl=1" title="Screen Shot 2020-01-28 at 10.00.52 AM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e9733bc50aee8675bd57c42ec78cdf6fc800eb5_2_690x431.png" alt="Screen Shot 2020-01-28 at 10.00.52 AM.png" data-base62-sha1="fMktbw1HIPXaRI7KM7exawEJW73" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e9733bc50aee8675bd57c42ec78cdf6fc800eb5_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e9733bc50aee8675bd57c42ec78cdf6fc800eb5_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e9733bc50aee8675bd57c42ec78cdf6fc800eb5_2_1380x862.png 2x" data-dominant-color="625379"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-28 at 10.00.52 AM.png</span><span class="informations">3360×2100 537 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93d5dbfa21d1841534859eed3193e652849c2b06.png" data-download-href="/uploads/short-url/l5Onx2f2zbfGd8uW6p7N2u3cUS2.png?dl=1" title="Screen Shot 2020-01-28 at 10.06.55 AM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93d5dbfa21d1841534859eed3193e652849c2b06_2_690x431.png" alt="Screen Shot 2020-01-28 at 10.06.55 AM.png" data-base62-sha1="l5Onx2f2zbfGd8uW6p7N2u3cUS2" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93d5dbfa21d1841534859eed3193e652849c2b06_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93d5dbfa21d1841534859eed3193e652849c2b06_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93d5dbfa21d1841534859eed3193e652849c2b06_2_1380x862.png 2x" data-dominant-color="62537A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-28 at 10.06.55 AM.png</span><span class="informations">3360×2100 542 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @Lexus_H (2020-01-28 15:15 UTC)

<p>These are after I changed my range from -10 to 10.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1400d624e0ad691594995ed0beb76690e54ad2b6.jpeg" data-download-href="/uploads/short-url/2QXlb7q0OExDgX8ZmYHUBadEl3o.jpeg?dl=1" title="Screen Shot 2020-01-28 at 10.14.33 AM.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1400d624e0ad691594995ed0beb76690e54ad2b6_2_690x431.jpeg" alt="Screen Shot 2020-01-28 at 10.14.33 AM.jpg" data-base62-sha1="2QXlb7q0OExDgX8ZmYHUBadEl3o" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1400d624e0ad691594995ed0beb76690e54ad2b6_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1400d624e0ad691594995ed0beb76690e54ad2b6_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1400d624e0ad691594995ed0beb76690e54ad2b6_2_1380x862.jpeg 2x" data-dominant-color="AD848B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-28 at 10.14.33 AM.jpg</span><span class="informations">3360×2100 1.4 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e970653e8ac86008b1dad723cf6a4f86d6e8ce0b.jpeg" data-download-href="/uploads/short-url/xj63wsCOhlMmis4BiThgy4V5khR.jpeg?dl=1" title="Screen Shot 2020-01-28 at 10.14.25 AM.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e970653e8ac86008b1dad723cf6a4f86d6e8ce0b_2_690x431.jpeg" alt="Screen Shot 2020-01-28 at 10.14.25 AM.jpg" data-base62-sha1="xj63wsCOhlMmis4BiThgy4V5khR" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e970653e8ac86008b1dad723cf6a4f86d6e8ce0b_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e970653e8ac86008b1dad723cf6a4f86d6e8ce0b_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e970653e8ac86008b1dad723cf6a4f86d6e8ce0b_2_1380x862.jpeg 2x" data-dominant-color="AD848B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-28 at 10.14.25 AM.jpg</span><span class="informations">3360×2100 1.4 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @bpaniagua (2020-01-28 15:45 UTC)

<p>Hi Erin,</p>
<p>You dont see much because you are visualizing the “normals” map. The magnitude of those maps goes from -1 to 1 (the magnitude of unit vectors pointing in or out)</p>
<p>In the attribute drop down menu, please change to “Signed”, there your values go from -8 to 8 mm (roughly). Play with changing the range to -5 to 5 and you should definitely see something.</p>
<p>Please let us know how it goes,<br>
Bea</p>

---

## Post #9 by @manjula (2020-01-28 18:56 UTC)

<p>In my screenshot above i have rounded in white where you need to change the attribute from normal to signed.  Then changes the value range to -5 to 5 or far as it makes sense in the range section which i have pointed too.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8d7afeddfd9c1c1bf507640418b823b0cb7eb67.png" data-download-href="/uploads/short-url/qnbXF6Qo0ymXXljeScSGZfqFkCH.png?dl=1" title="Screenshot from 2020-01-22 20-08-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d7afeddfd9c1c1bf507640418b823b0cb7eb67_2_690x330.png" alt="Screenshot from 2020-01-22 20-08-16" data-base62-sha1="qnbXF6Qo0ymXXljeScSGZfqFkCH" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d7afeddfd9c1c1bf507640418b823b0cb7eb67_2_690x330.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d7afeddfd9c1c1bf507640418b823b0cb7eb67_2_1035x495.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8d7afeddfd9c1c1bf507640418b823b0cb7eb67.png 2x" data-dominant-color="565357"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-01-22 20-08-16</span><span class="informations">1333×639 79.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Lexus_H (2020-01-29 04:41 UTC)

<p>Hi!</p>
<p>Please see my screenshot below.  The defect change especially <span class="hashtag">#30</span> D is about 5mm so I should see more definite color(green or red) but I do not see it.</p>
<p>Please let me know!</p>
<p>Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3da384e4b941f6960ab11246917271fde377b6a.jpeg" data-download-href="/uploads/short-url/yNdyGjleWXtbYEhZ1AQk0PJ8hoC.jpeg?dl=1" title="Screen Shot 2020-01-28 at 11.33.58 PM.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3da384e4b941f6960ab11246917271fde377b6a_2_690x431.jpeg" alt="Screen Shot 2020-01-28 at 11.33.58 PM.jpg" data-base62-sha1="yNdyGjleWXtbYEhZ1AQk0PJ8hoC" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3da384e4b941f6960ab11246917271fde377b6a_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3da384e4b941f6960ab11246917271fde377b6a_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3da384e4b941f6960ab11246917271fde377b6a_2_1380x862.jpeg 2x" data-dominant-color="A7A1A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-28 at 11.33.58 PM.jpg</span><span class="informations">3360×2100 1.13 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @manjula (2020-01-29 08:16 UTC)

<p>Hi Lexus,</p>
<p>Can you please add a two points to the color map near the median with different color and move it around a bit.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbcbcf9d57f82afc5df18e78988ac8d7becf1d45.png" data-download-href="/uploads/short-url/zVuvven8hhqKOdV3sopuNM0VXoh.png?dl=1" title="Screenshot from 2020-01-29 09-09-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbcbcf9d57f82afc5df18e78988ac8d7becf1d45_2_690x252.png" alt="Screenshot from 2020-01-29 09-09-46" data-base62-sha1="zVuvven8hhqKOdV3sopuNM0VXoh" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbcbcf9d57f82afc5df18e78988ac8d7becf1d45_2_690x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbcbcf9d57f82afc5df18e78988ac8d7becf1d45_2_1035x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbcbcf9d57f82afc5df18e78988ac8d7becf1d45.png 2x" data-dominant-color="4E4E50"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-01-29 09-09-46</span><span class="informations">1035×379 51.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If it does not work i guess there is some problem at Model to model distance measurement step or even at the registration step. If you could share some screenshots of the process or share your models some one might be able to help</p>

---

## Post #12 by @bpaniagua (2020-01-29 13:02 UTC)

<p>Agreeing with Manjula here, continue saturating the color map (go down to -1,1, or lower)  until you see something. It seems to be a difference in the crop between the two models, particularly in the mandibular area towards the chin and that is driving the most of the color interpolation.</p>
<p>Could you please take a snapshot of the two models overlayed with transparency and share that with us??</p>

---

## Post #13 by @Lexus_H (2020-01-30 02:22 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d75b3c1f6da705d4dd8ec059ec03ffdc70e1cc0f.png" data-download-href="/uploads/short-url/uJ87O2u7Pt0XAwA7N6dPpUTUsd9.png?dl=1" title="Screen Shot 2020-01-29 at 9.09.20 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d75b3c1f6da705d4dd8ec059ec03ffdc70e1cc0f_2_690x431.png" alt="Screen Shot 2020-01-29 at 9.09.20 PM.png" data-base62-sha1="uJ87O2u7Pt0XAwA7N6dPpUTUsd9" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d75b3c1f6da705d4dd8ec059ec03ffdc70e1cc0f_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d75b3c1f6da705d4dd8ec059ec03ffdc70e1cc0f_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d75b3c1f6da705d4dd8ec059ec03ffdc70e1cc0f_2_1380x862.png 2x" data-dominant-color="6B5D77"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-29 at 9.09.20 PM.png</span><span class="informations">3360×2100 766 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks for the feedback!</p>
<p>May I have your email address?  I will send you pre and post STL models via google drive. I can also share pre/post dicom files as well, if you want. Perhaps registration and hardening are issues as you both stated.</p>
<p>I will also send you screenshots of each step and send them.  I would like to start from the dicom files.</p>
<p>Many thanks,</p>
<p>Erin</p>

---

## Post #14 by @manjula (2020-01-30 14:12 UTC)

<p>Hi Erin,</p>
<p>I tried with your data. I think it works well. I did not do a good registration so the teeth are not well aligned.  I think there is a error in your workflow. I will try to write the workflow in the afternoon.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/053fe4e65f63eea75e81eb8a69d0f7d4c3ed2dfd.jpeg" data-download-href="/uploads/short-url/KrhlZTgiGrvC2vNQNlBOj5wCTz.jpeg?dl=1" title="Screenshot from 2020-01-30 15-10-03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/053fe4e65f63eea75e81eb8a69d0f7d4c3ed2dfd_2_565x500.jpeg" alt="Screenshot from 2020-01-30 15-10-03" data-base62-sha1="KrhlZTgiGrvC2vNQNlBOj5wCTz" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/053fe4e65f63eea75e81eb8a69d0f7d4c3ed2dfd_2_565x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/053fe4e65f63eea75e81eb8a69d0f7d4c3ed2dfd_2_847x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/053fe4e65f63eea75e81eb8a69d0f7d4c3ed2dfd_2_1130x1000.jpeg 2x" data-dominant-color="43494D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-01-30 15-10-03</span><span class="informations">1206×1067 330 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @Lexus_H (2020-01-30 16:25 UTC)

<p>Looking forward to a more detailed workflow.  Since I am working with CBCT scans not CT nor MRI, I was using Slicer CMF, FYI.</p>
<p>Thanks,</p>
<p>Erin</p>

---

## Post #16 by @bpaniagua (2020-01-30 17:54 UTC)

<p>Hi all,</p>
<p>Manjula, thanks for that snapshot. The registration seems wrong, as illustrated for a pattern of positive distances parallel to the longest axis of the model. Erin, is it possible to see both of your models?</p>
<p>Also, have you tried to manually approximating your models to see if you can generate a better colormap?</p>
<p>Thanks,<br>
Bea</p>

---

## Post #17 by @manjula (2020-01-30 19:47 UTC)

<p>yes registration is wrong. i did not did the registration properly. it was just a quick test !</p>

---

## Post #18 by @manjula (2020-01-30 21:02 UTC)

<p>Hi <a class="mention" href="/u/lexus_h">@Lexus_H</a>  and <a class="mention" href="/u/bpaniagua">@bpaniagua</a></p>
<p>Sorry i was bit busy.</p>
<p>I did use the models Erin send for registration with CMF Regis - surface registration</p>
<p>With max iterations and max landmarks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8206cd6c11e4129b82c01da7e22c3eb2d4dc5cba.jpeg" data-download-href="/uploads/short-url/iygE0wA9sav3KEkSTMVXlHB7RXA.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8206cd6c11e4129b82c01da7e22c3eb2d4dc5cba_2_690x428.jpeg" alt="Screenshot" data-base62-sha1="iygE0wA9sav3KEkSTMVXlHB7RXA" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8206cd6c11e4129b82c01da7e22c3eb2d4dc5cba_2_690x428.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8206cd6c11e4129b82c01da7e22c3eb2d4dc5cba_2_1035x642.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8206cd6c11e4129b82c01da7e22c3eb2d4dc5cba.jpeg 2x" data-dominant-color="9B8DB2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1332×828 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please see the video</p>
<p>            <iframe src="https://www.youtube.com/embed/JST4mpQrMUs?feature=oembed&amp;wmode=opaque" width="480" height="360" frameborder="0" allowfullscreen="" class="youtube-onebox" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>
<p>The registration is not good. This is similar to problem i encountered with my previous work.</p>
<aside class="quote quote-modified" data-post="5" data-topic="9424">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/revisiting-rigid-mesh-registration/9424/5">Revisiting Rigid Mesh Registration</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    <a class="mention" href="/u/lassoan">@lassoan</a> 
These are the results I get with the cloud compare fine registration with RMS. As you can see when i look at the model to model distance and view it in shape population viewer with the same setting… our land marks show almost exact matches ( Green ) in the viewer. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6032afd17d99626c43152c7376cc69a11673b5e9.png" data-download-href="/uploads/short-url/dJ0qQSmPcSRQ57o8qPCSm90nWm5.png?dl=1" title="Screenshot from 2019-12-08 13-16-08" rel="noopener nofollow ugc">[Screenshot from 2019-12-08 13-16-08]</a> <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42bdc7101eb0a609528bd60a6c9461dcc1841c9e.png" data-download-href="/uploads/short-url/9wq6Nx92YFzxVh6MndqAZznlMdg.png?dl=1" title="Screenshot from 2019-12-08 13-15-52" rel="noopener nofollow ugc">[Screenshot from 2019-12-08 13-15-52]</a> 
<a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae13521e98b27443c7f8f6d26d1d439d2ebe8bc9.png" data-download-href="/uploads/short-url/oPWtpJCKn4LmyqmhdQJUVV1xdXz.png?dl=1" title="Screenshot from 2019-12-08 13-17-27" rel="noopener nofollow ugc">[Screenshot from 2019-12-08 13-17-27]</a> <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4ba7e585f5ef56784afc255624a62e0a86899099.jpeg" data-download-href="/uploads/short-url/aNhwFVKze00WvU5cp7SfXz13xlD.jpeg?dl=1" title="Screenshot from 2019-12-08 13-22-16" rel="noopener nofollow ugc">[Screenshot from 2019-12-08 13-22-16]</a> 
I get almost same resutls with the cloud compare iteration method al…
  </blockquote>
</aside>

<p>I solve my problem with cloud compare but i wanted to stick to one software for my work and i got good results with CMR- ROI registration.</p>
<p>In this case i did not do the ROI registration because i again encountered the bug that i reported on this some time back.</p>
<aside class="quote" data-post="1" data-topic="9443">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/cmfreg-roi-registration-bug/9443">CMFReg - ROI registration Bug</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    There is a bug with CMF reg ROI registration method. I found this in the stable version as well as the nightly build.  This is from the nightly build. 
Landmarks ROI does change dynamically and is kept at a fixed value. Can some one please tell me how to fix this ? ROI is stuck at 10. 
I did get rid of the all the configurations files and started with fresh install. (i am using Linux)
  </blockquote>
</aside>

<p>I use these models in cloud compare even with default setting i got good results.</p>
<p>please check the color maps with both registration methods</p>
<p>            <iframe src="https://www.youtube.com/embed/qU1iyDtL6Us?feature=oembed&amp;wmode=opaque" width="480" height="360" frameborder="0" allowfullscreen="" class="youtube-onebox" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>
<p>Erin i think you can try CMF ROI method. I think it should work pretty well.</p>
<p>Also since you have DICOM data why don’t you do the Image registration (General Registration -BRAINS) and then do the segmentation. Then your segments will be created properly registered. It would be great if <a class="mention" href="/u/bpaniagua">@bpaniagua</a> or Prof <a class="mention" href="/u/lassoan">@lassoan</a> can tell further about this.</p>
<p>Is registration on DICOM will be more accurate than registering the Surface models/Segments ?</p>
<p>Despite the answer to me previously by Prof Lasso on registration i am still baffled by the accuracy of cloud compare registration over CMF Surface registration. <img src="https://emoji.discourse-cdn.com/twitter/star_struck.png?v=14" title=":star_struck:" class="emoji" alt=":star_struck:" loading="lazy" width="20" height="20"></p>
<p>In any case the problem that we set out to see seems like you are not measuring the model to model distance properly. Please see the video.</p>
<p>            <iframe src="https://www.youtube.com/embed/-KhemBa7wbs?feature=oembed&amp;wmode=opaque" width="480" height="360" frameborder="0" allowfullscreen="" class="youtube-onebox" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>

---

## Post #19 by @lassoan (2020-01-30 21:44 UTC)

<aside class="quote no-group" data-username="manjula" data-post="18" data-topic="9902">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Is registration on DICOM will be more accurate than registering the Surface models/Segments ?</p>
</blockquote>
</aside>
<p>Image registration would try to align soft tissues as well, so you would need to apply masking, but that would be essentially the same kind of thresholding that you do to extract the surface. Image-based registration would be also more vulnerable to image artifacts (due to presence of metals). So, unless you register a small region, such as a single tooth, surface registration is probably more appropriate. It also allows you to use the same method to register CBCT/CBCT and CBCT/intra-oral surface scan.</p>
<aside class="quote no-group" data-username="manjula" data-post="18" data-topic="9902">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Despite the answer to me previously by Prof Lasso on registration i am still baffled by the accuracy of cloud compare registration over CMF Surface registration. <img src="https://emoji.discourse-cdn.com/twitter/star_struck.png?v=14" title=":star_struck:" class="emoji" alt=":star_struck:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>Rigid surface registration of low-noise surfaces with good initialization is trivial, using ICP. Maybe the problem is that the cut surface is included in the registration, which of course must be excluded because they are not exactly the same on the two models. If you cut those off (leaving the cut-off ends open) then registration must be accurate.</p>
<p>It would be nice to add a surface selection tool to SlicerCMF that would allow to select a part of a surface for registration.</p>

---

## Post #20 by @manjula (2020-01-30 22:18 UTC)

<p>Thank you for the explanations. First questions is answered understood.</p>
<p>With regard to second question i am not sure what you meant by the cut surface ?</p>
<p>In any case the way i understood was the anterior and posterior ends of the mandible.</p>
<p>So i just  clipped around the teeth and did the CMF surface registration with 4000 iterations and the results were much  better.  Then i applied the transform to the whole model and got a much better color map. I dont know is that what you meant.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e9a5d43bbe924796b78b63f7fc10ed71275add4.png" data-download-href="/uploads/short-url/25bpkG7gLqUR6oQhQaAgXp5K0T2.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e9a5d43bbe924796b78b63f7fc10ed71275add4_2_675x500.png" alt="Screenshot" data-base62-sha1="25bpkG7gLqUR6oQhQaAgXp5K0T2" width="675" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e9a5d43bbe924796b78b63f7fc10ed71275add4_2_675x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e9a5d43bbe924796b78b63f7fc10ed71275add4_2_1012x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e9a5d43bbe924796b78b63f7fc10ed71275add4.png 2x" data-dominant-color="9E9CCA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1160×858 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dacaf4f531076f0544d8638624a7b2881b063d82.jpeg" data-download-href="/uploads/short-url/vdwV8Mh93t9vdfsNp31vaciWQIW.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dacaf4f531076f0544d8638624a7b2881b063d82_2_690x478.jpeg" alt="Screenshot_1" data-base62-sha1="vdwV8Mh93t9vdfsNp31vaciWQIW" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dacaf4f531076f0544d8638624a7b2881b063d82_2_690x478.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dacaf4f531076f0544d8638624a7b2881b063d82_2_1035x717.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dacaf4f531076f0544d8638624a7b2881b063d82.jpeg 2x" data-dominant-color="347336"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1236×858 309 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And ofcourse if we can select the surface then it will absolutely solve this problem i guess… <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #21 by @Lexus_H (2020-01-31 00:07 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4.jpeg" data-download-href="/uploads/short-url/vdsF93MFdRajCnawsG5k6afoBfK.jpeg?dl=1" title="Screen Shot 2020-01-30 at 6.45.07 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_690x431.jpeg" alt="Screen Shot 2020-01-30 at 6.45.07 PM.png" data-base62-sha1="vdsF93MFdRajCnawsG5k6afoBfK" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_1380x862.jpeg 2x" data-dominant-color="ACADC7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-30 at 6.45.07 PM.png</span><span class="informations">3360×2100 655 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is surface registration which I could not get it to register well.  Please notice the transparent model that did not superimpose well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83.jpeg" data-download-href="/uploads/short-url/o1PuHFoRiuTLujmDll5Zkszvbl9.jpeg?dl=1" title="Screen Shot 2020-01-30 at 6.50.31 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_690x431.jpeg" alt="Screen Shot 2020-01-30 at 6.50.31 PM.png" data-base62-sha1="o1PuHFoRiuTLujmDll5Zkszvbl9" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_1380x862.jpeg 2x" data-dominant-color="ABADC6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-30 at 6.50.31 PM.png</span><span class="informations">3360×2100 660 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is a registered post defect model with CMF fiducial registration which I believe, works better than ROI.  Do I have to see transparent gray for pre defect model?</p>
<p>Dr. P, yes I manually approximated before I segmented both images then created STL for surface registration, in this case, I used fiducial registration.</p>
<p>Even Prof. Lassoan stated that I should use surface registration but somehow surface registration is not giving me a good result.   Also, I even clipped to make the two models more even at the borders(distal to molars and mesial to anteriors)</p>
<p>Hi Manjula, I will try general registration using DICOM files.  your recommended video clip does not have voice recorded so it is kind of hard for me to follow.  Also, should I use slicer CMF for general registration or just slicer?</p>
<p>Can you also explain to me what cloud compare is?</p>
<p>Many thanks,</p>
<p>If anyone is willing to try with dicom files to evaluate whether my work step was OK or not, please let me know, I can transfer them via google drive link.  Since I sent my stls and my registered and clipped model and model to model is simply plugging your models in order to generate vtk file for SPV, I do not know what I’m doing wrong.  Only the periodontal defect is the change and that should be colored based on the depth and allocated color in the color bar not the rest of the mandible (teeth can move bc it is dry mandible but not as much as defect sizes up to 9mm).</p>

---

## Post #22 by @Lexus_H (2020-01-31 00:13 UTC)

<p>Hi Manjula,</p>
<p>Are you able to send me the surface registered model to me so I can play around with it to see if the periodontal bone defect matches my gold standard?</p>
<p>Since I just realized that your maximum was -4 to 4, it colored the same as red.</p>
<p>I believe you have my email address from the google drive link.</p>
<p>Thanks,</p>
<p>Erin</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4.jpeg" data-download-href="/uploads/short-url/vdsF93MFdRajCnawsG5k6afoBfK.jpeg?dl=1" title="Screen Shot 2020-01-30 at 6.45.07 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_690x431.jpeg" alt="Screen Shot 2020-01-30 at 6.45.07 PM.png" data-base62-sha1="vdsF93MFdRajCnawsG5k6afoBfK" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_1380x862.jpeg 2x" data-dominant-color="ACADC7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-30 at 6.45.07 PM.png</span><span class="informations">3360×2100 655 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83.jpeg" data-download-href="/uploads/short-url/o1PuHFoRiuTLujmDll5Zkszvbl9.jpeg?dl=1" title="Screen Shot 2020-01-30 at 6.50.31 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_690x431.jpeg" alt="Screen Shot 2020-01-30 at 6.50.31 PM.png" data-base62-sha1="o1PuHFoRiuTLujmDll5Zkszvbl9" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_1380x862.jpeg 2x" data-dominant-color="ABADC6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-30 at 6.50.31 PM.png</span><span class="informations">3360×2100 660 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @Lexus_H (2020-01-31 15:24 UTC)

<p>Hi Manjula,</p>
<p>This is a color map page using slicer CMF 5.0 that i generated using Manjula’s registered models using cloud compare.  Not much better as you can see.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2531ed8880e91ddff8f4c41289e406ca78c1e514.jpeg" data-download-href="/uploads/short-url/5j2DsaVg2NqZCcYV2YmGPSc0Sag.jpeg?dl=1" title="color map but no defects shown.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2531ed8880e91ddff8f4c41289e406ca78c1e514_2_690x431.jpeg" alt="color map but no defects shown.png" data-base62-sha1="5j2DsaVg2NqZCcYV2YmGPSc0Sag" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2531ed8880e91ddff8f4c41289e406ca78c1e514_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2531ed8880e91ddff8f4c41289e406ca78c1e514_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2531ed8880e91ddff8f4c41289e406ca78c1e514_2_1380x862.jpeg 2x" data-dominant-color="9E989C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">color map but no defects shown.png</span><span class="informations">3360×2100 800 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4.jpeg" data-download-href="/uploads/short-url/vdsF93MFdRajCnawsG5k6afoBfK.jpeg?dl=1" title="Screen Shot 2020-01-30 at 6.45.07 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_690x431.jpeg" alt="Screen Shot 2020-01-30 at 6.45.07 PM.png" data-base62-sha1="vdsF93MFdRajCnawsG5k6afoBfK" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dac8f82ec179ad0a1e1e27a807af8dcce8aa3ed4_2_1380x862.jpeg 2x" data-dominant-color="ACADC7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-30 at 6.45.07 PM.png</span><span class="informations">3360×2100 655 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83.jpeg" data-download-href="/uploads/short-url/o1PuHFoRiuTLujmDll5Zkszvbl9.jpeg?dl=1" title="Screen Shot 2020-01-30 at 6.50.31 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_690x431.jpeg" alt="Screen Shot 2020-01-30 at 6.50.31 PM.png" data-base62-sha1="o1PuHFoRiuTLujmDll5Zkszvbl9" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8692615a16740d2332eaec2320c0f1f870f0a83_2_1380x862.jpeg 2x" data-dominant-color="ABADC6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-30 at 6.50.31 PM.png</span><span class="informations">3360×2100 660 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @manjula (2020-01-31 15:33 UTC)

<p>Well i think you are not doing it properly somewhere because this is what you should see if done correctly</p>
<div class="lazyYT" data-youtube-id="qU1iyDtL6Us" data-youtube-title="out" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Also you need to change the attribute to signed and also the figure you see is just a scale not in millimeters or anything.<br>
x 0.5 is the center (Superimposed) and to either side you get the deviation by the percentage.</p>
<p>if the range is for e.g -5 to 5 in mm then at ever 0.1 position you will move 1 mm + or -</p>

---
