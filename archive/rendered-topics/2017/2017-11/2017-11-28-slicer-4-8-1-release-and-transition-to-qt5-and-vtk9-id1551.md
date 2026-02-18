# Slicer 4.8.1 release and transition to Qt5 and VTK9

**Topic ID**: 1551
**Date**: 2017-11-28
**URL**: https://discourse.slicer.org/t/slicer-4-8-1-release-and-transition-to-qt5-and-vtk9/1551

---

## Post #1 by @jcfr (2017-11-28 22:57 UTC)

<p>Hi Slicers,</p>
<p>Next week, I suggest we release Slicer 4.8.1 based of the current master.</p>
<p>Then, we will toggle the default version of Qt, VTK as well as the C++ version to Qt5, VTK9 and C++11.</p>
<p>Let us know what you think.</p>

---

## Post #2 by @hjmjohnson (2017-11-29 00:02 UTC)

<p>JC,</p>
<p>I am so excited for these changes!  I can’t wait for C++11 to be the default.  I think that the added checks and extended capabilities of C++11 will make the overall code base much stronger in the long run.</p>
<p>Hans</p>

---

## Post #3 by @jcfr (2017-12-05 23:48 UTC)

<p>Hi Slicers,</p>
<p>If tomorrow dashboard is green and unless there is any objection, we will release Slicer 4.8.1 based on current master <code>(*)</code>.</p>
<p><code>(*)</code> current master: This means cherry-picking all commits since the release onto <a href="https://github.com/Slicer/Slicer/tree/master-48">slicer/Slicer@master-48</a> branch</p>

---

## Post #4 by @lassoan (2017-12-06 15:52 UTC)

<p>VMTK extension packaging on Mac broke by the changes done right after releasing 4.8.0. It means that after 4.8.1 is merged, VMTK will not be available for Mac in 4.8.1. <a class="mention" href="/u/jcfr">@jcfr</a> Could you have a look and see if you can fix it? See details here: <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/11">https://github.com/vmtk/SlicerExtension-VMTK/issues/11</a></p>

---

## Post #5 by @jcfr (2017-12-06 15:54 UTC)

<p>Most likely related to <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26488">r26488</a>, I will  have a look asap.</p>

---

## Post #6 by @jcfr (2017-12-15 23:55 UTC)

<blockquote>
<p>VMTK extension packaging</p>
</blockquote>
<p>This is the last outstanding issue. As soon as this is addressed, most likely tomorrow, I will cut the release.</p>

---

## Post #7 by @jcfr (2017-12-20 03:56 UTC)

<p>Updates:</p>
<ul>
<li>
<p>The VMTK issue should now be fixed. Changes were specific to the extension. See <a href="https://github.com/vmtk/vmtk/pull/209">PR vmtk/vmtk#209</a></p>
</li>
<li>
<p>The slicer-4.8 maintenance branch is currently being updated and Slicer 4.8.1 will be tagged shortly.</p>
</li>
</ul>
<p><em>all of that from above the Atlantic at 37001 feet (or 11280m)</em></p>

---

## Post #8 by @jcfr (2017-12-20 05:29 UTC)

<p>Packages for Slicer 4.8.1 are currently being generated.</p>
<p>Once this is complete, the regular nightly builds will start.</p>
<p>Notes:</p>
<ul>
<li>
<p>At first, packages for Slicer 4.8.1 will not be available on <a href="http://download.slicer.org">http://download.slicer.org</a>. They first have to be marked as released. Also the windows packages will have to be signed.</p>
<ul>
<li>
<p>In the mean time, you will be able to download the packages <a>directly from CDash</a> clicking on the <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81f83a1cebed98b499cc092f78bbc68f144688da.png" alt="" data-base62-sha1="ixLpTdAAICZ5ytWMznFxiZb8cR4" role="presentation" width="16" height="16"> icon near each build.</p>
</li>
<li>
<p>The process will be completed in the coming days. Thanks for your patience</p>
</li>
</ul>
</li>
<li>
<p>Expect some delay, since additional installer are being generated. Extensions build will take a little longer before being available.</p>
</li>
<li>
<p>Starting today, extensions for Slicer 4.8.0 will <em>NOT</em> be built anymore. Instead, extensions for Slicer 4.8.1 will be built daily.</p>
</li>
</ul>

---

## Post #9 by @jcfr (2017-12-27 08:49 UTC)

<blockquote>
<p>The process will be completed in the coming days. Thanks for your patience</p>
</blockquote>
<p>Slicer 4.8.1 packages have been marked as released (see <a href="http://slicer.kitware.com/midas3/folder/4989">http://slicer.kitware.com/midas3/folder/4989</a>) and  should show up on <a href="http://download.slicer.org/">http://download.slicer.org/</a> shortly.</p>

---

## Post #10 by @ihnorton (2018-01-02 19:23 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="1551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Then, we will toggle the default version of Qt, VTK as well as the C++ version to Qt5, VTK9 and C++11.</p>
</blockquote>
</aside>
<p>Are these items below what is still pending before the switch can be flipped?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#To_Do_List" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#To_Do_List</a></p>

---

## Post #11 by @lassoan (2018-01-03 00:42 UTC)

<p>As we have a functional stable release, I think we can afford to have some limitations in nightly releases. I would vote for switching now.</p>

---

## Post #12 by @jcfr (2018-01-03 06:19 UTC)

<p>MacOS and Linux build will be broken. If you can wait few days, we can do<br>
so during the project week.</p>
<p>Best,<br>
Jc</p>

---

## Post #13 by @Davide_Punzo (2018-01-16 23:06 UTC)

<p>Ciao <a class="mention" href="/u/jcfr">@jcfr</a>, I am just super curious about the state of the transition to Qt5/VTK9 after the project week!</p>

---
