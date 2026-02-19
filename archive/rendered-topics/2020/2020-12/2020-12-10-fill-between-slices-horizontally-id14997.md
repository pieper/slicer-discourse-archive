---
topic_id: 14997
title: "Fill Between Slices Horizontally"
date: 2020-12-10
url: https://discourse.slicer.org/t/14997
---

# Fill between slices horizontally

**Topic ID**: 14997
**Date**: 2020-12-10
**URL**: https://discourse.slicer.org/t/fill-between-slices-horizontally/14997

---

## Post #1 by @Chungmh (2020-12-10 21:11 UTC)

<p>Currently I am trying to segment the cartilages and meniscus. I have already created segments horizontally.  however when I tried to fill between slices they are not connecting?</p>
<p>Does anyone knows why?</p>
<p>I really need this to work. I did once before it worked just fine but today i try again its not working</p>

---

## Post #2 by @lassoan (2020-12-10 21:22 UTC)

<p>You can fill slices only along one axis at a time. If you painted slices in different orientations then you need to fill between them in several steps. In each step, you show only those segments that have the same orientation and hide all the others (that are in a different orientation or already filled), and then apply “Fill between slices”. Make sure to enable overlapping segments to preserve the segments that are hidden.</p>
<p>If doing this in several steps is not convenient then you may also try methods that work with arbitrarily placed seed regions, such as “Grow from seeds”.</p>
<p>Let us know how it works for you.</p>

---

## Post #3 by @Chungmh (2020-12-10 22:39 UTC)

<p>Hi I have only sliced in one direction as shown in the picture <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ab002f5f359328ac772bf02c238987a1e696e7d.jpeg" data-download-href="/uploads/short-url/fdNIk6qyBSYLJXuGiOjOYxnqHlX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ab002f5f359328ac772bf02c238987a1e696e7d_2_375x500.jpeg" alt="image" data-base62-sha1="fdNIk6qyBSYLJXuGiOjOYxnqHlX" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ab002f5f359328ac772bf02c238987a1e696e7d_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ab002f5f359328ac772bf02c238987a1e696e7d_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ab002f5f359328ac772bf02c238987a1e696e7d_2_750x1000.jpeg 2x" data-dominant-color="666C99"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1512×2016 1.38 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The fill between option is not connecting the gaps between each slices for some reason and i do not know why</p>
<p>I even tried to start a new segmentation for testing and I just did 2 slices from the sagittal view. And tried the fill between, however it is still not connecting thoes 2 slices</p>

---

## Post #4 by @lassoan (2020-12-11 03:01 UTC)

<p>Filling only happens between standalone slices (that have completely empty neighbors). Nothing is filled in the image above anymore, because none of the slices look like standalone (there are 2 or more neighbor non-empty slices).</p>

---

## Post #5 by @Chungmh (2020-12-11 18:57 UTC)

<p>Ok got it. So to make the filling happens how many empty slices should be between each slice. I will go try it again and update you</p>
<p>Thank you</p>

---

## Post #6 by @lassoan (2020-12-11 19:10 UTC)

<p>Each slice that you need to fill between has to be a single slice with at least one empty slice on each side.</p>
<p>If two or more neighbor slices are segmented then it will be considered as a complete 3D object and will not be connected to other slices on either side.</p>

---

## Post #7 by @Chungmh (2020-12-11 22:24 UTC)

