# How to call CreateNewROI and CropVolume in python script

**Topic ID**: 40534
**Date**: 2024-12-05
**URL**: https://discourse.slicer.org/t/how-to-call-createnewroi-and-cropvolume-in-python-script/40534

---

## Post #1 by @Amy_Morton (2024-12-05 21:40 UTC)

<p>I would like to repeatedly create roi nodes and use them to create subvolumes… how do I call the underlying functions of the ui pushbuttons in the CropVolume module?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae5e5519f412a0f59f9b548eb170f045578ce3b4.png" data-download-href="/uploads/short-url/oSxbxz6oIIxmJjph0lPdvQ0bLmY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae5e5519f412a0f59f9b548eb170f045578ce3b4_2_690x409.png" alt="image" data-base62-sha1="oSxbxz6oIIxmJjph0lPdvQ0bLmY" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae5e5519f412a0f59f9b548eb170f045578ce3b4_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae5e5519f412a0f59f9b548eb170f045578ce3b4_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae5e5519f412a0f59f9b548eb170f045578ce3b4.png 2x" data-dominant-color="49474A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1211×718 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-12-07 22:32 UTC)

<p>Here are the general instructions:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>
<p>You should avoid calling the callbacks for the buttons and instead have a look at the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.h">underlying logic</a> (it’s in c++ but you can call it from python).</p>

---

## Post #3 by @chir.set (2024-12-08 07:16 UTC)

<aside class="quote no-group" data-username="Amy_Morton" data-post="1" data-topic="40534">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amy_morton/48/67318_2.png" class="avatar"> Amy_Morton:</div>
<blockquote>
<p>create roi nodes and use them to create subvolumes</p>
</blockquote>
</aside>
<p>You may find an example Python function <a href="https://gitlab.com/chir-set/RcHacks7/-/blob/f368ea0272ee13dd09cfd224c272113868dd97f1/00-Lib.py.txt#L70" rel="noopener nofollow ugc">here</a>.</p>

---
