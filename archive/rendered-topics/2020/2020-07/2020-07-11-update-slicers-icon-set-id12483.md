---
topic_id: 12483
title: "Update Slicers Icon Set"
date: 2020-07-11
url: https://discourse.slicer.org/t/12483
---

# Update Slicer's icon set

**Topic ID**: 12483
**Date**: 2020-07-11
**URL**: https://discourse.slicer.org/t/update-slicers-icon-set/12483

---

## Post #1 by @lassoan (2020-07-11 02:20 UTC)

<p>We are making great progress with supporting dark mode in Slicer (see <a href="https://github.com/Slicer/Slicer/pull/4993">here</a>). However, our current icon set holds us back, as many of the icons are not very well visible/recognizable over dark background. Refreshing our icon set is also necessary because they have not been updated to match the much higher resolution of current displays. Also, many new icons were added, which don’t follow the style of the original Slicer icon set.</p>
<p>The question is, how could we get a new icon set and make sure we have a sustainable source of new icons for new features that are going to be added in the future?</p>
<p>Requirements:</p>
<ul>
<li>we should to get the complete new replacement icon in no more than 1-2 months</li>
<li>sustainability:
<ul>
<li>we should be able to get new icons for new features in no more than 1-2 weeks</li>
<li>we should be able to regenerate the icons at arbitrary resolutions (access to vector source)</li>
<li>preferably icon source should be editable with free software (Inkscape)</li>
</ul>
</li>
<li>openness:
<ul>
<li>we should be able to host all the used icons in our public github repository</li>
<li>we should be allowed to modify and combine icons</li>
<li>extension developers should be able to create similar style icons (maybe with slightly different color scheme)</li>
<li><strong>Question: is it important that companies who develop Slicer-based products can use the icons without buying license (typically few hundred $)?</strong></li>
</ul>
</li>
<li>style:
<ul>
<li>design should be simple, but not too simple: monochrome line icons are probably too simple (it could be hard to create meaningful icons for complex features); full-color, gradient, 3D icons are not trendy in these years</li>
<li>compatible with both light and dark background</li>
</ul>
</li>
</ul>
<p><strong>Question: Any more requirements to add?</strong></p>
<p>I’ve done some research and found that there could be two potential solutions for obtaining an icon set.</p>
<p>Option A. that there are very nice icon sets (containing thousands of icons), which could replace about 2/3 of our existing stock icons and could be used for constructing the remaining application-specific icons. This would allow us to get started quickly, create new icons in the future as needed (using/combining/customizing existing icons), and it would be inexpensive (probably a few hundred, worst case a few thousand $). The only limitation would be that we would not own the images, so companies that build products based on Slicer and use these icons would probably need to pay a few hundred $.</p>
<p>Option B. Hire a designer, who would create custom icons for us. The cost could be about $20-$40/icon and maybe we could negotiate a deal that they transfer ownership of the icon to Slicer (into the public domain), but maybe not. We need 150 commonly used icons and about 60-80 custom icons, so the total cost could be about $5-10k. It could take a while to design these icons, and long-term sustainability could be a question (as we would not have thousands of pre-created icons that we could choose from when adding new features, but we would rely on the availability of a single person).</p>
<p><strong>Question: Do we agree that Option A (starting from stock icon set) seems to be a better approach?</strong></p>
<p>Finally, about the style:</p>
<ul>
<li>We probably don’t want complex, detailed, gradient, 3D-effect icons, as they are not trendy.</li>
<li>There are duotone icons, which are solid icons using two colors in addition to the background color. These look nice, but usually the icon sets are much smaller, so it is not easy to find icon sets that cover most of our needs. Example:</li>
</ul>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://roundicons.com/accent-duo-tone-icons/">
  <header class="source">

      <a href="https://roundicons.com/accent-duo-tone-icons/" target="_blank" rel="noopener">Round Icons</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:600/338;"><img src="https://roundicons.com/wp-content/uploads/2019/08/Accent-Duo-Tone-Icons-Freebie.png" class="thumbnail" width="" height=""></div>

<h3><a href="https://roundicons.com/accent-duo-tone-icons/" target="_blank" rel="noopener">Accent Duo Tone Icons - Round Icons</a></h3>

  <p>2000 Premium accent duo tone icons provided in 5 color packs to choose from, vector files included Ai SVG Sketch Figma Adobe XD Png and Eps</p>

  <p>
    <span class="label1">Est. reading time: 66 minutes</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<ul>
<li>Line icons are nice and simple and trendy. With only a single color, they are pretty dull and hard to distinguish, but since we have access to the editable vector-graphics source of the icons, we can easily color them. They are easy to edit and combine them, since they are just lines. There are huge, inexpensive line icon sets, for example this:</li>
</ul>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://roundicons.com/native-line-solid-icons-pack/">
  <header class="source">

      <a href="https://roundicons.com/native-line-solid-icons-pack/" target="_blank" rel="noopener">Round Icons</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:600/338;"><img src="https://roundicons.com/wp-content/uploads/2017/01/native-line-icons-freebie-preview.png" class="thumbnail" width="" height=""></div>

<h3><a href="https://roundicons.com/native-line-solid-icons-pack/" target="_blank" rel="noopener">7,000 Native line icons pack - Round Icons Premium</a></h3>

  <p>Get above the competition with this massive Line icons pack, 109 categories containing 7,000 icons made for websites, IOS and Android apps.</p>

  <p>
    <span class="label1">Est. reading time: 80 minutes</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For example, we can color (using open-source Inkscape editor) a line drawing icon by using <a href="https://coolors.co/db5461-353238-47682c-a0ecd0-2de1c2">this</a> palette like this:<br>
Original:<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e968dbea86bb8051d0cdc2329d15e9033d55e2d.png" alt="image" data-base62-sha1="klomm8AmVC474tr8ukKrE1RTmsl" width="111" height="126"></p>
<p><strong>Question: Would line drawings with flat duotone-like coloring seem like a good style or there are other suggestions?</strong></p>

---

## Post #2 by @Davide_Punzo (2020-07-11 13:26 UTC)

