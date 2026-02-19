---
topic_id: 16983
title: "Vmtk Centerline Extraction Trouble"
date: 2021-04-07
url: https://discourse.slicer.org/t/16983
---

# VMTK centerline extraction trouble?

**Topic ID**: 16983
**Date**: 2021-04-07
**URL**: https://discourse.slicer.org/t/vmtk-centerline-extraction-trouble/16983

---

## Post #1 by @rsulser (2021-04-07 14:21 UTC)

<p>Operating system: Windows 10 (20H2)<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Extraction of centerline within a model<br>
Actual behavior: Centerline curve is not constrained to the model space</p>
<p>Hello all -</p>
<p>Wondering if anyone can help me troubleshoot extracting a centerline from a structure (in this case, a segmented spiral ganglion). I’m doing my best to follow along with some of the tutorial videos posted by PerkLab, but I am having some difficulties in extracting a centerline curve (see images hopefully attached). The centerline model seems to have been created successfully, but the curve itself only contains three control points and exceeds the bounds of the model - what steps can I take to constrain the curve inside my target model?</p>
<p>Any help in troubleshooting would be greatly appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/986a60f963abb7be99158231e34b7304472a3eeb.jpeg" data-download-href="/uploads/short-url/lKkurAp0BMxdpZdzd9VERZE1jez.jpeg?dl=1" title="Screenshot 2021-04-06 160151" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/986a60f963abb7be99158231e34b7304472a3eeb_2_690x370.jpeg" alt="Screenshot 2021-04-06 160151" data-base62-sha1="lKkurAp0BMxdpZdzd9VERZE1jez" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/986a60f963abb7be99158231e34b7304472a3eeb_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/986a60f963abb7be99158231e34b7304472a3eeb_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/986a60f963abb7be99158231e34b7304472a3eeb_2_1380x740.jpeg 2x" data-dominant-color="8A8B90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-04-06 160151</span><span class="informations">1920×1030 352 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4349ea744d69356a974da8a3575b0b486f5aebda.jpeg" data-download-href="/uploads/short-url/9BglYAjkcXNLPfmZ5XGSoFgWfeG.jpeg?dl=1" title="Screenshot 2021-04-06 160242" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4349ea744d69356a974da8a3575b0b486f5aebda_2_690x370.jpeg" alt="Screenshot 2021-04-06 160242" data-base62-sha1="9BglYAjkcXNLPfmZ5XGSoFgWfeG" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4349ea744d69356a974da8a3575b0b486f5aebda_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4349ea744d69356a974da8a3575b0b486f5aebda_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4349ea744d69356a974da8a3575b0b486f5aebda_2_1380x740.jpeg 2x" data-dominant-color="8A8A8F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-04-06 160242</span><span class="informations">1920×1030 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-04-14 05:32 UTC)

<p>The centerline curve looks nice. Maybe the two endpoints are connected because you created a closed curve? Or maybe the smooth curve that connects the two endpoints are the centerline curve and it cannot follow the actual curve because you have chosen polynomial interpolation interpolation instead of spline? It is hard to guess. It would help if you could share your scene file (saved as .mrb).</p>

---

## Post #3 by @rsulser (2021-04-14 15:19 UTC)

<p>Hi Andras-</p>
<p>Unfortunately, it looks like I’m actually not authorized to share my .mrb scene here (looks like I’m limited to jpg, jpeg, png, gif, mp4 on this forum, but am happy to image/send anything that might be useful!) ***EDIT: <a href="https://www.dropbox.com/s/awbv7o85jmycrgi/2021-04-04-Scene.mrb?dl=0" rel="noopener nofollow ugc">here</a> is a dropbox link</p>
<p>Apologies for any confusion, the spiral within the model is the centerline model, and the arc connecting the endpoints is the centerline curve (see attached images).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c08bc52e361a641be665bbbc28dbcc20c998b2e.jpeg" data-download-href="/uploads/short-url/aQD0evVPcmmawzLIhZx5npNKQLY.jpeg?dl=1" title="Screenshot 2021-04-14 105656" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c08bc52e361a641be665bbbc28dbcc20c998b2e_2_690x370.jpeg" alt="Screenshot 2021-04-14 105656" data-base62-sha1="aQD0evVPcmmawzLIhZx5npNKQLY" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c08bc52e361a641be665bbbc28dbcc20c998b2e_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c08bc52e361a641be665bbbc28dbcc20c998b2e_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c08bc52e361a641be665bbbc28dbcc20c998b2e_2_1380x740.jpeg 2x" data-dominant-color="87888D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-04-14 105656</span><span class="informations">1920×1030 344 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will certainly look into polynomial vs spline interpolation. Looking at the centerline curve, it appears the curve is a spline with three control points (the two endpoints and one in the center of the model). Based on the video tutorials I’ve found, this looks to be a small amount of control points - perhaps this has something to do with the issue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b0cda5451da3aa12a24ad179b6e60f8f06dd72f.png" data-download-href="/uploads/short-url/m7DxN3XMOjFkIyFF4Gq5XV9zVvN.png?dl=1" title="Screenshot 2021-04-14 112200" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b0cda5451da3aa12a24ad179b6e60f8f06dd72f_2_690x370.png" alt="Screenshot 2021-04-14 112200" data-base62-sha1="m7DxN3XMOjFkIyFF4Gq5XV9zVvN" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b0cda5451da3aa12a24ad179b6e60f8f06dd72f_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b0cda5451da3aa12a24ad179b6e60f8f06dd72f_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b0cda5451da3aa12a24ad179b6e60f8f06dd72f_2_1380x740.png 2x" data-dominant-color="808287"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-04-14 112200</span><span class="informations">1920×1030 356 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In any case, thank you for your time and help!</p>
<p>EDIT: fixed the uploaded files, hopefully this makes things a little more clear</p>

