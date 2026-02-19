---
topic_id: 10657
title: "Link Openigtlink To 3D Slicer"
date: 2020-03-12
url: https://discourse.slicer.org/t/10657
---

# Link OpenIGTLink to 3D Slicer

**Topic ID**: 10657
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/link-openigtlink-to-3d-slicer/10657

---

## Post #1 by @kobidk (2020-03-12 10:04 UTC)

<p>Operating system: Window 10<br>
Slicer version:4.10.0<br>
Expected behavior: 3D Slicer viewer should recognizer OpenIGTLink IF<br>
Actual behavior: I didn’t get the connectors setting interface</p>
<p>The following remark in the document is no clear :</p>
<p>The OpenIGTLink IF module requires <a href="http://svn.na-mic.org/NAMICSandBox/trunk/OpenIGTLink" rel="nofollow noopener">The OpenIGTLink Library</a>. The library is downloaded and built in Slicer3-lib directory automatically when you run Slicer3/Script/getbuildtest.tcl.</p>
<p>The 3D Current version doesn’t have Slicer3-lib  directory.  I manage to build the library. OpenIGTLink.dll also igtlutil.dll OpenIGTLink.lib<br>
The executable file : igtlSocketTest.exe was not exited in the build products.<br>
Do I really need it.</p>

---

## Post #2 by @pieper (2020-03-12 14:49 UTC)

<p>With modern Slicer you can get the OpenIGTLink extension:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/openigtlink/SlicerOpenIGTLink" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/945382?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/openigtlink/SlicerOpenIGTLink" target="_blank">openigtlink/SlicerOpenIGTLink</a></h3>

<p>OpenIGTLinkIF module as an Slicer Extension. Contribute to openigtlink/SlicerOpenIGTLink development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
