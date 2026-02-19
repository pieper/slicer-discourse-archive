---
topic_id: 3789
title: "How To Update The Progress Bar From A Scripted Cli"
date: 2018-08-15
url: https://discourse.slicer.org/t/3789
---

# How to update the progress bar from a scripted CLI

**Topic ID**: 3789
**Date**: 2018-08-15
**URL**: https://discourse.slicer.org/t/how-to-update-the-progress-bar-from-a-scripted-cli/3789

---

## Post #1 by @ihnorton (2018-08-15 20:25 UTC)

<p>I added an example to the Python scripting documentation, demonstrating how to use the Slicer Execution Model XML-based (<code>&lt;filter-progress&gt;...&lt;/filter-progress&gt;</code>) reporting format from a scripted CLI. Getting the bar to update in realtime requires one small detail, to flush stdout after each update, or else Slicer will not see/parse the output until the CLI completes.</p>
<p>See example code here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_update_progress_bar_in_scripted_.28Python.2C_or_other.29_CLI_modules" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_update_progress_bar_in_scripted_.28Python.2C_or_other.29_CLI_modules</a></p>

---

## Post #2 by @strider_hunter (2020-10-02 12:37 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> As an update to the Python FAQs, one could also add a question on “How to access progress bar of scripted CLI from scripted module”</p>
<ul>
<li>MyModule.py</li>
</ul>
<pre><code class="lang-auto">def createProgressDialog(parent=None, value=0, maximum=100, windowTitle="Processing..."):
    import qt # qt.qVersion()
    progressIndicator = qt.QProgressDialog()  #(parent if parent else self.mainWindow())
    progressIndicator.minimumDuration = 0
    progressIndicator.maximum = maximum
    progressIndicator.value = value
    progressIndicator.windowTitle = windowTitle
    return progressIndicator
      

class MyModuleWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):

    def setup(self)

        parametersFormLayout = qt.QFormLayout(myInputCollapsibleButton)
        self.testButton = qt.QPushButton('Test')
        self.testButton.enabled = True
        self.testButton.clicked.connect(self.onTestButton)
        parametersFormLayout.addRow(self.TestButton)
    
    def onTestButton(self):
        myCli = slicer.modules.tmp2cli
        cliNode = None
        myInt = 100
        cliNode = slicer.cli.run(myCli, cliNode, {'myString': 'hello World', 'myInt':100} )
        cliNode.AddObserver('ModifiedEvent', self.onCliModified)
        self.progressBar = myUtil.createProgressDialog(None, 0, myInt)
    
    def onCliModified(self, caller, event):
        self.progressBar.setValue(caller.GetProgress())
        if caller.GetStatus() == 32: 
            self.progressBar.close()
</code></pre>
<ul>
<li>MyModuleCLI.py</li>
</ul>
<pre><code class="lang-auto">#!/usr/bin/env python-real

import os
import sys
import time

def main(params):
    myString = params[1]
    myint = params[3]

    print("""&lt;filter-start&gt;&lt;filter-name&gt;TestFilter&lt;/filter-name&gt;&lt;filter-comment&gt;ibid&lt;/filter-comment&gt;&lt;/filter-start&gt;""")
    sys.stdout.flush()

    for i in range(0,myint):
        print("""&lt;filter-progress&gt;{}&lt;/filter-progress&gt;""".format(i/float(myint)))
        sys.stdout.flush()
        time.sleep(0.5)

    print("""&lt;filter-end&gt;&lt;filter-name&gt;TestFilter&lt;/filter-name&gt;&lt;filter-time&gt;{}&lt;/filter-time&gt;&lt;/filter-end&gt;""".format(myint))
    sys.stdout.flush()

if __name__ == "__main__":
    print (' ===================== ', len(sys.argv))
    for id, each in enumerate(sys.argv):
        print (' - sys.argv[{}] = {}'.format(id, each))
    if len(sys.argv) &gt; 1:
        main(sys.argv[1:])
</code></pre>

---

## Post #3 by @lassoan (2020-10-03 03:43 UTC)

<p>Thanks a lot, I’ve added it here:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_display_progress_bar_for_CLI_module_execution_in_a_scripted_module" target="_blank" rel="noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_display_progress_bar_for_CLI_module_execution_in_a_scripted_module" target="_blank" rel="noopener">Documentation/Nightly/Developers/FAQ/Python Scripting - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
