# Path of the loaded fiber bundle

**Topic ID**: 30524
**Date**: 2023-07-11
**URL**: https://discourse.slicer.org/t/path-of-the-loaded-fiber-bundle/30524

---

## Post #1 by @Kening_Zhang (2023-07-11 16:16 UTC)

<p>Dear developers,<br>
I am trying to get the file path of the fiber bundle loaded in the slicer, here I use a selector to assign a data, and I try to use command GetStorageNode().GetFileName() to get the path.<br>
This is my code:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59be0a10d5b64ddeb698c28bd23b8c8807cb8dfa.png" data-download-href="/uploads/short-url/cNTErbBVr2KEpchMCtNbKr68kNc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59be0a10d5b64ddeb698c28bd23b8c8807cb8dfa_2_645x500.png" alt="image" data-base62-sha1="cNTErbBVr2KEpchMCtNbKr68kNc" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59be0a10d5b64ddeb698c28bd23b8c8807cb8dfa_2_645x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59be0a10d5b64ddeb698c28bd23b8c8807cb8dfa_2_967x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59be0a10d5b64ddeb698c28bd23b8c8807cb8dfa.png 2x" data-dominant-color="39414A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1226×950 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, it failed<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67935196bad4932933e7c7afb2420c61b6ff46f7.png" data-download-href="/uploads/short-url/eMgO7dlrpeyfmSjjEvzwBcAysrd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67935196bad4932933e7c7afb2420c61b6ff46f7_2_690x95.png" alt="image" data-base62-sha1="eMgO7dlrpeyfmSjjEvzwBcAysrd" width="690" height="95" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67935196bad4932933e7c7afb2420c61b6ff46f7_2_690x95.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67935196bad4932933e7c7afb2420c61b6ff46f7_2_1035x142.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67935196bad4932933e7c7afb2420c61b6ff46f7.png 2x" data-dominant-color="3B2525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1332×184 39.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It seems like the ‘atlas’ file I loaded doesn’t have a storage node,<br>
but I indeed load it from local disk.<br>
I wonder how to solve this problem.</p>
<p>Best wishes and thanks!<br>
Joshua</p>

---

## Post #2 by @pieper (2023-07-11 18:16 UTC)

<p>Good question.</p>
<p>It looks like the <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/34dca8edf493a2261e5cc3fb1487b0933b4600c8/Modules/Loadable/TractographyDisplay/Logic/vtkSlicerFiberBundleLogic.cxx#L113-L142">AddFiberBundle method</a> doesn’t include these lines that are in the corresponding code of the AddModel method.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/f6d4eccebe92e0e981009c1f7b89884c9cba7b1a/Modules/Loadable/Models/Logic/vtkSlicerModelsLogic.cxx#L310-L312">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/f6d4eccebe92e0e981009c1f7b89884c9cba7b1a/Modules/Loadable/Models/Logic/vtkSlicerModelsLogic.cxx#L310-L312" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/f6d4eccebe92e0e981009c1f7b89884c9cba7b1a/Modules/Loadable/Models/Logic/vtkSlicerModelsLogic.cxx#L310-L312" target="_blank" rel="noopener">Slicer/Slicer/blob/f6d4eccebe92e0e981009c1f7b89884c9cba7b1a/Modules/Loadable/Models/Logic/vtkSlicerModelsLogic.cxx#L310-L312</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="310" style="counter-reset: li-counter 309 ;">
          <li>// Associate with storage node</li>
          <li>this-&gt;GetMRMLScene()-&gt;AddNode(storageNode);</li>
          <li>modelNode-&gt;SetAndObserveStorageNodeID(storageNode-&gt;GetID());</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>As a result you are getting a blank storage node instead of the one used to read the data.</p>
<p>Would you be able to make a pull request for this?</p>

---

## Post #3 by @Kening_Zhang (2023-07-12 15:49 UTC)

<p>Dear piper,<br>
I found there some differents between volume and fiber bundle<br>
Does it just need these codes?<br>
// Associate with storage node<br>
this-&gt;GetMRMLScene()-&gt;AddNode(storageNode);</p>
<p>// Set the storage node ID for the fiber bundle node<br>
fiberBundleNode-&gt;SetAndObserveStorageNodeID(storageNode-&gt;GetID());</p>
<p>Thanks,<br>
Joshua</p>

---

## Post #4 by @pieper (2023-07-12 21:11 UTC)

<p>Yes, from what I can see that is the missing code that needs to be added.  If you aren’t familiar with the process I can probably find time to add it and test that it works, but if you can give it a try it would be appreciated.</p>

---

## Post #5 by @Kening_Zhang (2023-07-13 05:19 UTC)

<p>I’m sorry I’m not familiar with this process, * I thought you might be needed to complete this step</p>

---

## Post #6 by @pieper (2023-07-13 19:23 UTC)

<p>I went ahead and added the missing line.  It will be in tomorrow’s version of SlicerDMI and it would be great if you could test it out.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerDMRI/SlicerDMRI/pull/173">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/173" target="_blank" rel="noopener">github.com/SlicerDMRI/SlicerDMRI</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/173" target="_blank" rel="noopener">BUG: add fiber storage node to the scene</a>
      </h4>

    <div class="branches">
      <code>SlicerDMRI:master</code> ← <code>SlicerDMRI:save-storage-node</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-07-13" data-time="19:22:30" data-timezone="UTC">07:22PM - 13 Jul 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 0 deletions">
          <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/173/files" target="_blank" rel="noopener">
            <span class="added">+1</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The storage node was used but not saved in the scene, making the behavior incons<span class="show-more-container"><a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/173" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">istent with corresponding method in the models superclass.

See discussion here: https://discourse.slicer.org/t/path-of-the-loaded-fiber-bundle/30524</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @Kening_Zhang (2023-07-14 08:20 UTC)

<p>Dear pieper,<br>
Thanks a lot, I will test it tomorrow.<br>
Best regards,<br>
Joshua</p>

---
