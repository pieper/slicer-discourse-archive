---
topic_id: 46084
title: "Issues With Scaling Information Added To Tiff Volume Tried I"
date: 2026-02-08
url: https://discourse.slicer.org/t/46084
---

# Issues with scaling information added to .tiff volume- tried ImageStacks and saving as .nrrd?

**Topic ID**: 46084
**Date**: 2026-02-08
**URL**: https://discourse.slicer.org/t/issues-with-scaling-information-added-to-tiff-volume-tried-imagestacks-and-saving-as-nrrd/46084

---

## Post #1 by @alsig (2026-02-08 00:27 UTC)

<p>Hi everyone,</p>
<p>I am having a issue when trying to import/save TIFF data in a way that lets me add the scaling information. I have a single file ImageJ hyperstack .tiff that has my entire volume, with  X-Y scale of 0.001282 microns/pixel and a Z-step size of 0.000641 microns. When I initially loaded it using add data, it opens without any issues, and I can easily scroll through all the slices as expected.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d52bc708296e4dc77812589584d4f34b73caeff.jpeg" data-download-href="/uploads/short-url/hSEWAPviFoY2D4n3VyOCsZ5UtaL.jpeg?dl=1" title="normal volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d52bc708296e4dc77812589584d4f34b73caeff_2_690x388.jpeg" alt="normal volume" data-base62-sha1="hSEWAPviFoY2D4n3VyOCsZ5UtaL" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d52bc708296e4dc77812589584d4f34b73caeff_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d52bc708296e4dc77812589584d4f34b73caeff_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d52bc708296e4dc77812589584d4f34b73caeff_2_1380x776.jpeg 2x" data-dominant-color="393937"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">normal volume</span><span class="informations">1920×1080 293 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to edit the volume to include the correct spacing/unit conversions, which in my case is (XYZ) like this in the volumes module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0aca1c812b3e435813fd848f6a492f05407f7e7.jpeg" data-download-href="/uploads/short-url/pcVTCjRHXSJ5Krxr7ebIheEzoUf.jpeg?dl=1" title="scaled volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0aca1c812b3e435813fd848f6a492f05407f7e7_2_690x388.jpeg" alt="scaled volume" data-base62-sha1="pcVTCjRHXSJ5Krxr7ebIheEzoUf" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0aca1c812b3e435813fd848f6a492f05407f7e7_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0aca1c812b3e435813fd848f6a492f05407f7e7_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0aca1c812b3e435813fd848f6a492f05407f7e7_2_1380x776.jpeg 2x" data-dominant-color="31302F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">scaled volume</span><span class="informations">1920×1080 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Although that looked fine initially, when I saved the volume from there as a .nrrd, as I saw recommended here to preserve the 3D volume information, and opened the new .nrrd file, I completely lost the ability to see or scroll through the slices, and only had a single slice view. B I tried to import the data using the SlicerMorph ImageStacks extension like this instead, but ended up with a very strange looking volume that did not show up in the viewing planes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2ba3363a9ecca0cbcbe11eb94985774b9898d5e8.png" data-download-href="/uploads/short-url/6e2d4XfvPnrhZ9c8kslAC6ESUXK.png?dl=1" title="ImageStacks import" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2ba3363a9ecca0cbcbe11eb94985774b9898d5e8_2_690x388.png" alt="ImageStacks import" data-base62-sha1="6e2d4XfvPnrhZ9c8kslAC6ESUXK" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2ba3363a9ecca0cbcbe11eb94985774b9898d5e8_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2ba3363a9ecca0cbcbe11eb94985774b9898d5e8_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2ba3363a9ecca0cbcbe11eb94985774b9898d5e8_2_1380x776.png 2x" data-dominant-color="373635"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ImageStacks import</span><span class="informations">1920×1080 316 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone have any ideas on how to fix this, or what I am doing wrong? Any advice is greatly appreciated!</p>

---

## Post #2 by @pieper (2026-02-08 15:37 UTC)

<p>The units feature in Slicer may not be working well in all cases, and since Slicer is natively in mm, such small numbers may not be well preserved.  You might be better off just keeping track of the scale yourself so that the numbers for spacing are around 1, especially if you are going to do calculations or measurements of the data.</p>
<p>Looks like cool data - is it some kind of cell or egg?  Share some 3D renderings if you get a chance.</p>

