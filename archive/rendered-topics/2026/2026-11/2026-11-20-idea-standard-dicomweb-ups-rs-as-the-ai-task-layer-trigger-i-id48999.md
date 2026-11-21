---
topic_id: 48999
title: "Idea - standard DICOMweb UPS-RS as the AI-task layer (trigger inference + read results in Slicer)"
date: 2026-11-20
url: https://discourse.slicer.org/t/48999
last_bumped: 2026-11-20T13:54:37.837Z
---

# Idea - standard DICOMweb UPS-RS as the AI-task layer (trigger inference + read results in Slicer)

**Topic ID**: 48999
**Date**: 2026-11-20
**URL**: https://discourse.slicer.org/t/idea-standard-dicomweb-ups-rs-as-the-ai-task-layer-trigger-inference-read-results-in-slicer/48999

---

## Post #1 by @clicker71 (2026-11-20 13:54 UTC)

<p>Hi everyone,<br>
I keep seeing excellent AI integrations land in Slicer as one-off extensions -<br>
the torchvulkan / GPU TotalSegmentator thread, MONAI-Label, per-model<br>
segmentation extensions. Each of them re-solves the same plumbing: run a model,<br>
get a result, show it in the scene. I would like to propose using the standard<br>
that already exists for exactly this plumbing - DICOMweb UPS-RS (PS3.18 section 11).<br>
The loop:<br>
1. The user selects data in Slicer and triggers a task.<br>
2. Slicer, as the Task Requester, creates a UPS workitem on the DICOMweb origin  (POST /workitems), naming the study/series as the input.<br>
3. Any Task Performer - TotalSegmentator, MONAI, NVIDIA, clinfer, whatever -<br>
claims the workitem (Change State to IN PROGRESS), runs, writes its result<br>
back as DICOM SEG / SR / PR via STOW-RS, and marks it COMPLETED.<br>
4. Slicer subscribes (PS3.18 11.10/11.11, N-EVENT-REPORT over the event channel), sees COMPLETED, and loads the result over WADO-RS into the scene.<br>
No vendor-specific glue anywhere: the workitem is the contract. The same<br>
performer works from Weasis, from OHIF, from Slicer, unchanged.<br>
This is not hypothetical. The full loop already runs end-to-end against an open<br>
DICOMweb origin (Clarus) with an open performer (clinfer), driven from the<br>
Weasis viewer - screenshots in this Weasis PR comment:</p><aside class="onebox githubpullrequest github-onebox" data-onebox-src="https://github.com/nroduit/Weasis/pull/950#issuecomment-6219616602">
    <header class="source github-onebox__header">
  <span class="github-onebox__label" role="img" aria-label="Comment" title="Comment">
    <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path></svg>
    <span>Comment</span>
  </span>
    <a class="github-onebox__repo" href="https://github.com/nroduit/Weasis/pull/950#issuecomment-6219616602" target="_blank" rel="noopener nofollow ugc">
      <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6.766 11.328c-2.063-.25-3.516-1.734-3.516-3.656 0-.781.281-1.625.75-2.188-.203-.515-.172-1.609.063-2.062.625-.078 1.468.25 1.968.703.594-.187 1.219-.281 1.985-.281.765 0 1.39.094 1.953.265.484-.437 1.344-.765 1.969-.687.218.422.25 1.515.046 2.047.5.593.766 1.39.766 2.203 0 1.922-1.453 3.375-3.547 3.64.531.344.89 1.094.89 1.954v1.625c0 .468.391.734.86.547C13.781 14.359 16 11.53 16 8.03 16 3.61 12.406 0 7.984 0 3.563 0 0 3.61 0 8.031a7.88 7.88 0 0 0 5.172 7.422c.422.156.828-.125.828-.547v-1.25c-.219.094-.5.156-.75.156-1.031 0-1.64-.562-2.078-1.609-.172-.422-.36-.672-.719-.719-.187-.015-.25-.093-.25-.187 0-.188.313-.328.625-.328.453 0 .844.281 1.25.86.313.452.64.655 1.031.655s.641-.14 1-.5c.266-.265.47-.5.657-.656"></path></svg>
      <span>nroduit/Weasis</span>
    </a>