<p>Hi I have re-segmented as shown (1) . However when i try fill in between slices it is not working and I am not sure why, the gaps between each slices are not connecting<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/461524af10317991fbbcd619526cae6aec452bd0.jpeg" data-download-href="/uploads/short-url/9ZYIMgLa55TwdXhSXU4xOGw1G5W.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/461524af10317991fbbcd619526cae6aec452bd0_2_507x500.jpeg" alt="image" data-base62-sha1="9ZYIMgLa55TwdXhSXU4xOGw1G5W" width="507" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/461524af10317991fbbcd619526cae6aec452bd0_2_507x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/461524af10317991fbbcd619526cae6aec452bd0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/461524af10317991fbbcd619526cae6aec452bd0.jpeg 2x" data-dominant-color="767888"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">703×693 91.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> (1)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d5828e9a3694ab31294bfbacc6e4ccaaed7184a.jpeg" data-download-href="/uploads/short-url/kaocHvhI9hPSx9eVm35jD8YQwL8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d5828e9a3694ab31294bfbacc6e4ccaaed7184a_2_690x335.jpeg" alt="image" data-base62-sha1="kaocHvhI9hPSx9eVm35jD8YQwL8" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d5828e9a3694ab31294bfbacc6e4ccaaed7184a_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d5828e9a3694ab31294bfbacc6e4ccaaed7184a_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d5828e9a3694ab31294bfbacc6e4ccaaed7184a_2_1380x670.jpeg 2x" data-dominant-color="636579"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1913×931 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> (2)</p>
<p>Thank you very much for your help</p>

---

## Post #8 by @lassoan (2020-12-11 23:17 UTC)

<p>Sorry for all the troubles. It seems that you segment on oblique slices (you can see that from the warning icon displayed next to the segmentation node selector). This way when you paint on one slice, you actually paint on several slices of the segmentation. Unfortunately, fill between slices algorithm always works on the original slices, cannot work on oblique slices.</p>
<p>You can either try Grow from seeds effect (that does not require this strict slice-by-slice painting), or you can resample the segmentation geometry with rotated axes.</p>
<p>Knee MRI segmentation is hard, but it should be possible to establish a good segmentation workflow.</p>
<p><a class="mention" href="/u/carlp">@carlp</a> I saw some amazingly high quality knee segmentations from you. Could you help with some advice here? Or - it’s soon time for Christmas, so maybe I can ask such things - could you create a screencast video that shows how you segment a knee?</p>

---

## Post #9 by @Chungmh (2020-12-11 23:23 UTC)

<p>Hi Andras,</p>
<p>thank you very much. I will explore the grow from seeds effect options as well as rotated axes. But may I know how does the rotated axes work?</p>
<p>Also the screencast will be insanely helpful as i am trying to obtain a geometry for a FEA analysis, meaning that i would require a a decent quality of the knee segmentation.</p>
<p>Thank you</p>

---

## Post #10 by @lassoan (2020-12-11 23:28 UTC)

<p>See this page for more information on segmentation on oblique slices: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/</a></p>

---

## Post #11 by @Chungmh (2020-12-11 23:30 UTC)

<p>Thank you. I will let you know how I get on. Hope you and your family have a nice Christmas</p>

---

## Post #12 by @Chungmh (2020-12-14 22:15 UTC)

<p>Hi currently I am just segmenting each slice as I only need the overall geometry and i will redraw the structure in solidworks. However I ran into a problem where if i paint something in one slice it affects its direct neighbour slice,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c50063857130f12e6b2aa93527b757a7f11a3a81.jpeg" data-download-href="/uploads/short-url/s6KTsLWDBFCBBVPllFaMoMhjqrn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c50063857130f12e6b2aa93527b757a7f11a3a81_2_488x500.jpeg" alt="image" data-base62-sha1="s6KTsLWDBFCBBVPllFaMoMhjqrn" width="488" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c50063857130f12e6b2aa93527b757a7f11a3a81_2_488x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c50063857130f12e6b2aa93527b757a7f11a3a81.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c50063857130f12e6b2aa93527b757a7f11a3a81.jpeg 2x" data-dominant-color="6E6465"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">546×559 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b992c131ccf1d2f47a83cf081b52e0158a171a17.jpeg" data-download-href="/uploads/short-url/qtEKEr8T0FnZcNjM477UTZmVdll.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b992c131ccf1d2f47a83cf081b52e0158a171a17.jpeg" alt="image" data-base62-sha1="qtEKEr8T0FnZcNjM477UTZmVdll" width="431" height="500" data-dominant-color="706263"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">448×519 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @lassoan (2020-12-15 03:26 UTC)

<p>This is normal when you segment on oblique (non-axis oriented) slices. See this page for more details: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/</a></p>

---

## Post #14 by @Chungmh (2020-12-19 22:54 UTC)

