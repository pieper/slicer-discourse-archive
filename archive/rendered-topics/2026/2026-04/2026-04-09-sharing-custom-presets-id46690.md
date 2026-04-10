---
topic_id: 46690
title: "Sharing Custom Presets"
date: 2026-04-09
url: https://discourse.slicer.org/t/46690
---

# Sharing custom presets

**Topic ID**: 46690
**Date**: 2026-04-09
**URL**: https://discourse.slicer.org/t/sharing-custom-presets/46690

---

## Post #1 by @muratmaga (2026-04-09 05:52 UTC)

<p>This is something I wanted for the SlicerMorph project for a while and I bite the bullet and asked copilot to create a github repo to share and add presets.</p>
<p>As indicated in the contributing.MD you simply add two items to the preset folder volume property json file and a png (file prefixes need to be identical). After the PR is merged, an automated action updates the README file with the new entries for easy visual browsing. You can click on the download to get the URL of the vp.json file which you can use the Sample Data module to import directly into the scene.</p>
<p>I am sure we can build something much easier to add and grow but I wanted to have the conversation started.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerMorph/VPs?tab=readme-ov-file">
  <header class="source">

      <a href="https://github.com/SlicerMorph/VPs?tab=readme-ov-file" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/60042b5b840c5615edb262fcc3fef5d1/SlicerMorph/VPs?tab=readme-ov-file" class="thumbnail">

  <h3><a href="https://github.com/SlicerMorph/VPs?tab=readme-ov-file" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/VPs: trial repo for sharing volume rendering properties</a></h3>

    <p><span class="github-repo-description">trial repo for sharing volume rendering properties</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2026-04-09 12:22 UTC)

<p>I like this, thanks for putting it together.</p>
<p>To make it easier to grow the collection, we could create some code that automates the contribution process.  Basically if you have a rendering you like, you could just do a one-click submission by using <code>gh</code> under the hood to do the whole PR process.</p>

---

## Post #3 by @muratmaga (2026-04-09 16:00 UTC)

<p>Yes, definitely if you have gh installed and authenticated it is a one liner. So that might be an option for people who are already using MorphoDepot since it is already there, but I am not sure if gh CLI use is  general enough to build a tool around it just for this.</p>
<p>I do make the screenshots in the hiresScreenCapture because it is much easier to control the aspect ratio and get 1:1 (or close).</p>

---

## Post #4 by @muratmaga (2026-04-09 21:49 UTC)

<p>Spent a bit more time to make it a bit more automated. So now you create your volume property in Slicer and upload it directly from a module.</p>
<p>If you want to try out, you can try the <strong>vp-submit</strong> branch in the SlicerMorph  <code>git clone --branch vp-submit https://github.com/SlicerMorph/SlicerMorph.git</code></p>
<p>After that you can:</p>
<ol>
<li>
<p>Load a volume and enable volume rendering and create one <strong>VolumeProperty</strong> preset in the scene (or edit one of the existing preset to make it different).</p>
</li>
<li>
<p>While strictly not necessary, I suggest renaming it different from the original preset name.</p>
</li>
</ol>
<h3><a name="p-133121-submitting-a-preset-1" class="anchor" href="#p-133121-submitting-a-preset-1" aria-label="Heading link"></a><strong>Submitting a preset</strong></h3>
<ol>
<li>
<p>Open the <strong>SubmitVolumeRenderingPreset</strong> module (under <em>SlicerMorph Utilities</em>).</p>
</li>
<li>
<p>Select your vp from the dropdown. You can hit refresh to get all the volume property loaded in the scene  Fill in an optional description and author name.</p>
</li>
<li>
<p>Choose a 3-D view and arrange it as you want it to appear in the gallery.</p>
</li>
<li>
<p>Click  <strong>– Upload and submit to GitHub</strong>. The module uploads both vp.json and the captures screenshot automatically (saved to a temp location) and opens a pre-filled GitHub issue in your browser.</p>
</li>
<li>
<p>Click <strong>Submit new issue</strong></p>
</li>
</ol>
<p>This would create a PR for me to take a quick look and once merged it will be shown at <a href="https://github.com/SlicerMorph/VPs?tab=readme-ov-file" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/VPs: trial repo for sharing volume rendering properties · GitHub</a></p>
<p>Note that I decided to use the new JSON based volume rendering property file as opposed to old txt file. Make sure you are trying with a preview version.</p>
<p>Suggestions are welcomed.</p>

---
