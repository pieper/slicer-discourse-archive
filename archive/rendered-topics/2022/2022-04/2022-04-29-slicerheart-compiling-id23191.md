# SlicerHeart compiling

**Topic ID**: 23191
**Date**: 2022-04-29
**URL**: https://discourse.slicer.org/t/slicerheart-compiling/23191

---

## Post #1 by @whu (2022-04-29 07:09 UTC)

<p>who can share the experience of  building SlicerHeart from source ?<br>
1)strange error<br>
CMake Error at xx/SlicerHeart-build/ITKStrain-prefix/tmp/ITKStrain-gitupdate.cmake:97 (execute_process):<br>
2&gt;  execute_process failed command indexes:<br>
2&gt;<br>
2&gt;    1: “Child return code: 128”<br>
2)CMake variable EXTENSION_WC_REVISION is empty<br>
I have added the EXTENSION_WC_REVISION  STRING 30379 in cmake gui.</p>
<p>thanks</p>

---

## Post #2 by @cpinter (2022-04-29 10:34 UTC)

<p>You don’t need to add any variables.</p>
<p>Can you please describe your configure and build process step by step, with as much detail as possible? Thanks.</p>

---

## Post #3 by @adamrankin (2022-04-29 13:19 UTC)

<p>This can happen when the folder is not checked out from source (ie is not a git repository).</p>
<p>A workaround is to set that variable to something (1 is fine) and also set the SlicerHeart_WC_REVISION to 1 as well. This will bypass the version control checks.</p>
<p>Edit: if it’s a sub project, you’ll have to add the &lt;projectname&gt;_WC_REVISION variable to the project failing to configure.</p>

---

## Post #4 by @whu (2022-04-29 14:40 UTC)

<p>god, after using the default setting of the cmake without changing any item, all passed…<br>
sometimes I just want to add some option, as ITK_FILTER<br>
… thanks for all friends</p>

---

## Post #5 by @whu (2022-04-30 02:23 UTC)

<p>The successfully compiled SlicerHeart  has been installled mannully , by adding the directory Edit-&gt;Setting-&gt;Module.  Some function need the SlicerIGT module installed first, this module is added the same as SlicerHeart.  But when calling the SlicerHeart, Slicer GUI shows  a error message-box, SlicerHeart haven’t installed…  how to solve this kind of question? thansk</p>

---

## Post #6 by @lassoan (2022-05-03 23:09 UTC)

<p>You need to add the SlicerIGT build folders to the additional module paths, too:<br>
<code>...\SlicerIGT_R\lib\Slicer-4.13\qt-loadable-modules\Release</code><br>
<code>...\SlicerIGT_R\lib\Slicer-4.13\qt-scripted-modules</code></p>

---

## Post #7 by @whu (2022-05-04 13:02 UTC)

<p>After exactly added  the …/Release directory（firstly just to the …-modules directory）, all problem solved. Perfect!<br>
Thanks!</p>

---
