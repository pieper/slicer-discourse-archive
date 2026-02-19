---
topic_id: 16501
title: "How To Get Name Of Loaded Mrb File With Python"
date: 2021-03-12
url: https://discourse.slicer.org/t/16501
---

# How to get name of loaded mrb file with python?

**Topic ID**: 16501
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/how-to-get-name-of-loaded-mrb-file-with-python/16501

---

## Post #1 by @mikebind (2021-03-12 17:37 UTC)

<p>I am loading a series of mrb files, doing some processing, and saving some results to csv files.  I’d like to generate the csv file name based on the mrb file name, but I can’t figure out where this is stored in Slicer.  I found slicer.mrmlScene.GetRootDirectory(), which gives me the directory I want to save to, and I know that for mrml nodes I can get their save filenames via their associated storage node, but I can’t figure out where the scene itself keeps track of its filename.  I’ve tried poking around in various documentation locations and searching around in the Slicer github repo, but I have not been able to find where the filename for the loaded scene or mrb is stored. I’ll keep looking, but if someone has a quick tip, that would be very helpful! Thanks!</p>

---

## Post #2 by @mikebind (2021-03-12 18:11 UTC)

<p>OK, I found it.  slicer.mrmlScene.GetURL() has the file path and file name of the .mrml file, and if it was actually an mrb file, it has the same path and name, just an .mrb extension instead. I assume the function is “GetURL” because mrml scenes can potentially be accessed via remote URL and not just local files?</p>

---

## Post #3 by @lassoan (2021-03-14 05:33 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="16501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I assume the function is “GetURL” because mrml scenes can potentially be accessed via remote URL and not just local files?</p>
</blockquote>
</aside>
<p>Yes. <code>GetURL</code> method name may appear very forward-looking, but actually the name has a long history.</p>
<p>MRML API was designed 15-20 years ago and that time loading scenes from network was an important use case because of limited resources in desktop computers. As computers got better, loading from network was rarely used anymore but the method name remained. As networks are getting faster and data sets are getting larger, loading from network is becoming relevant again, so we may revive this rarely used feature, with modern protocols (DICOMweb). First step in this direction is <a href="https://github.com/lassoan/SlicerDICOMwebBrowser">DICOMweb browser</a> and DICOM send via DICOMweb.</p>

---
