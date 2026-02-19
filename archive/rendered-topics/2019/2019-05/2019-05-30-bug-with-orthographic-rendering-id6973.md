---
topic_id: 6973
title: "Bug With Orthographic Rendering"
date: 2019-05-30
url: https://discourse.slicer.org/t/6973
---

# Bug with Orthographic rendering

**Topic ID**: 6973
**Date**: 2019-05-30
**URL**: https://discourse.slicer.org/t/bug-with-orthographic-rendering/6973

---

## Post #1 by @muratmaga (2019-05-30 17:29 UTC)

<p>When orthographic rendering is enabled, modifying any of the 3D scene options (box, labels, background etc) resets the field of view (like zoom level). We use orthographic rendering quite a bit to enable the ruler option to prepare figures for publication purposes.</p>
<p>On a related note, it would be good to revert the ruler color to black, if the 3D scene background is white. Otherwise it is not visible.</p>

---

## Post #2 by @pieper (2019-05-30 19:02 UTC)

<p>Yes, the reset happens at the line highlighted below.  If I remove that line then the field of view is not reset when changing view parameters, but the first time you enter orthographic mode the field of view is very small (at least for the MRHead dataset).  I’m not sure that’s better.</p>
<p>For the ruler color, maybe better to let the user select black or white ruler (e.g. white ruler over a dark specimen might make sense even if the background it white).  We could just add some more rows to the off/thick/thin ruler menu for this.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/d9cad8916139374f5462e137b878697387874cb8/Libs/MRML/DisplayableManager/vtkMRMLViewDisplayableManager.cxx#L473" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/d9cad8916139374f5462e137b878697387874cb8/Libs/MRML/DisplayableManager/vtkMRMLViewDisplayableManager.cxx#L473" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/d9cad8916139374f5462e137b878697387874cb8/Libs/MRML/DisplayableManager/vtkMRMLViewDisplayableManager.cxx#L473</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="463" style="counter-reset: li-counter 462 ;">
<li>  assert(this-&gt;External-&gt;GetRenderer()-&gt;IsActiveCameraCreated());</li>
<li>
</li>
<li>  vtkCamera *cam = this-&gt;External-&gt;GetRenderer()-&gt;GetActiveCamera();</li>
<li>  if (this-&gt;External-&gt;GetMRMLViewNode()-&gt;GetRenderMode() == vtkMRMLViewNode::Perspective)</li>
<li>    {</li>
<li>    cam-&gt;ParallelProjectionOff();</li>
<li>    }</li>
<li>  else if (this-&gt;External-&gt;GetMRMLViewNode()-&gt;GetRenderMode() == vtkMRMLViewNode::Orthographic)</li>
<li>    {</li>
<li>    cam-&gt;ParallelProjectionOn();</li>
<li class="selected">    cam-&gt;SetParallelScale(this-&gt;External-&gt;GetMRMLViewNode()-&gt;GetFieldOfView());</li>
<li>    }</li>
<li>}</li>
<li>
</li>
<li>//---------------------------------------------------------------------------</li>
<li>void vtkMRMLViewDisplayableManager::vtkInternal::UpdateStereoType()</li>
<li>{</li>
<li>  vtkDebugWithObjectMacro(this-&gt;External, &lt;&lt; "UpdateStereoType:" &lt;&lt;</li>
<li>                this-&gt;External-&gt;GetMRMLViewNode()-&gt;GetStereoType());</li>
<li>
</li>
<li>  vtkRenderWindow * renderWindow = this-&gt;External-&gt;GetRenderer()-&gt;GetRenderWindow();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2019-05-30 19:48 UTC)

<p>Reset happening while changing rendering types is acceptable, at least for me. What’s annoying is after I set up the scene in the orientation I would to present, and had to change the background, or remove the box or labels and it resets. It makes is hard to produce consistent looking images interactively.</p>
<p>I am not sure how white ruler with show up on dark specimen. I personally prefer not to overlay the ruler on the image being rendered so that nothing is obstructed. Maybe an option to set the color?</p>

---

## Post #4 by @pieper (2019-05-30 20:08 UTC)

<p>Right now I believe it goes through this same path when any mode is changed, meaning the orthographic view is reset.  Yes, it’s probably possible to bypass that.  Right now there’s just one path, and any time a view parameter is changed that parallel scale setting is updated.  I guess the real question is why manipulating the view doesn’t set the view node’s field of view to match the ParallelScale so that it can be reset correctly.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="6973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I am not sure how white ruler with show up on dark specimen. I personally prefer not to overlay the ruler on the image being rendered so that nothing is obstructed. Maybe an option to set the color?</p>
</blockquote>
</aside>
<p>What I meant was an image like below.  In general for this I think it would be better for the user to explicitly set the color rather than having it change automatically so there’s more control.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f65c66beb842cfc3138e8a70ff9eeafe4ebb669.jpeg" alt="image" data-base62-sha1="ib0GPF7MG7LxXXgF0JpwrKdEizn" width="423" height="299"></p>

---

## Post #5 by @pieper (2019-05-30 20:37 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="6973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I guess the real question is why manipulating the view doesn’t set the view node’s field of view to match the ParallelScale so that it can be reset correctly.</p>
</blockquote>
</aside>
<p>I found that indeed, the view node wasn’t being updated by the camera widget and that’s why the view was getting reset when the modes were changed.  I went ahead and <a href="https://github.com/Slicer/Slicer/commit/773d1ff461766b7124875c7e48edeabf67ce4fd4">committed a fix</a> that works for me - if anyone sees any side effects let me know.</p>

---

## Post #6 by @muratmaga (2019-05-31 00:04 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>. I am all for giving the user the option to set the color of the ruler and the text. Would be a nice feature to have.</p>

---

## Post #7 by @pieper (2019-05-31 20:29 UTC)

<p>I went ahead and implemented the options for ruler color.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/1147">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/1147" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/1147" target="_blank" rel="noopener">selecting lightbox 3x3 crashes Slicer</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:38:28" data-timezone="UTC">10:38PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:38:29" data-timezone="UTC">10:38PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=1147). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @pieper (2019-05-31 22:00 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> just commited the ruler color options (added a yellow option too per <a class="mention" href="/u/lassoan">@lassoan</a>’s suggestion).  You can try it in a future nightly build.</p>

---
