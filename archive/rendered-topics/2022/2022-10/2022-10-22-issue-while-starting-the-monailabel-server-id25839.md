# Issue while starting the MONAILabel server

**Topic ID**: 25839
**Date**: 2022-10-22
**URL**: https://discourse.slicer.org/t/issue-while-starting-the-monailabel-server/25839

---

## Post #1 by @deboshree_roy (2022-10-22 11:44 UTC)

<p>Problem report for Slicer 5.0.3 win-amd64: [please describe expected and actual behavior]<br>
While initializing the server an error message -<br>
[2022-10-22 12:03:10,941] [2356] [MainThread] [INFO] (uvicorn.error:59) - Application startup complete.<br>
[2022-10-22 12:03:11,013] [2356] [MainThread] [INFO] (uvicorn.error:206) - Uvicorn running on <a href="http://0.0.0.0:8000" rel="noopener nofollow ugc">http://0.0.0.0:8000</a> (Press CTRL+C to quit)</p>
<p>I am able to grow seeds, while training the model or auto segmentation of model the software stops responding.<br>
uvicorn version - 0.17.6<br>
Earlier I was using the latest version available.<br>
The issue persiste with both the servers</p>

---

## Post #2 by @pieper (2022-10-22 15:28 UTC)

<p>Looks like you are asking about MONAI Label.  Probably better to post to the project-specific discussion page.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Project-MONAI/MONAILabel/discussions">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Project-MONAI/MONAILabel/discussions" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/8eddb7e87ecf1a6697bcca97c295361090b36ae57320cb7678352dabab742a09/Project-MONAI/MONAILabel" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Project-MONAI/MONAILabel/discussions" target="_blank" rel="noopener">Discussions · Project-MONAI/MONAILabel</a></h3>

  <p>MONAI Label is an intelligent open source image labeling and learning tool. - Discussions · Project-MONAI/MONAILabel</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @natachavalador (2025-01-27 18:09 UTC)

<p>Hi,<br>
It seems I am facing the same problem with the server.</p>
<p>. Running on my own pc (Windows 11)<br>
. 3D Slicer installed with MonaiLabel plug-in working<br>
. Tryed Anaconda, Python 3.11 and Visual Studio Code as an interface<br>
. Followed precisely all tutorials from Andres Pinto and the server remains not working<br>
. Tried to mix my personal IP with the Port :8000 and the error remains</p>
<p>Could you please help me?</p>
<p>KR,<br>
Natacha Valador</p>

---
