---
topic_id: 24400
title: "Starting Slicer From Github Actions Workflow"
date: 2022-07-19
url: https://discourse.slicer.org/t/24400
---

# Starting Slicer from GitHub Actions workflow

**Topic ID**: 24400
**Date**: 2022-07-19
**URL**: https://discourse.slicer.org/t/starting-slicer-from-github-actions-workflow/24400

---

## Post #1 by @jamesobutler (2022-07-19 20:06 UTC)

<p>I’m attempting to start Slicer (specifically a custom app) from a GitHub actions workflow, but I’m constantly running into “Graphics capability of this computer is not sufficient to run this application” issues. Does anyone know what might be going wrong here with my setup?</p>
<p>I have setup a <a href="https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners" rel="noopener nofollow ugc">self-hosted</a> GitHub actions runner on a Windows desktop that is running a Quadro P620 graphics card.  Maybe my understanding of how GitHub actions work is not correct? The runner is a desktop with a graphics card and a connected monitor for display. Starting the application directly on the desktop does not run into this graphics capability issue. I have taken a look at <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start" class="inline-onebox" rel="noopener nofollow ugc">Get Help — 3D Slicer documentation</a> and tried to follow the instructions there, but I keep running into the same graphics capability warning.</p>

---

## Post #2 by @pieper (2022-07-19 20:39 UTC)

<p>This sounds like what happens with some RDP (remote desktop protocol) on sessions windows.  Do you specifically need windows?  I’ve had good luck with <code>xvfb</code> on linux</p>

---

## Post #3 by @jamesobutler (2022-07-19 20:52 UTC)

<p>I don’t necessarily need to use Windows. It is just the self-hosted runner for GitHub Actions is a Windows Desktop in my office.</p>

---

## Post #4 by @lassoan (2022-07-19 23:35 UTC)

<p>For continuous integration, a native Linux would be probably a better choice than Windows: using software renderers are much more common on Linux, and also because the build is about 5-6x faster compared to Windows (30 minutes for a full Slicer build from scratch, instead of 2.5-3 hours). You would probably also want to share the build result as a docker image (so that you can try the application and not just run the tests on it), which again is probably simpler to do on Linux.</p>

---

## Post #5 by @jamesobutler (2022-07-20 01:29 UTC)

<p>Not sure if you all have had experiences with both Azure Pipelines and GitHub Actions. I had been starting Slicer successfully through an Azure Pipelines run, but once I switched to GitHub Actions it isn’t running the same. This was surprising to me since my impression was that these two options were very very similar.</p>

---

## Post #6 by @pieper (2022-07-20 03:04 UTC)

<p>That’s interesting.  I also assumed github actions on windows and Azure pipelines would be pretty similar.  It seems Andras and I have had the same experience that 90% (or so) of issues you’d want to catch in CI are platform-independent so it’s probably cleaner to have linux as the baseline.  Of course if you want to test against windows APIs or VS versions you’ll need windows.  Perhaps you can set up something other than RDP with the github actions (vnc on windows tends to work well, as does google chrome remote desktop although it may not be easy to use in CI).</p>

---
