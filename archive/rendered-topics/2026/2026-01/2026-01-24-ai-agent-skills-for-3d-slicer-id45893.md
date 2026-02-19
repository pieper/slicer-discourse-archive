---
topic_id: 45893
title: "Ai Agent Skills For 3D Slicer"
date: 2026-01-24
url: https://discourse.slicer.org/t/45893
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
