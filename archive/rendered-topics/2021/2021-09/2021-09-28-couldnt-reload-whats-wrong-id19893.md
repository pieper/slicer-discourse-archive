# Couldn't Reload, what's wrong

**Topic ID**: 19893
**Date**: 2021-09-28
**URL**: https://discourse.slicer.org/t/couldnt-reload-whats-wrong/19893

---

## Post #1 by @jumbojing (2021-09-28 10:28 UTC)

<pre><code class="lang-auto">[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -   File "/Applications/Slice98.app/Contents/bin/Python/slicer/ScriptedLoadableModule.py", line 195, in onReload
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -     slicer.util.reloadScriptedModule(self.moduleName)
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -   File "/Applications/Slice98.app/Contents/bin/Python/slicer/util.py", line 1164, in reloadScriptedModule
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -     moduleName, fp, filePath, ('.py', 'r', imp.PY_SOURCE))
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -   File "/Applications/Slice98.app/Contents/lib/Python/lib/python3.6/imp.py", line 235, in load_module
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -     return load_source(name, filename, file)
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -   File "/Applications/Slice98.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -     module = _exec(spec, sys.modules[name])
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 674, in exec_module
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 780, in get_code
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -   File "/Applications/Slice98.app/Contents/lib/Python/lib/python3.6/imp.py", line 156, in get_data
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -     return file.read()
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -   File "/Applications/Slice98.app/Contents/bin/../lib/Python/lib/python3.6/encodings/ascii.py", line 26, in decode
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) -     return codecs.ascii_decode(input, self.errors)[0]
[CRITICAL][Stream] 28.09.2021 18:24:37 [] (unknown:0) - UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 1034: ordinal not in range(128)

</code></pre>

---

## Post #2 by @lassoan (2021-09-28 13:22 UTC)

<p>You used non-ASCII characters (probably international characters using UTF-8 encoding) in your source file.</p>
<p>Instead of writing unicode characters in your .py file, it is better if you write all the code and user-displayable text in English, using ASCII characters, and use translation infrastructure to replace it with text in any language, using UTF-8 encoding. Unfortunately, the translation infrastructure is not yet fully in place, but we have received funding recently and there should be significant progress in the coming months. See more information <a href="https://github.com/Slicer/Slicer/wiki/I18N">here</a>.</p>
<p>In the short term, you can try if adding <code># coding: utf8</code> as the first line of your .py file fixes the issue. If that does not work, then you may need to replace utf-8 character by escape sequences. For example, instead of writing <code>résumé</code>, you can write <code>b"r\xc3\xa9sum\xc3\xa9".decode("utf-8")</code></p>
<pre><code class="lang-auto">&gt;&gt;&gt; "résumé".encode("utf-8")
b'r\xc3\xa9sum\xc3\xa9'

&gt;&gt;&gt; b"r\xc3\xa9sum\xc3\xa9".decode("utf-8")
'résumé'
</code></pre>

---

## Post #3 by @jumbojing (2021-09-29 11:19 UTC)

<p>我用了<a href="https://marketplace.visualstudio.com/items?itemName=cwan.native-ascii-converter" rel="noopener nofollow ugc">Native-ASCII Converter - Visual Studio Marketplace</a></p>
<p>谢谢老师</p>

---

## Post #4 by @lassoan (2021-09-29 18:52 UTC)

<p>On Windows and Linux module reload worked well with files using UTF-8 encoding, but apparently macOS had trouble. I’ve <a href="https://github.com/Slicer/Slicer/commit/44ad869db6ab9e937dda2be7d14bfd7472742f4b">added explicit specification of the encoding</a>, so you reloading will work if you use special characters in the file from tomorrow. That said, I would still highly recommend to keep the source code ASCII and use translation infrastructure to add messages in different languages.</p>

---