</header>


  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <div class="github-info-container">

      <h4>
        Comment by
        <a href="https://github.com/clicker71" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/121013440?v=4" class="onebox-avatar-inline" width="20" height="20">
          clicker71
        </a> - <a href="https://github.com/nroduit/Weasis/pull/950#issuecomment-6219616602" target="_blank" rel="noopener nofollow ugc">Explorer hooks for plugins: context-menu contributor, thumbnail badges, DICOMweb origin of a study</a>
      </h4>



    <div class="branches">
      <code title="master">master</code> ← <code title="ups-explorer-hooks">ups-explorer-hooks</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Thanks for the explorer hooks - exactly the three extension points phase 2 needs<span class="show-more-container"><a href="https://github.com/nroduit/Weasis/pull/950" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> (context-menu contributor, thumbnail badges, DICOMweb origin).

Here is how we see phase 2 on top of them: Clarus as the origin, clinfer as the performer, one patient `XRV-DEMO` with a chest study (AI applies) and a knee study (it does not).

**1. Availability.** The badge is an availability indicator, not decoration: only the chest series carries it, because the catalogue task targets `*lung*` and the knee series has no matching BodyPartExamined. In the mergeable build this maps to `AI_TASK` / `AI_RESULT` through `SeriesBadgeProvider`.

![Badge on the chest series, none on the knee](https://raw.githubusercontent.com/clicker71/clarus-pacs/main/images/weasis-demo-robot-visibility.png)

**2. Done.** Run (Create, RAD-80) -&gt; clinfer claims -&gt; COMPLETED. The badge flips to the result state, and "Show tasks" names the derived object by its own SOP Class UID (Secondary Capture), not a hard-coded one.

![Done with the result named](https://raw.githubusercontent.com/clicker71/clarus-pacs/main/images/weasis-demo-task-done.png)

**3. Cancel.** While a task is queued or running, the menu offers Cancel (Request Cancellation, 11.8).

![Cancel while pending](https://raw.githubusercontent.com/clicker71/clarus-pacs/main/images/weasis-demo-ability-to-cancel.png)

Two questions on the menu behaviour:

- After COMPLETED, "Run" stays enabled (Create-if-none allows a re-run). Should the menu grey the entry once the task has a completed workitem, or keep it re-runnable? Today we disable it only while SCHEDULED / IN PROGRESS.
- The dialog lists each result as plain text. We would rather render it as a clickable entry that loads the object (image / SR / SEG) through the WADO-RS path - the performer already names the Series Instance UID (0020,000E) in the Output Information Sequence, so a direct retrieve URL is buildable. Is that the direction you want?

The workitem codes are minted under the private scheme `99CLARUS` (PS3.3 Table 8.8-1) - the deployment vocabulary, not part of Weasis.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For transparency, the same idea is filed for OHIF<br>
( <a href="https://github.com/OHIF/Viewers/issues/6369" class="inline-onebox" rel="noopener nofollow ugc">[Feature Request] UPS-RS User Agent (Task Requester + Watcher) to trigger AI workflows from the viewer · Issue #6369 · OHIF/Viewers · GitHub</a> ) and is under discussion with the dwv maintainer for a browser client.</p>
<p>Question for the Slicer community: would a UPS-RS User Agent extension for Slicer be useful - a worklist module that does the create / claim / subscribe / load loop, so any performer plugs in through one standard interface instead of each shipping its own workflow? Would the MONAI-Label / TotalSegmentator / NVIDIA AIAA folks see value in a common task contract?</p>
<p>I am happy to write the extension (Python, standard-only) and test it against Clarus and dcm4chee-arc as the origins, keeping it dependency-minimal.</p>
<p>Best regards,<br>
Daniil , <a href="https://github.com/clicker71/clarus-pacs" rel="noopener nofollow ugc">Clarus PACS</a></p>

---
