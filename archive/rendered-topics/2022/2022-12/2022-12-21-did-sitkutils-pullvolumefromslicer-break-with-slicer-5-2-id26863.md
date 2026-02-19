---
topic_id: 26863
title: "Did Sitkutils Pullvolumefromslicer Break With Slicer 5 2"
date: 2022-12-21
url: https://discourse.slicer.org/t/26863
---

# Did sitkUtils.PullVolumeFromSlicer() break with Slicer 5.2?

**Topic ID**: 26863
**Date**: 2022-12-21
**URL**: https://discourse.slicer.org/t/did-sitkutils-pullvolumefromslicer-break-with-slicer-5-2/26863

---

## Post #1 by @Alex_Gilman (2022-12-21 00:36 UTC)

<p>Under Ubuntu 20.04, <code>sitkUtils.PullVolumeFromSlicer()</code> works fine in Slicer 5.0.3. In 5.2.1 and later, the call consistently raises an error:</p>
<pre><code class="lang-auto">  File "/bin/slicer5.2.1/Slicer-5.2.1-linux-amd64/bin/Python/sitkUtils.py", line 36, in PullVolumeFromSlicer
    sitkimage = sitk.ReadImage(myNodeFullITKAddress)
  File "/bin/slicer5.2.1/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/SimpleITK/extra.py", line 346, in ReadImage
    return reader.Execute()
  File "/slicer5.2.1/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/SimpleITK/SimpleITK.py", line 8015, in Execute
    return _SimpleITK.ImageFileReader_Execute(self)
RuntimeError: Exception thrown in SimpleITK ImageFileReader_Execute: /tmp/SimpleITK/Code/IO/src/sitkImageReaderBase.cxx:97:
sitk::ERROR: The file "slicer:0x273bf60#vtkMRMLLabelMapVolumeNode1" does not exist.
</code></pre>
<p>Is this a known issue? Does it affect other platforms? Is there a workaround?</p>

---

## Post #2 by @jamesobutler (2022-12-21 01:30 UTC)

<p>Using Slicer 5.2.1 on Windows I do not observe an error with the following code:</p>
<pre><code class="lang-auto">import SampleData
mrhead_volume = SampleData.SampleDataLogic().downloadMRHead()

import sitkUtils as su
simpleitk_image = su.PullVolumeFromSlicer(mrhead_volume)
</code></pre>
<p>There were some fixes for sitkUtils functionality made by <a class="mention" href="/u/jcfr">@jcfr</a> in <a href="https://github.com/Slicer/Slicer/pull/6606" class="inline-onebox" rel="noopener nofollow ugc">BUG: Update SimpleITK to fix test_sitkUtils by jcfr · Pull Request #6606 · Slicer/Slicer · GitHub</a> which should have found any issues across platforms.</p>
<p>Can you confirm if the code snippet above fails for you on Ubuntu 20.04? Are you using Slicer 5.2.1 downloaded from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a> or did you build it from source on your own?</p>

---

## Post #3 by @Alex_Gilman (2022-12-21 01:42 UTC)

<p>I am using the official Slicer 5.2.1 download. However, there are a number of additional packages installed into it, some of which are in-house code. Your question prompted me to try a clean download, and the problem does <strong>not</strong> reproduce. Thank you for that, I will investigate our post-installation steps to track down the cause.</p>

---

## Post #4 by @jamesobutler (2022-12-21 01:45 UTC)

<p>SimpleITK works in Slicer with a customized version. I would be suspicious if any of your additional python packages uninstalled/installed a different version of SimpleITK.</p>

---

## Post #5 by @jamesobutler (2022-12-21 01:48 UTC)

<p>Xref the following error which happened upon installing a python package that installed another version of SimpleITK rather than keeping the Slicer customized version.</p>
<aside class="quote quote-modified" data-post="9" data-topic="26457">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-5-3-preview-warnings-and-error-messages/26457/9">Slicer 5.3 Preview warnings and error messages</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    “Lungmask” segmentation throws: 
Traceback (most recent call last):
  File "C:/Users/rudol/Documents/MySlicerExtensions/SlicerLungCTAnalyzer/LungCTSegmenter/LungCTSegmenter.py", line 605, in runProcessing
    self.logic.applySegmentation()
  File "C:/Users/rudol/Documents/MySlicerExtensions/SlicerLungCTAnalyzer/LungCTSegmenter/LungCTSegmenter.py", line 1688, in applySegmentation
    inputVolumeSitk = sitkUtils.PullVolumeFromSlicer(self.inputVolume)
  File "C:\Users\rudol\AppData\Local\NA-MIC\Sli…
  </blockquote>
</aside>


---

## Post #6 by @Alex_Gilman (2022-12-21 02:01 UTC)

<p>One of our in-house dependencies specified a different version of SimpleITK, which replaced Slicer’s custom version, leading to the issue. Thank you for such prompt assistance!</p>

---

## Post #7 by @jamesobutler (2022-12-21 02:09 UTC)

<p>Can you provide us info with which package was changing the SimpleITK version? Was it choosing the a newer or older SimpleITK version?</p>
<p>This issue with updating SimpleITK is currently tracked at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6711">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6711" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6711" target="_blank" rel="noopener nofollow ugc">Slicer's embedded SimpleITK can be removed by pip</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-30" data-time="03:18:50" data-timezone="UTC">03:18AM - 30 Nov 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

