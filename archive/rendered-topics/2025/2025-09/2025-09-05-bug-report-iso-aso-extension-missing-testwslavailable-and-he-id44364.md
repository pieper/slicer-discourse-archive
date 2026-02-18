# Bug Report ISO ASO Extension – Missing testWslAvailable and helper methods cause crash

**Topic ID**: 44364
**Date**: 2025-09-05
**URL**: https://discourse.slicer.org/t/bug-report-iso-aso-extension-missing-testwslavailable-and-helper-methods-cause-crash/44364

---

## Post #1 by @fabien-prog (2025-09-05 16:58 UTC)

<p>Hi everyone,</p>
<p>I ran into an issue trying to use the ISO ASO extension (Automated Dental Tools) in 3D Slicer 5.8.1 on Windows 11 with WSL2 + Ubuntu 24.04.</p>
<h3><a name="p-128211-problem-1" class="anchor" href="#p-128211-problem-1" aria-label="Heading link"></a>Problem</h3>
<p>When launching ISO ASO and clicking <em>Run</em>, the module gets stuck at <em>“Checking if WSL is installed, this task may take a moment”</em>. In the Slicer log, I see this error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File ".../ASO.py", line 1506, in onCheckRequirements
    if self.logic.testWslAvailable():
AttributeError: 'ASOLogic' object has no attribute 'testWslAvailable'

</code></pre>
<p>Later, even after adding that function to ASO.py, I hit:</p>
<pre><code class="lang-auto">AttributeError: 'ASOWidget' object has no attribute 'format_time'

</code></pre>
<h3><a name="p-128211-cause-2" class="anchor" href="#p-128211-cause-2" aria-label="Heading link"></a>Cause</h3>
<p>The current extension code is calling functions that don’t exist in <code>ASOLogic</code> and <code>ASOWidget</code>:</p>
<ul>
<li>
<p><code>ASOLogic.testWslAvailable()</code></p>
</li>
<li>
<p><code>ASOWidget.format_time()</code></p>
</li>
<li>
<p><code>ASOWidget.update_ui_time()</code></p>
</li>
</ul>
<p>Without these, the requirements check crashes and the module never gets to create the conda environment.</p>
<h3><a name="p-128211-workaround-fix-3" class="anchor" href="#p-128211-workaround-fix-3" aria-label="Heading link"></a>Workaround / Fix</h3>
<p>I was able to fix it by adding these functions back into the extension:</p>
<p><strong>Inside <code>ASOLogic</code> (ASO.py):</strong></p>
<pre><code class="lang-auto">def testWslAvailable(self) -&gt; bool:
    if platform.system() != "Windows":
        return False
    try:
        result = subprocess.run(
            ["wsl", "--status"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except Exception:
        return False

</code></pre>
<p><strong>Inside <code>ASOWidget</code> (ASO.py):</strong></p>
<pre><code class="lang-auto">def format_time(self, seconds: float) -&gt; str:
    if seconds &lt; 60:
        return f"{int(seconds)}s"
    elif seconds &lt; 3600:
        return f"{int(seconds // 60)}min {int(seconds % 60)}s"
    else:
        return f"{int(seconds // 3600)}h {int((seconds % 3600) // 60)}min {int(seconds % 60)}s"

def update_ui_time(self, start_time: float, previous_time: float) -&gt; str:
    current_time = time.time()
    elapsed = current_time - start_time
    return self.format_time(elapsed)

</code></pre>
<h3><a name="p-128211-result-4" class="anchor" href="#p-128211-result-4" aria-label="Heading link"></a>Result</h3>
<p>With these added, the ISO ASO extension now correctly:</p>
<ul>
<li>
<p>Detects WSL2</p>
</li>
<li>
<p>Detects Miniconda</p>
</li>
<li>
<p>Creates the conda environment in WSL</p>
</li>
<li>
<p>Moves on to library installation</p>
</li>
</ul>
<p>Hope this helps others who get stuck at the same point!</p>
<p>Fabien</p>

---
