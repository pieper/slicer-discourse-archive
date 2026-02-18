# Support python text highlighting in Text module

**Topic ID**: 34511
**Date**: 2024-02-24
**URL**: https://discourse.slicer.org/t/support-python-text-highlighting-in-text-module/34511

---

## Post #1 by @muratmaga (2024-02-24 00:41 UTC)

<p>As discussed in this thread, it would be nice to have a simple text editor that supports code highlight and indentation that can be routed directly into the python console for interactive python scripts.</p>
<p>Would be a valuable tool for novices starting to learn Slicer API and python programming and test samples from Script repository.</p>
<aside class="quote quote-modified" data-post="9" data-topic="34455">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/directly-interacting-with-python-console/34455/9">Directly interacting with python console</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    THis is interesting, I will give it a try. 
Meanwhile, what I was thinking is that we already have a Texts module in Slicer. Would it be possible it to support code highlighting and indentations and have route the code the python console? 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61648005019eb55b29d8e686ce0bf1c091c23801.png" data-download-href="/uploads/short-url/dTzDn9bUfr6LUmDQBaLrHOHRxa9.png?dl=1" title="image">[image]</a>
  </blockquote>
</aside>


---

## Post #2 by @timeanddoctor (2024-02-24 01:35 UTC)

<p>Cool…<br>
like the sublime Text?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c49e22818cbfd8ac036a72722d801ef86558be4.png" alt="image" data-base62-sha1="aSSA6d1R654hvfH52oryAGRm85K" width="457" height="168"></p>

---

## Post #3 by @timeanddoctor (2024-02-24 02:00 UTC)

<pre><code class="lang-auto">'''

li zhenzhu
Ningbo NO.2 Hospital

'''

import os
from pathlib import Path
import sys
import re

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self._highlighter = Highlighter()

        self.setup_file_menu()
        self.setup_editor()

        self.setCentralWidget(self._editor)
        self.setWindowTitle(self.tr("Syntax Highlighter"))

    def new_file(self):
        self._editor.clear()

    def open_file(self, path=""):
        file_name = path

        if not file_name:
            file_name, _ = QFileDialog.getOpenFileName(self, self.tr("Open File"), "",
                                                       "Python Files (*.py)")

        if file_name:
            in_file = QFile(file_name)
            if in_file.open(QFile.ReadOnly | QFile.Text):
                stream = QTextStream(in_file)
                self._editor.setPlainText(stream.readAll())

    def setup_editor(self):
        class_format = QTextCharFormat()
        class_format.setFontWeight(QFont.Bold)
        class_format.setForeground(Qt.blue)
        pattern = r'^\s*class\s+\w+\(.*$'
        self._highlighter.add_mapping(pattern, class_format)

        function_format = QTextCharFormat()
        function_format.setFontItalic(True)
        function_format.setForeground(Qt.blue)
        pattern = r'^\s*def\s+\w+\s*\(.*\)\s*:\s*$'
        self._highlighter.add_mapping(pattern, function_format)

        comment_format = QTextCharFormat()
        comment_format.setBackground(QColor("#77ff77"))
        self._highlighter.add_mapping(r'^\s*#.*$', comment_format)

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self._editor = QPlainTextEdit()
        self._editor.setFont(font)
        self._highlighter.setDocument(self._editor.document())

    def setup_file_menu(self):
        file_menu = self.menuBar().addMenu(self.tr("&amp;File"))

        new_file_act = file_menu.addAction(self.tr("&amp;New..."))
        new_file_act.setShortcut(QKeySequence(QKeySequence.New))
        new_file_act.triggered.connect(self.new_file)

        open_file_act = file_menu.addAction(self.tr("&amp;Open..."))
        open_file_act.setShortcut(QKeySequence(QKeySequence.Open))
        open_file_act.triggered.connect(self.open_file)

        quit_act = file_menu.addAction(self.tr("E&amp;xit"))
        quit_act.setShortcut(QKeySequence(QKeySequence.Quit))
        quit_act.triggered.connect(self.close)

        help_menu = self.menuBar().addMenu("&amp;Help")
        help_menu.addAction("About &amp;Qt", qApp.aboutQt)  # noqa: F821


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        QSyntaxHighlighter.__init__(self, parent)

        self._mappings = {}

    def add_mapping(self, pattern, format):
        self._mappings[pattern] = format

    def highlightBlock(self, text):
        for pattern, format in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, format)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(640, 512)
    window.show()
    window.open_file(os.fspath(Path(__file__).resolve()))
    sys.exit(app.exec())
