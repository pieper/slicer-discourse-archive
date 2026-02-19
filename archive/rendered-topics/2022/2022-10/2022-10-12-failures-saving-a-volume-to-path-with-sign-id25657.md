---
topic_id: 25657
title: "Failures Saving A Volume To Path With Sign"
date: 2022-10-12
url: https://discourse.slicer.org/t/25657
---

# Failures saving a volume to path with % sign

**Topic ID**: 25657
**Date**: 2022-10-12
**URL**: https://discourse.slicer.org/t/failures-saving-a-volume-to-path-with-sign/25657

---

## Post #1 by @jamesobutler (2022-10-12 18:55 UTC)

<p>I’m observing an issue with some file I/O when reading/writing metaimage mhd+raw data in a filepath location that contains a character such as “%”.  I have seen users utilize this character for a directory name when describing a volume such as the concentration of a drug. This “%” character is also a valid character in the Windows file system.</p>
<p>Below is a python code snippet to observe the issue which can also be triggered when defining an output filepath for a metaimage using the Slicer Save dialog.  You will see below that the output reports that the .mhd is written, but the corresponding raw file is not present. When writing the split file format for nrrd (nhdr+raw) is successful writing out both files.</p>
<p>The saving of the volume is successful with the single file format of .mha.</p>
<pre><code class="lang-python">import os
import SampleData

volume_node = SampleData.SampleDataLogic().downloadMRHead()

output_filepath = os.path.join(os.getenv("USERPROFILE"), "Downloads", "2%concentration", "MyVolume.mhd")
slicer.util.saveNode(volume_node, output_filepath)
print(f"{output_filepath} exists?: {os.path.exists(output_filepath)}")
raw_filepath = os.path.splitext(output_filepath)[0] + '.raw'
print(f"{raw_filepath} exists?: {os.path.exists(raw_filepath)}")

output_filepath = os.path.join(os.getenv("USERPROFILE"), "Downloads", "2%concentration", "MyVolume.nhdr")
slicer.util.saveNode(volume_node, output_filepath)
print(f"{output_filepath} exists?: {os.path.exists(output_filepath)}")
raw_filepath = os.path.splitext(output_filepath)[0] + '.raw.gz'
print(f"{raw_filepath} exists?: {os.path.exists(raw_filepath)}")
</code></pre>
<p>Is there a workaround to support saving the split file format for metaimage to a filepath with a “%” character? Or does something need to be done to update to a newer version of the metaimage I/O library which might contain a bug fix?</p>

---

## Post #2 by @jamesobutler (2022-10-12 19:01 UTC)

<p>It appears MetaIO has an issue written up for this and a PR trying to close it. <a class="mention" href="/u/dzenanz">@dzenanz</a> Do you know who might be able to help move this along?</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Kitware/MetaIO/issues/68">
  <header class="source">

      <a href="https://github.com/Kitware/MetaIO/issues/68" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/MetaIO</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/MetaIO/issues/68" target="_blank" rel="noopener nofollow ugc">Assumed string encoding for .mhd differs on platforms</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-01-10" data-time="15:25:22" data-timezone="UTC">03:25PM - 10 Jan 19 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/codeling" target="_blank" rel="noopener nofollow ugc">
          <img alt="codeling" src="https://avatars.githubusercontent.com/u/1629217?v=4" class="onebox-avatar-inline" width="20" height="20">
          codeling
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Looking at the .mhd documentation, I see no explicit mention of any assumed enco<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ding (or a setting for it).

Yet when ElementDataFile points to a filename containing special characters, the character encoding is highly relevant for MetaIO to find the actual file. In my experiments (utilizing the MetaIO included in ITK), on Windows, an encoding of cp1252 is assumed, while on Linux, an encoding of utf-8 is expected. This means that when the filename given under ElementDataFile contains special characters, a separate .mhd file is required for Linux and Windows (and potentially more for other platforms I have not tested). What is thus required to make this consistent (and .mhd files with special characters transferrable between platforms), in my opinion, is to implement one of two options:

1. That .mhd files are required to have a specific encoding (utf-8 seems to  be the logic choice), or
2. To have a separate entry specifying the encoding of the .mhd file

