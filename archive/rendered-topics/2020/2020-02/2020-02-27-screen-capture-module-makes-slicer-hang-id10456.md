# Screen Capture module makes Slicer hang

**Topic ID**: 10456
**Date**: 2020-02-27
**URL**: https://discourse.slicer.org/t/screen-capture-module-makes-slicer-hang/10456

---

## Post #1 by @Fernando (2020-02-27 10:43 UTC)

<p>Hi all,</p>
<p>When I try to make a GIF with the Screen Capture module, Slicer hangs and I need to force quit. I’m quite confident it happens when <code>ffmpeg</code> is called. I open Slicer from <code>zsh</code> and I think this shell is not happy with some characters in the command line. If I run the command with quotes outside Slicer, it works fine. It also works if I open Slicer from <code>bash</code>. I tried using quotes <a href="https://github.com/Slicer/Slicer/blob/09d3554e74422e3bb504d2f7f2364e9534284453/Modules/Scripted/ScreenCapture/ScreenCapture.py#L755" rel="nofollow noopener">here</a>, i.e. <code>"-filter_complex \"palettegen,[v]paletteuse\""</code>, with no luck.</p>
<p>I’m using iTerm2 on macOS Sierra 10.12.6.</p>

---

## Post #2 by @lassoan (2020-02-27 13:42 UTC)

<p>How does the correctly working command line look like?</p>
<p>Python <code>subprocess.Popen</code> expects command-line arguments in a list but GUI for getting arguments from users as a list of strings would be quite complicated, so we just use a string and <a href="https://github.com/Slicer/Slicer/blob/09d3554e74422e3bb504d2f7f2364e9534284453/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1275">split to arguments at space characters</a>. Maybe you can try to replace this simple split with a version that does not split along spaces within quoted strings (like <a href="https://stackoverflow.com/questions/16710076/python-split-a-string-respect-and-preserve-quotes">this</a>).</p>

---

## Post #3 by @Fernando (2020-02-27 21:40 UTC)

<p>Ok so I might have omitted some information. Sorry about that.</p>
<p>In macOS, I always open Slicer from the command line as <code>path_to_slicer &amp;!</code>. I have noticed that the problem is caused by the <a href="https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html" rel="nofollow noopener"><code>&amp;</code></a>. When Slicer hangs, I just run <code>fg</code> in the terminal and the <code>ffmpeg</code> is run. I’m still not sure this behavior is expected. This is the same in <code>bash</code> and <code>zsh</code>.</p>
<p>Still confused by the command line. This one doesn’t work on <code>zsh</code>:</p>
<pre><code class="lang-auto">/usr/local/bin/ffmpeg -y -r 0.4 -start_number 0 -i /Users/fernando/tmp/SlicerCapture/tmp-PHBIZ-%05d.png -filter_complex palettegen,[v]paletteuse /Users/fernando/tmp/SlicerCapture/SlicerCapture.gif
zsh: no matches found: palettegen,[v]paletteuse
</code></pre>
<p>But this one does:</p>
<pre><code class="lang-auto">/usr/local/bin/ffmpeg -y -r 0.4 -start_number 0 -i /Users/fernando/tmp/SlicerCapture/tmp-PHBIZ-%05d.png -filter_complex "palettegen,[v]paletteuse" /Users/fernando/tmp/SlicerCapture/SlicerCapture.gif
</code></pre>
<p>I guess I can just stop calling Slicer as a background process.</p>

---

## Post #4 by @lassoan (2020-02-28 16:47 UTC)

<p>It might have something to do with console output redirection or usage of " characters in Python <code>subprocess.Popen</code>. If you can experiment with this a bit more (e.g., trying to call subprocess.Popen directly to run ffmpeg in Slicer’s Python console and see if you can find a working variant) then it would be great. If not, then I guess it’s useful information that running Slicer as a background process may lead to issues.</p>

---

## Post #5 by @Fernando (2020-03-01 10:29 UTC)

<p>Running just ffmpeg with Popen in the console causes the problem as well. <a href="https://stackoverflow.com/questions/47115191/when-i-run-ffmpeg-in-the-background-how-do-i-prevent-suspended-tty-output" rel="nofollow noopener">Apparently</a>, this can be solved adding <code>-nostdin</code> to the parameters. I’ll open a PR.</p>

---