</code></pre>
<p>this from <a href="https://doc.qt.io/qtforpython-6/examples/example_widgets_richtext_syntaxhighlighter.html" class="inline-onebox" rel="noopener nofollow ugc">Syntax Highlighter Example - Qt for Python</a></p>
<p>the picture after running<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa631e09efee6e21afdac22260ae1ca042278096.png" data-download-href="/uploads/short-url/ojjwJeph6lTZ3a1eK0mLyRy2aoK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa631e09efee6e21afdac22260ae1ca042278096.png" alt="image" data-base62-sha1="ojjwJeph6lTZ3a1eK0mLyRy2aoK" width="622" height="500" data-dominant-color="FAFAFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">909×730 19.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-02-24 02:57 UTC)

<p>Yes, something like that. A real basic editor, just a step above a text editor that preserve indentations, and  some highlighting…</p>

---

## Post #5 by @lassoan (2024-02-24 16:30 UTC)

<p>Storing code snippets in the scene is a good idea. The Texts module GUI is simple and fast (can handle text updates at hundreds of times per second for IGT use cases), so I would not try to add serious text editing features to it.</p>
<p>Jupyter notebook is a close-to-perfect solution for script development (it supports syntax highlighting, auto-complete, function documentation, code block execution, interactive step-by-step debugging, etc.) and it is already available in Slicer. But it is somewhat heavyweight (requires packages of about 1GB in total) and by default saves the text in a separate file (so we would need to figure out a solution for saving it to the scene). So, it may make sense to explore alternatives.</p>
<p>Trying to improve QTextEdit to match features of a modern code editor is hard. We know from our experience with the Python console. It took a lot of time of several developers and it is still very limited and has a number of bugs that we can not find time to fix.</p>
<p>Embedding an existing editor (implemented in C++, Python, or running in the web browser) could work. Embedding VS Code would be quite an obvious choice due to its popularity, and it should be feasible, too (see for example in github and <a href="https://plainenglish.io/blog/embed-a-runnable-vs-code-clone-with-react-882173be2aae">elsewhere</a>). Marimo is quite lighweight, uses text for script storage, and has a notebook-like interface, but somebody would need to figure out how to run it within an existing Python session. There are many web-based code editors out there.</p>
<p>It could be also possible to develop plugins for an existing editor that to allow remote code execution in Slicer’s Python environment. Similarly to how it is discussed <a href="https://stackoverflow.com/questions/53320958/vscode-python-remote-interpreter">here</a>.</p>

---

## Post #6 by @muratmaga (2024-02-24 23:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="34511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Trying to improve QTextEdit to match features of a modern code editor is hard.</p>
</blockquote>
</aside>
<p>Do we really need all the features of a full fledged code editor? What I was seeking is meant to provide simple, internal mechanism to direct python code into console. what you are proposing is almost integrating a full IDE into Slicer, which I am all for it, but is sum of the requirement to make it work would be any less than Jupyter Notebook?</p>
<p>From the example <a class="mention" href="/u/timeanddoctor">@timeanddoctor</a> pasted above (and I saw online the same link), I thought it might be a simple change to the Text module, but of course I will defer to you folks.</p>

---

## Post #7 by @cpinter (2024-03-01 10:48 UTC)

<p>I support Murat’s idea, having a simple editor inside Slicer that executes the code in the console on a button press would be really useful, and the Texts module could be a natural place for it, given that it is the only place with a sizeable text field, and then the snippets could be stored in the scene.</p>
<p>The reason it would be useful is that many times I am experimenting with simple things like setting display options, string operations, or anything that is relatively short, I open Notepad++, start typing there, and then copy-paste the code until it does what I exactly want it to do. Then I paste it in the actual code. The reason that I cannot just do the edit-copy-paste cycle in my VS code with all the code is that it is indented, so it does not run in the console (and many times I need to use temporary variables to get it to run etc.).</p>
<p>In terms of features I think relatively basic things could do the trick, like support of indentation with tab. I think this alone could speed up this development style a lot. A full-fledged editor would be awesome of course, but this simlpe feature in Texts would take very little development, but would still improve such workflows considerably.</p>
<p>As far as I know <a class="mention" href="/u/pieper">@pieper</a> works a similar way, maybe he could comment on this too. (Edit: I see he already answered in the previous topic)</p>