Or am I missing something here, is there an encoding specification somewhere already?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Kitware/MetaIO/pull/113">
  <header class="source">

      <a href="https://github.com/Kitware/MetaIO/pull/113" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/MetaIO</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Kitware/MetaIO/pull/113" target="_blank" rel="noopener nofollow ugc">Make ElementDataFileName always use UTF-8 encoding</a>
      </h4>

    <div class="branches">
      <code>Kitware:master</code> ← <code>codeling:master</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-08-10" data-time="12:34:31" data-timezone="UTC">12:34PM - 10 Aug 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/codeling" target="_blank" rel="noopener nofollow ugc">
            <img alt="codeling" src="https://avatars.githubusercontent.com/u/1629217?v=4" class="onebox-avatar-inline" width="20" height="20">
            codeling
          </a>
        </div>

        <div class="lines" title="2 commits changed 3 files with 82 additions and 6 deletions">
          <a href="https://github.com/Kitware/MetaIO/pull/113/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+82</span>
            <span class="removed">-6</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Attempt to fix https://github.com/Kitware/MetaIO/issues/68.

Limitations:
- O<span class="show-more-container"><a href="https://github.com/Kitware/MetaIO/pull/113" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">nly handles the `ElementDataFileName` field in datasets of type metaImage; I have seen the same field being used in e.g. metaArray and metaFEMObject as well, but I cannot test these at the moment; as for other MET_STRING fields, I have no idea if any might need such handling as well, and if so what consequences this might have, therefore I didn't touch them.
- Not sure if all possible cases are handled correctly; I only have limited ability to test, and I don't know all possibilites of how the code is used from VTK/ITK. There is for example a logic of determining the ElementDataFileName from the FileName in the ::Write method, which I don't fully get; or rather I don't get why it intermittently sets the ElementDataFileName to the full data file path, and only later cuts away the path again; because this makes it a bit tricky to handle if the path itself also contains special characters - one should not encode the full path immediately in utf-8, since later, the path is extracted again from the ElementDataFileName, and a comparisons to the non-utf-8 encoded version of the file path is done....
- The file name itself still has to be specified in local encoding (on Windows).
-  I considered adding a test case to testMeta3Image.cxx, but couldn't figure out how to set the file name properly, as source files are by default stored in utf-8 (but we would need to provide an ANSI filename on Windows)

