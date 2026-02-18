# Sad to see Slicer deteriorate

**Topic ID**: 35102
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/sad-to-see-slicer-deteriorate/35102

---

## Post #1 by @Greydon_Gilmore (2024-03-26 15:07 UTC)

<pre data-code-wrap="console"><code class="lang-console">OS: Pop!_OS 22.04 LTS jammy x86_64
Slicer version: 5.6.1
</code></pre>
<p>It’s been a good run for 3D Slicer, sad to see the development take a turn for the worse every new update that comes out since 4.11.</p>
<p>Newest bug/issue in 5.6.1 in the transforms module. If you attempt to manually correct the transform using the slider bars, while adjusting the rotation, the translation sliders will move to completely random values and render the transform useless.</p>
<p>3D Slicer is very unreliable.</p>

---

## Post #2 by @pieper (2024-03-26 15:19 UTC)

<p>Well, gee, that’s a pretty negative comment - certainly I disagree strongly!  Slicer is definitely better than ever and continues to improve thanks to a devoted community.</p>
<p>As a case in point, you are probably referring to an issue that was quickly fixed as soon as it was pointed out:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7594">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7594" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7594" target="_blank" rel="noopener">BUG: Fix unrelated matrix elements overwritten in transform editor</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-transform-editing</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-02-20" data-time="17:46:20" data-timezone="UTC">05:46PM - 20 Feb 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 31 additions and 28 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7594/files" target="_blank" rel="noopener">
            <span class="added">+31</span>
            <span class="removed">-28</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is a fix for the transformation matrix editing glitch that @RafaelPalomar d<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7594" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">emonstrated during the weekly developer meeting.

In transforms module, when linear transformation matrix values were edited using spinboxes and then by directly editing the matrix, the value that was previously edited in the spinbox got overwritten by the new value.

The issue was that a single slot was used for all signals coming from all sliders and in the slot implementation the active focus was used to determine which axis should be updated. Fixed by using a separate slot for each axis. This way we don't rely on the GUI widget focus, which may go through complex transitions during transform editing using various widgets.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2024-03-26 16:47 UTC)

<p>Perhaps you might want to get involved with the development and helping the slicer to become better?</p>
<p>I am not sure what is the use of a comment like this for a free and a community developed and supported product.</p>

---

## Post #4 by @chir.set (2024-03-26 17:35 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>what is the use of a comment like this</p>
</blockquote>
</aside>
<p>Just a click-bait. OP wanted attention. He is served. Me was amused, take it as entertainment.</p>

---

## Post #5 by @Greydon_Gilmore (2024-03-27 09:13 UTC)

<p>I am married to 3D Slicer. I spend every waking moment of every day in 3D Slicer. When my eyes open to when my eyes close I am working in 3D Slicer. All our new trainees are taught 3D Slicer.</p>
<p>3D Slicer is the ONLY tool in my arsenal that I need multiple versions, installed on my system to perform different tasks.</p>
<p>You say you want community engagement but you don’t. You implement changes that are not good for the community but are things the internal developers want.</p>
<p>Your handling of coordinate systems to what file extensions you do and do not accept from version to version makes my head spin.</p>
<p>All of a sudden, a robust file format FCSV, is now complete chaos. In 5.6, I now have 2 additional columns added to the file WITHOUT being defined in the header line. 16 data columns but only 14 header definitions. Its many of these small things that add up and are making Slicer very unstable.</p>
<p>I will always love 3D Slicer, just any version before v5.</p>

---

## Post #6 by @jamesobutler (2024-03-27 11:27 UTC)

<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="5" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>All of a sudden, a robust file format FCSV, is now complete chaos. In 5.6, I now have 2 additional columns added to the file WITHOUT being defined in the header line. 16 data columns but only 14 header definitions. Its many of these small things that add up and are making Slicer very unstable.</p>
</blockquote>
</aside>
<p>Greydon…I understand your frustration with having to update your code for your lab to work with the latest Slicer. Backwards compatibility is always attempted to be maintained, but Slicer is also a research tool that makes many things possible and things will change to support that. FCSV format cannot be in “total chaos” but then also considered “many of these small things”. I agree that the header comment field should describe the 2 additional column fields for clarity about what they mean. A suggestion to fix that would be helpful for the community. If we can help you update your scripts based on these 2 extra columns let us know! We are here to help which is why there is a support category on the forum. I see in your older posts you have successfully used the migration guide in years past to update your code. We can support your efforts again.</p>

---

## Post #7 by @mikebind (2024-03-27 15:14 UTC)

