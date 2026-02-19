---
topic_id: 17931
title: "How To Read Bimg File Format"
date: 2021-06-03
url: https://discourse.slicer.org/t/17931
---

# How to read .bimg file format?

**Topic ID**: 17931
**Date**: 2021-06-03
**URL**: https://discourse.slicer.org/t/how-to-read-bimg-file-format/17931

---

## Post #1 by @sulaimanvesal (2021-06-03 04:27 UTC)

<p>Hi,</p>
<p>I wanted to ask, if we can read .bimg file format in 3D slicer! I have received some raw ultrasound data stored in *<strong>.bimg</strong> file format (I think, it’s a video frames). However, I looked all  over the net to find some information but no success.</p>

---

## Post #2 by @lassoan (2021-06-03 13:20 UTC)

<p>This is the first time I hear about this file format. I would recommend to ask your collaborators to save images in more commonly used formats, such as <em>nrrd</em>.</p>
<p>You can read any uncompressed image data set using <a href="https://github.com/lassoan/SlicerRawImageGuess">RawImageGuess</a>.</p>
<p>If you often need to read such files and you can make sense of the file format (the image header is in text or easy-to-parse binary) then you can write a simple <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py#L28-L84">Python-scripted file reader plugin</a>.</p>

---

## Post #3 by @niseto (2025-08-05 13:27 UTC)

<p>I have the same question. Did you manage to open .bimg files? I tried with RawImageGuess but, altough I see data and sometimes it clears up a bit, I was not able to load it correctly.</p>

---

## Post #4 by @Unicom (2025-08-11 06:46 UTC)

<blockquote>
<p>.bimg files are a proprietary file format used to store ultrasound image data, primarily associated with FUJIFILM VisualSonics Vevo series ultrasound imaging systems. They are typically used to store reconstructed ultrasound images or video frame data and are commonly found in small animal or preclinical imaging studies. Files in this format usually range from 17MB to 99MB in size and are stored in research folders along with other auxiliary files (such as .vxml or .pimg).</p>
</blockquote>
<p>To read or analyze .bimg files, the use of FUJIFILM VisualSonics’ Vevo LAB software is recommended. If an open-source alternative is needed, one can try the 3D Slicer software combined with the RawImageGuess tool, though custom scripts or conversion to more general formats like NRRD may be required.</p>
<p>Share the download link for the file, and I can assist with analysis and testing.</p>

---

## Post #5 by @niseto (2025-08-11 08:09 UTC)

<p>That would be great! I can’t seem to make RawImageGuess work for these images.</p>
<p>Here’s a link to a bimg file and associated auxiliary files: <a href="https://www.dropbox.com/scl/fi/psni1fbvy0wakkqn22ygb/bimg_test.zip?rlkey=kncv9y4uiedwm930tlqko2pvd&amp;st=v4pqzoi4&amp;dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/scl/fi/psni1fbvy0wakkqn22ygb/bimg_test.zip?rlkey=kncv9y4uiedwm930tlqko2pvd&amp;st=v4pqzoi4&amp;dl=0</a></p>
<p>Many thanks!</p>

---

## Post #6 by @Unicom (2025-08-11 11:52 UTC)

<blockquote>
<p>Here’s a link to a bimg file and associated auxiliary files:</p>
</blockquote>
<p>The device and software information is as follows：</p>
<ul>
<li><strong>Manufacturer:</strong> FUJIFILM VisualSonics</li>
<li><strong>System Series:</strong> Vevo 3100 series</li>
<li><strong>Accompanying Software:</strong> VevoLab (Version 3.2.7.15251)</li>
<li><strong>Transducer Model:</strong> MX550D (a high-frequency linear transducer)</li>
</ul>
<p>This image data can only be opened with this software (though it might be convertible to DICOM format), and the software requires a dongle to run.<br>
There is such equipment at an animal experiment center of a university in my city, but it is some distance away from me.</p>

---