---

## Post #4 by @lassoan (2021-04-15 02:02 UTC)

<p>Thank you, the scene file was very useful. The problem was that the curve’s sampling distance was hardcoded to 1mm, which worked well in general, but for your tiny structure of about 1mm in size it meant that only a few control points were used to define the curve.</p>
<p>I’ve added an option to set curve sampling distance in Advanced section (the change will be available in the extensions manager tomorrow). If you set curve sampling distance it to 0.01 then the curve will be extracted accurately.</p>

---

## Post #5 by @hherhold (2021-04-15 10:24 UTC)

<p>Oh wow, this is probably why I was having trouble with this as well - the features I look at are often 10 microns in diameter. I will have to try this again.</p>

---

## Post #6 by @rsulser (2021-04-15 19:28 UTC)

<p>Update: This fix worked perfectly, I’m able to set the sampling distance and extract the curve successfully. Thanks all!</p>

---

## Post #7 by @hherhold (2021-04-17 17:02 UTC)

<p>I don’t see SlicerVMTK in the Extensions Manager for the last few nightly builds. Did it build ok?</p>
<p>Thanks!</p>

---

## Post #8 by @chir.set (2021-04-17 17:20 UTC)

<p>It will probably be missing for nightlies until it gets ported for VTK9. It will surely come, as time permits, the devs are certainly very busy.<br>
If you need recent Slicer functionalities and SlicerVMTK, both must be built with VTK8.</p>

---

## Post #9 by @pieper (2021-04-17 18:41 UTC)

<p>Yes, there’s a quirky build error that needs to get tracked down.  VMTK happens to be one of the more complex extensions since it provides it’s own vtk and itk subclasses and there’s something going wrong with the python build configuration variables.</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=2216202" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/viewBuildError.php?buildid=2216202</a></p>

---

## Post #10 by @Pavel_Zhabyeyev (2022-01-21 20:32 UTC)

<p>I cannot make VMTK centerline extraction work for multiple point (&gt;2) on aorta example from the library. I have seeded on point, used auto detect to find more, deleted some non relevant. Once I try to run the module. It gets stuck in “Generate curves and quantification tables” for tens of minutes. Allocated memory grows and grows: currently like 45 Gb out of 128 Gb.</p>
<p>I am using recently downloaded version for windows from <a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3974eca60a9475ab4ceab4bc463439012f0bab91.png" data-download-href="/uploads/short-url/8chIXGOxcoAQRRHtfUcfsmPvcL7.png?dl=1" title="HungUp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3974eca60a9475ab4ceab4bc463439012f0bab91_2_690x388.png" alt="HungUp" data-base62-sha1="8chIXGOxcoAQRRHtfUcfsmPvcL7" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3974eca60a9475ab4ceab4bc463439012f0bab91_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3974eca60a9475ab4ceab4bc463439012f0bab91_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3974eca60a9475ab4ceab4bc463439012f0bab91_2_1380x776.png 2x" data-dominant-color="B9BADB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">HungUp</span><span class="informations">1920×1080 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @mikebind (2022-01-21 20:49 UTC)

<p><a class="mention" href="/u/pavel_zhabyeyev">@Pavel_Zhabyeyev</a>, the VMTK extension has been working for months now, so it is likely unrelated to the earlier posts on this thread.  I would suggest reposting this as a new topic.  It is more likely to get attention that way.</p>

---

## Post #12 by @Pavel_Zhabyeyev (2022-01-22 00:36 UTC)

<p>Mike, I am not alleging that VMTK is terribly broken. Most likely, I did not set one of the parameters properly or did not initialize something somewhere. I was trying to follow the YouTube tutorial <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" class="inline-onebox" rel="noopener nofollow ugc">New vessel branch extraction module for 3D Slicer - YouTube</a><br>
It seems I set everything as it was described there, but the slicer was stuck / unresponsive.</p>
<p>I have submitted the new topic.</p>

---
