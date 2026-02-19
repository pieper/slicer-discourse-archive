---
topic_id: 19890
title: "How To Group Fiducial Markups"
date: 2021-09-28
url: https://discourse.slicer.org/t/19890
---

# How to group fiducial markups?

**Topic ID**: 19890
**Date**: 2021-09-28
**URL**: https://discourse.slicer.org/t/how-to-group-fiducial-markups/19890

---

## Post #1 by @Kruthi (2021-09-28 00:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38.png" data-download-href="/uploads/short-url/iK4jgtvg9LdHV2MurN7Nfn9p9Rm.png?dl=1" title="Screenshot 2021-09-27 at 8.14.15 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38_2_690x424.png" alt="Screenshot 2021-09-27 at 8.14.15 PM" data-base62-sha1="iK4jgtvg9LdHV2MurN7Nfn9p9Rm" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38.png 2x" data-dominant-color="EEEEED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-09-27 at 8.14.15 PM</span><span class="informations">1074×660 72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hello,</p>
<p>I am having issues grouping the individual folders of fiducial markups into a single folder so I can edit them at the parent level to reflect the changes made to all of it. From the picture attached, t how do I group the already created markups highlighted in a blue box into a parent folder? I tried going to Data module and right clicking on the empty space in the subject hierarchy to create hierarchy from the loaded directory structure and also tried creating a new folder and dropping these markups into them. But I cannot see any changes made to these markups when I edit the parent folder. Any guidance on this is appreciated.</p>

---

## Post #2 by @smrolfe (2021-09-28 00:40 UTC)

<p>We’ve been testing an add-on to the SlicerMorph extension that will do this. I will push this tonight, so it should be available in the SlicerMorph extension in the next preview build.</p>

---

## Post #3 by @Kruthi (2021-09-28 06:12 UTC)

<p>Does that mean that it is not possible to do this under the subject hierarchy?</p>

---

## Post #4 by @smrolfe (2021-09-28 07:02 UTC)

<p>Visibility, opacity, and color can be set at the folder level as described in the post <a href="https://discourse.slicer.org/t/grouped-markups-display-control/19579/4">here</a>.</p>
<p>The <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/FormatMarkups/FormatMarkups.py" rel="noopener nofollow ugc">SlicerMorph implementation</a> copies most display properties (glyph, label, etc), and lock flags, from one node in a folder to each sibling. There is also an option to assign a unique color to each node.</p>

---

## Post #5 by @Kruthi (2021-09-28 20:48 UTC)

<p>I tried creating a new folder and added the markup-fiducial that I wanted to edit or turn off the visibility at once by dragging each file individually and also by choosing all at once and dropping them in the new folder. I did this under the data module. See the attached images. I do not get all the markups under the folder when I view them under the markups module. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38.png" data-download-href="/uploads/short-url/iK4jgtvg9LdHV2MurN7Nfn9p9Rm.png?dl=1" title="Screenshot 2021-09-27 at 8.14.15 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38_2_690x424.png" alt="Screenshot 2021-09-27 at 8.14.15 PM" data-base62-sha1="iK4jgtvg9LdHV2MurN7Nfn9p9Rm" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/835c4e06f982691dc1aff4ff2d78c0bad250ec38.png 2x" data-dominant-color="EEEEED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-09-27 at 8.14.15 PM</span><span class="informations">1074×660 72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1049662dba2e393455e950450b57b937f65c9342.png" data-download-href="/uploads/short-url/2k4TzWWjaMRU2hwVcB8nPvPwaeC.png?dl=1" title="Screenshot 2021-09-28 at 4.41.36 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1049662dba2e393455e950450b57b937f65c9342_2_449x500.png" alt="Screenshot 2021-09-28 at 4.41.36 PM" data-base62-sha1="2k4TzWWjaMRU2hwVcB8nPvPwaeC" width="449" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1049662dba2e393455e950450b57b937f65c9342_2_449x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1049662dba2e393455e950450b57b937f65c9342_2_673x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1049662dba2e393455e950450b57b937f65c9342_2_898x1000.png 2x" data-dominant-color="ECECEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-09-28 at 4.41.36 PM</span><span class="informations">1084×1206 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also when I create a folder in the Markups module, it does not allow me to drag and drop the files into the folder. If I manage to individually drag and drop them into the new folder, when I turn off the eye icon it escapes back out of the folder.</p>
<p>After trying to create folders and failing,I am having issues to load the new set of .mrb folders to try on another subject so I have to close the entire software and re-open again to load the next subject.</p>

---

## Post #6 by @smrolfe (2021-09-28 21:16 UTC)

<p>I’m not seeing this issue with the folders, which version of Slicer and OS are you using?</p>

---

## Post #7 by @Kruthi (2021-09-28 22:04 UTC)

<p>Im using Slicer 4.11.20210226<br>
and Mac OS</p>

---

## Post #8 by @smrolfe (2021-09-28 22:36 UTC)

<p>I’m seeing the same behavior using the Stable version (4.11.20210226). The current Preview version doesn’t have these issues, so it’s probably due to a bug fix since the last stable was released. I’d recommend you download the Preview version and use that instead.</p>

---

## Post #9 by @Kruthi (2021-09-29 05:12 UTC)

<p>Still does not work for the entire set of markups I just dragged and dropped. Only part of the markups in the folder change the properties as edited at the folder level.</p>
<p>Also the module panel cannot be resized to expand or reduce vertically, which makes it very hard to drag and drop the markups into the folder</p>

---

## Post #10 by @Kruthi (2021-09-29 05:15 UTC)