<p>Updating the icons will be great. Modern icons would greatly help for a first good impression with new users. Minimalist/flat is the current trend which is good. However, I would avoid choosing a super flat / super minimalist style (e.g.: <a href="https://www.streamlineicons.com" rel="nofollow noopener">https://www.streamlineicons.com</a>); or at least not for everything. I am not sure which icons package is the best, but we should ensure also that there are enough “medical/scientific/computing” icons in the package (otherwise probably it would not make sense to go with <strong>Option A</strong>). I’ll scan the web too for icon sets, so we can see all the options.</p>

---

## Post #3 by @Davide_Punzo (2020-07-11 13:47 UTC)

<p>This was from Steve when we were talking about icons in an old post: <a href="https://react.ohif.org/elements/icon" rel="nofollow noopener">https://react.ohif.org/elements/icon</a></p>

---

## Post #4 by @lassoan (2020-07-11 15:11 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="3" data-topic="12483" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>This was from Steve when we were talking about icons in an old post: <a href="https://react.ohif.org/elements/icon">https://react.ohif.org/elements/icon</a></p>
</blockquote>
</aside>
<p>Thank you. This is a selection from the <a href="https://fontawesome.com">font awesome icon set</a>. They look “modern” but I find many of the icons very loosely related to their assigned meaning. This is a good example of how hard it is to find expressive icons in a small icon set.</p>
<aside class="quote no-group" data-username="Davide_Punzo" data-post="2" data-topic="12483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>I would avoid choosing a super flat / super minimalist style (e.g.: <a href="https://www.streamlineicons.com">https://www.streamlineicons.com </a>); or at least not for everything</p>
</blockquote>
</aside>
<p>I agree that monochrome line drawing is too simple for a desktop application, because appearance of standard widgets, buttons, sliders are much more detailed, it looks odd that icons are so minimalistic. However, with duotone coloring, they can be made quite nice. It makes icons much easier to color if lines are closed and Streamline icons tend to leave curves open, so for that reason this icon set might not be ideal.</p>
<aside class="quote no-group" data-username="Davide_Punzo" data-post="2" data-topic="12483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>the best, but we should ensure also that there are enough “medical/scientific/computing” icons in the package</p>
</blockquote>
</aside>
<p>Ide checked out 10-20 largest icon sets and medical/scientific icons are mostly useless, as they are not specific enough for the features that we need. However, about 2/3 of the Slicer icons are generic computing/GUI icons (arrows, files, folders, layers, show, add, delete, etc), so we can find suitable icons for these in most sets. For the rest, we can get inspiration from thousands of other icons, modify them, combine them.</p>

---

## Post #5 by @pieper (2020-07-11 15:53 UTC)

<p>I’d really prefer to avoid anything that requires people to buy a license to reuse Slicer.  It would be so much nicer if someone with talent who believes the the value of free medical software to spend time making icons.</p>
<p>Such people may be hard to find, but we have found people who contribute code, tutorials, and support, so maybe we can encourage icon contributions too.</p>
<p>Maybe we can reach out to a community of artists to ask for help.</p>

---

## Post #6 by @Davide_Punzo (2020-07-11 17:17 UTC)

<p>I agree and having a shared repository, something like CTK, would be amazing. On the other hand, if we have to do this ourselves without professional help, an icon package will help. In general, I also would like to avoid any strict license. I guess at the end, it is a balance of the resourses that we will have for this and interest in updating the icons from the community.</p>

---

## Post #7 by @mikebind (2020-07-14 00:03 UTC)

<p>A fee to license the icons would be a barrier for creating a small scale commercial product for me.  Probably not an insurmountable barrier, but it would factor in.  It would also feel pretty odd that out of all the amazing tools and capabilities of Slicer, the part that wasn’t free was the icons. If Slicer goes that route, which would be very understandable, it would be great if there were an option to use existing free icons and/or substitute custom developer-supplied icons.  I can imagine developing a Slicelet with a pretty small set of needed icons, and I might prefer to create a few or use older style icons rather than pay a licensing fee.</p>

---

## Post #8 by @lassoan (2020-07-14 05:48 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="7" data-topic="12483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>It would also feel pretty odd that out of all the amazing tools and capabilities of Slicer, the part that wasn’t free was the icons.</p>
</blockquote>
</aside>
<p>I fully agree that it would be so much better to find an artist who could can design a few hundred nice icons in no more than 1-2 months for no more than a few thousand $, put all the icons into the public domain, and make a commitment to be available for designing new icons when needed. However, it is just so much unlikely to happen. If you know someone the let us know.</p>
<p>In contrast, paying about $1000 for an existing icon set a maybe few thousand $ for someone to combine/customize them to create icons Slicer-specific features sounds something that can be done. Risk and cost is quite small and the whole project could be completed in a couple of weeks.</p>
<aside class="quote no-group" data-username="mikebind" data-post="7" data-topic="12483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>A fee to license the icons would be a barrier for creating a small scale commercial product for me.</p>
</blockquote>
</aside>
<p>Replacing the default Slicer branding (custom style sheet, icons, etc.) is usually among the very first tasks in commercial product development projects (everybody wants his application to look unique). It should be already possible to override the default icon set without changing Slicer’s source (by setting Slicer_LOGOS_RESOURCE variable to your custom resource file).</p>
<p>Maintaining two icon sets within Slicer would be too much work (we already struggle with only one), but licensing fee for an icon set for a single developer is usually less than a few hundred $ but may cost much less (<a href="https://roundicons.com/native-line-solid-icons-pack/">roundicons vector native line icon set</a> contains 7000 icons and costs $45).</p>

---

## Post #9 by @Davide_Punzo (2020-07-14 08:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="12483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I fully agree that it would be so much better to find an artist who could can design a few hundred nice icons in no more than 1-2 months for no more than a few thousand $, put all the icons into the public domain, and make a commitment to be available for designing new icons when needed. However, it is just so much unlikely to happen. If you know someone the let us know.</p>
</blockquote>
</aside>
<p>I think finding a good icon designer on upwork/fiverr/etc. is not a problem. I guess the issue may be where we can get the funding for it. Unfortunately, as now I am a freelancer too, I don’t have funding possibilities at the moment.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="12483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maintaining two icon sets within Slicer would be too much work (we already struggle with only one), but licensing fee for an icon set for a single developer is usually less than a few hundred $ but may cost much less (<a href="https://roundicons.com/native-line-solid-icons-pack/" rel="noopener nofollow ugc">roundicons vector native line icon set</a> contains 7000 icons and costs $45).</p>
</blockquote>
</aside>
<p>I agree, and a cost of ~100 dollars license should not be an issue also for small scale commercial product.</p>
<p>On the other hand a good icon artist/designer may create something much better and customized for 3DSlicer.</p>

---

## Post #10 by @lassoan (2020-07-15 04:04 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="9" data-topic="12483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>I think finding a good icon designer on upwork/fiverr/etc. is not a problem.</p>
</blockquote>
</aside>
<p>It is actually not easy: it is a huge task to design hundreds of icons, it may cost tens of thousands of $, you need to find an artist who is willing to give up all rights on his creations, to make sure the right person is found, we would need a multi-round selection process, etc.</p>
<p>Kitware has a few full-time UI/UX designers, who might be able to help with this. <a class="mention" href="/u/jcfr">@jcfr</a> will ask and report back next week.</p>

---

## Post #11 by @jcfr (2020-07-15 14:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="12483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Kitware has a few full-time UI/UX designers, who might be able to help with this. <a class="mention" href="/u/jcfr">@jcfr</a> will ask and report back next week.</p>
</blockquote>
</aside>
<p>I  just created an entry in our UI/UK task tracker, I will report back once i have an update.</p>

---

## Post #12 by @pll_llq (2021-09-21 15:25 UTC)

<p>Here’s a link to previous notes on this topic</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5051">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5051" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5051" target="_blank" rel="noopener nofollow ugc">Issue used to capture the list of all pngs found in Slicer code base</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-07-21" data-time="14:21:20" data-timezone="UTC">02:21PM - 21 Jul 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Reference: https://discourse.slicer.org/t/update-slicers-icon-set/12483/11

Li<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">st of png files found in Slicer code base on July 21, 2020:

Generated using

```bash
cd Slicer
for icon in $(find . | ack "\.png$"); do
  name=$(basename $icon); echo -n "| $name"; echo "| \![](https://github.com/Slicer/Slicer/raw/master/$icon) |";
done
```


| Name | Icon |
|----|---|
| SuperLoadableModuleTemplate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/SuperBuildExtensionTemplate/SuperLoadableModuleTemplate/Resources/Icons/SuperLoadableModuleTemplate.png) |
| CLIExtensionTemplate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/CLIExtensionTemplate/CLIExtensionTemplate.png) |
| ScriptedLoadableModuleTemplate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/ScriptedLoadableExtensionTemplate/ScriptedLoadableModuleTemplate/Resources/Icons/ScriptedLoadableModuleTemplate.png) |
| ScriptedLoadableExtensionTemplate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/ScriptedLoadableExtensionTemplate/ScriptedLoadableExtensionTemplate.png) |
| ScriptedSegmentEditorEffectExtensionTemplate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/ScriptedSegmentEditorEffectExtensionTemplate/ScriptedSegmentEditorEffectExtensionTemplate.png) |
| SegmentEditorEffect.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/ScriptedSegmentEditorEffectExtensionTemplate/ScriptedSegmentEditorEffectModuleTemplate/SegmentEditorScriptedSegmentEditorEffectModuleTemplateLib/SegmentEditorEffect.png) |
| EditorExtensionTemplate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/EditorExtensionTemplate/EditorExtensionTemplate.png) |
| EditorEffectTemplate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/EditorExtensionTemplate/EditorEffectTemplate/EditorEffectTemplate.png) |
| LoadableModuleTemplate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/LoadableExtensionTemplate/LoadableModuleTemplate/Resources/Icons/LoadableModuleTemplate.png) |
| LoadableExtensionTemplate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Extensions/Testing/LoadableExtensionTemplate/LoadableExtensionTemplate.png) |
| SubjectHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Docs/_build/html/_images/SubjectHierarchy.png) |
| SlicesCrosshair.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Docs/_build/html/_images/SlicesCrosshair.png) |
| SlicerLoadData.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Docs/_build/html/_images/SlicerLoadData.png) |
| SlicerSave.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Docs/_build/html/_images/SlicerSave.png) |
| SlicerLoadDICOM.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Docs/_build/html/_images/SlicerLoadDICOM.png) |
| file.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Docs/_build/html/_static/file.png) |
| minus.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Docs/_build/html/_static/minus.png) |
| plus.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Docs/_build/html/_static/plus.png) |
| Model.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Models/SubjectHierarchyPlugins/Resources/Icons/Model.png) |
| SlicerModels.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Models/Resources/Icons/Medium/SlicerModels.png) |
| SlicerAddModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Models/Resources/Icons/Medium/SlicerAddModel.png) |
| SlicerModels.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Models/Resources/Icons/Large/SlicerModels.png) |
| SlicerAddModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Models/Resources/Icons/Large/SlicerAddModel.png) |
| SlicerModels.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Models/Resources/Icons/Small/SlicerModels.png) |
| SlicerAddModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Models/Resources/Icons/Small/SlicerAddModel.png) |
| SlicerModels.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Models/Resources/Icons/XLarge/SlicerModels.png) |
| SlicerAddModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Models/Resources/Icons/XLarge/SlicerAddModel.png) |
| GridIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Transforms/Widgets/Resources/Icons/GridIcon.png) |
| ContourIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Transforms/Widgets/Resources/Icons/ContourIcon.png) |
| GlyphIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Transforms/Widgets/Resources/Icons/GlyphIcon.png) |
| Transform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Transforms/SubjectHierarchyPlugins/Resources/Icons/Transform.png) |
| TranslateFirst.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Transforms/Resources/Icons/TranslateFirst.png) |
| Transforms.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Transforms/Resources/Icons/Transforms.png) |
| LoadTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Transforms/Resources/Icons/LoadTransform.png) |
| RotateFirst.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Transforms/Resources/Icons/RotateFirst.png) |
| LoadVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/CropVolume/Resources/Icons/LoadVolume.png) |
| CropVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/CropVolume/Resources/Icons/CropVolume.png) |
| CT-Lung.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Lung.png) |
| DTI-FA-Brain.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/DTI-FA-Brain.png) |
| CT-Muscle.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Muscle.png) |
| CT-X-ray.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-X-ray.png) |
| CT-Air.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Air.png) |
| CT-Bones.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Bones.png) |
| CT-AAA2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-AAA2.png) |
| CT-Chest-Vessels.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Chest-Vessels.png) |
| MR-T2-Brain.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/MR-T2-Brain.png) |
| CT-Cardiac2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Cardiac2.png) |
| CT-Soft-Tissue.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Soft-Tissue.png) |
| CT-Chest-Contrast-Enhanced.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Chest-Contrast-Enhanced.png) |
| CT-Cardiac.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Cardiac.png) |
| CT-Fat.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Fat.png) |
| CT-AAA.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-AAA.png) |
| CT-Coronary-Arteries.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Coronary-Arteries.png) |
| CT-MIP.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-MIP.png) |
| CT-Coronary-Arteries-3.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Coronary-Arteries-3.png) |
| MR-MIP.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/MR-MIP.png) |
| CT-Cropped-Volume-Bone.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Cropped-Volume-Bone.png) |
| CT-Liver-Vasculature.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Liver-Vasculature.png) |
| MR-Angio.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/MR-Angio.png) |
| MR-Default.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/MR-Default.png) |
| VolumeRendering.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/VolumeRendering.png) |
| CT-Coronary-Arteries-2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Coronary-Arteries-2.png) |
| CT-Bone.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Bone.png) |
| CT-Cardiac3.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Cardiac3.png) |
| CT-Pulmonary-Arteries.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/VolumeRendering/Resources/Icons/CT-Pulmonary-Arteries.png) |
| SlicerWWW-Original.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SlicerWelcome/Resources/Images/SlicerWWW-Original.png) |
| WelcomeLogo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SlicerWelcome/Resources/Images/WelcomeLogo.png) |
| SlicerAdvancedGear-Original.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SlicerWelcome/Resources/Images/SlicerAdvancedGear-Original.png) |
| SlicerLoadDicom-Original.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SlicerWelcome/Resources/Images/SlicerLoadDicom-Original.png) |
| SlicerLoadData-Original.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SlicerWelcome/Resources/Images/SlicerLoadData-Original.png) |
| WelcomeSubjectHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SlicerWelcome/Resources/Images/WelcomeSubjectHierarchy.png) |
| SlicerWelcome.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SlicerWelcome/Resources/Icons/SlicerWelcome.png) |
| Chat.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SlicerWelcome/Resources/Icons/Chat.png) |
| Plot.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Plots/SubjectHierarchyPlugins/Resources/Icons/Plot.png) |
| Plots.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Plots/Resources/Icons/Plots.png) |
| SlicerPlotSeries.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Plots/Resources/Icons/XSmall/SlicerPlotSeries.png) |
| SlicerPlotSeries.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Plots/Resources/Icons/Medium/SlicerPlotSeries.png) |
| SlicerPlotSeries.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Plots/Resources/Icons/Large/SlicerPlotSeries.png) |
| SlicerPlotSeries.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Plots/Resources/Icons/Small/SlicerPlotSeries.png) |
| SlicerPlotSeries.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Plots/Resources/Icons/XLarge/SlicerPlotSeries.png) |
| Master|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Testing/Data/Input/Master) |
| Scene|  ![](https://github.com/Slicer/Slicer/raw/master/Scene) |
| View.png|  ![](https://github.com/Slicer/Slicer/raw/master/View.png) |
| AnnotationEditDistance.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationEditDistance.png) |
| AnnotationPointWithArrow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationPointWithArrow.png) |
| AnnotationEditText.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationEditText.png) |
| AnnotationEditROI.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationEditROI.png) |
| AnnotationLock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationLock.png) |
| AnnotationVisibility.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationVisibility.png) |
| AnnotationROIWithArrow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationROIWithArrow.png) |
| SnapshotRestore.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/SnapshotRestore.png) |
| AnnotationOldMousePick.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationOldMousePick.png) |
| AnnotationROI.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationROI.png) |
| AnnotationTextWithArrow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationTextWithArrow.png) |
| AnnotationText.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationText.png) |
| AnnotationDelete.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationDelete.png) |
| LayoutOneUp3DView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/LayoutOneUp3DView.png) |
| LayoutOneUpYellowSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/LayoutOneUpYellowSliceView.png) |
| AnnotationEditAngle.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationEditAngle.png) |
| AnnotationDistance.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationDistance.png) |
| AnnotationResetView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationResetView.png) |
| AnnotationOldMousePlace.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationOldMousePlace.png) |
| AnnotationDistanceWithArrow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationDistanceWithArrow.png) |
| AnnotationSaveScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationSaveScene.png) |
| AnnotationEditBidimensional.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationEditBidimensional.png) |
| AnnotationBidimensionalWithArrow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationBidimensionalWithArrow.png) |
| AnnotationMouseMode.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationMouseMode.png) |
| AnnotationSelectAll.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationSelectAll.png) |
| AnnotationEditSpline.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationEditSpline.png) |
| ViewCamera.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/ViewCamera.png) |
| AnnotationAddPointList.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationAddPointList.png) |
| AnnotationDeselectAll.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationDeselectAll.png) |
| AnnotationBidimensional.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationBidimensional.png) |
| AnnotationCancel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationCancel.png) |
| AnnotationUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationUnlock.png) |
| AnnotationOkDone.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationOkDone.png) |
| AnnotationScreenShot.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationScreenShot.png) |
| AnnotationPrint.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationPrint.png) |
| AnnotationPause.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationPause.png) |
| AnnotationSpline.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationSpline.png) |
| AnnotationInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationInvisible.png) |
| AnnotationVolumesModule.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationVolumesModule.png) |
| AnnotationMouseModePick.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationMouseModePick.png) |
| AnnotationEditNote.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationEditNote.png) |
| LayoutOneUpGreenSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/LayoutOneUpGreenSliceView.png) |
| AnnotationVolumeInformationExtractor.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationVolumeInformationExtractor.png) |
| AnnotationSaveAnnotations.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationSaveAnnotations.png) |
| Annotation.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/Annotation.png) |
| AnnotationMoveUp.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationMoveUp.png) |
| AnnotationPoints.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationPoints.png) |
| AnnotationInformation.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationInformation.png) |
| AnnotationEditPoint.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationEditPoint.png) |
| AnnotationMouseModeInspect.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationMouseModeInspect.png) |
| AnnotationReport.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationReport.png) |
| AnnotationAngleWithArrow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationAngleWithArrow.png) |
| AnnotationPolyline.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationPolyline.png) |
| AnnotationMouseModeWindowLevel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationMouseModeWindowLevel.png) |
| AnnotationAngle.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationAngle.png) |
| AnnotationMouseModePlace.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationMouseModePlace.png) |
| AnnotationPlayForward.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationPlayForward.png) |
| AnnotationLine.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationLine.png) |
| AnnotationPoint.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationPoint.png) |
| LayoutOneUpRedSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/LayoutOneUpRedSliceView.png) |
| AnnotationEditPolyline.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationEditPolyline.png) |
| AnnotationNote.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationNote.png) |
| AnnotationMoveDown.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationMoveDown.png) |
| upennpalmtree.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/upennpalmtree.png) |
| AnnotationMouseModeTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationMouseModeTransform.png) |
| AnnotationLayout.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/AnnotationLayout.png) |
| UPenn_logo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Annotations/Resources/Icons/UPenn_logo.png) |
| ResetProperty.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Terminologies/Widgets/Resources/Icons/ResetProperty.png) |
| Warning.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/Warning.png) |
| Patient.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/Patient.png) |
| Folder.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/Folder.png) |
| Study.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/Study.png) |
| Unknown.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/Unknown.png) |
| NoTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/NoTransform.png) |
| Chart.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/Chart.png) |
| LinearTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/LinearTransform.png) |
| Transform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/Transform.png) |
| FolderTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/FolderTransform.png) |
| Colors.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/Colors.png) |
| DeformableTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Widgets/Resources/Icons/DeformableTransform.png) |
| SubjectHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Resources/Icons/SubjectHierarchy.png) |
| Help.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SubjectHierarchy/Resources/Icons/Help.png) |
| Table.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Tables/SubjectHierarchyPlugins/Resources/Icons/Table.png) |
| Tables.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Tables/Resources/Icons/Tables.png) |
| MarkupsFiducial.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/SubjectHierarchyPlugins/Resources/Icons/MarkupsFiducial.png) |
| MarkupsLine.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/SubjectHierarchyPlugins/Resources/Icons/MarkupsLine.png) |
| MarkupsOpenCurve.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/SubjectHierarchyPlugins/Resources/Icons/MarkupsOpenCurve.png) |
| MarkupsPlane.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/SubjectHierarchyPlugins/Resources/Icons/MarkupsPlane.png) |
| MarkupsClosedCurve.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/SubjectHierarchyPlugins/Resources/Icons/MarkupsClosedCurve.png) |
| MarkupsAngle.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/SubjectHierarchyPlugins/Resources/Icons/MarkupsAngle.png) |
| Ellipsis.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/Ellipsis.png) |
| MarkupsAngleMouseModePlace.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsAngleMouseModePlace.png) |
| MarkupsLineMouseModePlace.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsLineMouseModePlace.png) |
| MarkupsListUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsListUnlock.png) |
| MarkupsPlaneMouseModePlace.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsPlaneMouseModePlace.png) |
| MarkupsMouseModePlace.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsMouseModePlace.png) |
| MarkupsMoveDown.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsMoveDown.png) |
| MarkupsDeleteAllRows.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsDeleteAllRows.png) |
| MarkupsSelectedOrUnselected.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsSelectedOrUnselected.png) |
| MarkupsCurveMouseModePlace.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsCurveMouseModePlace.png) |
| MarkupsLineMouseModePlaceAdd.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsLineMouseModePlaceAdd.png) |
| Markups.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/Markups.png) |
| MarkupsUnselected.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsUnselected.png) |
| MarkupsDeselectAll.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsDeselectAll.png) |
| MarkupsClosedCurveMouseModePlace.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsClosedCurveMouseModePlace.png) |
| MarkupsAddFiducial.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsAddFiducial.png) |
| MarkupsSelected.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsSelected.png) |
| MarkupsAngleMouseModePlaceAdd.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsAngleMouseModePlaceAdd.png) |
| MarkupsMoveUp.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsMoveUp.png) |
| MarkupsMouseModePlaceAdd.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsMouseModePlaceAdd.png) |
| MarkupsListLock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsListLock.png) |
| MarkupsClosedCurveMouseModePlaceAdd.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsClosedCurveMouseModePlaceAdd.png) |
| MarkupsCurveMouseModePlaceAdd.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsCurveMouseModePlaceAdd.png) |
| MarkupsPlaneMouseModePlaceAdd.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsPlaneMouseModePlaceAdd.png) |
| MarkupsDeleteSelectedRows.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsDeleteSelectedRows.png) |
| MarkupsDelete.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Markups/Resources/Icons/MarkupsDelete.png) |
| Reformat.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Reformat/Resources/Icons/Reformat.png) |
| ViewControllers.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/ViewControllers/Resources/Icons/ViewControllers.png) |
| Cameras.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Cameras/Resources/Icons/Cameras.png) |
| WindowLevelPreset-Abdomen.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Widgets/Resources/Icons/WindowLevelPreset-Abdomen.png) |
| WindowLevelPreset-Lung.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Widgets/Resources/Icons/WindowLevelPreset-Lung.png) |
| WindowLevelPreset-Brain.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Widgets/Resources/Icons/WindowLevelPreset-Brain.png) |
| WindowLevelPreset-CT-air.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Widgets/Resources/Icons/WindowLevelPreset-CT-air.png) |
| WindowLevelPreset-PET.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Widgets/Resources/Icons/WindowLevelPreset-PET.png) |
| WindowLevelPreset-CT-bone.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Widgets/Resources/Icons/WindowLevelPreset-CT-bone.png) |
| WindowLevelPreset-DTI.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Widgets/Resources/Icons/WindowLevelPreset-DTI.png) |
| Labelmap.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/SubjectHierarchyPlugins/Resources/Icons/Labelmap.png) |
| VolumeVisibilityOn.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/SubjectHierarchyPlugins/Resources/Icons/VolumeVisibilityOn.png) |
| Volume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/SubjectHierarchyPlugins/Resources/Icons/Volume.png) |
| DiffusionTensorVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/SubjectHierarchyPlugins/Resources/Icons/DiffusionTensorVolume.png) |
| VolumeVisibilityOff.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/SubjectHierarchyPlugins/Resources/Icons/VolumeVisibilityOff.png) |
| SlicerAddVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/Medium/SlicerAddVolume.png) |
| SlicerVolumes.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/Medium/SlicerVolumes.png) |
| SlicerAddVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/Large/SlicerAddVolume.png) |
| SlicerVolumes.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/Large/SlicerVolumes.png) |
| SlicerAddVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/Small/SlicerAddVolume.png) |
| SlicerVolumes.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/Small/SlicerVolumes.png) |
| Volumes.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/Volumes.png) |
| LoadVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/LoadVolume.png) |
| SlicerAddVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/XLarge/SlicerAddVolume.png) |
| SlicerVolumes.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Volumes/Resources/Icons/XLarge/SlicerVolumes.png) |
| pqVcrFirst24.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Widgets/Resources/Icons/pqVcrFirst24.png) |
| pqVcrBack24.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Widgets/Resources/Icons/pqVcrBack24.png) |
| VcrRecord16.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Widgets/Resources/Icons/VcrRecord16.png) |
| pqVcrLast24.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Widgets/Resources/Icons/pqVcrLast24.png) |
| pqCamera24.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Widgets/Resources/Icons/pqCamera24.png) |
| pqVcrLoop24.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Widgets/Resources/Icons/pqVcrLoop24.png) |
| pqVcrPlay24.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Widgets/Resources/Icons/pqVcrPlay24.png) |
| pqVcrForward24.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Widgets/Resources/Icons/pqVcrForward24.png) |
| pqVcrPause24.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Widgets/Resources/Icons/pqVcrPause24.png) |
| DataNodeHidden.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Resources/Icons/DataNodeHidden.png) |
| Sequences.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Resources/Icons/Sequences.png) |
| DataNodeUnhidden.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Resources/Icons/DataNodeUnhidden.png) |
| DataNodeDelete.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Resources/Icons/DataNodeDelete.png) |
| Remove.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Resources/Icons/Remove.png) |
| Add.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Sequences/Resources/Icons/Add.png) |
| SlicerCopyColor.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Colors/Resources/Icons/SlicerCopyColor.png) |
| Colors.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Colors/Resources/Icons/Colors.png) |
| Text.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Texts/SubjectHierarchyPlugins/Resources/Icons/Text.png) |
| SlicerTexts.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Texts/Resources/Icons/SlicerTexts.png) |
| Completed.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/Completed.png) |
| NotStarted.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/NotStarted.png) |
| ClearSelection.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/ClearSelection.png) |
| Master.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/Master.png) |
| Edit.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/Edit.png) |
| InProgress.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/InProgress.png) |
| Present.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/Present.png) |
| MakeModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/MakeModel.png) |
| SlicerRotateWarning.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/SlicerRotateWarning.png) |
| Remove.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/Remove.png) |
| Flagged.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/Flagged.png) |
| Help.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/Help.png) |
| Add.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Widgets/Resources/Icons/Add.png) |
| Segment.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/SubjectHierarchyPlugins/Resources/Icons/Segment.png) |
| Segmentation.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/SubjectHierarchyPlugins/Resources/Icons/Segmentation.png) |
| AddLabelmap.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Resources/Icons/AddLabelmap.png) |
| Segmentations.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/Resources/Icons/Segmentations.png) |
| FillBetweenSlices.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/FillBetweenSlices.png) |
| Hollow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/Hollow.png) |
| Logical.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/Logical.png) |
| Smoothing.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/Smoothing.png) |
| GrowFromSeeds.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/GrowFromSeeds.png) |
| LevelTracing.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/LevelTracing.png) |
| Margin.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/Margin.png) |
| Threshold.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/Threshold.png) |
| Erode.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/Erode.png) |
| Draw.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/Draw.png) |
| Islands.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Python/Resources/Icons/Islands.png) |
| Erase.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Resources/Icons/Erase.png) |
| Rectangle.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Resources/Icons/Rectangle.png) |
| CursorBaseArrow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Resources/Icons/CursorBaseArrow.png) |
| NullEffect.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Resources/Icons/NullEffect.png) |
| Paint.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Segmentations/EditorEffects/Resources/Icons/Paint.png) |
| SceneView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/SubjectHierarchyPlugins/Resources/Icons/SceneView.png) |
| Layout3DView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/Layout3DView.png) |
| LayoutGreenSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/LayoutGreenSliceView.png) |
| Delete.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/Delete.png) |
| MoveUp.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/MoveUp.png) |
| LayoutYellowSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/LayoutYellowSliceView.png) |
| Camera.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/Camera.png) |
| Restore.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/Restore.png) |
| MoveDown.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/MoveDown.png) |
| SelectCameras.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/SelectCameras.png) |
| LayoutFull.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/LayoutFull.png) |
| LayoutRedSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/SceneViews/Resources/Icons/LayoutRedSliceView.png) |
| SubjectHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Data/Resources/Icons/SubjectHierarchy.png) |
| Data.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Loadable/Data/Resources/Icons/Data.png) |
| ITKLogo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/CLI/ImageData/ITKLogo.png) |
| MITLogo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/CLI/ImageData/MITLogo.png) |
| BillsLogo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/CLI/ImageData/BillsLogo.png) |
| MIT_NAMIC_Logo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/CLI/ImageData/MIT_NAMIC_Logo.png) |
| MIT_NAMIC_PNL_Logo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/CLI/ImageData/MIT_NAMIC_PNL_Logo.png) |
| NAMICLogo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/CLI/ImageData/NAMICLogo.png) |
| ITKLogo16x16.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/CLI/ImageData/ITKLogo16x16.png) |
| logo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/CLI/ExpertAutomatedRegistration/logo.png) |
| PreDentalSurgery.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/PreDentalSurgery.png) |
| DTIVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/DTIVolume.png) |
| CTChest.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/CTChest.png) |
| MRBrainTumor2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/MRBrainTumor2.png) |
| BaselineVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/BaselineVolume.png) |
| CTBrain.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/CTBrain.png) |
| MRHead.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/MRHead.png) |
| dwi.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/dwi.png) |
| CTPCardioSeq.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/CTPCardioSeq.png) |
| Panoramix-cropped.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/Panoramix-cropped.png) |
| CTCardioSeq.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/CTCardioSeq.png) |
| MRBrainTumor1.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/MRBrainTumor1.png) |
| DTIBrain.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/DTIBrain.png) |
| MRProstate.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/MRProstate.png) |
| CTACardio.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/CTACardio.png) |
| TinyPatient.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SampleData/Resources/Icons/TinyPatient.png) |
| ExtensionWizard.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/ExtensionWizard/ExtensionWizardLib/Icons/XSmall/ExtensionWizard.png) |
| ExtensionWizard.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/ExtensionWizard/ExtensionWizardLib/Icons/Medium/ExtensionWizard.png) |
| ExtensionWizard.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/ExtensionWizard/ExtensionWizardLib/Icons/ExtensionWizard.png) |
| ExtensionWizard.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/ExtensionWizard/ExtensionWizardLib/Icons/XLarge/ExtensionWizard.png) |
| SegmentEditor.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SegmentEditor/Resources/Icons/SegmentEditor.png) |
| SegmentStatistics.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/SegmentStatistics/Resources/Icons/SegmentStatistics.png) |
| DefaultTool.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/DefaultTool.png) |
| SaveIsland.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/SaveIsland.png) |
| IdentifyIslands.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/IdentifyIslands.png) |
| FastMarchingEffect.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/FastMarchingEffect.png) |
| RemoveIslands.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/RemoveIslands.png) |
| NextCheckPoint.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/NextCheckPoint.png) |
| LevelTracing.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/LevelTracing.png) |
| Paint.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/Paint.png) |
| DilateLabel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/DilateLabel.png) |
| Threshold.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/Threshold.png) |
| GrowCutSegment.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/GrowCutSegment.png) |
| WandEffect.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/WandEffect.png) |
| MakeModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/MakeModel.png) |
| PreviousCheckPoint.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/PreviousCheckPoint.png) |
| ChangeIsland.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/ChangeIsland.png) |
| ErodeLabel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/ErodeLabel.png) |
| ToolbarEditorToolbox.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/ToolbarEditorToolbox.png) |
| WatershedFromMarkerEffect.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/WatershedFromMarkerEffect.png) |
| ImplicitRectangle.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/ImplicitRectangle.png) |
| ChangeLabel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/ChangeLabel.png) |
| EraseLabel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/EraseLabel.png) |
| Draw.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/EditorLib/Resources/Icons/Draw.png) |
| DICOMPatcher.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/DICOMPatcher/Resources/Icons/DICOMPatcher.png) |
| SlicerWatermark.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/ScreenCapture/Resources/SlicerWatermark.png) |
| ScreenCapture.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/ScreenCapture/Resources/Icons/ScreenCapture.png) |
| CropVolumeSequence.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/CropVolumeSequence/Resources/Icons/CropVolumeSequence.png) |
| SlicerAdvancedGear-Small.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/DataProbe/Resources/Icons/SlicerAdvancedGear-Small.png) |
| LabelStatistics.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Modules/Scripted/LabelStatistics/Resources/Icons/LabelStatistics.png) |
| TemplateKey.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Utilities/Templates/Extensions/Default/TemplateKey.png) |
| TemplateKeyEffect.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Utilities/Templates/Modules/ScriptedEditorEffect/TemplateKeyEffect.png) |
| TemplateKey.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Utilities/Templates/Modules/Loadable/Resources/Icons/TemplateKey.png) |
| SegmentEditorEffect.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Utilities/Templates/Modules/ScriptedSegmentEditorEffect/SegmentEditorTemplateKeyLib/SegmentEditorEffect.png) |
| TemplateKey.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Utilities/Templates/Modules/Scripted/Resources/Icons/TemplateKey.png) |
| ClippingUnion.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ClippingUnion.png) |
| LayoutConvetionalQuantitativeView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutConvetionalQuantitativeView.png) |
| SnapshotDelete.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SnapshotDelete.png) |
| GreenSpaceNegative.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/GreenSpaceNegative.png) |
| SlicerAutomaticSliceSpacing.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicerAutomaticSliceSpacing.png) |
| ViewFeaturesVisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewFeaturesVisible.png) |
| LayoutOneUpQuantitativeView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutOneUpQuantitativeView.png) |
| HotLinkOn.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/HotLinkOn.png) |
| PushPinIn.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/PushPinIn.png) |
| LayoutFourByThreeSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutFourByThreeSliceView.png) |
| SnapshotRestore.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SnapshotRestore.png) |
| ClippingIntersection.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ClippingIntersection.png) |
| ViewCenter.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewCenter.png) |
| VisibleOn.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/VisibleOn.png) |
| SliceViewerOR.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceViewerOR.png) |
| tintWarmTint1.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/tintWarmTint1.png) |
| tintCoolTint1.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/tintCoolTint1.png) |
| tintWarmTint2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/tintWarmTint2.png) |
| discreteOcean.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteOcean.png) |
| discreteInvertedGrey.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteInvertedGrey.png) |
| discreteCool3.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteCool3.png) |
| discreteYellow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteYellow.png) |
| discreteCyan.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteCyan.png) |
| labelsPelvisColor.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/labelsPelvisColor.png) |
| shadeCoolShade2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/shadeCoolShade2.png) |
| shadeCoolShade1.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/shadeCoolShade1.png) |
| discreteDesert.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteDesert.png) |
| shadeWarmShade2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/shadeWarmShade2.png) |
| tintCoolTint2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/tintCoolTint2.png) |
| discreteCool2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteCool2.png) |
| shadeWarmShade3.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/shadeWarmShade3.png) |
| discreteReverseRainbow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteReverseRainbow.png) |
| shadeCoolShade3.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/shadeCoolShade3.png) |
| petPETHeat.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/petPETHeat.png) |
| genericColors.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/genericColors.png) |
| shadeWarmShade1.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/shadeWarmShade1.png) |
| tintCoolTint3.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/tintCoolTint3.png) |
| blankLUT.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/blankLUT.png) |
| tintWarmTint3.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/tintWarmTint3.png) |
| discreteRandomIntegers.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteRandomIntegers.png) |
| discreteFullRainbow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteFullRainbow.png) |
| petPETRainbow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/petPETRainbow.png) |
| genericAnatomyColors.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/genericAnatomyColors.png) |
| SPL-BrainAtlas-ColorFile.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/SPL-BrainAtlas-ColorFile.png) |
| discreteWarm2.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteWarm2.png) |
| discreteLabels.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteLabels.png) |
| discreteIron.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteIron.png) |
| slicerBrainLUT2010.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/slicerBrainLUT2010.png) |
| discretefMRIPA.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discretefMRIPA.png) |
| cartilegeMIdGEMRIC-3T.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/cartilegeMIdGEMRIC-3T.png) |
| slicerShortLUT.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/slicerShortLUT.png) |
| petPETMIP.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/petPETMIP.png) |
| discreteWarm3.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteWarm3.png) |
| discreteMagenta.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteMagenta.png) |
| discreteBlue.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteBlue.png) |
| discreteRandom.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteRandom.png) |
| labelsCustom.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/labelsCustom.png) |
| discreteGrey.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteGrey.png) |
| discreteGreen.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteGreen.png) |
| discreteCool1.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteCool1.png) |
| discreteWarm1.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteWarm1.png) |
| cartilegeMRIdGEMRIC-1.5T.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/cartilegeMRIdGEMRIC-1.5T.png) |
| AbdomenColors.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/AbdomenColors.png) |
| discreteRed.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteRed.png) |
| discreteRainbow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discreteRainbow.png) |
| discretefMRI.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/discretefMRI.png) |
| labelsNonSemantic.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LUTs/labelsNonSemantic.png) |
| SlicesComposite.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesComposite.png) |
| GreenSpacePositive.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/GreenSpacePositive.png) |
| column_add.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/column_add.png) |
| SlicerManualSliceSpacing.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicerManualSliceSpacing.png) |
| row_delete.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/row_delete.png) |
| LayoutOneUp3DView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutOneUp3DView.png) |
| LayoutOneUpYellowSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutOneUpYellowSliceView.png) |
| LayoutConventionalWidescreenView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutConventionalWidescreenView.png) |
| SlicesFeaturesVisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesFeaturesVisible.png) |
| LayoutFourUpTableView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutFourUpTableView.png) |
| LayoutTabbed3DView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutTabbed3DView.png) |
| SliceWidgetOff.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceWidgetOff.png) |
| SlicesLabelOutlineAndFill.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesLabelOutlineAndFill.png) |
| LayoutCompareView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutCompareView.png) |
| ViewOrtho.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewOrtho.png) |
| ViewAxis.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewAxis.png) |
| Ruler.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/Ruler.png) |
| row_header_lock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/row_header_lock.png) |
| LayoutTabbedSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutTabbedSliceView.png) |
| LayoutFourUpView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutFourUpView.png) |
| ViewCamera.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewCamera.png) |
| ViewFPS.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewFPS.png) |
| SliceWidgetOn.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceWidgetOn.png) |
| LinkOn.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LinkOn.png) |
| ViewRock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewRock.png) |
| SlicesLabelOpacity.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesLabelOpacity.png) |
| LayoutLightboxView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutLightboxView.png) |
| SliceInterpolationOff.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceInterpolationOff.png) |
| LayoutTwoOverTwoView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutTwoOverTwoView.png) |
| ViewPitch.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewPitch.png) |
| SlicesToggleFgBg.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesToggleFgBg.png) |
| ViewRoll.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewRoll.png) |
| SlicesFadeToBG.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesFadeToBG.png) |
| ViewStereo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewStereo.png) |
| SlicesCrosshair.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesCrosshair.png) |
| RedSpacePositive.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/RedSpacePositive.png) |
| LayoutDual3DView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutDual3DView.png) |
| LayoutThreeByThreeSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutThreeByThreeSliceView.png) |
| SlicesFitToWindow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesFitToWindow.png) |
| SliceViewerBG.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceViewerBG.png) |
| SlicesFieldOfView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesFieldOfView.png) |
| SlicesAnnotation.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesAnnotation.png) |
| VisiblePartially.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/VisiblePartially.png) |
| ViewYaw.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewYaw.png) |
| column_header_lock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/column_header_lock.png) |
| row_add.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/row_add.png) |
| SliceViewerFG.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceViewerFG.png) |
| ViewZoomOut.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewZoomOut.png) |
| VisibleOrInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/VisibleOrInvisible.png) |
| LayoutThreeOverThreeView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutThreeOverThreeView.png) |
| SlicesLabelNoOutline.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesLabelNoOutline.png) |
| YellowSpaceNegative.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/YellowSpaceNegative.png) |
| LayoutOneUpGreenSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutOneUpGreenSliceView.png) |
| SlicesWinLevThreshCol.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesWinLevThreshCol.png) |
| ViewCapture.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewCapture.png) |
| SliceViewerSEG.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceViewerSEG.png) |
| RedSpaceNegative.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/RedSpaceNegative.png) |
| LayoutTriple3DView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutTriple3DView.png) |
| LayoutSideBySideCompareView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutSideBySideCompareView.png) |
| SlicerRotateToPixelSpace.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicerRotateToPixelSpace.png) |
| SlicesLabelFill.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesLabelFill.png) |
| SlicesSpatialUnit.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesSpatialUnit.png) |
| YellowSpacePositive.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/YellowSpacePositive.png) |
| ViewSpin.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewSpin.png) |
| LayoutThreeOverThreeQuantitativeView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutThreeOverThreeQuantitativeView.png) |
| LayoutChooseView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutChooseView.png) |
| Layout3DTableView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/Layout3DTableView.png) |
| LayoutFourByTwoSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutFourByTwoSliceView.png) |
| OrientationMarker.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/OrientationMarker.png) |
| LayoutFourUpQuantitativeTableView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutFourUpQuantitativeTableView.png) |
| PushPinOut.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/PushPinOut.png) |
| LayoutFourOverFourView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutFourOverFourView.png) |
| ViewPerspective.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewPerspective.png) |
| SliceInterpolationOn.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceInterpolationOn.png) |
| LayoutFiveByTwoSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutFiveByTwoSliceView.png) |
| ViewZoomIn.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewZoomIn.png) |
| SlicesLabelOutline.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesLabelOutline.png) |
| column_delete.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/column_delete.png) |
| LayoutCompareViewGrid.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutCompareViewGrid.png) |
| LayoutFourUpQuantitativeView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutFourUpQuantitativeView.png) |
| LayoutSideBySideView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutSideBySideView.png) |
| SliceMoreOptions.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceMoreOptions.png) |
| SlicesFadeToFG.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SlicesFadeToFG.png) |
| LayoutConventionalView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutConventionalView.png) |
| LayoutOneUpRedSliceView.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LayoutOneUpRedSliceView.png) |
| ViewCameraSelect.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/ViewCameraSelect.png) |
| LinkOff.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/LinkOff.png) |
| VisibleOff.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/VisibleOff.png) |
| SliceViewerLB.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/Widgets/Resources/Icons/SliceViewerLB.png) |
| vtkMRMLCameraDisplayableManagerTest1.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/DisplayableManager/Testing/Baseline/vtkMRMLCameraDisplayableManagerTest1.png) |
| vtkMRMLModelDisplayableManagerTest.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/DisplayableManager/Testing/Baseline/vtkMRMLModelDisplayableManagerTest.png) |
| vtkMRMLThreeDReformatDisplayableManagerTest1.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Libs/MRML/DisplayableManager/Testing/Baseline/vtkMRMLThreeDReformatDisplayableManagerTest1.png) |
| 3DSlicer-DesktopIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/3DSlicer-DesktopIcon.png) |
| NAMIC.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/NAMIC.png) |
| TATRC.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/TATRC.png) |
| CIMIT.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/CIMIT.png) |
| CTSC.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/CTSC.png) |
| NCI.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/NCI.png) |
| CISST.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/CISST.png) |
| QIICR.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/QIICR.png) |
| CSAIL.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/CSAIL.png) |
| BrainScienceFoundation.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/BrainScienceFoundation.png) |
| NITRC.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/NITRC.png) |
| Bills.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/Bills.png) |
| MIT_NAMIC_PNL.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/MIT_NAMIC_PNL.png) |
| NIH.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/NIH.png) |
| Gatech.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/Gatech.png) |
| BIRN-NoText.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/BIRN-NoText.png) |
| SPL.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/SPL.png) |
| Geresearch.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/Geresearch.png) |
| NIBIB.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/NIBIB.png) |
| NAC.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/NAC.png) |
| HCNR.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/HCNR.png) |
| MIT.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/MIT.png) |
| NCRR.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/NCRR.png) |
| SCI.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/SCI.png) |
| NCIGT.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/NCIGT.png) |
| MC.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/MC.png) |
| Kitware.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/Kitware.png) |
| ITK.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/ITK.png) |
| BIRN.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/BIRN.png) |
| PNL.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/PNL.png) |
| Isomics.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/Logos/Isomics.png) |
| 3DSlicerLogo-app-icon-centered.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Resources/3DSlicerLogo-app-icon-centered.png) |
| Slicer-Logo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Applications/SlicerApp/Resources/Images/Slicer-Logo.png) |
| Slicer-SplashScreen.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png) |
| Slicer-ModulePanelLogo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Applications/SlicerApp/Resources/Images/Slicer-ModulePanelLogo.png) |
| Slicer-DesktopIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Applications/SlicerApp/Resources/Icons/Medium/Slicer-DesktopIcon.png) |
| Slicer-DesktopIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Applications/SlicerApp/Resources/Icons/Large/Slicer-DesktopIcon.png) |
| Slicer-DesktopIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Applications/SlicerApp/Resources/Icons/Small/Slicer-DesktopIcon.png) |
| Slicer-DesktopIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Applications/SlicerApp/Resources/Icons/XXLarge/Slicer-DesktopIcon.png) |
| Slicer-DesktopIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Applications/SlicerApp/Resources/Icons/XLarge/Slicer-DesktopIcon.png) |
| AnnotationPointWithArrow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Testing/Cxx/Resources/Icons/AnnotationPointWithArrow.png) |
| AnnotationDistanceWithArrow.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Testing/Cxx/Resources/Icons/AnnotationDistanceWithArrow.png) |
| SaveScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/SaveScene.png) |
| TreeClose.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/TreeClose.png) |
| MouseSinglePlaceMode.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/MouseSinglePlaceMode.png) |
| ModuleHistory.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/ModuleHistory.png) |
| MousePlaceMode.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/MousePlaceMode.png) |
| SlicerEditCut.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerEditCut.png) |
| SlicerEditCopy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerEditCopy.png) |
| SlicerUndo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerUndo.png) |
| SlicerHome.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerHome.png) |
| SlicerDownloadMRHead.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerDownloadMRHead.png) |
| SlicerEditPaste.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerEditPaste.png) |
| SlicerInteractivePlotting.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerInteractivePlotting.png) |
| SlicerRedo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerRedo.png) |
| SlicerCheckForUpdates.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerCheckForUpdates.png) |
| SlicerConfigure.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XSmall/SlicerConfigure.png) |
| SlicerDataBundle.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerDataBundle.png) |
| SlicerEditCut.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerEditCut.png) |
| SlicerVisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerVisible.png) |
| SlicerLoadScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerLoadScene.png) |
| SlicerVisibleInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerVisibleInvisible.png) |
| SlicerLock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerLock.png) |
| SlicerLoadVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerLoadVolume.png) |
| SlicerAddData.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerAddData.png) |
| SlicerLockUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerLockUnlock.png) |
| SlicerInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerInvisible.png) |
| SlicerEditCopy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerEditCopy.png) |
| SlicerAddScalarOverlay.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerAddScalarOverlay.png) |
| SlicerAddScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerAddScene.png) |
| SlicerUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerUnlock.png) |
| SlicerCloseScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerCloseScene.png) |
| SlicerAddTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerAddTransform.png) |
| SlicerAddVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerAddVolume.png) |
| SlicerUndo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerUndo.png) |
| SlicerLoadData.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerLoadData.png) |
| SlicerAddHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerAddHierarchy.png) |
| SlicerHome.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerHome.png) |
| SlicerDatabase.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerDatabase.png) |
| SlicerAddColorLUT.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerAddColorLUT.png) |
| SlicerAddFiducialList.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerAddFiducialList.png) |
| SlicerDownloadMRHead.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerDownloadMRHead.png) |
| SlicerAddModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerAddModel.png) |
| SlicerSave.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerSave.png) |
| SlicerHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerHierarchy.png) |
| SlicerEditPaste.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerEditPaste.png) |
| SlicerInteractivePlotting.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerInteractivePlotting.png) |
| SlicerRedo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerRedo.png) |
| SlicerCheckForUpdates.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerCheckForUpdates.png) |
| SlicerLoadDICOM.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerLoadDICOM.png) |
| SlicerImportDICOM.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerImportDICOM.png) |
| SlicerConfigure.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Medium/SlicerConfigure.png) |
| MouseRotateMode.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/MouseRotateMode.png) |
| ExtensionDefaultIcon.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/ExtensionDefaultIcon.png) |
| SlicerEditCut.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerEditCut.png) |
| SlicerVisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerVisible.png) |
| SlicerLoadScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerLoadScene.png) |
| SlicerVisibleInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerVisibleInvisible.png) |
| SlicerLock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerLock.png) |
| SlicerAddData.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerAddData.png) |
| SlicerLockUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerLockUnlock.png) |
| SlicerInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerInvisible.png) |
| SlicerEditCopy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerEditCopy.png) |
| SlicerAddScalarOverlay.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerAddScalarOverlay.png) |
| SlicerAddScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerAddScene.png) |
| SlicerUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerUnlock.png) |
| SlicerAddTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerAddTransform.png) |
| SlicerAddVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerAddVolume.png) |
| SlicerUndo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerUndo.png) |
| SlicerAddHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerAddHierarchy.png) |
| SlicerHome.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerHome.png) |
| SlicerAddColorLUT.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerAddColorLUT.png) |
| SlicerAddFiducialList.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerAddFiducialList.png) |
| SlicerDownloadMRHead.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerDownloadMRHead.png) |
| SlicerAddModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerAddModel.png) |
| SlicerHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerHierarchy.png) |
| SlicerEditPaste.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerEditPaste.png) |
| SlicerInteractivePlotting.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerInteractivePlotting.png) |
| SlicerRedo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerRedo.png) |
| SlicerCheckForUpdates.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerCheckForUpdates.png) |
| SlicerConfigure.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Large/SlicerConfigure.png) |
| MouseViewTransformMode.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/MouseViewTransformMode.png) |
| SlicerDataBundle.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerDataBundle.png) |
| SlicerEditCut.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerEditCut.png) |
| SlicerVisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerVisible.png) |
| SlicerLoadScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerLoadScene.png) |
| SlicerVisibleInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerVisibleInvisible.png) |
| SlicerLock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerLock.png) |
| SlicerAddData.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerAddData.png) |
| SlicerLockUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerLockUnlock.png) |
| SlicerInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerInvisible.png) |
| SlicerEditCopy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerEditCopy.png) |
| SlicerAddScalarOverlay.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerAddScalarOverlay.png) |
| SlicerAddScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerAddScene.png) |
| SlicerUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerUnlock.png) |
| SlicerCloseScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerCloseScene.png) |
| SlicerAddTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerAddTransform.png) |
| SlicerAddVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerAddVolume.png) |
| SlicerUndo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerUndo.png) |
| SlicerLoadData.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerLoadData.png) |
| SlicerAddHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerAddHierarchy.png) |
| SlicerHome.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerHome.png) |
| SlicerAddColorLUT.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerAddColorLUT.png) |
| SlicerAddFiducialList.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerAddFiducialList.png) |
| SlicerAddModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerAddModel.png) |
| SlicerSave.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerSave.png) |
| SlicerHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerHierarchy.png) |
| SlicerEditPaste.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerEditPaste.png) |
| SlicerInfoRight.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerInfoRight.png) |
| SlicerInteractivePlotting.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerInteractivePlotting.png) |
| SlicerRedo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerRedo.png) |
| SlicerCheckForUpdates.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerCheckForUpdates.png) |
| SlicerInfoLeft.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerInfoLeft.png) |
| SlicerLoadDICOM.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerLoadDICOM.png) |
| SlicerConfigure.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Small/SlicerConfigure.png) |
| MousePickMode.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/MousePickMode.png) |
| Go.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Go.png) |
| SlicerEditCut.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerEditCut.png) |
| SlicerVisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerVisible.png) |
| SlicerLoadScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerLoadScene.png) |
| SlicerVisibleInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerVisibleInvisible.png) |
| SlicerLock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerLock.png) |
| SlicerAddData.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerAddData.png) |
| SlicerLockUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerLockUnlock.png) |
| SlicerInvisible.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerInvisible.png) |
| SlicerEditCopy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerEditCopy.png) |
| SlicerAddScalarOverlay.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerAddScalarOverlay.png) |
| SlicerAddScene.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerAddScene.png) |
| SlicerUnlock.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerUnlock.png) |
| SlicerAddTransform.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerAddTransform.png) |
| SlicerAddVolume.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerAddVolume.png) |
| SlicerUndo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerUndo.png) |
| SlicerAddHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerAddHierarchy.png) |
| SlicerHome.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerHome.png) |
| SlicerAddColorLUT.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerAddColorLUT.png) |
| SlicerAddFiducialList.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerAddFiducialList.png) |
| SlicerDownloadMRHead.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerDownloadMRHead.png) |
| SlicerAddModel.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerAddModel.png) |
| SlicerHierarchy.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerHierarchy.png) |
| SlicerEditPaste.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerEditPaste.png) |
| SlicerInteractivePlotting.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerInteractivePlotting.png) |
| SlicerRedo.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerRedo.png) |
| SlicerCheckForUpdates.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerCheckForUpdates.png) |
| SlicerConfigure.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/XLarge/SlicerConfigure.png) |
| MouseWindowLevelMode.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/MouseWindowLevelMode.png) |
| TreeOpen.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/TreeOpen.png) |
| CheckModified.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/CheckModified.png) |
| Extension.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Extension.png) |
| DownloadExtension.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/DownloadExtension.png) |
| MouseSinglePickMode.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/MouseSinglePickMode.png) |
| Search.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/Search.png) |
| CheckModifiedData.png|  ![](https://github.com/Slicer/Slicer/raw/master/./Base/QTGUI/Resources/Icons/CheckModifiedData.png) |</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #13 by @lassoan (2021-09-22 17:56 UTC)

<p>I’ve found a way to fix Slicer’s blurred icons on high-resolution screens (which is nowadays most laptop screens and many desktop monitors, too). However, for many icons there is no high-resolution versions, so we would need to re-draw many of them. If we spend time with re-drawing icons, it would make sense to make them looking more consistent, more moder, and dark-theme-friendly.</p>
<p>I’ve created a Labs page for describing this project: <a href="https://github.com/Slicer/Slicer/wiki/Modern-Look" class="inline-onebox">Modern Look · Slicer/Slicer Wiki · GitHub</a></p>
<p>I’m currently experimenting with how to create icons and will soon submit a draft pull request that demonstrates some of the early results.</p>

---

## Post #14 by @lassoan (2021-09-22 23:55 UTC)

<p>The pull request that updates a number of icons is available here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5887">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5887" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5887" target="_blank" rel="noopener">ENH: Improve icon set</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:improve-icons</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-22" data-time="23:50:47" data-timezone="UTC">11:50PM - 22 Sep 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 56 files with 1073 additions and 49 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5887/files" target="_blank" rel="noopener">
          <span class="added">+1073</span>
          <span class="removed">-49</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is a work in progress and the pull request is submitted so that we can star<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5887" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">t discussion before proceeding with further updates.

A few new icons are added that use more modern style (flat, duotone) and have higher resolution, and look OK over both light and dark backgrounds. All icons are based on Google material design icon set (https://fonts.google.com/icons), edited in Inkscape, exported in native 24x24 and double 48x48 resolution.

![image](https://user-images.githubusercontent.com/307929/134435339-2f1bd529-8c4b-4ded-a40d-4a58cf59d285.png)

![image](https://user-images.githubusercontent.com/307929/134435436-5e94aa38-8919-4108-a009-caac180b4175.png)

A summary of the overall effort is described on this labs page: https://github.com/Slicer/Slicer/wiki/Modern-Look

Questions:
- Does the workflow of getting SVG from "Google material design" icon set, editing in Inkscape, exporting to 24x24 and 48x48 sound good?
- Is this minimalistic style, web-like generally a good direction? It would mean that we would need to replace all the icons that come from the Qt theme (as they are more detailed, 3D-like style). There would still be some inconsistency, as buttons themselves have a kind of 3D/gradient look (but maybe that could be removed by adjusting the color table).
- Should we use the same colors in light and dark mode? Switching over to different icons or somehow dynamically recolor all the icons could result in better contrast, but could be much harder to implement. Or should we add shadows (that would improve contrast but would make it a bit more difficult to create the icons). Or should we just go all-in on dark mode and remove light mode completely?
- What colors should we use? We could use the same 2-3 colors for all icons, or we could use different colors for different categories (e.g., file operations are orange, markups are blue, segmentations is green, ...) but we might run out of nice, distinguishable colors that work well over both light and dark background; and it may be difficult to be consistent. However, more colors can make it easier to find buttons. For example, above the blue module selection buttons separate nicely from the yellow file load/save icons.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Anyone is welcome to comment on the discussion there.</p>

---
