---
topic_id: 45893
title: "AI Agent Skills for 3D Slicer?"
date: 2026-01-24
url: https://discourse.slicer.org/t/45893
last_bumped: 2026-06-06T19:58:04.523Z
---

# AI Agent Skills for 3D Slicer?

**Topic ID**: 45893
**Date**: 2026-01-24
**URL**: https://discourse.slicer.org/t/ai-agent-skills-for-3d-slicer/45893

---

## Post #1 by @mikebind (2026-01-24 23:52 UTC)

<p>I noticed in the most recent release notes for VS Code support for “Agent Skills”, which are an <a href="https://agentskills.io/home" rel="noopener nofollow ugc">open-standard platform-agnostic method of specifying helpful standards and domain-specific reference materials for AI Agents to reference</a>.  This seems like potentially a great way of improving Slicer-specific coding abilities for AI agents. This could also be connected with improving the effectiveness of the prototype tool described in this thread <a href="https://discourse.slicer.org/t/developer-agent-for-slicer/44787">Developer Agent for Slicer - Support - 3D Slicer Community</a>.  While I think this is still in the realm of rapid development (and so may not be stable), it does intend to be an open standard and currently looks like it has fairly wide support. Has anyone tried to use this framework in the context of Slicer extension development?  I think there is an opportunity here to develop some shared community resources like a “skill repository” (skills are intended to be shareable).  Personally, I am just starting to try to dip a toe into using an agent to explore developing a segment editor effect, so I don’t yet have enough experience to try to set up anything useful, it just seems like an intriguing and intuitively sensible approach to improving Slicer-related coding via agents. Any experience or thoughts?</p>

---

## Post #2 by @muratmaga (2026-01-25 00:22 UTC)

<p>Actually this was a topic I was planning to do as a project week project, alas other things intervened and I am not headed to Las Palmas.</p>
<p>I tried a few things on my end (as you linked above). The latest iteration of it uses DeepSeek inference engine on the JS2, which mitigates the need of API keys or subscriptions (though you have to either run inside the JS2 -which is not an issue if you are using MorphoCloud- or need to tunnel the request).</p>
<p>I am more interested in educational aspect of this, bringing people who are not used to coding and wouldn’t invest the time on their own but with a little bit of help would maybe be able to hack together something…</p>

---

## Post #3 by @pieper (2026-01-25 11:02 UTC)

<p>A related project will be going on at Project Week:</p>
<p><a href="https://projectweek.na-mic.org/PW44_2026_GranCanaria/Projects/ClaudeScientificSkillForImagingDataCommons/">https://projectweek.na-mic.org/PW44_2026_GranCanaria/Projects/ClaudeScientificSkillForImagingDataCommons/</a></p>
<p>Informally I know there will be a lot of discussion about how these tools are changing out coding habits and how they are working out for developers and users with more or less experience.  We’ll try to capture those experiences and publish any experiments that come up during the week.</p>

---

## Post #4 by @Sveng (2026-06-05 15:45 UTC)

<aside class="quote no-group quote-modified" data-username="mikebind" data-post="1" data-topic="45893" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I noticed in the most recent release notes for VS Code support for “Agent Skills”, which are an <a href="https://agentskills.io/home" rel="noopener nofollow ugc">open-standard platform-agnostic method of specifying helpful standards and domain-specific reference materials for AI Agents to reference</a>. This seems like potentially a great way of improving Slicer-specific coding abilities for AI agents. This could also be connected with improving the effectiveness of the prototype tool described in this thread <a href="https://discourse.slicer.org/t/developer-agent-for-slicer/44787">Developer Agent for Slicer - Support - 3D Slicer Community</a>. While I think this is still in the realm of rapid development (and so may not be stable), it does intend to be an open standard and currently looks like it has fairly wide support. Has anyone tried to use this framework in the context of Slicer extension development? I think there is an opportunity here to develop some shared community resources like a “skill repository” (skills are intended to be shareable). I recently used <a href="https://mac.eltima.com/ai-headshot-generator-app/" rel="noopener nofollow ugc">Eltima AI for iphone</a> to generate a high quality developer avatar. Personally, I am just starting to try to dip a toe into using an agent to explore developing a segment editor effect, so I don’t yet have enough experience to try to set up anything useful, it just seems like an intriguing and intuitively sensible approach to improving Slicer-related coding via agents. Any experience or thoughts?</p>
</blockquote>
</aside>
<p>This is actually a brilliant idea. Standard LLMs tend to hallucinate Slicer functions a lot because they just don’t have enough specialized training data.</p>
<p>An open standard “Agent Skills” repository is exactly what the community needs to fix that. Feeding an agent structured, domain-specific references and boilerplate for things like the Segment Editor or volume rendering would drastically improve its output and save everyone a ton of debugging time.</p>
<p>Even if you’re just dipping your toes in with a segment editor effect, just mapping out a basic reference guide or schema of Slicer specific coding standards could be the foundation for that community repo. I haven’t experimented with this specific VS Code framework yet, but building a shared skill repository sounds like the absolute right move to supercharge Slicer development.</p>

---

## Post #5 by @pieper (2026-06-05 15:48 UTC)

<p>See this thread for more recent developments: <a href="https://discourse.slicer.org/t/new-slicer-skill-ai-tool/46243" class="inline-onebox">New slicer-skill ai tool</a></p>

---

## Post #6 by @Hemran_313 (2026-06-06 19:57 UTC)

<p>I think its a pretty interesting idea, one of the biggest issues with AI tools and slicer development is that they often dont know much about Slicers APIs and development patterns. Having shared “skills” or reference material could help a lot with that. Even a small community repository covering common tasks like module creation, Segment Editor effects, and MRML usage could make AI generated code much more accurate.</p>

---

## Post #7 by @Hemran_313 (2026-06-06 19:58 UTC)

<p>good, saw it.</p><aside class="quote quote-modified" data-post="1" data-topic="46243">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-slicer-skill-ai-tool/46243">New slicer-skill ai tool</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
    </div>
  </div>
  <blockquote>
    After learning from <a href="https://github.com/pieper/slicer-skill?tab=readme-ov-file#related-projects" rel="noopener nofollow ugc">previous experiments, several productive discussions</a> at project week and at the <a href="https://github.com/pieper/slicer-skill?tab=readme-ov-file#related-projects" rel="noopener nofollow ugc">last developer meeting</a>, I put together this <a href="https://github.com/pieper/slicer-skill" rel="noopener nofollow ugc">slicer-skill</a> that can be used with coding agents like Claude code. 
It involves pulling down all the source code from Slicer and libraries like VTK, ITK, etc, together with all the discourse archives and other material like the source code for all the extensions.  It also includes a new mcp server so that it can iterate on doing programming tasks. 
I thi…
  </blockquote>
</aside>


---
