# Show 2D slices based on needle tip location in Slicer 4

**Topic ID**: 9836
**Date**: 2020-01-16
**URL**: https://discourse.slicer.org/t/show-2d-slices-based-on-needle-tip-location-in-slicer-4/9836

---

## Post #1 by @gjackson (2020-01-16 14:31 UTC)

<p>Hi all,</p>
<p>I’m using OpenIGTLinkIF to stream tracking data from an NDI Aurora tracking system into Slicer. (I work at NDI.) I’m tracking a needle, and in Slicer 3.x was able to have the relevant 2D slices show based on the position of the needle tip, with the needle tip showing in the 2D images. I believe all this was controlled in the “Visualization/Slice Control” section of the OpenIGTLink module. It seems that in Slicer 4.4/4.10, the “Visualization/Slice Control” section is no longer there. Is there some way to do this in Slicer 4?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-01-16 14:43 UTC)

<p>This feature is implemented in SlicerIGT extension’s Volume Reslice Driver module. See <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> for more information about how to sett up Slicer as sophisticated image guidance and navigation systems. If you write more details about your application then we are happy to give you further pointers.</p>

---

## Post #3 by @gjackson (2020-01-16 15:06 UTC)

<p>Thanks Andras! I just tried to download the SlicerIGT extension (via Slicer 4.4 extension manager) but the download failed. I then tried to download it directly from <a href="http://slicer.kitware.com/midas3/slicerappstore/extension/view?extensionId=91085" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore/extension/view?extensionId=91085</a> and got the following error:</p>
<p><strong>The system has encountered the following error:</strong></p>
<p><strong>Unable to find file on the disk</strong><br>
<strong>In /projects/src/Midas3/core/controllers/components/DownloadBitstreamComponent.php, line: 45</strong><br>
<strong>At 10:05:29 2020-01-16.</strong></p>
<p>Any ideas?</p>
<p>Thanks for your help!</p>

---

## Post #4 by @lassoan (2020-01-16 15:07 UTC)

<p>You always need to use latest stable or latest preview version of Slicer (currently 4.10.2 or 4.11.x).</p>

---

## Post #5 by @gjackson (2020-01-16 15:58 UTC)

<p>Hi Andras,</p>
<p>I can’t seem to get it working in 4.10.2 or  4.11. In the OpenIGTLinkIF module, under I/O Configuration, when I expand Scene and IGTLConnector, nothing appears under IN. When I use Slicer 4.4, the two tools I have connected show up right away, but not in 4.10.2 or 4.11. (I had this problem early, which is actually why I was using 4.4)</p>
<p>This is 4.11 (4.10.2 does the same):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da1abe253f2d34163bfc3ac2743e336a1bb12c97.png" data-download-href="/uploads/short-url/v7rnQAoCixKFidXopVMTdVDmkVp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da1abe253f2d34163bfc3ac2743e336a1bb12c97.png" alt="image" data-base62-sha1="v7rnQAoCixKFidXopVMTdVDmkVp" width="602" height="500" data-dominant-color="EFF3F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">649×539 12.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And here is 4.4:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/462ff9295e4a4961516b5a35ba2391ca559599ee.png" data-download-href="/uploads/short-url/a0UcIT3SiOHjZHiFuRbx6ogEgc6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/462ff9295e4a4961516b5a35ba2391ca559599ee.png" alt="image" data-base62-sha1="a0UcIT3SiOHjZHiFuRbx6ogEgc6" width="596" height="500" data-dominant-color="F1F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">650×545 13.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @lassoan (2020-01-16 16:09 UTC)

<p>If transforms don’t show up then you don’t receive them. What software do you use as OpenIGTLink server?</p>

---

## Post #7 by @gjackson (2020-01-16 16:11 UTC)

<p>We have an OpenIGTLink server built into our NDI software.</p>

---

## Post #8 by @lassoan (2020-01-17 14:03 UTC)

<p>Do you use latest OpenIGTLink library version?<br>
Is it a standalone application? Can we access it (preferably the source code, but at least a binary package) so that we can test it with Slicer?</p>

---

## Post #9 by @gjackson (2020-01-20 12:13 UTC)

<p>Hi Andras,</p>
<p>I’m not sure–I will check with our development team whether we are using the lastest library version.</p>
<p>I can’t share the source code with you, but I can share the program. Do you have access to an NDI device (either Polaris or Aurora) and our NDI ToolBox software? If so, you can start our OpenIGT link server by starting NDI ToolBox via the command line. From the ToolBox install directly, use “jre\bin\java -cp toolbox.jar ndi.app.igtlink.IGTLinkPanel”.</p>

---

## Post #10 by @lassoan (2020-01-20 12:45 UTC)

<p>We have a couple of NDI trackers, so we’ll test with them after we get back from the Slicer project on February 3.</p>

---
