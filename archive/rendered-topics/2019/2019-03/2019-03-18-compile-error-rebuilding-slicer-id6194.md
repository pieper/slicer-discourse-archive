---
topic_id: 6194
title: "Compile Error Rebuilding Slicer"
date: 2019-03-18
url: https://discourse.slicer.org/t/6194
---

# Compile error rebuilding Slicer

**Topic ID**: 6194
**Date**: 2019-03-18
**URL**: https://discourse.slicer.org/t/compile-error-rebuilding-slicer/6194

---

## Post #1 by @Lorensen (2019-03-18 19:33 UTC)

<p>Folks,</p>
<p>I’m building Slicer HEAD in a fresh directory<br>
c++ (GCC) 8.2.0<br>
cmake version 3.14.0<br>
ubuntu 14.04</p>
<p>I get the following compile error:<br>
[100%] Relocate _sysconfigdata.py and update pybuilddir.txt<br>
Segmentation fault (core dumped)<br>
make[5]: *** [bin/pybuilddir.txt] Error 139<br>
make[4]: *** [CMakeBuild/python/CMakeFiles/update_sysconfig.dir/all] Error 2<br>
make[3]: *** [all] Error 2<br>
make[2]: *** [python-prefix/src/python-stamp/python-build] Error 2<br>
make[1]: *** [CMakeFiles/python.dir/all] Error 2<br>
make: *** [all] Error 2</p>

---

## Post #2 by @Lorensen (2019-03-19 20:21 UTC)

<p>Has anyone else had this problem? Has anyone built Slicer with gcc 8.2?</p>

---

## Post #3 by @jamesobutler (2019-03-19 21:01 UTC)

<p>In Slicer’s mantis bug tracker there is issue <a href="https://issues.slicer.org/view.php?id=4612" rel="noopener nofollow ugc">4612</a> which appears to match the problem you are having and is still listed as an open issue.</p>
<blockquote>
<p>0004612: Build error with GCC/G++ 8.2.0<br>
When building Slicer Git Master with GCC/G++ 8.2.0, the build fails with a segmentation fault:</p>
</blockquote>

---

## Post #4 by @Lorensen (2019-03-19 21:18 UTC)

<p>James, thanks for the response.</p>
<p>Bill</p>

---

## Post #5 by @Lorensen (2019-03-21 05:24 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> I applied the suggested fix in <a href="https://issues.slicer.org/view.php?id=4612" rel="nofollow noopener">issue 4612</a>.</p>
<p>Slicer compiled and runs fine.</p>
<p>How do we get that fix into slicer?</p>
<p>Bill</p>

---

## Post #6 by @jamesobutler (2019-03-21 06:30 UTC)

<p>If the fix that worked for you was updating Slicer’s python from 2.7.13 to a version that is &lt;3.0 and &gt;=2.7.15 that is great to hear.</p>
<p>Work is scheduled to move Slicer to python 3 and this is happening starting this Monday. See</p><aside class="quote quote-modified" data-post="3" data-topic="4662">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/updating-slicer-to-work-with-python-3/4662/3">Updating slicer to work with python 3</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    This past week, we were busy modernizing the Slicer code base. See <a href="https://discourse.slicer.org/t/c-11-modernization-update-to-itk5-removal-of-obsolete-qt4-and-vtk7-support/6165" class="inline-onebox">C++11 modernization, update to ITK5, removal of obsolete Qt4 and VTK7 support</a> 
This delayed the transition to Python 3. The associated effort will be resumed on March 25th. 
In the mean time, here is a work-in-progress topic based on some preliminary work from  <a class="mention" href="/u/ihnorton">@ihnorton</a> 


Cc: <a class="mention" href="/u/bpaniagua">@bpaniagua</a> <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a>
  </blockquote>
</aside>

<p>It seems like python 3.6.5 and later also has the fix. So the transition to python 3 next week will be the likely path to how the issue will be resolved in Slicer.</p>

---

## Post #7 by @Lorensen (2019-03-21 11:23 UTC)

<p>I can wait for the update to python3. I’ll use the python2 fix for now.</p>
<p>Thanks</p>

---
