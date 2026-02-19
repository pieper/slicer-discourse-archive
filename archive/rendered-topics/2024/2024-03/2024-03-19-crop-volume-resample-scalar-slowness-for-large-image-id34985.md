---
topic_id: 34985
title: "Crop Volume Resample Scalar Slowness For Large Image"
date: 2024-03-19
url: https://discourse.slicer.org/t/34985
---

# Crop volume / resample scalar slowness for large image

**Topic ID**: 34985
**Date**: 2024-03-19
**URL**: https://discourse.slicer.org/t/crop-volume-resample-scalar-slowness-for-large-image/34985

---

## Post #1 by @muratmaga (2024-03-19 21:14 UTC)

<p>I sometimes use CropVolume to supersample some of my volumes. For large volumes (e.g., expected size after supersampling is ~20GB), resamplescalarvolume runs multithreadedly (utilizing all cores) and then there is a really long single threaded piece, sometimes taking tens of minutes for the task the finish.</p>
<p>I know the computer is not resource bound (no lack of RAM or anything)? Is it the copying of the contents to the array to the new volume?  Would it be sped up somehow?</p>

---

## Post #2 by @pieper (2024-08-04 16:38 UTC)

<p>I haven’t looked at code in a long time, I would guess this is due to the CLI communicating the volumes with compression enabled.  If someone has time to dig in, it’s probably just a simple change in a flag.</p>

---

## Post #3 by @muratmaga (2024-08-04 20:56 UTC)

<p>You mean during resampling there is data written to disk (and compressed)?</p>

---

## Post #4 by @pieper (2024-08-05 18:14 UTC)

<p>Yes, under the hood the CropVolume module uses the <code>Resample Scalar/Vector/DWI</code> CLI module and communicates via files.  The CLI management code may need to be tweaked to offer an uncompressed mode.</p>

---

## Post #5 by @muratmaga (2024-08-05 23:27 UTC)

<p>Yes, it would be good to disable the compression. <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #6 by @pieper (2024-08-06 20:43 UTC)

<p>The Slicer CLI code already disables compression when writing out volumes but then reads back whatever the CLI writes.</p>
<p>We could probably just remove this line:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ResampleScalarVectorDWIVolume/ResampleScalarVectorDWIVolume.cxx#L1299">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ResampleScalarVectorDWIVolume/ResampleScalarVectorDWIVolume.cxx#L1299" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ResampleScalarVectorDWIVolume/ResampleScalarVectorDWIVolume.cxx#L1299" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/CLI/ResampleScalarVectorDWIVolume/ResampleScalarVectorDWIVolume.cxx#L1299</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1289" style="counter-reset: li-counter 1288 ;">
          <li>  RASLPS&lt;VectorImageType&gt;( outputImage );</li>
          <li>}</li>
          <li>outputImage-&gt;SetMetaDataDictionary( dico );</li>
          <li>// Save transformed image</li>
          <li>typedef itk::ImageFileWriter&lt;VectorImageType&gt; WriterType;</li>
          <li>try</li>
          <li>{</li>
          <li>  typename WriterType::Pointer writer = WriterType::New();</li>
          <li>  writer-&gt;SetInput( outputImage );</li>
          <li>  writer-&gt;SetFileName( list.outputVolume.c_str() );</li>
          <li class="selected">  writer-&gt;UseCompressionOn();</li>
          <li>  writer-&gt;Update();</li>
          <li>}</li>
          <li>catch( itk::ExceptionObject &amp;exception )</li>
          <li>{</li>
          <li>  std::cerr &lt;&lt; exception &lt;&lt; std::endl;</li>
          <li>  return EXIT_FAILURE;</li>
          <li>}</li>
          <li>// If there was a problem while computing the transformed dwmri, exits with an error</li>
          <li>if( dwmriProblem )</li>
          <li>{</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Removing it would avoid the deflate/inflate cycle when reading back the data.  I don’t see any downsides to this except that it would use a little more disks space temporarily.</p>

---

## Post #7 by @lassoan (2024-08-12 12:30 UTC)

<p>I agree that it does not make sense to enable compression by default for CLI outputs, as they are primarily used for processing. We should from all CLIs this explicit forcing of compression, except modules that may be used for creating data for archiving, such as <code>CreateDICOMSeries</code>. Interestingly, <code>CreateDICOMSeries</code> module already has a <code>useCompression</code> parameter that can be used for enabling compression. I’ll submit a pull request.</p>

---

## Post #8 by @lassoan (2024-08-12 23:16 UTC)

<p>The pull request that disables compression for all output images in all CLI modules by default is available here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7885">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7885" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7885" target="_blank" rel="noopener">ENH: Disable compression for CLI output files</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:uncompressed-cli-output-image</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-08-12" data-time="23:15:38" data-timezone="UTC">11:15PM - 12 Aug 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 23 files with 0 additions and 23 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7885/files" target="_blank" rel="noopener">
            <span class="added">+0</span>
            <span class="removed">-23</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">CLI modules are primarily used for processing and the output file is just used f<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7885" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">or temporary storage. Therefore, usually compression has no benefits, but it slows down the execution time.

If it turns out in the future that some modules would benefit from having compressed output, those modules could get an optional "--useCompression" flag, similarly to CreateDICOMSeries module.

See discussion at https://discourse.slicer.org/t/crop-volume-resample-scalar-slowness-for-large-image/34985/6</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