<p>HI,<br>
i have tried the grow from seed it indeed works faster but i want to ask why is my segmentation coarse, as shown below. Thank you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4af42e6860db9f3ef24a721312723cdc2dc06676.jpeg" data-download-href="/uploads/short-url/aH4uiV7t0nCaQPxn68m4O6WBsAm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4af42e6860db9f3ef24a721312723cdc2dc06676_2_676x500.jpeg" alt="image" data-base62-sha1="aH4uiV7t0nCaQPxn68m4O6WBsAm" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4af42e6860db9f3ef24a721312723cdc2dc06676_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4af42e6860db9f3ef24a721312723cdc2dc06676_2_1014x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4af42e6860db9f3ef24a721312723cdc2dc06676.jpeg 2x" data-dominant-color="9D9A93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1213×896 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @manjula (2020-12-20 10:38 UTC)

<p>I think that is because of low resolution.</p>
<p>Few thigns that come to my mind that you can do is,</p>
<ol>
<li>Oversample  (from segment editor, specify geometry option)</li>
<li>reslice it useing Crop volume  (Setting spacing scale to &lt;1.0x )</li>
<li>Apply smoothing</li>
</ol>
<p>I prefer reslicing because oversample for me takes too much power.</p>

---

## Post #16 by @Chungmh (2020-12-20 14:37 UTC)

<p>ok got it thank you. i will try another CT scan see if it has a better resolution.</p>

---

## Post #17 by @Chungmh (2020-12-27 13:59 UTC)

<p>Hi I am currently trying to use the oversampling option, I want to ask what does it actually achieve?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74efed07ff5ffac9e81f96e816188d1b7692b9c6.png" alt="image" data-base62-sha1="gGtqnqrCGZajhkgGXOS1pUlUfOu" width="429" height="361"><br>
my model turned like this after</p>
<p>Thank you.</p>
<p>Hope you had a lovely holiday</p>

---

## Post #18 by @manjula (2020-12-27 15:14 UTC)

<p>You can see in this post.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14549">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/oversampling-and-spacing-in-crop/14549/2">Oversampling and Spacing in crop</a></div>
<blockquote>
<p>Exactly. We can call oversampling “digital zoom”.</p>
<p>It does not add new information (the oversampled image should look exactly the same as the original), it just allows representing finer details in the image or segmentation. For example, if you apply a sharpening filter then you can enhance finer details, or if you segment structures, you can represent thinner walls or smaller vessels.</p>
</blockquote>
</aside>

---

## Post #19 by @Carlp (2021-03-02 12:05 UTC)

<p>Greetings and thanks for the kind words =]</p>
<p>You can find several video demonstrations of our knee segmentation software using AI on <a href="https://nordiccad.com" rel="noopener nofollow ugc">nordiccad.com</a></p>

---

## Post #20 by @radiodid (2022-08-30 15:04 UTC)

<p>Hi<br>
Maybe someone knows how to solve the same problem for CT only? Fill between slices does not work. Instead, the slices just get thicker but don’t merge. It’s definitely not a problem with a CT scan, because I tried to do it on another PC and everything was fine. It is also not possible to label other CTs, even in different projections.<br>
I tried to reinstall the application, and reboot the PC - same problem.</p>

---

## Post #21 by @lassoan (2022-08-30 18:41 UTC)

<p>Fill between slices work well on many computers on all kinds of data sets, so there should be something unusual about your data or how you use the tool.</p>
<p>The best would be if you could share an example data set that you have trouble segmenting using this effect. If you cannot reproduce the issue on any public data set then you can post a screen capture video or a few screenshots and then we may see what’s wrong.</p>

---

## Post #22 by @radiodid (2022-08-30 18:51 UTC)

<p>I agree with you about functionality, because I have worked with Slicer many times.  The most interesting thing is that I worked with the same files literally yesterday and performed the same actions and everything worked perfectly, but today it doesn’t.  Although all the “ingredients” are the same.</p>

---

## Post #23 by @radiodid (2022-09-03 16:21 UTC)

<p>As a result, after a few days, the problem somehow solved itself.</p>

---
