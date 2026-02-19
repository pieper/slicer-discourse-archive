---
topic_id: 23950
title: "Image Position Patient Attribute 0020 0032 In Dicom File Not"
date: 2022-06-19
url: https://discourse.slicer.org/t/23950
---

# Image Position (Patient) Attribute (0020,0032) in DICOM file not handled

**Topic ID**: 23950
**Date**: 2022-06-19
**URL**: https://discourse.slicer.org/t/image-position-patient-attribute-0020-0032-in-dicom-file-not-handled/23950

---

## Post #1 by @lcaucci78 (2022-06-19 17:58 UTC)

<p>Hello,</p>
<p>One application I am working on uses dcmtk to create a DICOM file, which I then load into Slicer, along with an STL file I have.  I want the voxel volume from the DICOM file be positioned in a specific way with respect to the triangle mesh in the STL file (think to this as positioning a SPECT-reconstructed volume with respect the mesh of a patient).  To this end, I use Image Position (Patient) Attribute (0020,0032) when I create the DICOM file.  However, Slicer seems to ignore anything I set for Image Position (Patient) Attribute, and it is always using (0, 0, 0) for that attribute.  Am I doing something wrong?</p>
<p>I am using Slicer 5.0.2 r30822/a4420c3.</p>
<p>Sincerely,<br>
Luca</p>

---

## Post #2 by @pieper (2022-06-19 18:06 UTC)

<p>Hi -</p>
<p>Be sure you are importing via the DICOM module.  Slicer is pretty careful to respect what’s in the dicom header so I suspect the alignment error is elsewhere, such as the coordinate system assumptions of the STL file.</p>
<p>If you do find any issues with coordinate system handling please report it with example (anonymized) data to reproduce.</p>
<p>Refer to this page:<br>
<a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @lcaucci78 (2022-06-22 08:17 UTC)

<p>Hello Steve,</p>
<p>Thanks for getting back to me that fast.  I took some time to go over the DICOM documentation to diligently come up with a piece of code that produces the result I want (i.e., a DICOM file with Image Position (Patient) Attribute (0020,0032) being accounted for when I load the file into Slicer).  I think I got it now!</p>
<p>I also looked a bit into Slider source code to understand what tags and sequences it expects when it is about to read (0020,0032).  I notice something that I want to bring to your attention (<a href="https://github.com/Slicer/Slicer/blob/1026bb846d29fe9099de9ec002e332168da8392a/Modules/CLI/PETStandardUptakeValueComputation/itkDCMTKFileReader.cxx#L1111" class="inline-onebox" rel="noopener nofollow ugc">Slicer/itkDCMTKFileReader.cxx at 1026bb846d29fe9099de9ec002e332168da8392a · Slicer/Slicer · GitHub</a>):</p>
<pre><code class="lang-auto">if((this-&gt;GetElementSQ(0x5200,0x9229,originSequence,false) == EXIT_SUCCESS ||
      this-&gt;GetElementSQ(0X5200,0X9239,originSequence,false) == EXIT_SUCCESS) &amp;&amp;
     originSequence.GetSequence(0,subSequence,false) == EXIT_SUCCESS &amp;&amp;
     subSequence.GetElementSQ(0x0028,0x9113,subsubSequence,false) == EXIT_SUCCESS)
    {
    subsubSequence.GetElementDS&lt;double&gt;(0x0020,0x0032,3,origin,true);
    return EXIT_SUCCESS;
    }
</code></pre>
<p>It seems to me that Slicer uses DCMTK to look for Tag (5200,9229) “Shared Functional Groups Sequence Attribute” and if it does not find it, it looks for Tag (5200,9239), which I could not find in the DICOM documentation.  I think the logical thing to do would be to look for “Per-frame Functional Groups Sequence Attribute” (5200,9230) instead.</p>
<p>I have not run any test to confirm that this is indeed a typo-induced bug.</p>
<p>Sincerely,<br>
Luca</p>

---

## Post #4 by @lassoan (2022-06-22 14:53 UTC)

<p>Good catch, indeed the file reader should use (0x5200, 0x9230) instead of (0x5200, 0x9239). It seems that itkDCMTKFileReader.cxx was copied from ITK in 2012 and all the changes since then were just to fix compilation issues.</p>
<p>It seems that we can switch to the DCMTK reader in ITK, where the correct tags are used. I’ve submitted a pull request with this change:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6446">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6446" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6446" target="_blank" rel="noopener">ENH: Remove custom itkDCMTKFileReader from PETStandardUptakeValueComputation</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:pet-suv-remove-itk-dcmtk-reader</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-06-22" data-time="14:51:00" data-timezone="UTC">02:51PM - 22 Jun 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 3 files with 0 additions and 1583 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6446/files" target="_blank" rel="noopener">
          <span class="added">+0</span>
          <span class="removed">-1583</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">itkDCMTKFileReader was added in 2012 but it seems that current itkDCMTKFileReade<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6446" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">r in ITK works just as well.
The 2012 version has a bug (it should use (0x5200, 0x9230) instead of (0x5200, 0x9239) tag - see https://discourse.slicer.org/t/image-position-patient-attribute-0020-0032-in-dicom-file-not-handled/23950/3) therefore it makes sense to switch to the ITK implementation.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
