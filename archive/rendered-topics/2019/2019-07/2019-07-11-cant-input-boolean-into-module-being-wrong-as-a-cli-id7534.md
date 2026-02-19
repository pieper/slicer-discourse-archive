---
topic_id: 7534
title: "Cant Input Boolean Into Module Being Wrong As A Cli"
date: 2019-07-11
url: https://discourse.slicer.org/t/7534
---

# Can't input boolean into module being wrong as a cli

**Topic ID**: 7534
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/cant-input-boolean-into-module-being-wrong-as-a-cli/7534

---

## Post #1 by @jrojasUNC (2019-07-11 15:44 UTC)

<p>Operating system: Windows 10 64 bit<br>
Slicer version:4.11 nightly<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,</p>
<p>I’m trying to run my own scripted module as a cli. I can input a string into the module just fine, but when I try to input a boolean, the long flag appears in the argv but not the value.</p>
<p>My xml file looks like this:</p>
<pre><code class="lang-python">&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;executable&gt;
  &lt;category&gt;filtering&lt;/category&gt;
  &lt;title&gt;MyModule&lt;/title&gt;
  &lt;description&gt;module to do things&lt;/description&gt;
  &lt;version&gt;1.0&lt;/version&gt;
  &lt;parameters&gt;
    &lt;label&gt;IO&lt;/label&gt;
    &lt;description&gt;Input/output parameters&lt;/description&gt;
    &lt;string&gt;
      &lt;longflag&gt;filename&lt;/longflag&gt;
      &lt;label&gt;sequence filename&lt;/label&gt;
      &lt;channel&gt;input&lt;/channel&gt;
      &lt;description&gt;filename of sequence to be processed&lt;/description&gt;
    &lt;/string&gt;
    &lt;boolean&gt;
      &lt;longflag&gt;writefile&lt;/longflag&gt;
      &lt;label&gt;write file&lt;/label&gt;
      &lt;channel&gt;input&lt;/channel&gt;
      &lt;description&gt;write output nrrd file&lt;/description&gt;
    &lt;/boolean&gt;
  &lt;/parameters&gt;
&lt;/executable&gt;

And my python file looks like:

#!/usr/bin/env python-real
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    FILENAME = sys.argv[sys.argv.index('--filename') + 1]
    WRITEFILE = sys.argv[sys.argv.index('--writefile') + 1]

    # Do stuff
</code></pre>
<p>In slicer, I add the additional module path and run the following code:</p>
<pre><code class="lang-python">parameters = {}
parameters["filename"] = "fullFilenameOfImage"
parameters["writefile"] = True
cli_node = slicer.cli.runSync(slicer.modules.mycli, None, parameters)
</code></pre>
<p>if I add a print statement to my py file to print argv and I use <code>cli_node.GetOutputText()</code>, I get:<br>
<code>MyModule standard output:\n\n['path/myCLI.py', '--filename', 'fullFilenameOfImage', '--writefile']\r\n</code></p>
<p>The long flag is displayed but there is no  value after it so when I do <code>cli_node.GetErrorText()</code> I get:<br>
<code>MyModule standard error:\n\nTraceback (most recent call last):\r\n File "path/myCLI.py", line 16, in &lt;module&gt;\r\n WRITEFILE = sys.argv[sys.argv.index(\'--writefile\') + 1]\r\nIndexError: list index out of range\r\n</code></p>
<p>I tried <code>parameters["writefile"] = slicer.util.toBool(True)</code> and <code>slicer.util.toBool("true")</code> but I get the same result.</p>
<p>Thank you for your help,</p>
<p>Juan</p>

---

## Post #2 by @lassoan (2019-07-11 16:13 UTC)

<p>What you describe is the correct behavior. If you check the “write file” checkbox then <code>--writefile</code> will be added to the command-line argument list, if unchecked then the <code>--writefile</code> will not be added. You can check the flag like this:</p>
<pre><code>writeFile = '--writefile' in sys.argv</code></pre>

---

## Post #3 by @pieper (2019-07-11 16:25 UTC)

<p>Also this looks like a bug:</p>
<pre><code class="lang-auto">WRITEFILE = sys.argv[sys.argv.index('--writefile') + 1]
</code></pre>
<p>since writefile is a boolean it won’t have an extra argument.</p>

---

## Post #4 by @jrojasUNC (2019-07-11 16:39 UTC)

<p>I see. I didn’t see that in the wiki. Thank you both!</p>

---
