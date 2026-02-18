# How to debug python library written in C++

**Topic ID**: 29364
**Date**: 2023-05-08
**URL**: https://discourse.slicer.org/t/how-to-debug-python-library-written-in-c/29364

---

## Post #1 by @dzenanz (2023-05-08 21:13 UTC)

<p>I have a <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/pythonizationDev/ScanConvertCurvilinearArray/ScanConvertCurvilinearArray.py" rel="noopener nofollow ugc">Scripted module</a> which invokes functionality from ITKUltrasound. However, the result of this invocation is an all-zero image. Python <a href="https://github.com/KitwareMedical/ITKUltrasound/commit/86aff3587a7efbb028e2ca210e2ad46424a1b964" rel="noopener nofollow ugc">unit test</a> in ITKUltrasound itself produces non-zero output. What is the best way to debug this situation? ITK is <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/d230be0c980cc1e14e047f0d5376b714354fcf59/ITKUltrasoundCommon/ITKUltrasoundCommon.py#L92" rel="noopener nofollow ugc">pip-installed from PyPI</a>.</p>

---

## Post #2 by @lassoan (2023-05-09 01:06 UTC)

<p>You could try writing all the inputs into files and run it using the unit test. That should tell if the problem is in how your module prepares the input data or reads the output data; or the problem is in the Python package. If you have the answer for this then I can further ideas for next steps.</p>

---

## Post #3 by @dzenanz (2023-05-09 12:54 UTC)

<p>Slicer <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/d230be0c980cc1e14e047f0d5376b714354fcf59/ScanConvertCurvilinearArray/ScanConvertCurvilinearArray.py#L485-L486" rel="noopener nofollow ugc">unit test</a> is equivalent to ITKUltrasound <a href="https://github.com/KitwareMedical/ITKUltrasound/blob/86aff3587a7efbb028e2ca210e2ad46424a1b964/wrapping/test/CMakeLists.txt#L47-L59" rel="noopener nofollow ugc">unit test</a> with regard to input image and parameters. And the image is <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/d230be0c980cc1e14e047f0d5376b714354fcf59/ScanConvertCurvilinearArray/ScanConvertCurvilinearArray.py#L342" rel="noopener nofollow ugc">non-zero</a> just before passing it into the function.</p>

---

## Post #4 by @pieper (2023-05-09 13:30 UTC)

<p>I’d try breaking this down to the simplest operations that you know should be working, like passing an image back and forth unchanged, then adding a small filter, and ultimately getting back to the full pipeline.  I don’t think using the pypi ITK has gotten a lot of testing in Slicer.</p>

---

## Post #5 by @dzenanz (2023-05-09 13:49 UTC)

<p>I am the first kitten for testing ITK from PyPI <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<p>I have another <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/d230be0c980cc1e14e047f0d5376b714354fcf59/BModeFromRF/BModeFromRF.py#L281-L290" rel="noopener nofollow ugc">module which works</a>, so at least one filter works correctly.</p>

---

## Post #6 by @dzenanz (2023-05-09 17:09 UTC)

<p>Running this from test script from within Slicer produces expected result:</p>
<pre><code class="lang-auto">import math
import itk

itk.auto_progress(2)

pixel_type = itk.UC
dimension = 3
image_type = itk.CurvilinearArraySpecialCoordinatesImage[pixel_type, dimension]
reader = itk.ImageFileReader[image_type].New()
reader.SetFileName(r"C:\Dev\SlicerITKUltrasound\ScanConvertCurvilinearArray\Data\ScanConvertCurvilinearArrayTestInput.mha")
reader.Update()
image = reader.GetOutput()
image.DisconnectPipeline()

image.SetLateralAngularSeparation(0.00862832)
image.SetFirstSampleDistance(26.4)
image.SetRadiusSampleSize(0.0513434)

output_size = [800, 800, 1]
output_spacing = [0.15] * dimension
output_origin = [output_size[0] * output_spacing[0] / -2.0, 26.4 * math.cos(math.pi / 4.0), 0.0]

result = itk.resample_image_filter(image, size=output_size, output_spacing=output_spacing, output_origin=output_origin)
itk.imwrite(result, r"C:\Dev\SlicerITKUltrasound\ScanConvertCurvilinearArray\Data\Output.mha")
</code></pre>
<p>This confirms that ITK within Slicer works. This at least narrows the problem down to how parameters are passed.</p>

---

## Post #7 by @dzenanz (2023-05-09 17:52 UTC)

<p>After more debugging, I discovered that I forgot to call <code>inputImage.SetRegions(itkImage.GetLargestPossibleRegion())</code>, which should go just before <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/d230be0c980cc1e14e047f0d5376b714354fcf59/ScanConvertCurvilinearArray/ScanConvertCurvilinearArray.py#L387" rel="noopener nofollow ugc"><code>inputImage.SetPixelContainer(itkImage.GetPixelContainer())</code></a>.</p>

---

## Post #8 by @lassoan (2023-05-10 03:19 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> Could you implement utility functions for passing images between ITK and Slicer that we could put into <code>slicer.util</code>? If there is a way to do it without writing to file (e.g., via numpy arrays) then it is nice. But the utility functions would help even if we used files, as it would make things easier for users, we could ensure that optimal settings are used (we could automatically generate a filename, use a problem-free file format, turn off compression, etc.), and later we could further optimize things with in-memory transfer.</p>
<p>We have an example in the Slicer script repository for using SimpleITK in Slicer. If we have the utility functions then we could add one or few examples for ITKPython filters, too. You can <a href="https://github.com/Slicer/Slicer/blob/main/Docs/developer_guide/script_repository/volumes.md#running-an-itk-filter-in-python-using-simpleitk">edit this page</a> directly and send a pull request with the suggested changes.</p>

