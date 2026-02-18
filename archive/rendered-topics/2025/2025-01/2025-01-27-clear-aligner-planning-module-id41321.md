# Clear Aligner Planning Module

**Topic ID**: 41321
**Date**: 2025-01-27
**URL**: https://discourse.slicer.org/t/clear-aligner-planning-module/41321

---

## Post #1 by @manjula (2025-01-27 17:22 UTC)

<p>Dear all,</p>
<p>We are planning to develop an open-source module for designing clear aligners for 3D Slicer. Our aim is to create a tool that allows dental professionals to design clear aligners for both thermoforming and direct 3D printing, making cutting-edge orthodontic technology more accessible to everyone.</p>
<p><a class="mention" href="/u/pramudithasj">@pramudithaSJ</a> , <a class="mention" href="/u/aravinda_sandaruwan">@Aravinda_Sandaruwan</a> and <a class="mention" href="/u/sasikala_kottegoda">@Sasikala_Kottegoda</a> have volunteered to take on the programming for this project. While they’re software programmers they are new to 3D Slicer and could really use the guidance of experienced members in this community. We’d deeply appreciate any help you can offer, <strong>especially in getting the architecture right from the start</strong>.</p>
<p>Here’s what we conceive for the module:</p>
<ol>
<li><strong>AI-Powered Tooth Segmentation</strong> : Automatically segment individual teeth from Intra Oral Scans (IOS)</li>
<li><strong>Editing and Aligning:</strong> Develop tools to import, align, and edit intraoral scans (IOS), cone-beam CT (CBCT) data, and patient photos.</li>
<li><strong>Easy Tooth Movement and Alignment</strong> : Intuitive tools to adjust tooth positions, including automatic alignment.</li>
<li><strong>Real-Time Visualization</strong> : Simulate and visualize treatment plan stages to better plan tooth movements and communicate effectively with patients and clinicians</li>
<li><strong>Staging and Sequencing</strong> : Tools to create multiple treatment stages, giving precise control over tooth movement sequences.</li>
<li><strong>Manufacturing-Ready Models</strong> : Generate 3D-printable models for thermoforming and generating the shell for direct 3D printing.</li>
<li><strong>AI-Driven Optimization</strong> : Incorporate AI model to get trained on the treatment planning and later do the treatment planning</li>
<li><strong>User-Friendly Workflow</strong> : Build an interface that’s simple to navigate.</li>
</ol>
<p>Most of the tools needed for this is already in the 3D Slicer. We are looking to piece them together and also to improve some of them further.</p>
<p>We warmly invite the community to share your feedback, ideas, and expertise to help us fast-track the development of this module into a functional prototype within the next 3 months.</p>
<p>Thank you<br>
Manjula</p>

---

## Post #2 by @pieper (2025-01-28 07:55 UTC)

<p>Dear Manjula -</p>
<p>This sounds like an exciting project and as you say, many of the elements are already present in Slicer so the project sounds achievable, but still ambitious.</p>
<p>I suggest the team begin by studying other open extensions carefully and perform experiments to get comfortable with each of the required technical components.  This could take the form of open experimental scripts and tests that can later be assembled into a friendly workflow (that is, debug and understand the technical parts before attempting to assemble them).</p>
<p>As you plan to make the results open doing these experiments in open, simple reproducible scripts that operate on open data will make it more fruitful in interacting with other developers to solve any questions that arise.</p>
<p>-Steve</p>

---

## Post #3 by @cpinter (2025-01-29 11:31 UTC)

