---
topic_id: 28872
title: "Remove Ct Table From Volume Rendering"
date: 2023-04-12
url: https://discourse.slicer.org/t/28872
---

# Remove CT table from volume rendering

**Topic ID**: 28872
**Date**: 2023-04-12
**URL**: https://discourse.slicer.org/t/remove-ct-table-from-volume-rendering/28872

---

## Post #1 by @Jonathan_Millard (2023-04-12 20:37 UTC)

<p>Hello all,</p>
<p>I am attempting to visualize the skeletal elements of a CT scan (DICOM), along with taking screenshots suitable for publication. I am using the volume rendering module CT-AAA2 preset and it looks lovely; however, I can’t figure out how to manually eliminate the CT table from the image to assist with the picture clarity (I am attempting to visualize the sacrum and an unusual growth on the L side, but the table is obscuring the view.) As far as I can tell, I can only selectively crop the ROI A-P, Lateral-Medial, Superior-Inferior, but I can not crop close enough to the specimen without cutting out portions of the bone. I have attempted troubleshooting, but with no success. Any advice would be greatly appreciated - the DICOM viewer that came with the scan is not as clean as the image that 3DSlicer can produce.<br>
Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/793588ac34799d33ff94d34a8de8eb8f9216a1a2.jpeg" data-download-href="/uploads/short-url/higt7DnObsjVVSOG7jXtAxeLNFE.jpeg?dl=1" title="Screenshot 2023-04-12 162911" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/793588ac34799d33ff94d34a8de8eb8f9216a1a2_2_690x357.jpeg" alt="Screenshot 2023-04-12 162911" data-base62-sha1="higt7DnObsjVVSOG7jXtAxeLNFE" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/793588ac34799d33ff94d34a8de8eb8f9216a1a2_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/793588ac34799d33ff94d34a8de8eb8f9216a1a2_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/793588ac34799d33ff94d34a8de8eb8f9216a1a2_2_1380x714.jpeg 2x" data-dominant-color="A49DA9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-12 162911</span><span class="informations">1916×993 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-04-12 20:40 UTC)

<p>Easiest would be to use the Segment editor with the scissors to outline the part you want to keep and then use the mask volume tool to make a new volume to render.  Should be just a few clicks.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html</a></p>

---

## Post #3 by @chir.set (2023-04-12 21:02 UTC)

<p>You may <em>also</em> try the ‘Remove CT table’ module in SlicerSandbox extension that you may install using the Enxtensions manager.</p>
<p>Another option is to use <a href="https://github.com/chir-set/Tools7/tree/master/BodyIsolation" rel="noopener nofollow ugc">this</a> module that does more or less the same thing. No guarantees, just worth a try. Please read its limitations. Your result is much welcome.</p>

---

## Post #4 by @Jonathan_Millard (2023-04-12 21:05 UTC)

<p>Hey, Steve!</p>
<p>Thank you for your reply. I did think to attempt to make a segment from the scan and simply crop the CT table out with the scissors tool; however, I can’t seem to edit any of the scan with the tools. Here is a look at the screen with the thresholding tool selected; it looks like the editable area is somehow outside of the content of the scan. I have <em>some</em> experiencing segmenting, and I have never come across this problem. Since I don’t need to create a file for 3D printing etc. I thought maybe there was an easier way to selectively “crop” the image in the volume rendering module.</p>
<p>Thank you for your time, I appreciate the guidance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af859dc75bae8c1eddcfaa880fe324f9a11c2a11.png" data-download-href="/uploads/short-url/p2JPoBkOX634OUUU3dQNoSyxGHD.png?dl=1" title="Screenshot 2023-04-12 164847" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af859dc75bae8c1eddcfaa880fe324f9a11c2a11_2_690x439.png" alt="Screenshot 2023-04-12 164847" data-base62-sha1="p2JPoBkOX634OUUU3dQNoSyxGHD" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af859dc75bae8c1eddcfaa880fe324f9a11c2a11_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af859dc75bae8c1eddcfaa880fe324f9a11c2a11_2_1035x658.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af859dc75bae8c1eddcfaa880fe324f9a11c2a11_2_1380x878.png 2x" data-dominant-color="242525"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-12 164847</span><span class="informations">1543×983 245 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @pieper (2023-04-12 21:31 UTC)

