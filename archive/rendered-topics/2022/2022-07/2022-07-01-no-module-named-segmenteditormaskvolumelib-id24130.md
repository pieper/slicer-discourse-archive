# No module named 'SegmentEditorMaskVolumeLib'

**Topic ID**: 24130
**Date**: 2022-07-01
**URL**: https://discourse.slicer.org/t/no-module-named-segmenteditormaskvolumelib/24130

---

## Post #1 by @jmhuie (2022-07-01 06:04 UTC)

<p>Until recently, my extension <a href="https://github.com/jmhuie/Slicer-SegmentGeometry" rel="noopener nofollow ugc">SegmentGeometry</a> imported the SegmentEditorMaskVolumeLib from the SegmentEditor with no problem. However, I recently updated Slicer on my computer along with the extensions and now it no longer works. When I try to execute the SegmentGeometry module, I get an error that says ‘No module named ‘SegmentEditorMaskVolumeLib’’. Was this module deprecated recently? Any help would be appreciated.</p>
<p>Thanks</p>

---

## Post #2 by @jamesobutler (2022-07-01 10:46 UTC)

<p>Is your SegmentGeometry extension still expecting that the MaskVolume effect is in the experimental set of effects of the SegmentEditorExtraEffects extension? As of January 30th, 2021 the MaskVolume effect was <a href="https://github.com/Slicer/Slicer/commit/12f40a20e73bc2703fdafc710603a9e4a5dc0766" rel="noopener nofollow ugc">moved into Slicer core</a> code after it was determined to be mature enough. That specific import you mentioned is a type of import for the SegmentEditorExtraEffects extension which is outdated since MaskVolume is in Slicer core.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/4ebd40cdd1f222ac2dc08d3a75720da7cdf46ae6/SegmentGeometry.s4ext#L15">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/4ebd40cdd1f222ac2dc08d3a75720da7cdf46ae6/SegmentGeometry.s4ext#L15" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/4ebd40cdd1f222ac2dc08d3a75720da7cdf46ae6/SegmentGeometry.s4ext#L15" target="_blank" rel="noopener nofollow ugc">Slicer/ExtensionsIndex/blob/4ebd40cdd1f222ac2dc08d3a75720da7cdf46ae6/SegmentGeometry.s4ext#L15</a></h4>



    <pre class="onebox"><code class="lang-s4ext">
      <ol class="start lines" start="5" style="counter-reset: li-counter 4 ;">
          <li>#</li>
          <li>
          </li>
<li># This is source code manager (i.e. svn)</li>
          <li>scm git</li>
          <li>scmurl https://github.com/jmhuie/Slicer-SegmentGeometry.git</li>
          <li>scmrevision main  </li>
          <li>
          </li>
<li># list dependencies</li>
          <li># - These should be names of other modules that have .s4ext files</li>
          <li># - The dependencies will be built first</li>
          <li class="selected">depends     SegmentEditorExtraEffects</li>
          <li>
          </li>
<li># Inner build directory (default is .)</li>
          <li>build_subdirectory .</li>
          <li>
          </li>
<li># homepage</li>
          <li>homepage    https://github.com/jmhuie/Slicer-SegmentGeometry</li>
          <li>
          </li>
<li># Firstname1 Lastname1 ([SubOrg1, ]Org1), Firstname2 Lastname2 ([SubOrg2, ]Org2)</li>
          <li># For example: Jane Roe (Superware), John Doe (Lab1, Nowhere), Joe Bloggs (Noware)</li>
          <li>contributors Jonathan Huie (George Washington University)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jmhuie (2022-07-01 14:04 UTC)

<p>Ah yes, looks like it had to do with that but the problem didn’t become apparent until Slicer 5.0.2. Anyhow, I managed to make the quick fix by importing “SegmentEditorEffects” instead of “SegmentEditorMaskVolumeLib”. Thanks for your help!</p>

---

## Post #4 by @jamesobutler (2022-07-01 14:41 UTC)

<p>The SegmentEditorExtraEffects extension still included MaskVolume up until recently in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/commit/afb7e22630ae2d36405f57305eb0a9da84e0e457" class="inline-onebox" rel="noopener nofollow ugc">Remove Slicer4 support · lassoan/SlicerSegmentEditorExtraEffects@afb7e22 · GitHub</a> for backwards compatibility of older versions that did not have it in Slicer core. This is why it had still worked for you.</p>

---
