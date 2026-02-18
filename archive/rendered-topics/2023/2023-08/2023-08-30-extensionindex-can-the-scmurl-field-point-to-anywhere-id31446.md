# ExtensionIndex : can the scmurl field point to anywhere?

**Topic ID**: 31446
**Date**: 2023-08-30
**URL**: https://discourse.slicer.org/t/extensionindex-can-the-scmurl-field-point-to-anywhere/31446

---

## Post #1 by @chir.set (2023-08-30 10:58 UTC)

<p>Hi,</p>
<p>I wish to know if the scmurl field of the *.s4ext file in the ExtensionIndex must point to a github repository? Would an extension be built if it points elsewhere, to a gitlab repository for example?</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2023-08-30 12:39 UTC)

<p>Yes, gitlab should be fine as long as the scmurl points to something that can be cloned.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#supported-metadata-fields" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#supported-metadata-fields</a></p>

---

## Post #3 by @andrew_why_not (2024-09-18 08:15 UTC)

<p>Hello!</p>
<p>And what about the modules built and available only locally? For instance, if I pack a module locally and distribute it myself, where scmurl should point at?</p>

---

## Post #4 by @pieper (2024-09-18 14:43 UTC)

<p>If you are using the regular build process for extensions you will need to point somewhere.  It can be a directory that contains a git repository (just use the file path).</p>

---
