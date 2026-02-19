---
topic_id: 1259
title: "Measuring Thickness"
date: 2017-10-21
url: https://discourse.slicer.org/t/1259
---

# Measuring thickness

**Topic ID**: 1259
**Date**: 2017-10-21
**URL**: https://discourse.slicer.org/t/measuring-thickness/1259

---

## Post #1 by @navid_mosleminiya (2017-10-21 13:08 UTC)

<p>how can I measure thickness in every point of the object and report with a color map<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd5ce43f399bcd6380156e854df69af6e6c722ee.jpeg" data-download-href="/uploads/short-url/r1bgc9WWkAKcqGCKZef0sVNRZMi.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/bd5ce43f399bcd6380156e854df69af6e6c722ee_2_690x388.jpg" alt="image" data-base62-sha1="r1bgc9WWkAKcqGCKZef0sVNRZMi" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/bd5ce43f399bcd6380156e854df69af6e6c722ee_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/bd5ce43f399bcd6380156e854df69af6e6c722ee_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/bd5ce43f399bcd6380156e854df69af6e6c722ee_2_1380x776.jpg 2x" data-dominant-color="817775"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×900 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
like this photo?</p>

---

## Post #2 by @pieper (2017-10-23 18:07 UTC)

<p>If you have two models, one of the inner surface and one of the outer surface you could use this extension:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Extensions/ModelToModelDistance" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Extensions/ModelToModelDistance</a></p>
<p>Or if you means specifically you want to measure cortical thickness from mri you could look into Freesurfer (<a href="http://surfer.nmr.mgh.harvard.edu/">http://surfer.nmr.mgh.harvard.edu/</a>)</p>

---

## Post #3 by @navid_mosleminiya (2017-10-25 14:54 UTC)

<p>I want to perform cortical thickness analysis on a closed surface, isn’t this possible in the slicer at all?</p>

---

## Post #4 by @pieper (2017-10-25 15:25 UTC)

<p>Can you be more specific about what you need and why freesurfer doesn’t already do it?  Slicer does a lot of things but we try not to duplicate tools that already exist.</p>

---

## Post #5 by @navid_mosleminiya (2017-10-27 05:53 UTC)

<p>I need to do thickness analyzing in slicer, freesurfer is only on mac and linux which I don’t have and also is huge(4.4-4.6GB) so I would rather to do this with slicer</p>

---

## Post #6 by @pieper (2017-10-27 12:25 UTC)

<p>Sorry, I don’t think there’s any easy way to do that.</p>

---

## Post #7 by @ihnorton (2017-10-27 14:09 UTC)

<p>Options:</p>
<ul>
<li>run in a virtual machine (VirtualBox is free; I think VMWare Player or current equivalent is also still free and has better graphics performance)</li>
<li>if you have up-to-date Windows 10, you may be able to run under Windows Subsystem for Linux; someone posted instructions here:</li>
</ul>
<p><a href="http://nuclear-imaging.info/site_content/2016/09/12/installing-running-freesurfer-windows-10/" class="onebox" target="_blank">http://nuclear-imaging.info/site_content/2016/09/12/installing-running-freesurfer-windows-10/</a></p>
<p>(the second option will probably be faster and use less memory, but will have somewhat lower i/o performance and possibly unknown bugs if you hit unsupported syscalls)</p>

---

## Post #8 by @navid_mosleminiya (2017-10-27 17:01 UTC)

<p>tnx can you help me how I can do this after the installation?</p>

---

## Post #9 by @ihnorton (2017-10-27 17:22 UTC)

<p>Please follow the FreeSurfer support instructions and contact them with further questions.</p>
<p><a href="https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferSupport" class="onebox" target="_blank">https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferSupport</a></p>

---
