---
topic_id: 41482
title: "2025 02 04 Weekly Meeting Back To Regular Time"
date: 2025-02-04
url: https://discourse.slicer.org/t/41482
---

# 2025.02.04 Weekly Meeting - Back to regular time

**Topic ID**: 41482
**Date**: 2025-02-04
**URL**: https://discourse.slicer.org/t/2025-02-04-weekly-meeting-back-to-regular-time/41482

---

## Post #1 by @Sam_Horvath (2025-02-04 03:31 UTC)

<p>Tomorrow, we will be having our next weekly hangout at <strong>10:00 AM ET until 11:00 AM ET,</strong></p>
<p>Anyone is welcome to join at this link: <a href="https://bit.ly/slicer-googlemeet-hosted-by-kitware">https://bit.ly/slicer-googlemeet-hosted-by-kitware</a></p>
<hr>
<div class="discourse-post-event" data-start="2025-02-04 10:00" data-status="public" data-name="Weekly Meeting" data-url="https://bit.ly/slicer-googlemeet-hosted-by-kitware" data-timezone="America/New_York" data-allowed-groups="trust_level_0"></div>
<p><strong>Agenda:</strong></p>
<p>Please post to this thread to put a topic on the agenda!  We will try to prioritize agenda items during the meeting.</p>
<hr>
<p>Thanks<br>
Sam and J-Christophe</p>

---

## Post #2 by @Sam_Horvath (2025-02-04 03:33 UTC)

<p>CORRECTION - Meeting date will be 2025-02-04</p>

---

## Post #3 by @mau_igna_06 (2025-02-04 13:01 UTC)

<p>Hi <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I’d like to talk about the progress I’ve had on compiling a CLI module to use <a href="https://github.com/BrunoLevy/geogram/wiki/BooleanOps" rel="noopener nofollow ugc">Geogram’s (robust) boolean operations</a></p>

---

## Post #4 by @allemangd (2025-02-04 15:12 UTC)

<p>Overview of progress on <span class="hashtag-raw">#8181</span> for python requirements declarations.</p>
<p>Details here: <a href="https://github.com/Slicer/Slicer/pull/8181#issuecomment-2628257908" class="inline-onebox" rel="noopener nofollow ugc">Allow scripted modules to declare requirements and constraints, and enforce Slicer Core constraints. by allemangD · Pull Request #8181 · Slicer/Slicer · GitHub</a></p>
<p>Docs for this feature: <a href="https://slicer--8181.org.readthedocs.build/en/8181/developer_guide/python_packages.html" class="inline-onebox" rel="noopener nofollow ugc">Managing Python Packages — 3D Slicer documentation</a></p>
<p>I’d appreciate input on the remaining CMake issue for declaring the Slicer Core constraints.</p>

---

## Post #5 by @mau_igna_06 (2025-02-06 01:41 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> helped out a lot with CMake to add Geogram’s boolean operation for 3D models on Slicer.<br>
Currently it works as a CLI module, but I need to configure the library so it is delivered with the Sandbox extension</p>

---

## Post #6 by @jcfr (2025-02-11 14:50 UTC)

<h3><a name="p-122414-meeting-notes-1" class="anchor" href="#p-122414-meeting-notes-1" aria-label="Heading link"></a>Meeting Notes</h3>
<h4><a name="p-122414-project-week-recap-2" class="anchor" href="#p-122414-project-week-recap-2" aria-label="Heading link"></a>Project Week Recap</h4>
<ul>
<li><strong>SlicerTrame &amp; trame-slicer</strong>: Progress updates and integration discussions.</li>
<li><strong>Tutorial Maker</strong>: Improvements and workflow enhancements.</li>
<li><strong>Geogram</strong>: Reviewed advancements in mesh processing and potential applications.</li>
</ul>
<h4><a name="p-122414-curved-planar-reformat-cpr-3" class="anchor" href="#p-122414-curved-planar-reformat-cpr-3" aria-label="Heading link"></a>Curved Planar Reformat (CPR)</h4>
<ul>
<li><strong>Outcome from Project Week Discussions</strong>:
<ul>
<li>Following discussions with <a class="mention" href="/u/lassoan">@lassoan</a>, Thibault Pelletier, <a class="mention" href="/u/pieper">@pieper</a>, and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> during <a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/">42nd Slicer Project Week</a>, we have decided to introduce a <strong>GeneralizedReformat</strong> loadable module.</li>
<li><a class="mention" href="/u/lee_newberg">@Lee_Newberg</a> will work on the refactoring.</li>
<li>More details: <a href="https://github.com/Slicer/Slicer/pull/8148#issuecomment-2626225118">PR #8148</a>.</li>
</ul>
</li>
</ul>
<h4><a name="p-122414-refactor-corner-annotations-4" class="anchor" href="#p-122414-refactor-corner-annotations-4" aria-label="Heading link"></a>Refactor Corner Annotations</h4>
<ul>
<li><strong>Outcome from Project Week Discussions</strong>:
<ul>
<li><a class="mention" href="/u/lassoan">@lassoan</a> and the team agreed to proceed with integration once the remaining action items are addressed.</li>
<li><a class="mention" href="/u/arhowe00">@arhowe00</a> will review comments and finalize the work.</li>
<li>More details: <a href="https://github.com/Slicer/Slicer/pull/8143#issuecomment-2632089935">PR #8143</a>.</li>
</ul>
</li>
</ul>
<h4><a name="p-122414-scripted-modules-python-requirements-constraints-5" class="anchor" href="#p-122414-scripted-modules-python-requirements-constraints-5" aria-label="Heading link"></a>Scripted Modules: Python Requirements &amp; Constraints</h4>
<ul>
<li><a class="mention" href="/u/allemangd">@allemangd</a> discussed implementing support for <strong>scripted modules</strong> to declare Python requirements and constraints while enforcing <strong>Slicer Core constraints</strong>.</li>
<li>More details: <a href="https://github.com/Slicer/Slicer/pull/8181">PR #8181</a>.</li>
</ul>
<h4><a name="p-122414-nousnav-6" class="anchor" href="#p-122414-nousnav-6" aria-label="Heading link"></a>NousNav</h4>
<ul>
<li><strong>FDA Application</strong>: Moving forward with the <strong>FDA application process</strong>, with plans to <strong>publish associated documentation</strong>.</li>
</ul>
<h4><a name="p-122414-slicersofa-7" class="anchor" href="#p-122414-slicersofa-7" aria-label="Heading link"></a>SlicerSOFA</h4>
<ul>
<li>Review Pending PR: <a href="https://github.com/Slicer/SlicerSOFA/pull/43">PR #43</a>.</li>
<li><strong>SOFA Upgrade</strong>:
<ul>
<li>Moving forward with updating SOFA from 24.06 to 24.12.</li>
<li>SOFA 24.12 requires C++20, necessitating changes to ensure compatibility.</li>
</ul>
</li>
</ul>

---
