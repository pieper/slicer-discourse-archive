# How to convert a custom 3D Slicer plugin with ParameterNodes into a CLI-friendly module?

**Topic ID**: 44217
**Date**: 2025-08-27
**URL**: https://discourse.slicer.org/t/how-to-convert-a-custom-3d-slicer-plugin-with-parameternodes-into-a-cli-friendly-module/44217

---

## Post #1 by @khyatisethia (2025-08-27 08:43 UTC)

<p>Hi everyone,</p>
<p>I’ve been working on a custom plugin for 3D Slicer, and I’ve run into a design issue that makes it hard to reuse the logic outside of the GUI.</p>
<p>Right now, my <code>ModuleWidget</code> class is tightly coupled to the Slicer GUI elements:</p>
<ul>
<li>
<p><code>self.ui</code> and Qt widgets</p>
</li>
<li>
<p><code>qt.QSettings</code></p>
</li>
<li>
<p><code>slicer.util</code> helpers</p>
</li>
<li>
<p>ParameterNodes via <code>self._parameterNode</code></p>
</li>
<li>
<p>event filters, dialogs, and signal connections</p>
</li>
</ul>
<p>This setup works fine inside Slicer, but it makes it unsuitable for running the same functionality in a <strong>pure Python CLI script</strong> (no Slicer GUI).</p>
<p>The functionality right now it’s tied into the widget/ParameterNode infrastructure.</p>
<p>My idea is to move the main logic into a separate class and make it GUI-independent. Then the widget would only handle the GUI and parameter syncing, while the new class could be imported and used in a CLI context. But this is more work.</p>
<p><strong>Questions for the community:</strong></p>
<ul>
<li>
<p>What is the best way to convert any Custom Module to CLI module?</p>
</li>
<li>
<p>What is the recommended way to refactor a Slicer plugin if I want to reuse its logic outside of the GUI?</p>
</li>
<li>
<p>Is there a standard pattern for decoupling ParameterNodes from the processing logic?</p>
</li>
<li>
<p>Has anyone done a similar migration from a ScriptedLoadableModuleWidget to a CLI-usable module?</p>
</li>
</ul>
<p>Any advice, best practices, or examples would be really helpful!</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @pieper (2025-08-27 15:47 UTC)

<p>Can you be more specific about what your module does?</p>
<p>If you are using all these features of Slicer and you want to work outside of Slicer then you would need to find replacements somehow.  Mostly when we factor out Logic classes it’s for things with few dependencies on application-level features.  Things like image processing or linear algebra can factor out more easily, but signals, slots, and dialogs not so much.</p>

---

## Post #3 by @khyatisethia (2025-09-03 11:47 UTC)

<p>I’ve addressed the issue by moving the logic into a separate class, whereas previously it was integrated directly into the Widget class.</p>

---
