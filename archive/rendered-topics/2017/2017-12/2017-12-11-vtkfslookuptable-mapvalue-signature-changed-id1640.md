---
topic_id: 1640
title: "Vtkfslookuptable Mapvalue Signature Changed"
date: 2017-12-11
url: https://discourse.slicer.org/t/1640
---

# vtkFSLookupTable::MapValue signature changed

**Topic ID**: 1640
**Date**: 2017-12-11
**URL**: https://discourse.slicer.org/t/vtkfslookuptable-mapvalue-signature-changed/1640

---

## Post #1 by @dzenanz (2017-12-11 23:09 UTC)

<p>I get this compile error with hash xxx:<br>
<code>55&gt;c:\dev\slicer\libs\freesurfer\vtkFSLookupTable.h(84): error C2555: 'vtkFSLookupTable::MapValue': overriding virtual function return type differs and is not covariant from 'vtkLookupTable::MapValue' [C:\Dev\S3\Slicer-build\Libs\FreeSurfer\FreeSurfer.vcxproj]</code></p>
<p>The reason seems to be change of the MapValue method in VTK to return const char * (it was previously without <code>const</code>).</p>
<p>If we are trying to support two versions of VTK, we might need to wrap this definition in an <code>#if VTK9</code> block or something similar. If not, just adding <code>const</code> will do.</p>
<p>This was introduced in 47e5662bf321acb87f15e83d7f3415faeb44f72f (ENH: Update VTK)</p>

---

## Post #2 by @lassoan (2017-12-12 01:06 UTC)

<p>Yes, the best would be to keep compatibility with both VTK versions using <span class="hashtag">#ifdef</span>. Just send a pull request and we’ll review and merge.</p>

---

## Post #3 by @dzenanz (2017-12-12 15:26 UTC)

<p>Commit <a href="https://github.com/Slicer/VTK/commit/ce5575e36aef609c125b8c3a577a9cccd9cdde30" rel="nofollow noopener">ce5575e36aef609c125b8c3a577a9cccd9cdde30</a> by Sean McBride “Made vtkScalarsToColor::MapValue() return const” caused this. I think that change could simply be reverted, as it causes a divergence from mainline VTK. The reason for this change was not given in the commit message.</p>
<p>Edit: this is in Slicer’s fork of VTK.</p>

---

## Post #4 by @jcfr (2017-12-12 15:28 UTC)

<p>Or we could simply apply the same change on our fork of VTK7, that way after transitioning to VTK9 … the Slicer code base would work without any change.</p>

---

## Post #5 by @dzenanz (2017-12-12 17:04 UTC)

<p>If making return value const is the right thing to do, why not make a PR to mainstream VTK too? If it is not, we could apply this patch to VTK7 branch too.</p>

---

## Post #6 by @jcfr (2017-12-12 17:06 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="5" data-topic="1640">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>why not make a PR to mainstream VTK too?</p>
</blockquote>
</aside>
<p>As you pointed out, the change is already part of mainstream VTK.</p>
<p>the issue is that currently Slicer can be built with version of VTKs with and without this change.</p>
<p>I propose to update the “older” version of VTK used in Slicer to include the change</p>

---

## Post #7 by @dzenanz (2017-12-12 17:08 UTC)

<p>This change is <strong>not</strong> part of mainline VTK, that’s why I was suggesting its reversion.</p>
<p>Edit: it is, I was accidentally looking at an older master of VTK.</p>

---

## Post #8 by @jcfr (2017-12-12 17:19 UTC)

<p>Looking at the change in the master branch of VTK, it looks like the const correctness change is available. See <a href="https://github.com/Kitware/VTK/blame/master/Common/Core/vtkLookupTable.cxx#L740">https://github.com/Kitware/VTK/blame/master/Common/Core/vtkLookupTable.cxx#L740</a></p>
<p>If we backport the commit onto the older fork of VTK based of VTK7. See <a href="https://github.com/Slicer/VTK/tree/slicer-v7.1.0-2016-09-23-3b13ad9">https://github.com/Slicer/VTK/tree/slicer-v7.1.0-2016-09-23-3b13ad9</a></p>
<p>We wouldn’t have to make the code in Slicer more complex</p>

---

## Post #9 by @jcfr (2017-12-12 23:28 UTC)

<p>Commit was backported to the Slicer fork of VTK7.1, and Slicer code was updated to word with the const signature.</p>
<p>Additionally, the migration guide was updated. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/VTK7-Qt4-to-VTK9-Qt5#VTK9:_Signature_of_vtkFSLookupTable::MapValue_updated">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/VTK7-Qt4-to-VTK9-Qt5#VTK9:_Signature_of_vtkFSLookupTable::MapValue_updated</a></p>
<p>Fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26708">r26708</a></p>

---
