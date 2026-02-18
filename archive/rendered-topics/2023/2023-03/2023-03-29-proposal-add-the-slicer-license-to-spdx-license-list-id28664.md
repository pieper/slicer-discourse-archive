# Proposal: Add the Slicer license to SPDX license list

**Topic ID**: 28664
**Date**: 2023-03-29
**URL**: https://discourse.slicer.org/t/proposal-add-the-slicer-license-to-spdx-license-list/28664

---

## Post #1 by @jcfr (2023-03-29 18:43 UTC)

<h3><a name="p-92823-what-is-the-spdx-license-list-1" class="anchor" href="#p-92823-what-is-the-spdx-license-list-1" aria-label="Heading link"></a>What is the SPDX License List ?</h3>
<blockquote>
<p>The SPDX License List is an integral part of the SPDX Specification. The SPDX License List itself is a list of commonly found licenses and exceptions used in free and open or collaborative software, data, hardware, or documentation. The SPDX License List includes a standardized short identifier, the full name, the license text, and a canonical permanent URL for each license and exception.</p>
</blockquote>
<p>See <a href="https://spdx.org/licenses/" class="inline-onebox">SPDX License List | Software Package Data Exchange (SPDX)</a></p>
<h3><a name="p-92823-why-should-we-add-the-slicer-license-2" class="anchor" href="#p-92823-why-should-we-add-the-slicer-license-2" aria-label="Heading link"></a>Why should we add the Slicer license ?</h3>
<h4><a name="p-92823-tooling-integration-3" class="anchor" href="#p-92823-tooling-integration-3" aria-label="Heading link"></a>Tooling integration</h4>
<p>The SPDX license list is used by licensing tooling. See <a href="https://spdx.dev/tools-community/">https://spdx.dev/tools-community/</a></p>
<h4><a name="p-92823-github-integration-4" class="anchor" href="#p-92823-github-integration-4" aria-label="Heading link"></a>GitHub integration</h4>
<p>Having the license available in the SPDX license list is one of the first step to have the Slicer license detected by GitHub:</p>
<ul>
<li><a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository#detecting-a-license">GitHub Docs / Detecting a license</a></li>
<li><a href="https://github.com/github/choosealicense.com/blob/gh-pages/CONTRIBUTING.md#adding-a-license">Adding a license</a></li>
</ul>
<h3><a name="p-92823-steps-to-add-slicer-license-to-the-spdx-list-5" class="anchor" href="#p-92823-steps-to-add-slicer-license-to-the-spdx-list-5" aria-label="Heading link"></a>Steps to add Slicer license to the SPDX list</h3>
<p>The request should be submitted following these instructions.<br>
See <a href="https://github.com/spdx/license-list-XML/blob/main/CONTRIBUTING.md">https://github.com/spdx/license-list-XML/blob/main/CONTRIBUTING.md</a></p>
<p>To streamline the process, we should likely reuse material associated with <a href="https://discourse.slicer.org/t/apply-for-osi-open-source-license-status/17791" class="inline-onebox">Apply for OSI open source license status</a></p>
<p>The online tool streamlines the process.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/752e2173a89bafe43dc6ef9dc9a24750f006278c.png" data-download-href="/uploads/short-url/gICHjdTD8cvyAoOREx5cwy2BJla.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/752e2173a89bafe43dc6ef9dc9a24750f006278c_2_345x184.png" alt="image" data-base62-sha1="gICHjdTD8cvyAoOREx5cwy2BJla" width="345" height="184" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/752e2173a89bafe43dc6ef9dc9a24750f006278c_2_345x184.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/752e2173a89bafe43dc6ef9dc9a24750f006278c_2_517x276.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/752e2173a89bafe43dc6ef9dc9a24750f006278c_2_690x368.png 2x" data-dominant-color="F3F8FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3406×1824 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Suggested content for the request:</strong></p>
<p><em>Adapted from <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#license">https://slicer.readthedocs.io/en/latest/user_guide/about.html#license</a></em></p>
<ol>
<li>
<p>License Name:<br>
3D Slicer license</p>
</li>
<li>
<p>Short identifier:<br>
3d-slicer-license</p>
</li>
<li>
<p>License Author or steward:<br>
Brigham and Women’s Hospital (BWH)</p>
</li>
<li>
<p>Comments:</p>
<p>The 3D Slicer software is distributed under a BSD-style open source license that is broadly compatible with the Open Source Definition by The Open Source Initiative and contains no restrictions on legal uses of the software.</p>
<h3><a name="p-92823-historical-notes-about-the-license-6" class="anchor" href="#p-92823-historical-notes-about-the-license-6" aria-label="Heading link"></a>Historical notes about the license</h3>
<p>The Slicer License was drafted in 2005 by lawyers working for Brigham and Women’s Hospital (BWH), a teaching affiliate of Harvard Medical School, to be BSD-like but with a few extra provisions related to medical software. It is specific to BWH so it’s not directly reusable, but it could serve as a template for projects with similar goals.</p>
<p>It was written in part because BWH was the prime contractor on an NIH-funded development consortium (<a href="https://www.na-mic.org/">NA-MIC</a>) and wanted all code contributions to be compatible with ultimate use in real-world medical products (that is, commercial FDA-approved medical devices, which are almost universally closed source even if they build on open software). Compliance with the Slicer License was required for subcontractors, a group that included GE Research, Kitware and several universities (MIT, UNC…) who all reviewed and accepted this license.</p>
<p>The license has been in continuous use since 2005 for the 3D Slicer software package (<a href="http://slicer.org">slicer.org</a>) that as of 2021 has been downloaded more than a million times and has been referenced in about 12,000 academic publications (<a href="https://www.slicer.org/wiki/Main_Page/SlicerCommunity">https://www.slicer.org/wiki/Main_Page/SlicerCommunity</a>). Some of the code is also now being used in several medical products for which this license has been reviewed and accepted by the companies involved.</p>
<h3><a name="p-92823-license-terms-and-reasons-7" class="anchor" href="#p-92823-license-terms-and-reasons-7" aria-label="Heading link"></a>License terms and reasons</h3>
<p>Here are some of the key points that BWH included in addition to BSD terms to make the license suit the case of a large hospital distributing open source medical software.</p>
<p>For using and redistributing 3D Slicer:</p>
<blockquote>
<p>The license states that the code is “designed for research” and “CLINICAL APPLICATIONS ARE NEITHER RECOMMENDED NOR ADVISED” to make it extra clear that any commercial clinical uses of the code are solely the responsibility of the user and not BWH or the other developers. This is a disclaimer rather than a legal restriction.</p>
</blockquote>
<p>For making changes or adding any source code or data to 3D Slicer:</p>
<ul>
<li>
<p>Contributors explicitly grant royalty free rights if they contribute code covered by a patent they control (i.e. to avoid submarine patents).</p>
</li>
<li>
<p>No GPL or other copyleft code is allowed because that could make it complicated and risky to mix Slicer code with private intellectual property, which is often present in regulated medical products.</p>
</li>
<li>
<p>Contributors affirm that they have de-identified any patient data they contribute to avoid issues with HIPAA or related regulations.</p>
</li>
</ul>
<h3><a name="p-92823-status-compared-to-other-open-source-licenses-8" class="anchor" href="#p-92823-status-compared-to-other-open-source-licenses-8" aria-label="Heading link"></a>Status compared to other open source licenses</h3>
<p>As of June 2021, the Slicer License has been used for over 15 years without incident. In May of 2021, a discourse user <a href="https://discourse.slicer.org/t/apply-for-osi-open-source-license-status/17791">suggested</a> submitting the license to <a href="https://opensource.org/approval">the OSI license review process</a>. After some discussion and hearing no objections, the community leadership decided to <a href="https://lists.opensource.org/pipermail/license-review_lists.opensource.org/2021-May/thread.html">submit the license for review</a>. Although the OSI process is not legally binding, the discussion could give potential Slicer users perspective on how provisions of the license compare with other commonly used licenses. The discussion concluded that bundling the contribution agreement in the license makes it non-approvable by OSI and the requirement to use the software for legal purposes may not be consistent with the <a href="https://opensource.org/osd">Open Source Definition</a>. Otherwise the license terms appear not to be controversial. Interested parties should review the <a href="https://lists.opensource.org/pipermail/license-review_lists.opensource.org/2021-June/thread.html#5166">full discussion</a> for details.</p>
</li>
<li>
<p>License Request Url:<br>
TBD</p>
</li>
<li>
<p>URL(s):<br>
<a href="https://github.com/Slicer/Slicer/blob/main/License.txt">https://github.com/Slicer/Slicer/blob/main/License.txt</a></p>
</li>
<li>
<p>OSI Status:<br>
Rejected</p>
</li>
<li>
<p>Example Projects:</p>
</li>
</ol>
<ul>
<li><a href="https://github.com/Slicer/Slicer">https://github.com/Slicer/Slicer</a></li>
<li><a href="https://github.com/Slicer/SlicerExecutionModel">https://github.com/Slicer/SlicerExecutionModel</a></li>
<li><a href="https://github.com/mhalle/spl-brain-atlas">https://github.com/mhalle/spl-brain-atlas</a></li>
</ul>
<pre><code class="lang-auto"></code></pre>

---

## Post #2 by @mhalle (2023-03-29 19:43 UTC)

<p>Would this be a good time to get a clean URL for the license? Like <a href="https://slicer.org/license" rel="noopener nofollow ugc">https://slicer.org/license</a> ?</p>

---

## Post #3 by @jcfr (2023-03-29 22:50 UTC)

<aside class="quote no-group" data-username="mhalle" data-post="2" data-topic="28664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>Would this be a good time to get a clean URL for the license?</p>
</blockquote>
</aside>
<p>The following files are already available:</p>
<ul>
<li><a href="https://slicer.org/LICENSE">https://slicer.org/LICENSE</a> (<a href="https://www.slicer.org/LICENSE">https://www.slicer.org/LICENSE</a>)</li>
<li><a href="https://slicer.org/copyright/copyright.txt">https://slicer.org/copyright/copyright.txt</a> (and also <a href="https://www.slicer.org/copyright/copyright.txt">https://www.slicer.org/copyright/copyright.txt</a>)</li>
</ul>
<p>We should then reference <code>https://slicer.org/LICENSE</code> in the request.</p>
<p>That said, there an issue with the mime-type.</p>
<p>Would you be able to update the server configuration to ensure the file is server with the correct mime-type ?</p>
<p>I think a settings like the should be added:</p>
<pre><code class="lang-auto">location = /LICENSE {
    types { }
    default_type text/html;
}
</code></pre>
<p>we could also potentially add the following:</p>
<pre><code class="lang-auto">location = /license {
    return 301 https://slicer.org/LICENSE;
}

location = /license.txt {
    return 301 https://slicer.org/LICENSE;
}
</code></pre>
<p>or even look into having a case-insensitive matching rule …</p>

---

## Post #4 by @mhalle (2023-03-29 23:47 UTC)

<p>I don’t have access to <a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a> at this time. I agree with your proposed changes to the config.</p>
<p>-Mike</p>

---

## Post #5 by @jcfr (2023-10-17 22:19 UTC)

<p>The license has been submitted:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/spdx/license-list-XML/issues/2213">
  <header class="source">

      <a href="https://github.com/spdx/license-list-XML/issues/2213" target="_blank" rel="noopener">github.com/spdx/license-list-XML</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/spdx/license-list-XML/issues/2213" target="_blank" rel="noopener">New license request: 3d-slicer-license [SPDX-Online-Tools]</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-17" data-time="22:17:11" data-timezone="UTC">10:17PM - 17 Oct 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">**1.** License Name: 3D Slicer license

**2.** Short identifier: 3d-slicer-lic<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ense

**3.** License Author or steward: Brigham and Women’s Hospital (BWH)

**4.** Comments:

&gt; The 3D Slicer software is distributed under a BSD-style open source license that is broadly compatible with the Open Source Definition by The Open Source Initiative and contains no restrictions on legal uses of the software.
&gt; 
&gt; ### Historical notes about the license
&gt; 
&gt; See https://slicer.readthedocs.io/en/latest/user_guide/about.html#historical-notes-about-the-license
&gt; 
&gt; ### License terms and reasons
&gt; 
&gt; See https://slicer.readthedocs.io/en/latest/user_guide/about.html#license-terms-and-reasons
&gt; 
&gt; ### Status compared to other open source licenses
&gt; 
&gt; As of June 2021, the Slicer License has been used for over 15 years without incident. In May of 2021, a discourse user [suggested](https://discourse.slicer.org/t/apply-for-osi-open-source-license-status/17791) submitting the license to [the OSI license review process](https://opensource.org/approval). After some discussion and hearing no objections, the community leadership decided to [submit the license for review](https://lists.opensource.org/pipermail/license-review_lists.opensource.org/2021-May/thread.html). Although the OSI process is not legally binding, the discussion could give potential Slicer users perspective on how provisions of the license compare with other commonly used licenses. The discussion concluded that bundling the contribution agreement in the license makes it non-approvable by OSI and the requirement to use the software for legal purposes may not be consistent with the [Open Source Definition](https://opensource.org/osd). Otherwise the license terms appear not to be controversial. Interested parties should review the [full discussion](https://lists.opensource.org/pipermail/license-review_lists.opensource.org/2021-June/thread.html#5166) for details.
&gt; 
&gt; Copied from https://slicer.readthedocs.io/en/latest/user_guide/about.html#status-compared-to-other-open-source-licenses

**5.** License Request Url: http://tools.spdx.org/app/license_requests/312

**6.** URL(s):
* https://slicer.org/LICENSE
* https://github.com/Slicer/Slicer/blob/main/License.txt

**7.** OSI Status: Rejected

**8.** Example Projects:
* https://github.com/Slicer/Slicer
* https://github.com/Slicer/SlicerExecutionModel
* https://github.com/mhalle/spl-brain-atlas</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jcfr (2024-05-09 17:22 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  The review process has been completed and the Slicer license is being added to the SPDX license list v3.24.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/open_book.png?v=12" title=":open_book:" class="emoji" alt=":open_book:" loading="lazy" width="20" height="20">  Reviewing notes are available at <a href="https://github.com/spdx/license-list-XML/issues/2213" class="inline-onebox">New license request: 3D-Slicer-1.0 · Issue #2213 · spdx/license-list-XML · GitHub</a></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> Thanks to everyone who provided feedback and helped move the process forward.</p>

---
