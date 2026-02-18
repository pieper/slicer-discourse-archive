# Surface Toolbox of 3D Slicer do not work in Windows

**Topic ID**: 40717
**Date**: 2024-12-16
**URL**: https://discourse.slicer.org/t/surface-toolbox-of-3d-slicer-do-not-work-in-windows/40717

---

## Post #1 by @Puja_Ghosh (2024-12-16 17:17 UTC)

<p>How to use surface toolbox in 3d slicer in Windows? why it keeps giving this error: C:\Users\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:2786: UserWarning: does not have observer<br>
warn(“does not have observer”)<br>
Can anyone please tell me if there is need for any installation or anything? if so, then how to do that?</p>

---

## Post #2 by @cpinter (2024-12-18 15:32 UTC)

<p>I don’t think this error has anything to do with why Surface Toolbox does not work for you. Unfortunately this error appears no matter what, but it’s harmless.</p>
<p>Can you describe in detail how Surface Toolbox does not work? What you do <em>exactly</em>, what steps in what order, then what do you expect, and what happens instead?</p>

---

## Post #3 by @Puja_Ghosh (2024-12-30 18:43 UTC)

<p>Thanks Pinter for your help. After running this command line: slicer.util.pip_install(“pyacvd&lt;0.3”), surface toolbox is working now.</p>

---

## Post #4 by @jamesobutler (2024-12-30 22:24 UTC)

<p><a class="mention" href="/u/puja_ghosh">@Puja_Ghosh</a> How did you determine that you needed pyacvd&lt;0.3?</p>
<p>Was it from this post? Or self-discovery?</p>
<aside class="quote" data-post="3" data-topic="38448">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/importerror-with-uniform-remesh/38448/3">ImportError with Uniform Remesh</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Unfortunately, pyacvd developers broke their package in their 0.3.0 version by adding C code that needs to be compiled and it is only compatible with VTK hosted on PyPI. I’ve <a href="https://github.com/pyvista/pyacvd/issues/56" rel="noopener nofollow ugc">submitted an issue to their tracker</a>, but since probably they will not fix this for a long time, I’ll add a version restriction to only use pyacvd&lt;0.3. 
In the meantime, you can fix the issue by executing slicer.util.pip_install("pyacvd&lt;0.3") in the Slicer Python console.
  </blockquote>
</aside>

<p>Can you confirm that pyacvd==0.3.1 works successfully? That would be a follow up to the below post.</p>
<aside class="quote" data-post="9" data-topic="38448">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/importerror-with-uniform-remesh/38448/9">ImportError with Uniform Remesh</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A new version of pyacvd is ready that does not depend on OpenMP. Please try if it works: 
pip_install("pyacvd==0.3.1")
  </blockquote>
</aside>

<p>Based on this information maybe <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> or <a class="mention" href="/u/lassoan">@lassoan</a> could update the install version at:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/blob/172c9d917ae695d14a3f1ad456e5bf61997b6231/SurfaceToolbox/SurfaceToolbox.py#L390">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/172c9d917ae695d14a3f1ad456e5bf61997b6231/SurfaceToolbox/SurfaceToolbox.py#L390" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/172c9d917ae695d14a3f1ad456e5bf61997b6231/SurfaceToolbox/SurfaceToolbox.py#L390" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerSurfaceToolbox/blob/172c9d917ae695d14a3f1ad456e5bf61997b6231/SurfaceToolbox/SurfaceToolbox.py#L390</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="380" style="counter-reset: li-counter 379 ;">
          <li>    return
</li>
          <li>  self.updateProcessCallback(message)
</li>
          <li>
</li>
          <li>@staticmethod
</li>
          <li>def installRemeshPrerequisites(force=False):
</li>
          <li>    # install required pyacvd package
</li>
          <li>    try:
</li>
          <li>        import pyacvd
</li>
          <li>    except ModuleNotFoundError as e:
</li>
          <li>        if force or slicer.util.confirmOkCancelDisplay("This function requires 'pyacvd' Python package. Click OK to install it now."):
</li>
          <li class="selected">            slicer.util.pip_install("pyacvd")
</li>
          <li>        else:
</li>
          <li>            return False
</li>
          <li>    return True
</li>
          <li>
</li>
          <li>@staticmethod
</li>
          <li>def remesh(inputModel, outputModel, subdivide=0, clusters=10000):
</li>
          <li>  """Uniformly remesh the surface using ACVD algorithm (https://github.com/pyvista/pyacvd). It requires pyacvd Python package.
</li>
          <li>
</li>
          <li>  :param subdivide: Subdivide each cells this number of times before remesh. Each subdivision creates 4 triangles for each input triangle.
</li>
          <li>    This is needed if the required number of desired points is higher than the number of points in the input mesh, or there are some too large cells in the input mesh.
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Puja_Ghosh (2024-12-30 22:27 UTC)

<p>Hi James,<br>
I got this command from the post that you have shared and it worked successfully for me.</p>

---

## Post #6 by @mau_igna_06 (2024-12-30 23:34 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>I’ve created a PR with the fix: <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/69" class="inline-onebox" rel="noopener nofollow ugc">BUG: fix uniform remesh not working by mauigna06 · Pull Request #69 · Slicer/SlicerSurfaceToolbox · GitHub</a></p>
<p>Have a great new year <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
