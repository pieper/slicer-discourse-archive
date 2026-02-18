# Save subject hierarchy

**Topic ID**: 8488
**Date**: 2019-09-18
**URL**: https://discourse.slicer.org/t/save-subject-hierarchy/8488

---

## Post #1 by @tabildskov (2019-09-18 22:33 UTC)

<p>Hello,</p>
<p>I am trying to save the subject hierarchy<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5645d0becc42809bba8c5f500ba68a10f6346e2.jpeg" data-download-href="/uploads/short-url/sad5xG7jxdqqa0suIWjD3hmhlDA.jpeg?dl=1" title="screen-grab-slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5645d0becc42809bba8c5f500ba68a10f6346e2_2_690x494.jpeg" alt="screen-grab-slicer" data-base62-sha1="sad5xG7jxdqqa0suIWjD3hmhlDA" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5645d0becc42809bba8c5f500ba68a10f6346e2_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5645d0becc42809bba8c5f500ba68a10f6346e2_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5645d0becc42809bba8c5f500ba68a10f6346e2_2_1380x988.jpeg 2x" data-dominant-color="777778"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen-grab-slicer</span><span class="informations">1466×1050 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> . The problem is, when I use the normal save command, it does not save the organization as I have it now.</p>
<p>Do I need to do something different in order to preserve the organization?</p>
<p>Thanks,</p>
<p>Tracy</p>

---

## Post #2 by @lassoan (2019-09-18 22:37 UTC)

<p>Subject hierarchy is saved in the scene file (.mrml) which is an XML file that can be parsed quote easily. You can also write a short Python script that iterates through the subject hierarchy node and writes it into any format you prefer.</p>

---

## Post #3 by @pieper (2019-09-18 22:50 UTC)

<aside class="quote no-group" data-username="tabildskov" data-post="1" data-topic="8488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tabildskov/48/6245_2.png" class="avatar"> tabildskov:</div>
<blockquote>
<p>The problem is, when I use the normal save command, it does not save the organization as I have it now.</p>
<p>Do I need to do something different in order to preserve the organization?</p>
</blockquote>
</aside>
<p>Are you saying it doesn’t reload in Slicer the way you saved it?  It’s should.  Or are you saying you want to access the hierarchy from external software?</p>

---

## Post #4 by @tabildskov (2019-09-18 22:51 UTC)

<p>Hi Sir,</p>
<p>When I open up the .mrml file many of the .vtk models do not open up in the folders I put them into.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bfb1bec79bf421f827e61e0ec9d1f2d2cc16f7a.jpeg" data-download-href="/uploads/short-url/mfS0pvy8V5pPi3Jy3qktb06oOAq.jpeg?dl=1" title="screen-grab-slicer-problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bfb1bec79bf421f827e61e0ec9d1f2d2cc16f7a_2_618x500.jpeg" alt="screen-grab-slicer-problem" data-base62-sha1="mfS0pvy8V5pPi3Jy3qktb06oOAq" width="618" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bfb1bec79bf421f827e61e0ec9d1f2d2cc16f7a_2_618x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bfb1bec79bf421f827e61e0ec9d1f2d2cc16f7a_2_927x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bfb1bec79bf421f827e61e0ec9d1f2d2cc16f7a_2_1236x1000.jpeg 2x" data-dominant-color="736F6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen-grab-slicer-problem</span><span class="informations">1541×1245 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is why I thought I was doing something wrong.</p>
<p>Thanks,</p>
<p>Tracy</p>

---

## Post #5 by @tabildskov (2019-09-18 23:13 UTC)

<p>Hi Mr. Pieper,</p>
<p>Thank you for your reply.</p>
<p>Yes. It does not reload into Slicer the way that I thought it would, based on the Subject hierarchy that I have.</p>
<p>I want to get this working right in Slicer before I do anything else.</p>
<p>Thanks,</p>
<p>Tracy</p>

---

## Post #6 by @tabildskov (2019-09-18 23:25 UTC)

<p>Hello,</p>
<p>If anyone is curious they can go to my filemail link below and download a zip file of may’s files. The link will stop working Oct 17 2019.</p>
<p>Link to scene data.<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://tj-s-biomedical-imaging.filemail.com/layouts/blue2019/img/favicons/favicon-32x32.png" class="site-icon" width="16" height="16">
      <a href="https://tj-s-biomedical-imaging.filemail.com/d/guwlyybqdfttits" target="_blank" rel="nofollow noopener">Filemail</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.filemail.com/layouts/blue2019/img/logo/logo-256.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://tj-s-biomedical-imaging.filemail.com/d/guwlyybqdfttits" target="_blank" rel="nofollow noopener">TJ's Biomedical Imaging - may zip file</a></h3>

<p>Click here to view and download these shared files from Filemail.com</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Thanks,<br>
Tracy</p>

---

## Post #7 by @cpinter (2019-09-18 23:48 UTC)

<p>Which Slicer version did you use to save the scene?<br>
Did you make a model hierarchy in the Models module, or folders in Data module / Subject hierarchy?</p>
<p>Please note that I basically reimplemented the way folders work with models, which includes an updated model hierarchy import from scene. This should be integrated in Slicer tonight or tomorrow, so it will be in Friday’s preview version. I’ll try to load your scene tomorrow and let you know if it’s different from your screenshot.</p>

---

## Post #8 by @cpinter (2019-09-19 15:10 UTC)

<p>I tried to load the scene in the latest version, I got a good-looking hierarchy. Please download the preview version tomorrow and try with that.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ad879869de414329b95e0b02ef2f57b8403fd7.png" data-download-href="/uploads/short-url/bWfpLKREz1Tz7YLl7EgbyrC7Yh1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ad879869de414329b95e0b02ef2f57b8403fd7.png" alt="image" data-base62-sha1="bWfpLKREz1Tz7YLl7EgbyrC7Yh1" width="355" height="500" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">382×537 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @tabildskov (2019-09-19 23:29 UTC)

<p>Hi Pinter,</p>
<p>I downloaded and installed the preview version and while I greatly appreciate your work unfortunately the preview version has other problems for me.</p>
<p>Here are a few of the abnormalities in the preview version.</p>
<ol>
<li>It has duplicate instances of the same model. Both instances have the same MRML ID.</li>
<li>One instance, I can rename the other instance I cannot rename.</li>
<li>If I try to delete one instance the geometry is deleted from the scene but the other instance remains (sometimes).</li>
</ol>
<p>Sorry about the bad news. I am sure you and the Slicer team will eventually get it right.</p>
<p>Thanks,</p>
<p>Tracy</p>

---

## Post #10 by @lassoan (2019-09-20 00:21 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> asked you to download the preview version <em>tomorrow</em> or later. Today’s version does not contain any of his fixes.</p>

---

## Post #11 by @cpinter (2019-09-20 13:42 UTC)

<p>Yes, please try it today (<a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.11.0-2019-09-19-macosx-amd64.dmg&amp;checksum=d7f7de624e0684410e209152ca17e872" rel="nofollow noopener">here’s the MacOS link</a>). After integrating someone it takes one night for the changes to appear in the downloaded installer.</p>
<p>If you find any errors in today’s preview or later, don’t hesitate to report it. It’s still fresh, so I’m happy to fix arising issues.</p>

---