<p>Try just playing with the scissors and the mask volume tools.  You will want to make the fill volume something like -1000 when you subtract the table.  To get a general idea of how the segment editor works google for tutorials.  If you really think there’s a bug or something special about your data let us know, but I think you just need to try some more things.</p>

---

## Post #6 by @lassoan (2023-04-14 02:09 UTC)

<p>The full process is explained step-by-step in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="hys1fmXmLVg" data-video-title="Remove patient table from CT images" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=hys1fmXmLVg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/hys1fmXmLVg/maxresdefault.jpg" title="Remove patient table from CT images" width="" height="">
  </a>
</div>

<p>However, CT table is usually designed so that radioopaque parts never directly touch the bones and the human body shape is generally a convex shape, so the <a href="https://github.com/PerkLab/SlicerSandbox#remove-ct-table">Remove CT table module</a> should work well in most cases, fully automatically. Have you tried it? Did it work? Have you tried the other module that <a class="mention" href="/u/chir.set">@chir.set</a> suggested?</p>

---

## Post #7 by @Jonathan_Millard (2023-04-14 14:40 UTC)

<p>Thank you, Steve!</p>
<p>I am convinced the program was being buggy. I tried multiple times to reupload the data, but every time I entered the segment editor I was unable to use any of the tools to create a segment <em>within</em> the tissue contained in the scan - I was only able to edit <em>outside</em> of the tissue contained in the scan. I tried again the next day and I was able to created segments - no problem. Thank you so much!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cf308baa858458ad75536ac3509645c7d094c06.png" alt="Screenshot 2023-04-14 092502" data-base62-sha1="4864aNMuaVWAobJ03Lwv35vLpPM" width="397" height="371"></p>

---

## Post #8 by @Jonathan_Millard (2023-04-14 14:43 UTC)

<p>Thank you, Andras!</p>
<p>I am convinced the program was being buggy. I simply reloaded my data again from fresh today and it worked fine. One can see the green thresholding highlighting <em>outside</em> of the tissue within my scan in the image I attached to my recent reply to Steve. Today, for whatever reason, it worked fine. I was able to use your recommended video to guide the masking process for my image - Thank you so much!</p>

---

## Post #9 by @lassoan (2023-04-15 03:05 UTC)

<p>Have you tried the fully automatic table removal? Did it work?</p>

---

## Post #10 by @chir.set (2023-04-15 08:16 UTC)

<p>It seems <a class="mention" href="/u/jonathan_millard">@Jonathan_Millard</a> is too busy to reply to helpers. Anyway, his last image shows success by whatever means, so good for him.</p>

---

## Post #11 by @Jonathan_Millard (2023-04-15 13:30 UTC)

<p>I didn’t try the fully automatic table removal, but after several attempts reloading the dataset the segmentation tools started cooperating. Thank you again for your time, your recommendations and linked video were extremely helpful!</p>

---

## Post #12 by @Jonathan_Millard (2023-04-15 13:36 UTC)

<p>Sorry, <a class="mention" href="/u/chir.set">@chir.set</a> - but as you can see, I have replied to helpers and expressed my genuine gratitude. I think the issue was an actual bug in the program, as evidenced by the thresholding tool image in my previous reply. After several attempts to reload my data, it finally worked. Thanks…</p>

---

## Post #13 by @pieper (2023-04-15 14:39 UTC)

<p><a class="mention" href="/u/jonathan_millard">@Jonathan_Millard</a> I’m very glad it worked for you in the end.</p>
<p>FYI, we take software bugs very seriously so if you have a way to replicate any issues you experienced please report them so that they can be investigated and fixed.  One of the main reasons we engage the community actively is to identify and fix issues so that everyone benefits.  Thanks for your help with this effort!</p>

---

## Post #14 by @lassoan (2023-04-15 16:16 UTC)

<p><a class="mention" href="/u/jonathan_millard">@Jonathan_Millard</a> I just asked about the automatic methods repeatedly because I was curious to see if that we developed works well; and to understand if there are some limitations of our tools that would make people not want to use them.</p>

---
