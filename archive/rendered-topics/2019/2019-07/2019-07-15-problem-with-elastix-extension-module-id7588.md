# Problem with Elastix extension module

**Topic ID**: 7588
**Date**: 2019-07-15
**URL**: https://discourse.slicer.org/t/problem-with-elastix-extension-module/7588

---

## Post #1 by @kuba_grepl (2019-07-15 13:27 UTC)

<p>Hello, I have a problem with Elastix extension. I tried repeat simple registration case of Free Sample Data according to the instructions in You Tube video:<a href="https://www.youtube.com/watch?v=cU0pWhn0-3o" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=cU0pWhn0-3o</a><br>
But something is wrong (see PrtScrn). Can anybody help me?<br>
Thank you, Kuba.<br>
University Hospital Hradec Kralove, Czech Republic.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3671b556effff1483bae602fc85f9b11ac96348d.png" data-download-href="/uploads/short-url/7LDoWY4LgYat3ULHPnC34D6o2OF.png?dl=1" title="ELASTIX" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/3671b556effff1483bae602fc85f9b11ac96348d_2_690x370.png" alt="ELASTIX" data-base62-sha1="7LDoWY4LgYat3ULHPnC34D6o2OF" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/3671b556effff1483bae602fc85f9b11ac96348d_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/3671b556effff1483bae602fc85f9b11ac96348d_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/3671b556effff1483bae602fc85f9b11ac96348d_2_1380x740.png 2x" data-dominant-color="EAEBED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ELASTIX</span><span class="informations">1915×1028 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-07-15 14:06 UTC)

<p>Probably you need to have your data in directories with only ascii characters in the paths - sorry, the program is limited in this regard.  Some internationalization is a <a href="https://discourse.slicer.org/t/slicer-internationalization/579">work in progress</a>, but we use a lot of libraries and not all the code handles non-ascii characters.</p>

---

## Post #3 by @kuba_grepl (2019-07-16 05:56 UTC)

