# How to convert DTI tensor nhdr file from NRRD0004 to NRRD0005

**Topic ID**: 13016
**Date**: 2020-08-15
**URL**: https://discourse.slicer.org/t/how-to-convert-dti-tensor-nhdr-file-from-nrrd0004-to-nrrd0005/13016

---

## Post #1 by @Xiaogai_Li (2020-08-15 21:11 UTC)

<p>Dear all,</p>
<p>I wonder if there is any way to convert DTI tensor file in .nhdr format from NRRD0004 to NRRD0005?<br>
As in the header file .nhdr for tensor,<br>
NRRD0004 has a line with six components, e.g. <em>sizes: 6 181 216 179</em>, while<br>
NRRD0005 has a line with nine components, e.g.  <em>sizes: 9 181 216 179</em></p>
<p>Strangely, earlier when I saved DTI tensor into .nhdr, it wrote a .nhdr file with 6 components (NRRD0004 ), but now always writes into with 9 components (NRRD0005), though I seemed to do exactly the same steps. Any way to convert between both using Slicer? Thanks a lot for your attention.</p>
<p>Best regards, Xiaogai</p>

---

## Post #2 by @pieper (2020-08-15 21:21 UTC)

<p>Probably your version 4 file uses <code>3D-symmetric-matrix</code> while the version 5 uses <code>3D-matrix</code>.  See the <a href="http://teem.sourceforge.net/nrrd/format.html">definitions here</a>.  Either should be fine for DTI.</p>
<p>If you really need to convert, <a href="http://teem.sourceforge.net/unrrdu/">the unu command</a> should be easy to use.</p>

---

## Post #3 by @Xiaogai_Li (2020-08-15 21:46 UTC)

<p>Thanks a lot! Exactly as you said, both are fine for DTI, and only differ <code>3D-symmetric-matrix</code> and <code>3D-matrix</code>.</p>
<p>I just checked <code>unu command</code>, seems <code>unu save</code> or <code>  unu convert</code> may work, but none seem to have option to specify the conversion. Will be really appreciated if you have insights on what command to use. Thank you very much.</p>

---

## Post #4 by @Xiaogai_Li (2020-08-15 21:57 UTC)

<p>Or if there is any way to specify in Slicer 3D to save DTI files into <code>3D-symmetric-matrix</code> (version 4) format?</p>
<p>I should have mentioned that the problem occurs when I have used module <code>Resample DTI Volume</code> in Slicer, then when saving to .nhdr always ended in version 5. Thanks!</p>

---

## Post #5 by @pieper (2020-08-16 20:59 UTC)

<p>Hmm, good question - I don’t know if there’s anyway to do that without writing a C or C++ program.    All the utilities in the teem suite are pretty powerful but I don’t recall anything that handles that particular operation.  Good luck!</p>

---

## Post #6 by @Chris_Rorden (2020-09-15 14:12 UTC)

<p>Is there any reason that Slicer changed from the 6 component 3D-symmetric-matrix to the 3D-matrix? The 9 volume stores<br>
XX XY XZ XY YY YZ XZ YZ ZZ<br>
while the 6 component format removes the redundant volumes (here upper triangle):<br>
XX XY XZ YY YZ ZZ<br>
So the resulting file size and memory demands, cache penalties, etc. are all limitations of the 9 component storage. Furthermore, the compact representation would ease <a href="http://dti-tk.sourceforge.net/pmwiki/pmwiki.php?n=Documentation.Interoperability" rel="noopener nofollow ugc">interoperability</a> with other tools.</p>

---

## Post #7 by @pieper (2020-09-15 19:32 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="6" data-topic="13016">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>Is there any reason that Slicer changed from the 6 component 3D-symmetric-matrix to the 3D-matrix?</p>
</blockquote>
</aside>
<p>I don’t recall if it was a deliberate choice.  Maybe <a class="mention" href="/u/ljod">@ljod</a> knows?  I agree that taking advantage of the symmetry is a good thing in general.</p>

---
