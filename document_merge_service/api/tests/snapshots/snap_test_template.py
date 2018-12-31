# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_template_list[Test Name-docx-template] 1"] = {
    "count": 1,
    "next": None,
    "previous": None,
    "results": [{"engine": "docx-template", "name": "Test Name", "template": None}],
}

snapshots[
    "test_template_merge_docx[TestNameTemplate-docx-template-template__template0] 1"
] = """<w:body xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml">
  <w:p>
    <w:pPr>
      <w:pStyle w:val="Normal"/>
      <w:rPr/>
    </w:pPr>
    <w:r>
      <w:rPr>
        <w:lang w:val="de-CH" w:eastAsia="zh-CN" w:bidi="hi-IN"/>
      </w:rPr>
      <w:t>Test</w:t>
    </w:r>
    <w:r>
      <w:rPr>
        <w:lang w:val="de-CH" w:eastAsia="zh-CN" w:bidi="hi-IN"/>
      </w:rPr>
      <w:t xml:space="preserve">: Test input</w:t>
    </w:r>
  </w:p>
  <w:sectPr>
    <w:type w:val="nextPage"/>
    <w:pgSz w:w="11906" w:h="16838"/>
    <w:pgMar w:left="1134" w:right="1134" w:header="0" w:top="1134" w:footer="0" w:bottom="1134" w:gutter="0"/>
    <w:pgNumType w:fmt="decimal"/>
    <w:formProt w:val="false"/>
    <w:textDirection w:val="lrTb"/>
    <w:docGrid w:type="default" w:linePitch="240" w:charSpace="0"/>
  </w:sectPr>
</w:body>
"""

snapshots[
    "test_template_merge_docx[TestNameMailMerge-docx-mailmerge-template__template1] 1"
] = """<w:body xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml">
  <w:p>
    <w:pPr>
      <w:pStyle w:val="Normal"/>
      <w:rPr/>
    </w:pPr>
    <w:r>
      <w:rPr>
        <w:lang w:val="de-CH" w:eastAsia="zh-CN" w:bidi="hi-IN"/>
      </w:rPr>
      <w:t>Test</w:t>
    </w:r>
    <w:r>
      <w:rPr>
        <w:lang w:val="de-CH" w:eastAsia="zh-CN" w:bidi="hi-IN"/>
      </w:rPr>
      <w:t xml:space="preserve">: {{ </w:t>
    </w:r>
    <w:r>
      <w:rPr>
        <w:lang w:val="de-CH" w:eastAsia="zh-CN" w:bidi="hi-IN"/>
      </w:rPr>
      <w:t xml:space="preserve">test </w:t>
    </w:r>
    <w:r>
      <w:rPr>
        <w:lang w:val="de-CH" w:eastAsia="zh-CN" w:bidi="hi-IN"/>
      </w:rPr>
      <w:t>}}</w:t>
    </w:r>
  </w:p>
  <w:sectPr>
    <w:type w:val="nextPage"/>
    <w:pgSz w:w="11906" w:h="16838"/>
    <w:pgMar w:left="1134" w:right="1134" w:header="0" w:top="1134" w:footer="0" w:bottom="1134" w:gutter="0"/>
    <w:pgNumType w:fmt="decimal"/>
    <w:formProt w:val="false"/>
    <w:textDirection w:val="lrTb"/>
    <w:docGrid w:type="default" w:linePitch="240" w:charSpace="0"/>
  </w:sectPr>
</w:body>
"""
