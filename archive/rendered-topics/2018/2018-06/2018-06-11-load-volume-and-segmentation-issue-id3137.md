# Load volume and segmentation issue

**Topic ID**: 3137
**Date**: 2018-06-11
**URL**: https://discourse.slicer.org/t/load-volume-and-segmentation-issue/3137

---

## Post #1 by @trnhx001 (2018-06-11 15:23 UTC)

<p>Operating system: Window 7<br>
Slicer version: 4.8.1<br>
Expected behavior:Load files and display successfully<br>
Actual behavior: False</p>
<p>Hi again,</p>
<p>I am new to using Python Interactor in 3D Slicer. I am trying to load DCOM/NRRD file for CT Scan Images, load 2 separate segmentations of the same part of carotid. I want to  smooth the segmentations and compare the two, and then save the views.</p>
<p>However, when I tried to load the volume. It keeps showing something like below:</p>
<blockquote>
<blockquote>
<blockquote>
<p>slicer.util.loadVolume(slicer.app.slicerHome + “D:\projects\From_CAD\carotid_annotations\subject9\4 CarotidAngio 1.0 B30f.nrrd”)<br>
False</p>
</blockquote>
</blockquote>
</blockquote>
<p>Can I know what I did wrong here? Moreover, is there anyway to download slicer module to use it in SPyder/Anaconda?</p>
<p>Thank you so much for your help.</p>

---

## Post #2 by @cpinter (2018-06-11 15:55 UTC)

<p>If you do this:</p>
<pre><code>path = slicer.app.slicerHome + “D:\projects\From_CAD\carotid_annotations\subject9_1.3.12.2.1107.5.1.4.54143.30000006102300243942100012919\4 CarotidAngio 1.0 B30f.nrrd”
path
</code></pre>
<p>then you’ll see that the string contains an invalid path. It is not a surprise, as you concatenate a(n almost) valid path to the Slicer home directory. I say almost valid, because backslases are not handled properly unless you add an ‘r’ character before the first quote.</p>
<p>That said, if you want a python script that you can re-use, then using full paths is not a good practice. Your original idea to use the home folder is a good one, but then you need to complete it with a relative path, and not an absolute one.</p>

---

## Post #3 by @Saima (2018-09-12 08:35 UTC)

<p>how to do the relative path setting?</p>

---

## Post #4 by @cpinter (2018-09-12 14:54 UTC)

<p>Please ask the question in a new thread and make it specific so that it can be answered. Thanks!</p>

---
