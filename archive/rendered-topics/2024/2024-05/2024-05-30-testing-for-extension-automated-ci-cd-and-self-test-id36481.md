---
topic_id: 36481
title: "Testing For Extension Automated Ci Cd And Self Test"
date: 2024-05-30
url: https://discourse.slicer.org/t/36481
---

# Testing for Extension: Automated CI/CD and Self Test

**Topic ID**: 36481
**Date**: 2024-05-30
**URL**: https://discourse.slicer.org/t/testing-for-extension-automated-ci-cd-and-self-test/36481

---

## Post #1 by @haphantran (2024-05-30 02:14 UTC)

<p>Hello,<br>
We’re developing a extension for 3D Slicer. I’m thinking about how we can do automated testing with CI/CD tool. If we can do with GitHub Action maybe. We can install 3D Slicer in the pipeline, but I don’t know how we can use GitHub action to run the script to open our extension and click some button to test it.<br>
About Self tests (test will run when we click Reload &amp; Test in the UI), can we check if all UI elements load, then click some elements then test the state of app (Similar to automated Web testing)?<br>
Thank you in advance.</p>

---

## Post #2 by @pieper (2024-05-30 17:37 UTC)

<p>For extensions that get built with Slicer as part of the nightly process the CI is done automatically and posted to <a href="https://slicer.cdash.org/projects">the dashboard</a>.  This includes building any C++ code, running SelfTests and other tests, and packaging for all platforms.  If you want to replicate that process yourself for a non-public extension all the code and scripts are available.</p>
<p>If your extension is private but python only, you could take a simpler route and develop some CI that just runs your extension code against a downloaded Slicer binary using a virtual desktop like Xvfb or Xdummy.</p>

---

## Post #3 by @jamesobutler (2024-05-30 18:27 UTC)

<p>SlicerDMRI created a GitHub Actions workflow to build and test its extension at time of PR instead of waiting for the nightly Slicer factory build and test of extensions.</p>
<p>See the workflow below.  <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/b4357b934f82c9ced74e0ba0defed7f0a89b792d/.github/workflows/build-test.yml" class="inline-onebox" rel="noopener nofollow ugc">SlicerDMRI/.github/workflows/build-test.yml at b4357b934f82c9ced74e0ba0defed7f0a89b792d · SlicerDMRI/SlicerDMRI · GitHub</a></p>
<p>It has a Build Slicer step which takes 2 hours and 20 minutes. You can see the various steps of the workflow in this run:</p><aside class="onebox githubactions" data-onebox-src="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/8791859403/job/24126917992?pr=235">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/8791859403/job/24126917992?pr=235" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">


      <svg width="24" height="24" class="github-icon github-icon-failure" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M1 12C1 5.925 5.925 1 12 1s11 4.925 11 11-4.925 11-11 11S1 18.075 1 12zm8.036-4.024a.75.75 0 00-1.06 1.06L10.939 12l-2.963 2.963a.75.75 0 101.06 1.06L12 13.06l2.963 2.964a.75.75 0 001.061-1.06L13.061 12l2.963-2.964a.75.75 0 10-1.06-1.06L12 10.939 9.036 7.976z"></path></svg>

  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/8791859403/job/24126917992?pr=235" target="_blank" rel="noopener nofollow ugc">ENH: Update extension metadata
</a>
    </h4>

      <div class="github-info">
        Build, test <span class="github-run-number">#169</span>
      </div>
  </div>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @haphantran (2024-07-28 21:59 UTC)

<p>Thank you so much. It looks promising for us. We will definitely try it.</p>

---
