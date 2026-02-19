---
topic_id: 35397
title: "Registrationqa Extension Not Available In Slicer V 5 6 1"
date: 2024-04-09
url: https://discourse.slicer.org/t/35397
---

# RegistrationQA extension not available in slicer v. 5.6.1

**Topic ID**: 35397
**Date**: 2024-04-09
**URL**: https://discourse.slicer.org/t/registrationqa-extension-not-available-in-slicer-v-5-6-1/35397

---

## Post #1 by @labixin (2024-04-09 15:48 UTC)

<p>Hello everyone,</p>
<p>Is RegistrationQA extension not available in “Extension manager” in the newest stable released version 5.6.1? Is it still under debugging? I remember that it existed in previous version 5.2.2.</p>
<p>If not available in “Extension manager”, how could I install this entension?</p>
<p>Thank you in advance. Your help is highly appreciated.</p>
<p>Sincerely,</p>
<p>Crayon</p>

---

## Post #2 by @jamesobutler (2024-04-09 20:24 UTC)

<aside class="onebox githubissue" data-onebox-src="https://github.com/gsi-biomotion/SlicerRegistrationQA/issues/16">
  <header class="source">

      <a href="https://github.com/gsi-biomotion/SlicerRegistrationQA/issues/16" target="_blank" rel="noopener nofollow ugc">github.com/gsi-biomotion/SlicerRegistrationQA</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/gsi-biomotion/SlicerRegistrationQA/issues/16" target="_blank" rel="noopener nofollow ugc">Update modules to use markups instead of annotations</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-09-14" data-time="19:05:10" data-timezone="UTC">07:05PM - 14 Sep 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Annotations module, which provides `vtkMRMLAnnotationROI` and `vtkMRMLAnnotation<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">Ruler` nodes have been deprecated since April 2021 and will be removed in Slicer-5.4 stable version early next year.
Since some modules in this extension use annotation nodes, these modules need to be updated to use markups nodes before the end of this year.

[This section](https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.3%3A_Removed_Annotation_module) of the migration guide should help with implementing the changes and any questions can be asked at the [Remove Annotations module topic in the Slicer forum](https://discourse.slicer.org/t/remove-annotations-module/25271).

Impacted modules:
RegistrationQA\Logic\vtkSlicerRegistrationQALogic.cxx 
RegistrationQA\SubjectHierarchyPlugins\qSlicerSubjectHierarchyRegistrationQAPlugin.cxx</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It appears the original developer created the code in the scope of their PhD and since then is unable to maintain the code to work with recent Slicer versions. <a class="mention" href="/u/lassoan">@lassoan</a> Did that developer ever give you admin access to that repo?</p>

---
