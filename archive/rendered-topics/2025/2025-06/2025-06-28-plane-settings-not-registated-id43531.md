# Plane settings not registated

**Topic ID**: 43531
**Date**: 2025-06-28
**URL**: https://discourse.slicer.org/t/plane-settings-not-registated/43531

---

## Post #1 by @philippepellerin (2025-06-28 09:30 UTC)

<p>Hi, the plane setting in the landmarks module is not registrated.<br>
I saved, as a bundle, some plane settings where I unticked the case plane setting visibility and setting the sliding ruler of visibility to 0. When I reopen the file, those settings are back to tick and 100.<br>
Slicer 5-9-0 2025-06-19<br>
Best regards.</p>

---

## Post #2 by @pieper (2025-06-28 13:11 UTC)

<p>Thanks for the report - it would help if you could file an issue on github.  I believe this would be in the <a href="https://github.com/Slicer/Slicer/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22">good first issue</a> category.  It’s probably a straightforward fix for someone who wants to learn the internals.</p>

---

## Post #3 by @philippepellerin (2025-06-28 14:26 UTC)

<p>I will try my best…</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #4 by @pieper (2025-06-28 14:37 UTC)

<p>That’s great, thanks for filing the issue <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>For background, we like to use discourse for things like how-to discussions and ideas for future work, and then github issues for concrete to-do items.  Once they are on github it will be a reminder that it needs to be addressed if/when we have some more developer support (resources are tight currently, so if anyone in the community what’s to chip in, please do!).</p>
<p>Here’s the link for reference:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8518">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8518" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8518" target="_blank" rel="noopener">plane setting not recording</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-28" data-time="14:17:23" data-timezone="UTC">02:17PM - 28 Jun 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/philippenoelmarie" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/45486120?v=4" class="onebox-avatar-inline" width="20" height="20">
          philippenoelmarie
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          good first issue
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In the markup module, when I create and edit a plane, in the plane settings, I t<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ick the visibility box and set the ruler to 0 out of 100 (I want to hide the arrow). Then, I save the file as a bundle (.mrb). When I reopen the bundle the arrow is displayed, the plane settings show that the visibility is ticked anew and the ruler set to 100.
Thus, it looks as if the save command has forgotten those values.
## Steps to reproduce
-create a plane with the markups module.
-go to the bottom, toward the "plane settings"
-tick the visibility.
-set  the visibility ruller to 100.
-save the file as a bundle.
-reopen the bundle.
-check, in the markup module the settings for this plane, down to the plane settings, box and ruller visibility.


- Slicer version: Slicer-5.0.9-2025-06-19
- Operating system:  Mac + sequoia 15-5</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @philippepellerin (2025-06-28 14:42 UTC)

<p>I would do more if I could,I would love it, but I know nothing about programming, sorry.<br>
I am simply an enthusiastic end-user. Thanks to your work, you made many of my dreams come true! Thank you very much for that.<br>
Best wishes.</p>
<p>Pr Philippe PELLERIN<br>
18 rue de la Carnoy 59130 Lambersart.<br>
Former coordinator of the French National Reference Center for Rare Craniomaxillofacial Malformations.<br>
Lille University Hospital; France.</p>

---

## Post #6 by @pieper (2025-06-28 14:54 UTC)

<p>That’s excellent to hear <a class="mention" href="/u/philippepellerin">@philippepellerin</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> We understand that not everyone is into programming, but your expert feedback is extremely valuable and appreciated.</p>
<p>In case you didn’t see it, there were several CMF-related projects last week at Project Week in Montreal, investigating the use of Silcer for orbit reconstruction, TMJ pain assessment, tooth labeling.  I think there are many other exciting applications to come.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW43_2025_Montreal/#projects">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW43_2025_Montreal/#projects" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW43_2025_Montreal/#projects" target="_blank" rel="noopener">Welcome to the web page for the 43rd Project Week!</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @philippepellerin (2025-06-28 15:02 UTC)

<p>I have been very happy to do the manual segmentations, which allowed to train the masticatory and oculo-motor muscles segmentation task in the total segmentator. Right now I am building a Skull Atlas out of 180 normal CT scans with the DeCA module which was an old dream coming true; I am in touch with Murat Maga on this one.</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---
