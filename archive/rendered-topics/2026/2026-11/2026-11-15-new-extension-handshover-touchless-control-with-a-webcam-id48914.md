---
topic_id: 48914
title: "New extension - HandsHover : touchless control with a webcam"
date: 2026-11-15
url: https://discourse.slicer.org/t/48914
last_bumped: 2026-11-15T19:32:59.562Z
---

# New extension - HandsHover : touchless control with a webcam

**Topic ID**: 48914
**Date**: 2026-11-15
**URL**: https://discourse.slicer.org/t/new-extension-handshover-touchless-control-with-a-webcam/48914

---

## Post #1 by @Paul_M (2026-11-15 19:32 UTC)

<p>Hello everyone,</p>
<p>I have been using 3D Slicer for about ten years, but this is my very first post.</p>
<p>I am a digestive surgeon in France, and I built a module for my own use that I would like to share with you.</p>
<p>My goal is to be able to control my 3D models while I am operating. It is mainly useful in colorectal surgery (mostly right hemicolectomy), sometimes in gastric surgery, and for rare cases.<br>
During my residency I tried to build something similar with an old Kinect, but with no coding skills at all I gave up.</p>
<p>I then used a Leap Motion a lot, but the company has changed hands, the device is no longer sold, and there is no longer any software support. It also emulated a mouse, so it was not very precise.</p>
<p>I still have no coding skills, but I used Claude to build it. HandsHover uses an ordinary webcam and Google’s MediaPipe hand tracking, running in a separate process so that Slicer stays responsive. It recognizes a few simple hand poses and drives Slicer’s views directly, without emulating a mouse. Almost everything is done with one hand:</p>
<ul>
<li>V sign + horizontal swipe: next / previous view (3D, Red, Green, Yellow)</li>
<li>pinch: rotate the 3D model, or scroll through slices (faster gesture = faster scrolling)</li>
<li>fist + up/down: zoom</li>
<li>index finger + move: pan</li>
<li>thumb up for 1 s: recenter the view</li>
<li>two fists for 1 s: pause / resume, to avoid accidental commands</li>
</ul>
<p>A banner at the top of the window always shows the active view, and camera images are processed locally on the computer: nothing is sent anywhere.</p>
<p>Here is the GitHub repository:</p>
<aside class="onebox githubrepo github-onebox" data-onebox-src="https://github.com/PaulMLH/HandsHover">
    <header class="source github-onebox__header">
  <span class="github-onebox__label" role="img" aria-label="Repository" title="Repository">
    <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path></svg>
    <span>Repository</span>
  </span>
    <a class="github-onebox__repo" href="https://github.com/PaulMLH/HandsHover" target="_blank" rel="noopener nofollow ugc">
      <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6.766 11.328c-2.063-.25-3.516-1.734-3.516-3.656 0-.781.281-1.625.75-2.188-.203-.515-.172-1.609.063-2.062.625-.078 1.468.25 1.968.703.594-.187 1.219-.281 1.985-.281.765 0 1.39.094 1.953.265.484-.437 1.344-.765 1.969-.687.218.422.25 1.515.046 2.047.5.593.766 1.39.766 2.203 0 1.922-1.453 3.375-3.547 3.64.531.344.89 1.094.89 1.954v1.625c0 .468.391.734.86.547C13.781 14.359 16 11.53 16 8.03 16 3.61 12.406 0 7.984 0 3.563 0 0 3.61 0 8.031a7.88 7.88 0 0 0 5.172 7.422c.422.156.828-.125.828-.547v-1.25c-.219.094-.5.156-.75.156-1.031 0-1.64-.562-2.078-1.609-.172-.422-.36-.672-.719-.719-.187-.015-.25-.093-.25-.187 0-.188.313-.328.625-.328.453 0 .844.281 1.25.86.313.452.64.655 1.031.655s.641-.14 1-.5c.266-.265.47-.5.657-.656"></path></svg>
      <span>PaulMLH/HandsHover</span>
    </a>
</header>


  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/3cfee3748efaabdcea56f93e38c32762/PaulMLH/HandsHover" class="thumbnail">

  <h3><a href="https://github.com/PaulMLH/HandsHover" target="_blank" rel="noopener nofollow ugc">GitHub - PaulMLH/HandsHover</a></h3>

    <p><span class="github-repo-description">Contribute to PaulMLH/HandsHover development by creating an account on GitHub.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And here is a link to a short video made quickly (a rather busy weekend on call, and bad weather in the north of France, hence the lighting conditions <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=16" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"> ):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="Rim-zK2K8bw" data-video-title="hands" data-video-start-time="" data-video-list-id="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Rim-zK2K8bw" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Rim-zK2K8bw/maxresdefault.jpg" title="hands" width="690" height="388">
  </a>
</div>

<p>I will keep improving it over time, based on my own use and on your feedback, if it finds an audience.</p>
<p>Thank you for reading, and any feedback is very welcome!</p>
<p>Best regards,<br>
Paul</p>

---