---

## Post #8 by @jamesobutler (2024-03-01 12:08 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="34511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>then copy-paste the code until it does what I exactly want it to do. Then I paste it in the actual code. The reason that I cannot just do the edit-copy-paste cycle in my VS code with all the code is that it is indented, so it does not run in the console</p>
</blockquote>
</aside>
<p>I work in a very similar way.</p>
<p>Further improvement of helping during this prototyping code snippet phase would be if valid execution in the python console could then go into a texts area as a code command history stack. Then I could copy-paste from there back into my editor more easily. Otherwise I have to filter through the python console to find my input lines between the output lines while also ignoring the <code>&gt;&gt;</code> prefix that is in the Python console for each line.</p>

---

## Post #9 by @muratmaga (2024-03-01 16:52 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="34511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>valid execution in the python console could then go into a texts area as a code command history stack.</p>
</blockquote>
</aside>
<p>That would be great.</p>

---

## Post #10 by @mikebind (2024-03-02 05:21 UTC)

<p>I think I would also potentially use this a lot if it were available.  I have two early stage development workflows that I use now:</p>
<ol>
<li>I have a sandbox module where I just add new logic functions to try them out and debug before embedding them in a new module.  The advantage of this approach is that the indentation and ‘self’ input arguments are then appropriate for directly cutting and pasting into another module’s logic class. The process to try the code involves remembering to save the file and reload the module before typing the desired logic function call into the python interactor.</li>
<li>I recently learned that you can run any .py file in Slicer’s python environment with the Ctrl-G key shortcut from the python interactor.  I now use this ALL THE TIME when writing code which is for one-time use or in unique situations, but where the process is complex enough to be difficult to work with line by line in the interactor. I use VS Code to edit the file and then Ctrl-G to run it.  I need to remember to save the file in VS Code before switching the focus back to Slicer, into the python interactor, and then hitting Ctrl-G, followed by the return key to run the file.</li>
</ol>
<p>I would probably use Text module code running similarly to the Ctrl-G method.  Advantages over Ctrl-G are:</p>
<ul>
<li>no need to change windows or focus, presumably a button in the Text module would just run execute the code in the Slicer environment</li>
<li>no need to save the edited text or reload a module before executing the code; hitting the “run code” button is the signal that you’re ready to try it as it is written</li>
</ul>
<p>Disadvantages vs Ctrl-G are:</p>
<ul>
<li>The Text module being open uses up the “module” panel.  When typing the code, I would very often want to refer to things in the Data module subject hierarchy (to see node names, mrml IDs, transform hierarchy info, perhaps node attributes, etc). I can imagine that I would often end up switching back and forth between the Data and Text modules in a way which might be less efficient than having the code up in a different window while I could examine the Data module at the same time as seeing the code.</li>
</ul>
<p>Time would tell whether it was more convenient to use the Text module code approach or the Ctrl-G + VS Code window approach. In any case, I would also  appreciate it if any code run via Ctrl-G or via the Texts module was logged in the history.  Currently, using the Ctrl-G approach, there is no way to see what was run when when looking back.</p>

---

## Post #11 by @pieper (2024-03-02 20:06 UTC)

<p>Here’s an experiment everyone should be able to try and if we like the approach we could flesh it out with more features like hotkeys, saving buffers to Text nodes, command history, etc.</p>
<p>The approach is to use the monaco editor, which is the core javascript code that runs in VSCode in a qSlicerWebWidget.  Since the python and javascript code can communicate its easy to send text buffers back and forth.</p>
<p>To try this you just need to paste this into your python console:</p>
<pre><code class="lang-auto">editor = slicer.qSlicerWebWidget()
editor.size = qt.QSize(900, 750)
editor.url = "https://pieper.github.io/SlicerEditor"
editor.show()
</code></pre>
<p>Then click the slicer icon to execute.</p>
<p>More info in the repository: <a href="https://github.com/pieper/SlicerEditor">https://github.com/pieper/SlicerEditor</a></p>

