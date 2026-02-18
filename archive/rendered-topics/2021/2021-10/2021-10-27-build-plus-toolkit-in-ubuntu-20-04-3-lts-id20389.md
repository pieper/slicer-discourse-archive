# Build Plus Toolkit in Ubuntu 20.04.3 LTS

**Topic ID**: 20389
**Date**: 2021-10-27
**URL**: https://discourse.slicer.org/t/build-plus-toolkit-in-ubuntu-20-04-3-lts/20389

---

## Post #1 by @lb123 (2021-10-27 16:27 UTC)

<p>Hi,</p>
<p>I’m trying to build Plus Toolkit 2.8 in Ubuntu 20.04.3 LTS.<br>
I have followed the information of this page <a href="https://github.com/PlusToolkit/PlusBuild/blob/master/Docs/BuildInstructionsLinux.md" class="inline-onebox" rel="noopener nofollow ugc">PlusBuild/BuildInstructionsLinux.md at master · PlusToolkit/PlusBuild · GitHub</a></p>
<p>The only thing I did in a different way is that I launched this command “sudo apt build-dep vtk7” instead of “sudo apt build-dep vtk” because the second one is not working.</p>
<p>During the building process, I am getting the following error:</p>
<pre><code class="lang-auto">[100%] Linking CXX shared library /home/user/devel/PlusBuild-bin/bin/libvtkViewsQt-7.1.so
[100%] Built target vtkViewsQt
[ 51%] No install step for 'vtk'
[ 53%] Completed 'vtk'
[ 53%] Built target vtk
make: *** [Makefile:95: all] Error 2
</code></pre>
<p>Have any of you already experienced this issue?<br>
Do you have any suggestion?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-10-28 02:05 UTC)

<p>This is already being discussed here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/PlusToolkit/PlusLib/discussions/858">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PlusToolkit/PlusLib/discussions/858" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/7c0d23d28a81944c05f0f2872375843dc7cae06d6f8ada4c494cd1233935cab0/PlusToolkit/PlusLib/discussions/858" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/PlusToolkit/PlusLib/discussions/858" target="_blank" rel="noopener">Build Plus Toolkit in Ubuntu 20.04.3 LTS · Discussion #858 · PlusToolkit/PlusLib</a></h3>

  <p>Hi, I’m trying to build Plus Toolkit 2.8 in Ubuntu 20.04.3 LTS. I have followed the information of this page https://github.com/PlusToolkit/PlusBuild/blob/master/Docs/BuildInstructionsLinux.md The ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
