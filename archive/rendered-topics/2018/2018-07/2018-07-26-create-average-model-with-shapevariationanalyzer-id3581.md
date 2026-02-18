# Create average model with shapevariationanalyzer

**Topic ID**: 3581
**Date**: 2018-07-26
**URL**: https://discourse.slicer.org/t/create-average-model-with-shapevariationanalyzer/3581

---

## Post #1 by @aseman (2018-07-26 08:27 UTC)

<p>Slicer version:4.8.1<br>
Hi 3D slicer experts:<br>
I want to compare the average of two group models to each other, so I use the shapevariationanalyzer module for computing the average models . It computes the mean group for me without any error ; but it doesn’t show the mean in the preview of Group’s mean Tab( even it doesn’t show any scene in this Tab). How I can see the mean group?<br>
thanks</p>

---

## Post #2 by @aseman (2018-08-02 18:28 UTC)

<p>Hi 3D slicer experts<br>
Unfortunately , I didn’t recieve any feedbacks for my question. I compute the average of models with shapevariationanalyzer module without error, but it doesn’t show any scene ; and the output csv and vtk file (Mean Groups. csv and  meanGroup [i] .vtk) is empty(the number of points is zero).Have you any idea about this problem?<br>
thanks a lot</p>

---

## Post #3 by @lassoan (2018-08-03 18:15 UTC)

<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> can you help?</p>

---

## Post #4 by @fedorov (2018-08-03 18:36 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> should this topic be moved from “Support” to the <a href="https://discourse.slicer.org/c/community/slicer-salt">“SlicerSALT” community</a> instead of assigning the “slicersalt” tag?</p>

---

## Post #5 by @lassoan (2018-08-03 21:12 UTC)

<p>Good point, I’ll update the tag, see if it helps reducing the response time.</p>

---

## Post #6 by @bpaniagua (2018-08-16 19:30 UTC)

<p>Hi all,</p>
<p>Sorry for the delay in replying. <a class="mention" href="/u/juanprietob">@juanprietob</a> could you please address this question?<br>
Thank you,</p>
<p>Bea</p>

---

## Post #7 by @bpaniagua (2018-08-16 19:31 UTC)

<p>Aseman,</p>
<p>Could you please tell us more about your input data?<br>
Thank you,</p>
<p>Bea</p>

---

## Post #8 by @juanprietob (2018-08-17 14:20 UTC)

<p>Hi,<br>
I can help you solve this issue. Do you know if your input shapes have the same number of points? Otherwise this module won’t work.</p>

---

## Post #9 by @aseman (2018-08-22 17:06 UTC)

<p>Hi,<br>
Execuse me for the delay in repliying. I have a number of heart models(vtk files) , Figure 1 at the bottom, and I could calculate the average of them using the shapevariationAnalyzer module(Figure 2 at the bottom) . for this purpose I converted  vtk files into the csv files using the creation of csv file for classification Groups Tab. then calculted the average using the computation of mean group Tab.but this average is irregular and does not look like the shape of the input heart models.<br>
1-is the mean obtained correct?<br>
2-is it’s irregular shape because of inadequate input data?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b387c60ebd967d7c9d34c9f080d54514413026de.png" data-download-href="/uploads/short-url/pCcmnseCxEkCoQWfUnQWy3btQpo.png?dl=1" title="figure1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b387c60ebd967d7c9d34c9f080d54514413026de_2_690x438.png" alt="figure1" data-base62-sha1="pCcmnseCxEkCoQWfUnQWy3btQpo" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b387c60ebd967d7c9d34c9f080d54514413026de_2_690x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b387c60ebd967d7c9d34c9f080d54514413026de.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b387c60ebd967d7c9d34c9f080d54514413026de.png 2x" data-dominant-color="82B2D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure1</span><span class="informations">742×472 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b301bef183509bf529f020cd476e479665f3ae6f.png" data-download-href="/uploads/short-url/pxzcSuLZuHCLTTbYgELFjnMc25N.png?dl=1" title="figure2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b301bef183509bf529f020cd476e479665f3ae6f_2_690x491.png" alt="figure2" data-base62-sha1="pxzcSuLZuHCLTTbYgELFjnMc25N" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b301bef183509bf529f020cd476e479665f3ae6f_2_690x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b301bef183509bf529f020cd476e479665f3ae6f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b301bef183509bf529f020cd476e479665f3ae6f.png 2x" data-dominant-color="73A2A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure2</span><span class="informations">853×608 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lili-yu22 (2025-01-03 04:43 UTC)

<p>can you help me ?I use the population analysis module in slicersalt5.0.0.I get the PCA mean of the group 1,but the color is always black,no matter I change it to become white .how can I do.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f981260c49a3f5e2853cb74768e6be5e9429d60e.jpeg" data-download-href="/uploads/short-url/zBdAzaBfNNxMkJHv5atKtUGEP2C.jpeg?dl=1" title="IMG_20250102_132404" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f981260c49a3f5e2853cb74768e6be5e9429d60e_2_375x500.jpeg" alt="IMG_20250102_132404" data-base62-sha1="zBdAzaBfNNxMkJHv5atKtUGEP2C" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f981260c49a3f5e2853cb74768e6be5e9429d60e_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f981260c49a3f5e2853cb74768e6be5e9429d60e_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f981260c49a3f5e2853cb74768e6be5e9429d60e_2_750x1000.jpeg 2x" data-dominant-color="575455"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20250102_132404</span><span class="informations">1920×2560 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @bpaniagua (2025-03-17 15:24 UTC)

<p>That is probably due to bad triangulation / bad normals. What happens if you try to process it in the surface toolbox? i.e. clean mesh</p>

---