<p>When I turned off the visibility at the folder level, slicer shut down unexpectedly.</p>

---

## Post #11 by @lassoan (2021-09-30 13:38 UTC)

<aside class="quote no-group" data-username="Kruthi" data-post="9" data-topic="19890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/4bbf92/48.png" class="avatar"> Kruthi:</div>
<blockquote>
<p>Also the module panel cannot be resized to expand or reduce vertically, which makes it very hard to drag and drop the markups into the folder</p>
</blockquote>
</aside>
<p>The view should autoscroll if you are near the edges. That said, if you want to move many points then it may be faster to write a few-line Python script to do what you need.</p>
<aside class="quote no-group" data-username="Kruthi" data-post="10" data-topic="19890" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/4bbf92/48.png" class="avatar"> Kruthi:</div>
<blockquote>
<p>When I turned off the visibility at the folder level, slicer shut down unexpectedly.</p>
</blockquote>
</aside>
<p>Please provide instructions how to reproduce the issue and we’ll fix it immediately. Slicer crashes are extremely rare and we take them very seriously.</p>

---

## Post #12 by @Kruthi (2021-09-30 19:57 UTC)

<p>Preview version crashes all the time.</p>

---

## Post #13 by @pieper (2021-09-30 20:04 UTC)

<p>It would be much more helpful if you could describe exactly which steps you take that lead to crashes.  As <a class="mention" href="/u/lassoan">@lassoan</a> said, we take crashes very seriously and ask for your help in fixing them.</p>

---

## Post #14 by @smrolfe (2021-09-30 21:18 UTC)

<p>I can also try to replicate the issue on my Mac with with your data if you have a sample you can share, along with the steps that lead to the crash.</p>

---

## Post #15 by @smrolfe (2021-09-30 22:09 UTC)

<p>I’m still not seeing a crash, but I did find an error in the data hierarchy that appears to be Mac specific, since it’s working fine on my Windows OS. The steps to replicate on a Mac are:</p>
<ol>
<li>Create a folder in the Data module</li>
<li>Create a few fiducial nodes (I used 3)</li>
<li>From the Data module, drag and drop the nodes in to the first folder. Adjusting the color/properties at the folder level did not work for me at this step.</li>
<li>Switch to the Markups module. In the module, the nodes do not appear in the folder.</li>
</ol>
<p>If the nodes had been dragged and dropped from the Markups module, everything works as expected, so that event is probably being missed by the Data module.</p>

---

## Post #16 by @lassoan (2021-10-01 02:06 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="15" data-topic="19890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>The steps to replicate on a Mac are</p>
</blockquote>
</aside>
<p>I cannot reproduce the error that you described. Can you reproduce it using an official Slicer build? Can you record a screen capture video?</p>

---

## Post #17 by @smrolfe (2021-10-01 06:56 UTC)

<p>I’m attaching a screen capture from the Mac preview version from the downloads page today, 4.13.0-2021-09-29 r30275.</p>
<p>After adjusting the folder properties, the folder is not visible in the Markups module. When switching back to the Data module, one of the markup nodes is not visible.</p>
<p>I’m also having this issue with an older Preview version on my computer, 4.13.0-2021-09-13 r30181. In the stable version I’m not able to add nodes to a folder.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10e1acef85671aeefb1ecb53f1e782155a265a71.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10e1acef85671aeefb1ecb53f1e782155a265a71.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10e1acef85671aeefb1ecb53f1e782155a265a71.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #18 by @Kruthi (2021-10-09 20:04 UTC)

<p>Hi,</p>
<p>Sorry for the delay. When I used the preview version, I loaded the scans which are saved in .mrb format, there are fiducial marker folders existing like the image I posted. I created a new folder and tried putting the first 3 fiducial folders, when I went beyond that the software just shut down and I got an error message. When I asked another colleague, they mentioned that this version usually crashes unexpectedly.</p>

---

## Post #19 by @pieper (2021-10-09 21:21 UTC)

<aside class="quote no-group" data-username="Kruthi" data-post="18" data-topic="19890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/4bbf92/48.png" class="avatar"> Kruthi:</div>
<blockquote>
<p>When I asked another colleague, they mentioned that this version usually crashes unexpectedly.</p>
</blockquote>
</aside>
<p>If you or your colleague know of specific actions that that lead to crashes please report the details so they can be fixed.</p>

---

## Post #20 by @Kruthi (2021-10-09 22:35 UTC)

<p>We do not use the preview version anymore. I dont think it was one particular action, but from my end, it was during the above mentioned steps when the software shut down.</p>

---

## Post #21 by @lassoan (2021-10-10 00:23 UTC)

<aside class="quote no-group" data-username="Kruthi" data-post="20" data-topic="19890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/4bbf92/48.png" class="avatar"> Kruthi:</div>
<blockquote>
<p>We do not use the preview version anymore</p>
</blockquote>
</aside>
<p>Within a couple of weeks, we’ll promote the latest Slicer Preview Release to become Latest Stable Release and extension updates for the previous stable release will stop. So, it is important to investigate and fix any problems in the preview release.</p>
<p>Most likely the crash has been fixed already, but just in case you can reproduce a crash with the very latest Slicer Preview Release then please describe the steps that you did. Your description above was quite good but without having your .mrb scene file the information was insufficient.</p>

---

## Post #22 by @muratmaga (2021-10-10 00:53 UTC)

<p>Just to clarify further, is this crash happen with the FormatMarkups module after Slicermorph extension or without?</p>

---

## Post #23 by @Kruthi (2021-10-10 04:48 UTC)

<p>I have not used slicermorph extension, so I guess its without</p>

---
