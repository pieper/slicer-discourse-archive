# Slicer Coverage Testing?

**Topic ID**: 28764
**Date**: 2023-04-05
**URL**: https://discourse.slicer.org/t/slicer-coverage-testing/28764

---

## Post #1 by @hannahm (2023-04-05 18:21 UTC)

<p>I know there have previous discussions about using the coverage python module with scripted modules (<a href="https://discourse.slicer.org/t/how-to-generate-a-test-coverage-report-for-scripted-module/20714" class="inline-onebox">How to generate a test coverage report for scripted module?</a>), but I was wondering if there was any additional thought towards this?</p>

---

## Post #2 by @jamesobutler (2023-04-05 20:55 UTC)

<p>I’m not aware of Slicer having determined what coverage all the tests/selfTests/etc actually cover. I’m sure other Slicer developers would agree that having quantification of coverage would be appreciated to see how well Slicer testing is actually doing and to find places in the code that are rarely executed.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a> Has the Slicer community ever gauged how well the core tests cover the code in a quantifiable metric?</p>
<p>It appears that <a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> began adding code coverage to <a href="https://gitlab.com/opendose/opendose3d" rel="noopener nofollow ugc">SlicerOpenDose</a>. <a class="mention" href="/u/alex_vergara">@Alex_Vergara</a>, how well did that work out for you in your Slicer extension? Did you run into issues with appropriately getting coverage metrics?</p>
<p>Based on recent conversations related to the Slicer Extensions Index and how to manage the growing list of extensions that are submitted and how to better provide timely reviews, code coverage of extensions could be used as one of the elements for a Extension score card similar to ITK’s <a href="https://github.com/InsightSoftwareConsortium/ITK/tree/v5.3.0/Modules/Remote#documenting-the-compliance-level-of-a-remote-module" rel="noopener nofollow ugc">remote module compliance level</a>. In the ever growing list of Slicer extensions, we could begin to rank extensions based on their compliance where extensions with no tests would be given a low score,  an extension with a single test given a better score, and an extension with tests that are proven with high code coverage to be given an even higher score. Currently the Slicer Extensions Index has a self-score which is then rarely updated.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Extensions/ScriptedLoadableExtensionTemplate.s4ext#L33-L35">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Extensions/ScriptedLoadableExtensionTemplate.s4ext#L33-L35" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Extensions/ScriptedLoadableExtensionTemplate.s4ext#L33-L35" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Extensions/ScriptedLoadableExtensionTemplate.s4ext#L33-L35</a></h4>



    <pre class="onebox"><code class="lang-s4ext">
      <ol class="start lines" start="33" style="counter-reset: li-counter 32 ;">
          <li># Give people an idea what to expect from this code</li>
          <li>#  - Is it just a test or something you stand behind?</li>
          <li>status</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jamesobutler (2023-04-10 15:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a> Do you all have any knowledge of past determination of how well Slicer testing covered the code? Or know if other groups have successfully utilized more quantifiable metrics regarding how well their testing covered their extensions?</p>

---

## Post #4 by @pieper (2023-04-10 16:17 UTC)

<p>I can’t think of anything other than what’s in the earlier posts.  It would definitely be nice to have.</p>

---

## Post #5 by @jcfr (2023-04-10 16:41 UTC)

<blockquote>
<p>how well Slicer testing covered the code?</p>
</blockquote>
<p>There are few scenarios to consider:</p>
<ol>
<li>independent python package  (e.g utility code)</li>
<li>python scripted module</li>
<li>C++ modules</li>
</ol>
<p>Coverage for (1) and (3) can be done respectively leveraging <a href="https://coverage.readthedocs.io/en/7.2.3/">coverage</a> and <a href="https://gcc.gnu.org/onlinedocs/gcc/Gcov.html">gcov</a>.</p>
<p>Both may also be reported in CDash (see <a href="https://gitlab.kitware.com/cmake/community/-/wikis/doc/ctest/Coverage">here</a>)</p>
<p>Challenge will be to instrument infrastructure and then merge coverage results involving both python and C++ code (e.g scripted modules, SubjectHierachy/DICOM/SegmentEditor plugins, …)</p>

---

## Post #6 by @lassoan (2023-04-10 18:20 UTC)

<p>It would be interesting to get some coverage statistics.</p>
<p>That said, at the application level I would prefer if user requirements (what are important for users to work correctly) would drive our testing efforts and not coverage percentages.</p>
<p>At library level we may not have specific user requirements, so coverage testing may be much more useful there. We could start with trying to add coverage testing to vtkAddon and MRML Core.</p>

---

## Post #7 by @Alex_Vergara (2023-04-11 07:36 UTC)

<p>Hi, coverage in my extension coverage reports only works if I perform the tests manually within Slicer. If I do the tests inside a docker container without GUI, the reports are not produced.</p>

---
