# How to get onClick a qt.QComboBox() in a table?

**Topic ID**: 10222
**Date**: 2020-02-12
**URL**: https://discourse.slicer.org/t/how-to-get-onclick-a-qt-qcombobox-in-a-table/10222

---

## Post #1 by @john123 (2020-02-12 16:51 UTC)

<p>I am using <code>qt.QTableWidget()</code> with 2 columns. The first column contains checkbox, while the second column is a <code>qt.QComboBox()</code>. I want to get the event when the user select the item in the <code>qt.QComboBox()</code>. How should I achieve it with Slicer and python?</p>
<pre><code class="lang-auto">        for i in range(4):            
            checkbox = qt.QTableWidgetItem()
            checkbox.setCheckState(False)    
            self.table.setItem(i,0,checkbox)

            self.combo = qt.QComboBox()
            self.combo.addItem("Item 1")
            self.combo.addItem("Item 2")              
            self.combo.setCurrentIndex(0)
            self.table.setCellWidget(0, 1, self.combo)        
</code></pre>

---

## Post #2 by @john123 (2020-02-13 16:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>: Could you please give me some hints to do it?</p>

---

## Post #3 by @jamesobutler (2020-02-13 17:57 UTC)

<p>Hi John,</p>
<p>As this is a question about using Qt, I would suggest you become familar with the Qt documentation as it is really helpful for determining available signals that a widget might have. I’m recommending this method because this was how I was able to learn! Here’s the link to the signals for a QComboBox - <a href="https://doc.qt.io/archives/qt-5.10/qcombobox.html#signals" rel="nofollow noopener">https://doc.qt.io/archives/qt-5.10/qcombobox.html#signals</a>. Other widgets can easily be searched with lots of helpful links on the various pages.</p>
<p>Once you know the type of signal to use then using it in python, as available through PythonQt, works like such:</p>
<pre><code class="lang-python">def myIndexChanged(index):
  print("ComboBox index changed to {}".format(index))

combo = qt.QComboBox()
combo.addItems(["Item 1", "Item 2"])
combo.currentIndexChanged.connect(myIndexChanged)
</code></pre>
<p>Hopefully this example and information helps you get acquainted with using Qt from python <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>

---