<p>The only solution I am aware of for point <span class="hashtag-raw">#1</span> is this extension</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/DCBIA-OrthoLab/SlicerDentalModelSeg">
  <header class="source">

      <a href="https://github.com/DCBIA-OrthoLab/SlicerDentalModelSeg" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/1f6b9bb034754fb801e2db3c52b121ce/DCBIA-OrthoLab/SlicerDentalModelSeg" class="thumbnail">

  <h3><a href="https://github.com/DCBIA-OrthoLab/SlicerDentalModelSeg" target="_blank" rel="noopener">GitHub - DCBIA-OrthoLab/SlicerDentalModelSeg: This extension aims to provide a GUI for a...</a></h3>

    <p><span class="github-repo-description">This extension aims to provide a GUI for a deep-learning automated teeth segmentation tool that we developed at the University of North Carolina in Chapel Hill in collaboration with the University of Michigan in Ann Arbor.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However, I just tried last week and was unable to run it with any of the following Slicer versions: 5.6.2, 5.7, 5.8, 5.2.1. There does not seem to bee much activity on this lately, neither on the development nor the support side (see <a href="https://github.com/DCBIA-OrthoLab/SlicerDentalModelSeg/issues/33" class="inline-onebox">Prediction done but without output · Issue #33 · DCBIA-OrthoLab/SlicerDentalModelSeg · GitHub</a>), but maybe you could try.<br>
Automatic IOS segmentation is difficult, because surface mesh segmentation is not really in the main stream, so training your own model is also far from trivial.</p>

---

## Post #4 by @manjula (2025-01-29 13:20 UTC)

<p>Thank you Steve and Csaba for the replies much appreciated.</p>
<p>The most challenging would be the segmentation of the teeth. Entire process hang on this. We are looking at the same extension and hoping to get it to work. I got it to work some time back but not sure the version. We will work on the above extension and see if we can get it to work. Otherwise we need to look at a alternative on how to get this done.</p>
<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="41321">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Automatic IOS segmentation is difficult</p>
</blockquote>
</aside>
<p>But this has been very successfully implemented this on all the commercial software we use for aligner planning. Any pointers on how this has been done ?</p>
<p>The manual segmentation can be done with the curve cut</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f37747741a6b7210f16441efca506d08f3f4388b.jpeg" data-download-href="/uploads/short-url/yJNzW9FmC2YZn0FiIXePIKKcjB9.jpeg?dl=1" title="Screenshot from 2025-01-29 18-49-34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f37747741a6b7210f16441efca506d08f3f4388b_2_690x431.jpeg" alt="Screenshot from 2025-01-29 18-49-34" data-base62-sha1="yJNzW9FmC2YZn0FiIXePIKKcjB9" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f37747741a6b7210f16441efca506d08f3f4388b_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f37747741a6b7210f16441efca506d08f3f4388b_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f37747741a6b7210f16441efca506d08f3f4388b_2_1380x862.jpeg 2x" data-dominant-color="B7B8B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-01-29 18-49-34</span><span class="informations">1920×1200 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>best<br>
Manjula</p>

---

## Post #5 by @Romulo_Alfaro (2025-05-10 10:55 UTC)

<div class="youtube-onebox lazy-video-container" data-video-id="RGQe-5urAjg" data-video-title="3D Slicer  instance segmentation  plugin for individual teeth" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=RGQe-5urAjg" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/RGQe-5urAjg/maxresdefault.jpg" title="3D Slicer  instance segmentation  plugin for individual teeth" width="690" height="388">
  </a>
</div>


---

## Post #6 by @miladshani (2025-09-03 18:16 UTC)

<p>Hello Manjula,</p>
<p>Any updates about clear aligner planning module? I have seen the instance segmentation plugin which is very good but is the rest under development or the project had been stopped? (I’m new here, sorry if I’m asking something obvious)</p>
<p>Just wanna have something like onyxceph for transplant aligner but open source.</p>
<p>thanks.</p>

---

## Post #7 by @fabien-prog (2025-09-22 20:15 UTC)

<p>I was able to use ALI, ASO and segmentation for IOS dental scans in my custom python app and in the Slicer app.</p>
<p>I’m running Slicer 5.8.1 on windows 11 with WSL2 (Ubuntu 24.04)</p>
<p>I could help! There was a few modifications I had to make to the CLI and QT files to make it work in wsl, but it works perfectly now with logging and cross sub-system file handling.</p>
<p>let me know if I could help in any way !</p>
<p>Fabien</p>

---

## Post #8 by @Souhail_Ben (2025-10-09 07:53 UTC)

<p>Hello Fabien,</p>
<p>Would love to learn how you achieved that over a quick chat, i’m working on something similar and maybe we can join forces !</p>
<p>Best,</p>
<p>Souhail</p>

---

## Post #9 by @fabien-prog (2025-10-16 01:18 UTC)

<p>Contact me on Reddit in private chat : <a href="https://www.reddit.com/user/Stayin_alive_ah/" class="inline-onebox" rel="noopener nofollow ugc">Reddit - The heart of the internet</a></p>

---
