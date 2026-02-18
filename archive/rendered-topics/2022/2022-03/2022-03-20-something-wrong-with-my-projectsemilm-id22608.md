# Something wrong with my ProjectSemiLM

**Topic ID**: 22608
**Date**: 2022-03-20
**URL**: https://discourse.slicer.org/t/something-wrong-with-my-projectsemilm/22608

---

## Post #1 by @yyl (2022-03-20 12:55 UTC)

<p>4.11<br>
windows10<br>
I use  ProjectSemiLM to transfer semilandmarks across samples.I have existing manual landmarks on each model and  use the PseudoLMGenerator to set surface semilandmarks by generating pseudo-landmarks for the whole template and removing the landmark set with the MarkupEditor.But when I use ProjectSemiLM,no new semilandmarks are generated.<br>
1.The models of samples are cropped by crop volume,I can’t guarantee the ROI is the same，does it matter?<br>
2.Is markups fiducial CSV same as fiducial CSV?what kind of landmarks should I save? And what kind of model shoule I choose when I select the reference model used to place the initial semi-landmark points?vtk or stl?<br>
3.Is there anyelse reference videos or tutorial other than <a href="https://www.youtube.com/watch?v=UD2tmFuaSJg" class="inline-onebox" rel="noopener nofollow ugc">SlicerMorph Patch Based Semi-landmarking (Part 2) Transferring the patches to new samples - YouTube</a> and <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ProjectSemiLM" class="inline-onebox" rel="noopener nofollow ugc">SlicerMorph/Docs/ProjectSemiLM at master · SlicerMorph/SlicerMorph · GitHub</a>?</p>
<p>Thank you very much!!!</p>

---

## Post #2 by @muratmaga (2022-03-20 16:23 UTC)

<aside class="quote no-group" data-username="yyl" data-post="1" data-topic="22608">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yyl/48/14582_2.png" class="avatar"> yyl:</div>
<blockquote>
<p>I use ProjectSemiLM to transfer semilandmarks across samples.I have existing manual landmarks on each model and use the PseudoLMGenerator to set surface semilandmarks by generating pseudo-landmarks for the whole template and removing the landmark set with the MarkupEditor.But when I use ProjectSemiLM,no new semilandmarks are generated.</p>
</blockquote>
</aside>
<p>To me this points out to potential an issue with the landmark correspondence between reference landmark sets (issues with ordering, number etc). If the thin plate spline transform fails, no landmarks will be transferred to the target.</p>
<p>Do you see an error if you open the log (Ctrl+0). Without seeing your data, this is as much as I can guess.</p>
<p><code> 2.Is markups fiducial CSV same as fiducial CSV?what kind of landmarks should I save? And what kind of model shoule I choose when I select the reference model used to place the initial semi-landmark points?vtk or stl?</code></p>
<p>Yes, both markups fcsv and fcsv are the same format. We suggest using PLY format as our model format actually (not vtk or stl).</p>
<p>The reference tutorial is what you linked. Are you having problem following the instructions there?</p>

---

## Post #3 by @yyl (2022-03-22 14:18 UTC)

<p>I checked the ordering and the number of my 11 landmarks, and the log said it can not load my file which has my target model inside.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69a04591ab7c6bdf0736c35a3fbb05f82e688e6a.png" data-download-href="/uploads/short-url/f4pvVPZ8j8EElxubiDppXb5XorE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69a04591ab7c6bdf0736c35a3fbb05f82e688e6a_2_690x136.png" alt="image" data-base62-sha1="f4pvVPZ8j8EElxubiDppXb5XorE" width="690" height="136" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69a04591ab7c6bdf0736c35a3fbb05f82e688e6a_2_690x136.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69a04591ab7c6bdf0736c35a3fbb05f82e688e6a_2_1035x204.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69a04591ab7c6bdf0736c35a3fbb05f82e688e6a_2_1380x272.png 2x" data-dominant-color="DBE5EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2000×397 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2022-03-22 21:33 UTC)

<p>Log shows you are trying to load the models from a scene file. You should follow the instructions of the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ProjectSemiLM" rel="noopener nofollow ugc">ProjectSemiLMPatches</a> carefully.</p>
<p>It asks for a folder of model files.</p>

---

## Post #5 by @yyl (2022-03-23 16:07 UTC)

<p>In the beginning, I put all the files in the same folder, or this caused projectsemiLM loaded the models from a scene file. Now I put the landmarks and model files in different folders and tried different save formats. But log said IndexError: list index out of range. I looked it up online and it might mean the list is empty. When I choose the mesh dictionary and the landmark dictionary,the preview window shows that No items match my search criteria. But I do put the target files in the folders. I have no idea of this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf615d0d8ac407501c9ed63d77697d5fb7135c1.png" data-download-href="/uploads/short-url/sXtGpYVZXCOHyDAqUdFAYGLkg1P.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf615d0d8ac407501c9ed63d77697d5fb7135c1.png" alt="image" data-base62-sha1="sXtGpYVZXCOHyDAqUdFAYGLkg1P" width="690" height="162" data-dominant-color="FBFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">878×207 5.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c32cf30f16e1a5b10f53cddf56a02ed7703d1f8a.png" data-download-href="/uploads/short-url/rQBprUKZxPFMNBFEOuMtidfvNqy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c32cf30f16e1a5b10f53cddf56a02ed7703d1f8a.png" alt="image" data-base62-sha1="rQBprUKZxPFMNBFEOuMtidfvNqy" width="690" height="189" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">843×232 7.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db0e8d61ff41791f800c3761c0aa65230ff12b95.png" data-download-href="/uploads/short-url/vfRK8sHKC5lmOwOVUdOWUvngwBf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db0e8d61ff41791f800c3761c0aa65230ff12b95.png" alt="image" data-base62-sha1="vfRK8sHKC5lmOwOVUdOWUvngwBf" width="690" height="264" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">826×317 4.31 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @smrolfe (2022-03-23 16:53 UTC)

<p>Currently, the ProjectSemiLM module assumes that each mesh and landmark file will have a numerical ID in the filename so they can be matched. For example, if you add “_1” at the end of the filenames for the corresponding mesh and landmark file in your “lm” and “stl” folders, it should resolve this issue should work.</p>
<p>I will also update the interface so this is no longer a requirement, so if you’d like to wait a day or two for a new build it should be available soon.</p>

---

## Post #7 by @yyl (2022-03-24 14:06 UTC)

<p>Thank you very much for your help. I transferred semilandmarks across samples successfully!!!</p>

---
