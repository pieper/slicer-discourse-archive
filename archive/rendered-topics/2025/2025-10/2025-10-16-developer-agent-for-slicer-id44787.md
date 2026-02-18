# Developer Agent for Slicer

**Topic ID**: 44787
**Date**: 2025-10-16
**URL**: https://discourse.slicer.org/t/developer-agent-for-slicer/44787

---

## Post #1 by @muratmaga (2025-10-16 15:04 UTC)

<p>As others, I have been using LLMs to help develop functionality in the Slicer. This is typically writing code in VS, then loading it into slicer and testing it, then copy and pasting the error back to the agent to iterate and fix the error.</p>
<p>I found this a bit intimidating (particularly VS code) as someone who doesn’t do programming as a day job. Particularly given nowadays our typical advise on the forum is to say “you can do this with chatcpt”, I thought if I can streamline a few things, and actually do all the work directly inside the Slicer. The idea is to do the prompting in Slicer (whether for a script or a module), let it run, and if it fails, capture the error and send it back to itself to correct it. Then the resultant script is loaded into the scene as a python text node and can be opened and edited inside our Script Editor (which I added a few more things that I think made it more usable, definitely for me).</p>
<p>At this point, as far as I can tell all of this is working. I am coming to a point that my technical skills and understanding is not sufficient to guide the internal prompting about how the agent should behave (as opposed to the user’s prompt about the task). I think it needs an insider view to edit those and create an agent behavior that’s more accurate in the first attempt than the iterating over endlessly. By the way this is all written via vibe coding, so I am not even claim the code is meaningful, but it does seem to do the job in the way I thought it might be useful. I am sure there are better ways to accomplish this, and probably use the tokens more sparingly.</p>
<p>If you want to give it a try, it is here <a href="https://github.com/muratmaga/SlicerDeveloperAgent" class="inline-onebox" rel="noopener nofollow ugc">GitHub - muratmaga/SlicerDeveloperAgent: an agent to develop Slicer modules through Gemini</a> . You need a GH token to access the models and the Script Editor extension is a dependency. While there is no documentation, it is quite self-explanatory and looks something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/eda8b2883da25d395e31b4d5353442583d5d6084.png" data-download-href="/uploads/short-url/xUqALsfeRGMP0NU97BnTSFRn108.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eda8b2883da25d395e31b4d5353442583d5d6084_2_344x500.png" alt="image" data-base62-sha1="xUqALsfeRGMP0NU97BnTSFRn108" width="344" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eda8b2883da25d395e31b4d5353442583d5d6084_2_344x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eda8b2883da25d395e31b4d5353442583d5d6084_2_516x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eda8b2883da25d395e31b4d5353442583d5d6084_2_688x1000.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">693×1006 75.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The goal is not to replace IDEs or people’s development environment, but to lower the barrier for people who don’t do programming for a living or would not even consider doing this since the prerequisites it. Maybe start with a simple script. Once that’s working perhaps try to convert it to a module that is more friendly. Or edit the existing python modules for additional tasks. I don’t think I can expand this any further on my own (due to time and said reasons), but if anyone wants to help out, please do so. This might be a nice PW activity.</p>

---

## Post #2 by @cpinter (2025-10-17 09:32 UTC)

<p>This is amazing, Murat! I haven’t tried it yet, just looked at the code quickly. As I understand there is no domain-specific training nor knowledge integration involved, there is simply a base prompt to which the user’s request is added. Is this correct?</p>
<p>I want to try this eventually as well when I have time. I think this could be a great tool for onboarding people and for actually doing smaller proejcts. Thanks for your efforts!</p>

---

## Post #3 by @muratmaga (2025-10-17 15:31 UTC)

<p>No, there is nothing specific, it is all off-the-shelf stuff. I am sure it can be improved a lot if we can somehow do finetuning specific to Slicer (and related things). Yes, there is a “persona” prompt, that gets appended to the user task prompt.</p>
<p>This is the part where we need to provide domain-specific guidelines to the model and programming tasks. For whatever reason, the quality of the results I am getting through this is lower than if I provide the same prompt directly to the agent in VScode using the same model.</p>

---

## Post #4 by @cpinter (2025-10-19 19:06 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="44787">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>lower than if I provide the same prompt directly to the agent in VScode</p>
</blockquote>
</aside>
<p>My guess would be that VS Code considers at least the file in the active tab (and in addition any that you explicitly specify). That could be already enough context to perform better.</p>

---

## Post #5 by @muratmaga (2025-10-19 19:43 UTC)

<p>Thats what i thought too, but previous script is also passed along with the error. So not sure how thats different then having it open in VSCode.</p>
<p>But clearly context is either not maintained in iterations or some other issue.</p>

---

## Post #6 by @lassoan (2025-10-20 17:03 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="44787">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>So not sure how thats different then having it open in VSCode.</p>
</blockquote>
</aside>
<p>It is not trivial at all how to provide your existing code as context for LLMs.<br>
Cursor is a company currently that does just this and it is currently valued at $30 billion. For me, VS Code works just as well as Cursor. So, it is not surprising that code generation works better inside the VS Code IDE.</p>
<p>For creating and developing a full module, it may be harder to do better than in an IDE. To make the first steps easier it may be enough to provide users templates, tutorials, a good agentic coding manifest (see some information for example <a href="https://arxiv.org/pdf/2509.14744">here</a>).</p>
<p>However, it could make sense to have a module in Slicer for creating and running code snippets to automate simple tasks (load some data, do some processing, set up visualization, export results, etc.). The module could automatically provide all the necessary context (where to look for code snippets, what data is in the scene, etc.). To facilitate this, we could:</p>
<ul>
<li>Develop a set of useful high-level functions, which would implement all the tasks that users frequently ask. I would guess that a few hundred small functions would provide all the necessary building blocks. The list of functions and their documentation would be used as context for the code generation.</li>
<li>Set up model context protocol in Slicer that would allow LLMs to verify themselves by testing code in Slicer. There was a post about it not too long ago: <a href="https://discourse.slicer.org/t/mcp-slicer-3d-slicer-model-context-protocol-integration/42292" class="inline-onebox">MCP-Slicer: 3D Slicer Model Context Protocol Integration</a>. The main difficulty is that you would want to run the LLM in a sandbox or you would really need to be careful about the API you expose.</li>
</ul>

---

## Post #7 by @muratmaga (2025-10-20 18:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="44787">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Cursor is a company currently that does just this and it is currently valued at $30 billion.</p>
</blockquote>
</aside>
<p>So if we can solve this problem, we wouldn’t need to worry about funding for Slicer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="44787">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, it could make sense to have a module in Slicer for creating and running code snippets to automate simple tasks (load some data, do some processing, set up visualization, export results, etc.). The module could automatically provide all the necessary context (where to look for code snippets, what data is in the scene, etc.). To facilitate this, we could:</p>
</blockquote>
</aside>
<p>That’s exactly what I would like to achieve.</p>

---

## Post #8 by @mau_igna_06 (2025-10-20 20:13 UTC)

<p>This thread sounds interesting</p>

---
