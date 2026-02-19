---
topic_id: 15115
title: "Updating Only Header Information For Metaimage Nrrd"
date: 2020-12-17
url: https://discourse.slicer.org/t/15115
---

# Updating only header information for MetaImage/NRRD

**Topic ID**: 15115
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/updating-only-header-information-for-metaimage-nrrd/15115

---

## Post #1 by @jamesobutler (2020-12-17 15:06 UTC)

<p>I’m using MetaImage and NRRD file types with custom header fields to store additional information about my volume. I am currently interested in updating the values of these custom fields, but I have only had success with writing the updated header field which also rewrites the image data.</p>
<p>I’ve currently been using SimpleITK to update the fields as I was unable to find an option in Slicer to save the custom fields.</p>
<pre><code class="lang-python">import SimpleITK as sitk
image = sitk.ReadImage("path/to/image.mhd")
image.SetMetaData("MyCustomField", "MyCustomValue")
writer = sitk.ImageFileWriter()
writer.SetFileName("same/path/to/image.mhd")
writer.Execute(image)  # also writes out the image raw file
</code></pre>
<p>I understand that likely only updating the header is possible when using split file formats like mhd+raw or nhdr+raw. Or is there a method with MHA and NRRD that can update the header fields and shift the bits so not to write the image data again?</p>
<p>Does anyone know of a method of only updating a field for the header file without the obvious opening of the file manually and writing it as simple text.</p>

---

## Post #2 by @lassoan (2020-12-17 15:18 UTC)

<p>I don’t know any file IO API that would support shift operation. A common technique to work around this limitation is to write a placeholder field with the maximum allowed length (e.g., some value with lots of padding spaces) and overwrite that field when the final length is known. Maybe the segmentation storage file format discussion today at 11am EST would be interesting for you.</p>

---

## Post #3 by @jamesobutler (2020-12-17 15:21 UTC)

<p>Being that these images are captured using <a href="https://plustoolkit.github.io/" rel="noopener nofollow ugc">PlusToolkit</a> I have also tried the <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationEditSequenceFile.html" rel="noopener nofollow ugc">EditSequenceFile</a> command line tool for updating the custom header field however it also writes the image data file (RAW) or at least I notice that the image data file has a new “Date Modified” time which makes me think it has been written down again.</p>
<pre><code class="lang-auto">EditSequenceFile.exe
--source-seq-file="C:\Users\JamesButler\Documents\FusedVolume.mhd"
--output-seq-file="C:\Users\JamesButler\Documents\FusedVolume.mhd"
--operation=UPDATE_FIELD_VALUE --field-name=MyCustomHeaderFieldn --updated-field-value=MyCustomValue
--maintain-custom-headers MyCustomHeaderField
</code></pre>
<p>Maybe all these methods SimpleITK/EditSequenceFile all depend on the same ITK writer which doesn’t currently support writing just the header file?</p>

---

## Post #4 by @lassoan (2020-12-17 15:43 UTC)

<p>We had to reimplement sequence file writers to allow streamed compressed writing, so we don’t rely on what ITK writer can do (for mha for sure, but I think for nrrd as well). If it currently rewrites the RAW file then it should not be hard to fix it.</p>

---

## Post #5 by @dzenanz (2020-12-17 20:14 UTC)

<p>Those custom implementations are in <a href="https://github.com/IGSIO/IGSIO/tree/73faef0140106e9abf7cb5fc9f0832c197a8c207/Source/SequenceIO" rel="noopener nofollow ugc">IGSIO</a> now.</p>

---

## Post #6 by @dzenanz (2020-12-24 16:42 UTC)

<p>Updates created:</p><aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/IGSIO/IGSIO/pull/21" target="_blank" rel="noopener nofollow ugc">github.com/IGSIO/IGSIO</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/IGSIO/IGSIO/pull/21" target="_blank" rel="noopener nofollow ugc">ENH: add support for not writing pixel data</a>
    </h4>

    <div class="branches">
      <code>IGSIO:master</code> ← <code>dzenanz:updateHeader</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-12-24" data-time="16:40:43" data-timezone="UTC">04:40PM - 24 Dec 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/dzenanz" target="_blank" rel="noopener nofollow ugc">
          <img alt="dzenanz" src="https://avatars3.githubusercontent.com/u/1792121?v=4" class="onebox-avatar-inline" width="20" height="20">
          dzenanz
        </a>
      </div>

      <div class="lines" title="1 commits changed 8 files with 146 additions and 111 deletions">
        <a href="https://github.com/IGSIO/IGSIO/pull/21/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+146</span>
          <span class="removed">-111</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/PlusToolkit/PlusLib/pull/753" target="_blank" rel="noopener nofollow ugc">github.com/PlusToolkit/PlusLib</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/PlusToolkit/PlusLib/pull/753" target="_blank" rel="noopener nofollow ugc">ENH: writing data file can be skipped in some circumstances</a>
    </h4>

    <div class="branches">
      <code>PlusToolkit:master</code> ← <code>dzenanz:editHeader</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-12-24" data-time="16:41:31" data-timezone="UTC">04:41PM - 24 Dec 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/dzenanz" target="_blank" rel="noopener nofollow ugc">
          <img alt="dzenanz" src="https://avatars3.githubusercontent.com/u/1792121?v=4" class="onebox-avatar-inline" width="20" height="20">
          dzenanz
        </a>
      </div>

      <div class="lines" title="1 commits changed 3 files with 21 additions and 7 deletions">
        <a href="https://github.com/PlusToolkit/PlusLib/pull/753/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+21</span>
          <span class="removed">-7</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<p>
and a related bug identified:</p><aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/IGSIO/IGSIO/issues/20" target="_blank" rel="noopener nofollow ugc">github.com/IGSIO/IGSIO</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/IGSIO/IGSIO/issues/20" target="_blank" rel="noopener nofollow ugc">NRRD Sequence IO produces invalid files when custom header fields are present</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-12-24" data-time="16:35:07" data-timezone="UTC">04:35PM - 24 Dec 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/dzenanz" target="_blank" rel="noopener nofollow ugc">
          <img alt="dzenanz" src="https://avatars3.githubusercontent.com/u/1792121?v=4" class="onebox-avatar-inline" width="20" height="20">
          dzenanz
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Custom header fields need := separator, while standard fields use : . Current source ignores this distinction. Reading then writing file...</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