---

## Post #3 by @muratmaga (2026-02-08 15:40 UTC)

<p>Your imported volume has only one slice for some reason. That is being displayed, there is nothing else to display hence the other two views are just a single line.</p>
<p>Review your import procedure to make sure all frames from your multiframe tiff is imported.</p>

---

## Post #4 by @muratmaga (2026-02-08 15:42 UTC)

<p>More accurately the z dimension has one. The fourth dimension seems to contain some information.</p>

---

## Post #5 by @alsig (2026-02-08 19:54 UTC)

<p>Thanks for your reply! Once I can figure out how to get it imported correctly, I’ll try keeping the scaling ratio but just using larger units (maybe like 1.282 x 1.282 x 0.641 mm) and convert myself afterwards to see if that help!</p>
<p>Thanks, they are micro-CT scans of a small crustacean called an ostracod! I’m segmenting out and modeling their brain anatomy! They look like eggs because their bodies have an outer carapace around it, kinda like a clamshell.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bd05019d81215170112809277fdf56c8c98e234.jpeg" data-download-href="/uploads/short-url/jWQFXgZpv8ABfxjefPt81HSAony.jpeg?dl=1" title="ostracod_vol_proj_body-side" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bd05019d81215170112809277fdf56c8c98e234_2_689x470.jpeg" alt="ostracod_vol_proj_body-side" data-base62-sha1="jWQFXgZpv8ABfxjefPt81HSAony" width="689" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bd05019d81215170112809277fdf56c8c98e234_2_689x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bd05019d81215170112809277fdf56c8c98e234_2_1033x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bd05019d81215170112809277fdf56c8c98e234.jpeg 2x" data-dominant-color="302111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ostracod_vol_proj_body-side</span><span class="informations">1308×892 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @alsig (2026-02-08 20:36 UTC)

<p>Thank you so much for your reply! Yes, I see that, but I don’t understand why that is happening. When I add the file with “Add Data” normally, it seems to keep all the frames of the tiff. It is only after I add in the volume –&gt; imaging space information and save it as a .nrrd, or try to use the ImageStacks import that this happens. Am I entering the spacing information wrong? I also don’t know what the 4th dimension would be doing here, as the file is just a Z-stack of X-Y images.</p>

---

## Post #7 by @pieper (2026-02-08 21:22 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0bf044fd512177f87242edc4c452872efdb516f.png" alt="image" data-base62-sha1="w4ccIkcIKugWpuTeLGkNdjuRrPh" width="421" height="33"></p>
<p>This input size is weird, since normally it would be something like <code>883x1425x839</code>, you have an extra <code>1</code> in the middle.  Maybe you can tweak this some way in imagej to flatten it back to 3D.  You say it’s a ‘hyperstack’ and I’m not sure what that is but maybe you can make it a regular ‘stack’ instead.  If this is a common kind of tiff file then if you can share an example maybe we can detect and fix it in ImageStacks.</p>
<p>Or, if you are handy in python I’m sure you can read the tiff into a numpy array and then make it a regular volume.</p>

---

## Post #8 by @muratmaga (2026-02-08 21:51 UTC)

<p>Hyperstack in fiji is for multichannel data as far as i know.</p>
<p>I suggest not skipping fiji and directly import thr multi frame tiff into Slicer.</p>

---

## Post #9 by @muratmaga (2026-02-08 23:27 UTC)

<aside class="quote no-group" data-username="alsig" data-post="1" data-topic="46084">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee59a6/48.png" class="avatar"> alsig:</div>
<blockquote>
<p>0.000641 microns.</p>
</blockquote>
</aside>
<p>Also are you sure this is in micrometers (microns) as opposed to millimeter. 0.000641 would be like 0.641 nanometer. At that scale the length of your ostracod would be 0.5 microns, which doesn’t look right to me.</p>

---

## Post #10 by @alsig (2026-02-09 00:08 UTC)

<p>You are absolutely right <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=15" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"> I definitely meant to say 0.000641 mm or 0.641 microns! That’s what I get for trying to operate on no sleep. Thanks for catching my dumb mistake here!</p>

---

## Post #11 by @alsig (2026-02-09 00:10 UTC)

<p>I’ll give that a try now! Thanks again for all the help!</p>

---
