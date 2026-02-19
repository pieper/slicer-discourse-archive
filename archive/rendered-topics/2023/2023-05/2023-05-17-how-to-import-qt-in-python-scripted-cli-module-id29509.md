---
topic_id: 29509
title: "How To Import Qt In Python Scripted Cli Module"
date: 2023-05-17
url: https://discourse.slicer.org/t/29509
---

# How to import Qt in Python scripted CLI module?

**Topic ID**: 29509
**Date**: 2023-05-17
**URL**: https://discourse.slicer.org/t/how-to-import-qt-in-python-scripted-cli-module/29509

---

## Post #1 by @benzwick (2023-05-17 14:59 UTC)

<p>Is it possible to import Qt inside a Python scripted CLI module? I want to display an error message to tell the user to modify the input parameters. When I try to <code>import qt</code> I get the following error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/ben/projects/SlicerCBM/SlicerFreeSurferCommands/FreeSurferSynthStripSkullStrip/FreeSurferSynthStripSkullStrip.py", line 4, in &lt;module&gt;
    import qt
  File "/opt/slicer/Slicer-5.2.2-linux-amd64/bin/Python/qt/__init__.py", line 19, in &lt;module&gt;
    from PythonQt.private import QObject
ModuleNotFoundError: No module named 'PythonQt'
</code></pre>

---

## Post #2 by @benzwick (2023-05-17 15:27 UTC)

<p>I also tried <code>import tkinter</code>:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/ben/projects/SlicerCBM/SlicerFreeSurferCommands/FreeSurferSynthStripSkullStrip/FreeSurferSynthStripSkullStrip.py", line 130, in &lt;module&gt;
    import tkinter
  File "/opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/python3.9/tkinter/__init__.py", line 37, in &lt;module&gt;
    import _tkinter # If this fails your Python may not be configured for Tk
ModuleNotFoundError: No module named '_tkinter'
</code></pre>
<p>This seems like the simplest way to do it:</p>
<pre><code class="lang-auto">    import slicer.util
    slicer.util.errorDisplay("Something wrong.")
</code></pre>
<p>but it also fails</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/ben/projects/SlicerCBM/SlicerFreeSurferCommands/FreeSurferSynthStripSkullStrip/FreeSurferSynthStripSkullStrip.py", line 129, in &lt;module&gt;
    slicer.util.errorDisplay("Something wrong.")
  File "/opt/slicer/Slicer-5.2.2-linux-amd64/bin/Python/slicer/util.py", line 2668, in errorDisplay
    import qt, logging
  File "/opt/slicer/Slicer-5.2.2-linux-amd64/bin/Python/qt/__init__.py", line 19, in &lt;module&gt;
    from PythonQt.private import QObject
ModuleNotFoundError: No module named 'PythonQt'
</code></pre>
<p>As an aside, are the <code>slicer.util</code> functions in general intended to be also used from CLI modules or do they only work in scripted modules?</p>

---

## Post #3 by @lassoan (2023-05-17 16:07 UTC)

<p>Python scripted CLI modules must never display any GUI. The user interface is generated automatically by Slicer. The algorithm must not be blocked by waiting for any user inputs. Progress information can be provided to the application by printing XML elements on the process output.</p>
<p>You can implement interactive GUI in Python in Python scripted loadable modules. A Python scripted loadable module can also call CLI modules (implemented in C++ or Python), so if you already have a CLI module then you can add a scripted loadable module if you need more customized, interactive GUI.</p>

---

## Post #4 by @benzwick (2023-05-17 16:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="29509">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The algorithm must not be blocked by waiting for any user inputs.</p>
</blockquote>
</aside>
<p>That makes a lot of sense.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="29509">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Progress information can be provided to the application by printing XML elements on the process output.</p>
</blockquote>
</aside>
<p>Is there an example of this somewhere?</p>
<p>All I want to do is display an error if the user doesn’t specify the correct input. I was using argparse like this:</p>
<pre><code class="lang-auto">    parser.add_argument('-i', '--image', required=True,
                        help='Input image to skullstrip.')
</code></pre>
<p>but it gives very noisy output:</p>
<pre><code class="lang-plaintext">FreeSurfer SynthStrip Skull Strip standard error:

usage: FreeSurferSynthStripSkullStrip.py [-h] -i IMAGE [-o OUT] [-m MASK]
                                         [-g | --gpu | --no-gpu] [-b BORDER]
                                         [--nocsf | --no-nocsf]
FreeSurferSynthStripSkullStrip.py: error: the following arguments are required: -i/--image

FreeSurfer SynthStrip Skull Strip standard output:

/home/ben/projects/SlicerCBM/SlicerFreeSurferCommands/FreeSurferSynthStripSkullStrip/FreeSurferSynthStripSkullStrip.py
</code></pre>
<p>The other alternative, which is more flexible is this:</p>
<pre><code class="lang-auto">    if not args.out and not args.mask:
        print("Error: User must request output Stripped Volume, Mask Volume, or both.")
        sys.exit(1)
</code></pre>
<p>which gives the following output:</p>
<pre><code class="lang-plaintext">FreeSurfer SynthStrip Skull Strip standard output:

/home/ben/projects/SlicerCBM/SlicerFreeSurferCommands/FreeSurferSynthStripSkullStrip/FreeSurferSynthStripSkullStrip.py
Error: User must request output Stripped Volume, Mask Volume, or both.
</code></pre>
<p>Is there a recommended way to do this? In C++ CLI modules the <code>PARSE_ARGS</code> macro seems to take care of this. By the way, where is that macro defined? I tried to search for it but couldn’t find it.</p>

---

## Post #5 by @lassoan (2023-05-17 16:32 UTC)

<p>If you print something on the error output and the process returns with an error then the error message is displayed in the CLI module GUI:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4b604069ff3b84920880e215d8eee512242e25e.png" data-download-href="/uploads/short-url/nv6gRKIKEZVGEYbBh3zzOrdERGK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4b604069ff3b84920880e215d8eee512242e25e_2_350x500.png" alt="image" data-base62-sha1="nv6gRKIKEZVGEYbBh3zzOrdERGK" width="350" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4b604069ff3b84920880e215d8eee512242e25e_2_350x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4b604069ff3b84920880e215d8eee512242e25e_2_525x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4b604069ff3b84920880e215d8eee512242e25e_2_700x1000.png 2x" data-dominant-color="47484A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1036×1478 69.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Progress reporting is described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel#Showing_Progress_in_an_Application" class="inline-onebox">Documentation/Nightly/Developers/SlicerExecutionModel - Slicer Wiki</a></p>

---

## Post #6 by @pieper (2023-05-17 17:12 UTC)

<aside class="quote no-group" data-username="benzwick" data-post="4" data-topic="29509">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>In C++ CLI modules the <code>PARSE_ARGS</code> macro seems to take care of this. By the way, where is that macro defined? I tried to search for it but couldn’t find it.</p>
</blockquote>
</aside>
<p>This is autogenerated from the XML description of the CLI, so you can find it in the build tree for the module.</p>

---
