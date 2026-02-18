# Import Numpy File in as image volume

**Topic ID**: 3653
**Date**: 2018-08-04
**URL**: https://discourse.slicer.org/t/import-numpy-file-in-as-image-volume/3653

---

## Post #1 by @stevenagl12 (2018-08-04 02:16 UTC)

<p>I have been working with trying to compress files down to NPY and NPZ files to save binary labelmaps for some of my data. Is there a way to import them into slicer? Every time I try the load data option with it, it doesn’t seem to want to load into the scene?</p>

---

## Post #2 by @lassoan (2018-08-04 09:30 UTC)

<p>NPY/NPZ file format is not widely supported outside numpy and I’m not sure if there is a standardized way of specifying essential metadata. In contrast, existing standard medical image computing file formats don’t have these issues. Since we already have more file formats than we need, it would be better not to introduce new ones. You can of course use NPY/NPZ for temporary, application-specific storage and we may consider adding readers/writers for these files if there is a standard way of using them for medical image storage.</p>

---

## Post #3 by @thewtex (2018-08-04 18:42 UTC)

<p>Instead of saving as NPY/NPZ,  it is possible to ITK to save the image in a file format supported by Slicer.</p>
<p>For example</p>
<pre><code class="lang-auto">$ python -m pip install --upgrade pip
$ python -m pip install itk
$ python
&gt;&gt;&gt; [... generate numpy array `arr`]
&gt;&gt;&gt; import itk
&gt;&gt;&gt; image = itk.GetImageFromArray(arr)
&gt;&gt;&gt; itk.imwrite(image, 'image.nrrd')
</code></pre>
<p>Hope this helps,<br>
Matt</p>

---

## Post #4 by @dzenanz (2022-11-09 15:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="3653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Since we already have more file formats than we need, it would be better not to introduce new ones.</p>
</blockquote>
</aside>
<p>Numpy authors introduced numpy format without asking us anything. And people unaware of ITK and Slicer have been saving images in .npy format for years now. It would be convenient if Slicer was able to open them.</p>
<p>Implementing <a href="https://numpy.org/devdocs/reference/generated/numpy.lib.format.html" rel="noopener nofollow ugc">npy format</a> support in C++ ITK would be a lot of work. Supporting NPY/NPZ file format via Python would be easy - use numpy to load .npy file, then convert it into an ITK image via <code>itk.GetImageFromArray(arr)</code> or <code>itk.GetImageViewFromArray(arr)</code>. I know that Slicer defers file opening to ITK. How hard would it be to add this Python loader to Slicer?</p>

---

## Post #5 by @pieper (2022-11-09 17:14 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="4" data-topic="3653">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>How hard would it be to add this Python loader to Slicer?</p>
</blockquote>
</aside>
<p>It’s very easy to add a custom reader/writer plugin to Slicer.  It’s just a hidden scripted module that registers a subclass <a href="https://github.com/pieper/SlicerDMRI/blob/nifiio/Modules/Scripted/NIfTIFile/NIfTIFile.py">something like this</a>.  Adding NPY/NPZ in a similar way would be great.</p>
<p>But we also want to support at least the direction and spacing info as metadata.  We’ve been discussing using xarray and/or zarr for these probably in <a href="https://ngff.openmicroscopy.org/latest/">ngff</a>.  I know <a class="mention" href="/u/thewtex">@thewtex</a> has been working on that and I think it is a good direction for Slicer but we haven’t gotten too serious yet.  <a href="https://gist.github.com/pieper/0e7edcf70c844925ea104e07aedbe92a">Here’s</a> and example zarr reader for ngff.</p>

---

## Post #6 by @dzenanz (2022-12-12 22:47 UTC)

<p>I just added a PR based on this discussion:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6733">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6733" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6733" target="_blank" rel="noopener nofollow ugc">Add NumpyDataLoader for reading .npy/.npz files</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>dzenanz:npyLoader</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-12" data-time="22:47:02" data-timezone="UTC">10:47PM - 12 Dec 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/dzenanz" target="_blank" rel="noopener nofollow ugc">
            <img alt="dzenanz" src="https://avatars.githubusercontent.com/u/1792121?v=4" class="onebox-avatar-inline" width="20" height="20">
            dzenanz
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 163 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6733/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+163</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As suggested in forum discussion
https://discourse.slicer.org/t/import-numpy-fi<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6733" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">le-in-as-image-volume/3653/5

Based on:
https://github.com/pieper/SlicerDMRI/blob/9565f89d16cd72618cd87f1c9046542450e4937b/Modules/Scripted/NIfTIFile/NIfTIFile.py

This works for my use case. Can you estimate how much extra effort is needed to get this merged?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
