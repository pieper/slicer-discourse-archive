# Volume compressed into ROI

**Topic ID**: 40085
**Date**: 2024-11-09
**URL**: https://discourse.slicer.org/t/volume-compressed-into-roi/40085

---

## Post #1 by @OwenProulx (2024-11-09 04:23 UTC)

<p>Hi, I’ve been having this issue for a while. I’ve been trying to create an ROI for one of my specimens, and when I load the ROI at full resolution, it instead compresses the whole volume into it, instead of cropping the unselected things out.</p>
<p>It doesn’t happen with smaller ROIs (like vertebrae for example), but when I create and ROI of a whole fish this happens<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af816310dc1d1868f6fbf9f3041bd12769caa5fb.png" data-download-href="/uploads/short-url/p2ALAPAgXL3xcEmimvrKTaVq9eP.png?dl=1" title="Screenshot 2024-11-08 125750" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af816310dc1d1868f6fbf9f3041bd12769caa5fb_2_690x199.png" alt="Screenshot 2024-11-08 125750" data-base62-sha1="p2ALAPAgXL3xcEmimvrKTaVq9eP" width="690" height="199" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af816310dc1d1868f6fbf9f3041bd12769caa5fb_2_690x199.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af816310dc1d1868f6fbf9f3041bd12769caa5fb_2_1035x298.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af816310dc1d1868f6fbf9f3041bd12769caa5fb_2_1380x398.png 2x" data-dominant-color="856F87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-11-08 125750</span><span class="informations">1905×551 83.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-11-09 14:44 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> or others might know off the top of their heads.</p>
<p>If not, <a class="mention" href="/u/owenproulx">@OwenProulx</a> please share the data and exact steps or else reproduce the issue on public data if you want others to help you replicate and fix the issue.</p>

---

## Post #3 by @muratmaga (2024-11-09 19:12 UTC)

<p>I never had this issue before. Can you try creating a new volume (instead of overwriting the existing volume), when you are importing the ROI at full res?</p>
<p>Also it will be helpful to tell us the exact steps you are following (along with any message that might be in the log file).</p>

---

## Post #4 by @OwenProulx (2024-11-13 01:42 UTC)

<p>I’ve tried creating a new volume and got the same result. Ive also submitted an instance on MorphoCloud. Here’s the error log:</p>
<p>Python 3.9.10 (main, Apr 5 2024, 01:02:26) [MSC v.1938 64 bit (AMD64)] on win32</p>
<p>[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>[Qt] libpng warning: iCCP: known incorrect sRGB profile</p>
<p>[FD] TIFFReadDirectory: Warning, Unknown field with tag 65280 (0xff00) encountered.</p>
<p>[FD] TIFFReadDirectory: Warning, Unknown field with tag 65281 (0xff01) encountered.</p>
<p>[FD] TIFFReadDirectory: Warning, Unknown field with tag 65280 (0xff00) encountered.</p>
<p>[FD] TIFFReadDirectory: Warning, Unknown field with tag 65281 (0xff01) encountered.</p>

---

## Post #5 by @muratmaga (2024-11-13 03:03 UTC)

<aside class="quote no-group" data-username="OwenProulx" data-post="4" data-topic="40085">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/6de8d8/48.png" class="avatar"> OwenProulx:</div>
<blockquote>
<p>FD] TIFFReadDirectory: Warning, Unknown field with tag 65280 (0xff00) encountered.</p>
<p>[FD] TIFFReadDirectory: Warning, Unknown field with tag 65281 (0xff01) encountered.</p>
<p>[FD] TIFFReadDirectory: Warning, Unknown field with tag 65280 (0xff00) encountered.</p>
<p>[FD] TIFFReadDirectory: Warning, Unknown field with tag 65281 (0xff01) encountered.</p>
</blockquote>
</aside>
<p>This is not an error, but warning. And it has nothing to do with your issue (it is simply complaning about some custom TIFF tags). Without your data and exact steps you are doing, we cannot replicate the issue.</p>
<p>This to me seems more of a rendering problem. What kind of a GPU do you have? Do you still get the same stretching if you use CPU raycasting.</p>
<p>You can also try skipping a slice, which will reduce the Z dimension and see if the problem persists (if it shouldn’t, if it is rendering related like I suggested).</p>

---

## Post #6 by @OwenProulx (2024-11-13 03:50 UTC)

<p>I have a AMD Ryzen 7 5800H and 32gb of RAM. I’m not sure what CPU raycasting is, is there a place I can upload my rec files and a description of my steps?</p>

---

## Post #7 by @muratmaga (2024-11-13 04:32 UTC)

<p>I already approved your morphocloud request and it is up and running. Please upload your data there, and describe your steps here.</p>

---

## Post #8 by @OwenProulx (2024-11-13 04:48 UTC)

<p>Sorry, very new to morphocloud, where should I upload my data? I tried adding a comment but it didn’t accept the reconstruction folder from my files. I’m currently uploading it to a google drive folder so it’s less intensive. It’s going to take quite a while however, is there an easier way?</p>

---

## Post #9 by @muratmaga (2024-11-13 04:53 UTC)

<p>Please read this document first: <a href="https://docs.google.com/document/d/1WRds-QWnDK1MnmEhGUPyBgjE9hitiddcElAPWiAYRg4/edit#heading=h.b0yi3m7wlfk8" class="inline-onebox" rel="noopener nofollow ugc">MorphoCloud OnDemand Instances - Google Docs</a></p>
<p>and then follow the instructions in the email sent to you by the MorphoCloud</p>

---

## Post #10 by @OwenProulx (2024-11-13 17:19 UTC)

<p>In the process of downloading my files to “My Data”, sorry for the wait, it took a long while to upload to google drive.</p>

---

## Post #11 by @muratmaga (2024-11-14 04:17 UTC)

<p>I don’t think one of your zip files uploaded fully, because when I decompressed it, it resultant stack was only 55GB in size (as opposed to 68GB your screenshot showed). However, I am not sure what is missing, since that seems complete.</p>
<p>Beyond that everything worked as expected.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ad7c441aa235333e3b00692705ad06214771f39.jpeg" data-download-href="/uploads/short-url/jOgasOXEgoPyXxxxuokuIFXLp7b.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ad7c441aa235333e3b00692705ad06214771f39_2_690x363.jpeg" alt="image" data-base62-sha1="jOgasOXEgoPyXxxxuokuIFXLp7b" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ad7c441aa235333e3b00692705ad06214771f39_2_690x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ad7c441aa235333e3b00692705ad06214771f39_2_1035x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ad7c441aa235333e3b00692705ad06214771f39_2_1380x726.jpeg 2x" data-dominant-color="7C7A7E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1012 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If this is not what you are getting, you are probably encountering a strange GPU driver issue, as the full resolution subvolume is not that big, it is only about a 1GB. You will probably benefit from running these on the MorphoCloud.</p>

---

## Post #12 by @muratmaga (2024-11-14 04:24 UTC)

<p>One more suggestion: While you have a massive dataset, the data portion of it is tiny (probably about 5%). If you have scanned and reconstructed this data yourself, you would immensely benefit from setting a ROI during the reconstruction process (using the Bruker’s Nrecon software), and reconstruct each fish as a separate dataset (you can create different subfolders). If you do that, what you will end up with will be about three 1-1.5GB datasets, as opposed to one massive 68GB dataset.</p>
<p>Your data transfers will be simpler, your data management will be simpler. Pretty much everything you want to do with this data will be easier.</p>

---

## Post #13 by @OwenProulx (2024-11-14 21:48 UTC)

<p>That’s a great tip, I’ll make sure to do that. Thanks for all your help!</p>

---
