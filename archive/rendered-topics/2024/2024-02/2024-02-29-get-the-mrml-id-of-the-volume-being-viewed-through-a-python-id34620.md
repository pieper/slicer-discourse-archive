# Get the MRML ID of the volume being viewed through a python script

**Topic ID**: 34620
**Date**: 2024-02-29
**URL**: https://discourse.slicer.org/t/get-the-mrml-id-of-the-volume-being-viewed-through-a-python-script/34620

---

## Post #1 by @petit223 (2024-02-29 17:55 UTC)

<p>I want to get the MRML ID of the volume being viewed on the interface through a python script<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/014cfd597bfd3628a6a9d4107fb469b453bea1a7.png" data-download-href="/uploads/short-url/bvqtuERszPt4bsOyIXXK0eUHMX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/014cfd597bfd3628a6a9d4107fb469b453bea1a7_2_690x308.png" alt="image" data-base62-sha1="bvqtuERszPt4bsOyIXXK0eUHMX" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/014cfd597bfd3628a6a9d4107fb469b453bea1a7_2_690x308.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/014cfd597bfd3628a6a9d4107fb469b453bea1a7_2_1035x462.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/014cfd597bfd3628a6a9d4107fb469b453bea1a7.png 2x" data-dominant-color="E4E9ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1110×496 55.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For example, now I want to get the MRML ID of “20005: Screen Save” through python code, which is ‘vtkMRMLScalarVolumeNode133’<br>
I tried using <code>slicer.app.applicationLogic().GetSelectionNode().GetActiveVolumeID()</code> but the result is not what I want.<br>
If anyone can help me I will be very grateful !!</p>

---

## Post #2 by @pieper (2024-02-29 19:29 UTC)

<p>The Data module lets you set all at once, but each slice view can have different data, so you can look up each one individually:</p>
<pre><code class="lang-auto">slicer.app.layoutManager().sliceWidget("Red").mrmlSliceCompositeNode().GetBackgroundVolumeID()
</code></pre>
<p>(get the list of view names with <code>slicer.app.layoutManager().sliceViewNames()</code>)</p>

---

## Post #3 by @petit223 (2024-03-01 13:12 UTC)

<p>Thank you very much !! I successfully got the ID I wanted.<br>
but I would also like to know how you came to know this code. I am an engineering student and am developing a 3D Slicer plug-in.<br>
thanks again for your kindness.</p>

---

## Post #4 by @pieper (2024-03-01 14:21 UTC)

<aside class="quote no-group" data-username="petit223" data-post="3" data-topic="34620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e5b9ba/48.png" class="avatar"> petit223:</div>
<blockquote>
<p>I would also like to know how you came to know this code</p>
</blockquote>
</aside>
<p>I had the advantage that I was one of the authors for that part of the code.</p>
<p>But in general, when I need to figure out how some Slicer code works I follow the method described here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>
<p>It also helps to read through the script repository, extensions, and other parts of the code just to learn what’s possible.</p>

---