Maybe a solution using vtksys iostreams (https://gitlab.kitware.com/paraview/paraview/-/merge_requests/3850) would be preferrable? Though this would probably break backwards-compatibility, since all file names would then be expected to be in UTF-8 format I guess?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @dzenanz (2022-10-12 21:50 UTC)

<p>Brad King (no profile on this forum) and <a class="mention" href="/u/jcfr">@jcfr</a>. They both commented on <a href="https://github.com/Kitware/MetaIO/issues/68" rel="noopener nofollow ugc">MetaIO#68</a>.</p>

---

## Post #4 by @todoooo (2022-10-13 13:00 UTC)

<p>Since % is not an extended character, I don’t see how the referenced MRs in MetaIO are relevant here.</p>
<p>Are you using a non-US keyboard? It is not clear to me what your Python code is demonstrating.</p>

---

## Post #5 by @jamesobutler (2022-10-13 16:39 UTC)

<p><a class="mention" href="/u/todoooo">@todoooo</a> I am using a regular US keyboard.</p>
<p>It appears relevant to the MetaIO issues because the ElementDataFile points to a filename with a special character (%) where the target filename is like the following:</p>
<p>“C:\Users\butlej30383\Downloads\2%concentration\MyVolume.mhd”</p>
<p>What my python code snippet is showing is that when saving the volume to this path, MetaIO only writes MyVolume.mhd, but does not write the corresponding MyVolume.raw (or MyVolume.zraw). <code>MetaImage: M_WriteElementsData: file stream is fail after write</code></p>
<p>Things save correctly if I save with the single file format<br>
“C:\Users\butlej30383\Downloads\2%concentration\MyVolume.mha”</p>
<p>The issue is when the separate ElementDataFile (.raw/.zraw) is to be a filepath that contains a special character such as %.</p>
<p>However when using the NRRD format, writing a MyVolume.nhdr is successful as it also writes the corresponding MyVolume.raw.gz. So NRRD is doing a better job handling this situation.</p>

---

## Post #6 by @lassoan (2022-10-13 17:04 UTC)

<p>MetaIO supports <a href="https://itk.org/Wiki/ITK/MetaIO/Documentation#Reading_DICOM_and_Other_One-Slice-Per-File_Data_Formats">One-Slice-Per-File Data Formats</a> and it uses the <code>%</code> character to specify the slice number in the filename format string.</p>
<p>Due to the special meaning of the <code>%</code> character, currently <a href="https://github.com/Kitware/MetaIO/blob/0b8c5284f3fe126968fd66c24639fd70b88e8788/src/metaImage.cxx#L1533">MetaIO does not allow using this chracter in the path</a>. This limitation should either be clearly documented or the implementation should be made more sophisticated (to somehow differentiate the <code>%</code> that refers to per-slice filename generation from simple <code>%</code> occurrences in the path; or by allowing completely disabling this extremely rarely used one-slice-per-file feature).</p>

---

## Post #7 by @todoooo (2022-10-14 00:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="25657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>MetaIO supports <a href="https://itk.org/Wiki/ITK/MetaIO/Documentation#Reading_DICOM_and_Other_One-Slice-Per-File_Data_Formats" rel="noopener nofollow ugc">One-Slice-Per-File Data Formats </a> and it uses the <code>%</code> character to specify the slice number in the filename format string.</p>
</blockquote>
</aside>
<p>It seems then that % in the filename should be treated with special meaning whereas % in the path name should be ignored.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="25657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>It appears relevant to the MetaIO issues because the ElementDataFile points to a filename with a special character (%) where the target filename is like the following:</p>
<p>“C:\Users\butlej30383\Downloads\2%concentration\MyVolume.mhd”</p>
</blockquote>
</aside>
<p>As far as utf-8 encoding is concerned % is not a special character.</p>

---

## Post #8 by @jamesobutler (2022-10-17 14:24 UTC)

<p>I’ve created the following issue to keep track of this problem:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Kitware/MetaIO/issues/114">
  <header class="source">

      <a href="https://github.com/Kitware/MetaIO/issues/114" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/MetaIO</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/MetaIO/issues/114" target="_blank" rel="noopener nofollow ugc">Unable to save data file to output filepath that contains a % character</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-10-17" data-time="14:24:20" data-timezone="UTC">02:24PM - 17 Oct 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As originally posted about in https://discourse.slicer.org/t/failures-saving-a-v<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">olume-to-path-with-sign/25657 and more specifically in 
https://discourse.slicer.org/t/failures-saving-a-volume-to-path-with-sign/25657/6 thanks to @lassoan:

&gt; MetaIO supports [One-Slice-Per-File Data Formats 1](https://itk.org/Wiki/ITK/MetaIO/Documentation#Reading_DICOM_and_Other_One-Slice-Per-File_Data_Formats) and it uses the % character to specify the slice number in the filename format string.
&gt; 
&gt; Due to the special meaning of the % character, currently [MetaIO does not allow using this chracter in the path](https://github.com/Kitware/MetaIO/blob/0b8c5284f3fe126968fd66c24639fd70b88e8788/src/metaImage.cxx#L1533). This limitation should either be clearly documented or the implementation should be made more sophisticated (to somehow differentiate the % that refers to per-slice filename generation from simple % occurrences in the path; or by allowing completely disabling this extremely rarely used one-slice-per-file feature).

As such, % used in the basename could possibly still be treated with the special meaning for the filename format string for One-Slice-Per-File functionality however, % used elsewhere in the filepath should be supported. Last resort would be to document this limitation.

The below code uses 3D Slicer to show that the mhd file is written for a volume output filepath that contains a "%", but the corresponding data file (.zraw) is not written.
```python
import os
import SampleData

volume_node = SampleData.SampleDataLogic().downloadMRHead()

output_filepath = os.path.join(os.getenv("USERPROFILE"), "Downloads", "2%concentration", "MyVolume.mhd")
slicer.util.saveNode(volume_node, output_filepath)
print(f"{output_filepath} exists?: {os.path.exists(output_filepath)}")
raw_filepath = os.path.splitext(output_filepath)[0] + '.zraw'  # default Slicer saves it compressed hence zraw and not raw
print(f"{raw_filepath} exists?: {os.path.exists(raw_filepath)}")
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
