# Subject Hierarchy ExportAs plugin working only for some systems

**Topic ID**: 12696
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/subject-hierarchy-exportas-plugin-working-only-for-some-systems/12696

---

## Post #1 by @muratmaga (2020-07-22 21:40 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> implemented an <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/ExportAs" rel="nofollow noopener">ExportAs</a> plugin for SlicerMorph extension which enables Export As a right-click context menu in the Data module. For markup nodes, this works 100% from the Markups module. For other data types (namely volumes and models) we have a strange issue that it works only on some windows and mac systems (seemed to be 100% functional in linux).  There appears no diagnostic error message on systems that it doesn’t work.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> any input would be greatly appreciated.</p>
<p>Here is the discussion of the issue<br>
</p><aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/ExportAs" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/45026482?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/ExportAs" target="_blank" rel="nofollow noopener">SlicerMorph/SlicerMorph</a></h3>

<p>Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2020-07-22 22:20 UTC)

<p>Could you debug it on one of the problematic computers?</p>
<p>You can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools">attach a Python debugger to Slicer</a>, add a breakpoint to the plugin and run the script step by step.</p>

---

## Post #3 by @pieper (2020-07-22 23:30 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> - It’s not clear it’s a python issue, but maybe something with the way plugins interact.  It doesn’t appear on my local build.  Murat posted some more info on the github issue so let’s carry on the investigation there.</p>

---