---

## Post #9 by @dzenanz (2023-05-10 14:19 UTC)

<p>I think that <code>getITKImageFromVolumeNode</code> and <code>setITKImageToVolumeNode</code> are ready for migration to <code>slicer.util</code>. Perhaps along with a rename, and a bit of parameter documentation. You might see some opportunity for refactoring, too. They already use in-memory transfer. I don’t remember any more whether the pixel array is copied or just referenced. They can be taken from here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/29a07dfc7714431182151b784356a0ab15afe59f/ITKUltrasoundCommon/ITKUltrasoundCommon.py#L98-L204">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/29a07dfc7714431182151b784356a0ab15afe59f/ITKUltrasoundCommon/ITKUltrasoundCommon.py#L98-L204" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/29a07dfc7714431182151b784356a0ab15afe59f/ITKUltrasoundCommon/ITKUltrasoundCommon.py#L98-L204" target="_blank" rel="noopener nofollow ugc">KitwareMedical/SlicerITKUltrasound/blob/29a07dfc7714431182151b784356a0ab15afe59f/ITKUltrasoundCommon/ITKUltrasoundCommon.py#L98-L204</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="98" style="counter-reset: li-counter 97 ;">
          <li># Adapted from TorchIO</li>
          <li># https://github.com/fepegar/torchio/blob/4c1b3d83a7962699a15afe76ae6f39db1aae7a99/src/torchio/data/io.py#L278-L285</li>
          <li>def get_rotation_and_spacing_from_affine(</li>
          <li>    self,</li>
          <li>    affine: np.ndarray,</li>
          <li>) -&gt; Tuple[np.ndarray, np.ndarray]:</li>
          <li>    # From https://github.com/nipy/nibabel/blob/master/nibabel/orientations.py</li>
          <li>    rotation_zoom = affine[:3, :3]</li>
          <li>    spacing = np.sqrt(np.sum(rotation_zoom * rotation_zoom, axis=0))</li>
          <li>    rotation = rotation_zoom / spacing</li>
          <li>    return rotation, spacing</li>
          <li>
          </li>
<li># Adapted from TorchIO</li>
          <li># https://github.com/fepegar/torchio/blob/4c1b3d83a7962699a15afe76ae6f39db1aae7a99/src/torchio/data/io.py#L384-L412</li>
          <li>def get_itk_metadata_from_ras_affine(</li>
          <li>    self,</li>
          <li>    affine: np.ndarray,</li>
          <li>    is_2d: bool=False,</li>
          <li>    lps: bool = True,</li>
          <li>) -&gt; Tuple[Any, Any, Any]:</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/29a07dfc7714431182151b784356a0ab15afe59f/ITKUltrasoundCommon/ITKUltrasoundCommon.py#L98-L204" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
The usage examples can be inspired by:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/29a07dfc7714431182151b784356a0ab15afe59f/BModeFromRF/BModeFromRF.py#L279-L290">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/29a07dfc7714431182151b784356a0ab15afe59f/BModeFromRF/BModeFromRF.py#L279-L290" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/29a07dfc7714431182151b784356a0ab15afe59f/BModeFromRF/BModeFromRF.py#L279-L290" target="_blank" rel="noopener nofollow ugc">KitwareMedical/SlicerITKUltrasound/blob/29a07dfc7714431182151b784356a0ab15afe59f/BModeFromRF/BModeFromRF.py#L279-L290</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="279" style="counter-reset: li-counter 278 ;">
          <li>itkImage = self.getITKImageFromVolumeNode(inputVolume)</li>
          <li>floatImage = itkImage.astype(itk.F)</li>
          <li>bmode_filter = itk.BModeImageFilter.New(floatImage, Direction=axisOfPropagation)</li>
          <li>
          </li>
<li>logging.info('Processing started')</li>
          <li>startTime = time.time()</li>
          <li>bmode_filter.Update()</li>
          <li>result = bmode_filter.GetOutput()</li>
          <li>stopTime = time.time()</li>
          <li>logging.info(f'Processing completed in {stopTime-startTime:.2f} seconds')</li>
          <li>
          </li>
<li>self.setITKImageToVolumeNode(result, outputVolume)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @dzenanz (2023-07-12 17:14 UTC)

<p>Could we get this into <code>slicer.util</code> before cutting the next release? When is the timeline for that? I am on vacation 17th-28th. I added a few more modules which use these functions, see <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/tree/pythonization" rel="noopener nofollow ugc">pythonization branch</a>.</p>

---

## Post #11 by @dzenanz (2023-07-14 18:28 UTC)

<p>I just created a PR to do this:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7094">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7094" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7094" target="_blank" rel="noopener nofollow ugc">Add Python utility functions: ITK image &lt;-&gt; volume node</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>dzenanz:itkVolumeUtil</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-07-14" data-time="18:27:48" data-timezone="UTC">06:27PM - 14 Jul 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/dzenanz" target="_blank" rel="noopener nofollow ugc">
            <img alt="dzenanz" src="https://avatars.githubusercontent.com/u/1792121?v=4" class="onebox-avatar-inline" width="20" height="20">
            dzenanz
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 112 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7094/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+112</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This was adapted from SlicerITKUltrasound extension at 6d7ea98bc329fc52e9c9bfddc<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7094" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">cc807cf76806fc2. Direct link: https://github.com/KitwareMedical/SlicerITKUltrasound/blob/6d7ea98bc329fc52e9c9bfddccc807cf76806fc2/ITKUltrasoundCommon/ITKUltrasoundCommon.py#L98-L204</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