<p>I’ve been using Slicer extensively for 5 years now, and while I have experienced backwards compatibility issues at times which have been setbacks in my tools, I have also seen huge increases in new capabilities in areas which make a lot of difference.  I have found the Slicer community on this forum the most helpful and responsive of any I have interacted with on the web, and have been very impressed by the speed with which issues, once identified, are corrected.  Because of its very wide range of capabilities, Slicer is used in so many different ways by so many different people that the willingness to make changes and introduce new things often might inadvertently break something for someone else. If you are happy on Slicer 4, you can remain using Slicer 4.  If you want the new capabilities of Slicer 5, then that involves making things compatible with the new changes in Slicer 5.  I will continue to prefer the choices the developers are making to prioritize the incorporation of new capabilities and improvements of old methods over maintaining strict backwards compatibility.</p>

---

## Post #8 by @muratmaga (2024-03-27 16:08 UTC)

<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="5" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>You say you want community engagement but you don’t. You implement changes that are not good for the community but are things the internal developers want.</p>
</blockquote>
</aside>
<p>That is because you are not engaged in the actual process of how things are decided. Most of these come in with long term discussion at project week or weekly calls, and there are importantly decisions. You can come and voice your opinion in those, and more importantly if you want to be in the driving seat about how those things are implement, find some funding (or dedicate your people’s time) to implement things that you need. You are welcomed to participate in all of these.</p>
<p>As a research tool, the needs of the slicer is typically determined by needs of the active funded projects that needs those. That makes sense, because those are the ones practically paying for all the costs of maintaining and developing the software. There is really no other money (apart from what Kitware donates in terms of computer infrastructure and their engineers time to make all that websites, extension manager, automatic update infrastructure to work). If there are conflict in needs, that’s usually handled in these meetings and usually come up with a solution, it may not be always great for everyone involved, but usually it is we find a fairly amicable and workable solution.</p>
<p>I will comment on the fcsv change a bit, because my group was involved in that. We created this great way of using blank landmark templates (so that everytime you get exactly the same number of landmarks in the same  order, if you are not familiar check the video <a href="https://www.youtube.com/watch?v=SUouhaIMWXw">Landmark Templates in 3D Slicer (youtube.com)</a>. This required a major reworking of the markups module infrastrucre and addition of new properties to markups that contains the state of the markup (set, unset, in progress etc). This cannot be handled by the fcsv format. Hence the decision going forward to create the warning about fcsv format being lossy and that people should be saving their files as JSON to avoid issues.</p>
<p>I understand your frustration. My lab have been using Slicer over a decade now, and we probably have about 10-12 thousands fcsv files we have collected from our samples during this time. We gradually migrate them to JSON as we need. It is not difficult. This wasn’t the first time it happened, and I am sure it won’t be the last. When Slicer 4 was released, the markups (it used to be called annotations) were of a different format too (every control point was saved individually).</p>
<p>Big changes like this every decade or so is almost expected. These changes are not made because it makes developers life easier, but it is made because the biomedical imaging software tools (i.e., commercial and other open source tools)  and community needs evolves over time. That means you have to maintain interoperability, you need to support new research directions and hardware changes. Ideally this should be done in a backward compatible way, but we don’t always have the resources.</p>
<p>This is where you come in. As <a class="mention" href="/u/jamesobutler">@jamesobutler</a> mentioned you can post you needs, and work with others on the community to express your issue and resolve them. If you can actually sponsor some of this work, then it is even faster. Becasue while the software is provided free, development and changes are not. And often these are not a lot of money. Depending on the ask and the scope of things, it might even cost less than an annual support contract of a commercial biomedical image analysis tool. Or a maybe the cost of a single seat.</p>

---

## Post #9 by @lassoan (2024-03-27 17:15 UTC)

<p><a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a> Other community members already nicely described how things happen and why, I would just emphasize that we like to get feedback that is specific enough so that we can discuss it and act on it. If many things bother you then please take the time to describe each.</p>

---

## Post #10 by @RafaelPalomar (2024-03-27 22:53 UTC)

<p><a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a>, there are more positive ways to channel frustration. Some of your assessments don’t look fair to me.</p>
<aside class="quote no-group quote-modified" data-username="Greydon_Gilmore" data-post="1" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>Newest bug/issue in 5.6.1 in the transforms module…</p>
</blockquote>
</aside>
<p>I did report that issue during the devs meeting (open to everyone) and it was solved in a matter of hours.</p>
<p><a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a>, if you have a list of bugs or issues, I would encourage you to report them using the appropriated channels, so the community can benefit in the same way as you can now benefit from the reporting I did about the transforms module. Using an already resolved issue to criticize the development course of 3D Slicer does not seem very constructive.</p>
<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="5" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>You say you want community engagement but you don’t. You implement changes that are not good for the community but are things the internal developers want.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a>, 3D Slicer is (by far) the largest medical image computing research platform out there with the largest community in the field. To be sure, every member has a different idea on  what  “good for the community” is. It would be more useful to everyone if you come up with concrete ways to improve Slicer so your ideas can be discussed.</p>

---

## Post #11 by @MCM-Fischer (2024-03-29 13:14 UTC)

<p>That’s a [?] mentality.<br>
You use 3D Slicer every day but you or the organization you work for do not have to pay any cent.<br>
You could pay by giving constructive feedback, participating in the decision making process, or by directly contributing to the code.<br>
Or you could stop using 3D Slicer and pay for commercial software with less capabilities facing the same issues.</p>
<p>What is the idea behind such a post? Frustrate the ones who participate in the development of 3D Slicer.</p>

---

## Post #12 by @Greydon_Gilmore (2024-03-29 15:31 UTC)

<p>If funds are required then funds we can support.</p>
<p>In the words of Dr. Kary Mullis from his book “Dancing Naked in the Mind Field”, it feels like “no one is minding the store”. Seems most are working in their silos and not minding the macro scale of 3D Slicer.</p>
<p>For our group this is not just a research tool. For our epilepsy patients, we perform radio-frequency ablation. During these sessions we burn their brain at specific sites. Deviations as small as 1mm could mean the difference between seizure freedom and harming eloquent brain areas.</p>
<p>While I appreciate bugs are being fixed in the nightly, they are not fixed in the version of 3D Slicer our clinical team have been trained on and use. We cannot continuously update our Slicer versions.</p>
<p>If there is an email group for developers then I’d appreciate being included.</p>

---

## Post #13 by @muratmaga (2024-03-29 15:48 UTC)

<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="12" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>For our group this is not just a research tool. For our epilepsy patients, we perform radio-frequency ablation. During these sessions we burn their brain at specific sites. Deviations as small as 1mm could mean the difference between seizure freedom and harming eloquent brain areas.</p>
</blockquote>
</aside>
<p>Then you should consider supporting slicer a lot more. First, it is not a clinical tool, that’s your choice to use in a clinical setting (you are not alone, there are others doing that as well).</p>
<p>You can choose to pay someone to keep 4.11 up to date for you. Or you can pay someone to build a custom slicer with all the specific issues you are encountering is fixed, and you can stick with that version. There are other alternatives too. The best to do, as other describe make a list of things important for you to get fixed, and then you can post this under jobs category, and I am sure people will respond.</p>
<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="12" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>If there is an email group for developers then I’d appreciate being included.</p>
</blockquote>
</aside>
<p>There is no other user group.</p>

---

## Post #14 by @shai-ikko (2024-04-01 08:23 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="13" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="12" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>If there is an email group for developers then I’d appreciate being included.</p>
</blockquote>
</aside>
<p>There is no other user group.</p>
</blockquote>
</aside>
<p>… but if following by email is your thing, you can get this forum to notify you on everything interesting. In any category you find interesting, click the bell sign on the top right, and you can choose which notifications to get. I’d guess the “Development” and “Feature requests” categories are pertinent.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f06441533a485b3ab01c19d5657aaed081486bb.png" data-download-href="/uploads/short-url/i7I3W10UBTMA146g3jNHw9iXImf.png?dl=1" title="Screenshot_20240401_112039" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f06441533a485b3ab01c19d5657aaed081486bb_2_689x245.png" alt="Screenshot_20240401_112039" data-base62-sha1="i7I3W10UBTMA146g3jNHw9iXImf" width="689" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f06441533a485b3ab01c19d5657aaed081486bb_2_689x245.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f06441533a485b3ab01c19d5657aaed081486bb_2_1033x367.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f06441533a485b3ab01c19d5657aaed081486bb.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20240401_112039</span><span class="informations">1181×420 83.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @muratmaga (2024-04-05 08:51 UTC)

<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="12" data-topic="35102">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>they are not fixed in the version of 3D Slicer our clinical team have been trained on and use.</p>
</blockquote>
</aside>
<p>I will re-iterate that if you are using Slicer in a clinical setting and this is important for you, you should take the responsibility of maintaining a stable version for your workflow by building slicer for your team locally.</p>
<p>With that in mind, the 5.6.2 patch version will have the transform bug fix. You can check from here for updates about when it is going to be released.</p><aside class="quote" data-post="2" data-topic="35300">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/release-of-slicer-5-6-2-in-progress/35300/2">Release of Slicer 5.6.2 in progress</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    <a name="p-109180-update-1" class="anchor" href="#p-109180-update-1" aria-label="Heading link"></a>Update

Slicer 5.6.2 packages are being generated  <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/hourglass_flowing_sand.png?v=15" title="hourglass_flowing_sand" alt="hourglass_flowing_sand" class="emoji">
Regular Preview and Stable builds have NOT been resumed
  </blockquote>
</aside>


---
