# How to compile MRML library

**Topic ID**: 37669
**Date**: 2024-08-02
**URL**: https://discourse.slicer.org/t/how-to-compile-mrml-library/37669

---

## Post #1 by @tomasbkk (2024-08-02 12:04 UTC)

<p>I’m trying to separate MRML library from Slicer and be able to build it separtely. So far I’ve gotten Slicer source code and used CMake to create VS solution files but I cannot find the MRML project or any of the other projects in libs folder.<br>
I checked CMake settings to see if I didn’t enable something but could not find anything relevant to MRML.<br>
As a first step I’d like to build MRML library as part of slicer, then I would like to build MRML separately.<br>
Any help with this would be appreciated.</p>
<p>As a side note, I’m not able to see any of the classes in Class View or even source code files in Solution Explorer in visual studio but I do see the projects such as itk, phyton-*, slicer, etc…<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f8c18e1fc6fcc0ebfc66d38e41ae5d2fcb52c8a.png" alt="image" data-base62-sha1="ickNkk91zdKCdI3pYYyf9SDXGX0" width="299" height="427"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fab0b170730893bc046ccc7ddea27521db5a3c45.png" alt="image" data-base62-sha1="zLHVIiRYGHqyb4D1klfST8wk8x7" width="260" height="293"></p>

---

## Post #2 by @lassoan (2024-08-03 21:40 UTC)

<p>Awesome! <a class="mention" href="/u/jcfr">@jcfr</a> is working on exactly this - making MRML easy to build independently from Slicer and make it available in Python and JavaScript. I’m not sure about the exact timeline, but probably it will be ready for testing within weeks.</p>

---

## Post #3 by @finetjul (2024-08-05 06:25 UTC)

<p>What you show is the “superbuild” of Slicer (its dependencies) and not the inner build of Slicer. You need to open the solution file that is 1 level down the tree.</p>
<p><span class="mention">@AlexyPellegrini</span> will soon update his <a href="https://github.com/Slicer/Slicer/pull/7491" rel="noopener nofollow ugc">draft PR</a>. Without additional funding, we expect something stable (yet limited to the core of Slicer) by the end of the year.</p>

---

## Post #4 by @tomasbkk (2024-08-05 07:07 UTC)

<p>Glad to hear about the MRML being made an independent library. Will wait for it.</p>
<p><a class="mention" href="/u/finetjul">@finetjul</a> can you tell me the name of the solution to open in the tree. There are so many, I tried opening SlicerExecutionModel but that doesn’t seem to be the right one.</p>

---

## Post #5 by @finetjul (2024-08-05 07:11 UTC)

<p>should be Slicer-build</p>

---