<p>Hello Steve. I renamed the user´s account (<a href="https://www.top-password.com/blog/rename-user-profile-directory-in-windows/" rel="nofollow noopener">https://www.top-password.com/blog/rename-user-profile-directory-in-windows/</a>) and everything work now.<br>
Thank you, Kuba.<br>
University Hospital Hradec Kralove, Czech Republic.</p>

---

## Post #4 by @lassoan (2019-07-16 12:16 UTC)

<p>You can also try a recent Preview Release , as it uses Python3, which handles unicode strings somewhat differently (but at least upgrade to the latest Stable Release so that you can benefit from all the developments and fixes we implemented in the last 2 years).</p>

---

## Post #5 by @kuba_grepl (2019-07-17 12:41 UTC)

<p>Thank you Andras!<br>
I use version 4.8.1, because extension manager (install extension) does not work in recent Stable Release 4.10.2 . I had also a problem with viewing DICOM files in version 4.10.2. In older version 4.8.1 everything is working.<br>
I successfully repeated simple example in youtube video mentioned above. In the next step, I tried to use Elastix with my own data sets. I have MR T2W and CT (with radiotherapy structure set) of the head and neck of one patient. MR is my fixed volume and I need to deform and match my CT data. Both scans are shifted more than 20cm. So I decided to use Transform Module to pre-align and then I used Elastix. But I received a very bad result.<br>
Where I made a mistake? (<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5aeb0fb9510865958a567b40a45ea2f4b99a9b3.png" data-download-href="/uploads/short-url/nDH3xsu554zXaft6zYRtrMI5XsD.png?dl=1" title="Before" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5aeb0fb9510865958a567b40a45ea2f4b99a9b3_2_690x370.png" alt="Before" data-base62-sha1="nDH3xsu554zXaft6zYRtrMI5XsD" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5aeb0fb9510865958a567b40a45ea2f4b99a9b3_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5aeb0fb9510865958a567b40a45ea2f4b99a9b3_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5aeb0fb9510865958a567b40a45ea2f4b99a9b3_2_1380x740.png 2x" data-dominant-color="7C7C85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Before</span><span class="informations">1915×1029 295 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>  I am a novice with 3D slicer.  Sorry for maybe stupid question…</p>

---

## Post #6 by @cpinter (2019-07-17 13:22 UTC)

<p>Thanks for the feedback about 4.10, very useful! The new extension manager is under construction, so that issue will be solved soon, but can you please tell us what kind of problems you had with DICOMs in 4.10?</p>
<p>About the registration, I don’t think you need pre-alignment. Also not sure that Elastix considers transforms that are not hardened, but hardening comes with some data loss.</p>

---

## Post #7 by @lassoan (2019-07-17 13:28 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="7588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>not sure that Elastix considers transforms that are not hardened</p>
</blockquote>
</aside>
<p>I can confirm that Elastix module only considers hardened transforms. There may be a slight image quality degradation due to resampling <em>only in the case when warping transform was applied</em> on the volume (no resampling is performed when linear transform is applied, so image quality is not impacted then).</p>

---

## Post #8 by @lassoan (2019-07-17 13:32 UTC)

<aside class="quote no-group" data-username="kuba_grepl" data-post="5" data-topic="7588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kuba_grepl/48/4161_2.png" class="avatar"> kuba_grepl:</div>
<blockquote>
<p>I use version 4.8.1, because extension manager (install extension) does not work in recent Stable</p>
</blockquote>
</aside>
<p>What operating system do you use? What do you mean by “does not work”? The extension manager does not appear? Does the application hang or crash? You can install extensions but they do not appear in the module list?</p>

---

## Post #9 by @kuba_grepl (2019-07-17 14:33 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="7588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>can you please tell us what kind of problems you had with DICOMs in 4.10?</p>
</blockquote>
</aside>
<p>When I try load Dicom data I obtain Error message (see PrtScrn) and after that, I can see image only in small zoom area but not in red, yellow and green windows (also PrtScrn).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ae6cd6deb8ba6228c72a19c236a53629eb1c4f8.png" data-download-href="/uploads/short-url/m6k1of6AfsIa4xhM99VO9Czm5ss.png?dl=1" title="Dicom%20load" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ae6cd6deb8ba6228c72a19c236a53629eb1c4f8_2_690x309.png" alt="Dicom%20load" data-base62-sha1="m6k1of6AfsIa4xhM99VO9Czm5ss" width="690" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ae6cd6deb8ba6228c72a19c236a53629eb1c4f8_2_690x309.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ae6cd6deb8ba6228c72a19c236a53629eb1c4f8_2_1035x463.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ae6cd6deb8ba6228c72a19c236a53629eb1c4f8_2_1380x618.png 2x" data-dominant-color="EFF1F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Dicom%20load</span><span class="informations">1905×855 72.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @kuba_grepl (2019-07-17 14:40 UTC)

<p>I use Win7 Professional. I mean that when I click on Install extension I can see only the empty black window.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d2fae0fb0e81fa28878fccc1b6109b965e3707e.png" data-download-href="/uploads/short-url/1SEmnfKy6FiWqlQOoBRNZmt0i5M.png?dl=1" title="Extension%20manager" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d2fae0fb0e81fa28878fccc1b6109b965e3707e_2_690x368.png" alt="Extension%20manager" data-base62-sha1="1SEmnfKy6FiWqlQOoBRNZmt0i5M" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d2fae0fb0e81fa28878fccc1b6109b965e3707e_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d2fae0fb0e81fa28878fccc1b6109b965e3707e_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d2fae0fb0e81fa28878fccc1b6109b965e3707e_2_1380x736.png 2x" data-dominant-color="0E0F10"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Extension%20manager</span><span class="informations">1909×1020 49.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @kuba_grepl (2019-07-17 14:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="7588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I can confirm that Elastix module only considers hardened transforms.</p>
</blockquote>
</aside>
<p>What exactly hardened transform means? Why my deformable registration mentioned above gives me bat results?</p>

---

## Post #12 by @cpinter (2019-07-17 14:52 UTC)

<p>The error message about DICOM SRO should not prevent loading anything. Are your data loaded fine after this?</p>
<p>I developed the SRO import/export plugin, so I’d appreciate if you send me your data (anonymized if possible) that brings out this error. Thank you!</p>

---

## Post #13 by @kuba_grepl (2019-07-17 18:13 UTC)

<p>As I wrote above, after this error message data are probably loaded, but I can not see images in red, yellow and green window. I can see image only in small square (zoom) in the left bottom corner of the screen. (see in PrtScrn). It is not problem of my data I tried it with free sample included in slicer with the same result.</p>

---

## Post #14 by @cpinter (2019-07-17 18:16 UTC)

<p>If the data is loaded, then there should be no problem with displaying it. Check it out in the Volumes module. See the dimensions and scalar range of the volume and see if it’s reasonable.</p>
<aside class="quote no-group" data-username="kuba_grepl" data-post="13" data-topic="7588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kuba_grepl/48/4161_2.png" class="avatar"> kuba_grepl:</div>
<blockquote>
<p>As I wrote above</p>
</blockquote>
</aside>
<p>Thank you, but I’d like to fix this issue if you’re willing to help me reproduce it.</p>

---

## Post #15 by @kuba_grepl (2019-07-17 18:49 UTC)

<p>I will check it again in my office tomorow and I will let you know.</p>

---

## Post #16 by @kuba_grepl (2019-07-18 10:26 UTC)

<p>I checked it again. I downloaded Sample Data (MRHead), opened Volume module and I can say that Dimensions are 256, 256, 112. The scalar range is 0 - 695. And again I can see image only in Data Probe (Show Zoomed Slice). How can I help you to identify where the problem is?</p>
<p>Thank you, Kuba.</p>

---

## Post #17 by @jamesobutler (2019-07-18 12:15 UTC)

<p>Based on your latest screenshot it shows that you are using Slicer 4.10.2 stable but it shows that you installed the SlicerRT extension that was built with Slicer 4.11 nightly revision 28371. This is a problem. Did you manually install a nightly extension for Slicer 4.10.2?</p>
<p>Uninstall this extension and reinstall using the extension manager within Slicer 4.10.2 stable. Or download the extension zip that is built specifically for Slicer 4.10.2 and install manually.</p>

---

## Post #18 by @lassoan (2019-07-18 12:32 UTC)

<aside class="quote no-group" data-username="kuba_grepl" data-post="16" data-topic="7588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kuba_grepl/48/4161_2.png" class="avatar"> kuba_grepl:</div>
<blockquote>
<p>And again I can see image only in Data Probe (Show Zoomed Slice). How can I help you to identify where the problem is?</p>
</blockquote>
</aside>
<p>I see what’s the problem now. Slicer-4.10 requires OpenGL version 3.2 to take advantage of new features in graphics cards. OpenGL 3.2 is supported on all computers that are manufactured in the last 5 years or so, but not on computers that are much older than that. I would recommend to upgrade your computer, not just because of Slicer but also because Windows 7 and 8 are very insecure to use.</p>

---

## Post #19 by @kuba_grepl (2019-07-18 13:52 UTC)

<p>Thank you Andras,<br>
you are right. I installed Slicer 4.10.2 on the newest computer in our department (Win 10, 8GB RAM, 2,8GHz) and the problem is solved.</p>

---
