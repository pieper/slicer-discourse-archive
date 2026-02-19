---
topic_id: 10055
title: "Simpleitk Itk Vtk Autocompletion"
date: 2020-01-31
url: https://discourse.slicer.org/t/10055
---

# simpleITK, ITK,VTK Autocompletion

**Topic ID**: 10055
**Date**: 2020-01-31
**URL**: https://discourse.slicer.org/t/simpleitk-itk-vtk-autocompletion/10055

---

## Post #1 by @manjula (2020-01-31 19:46 UTC)

<p>Hi all,</p>
<p>Maybe this is not the most appropriate place to post this.</p>
<p>I am using linux system and  eclipse +PyDev for 3D Slicer extension development that we are building. But the auto completion/suggestions for vtk,itk and SimpleITK is not complete.</p>
<p>I then tried with spyder thinking of better integration in conda and it was better than eclipse.</p>
<p>Can someone tell me is this a problem with my configuration and paths or something else ?</p>
<p>Can someone let me know of the python IDE or editor that  works well with itk,vtk and simpleITK in the sense of suggestions and auto completion feature.</p>
<p>I don’t face this problem with other libraries.</p>

---

## Post #2 by @manjula (2020-02-01 09:19 UTC)

<p>Figure that out !!!</p>

---

## Post #3 by @lassoan (2020-02-01 13:45 UTC)

<p>Getting auto-complete work for non-native Python packages is not easy. What we know that during debugging it should work perfectly, but we have mixed results outside the debugger.</p>
<p>What have you found out about auto-complete that helped you?</p>

---

## Post #4 by @manjula (2020-02-01 14:06 UTC)

<p>Well i had the new machine on which i did the fresh install of linux mint. Since i was struggling with autocompletion, i though it was due to paths not been configured/updated properly and i installed conda and the vtk, itk and SimpleITK --&gt; openJDK --&gt; Eclipse --&gt; pyDev --&gt; Configure anaconda3 paths and updated.</p>
<p>and now the autocompletion on itk and vtk and simpleITK works.</p>
<p>Technically it should work the other way round but still it is not working on the computer i am typing in.</p>

---