---

## Post #12 by @muratmaga (2024-03-02 20:43 UTC)

<p>This looks workable to me. Couple questions:</p>
<ol>
<li>
<p>When/if implemented will this still require an external URL to work, or the editor app would be fully local? Reaching out internet to work is always a challenge and potential obstacle in my particular work environment.</p>
</li>
<li>
<p>Would it be possible to highlight the code to be sent to console? (Currently it is sending everything).</p>
</li>
</ol>
<p>Otherwise, it seems fine to me with proper resizing of the window, some icons and shortcuts and ability to save the text buffers and retrieving them, it definitely fits the bill.</p>

---

## Post #13 by @pieper (2024-03-02 21:03 UTC)

<ol>
<li>
<p>Yes, it can be hosted from the Slicer WebServer if we want to bundle everything.  It’s not a huge amount of code but monaco has a lot of features like multiple language support that we may not want to carry along.</p>
</li>
<li>
<p>Yes, that <a href="https://github.com/pieper/SlicerEditor/commit/6b3b5dc155492635add7d277656166a37721cf92">is easy</a> - try refreshing.  For now it sends the selection if there is one, otherwise the full buffer.  It could be a separate button if we want.</p>
</li>
</ol>

---

## Post #14 by @pieper (2024-03-02 21:25 UTC)

<p>I think the one thing that would keep me from using this a lot would be the lack of autocomplete (the tab pop-up menu we have in the python console). For that we could either expose the <a href="https://github.com/commontk/CTK/blob/master/Libs/Scripting/Python/Widgets/ctkPythonConsole.h#L123">ctkPythonConsoleCompleter</a> or just reimplement it in python and hook it into monaco.</p>

---

## Post #15 by @muratmaga (2024-03-02 22:27 UTC)

<p>When incorporated, it will be nice if Edit button in Developer mode opens the module codes in this too (or people can continue to register their own preferred editors)</p>

---

## Post #16 by @cpinter (2024-03-04 16:02 UTC)

<p>This is amazing <a class="mention" href="/u/pieper">@pieper</a> ! I’ll use it a bit and see what could be next.</p>
<p><a class="mention" href="/u/mikebind">@mikebind</a> I wish I knew about the Ctrl-G combination earlier <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #17 by @Robert_Leo (2024-03-05 19:13 UTC)

<p>I’m excited about the potential of integrating a simple code editor within Slicer’s Text module. The ability to directly execute Python code from a lightweight editor would streamline the development process, especially for quick prototyping and testing. I agree that features like code highlighting and indentation support would be invaluable for beginners and experienced users alike. The idea of embedding an existing editor like VS Code sounds promising, but I appreciate the concern about keeping the solution lightweight. Looking forward to seeing how this feature evolves!</p>

---

## Post #18 by @pieper (2024-03-05 20:03 UTC)

<p><a class="mention" href="/u/robert_leo">@Robert_Leo</a> did you try the SlicerEditor demo linked above?  It already integrates the core editor features of vscode to run code.  It does not yet integrated with the Texts module but that would be very doable.</p>

---

## Post #19 by @oothomas (2024-06-12 21:12 UTC)

<p>Hi. I think I would like to work on this new feature during Project Week as well. I’ve created a draft project page:</p>
<p><a href="https://github.com/NA-MIC/ProjectWeek/issues/1128" rel="noopener nofollow ugc">Project: Simple Editor for Python Scripting · Issue #1128 · NA-MIC/ProjectWeek (github.com)</a></p>

---

## Post #20 by @muratmaga (2024-10-03 15:49 UTC)

<p>For posterity, this functionality is now available as an extension called ScriptEditor. See:</p>
<aside class="quote" data-post="17" data-topic="37806">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extension-scripteditor-a-simple-programming-editor/37806/17">New extension: ScriptEditor - a simple programming editor</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    Slightly revised version of this extension is now on the catalogue. The name was changed to ScriptEditor to avoid confusion with Segment Editor.
  </blockquote>
</aside>


---
