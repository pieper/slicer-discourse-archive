# Load self tests from a file external the main module

**Topic ID**: 42769
**Date**: 2025-05-01
**URL**: https://discourse.slicer.org/t/load-self-tests-from-a-file-external-the-main-module/42769

---

## Post #1 by @ejm-revvity (2025-05-01 22:23 UTC)

<p>I have a Slicer <code>ScriptedLoadableModule</code> and in the same physical file a series of tests. I would like to place the tests in a separate file. However, I’m not able to get the <code>SelfTests</code> module in Slicer to load/recognize this tests file. Is this possible?</p>
<p>In the main module I have:</p>
<pre><code class="lang-auto">import Tests
class Test(Tests.Tests):
    """Test class for module."""
</code></pre>
<p>In the external file I have:</p>
<p><code>class Tests(ScriptedLoadableModuleTest):</code></p>

---

## Post #2 by @lassoan (2025-05-01 22:31 UTC)

<p>Usually each SelfTest is a module (see for example <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Tables/Testing/Python/TablesSelfTest.py">TablesSelfTest</a>). Modules <a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Base/Python/slicer/ScriptedLoadableModule.py#L44-L51">register themselves as selftests</a>. If you want to break away from this convention then you can register any function as selftest the same way as modules do it.</p>

---

## Post #3 by @ejm-revvity (2025-05-02 21:48 UTC)

<p>I find that testing code mixed with implementation adds unnecessary noise for someone reading/maintaining it. This is, of course just my opinion.</p>
<p>So out of curiosity, if one took <a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Modules/Loadable/Tables/Testing/Python/TablesSelfTest.py#L51-L286" rel="noopener nofollow ugc">class TablesSelfTestTest</a> and moved it into its own module, would the Slicer SelfTests module discover/load it?</p>
<p>Answered my own question: no. I was assuming <code>ScriptedLoadableModuleTest</code> inherited from <code>ScriptedLoadableModule</code>.</p>

---

## Post #5 by @lassoan (2025-05-03 14:09 UTC)

<aside class="quote no-group" data-username="ejm-revvity" data-post="3" data-topic="42769">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ejm-revvity/48/80123_2.png" class="avatar"> ejm-revvity:</div>
<blockquote>
<p>I find that testing code mixed with implementation adds unnecessary noise for someone reading/maintaining it. This is, of course just my opinion.</p>
</blockquote>
</aside>
<p>There are certainly advantages and disadvantages of keeping the implementation and test together. The default scripted module template uses one file to encourage developers who are new to Slicer (and potentially new to programming) to add automated testing while still allowing them to have their module in a single file. I agree that it adds noise to the implementation; and if the module grows larger then it is better to split it up to several files.</p>
<hr>
<p>If you are interested in running Python tests without CTest/CMake then I would recommend to check out the <a href="https://github.com/KitwareMedical/SlicerPythonTestRunner">SlicerPythonTestRunner</a> extension. The SelfTests module is just for a slightly more convenient manual launching of some test (not that useful, maybe we should remove it to avoid confusion?).</p>
<p>Example SlicerPythonTestRunner test result:</p>
<p>                    <a href="https://raw.githubusercontent.com/KitwareMedical/SlicerPythonTestRunner/main/Screenshots/0.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/KitwareMedical/SlicerPythonTestRunner/main/Screenshots/0.png" width="362" height="433">
          </a>

</p>

---

## Post #6 by @ejm-revvity (2025-05-08 21:52 UTC)

<p>SlicerPythonTestRunner is exactly what I want!! <img src="https://emoji.discourse-cdn.com/twitter/crossed_fingers.png?v=14" title=":crossed_fingers:" class="emoji" alt=":crossed_fingers:" loading="lazy" width="20" height="20"></p>

---