When installing a package that requires a specific SimpleITK versi<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">on (e.g., TotalSegmentator requires SimpleITK==2.0.2) then installation of that package may replace Slicer's SimpleITK.

The new SimpleITK package mostly works, but the ITK IO plugins that Slicer provides (e.g., for in-memory file transfer between Slicer and ITK) don't work anymore.

## Steps to reproduce

Run `pip_install('TotalSegmentator')`.
Slicer's SimpleITK is uninstalled and SimpleITK-2.0.2 is installed.

## Expected behavior

Slicer's SimpleITK should not be uninstalled.

## Environment
- Slicer version: Slicer-5.2.1
- Operating system: Windows 11</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There is already discussion to switch Slicer to installing SimpleITK from SimpleITK’s published whl files rather than building from source. This was discussed at:</p>
<aside class="quote quote-modified" data-post="1" data-topic="25635">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/proposal-install-simpleitk-from-wheels-instead-of-building-from-source/25635">Proposal: Install SimpleITK from wheels instead of building from source</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Now that Slicer <a href="https://github.com/Slicer/Slicer/pull/6564" rel="noopener nofollow ugc">PR-6564</a> adding support for building ITK with a custom namespace has been integrated, installing SimpleITK from wheels should be possible. 
Pros: 

Reduced build time by a factor x2 (and probably more on windows)
Version of SimpleITK bundled in Slicer may be update-able using pip, this would allow to install a newer SimpleITK in a released Slicer distribution.
Reduced build-system complexity by removing external projects Swig, PCRE and SimpleITK and introducing python-SimpleITK


C…
  </blockquote>
</aside>


---

## Post #8 by @Alex_Gilman (2022-12-21 02:28 UTC)

<p>An in-house package specified <code>SimpleITK==2.1.1</code> as an install requirement. I believe that is older than the custom 2.2.0 version specified by Slicer. The issue you linked is precisely the one I am facing.</p>

---

## Post #9 by @lassoan (2022-12-21 02:50 UTC)

<p>Setting an exact version requirement for a Python package in a complex system is a really bad idea. Dependencies can be so tangled that by setting exact version requirements for a few packages can almost guarantee a failure somewhere. Usually exact version requirement are not even necessary, but it is just because developers are cutting corners (because setting an exact known version is simpler for a developer than exploring what range of versions work).</p>
<p>We ran into the same issue with TotalSegmentator and SimpleITK. If you cannot fix the problem in the package that sets the exact version requirement then you can use this technique to prevent replacement of SimpleITK:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/blob/70271651d7639bba716dcbd91dcc6e209b3fcdf1/TotalSegmentator/TotalSegmentator.py#L550-L594">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/70271651d7639bba716dcbd91dcc6e209b3fcdf1/TotalSegmentator/TotalSegmentator.py#L550-L594" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/70271651d7639bba716dcbd91dcc6e209b3fcdf1/TotalSegmentator/TotalSegmentator.py#L550-L594" target="_blank" rel="noopener">lassoan/SlicerTotalSegmentator/blob/70271651d7639bba716dcbd91dcc6e209b3fcdf1/TotalSegmentator/TotalSegmentator.py#L550-L594</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="550" style="counter-reset: li-counter 549 ;">
          <li># TotalSegmentator requires an exact SimpleITK version (2.0.2).</li>
          <li># Simply installing TotalSegmentator would uninstall Slicer's SimpleITK, which would break</li>
          <li># image IO plugins (in particular, the in-memory image transfer IO plugin).</li>
          <li>
          </li>
<li># As a workaround, TotalSegmentator installed without dependencies, then</li>
          <li># SimpleITK is removed from dependencies (from METADATA file)</li>
          <li># and then install TotalSegmentator with dependencies.</li>
          <li>
          </li>
<li>totalSegmentatorPackage = "git+https://github.com/wasserth/TotalSegmentator.git"</li>
          <li>
          </li>
<li># Install TotalSegmentator without dependencies</li>
          <li># (because we need to remove SimpleITK requirement before installing dependencies,</li>
          <li># as it would replace Slicer's SimpleITK)</li>
          <li>slicer.util.pip_install(totalSegmentatorPackage + " --no-deps" + (" --upgrade" if upgrade else ""))</li>
          <li>
          </li>
<li># Get path to site-packages\TotalSegmentator-1.4.0.dist-info\METADATA</li>
          <li>import importlib.metadata</li>
          <li>metadataPath = [p for p in importlib.metadata.files('TotalSegmentator') if 'METADATA' in str(p)][0]</li>
          <li>metadataPath.locate()</li>
          <li>
      </li>
</ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/70271651d7639bba716dcbd91dcc6e209b3fcdf1/TotalSegmentator/TotalSegmentator.py#L550-L594" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @lassoan (2023-02-07 14:00 UTC)

<p>Yet another case of a Python package requiring a very specific SimpleITK version has come up - see  <a href="https://discourse.slicer.org/t/run-a-python-script-as-subprocess-from-slicer/22668/12" class="inline-onebox">Run a Python script as subprocess from Slicer - #12 by lassoan</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> is there a solution for this? There are a number of bad-behaving Python packages out there that require a certain SimpleITK version. Should we drop the special Slicer memory image IO to make Slicer compatible with a broader range of SimpleITK versions?</p>

---
