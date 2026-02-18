# Looping through ctk.ctkCollapsibleButton widgets

**Topic ID**: 2895
**Date**: 2018-05-23
**URL**: https://discourse.slicer.org/t/looping-through-ctk-ctkcollapsiblebutton-widgets/2895

---

## Post #1 by @brhoom (2018-05-23 08:47 UTC)

<p>Dear all,<br>
I am trying to access ctk.ctkCollapsibleButton, I tried different things but nothing works. The goal is to creating/editing/removing objects during  the loading function of the python plugin. Here is something I tried:</p>
<pre><code> class myPluginWidget(ScriptedLoadableModuleWidget):
          def setup(self):
                print("=======================================================")   
                print("  myPlugin Title     ")
                print("=======================================================")           
                ScriptedLoadableModuleWidget.setup(self)
                self.initMainPanel()

          def initMainPanel(self):
                print(" initMainPanel ")   

                self.mainClpsBtn = ctk.ctkCollapsibleButton()
                self.mainClpsBtn.text = "my Plugin Title"
                self.layout.addWidget(self.mainClpsBtn)
                self.mainFormLayout = qt.QFormLayout(self.mainClpsBtn)

                self.pEDt= qt.QLineEdit()            
                self.pEDt.setText("some Text")
                self.mainFormLayout.addRow(  self.pEDt )
              
                self.runBtn = qt.QPushButton("Run")
                self.mainFormLayout.addRow(self.runBtn)

                items = (self.mainFormLayout.itemAt(i) for i in range(self.mainFormLayout.count())) 
                print(items)
                for w in items:
                     print(w.widget())
</code></pre>
<p>The output is</p>
<pre><code>        None
        None
</code></pre>
<p>I tried:</p>
<pre><code>                     print(w)
</code></pre>
<p>The out put is:</p>
<pre><code>       &lt;generator object &lt;genexpr&gt; at 0x7fa27003f690&gt;
       QLayoutItem (C++ Object 0x6877ee0)
       QLayoutItem (C++ Object 0x68f3270)
</code></pre>
<p>Same happened when I replaced self.mainFormLayout with self.layout. How can I get the type of the widget example QLineEdit or QPushButton and access their properties?</p>

---

## Post #2 by @pieper (2018-05-23 12:10 UTC)

<p>I don’t think PythonQt handles that level of runtime polymorphism - the w.widget() call should return a QWidget but it would need to be mapped back to the specific subtype.  You could try with pure PythonQt and see if that’s a bug or a known limitation of the wrapping.</p>
<p>In any case it’s probably best to keep explicit python references to the widgets you want to manipulate, e.g. a list of QPushButton instances and then you can access them directly.</p>

---

## Post #3 by @brhoom (2018-05-23 12:45 UTC)

<p>Thanks for your reply. I will go for the list idea for now.</p>

---

## Post #4 by @lassoan (2018-05-23 16:34 UTC)

<p>I would not recommend to delete any Qt widgets, as it is extremely difficult to do it correctly. You can hide any widgets that you don’t need (instead of deleting them); and show them if you need them again (instead of re-creating them).</p>

---

## Post #5 by @brhoom (2018-05-23 16:49 UTC)

<p>Thanks for the suggestion, I will consider this.</p>

---
