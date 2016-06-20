<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=gb2312">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 15">
<meta name=Originator content="Microsoft Word 15">
<link rel=File-List href="sqlalchemy架构翻译.files/filelist.xml">
<link rel=Edit-Time-Data href="sqlalchemy架构翻译.files/editdata.mso">
<!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]--><!--[if gte mso 9]><xml>
 <o:DocumentProperties>
  <o:Author>Zhiqiang He</o:Author>
  <o:LastAuthor>Hzq</o:LastAuthor>
  <o:Revision>2</o:Revision>
  <o:TotalTime>1681</o:TotalTime>
  <o:Created>2016-04-26T04:22:00Z</o:Created>
  <o:LastSaved>2016-04-26T04:22:00Z</o:LastSaved>
  <o:Pages>1</o:Pages>
  <o:Words>3142</o:Words>
  <o:Characters>17913</o:Characters>
  <o:Lines>149</o:Lines>
  <o:Paragraphs>42</o:Paragraphs>
  <o:CharactersWithSpaces>21013</o:CharactersWithSpaces>
  <o:Version>15.00</o:Version>
 </o:DocumentProperties>
 <o:OfficeDocumentSettings>
  <o:RelyOnVML/>
  <o:AllowPNG/>
 </o:OfficeDocumentSettings>
</xml><![endif]-->
<link rel=themeData href="sqlalchemy架构翻译.files/themedata.thmx">
<link rel=colorSchemeMapping href="sqlalchemy架构翻译.files/colorschememapping.xml">
<!--[if gte mso 9]><xml>
 <w:WordDocument>
  <w:DisplayBackgroundShape/>
  <w:TrackMoves>false</w:TrackMoves>
  <w:TrackFormatting/>
  <w:PunctuationKerning/>
  <w:DrawingGridVerticalSpacing>7.8 磅</w:DrawingGridVerticalSpacing>
  <w:DisplayHorizontalDrawingGridEvery>0</w:DisplayHorizontalDrawingGridEvery>
  <w:DisplayVerticalDrawingGridEvery>2</w:DisplayVerticalDrawingGridEvery>
  <w:ValidateAgainstSchemas/>
  <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>
  <w:IgnoreMixedContent>false</w:IgnoreMixedContent>
  <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>
  <w:DoNotPromoteQF/>
  <w:LidThemeOther>EN-US</w:LidThemeOther>
  <w:LidThemeAsian>ZH-CN</w:LidThemeAsian>
  <w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>
  <w:Compatibility>
   <w:SpaceForUL/>
   <w:BalanceSingleByteDoubleByteWidth/>
   <w:DoNotLeaveBackslashAlone/>
   <w:ULTrailSpace/>
   <w:DoNotExpandShiftReturn/>
   <w:AdjustLineHeightInTable/>
   <w:BreakWrappedTables/>
   <w:SnapToGridInCell/>
   <w:WrapTextWithPunct/>
   <w:UseAsianBreakRules/>
   <w:DontGrowAutofit/>
   <w:SplitPgBreakAndParaMark/>
   <w:EnableOpenTypeKerning/>
   <w:DontFlipMirrorIndents/>
   <w:OverrideTableStyleHps/>
   <w:UseFELayout/>
  </w:Compatibility>
  <m:mathPr>
   <m:mathFont m:val="Cambria Math"/>
   <m:brkBin m:val="before"/>
   <m:brkBinSub m:val="&#45;-"/>
   <m:smallFrac m:val="off"/>
   <m:dispDef/>
   <m:lMargin m:val="0"/>
   <m:rMargin m:val="0"/>
   <m:defJc m:val="centerGroup"/>
   <m:wrapIndent m:val="1440"/>
   <m:intLim m:val="subSup"/>
   <m:naryLim m:val="undOvr"/>
  </m:mathPr></w:WordDocument>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <w:LatentStyles DefLockedState="false" DefUnhideWhenUsed="false"
  DefSemiHidden="false" DefQFormat="false" DefPriority="99"
  LatentStyleCount="371">
  <w:LsdException Locked="false" Priority="0" QFormat="true" Name="Normal"/>
  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 1"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 2"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 3"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 4"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 5"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 6"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 7"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 8"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 9"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 9"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 1"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 2"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 3"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 4"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 5"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 6"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 7"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 8"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 9"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footnote text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="header"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footer"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index heading"/>
  <w:LsdException Locked="false" Priority="35" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="caption"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="table of figures"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="envelope address"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="envelope return"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footnote reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="line number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="page number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="endnote reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="endnote text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="table of authorities"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="macro"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="toa heading"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 5"/>
  <w:LsdException Locked="false" Priority="10" QFormat="true" Name="Title"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Closing"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Signature"/>
  <w:LsdException Locked="false" Priority="1" SemiHidden="true"
   UnhideWhenUsed="true" Name="Default Paragraph Font"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Message Header"/>
  <w:LsdException Locked="false" Priority="11" QFormat="true" Name="Subtitle"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Salutation"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Date"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text First Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text First Indent 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Note Heading"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Block Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Hyperlink"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="FollowedHyperlink"/>
  <w:LsdException Locked="false" Priority="22" QFormat="true" Name="Strong"/>
  <w:LsdException Locked="false" Priority="20" QFormat="true" Name="Emphasis"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Document Map"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Plain Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="E-mail Signature"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Top of Form"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Bottom of Form"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal (Web)"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Acronym"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Address"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Cite"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Code"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Definition"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Keyboard"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Preformatted"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Sample"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Typewriter"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Variable"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal Table"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation subject"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="No List"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Contemporary"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Elegant"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Professional"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Subtle 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Subtle 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Balloon Text"/>
  <w:LsdException Locked="false" Priority="39" Name="Table Grid"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Theme"/>
  <w:LsdException Locked="false" SemiHidden="true" Name="Placeholder Text"/>
  <w:LsdException Locked="false" Priority="1" QFormat="true" Name="No Spacing"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 1"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 1"/>
  <w:LsdException Locked="false" SemiHidden="true" Name="Revision"/>
  <w:LsdException Locked="false" Priority="34" QFormat="true"
   Name="List Paragraph"/>
  <w:LsdException Locked="false" Priority="29" QFormat="true" Name="Quote"/>
  <w:LsdException Locked="false" Priority="30" QFormat="true"
   Name="Intense Quote"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 1"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 1"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 2"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 2"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 2"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 3"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 3"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 3"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 4"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 4"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 4"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 5"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 5"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 5"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 6"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 6"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 6"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="19" QFormat="true"
   Name="Subtle Emphasis"/>
  <w:LsdException Locked="false" Priority="21" QFormat="true"
   Name="Intense Emphasis"/>
  <w:LsdException Locked="false" Priority="31" QFormat="true"
   Name="Subtle Reference"/>
  <w:LsdException Locked="false" Priority="32" QFormat="true"
   Name="Intense Reference"/>
  <w:LsdException Locked="false" Priority="33" QFormat="true" Name="Book Title"/>
  <w:LsdException Locked="false" Priority="37" SemiHidden="true"
   UnhideWhenUsed="true" Name="Bibliography"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="TOC Heading"/>
  <w:LsdException Locked="false" Priority="41" Name="Plain Table 1"/>
  <w:LsdException Locked="false" Priority="42" Name="Plain Table 2"/>
  <w:LsdException Locked="false" Priority="43" Name="Plain Table 3"/>
  <w:LsdException Locked="false" Priority="44" Name="Plain Table 4"/>
  <w:LsdException Locked="false" Priority="45" Name="Plain Table 5"/>
  <w:LsdException Locked="false" Priority="40" Name="Grid Table Light"/>
  <w:LsdException Locked="false" Priority="46" Name="Grid Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="Grid Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="Grid Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="46" Name="List Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="List Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="List Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 6"/>
 </w:LatentStyles>
</xml><![endif]-->
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:Helvetica;
	panose-1:2 11 6 4 2 2 2 2 2 4;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-536858881 -1073711037 9 0 511 0;}
@font-face
	{font-family:宋体;
	panose-1:2 1 6 0 3 1 1 1 1 1;
	mso-font-alt:SimSun;
	mso-font-charset:134;
	mso-generic-font-family:auto;
	mso-font-pitch:variable;
	mso-font-signature:3 680460288 22 0 262145 0;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:roman;
	mso-font-pitch:variable;
	mso-font-signature:-536870145 1107305727 0 0 415 0;}
@font-face
	{font-family:"Calibri Light";
	panose-1:2 15 3 2 2 2 4 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-1610611985 1073750139 0 0 415 0;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-536870145 1073786111 1 0 415 0;}
@font-face
	{font-family:"\@宋体";
	panose-1:2 1 6 0 3 1 1 1 1 1;
	mso-font-charset:134;
	mso-generic-font-family:auto;
	mso-font-pitch:variable;
	mso-font-signature:3 680460288 22 0 262145 0;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-parent:"";
	margin:0cm;
	margin-bottom:.0001pt;
	text-align:justify;
	text-justify:inter-ideograph;
	mso-pagination:none;
	font-size:10.5pt;
	mso-bidi-font-size:11.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:宋体;
	mso-fareast-theme-font:minor-fareast;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-font-kerning:1.0pt;}
p.MsoHeader, li.MsoHeader, div.MsoHeader
	{mso-style-priority:99;
	mso-style-link:"页眉 Char";
	margin:0cm;
	margin-bottom:.0001pt;
	text-align:center;
	mso-pagination:none;
	tab-stops:center 207.65pt right 415.3pt;
	layout-grid-mode:char;
	border:none;
	mso-border-bottom-alt:solid windowtext .75pt;
	padding:0cm;
	mso-padding-alt:0cm 0cm 1.0pt 0cm;
	font-size:9.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:宋体;
	mso-fareast-theme-font:minor-fareast;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-font-kerning:1.0pt;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
	{mso-style-priority:99;
	mso-style-link:"页脚 Char";
	margin:0cm;
	margin-bottom:.0001pt;
	mso-pagination:none;
	tab-stops:center 207.65pt right 415.3pt;
	layout-grid-mode:char;
	font-size:9.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:宋体;
	mso-fareast-theme-font:minor-fareast;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-font-kerning:1.0pt;}
p.MsoTitle, li.MsoTitle, div.MsoTitle
	{mso-style-priority:10;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-link:"标题 Char";
	mso-style-next:正文;
	margin-top:12.0pt;
	margin-right:0cm;
	margin-bottom:3.0pt;
	margin-left:0cm;
	text-align:center;
	mso-pagination:none;
	mso-outline-level:1;
	font-size:16.0pt;
	font-family:"Calibri Light",sans-serif;
	mso-ascii-font-family:"Calibri Light";
	mso-ascii-theme-font:major-latin;
	mso-fareast-font-family:宋体;
	mso-hansi-font-family:"Calibri Light";
	mso-hansi-theme-font:major-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:major-bidi;
	mso-font-kerning:1.0pt;
	font-weight:bold;}
a:link, span.MsoHyperlink
	{mso-style-noshow:yes;
	mso-style-priority:99;
	color:blue;
	text-decoration:underline;
	text-underline:single;}
a:visited, span.MsoHyperlinkFollowed
	{mso-style-noshow:yes;
	mso-style-priority:99;
	color:#954F72;
	mso-themecolor:followedhyperlink;
	text-decoration:underline;
	text-underline:single;}
code
	{mso-style-noshow:yes;
	mso-style-priority:99;
	mso-ansi-font-size:12.0pt;
	mso-bidi-font-size:12.0pt;
	font-family:宋体;
	mso-ascii-font-family:宋体;
	mso-fareast-font-family:宋体;
	mso-hansi-font-family:宋体;
	mso-bidi-font-family:宋体;}
pre
	{mso-style-priority:99;
	mso-style-link:"HTML 预设格式 Char";
	margin:0cm;
	margin-bottom:.0001pt;
	mso-pagination:widow-orphan;
	font-size:12.0pt;
	font-family:宋体;
	mso-bidi-font-family:宋体;}
p.MsoListParagraph, li.MsoListParagraph, div.MsoListParagraph
	{mso-style-priority:34;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	margin:0cm;
	margin-bottom:.0001pt;
	text-align:justify;
	text-justify:inter-ideograph;
	text-indent:21.0pt;
	mso-char-indent-count:2.0;
	mso-pagination:none;
	font-size:10.5pt;
	mso-bidi-font-size:11.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:宋体;
	mso-fareast-theme-font:minor-fareast;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-font-kerning:1.0pt;}
span.Char
	{mso-style-name:"页眉 Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:页眉;
	mso-ansi-font-size:9.0pt;
	mso-bidi-font-size:9.0pt;}
span.Char0
	{mso-style-name:"页脚 Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:页脚;
	mso-ansi-font-size:9.0pt;
	mso-bidi-font-size:9.0pt;}
span.Char1
	{mso-style-name:"标题 Char";
	mso-style-priority:10;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:标题;
	mso-ansi-font-size:16.0pt;
	mso-bidi-font-size:16.0pt;
	font-family:"Calibri Light",sans-serif;
	mso-ascii-font-family:"Calibri Light";
	mso-ascii-theme-font:major-latin;
	mso-fareast-font-family:宋体;
	mso-hansi-font-family:"Calibri Light";
	mso-hansi-theme-font:major-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:major-bidi;
	font-weight:bold;}
span.HTMLChar
	{mso-style-name:"HTML 预设格式 Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:"HTML 预设格式";
	mso-ansi-font-size:12.0pt;
	mso-bidi-font-size:12.0pt;
	font-family:宋体;
	mso-ascii-font-family:宋体;
	mso-fareast-font-family:宋体;
	mso-hansi-font-family:宋体;
	mso-bidi-font-family:宋体;
	mso-font-kerning:0pt;}
span.apple-converted-space
	{mso-style-name:apple-converted-space;
	mso-style-unhide:no;}
.MsoChpDefault
	{mso-style-type:export-only;
	mso-default-props:yes;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;}
 /* Page Definitions */
 @page
	{mso-page-border-surround-header:no;
	mso-page-border-surround-footer:no;
	mso-footnote-separator:url("sqlalchemy架构翻译.files/header.htm") fs;
	mso-footnote-continuation-separator:url("sqlalchemy架构翻译.files/header.htm") fcs;
	mso-endnote-separator:url("sqlalchemy架构翻译.files/header.htm") es;
	mso-endnote-continuation-separator:url("sqlalchemy架构翻译.files/header.htm") ecs;}
@page WordSection1
	{size:595.3pt 841.9pt;
	margin:72.0pt 90.0pt 72.0pt 90.0pt;
	mso-header-margin:42.55pt;
	mso-footer-margin:49.6pt;
	mso-paper-source:0;
	layout-grid:15.6pt;}
div.WordSection1
	{page:WordSection1;}
-->
</style>
<!--[if gte mso 10]>
<style>
 /* Style Definitions */
 table.MsoNormalTable
	{mso-style-name:普通表格;
	mso-tstyle-rowband-size:0;
	mso-tstyle-colband-size:0;
	mso-style-noshow:yes;
	mso-style-priority:99;
	mso-style-parent:"";
	mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
	mso-para-margin:0cm;
	mso-para-margin-bottom:.0001pt;
	mso-pagination:widow-orphan;
	font-size:10.5pt;
	mso-bidi-font-size:11.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-font-kerning:1.0pt;}
</style>
<![endif]--><!--[if gte mso 9]><xml>
 <o:shapedefaults v:ext="edit" spidmax="2049"/>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <o:shapelayout v:ext="edit">
  <o:idmap v:ext="edit" data="1"/>
 </o:shapelayout></xml><![endif]-->
</head>

<body bgcolor="#FFF2CC" lang=ZH-CN link=blue vlink="#954F72" style='tab-interval:
21.0pt;text-justify-trim:punctuation'>

<div class=WordSection1 style='layout-grid:15.6pt'>

<p class=MsoTitle><span lang=EN-US style='font-size:26.0pt'>SQLAlchemy<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>迈克·贝尔</span></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>是一个数据库工具包和基于</span><span lang=EN-US>Python</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>语言的对象关系映射系统，在</span><span lang=EN-US>2005</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>年被第一次介绍。最开始的时候，它追求在</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中提供一个端到端的系统来使用关系数据库，即用于数据库交互的</span><span
lang=EN-US>API</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>是可以直接被</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>调用的。即使在</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>发展的早期阶段，它的性能就吸引了很多关注。它的关键特征包括大量的对复杂数据库查询和对象映射的流畅处理，还有一个关于“工作单元”模式的实现，这个模式为数据库提供了一个高度自动化的可持续存储数据的系统。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>从一个小的、粗糙定义的概念开始，通过一系列的转变和改进迅速发展起来，尽管它的用户群不断增大，但它仍在反复考虑对它内部架构以及外部接口的优化。到</span><span
lang=EN-US>2009</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>年</span><span
lang=EN-US>1</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>月，</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><span
lang=EN-US>0.5</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本出来的时候，它已经开始假设一个可以证明</span><span
lang=EN-US>ta</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>处于多种产品部署的稳定形态了。通过</span><span
lang=EN-US>0.6</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>（</span><span
lang=EN-US>2010</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>年</span><span
lang=EN-US>4</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>月）和</span><span
lang=EN-US>0.7</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本（</span><span
lang=EN-US>2011</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>年</span><span
lang=EN-US>5</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>月），</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的架构和接口的进步增大了它达到最有效率且最稳定的系统的可能。从写这篇文章开始，</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>正被大量的组织在不同领域使用着，并被许多以事实为评判标准的</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>关系型数据库人员所考虑。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.1. </span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>数据库抽象的挑战</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>术语“数据库抽象”经常用来假定表示一个数据库通信系统，这个系统隐藏了主要的关于数据如何被存储和查询的细节。这个术语有时被带入一个极端，即这样一个系统不应该仅仅隐藏在使用中的关系数据库的细节，还应该隐藏数据库中的关系型结构的细节，甚至隐藏潜在的数据存储是否是关系型的。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>最普遍的关于对象关系映射系统的评论集中在一个假设上：这样的工具的主要目的是“隐藏”对关系型数据库的使用，掌握生成与数据库交互的任务以及把这个任务简化到一些实现细节上来。这个隐藏办法的中心是将设计和查询关系型结构的能力从开发人员那里拿走并交给一个不透明的黑箱子处理。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>那些深入了解关系型数据库的人知道这个方法是完全不切实际的。这个方法想使关系结构和数据库查询被极大地功能化，并包含应用核心的设计。然而这些结构在不同种类的查询（不仅仅是在需求的数据上的不同，还包括在想要的信息结构上的不同）中，应该怎样被设计、组织和操作呢？如果这个方面相关的具体设计使用被隐藏了，那么在最开始使用一个关系型数据库就没有任何意义。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>这个对潜在关系数据库的隐藏的追求和关系型数据库本身的需求的巨大差异经常被称为“对象关系阻抗失配”问题。而</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>多少为这个问题带来了新的解决方法。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-US
style='font-size:22.0pt;mso-bidi-font-size:11.0pt'>SQLAlchemy</span></b><b
style='mso-bidi-font-weight:normal'><span style='font-size:22.0pt;mso-bidi-font-size:
11.0pt;font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对数据库抽象的方法</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>主张开发者必须乐意考虑他</span><span lang=EN-US>/</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>她的数据的关系形式。一个预决定和隐藏模式、查询设计决策的系统排斥使用一个关系型数据库的有用性，导致所有的阻抗失配的经典问题。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>同时，这些决策的实现能够且应该通过水平尽可能高的模式来执行。关联对一个模式来说的对象模型且通过</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>查询来保持它，是一项重复性很高的任务。允许一些工具来自动化这些任务需要一个应用的开发，这个应用应该更简洁、更有能力且效率更高，并且在手动开发这些操作的过程中创建这个应用只需占用一小部分时间。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>为了这个目的，</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>自称它是一个工具包，来强调开发者作为所有关系型结构和这些结构与这个应用的联系的设计者</span><span
lang=EN-US>/</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>架构师的角色，而不是作为一个函数库的一个被动的用户。通过揭露相关概念，</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>信奉“漏洞抽象”的理念，鼓励开发者在应用和关系数据库之间剪裁一个定制的，完全自动化的交互层。</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的创新之处在于它允许了高度自动化但它没有减少对关系型数据库的控制。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.2. </span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>内核</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>/</span></b><b><span
style='font-size:26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";
mso-ascii-theme-font:major-latin;mso-hansi-font-family:"Calibri Light";
mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>对象关系映射二分法</span></b><b><span lang=EN-US
style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;mso-ascii-theme-font:
major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'><o:p></o:p></span></b></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>提供一个工具包方法的中心目标是作为一个丰富的接口，它暴露了数据库交互的每一层，将任务分成两个主要的部分叫做内核和对象关系映射。内核包括</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>数据库</span><span
lang=EN-US>API</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>交互，为数据库所理解的文本</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句的翻译，以及数据库集合的管理。这些特点都作为公共接口所提出。对象关系映射，是建立在内核之上的一个特殊的库。</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>提供的对象关系映射仅仅是许多可能的可以建立在内核上的对象抽象层中的一个，而许多开发者和开发组织直接在内核之上建立他们的应用程序。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
mso-fareast-font-family:宋体;color:#333333;mso-font-kerning:0pt;mso-no-proof:
yes'><v:shapetype id="_x0000_t75" coordsize="21600,21600" o:spt="75"
 o:preferrelative="t" path="m@4@5l@4@11@9@11@9@5xe" filled="f" stroked="f">
 <v:stroke joinstyle="miter"/>
 <v:formulas>
  <v:f eqn="if lineDrawn pixelLineWidth 0"/>
  <v:f eqn="sum @0 1 0"/>
  <v:f eqn="sum 0 0 @1"/>
  <v:f eqn="prod @2 1 2"/>
  <v:f eqn="prod @3 21600 pixelWidth"/>
  <v:f eqn="prod @3 21600 pixelHeight"/>
  <v:f eqn="sum @0 0 1"/>
  <v:f eqn="prod @6 1 2"/>
  <v:f eqn="prod @7 21600 pixelWidth"/>
  <v:f eqn="sum @8 21600 0"/>
  <v:f eqn="prod @7 21600 pixelHeight"/>
  <v:f eqn="sum @10 21600 0"/>
 </v:formulas>
 <v:path o:extrusionok="f" gradientshapeok="t" o:connecttype="rect"/>
 <o:lock v:ext="edit" aspectratio="t"/>
</v:shapetype><v:shape id="图片_x0020_1" o:spid="_x0000_i1040" type="#_x0000_t75"
 alt="http://www.aosabook.org/images/sqlalchemy/layers.png" style='width:340.5pt;
 height:324pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image001.png" o:title="layers"/>
</v:shape></span><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
mso-fareast-font-family:宋体;color:#333333;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:10.0pt;
font-family:宋体;mso-ascii-font-family:Helvetica;mso-hansi-font-family:Helvetica;
mso-bidi-font-family:Helvetica;color:#333333;mso-font-kerning:0pt'>图</span><span
lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
mso-fareast-font-family:宋体;color:#333333;mso-font-kerning:0pt'>20.1</span><span
style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:Helvetica;
mso-hansi-font-family:Helvetica;mso-bidi-font-family:Helvetica;color:#333333;
mso-font-kerning:0pt'>：</span><span lang=EN-US>SQLAlchemy</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>层的图解</span><span lang=EN-US
style='font-size:10.0pt;font-family:"Helvetica",sans-serif;mso-fareast-font-family:
宋体;color:#333333;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>内核</span><span
lang=EN-US>/</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象关系映射的划分已经成为</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的最典型的特点，这个特点有好的一面也有不好的一面。存在于</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中的明确的内核引导对象关系映射来关联映射数据库的类属性得到一个叫做“</span><span
lang=EN-US>Table</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>”的结构，而不是直接得到数据库表达的字符串列名；来用一个叫</span><span
lang=EN-US>select</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的结构生成一个选择查询，而不是将查询语句和目标属性直接拼接成一个字符串进行查询；来通过一个叫做</span><span
lang=EN-US>ResultProxy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的包装结构获得结果行，这显然将</span><span
lang=EN-US>select</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>结构映射到了每一个结果行，而不是从一个数据库指针到一个用户定义的对象直接传递数据。</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>内核元素在一个非常简单的以对象关系映射为中心的应用程序中可能是不可见的。然而，由</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>于内核是细致地集成于对象关系映射中来允许在对象关系映射和内核结构之间的数据流动传递，一个更加复杂的以对象关系映射为中心的应用程序可以下调一个或两个隐藏内核的级别来用一个更复杂的特殊的通过细致调整的方法处理数据库，正如现状需求的一样。随着</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>已经成熟，内核接口在定期使用时变得越来越不明确，因为对象关系映射继续提供更复杂和综合的模式。然而，内核的可用性也为</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>早期获得成功作出了一定贡献，因为当对象关系映射正在开发的时候它允许早期的用户来完成现在不可能完成的事情。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象关系映射</span><span
lang=EN-US>/</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>内核这种方法的负面影响是指令必须要经过更多步骤才能完成。</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的传统</span><span
lang=EN-US>C</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>实现对个人函数的调用有一个重大的不可避免的妨碍，这是</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>运行慢的原发性主因。传统的改善这个的方法包括通过重新处理和内联来缩短调用链，用</span><span
lang=EN-US>C</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>代码来替换临界性能的区域。</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>花费了许多年来使用这两种方法来提升性能。然而，越来越被人接受的</span><span
lang=EN-US>PyPy Python</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>解释器可能会保证抑制剩余的性能问题，这个解释器不需要将</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的内部构件的主要部分替换成</span><span
lang=EN-US>C</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>代码，因为</span><span
lang=EN-US>PyPy</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>解释器通过及时的内联和编译极大地减少了长调用链的影响。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.3. </span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>改良数据库应用程序接口系统</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'><o:p></o:p></span></b></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>本质上是一个通过数据库应用程序接口与数据库进行交互的一个系统。数据库应用程序接口本身不是一个实际存在的库，而只是一种规范。因此，数据库应用程序接口可以有针对性地为某个有特殊目标的数据库定制地实现，比如</span><span
lang=EN-US>MySQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>或</span><span
lang=EN-US>PostgreSQL</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，或者为非数据库应用程序接口的数据库适配器，例如</span><span
lang=EN-US>ODBC</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><span
lang=EN-US>JDBC</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>而定制地实现。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>数据库应用程序接口面临着两个挑战。第一个是为数据库应用程序接口的基本使用模式提供一个易于使用并且功能全面的外观模式。第二个是需要较好地处理数据库应用程序接口实现和潜在的数据库引擎的极端易变的特性。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-US
style='font-size:22.0pt;mso-bidi-font-size:11.0pt'>“</span></b><b
style='mso-bidi-font-weight:normal'><span style='font-size:22.0pt;mso-bidi-font-size:
11.0pt;font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>方言</span></b><b style='mso-bidi-font-weight:
normal'><span lang=EN-US style='font-size:22.0pt;mso-bidi-font-size:11.0pt'>”</span></b><b
style='mso-bidi-font-weight:normal'><span style='font-size:22.0pt;mso-bidi-font-size:
11.0pt;font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>系统（和别名之类的差不多）</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>数据库应用程序接口系统所描述的接口是极其简单的。它的核心组件包括数据库应用程序接口系统自己，连接对象，指针对象——一个数据库用语，代表一个特别的数据库语句的上下文和与它关联的结果。一个简单的这些对象之间的交互以及从一个数据库中查找数据的例子如下：</span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>connection = dbapi.connect(user=&quot;user&quot;,
pw=&quot;pw&quot;, host=&quot;host&quot;)<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>cursor = connection.cursor()<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>cursor.execute(&quot;select * from user_table where
name=?&quot;, (&quot;jack&quot;,))<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>print &quot;Columns in result:&quot;, [desc[0] for desc
in cursor.description]<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>for row in cursor.fetchall():<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp;
</span>print &quot;Row:&quot;, row<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>cursor.close()<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>connection.close()<o:p></o:p></span></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>创建了一个和经典数据库应用程序接口系统会话差不多的外观模式。这个外观模式的入口是</span><span
lang=EN-US>create_engine</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>函数的调用，调用之后数据库连接和相关配置信息就装配了。一个</span><span
lang=EN-US>Engine</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的实例就是产生的结果。这个对象就代表数据库应用程序接口系统的入口，但它自己并没有直接表现出来。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对于简单的语句执行，</span><span
lang=EN-US>Engine</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>提供了一个“模糊执行”的接口。捕获和关闭一个数据库应用程序接口系统连接和指针的行为都在这样的场景之后执行：</span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>engine = create_engine(&quot;postgresql://user:pw&amp;#64;host/dbname&quot;)<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>result = engine.execute(&quot;select * from table&quot;)<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>print result.fetchall()<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>当</span><span
lang=EN-US>SQLAlchemy0.2</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>出来的时候，</span><span
lang=EN-US>Connection</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象就加进来了，提供了明确维护数据库应用程序接口系统连接的作用域的能力：</span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>conn = engine.connect()<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>result = conn.execute(&quot;select * from table&quot;)<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>print result.fetchall()<o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-bottom:6.75pt;text-align:left;
line-height:13.5pt;mso-pagination:widow-orphan;tab-stops:45.8pt 91.6pt 137.4pt 183.2pt 229.0pt 274.8pt 320.6pt 366.4pt 412.2pt 458.0pt 503.8pt 549.6pt 595.4pt 641.2pt 687.0pt 732.8pt;
background:whitesmoke;word-break:break-all'><span lang=EN-US style='font-size:
9.0pt;font-family:"Courier New";mso-fareast-font-family:宋体;color:#333333;
mso-font-kerning:0pt'>conn.close()<o:p></o:p></span></p>

<p class=MsoNormal><span lang=EN-US>Engine</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>或</span><span lang=EN-US>Connection</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象的</span><span lang=EN-US>execute</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>函数返回的结果叫做一个</span><span lang=EN-US>ResultProxy</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>（结果代理）对象，它提供了一个与</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>指针相似的接口，但拥有更丰富的行为。</span><span
lang=EN-US>Engine</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，</span><span
lang=EN-US>Connection</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><span
lang=EN-US>ResultProxy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>分别是</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>组件的一个实例，特定</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>连接的一个实例和特定</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>指针的一个实例。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在这些场景的幕后，</span><span
lang=EN-US>Engine</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>类参照一个叫</span><span
lang=EN-US>Dialect</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的对象。</span><span
lang=EN-US>Dialect</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>是一个抽象类，许多类实现了它，每一个实现都是为了某个特定</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>或数据库的结合。为一个</span><span
lang=EN-US>Engine</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>创建的一个</span><span
lang=EN-US>Connection</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>将会指向这个</span><span
lang=EN-US>Dialect</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象来作出所有的决策，这些决策依赖于具体的</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>目标和使用中的数据库将会有不同的行为。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>Connection</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象一创建，就会从叫做</span><span lang=EN-US>Pool</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的资源库获得并维护一个实际的</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>连接，这个资源库</span><span
lang=EN-US>Pool</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>也与</span><span
lang=EN-US>Engine</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>相联系。</span><span
lang=EN-US>Pool</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>资源库负责创建新的</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>连接，通常还负责在内存池里维护这些连接来应对频繁的复用。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在一个语句的执行期间，一个额外的叫做</span><span
lang=EN-US>ExecutionContext</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的对象被</span><span
lang=EN-US>Connection</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>所创建。这个对象的生存周期从执行那个点开始一直贯穿</span><span
lang=EN-US>ResultProxy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的生存周期。这个对象也可以作为一个特殊的子类获得，用作一些</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和数据库方面的结合所需。</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>图</span><span
lang=EN-US>20.2</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>阐释了所有这些对象以及他们之间的相互关系以及和</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>组件之间的关系：</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
mso-fareast-font-family:宋体;color:#333333;mso-font-kerning:0pt;mso-no-proof:
yes'><v:shape id="图片_x0020_2" o:spid="_x0000_i1039" type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/engine.png"
 style='width:397.5pt;height:337.5pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image002.png" o:title="engine"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.2:Engine</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，</span><span lang=EN-US>Connection</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，</span><span lang=EN-US>ResultProxy API</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>处理</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'>DBAPI</span></b><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的可变性</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>为了处理</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>行为的可变性，首先我们考虑这个难题的作用域。</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>规范，当前在版本</span><span
lang=EN-US>2</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，被描述成一系列的</span><span
lang=EN-US>API</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>定义，这些定义允许一个在数据库行为上的较宽范围的可变性，并剩下了许多未定义的领域。最后，现实的</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>展示了在几个领域的很大的可变性，包括什么时候</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><span
lang=EN-US>unicode</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>字符串是可接受的以及什么时候它们是不可接受的；“</span><span
lang=EN-US>last inserted id</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>”（最新插入的</span><span
lang=EN-US>id</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>）——就是说，一个自动生成的主键——可能怎样在一个</span><span
lang=EN-US>insert</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句执行后被获得；以及有范围的参数的值可能怎样被指定和解读。它们也可能有大量的特殊的适应类型的行为，包括对二进制，精度小数，日期，布尔类型，以及</span><span
lang=EN-US>unicode</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>数据的处理。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>通过多层次的子类化来允许</span><span lang=EN-US>Dialect</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>和</span><span lang=EN-US>ExecutionContext</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>这两个对象的可变性，从而实现以上所说的处理。图</span><span
lang=EN-US>20.3</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>阐释了当以</span><span
lang=EN-US>psycopg2</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的方式使用</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>时</span><span
lang=EN-US>Dialect</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><span
lang=EN-US>ExecutionContext</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>两个类之间的关系。</span><span
lang=EN-US>PGDialect</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>类提供了一些行为，这些行为是针对</span><span
lang=EN-US>PostgreSQL</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>数据库的使用的，比如</span><span
lang=EN-US>ARRAY</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>数据类型和</span><span
lang=EN-US>schema</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>目录；</span></p>

<p class=MsoNormal><span lang=EN-US>PGDialect_psycopg2</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>这个类提供了一些针对</span><span lang=EN-US>psycopg2
DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的行为，包括</span><span
lang=EN-US>unicode</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>数据的处理器和服务器端的指针。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
mso-fareast-font-family:宋体;color:#333333;mso-font-kerning:0pt;mso-no-proof:
yes'><v:shape id="图片_x0020_3" o:spid="_x0000_i1038" type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/dialect-simple.png"
 style='width:352.5pt;height:314.25pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image003.png" o:title="dialect-simple"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.3</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：简单的</span><span lang=EN-US>Dialect/ExecutionContext</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>层</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>当处理一个支持多数据库的</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>时，一个上面所说的模式的变体就出现了。这样的例子包括</span><span
lang=EN-US>pyodbc</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，它通过</span><span
lang=EN-US>ODBC</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>处理任意多的数据库后端；以及</span><span
lang=EN-US>zxjdbc</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，一个只支持</span><span
lang=EN-US>Jython</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的处理</span><span
lang=EN-US>JDBC</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的驱动。随着一个</span><span
lang=EN-US>sqlalchemy.connectors</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>包中的混合类的使用，以上的关系是增广的，这个包提供了</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的多后端的普遍的一些行为。图</span><span
lang=EN-US>20.4</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>显示了</span><span
lang=EN-US>sqlalchemy.connectors.pyodbc</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>为</span><span lang=EN-US>MySQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>和</span><span lang=EN-US>Microsoft SQL
Server</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在特定</span><span
lang=EN-US>pyodbc</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><span
lang=EN-US>dialect</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>间共享的一些普遍的函数。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
mso-fareast-font-family:宋体;color:#333333;mso-font-kerning:0pt;mso-no-proof:
yes'><v:shape id="图片_x0020_4" o:spid="_x0000_i1037" type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/common-dbapi.png"
 style='width:414.75pt;height:258pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image004.png" o:title="common-dbapi"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.4</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：共享于</span><span lang=EN-US>dialect</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>层的普遍的</span><span lang=EN-US>DBAPI</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>行为</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.4. </span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>模式定义</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>随着数据库的连接和交互的建立，下一个任务是要规定后端不可知的</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句的创建和操纵。要达到这个目标，我们首先需要定义我们将怎样引用存在于一个数据库中的表和列——即模式。表和列代表了数据是如何组织的，并且大多数由表达式和命令组成的</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句引用了这些结构。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>一个对象关系映射或数据访问层需要提供编程访问</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语言的途径；在底层就是一个描述表和元组的可编程系统。这就是</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>提供的第一个强大的对于核心和对象关系映射的分割，通过提供</span><span
lang=EN-US>Table</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><span
lang=EN-US>Column</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>两个类来描述数据库的结构且独立于用户模型的类定义。把模式定义从对象关系映射分割出来的基本原理是关系模式可以按照关系数据库被清晰地设计，包括限定平台的细节（如果需要的话），不需要被对象关系的概念搞得一团糟——这样保持了一个分离的关系。独立于对象关系映射组件也意味着模式描述系统只是对任何其他种类的对象关系系统有用，而这些系统可能会建立在核心之上。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>Table</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>和</span><span lang=EN-US>Column</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>模型被归入叫做“元数据”的范围，元数据提供了容器对象叫做</span><span
lang=EN-US>MetaData</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>来代表一个</span><span
lang=EN-US>Table</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象的集合。这个结构主要从</span><span
lang=EN-US>Martin FowLer</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><span
lang=EN-US>Patterns of Enterprise Application Architecture</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>一书中关于“元数据映射”的描述中推断出来。图</span><span
lang=EN-US>20.5</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>显示了</span><span
lang=EN-US>sqlalchemy.schema</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>包中的一些重要元素。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_28" o:spid="_x0000_i1036"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/basic-schema.png"
 style='width:415.5pt;height:339.75pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image005.png" o:title="basic-schema"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.5</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：基本的</span><span lang=EN-US>sqlalchemy.schema</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象</span></p>

<p class=MsoNormal><span lang=EN-US>Table</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>代表一个实际出现在一个目标</span><span lang=EN-US>schema</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的表的名称和其他属性。它的</span><span lang=EN-US>Column</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象集合表示表中单独的列的名称和类型信息。一组完整的描述了约束，下标，以及序列的对象用于填充更多的细节，它们中的一些会影响引擎和</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>构造系统的一些行为。特别地，</span><span
lang=EN-US>ForeignKeyConstraint</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>这个类对确定两个表如何连接是极为重要的。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>Schema</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>包中的</span><span lang=EN-US>Table</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>和</span><span lang=EN-US>Column</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>相对于其他包来说是独一无二的，且它们是双继承的，</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>都从</span><span
lang=EN-US>sqlalchemy.shema</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><span
lang=EN-US>sqlalchemy.sql.expression</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>包中继承，不仅作为</span><span lang=EN-US>schema</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>水平的结构来提供服务，而且作为</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句的核心语法来提供服务。这个关系显示在图</span><span
lang=EN-US>20.6</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_27" o:spid="_x0000_i1035"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/table-column-crossover.png"
 style='width:415.5pt;height:121.5pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image006.png" o:title="table-column-crossover"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.6</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：</span><span lang=EN-US>Table</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>和</span><span lang=EN-US>Column</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>类的双继承</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在图</span><span
lang=EN-US>20.6</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中我们可以看到</span><span
lang=EN-US>Table</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><span
lang=EN-US>Column</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>从</span><span
lang=EN-US>sql</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>包中继承。作为“你可以从它里面查询”的一种特殊形式，称作</span><span
lang=EN-US>FromClause</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，以及作为“你可以在一个</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达式中使用的东西”，称作</span><span
lang=EN-US>ColumnElement</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.5. SQL</span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>表达式</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在</span><span
lang=EN-US>SQLalchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的开发期间，生成</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的方法是不清晰的。一个文本语言可能有一个可能的候选</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句；这是一个普遍的方法，这个方法处于著名的像</span><span
lang=EN-US>Hibernate</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><span
lang=EN-US>HQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>这样的对象关系工具的核心。然而对</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语言来说，有个更加有趣的选择：那就是使用</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的对象和表达式来生成表达树结构，甚至重定义</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的操作符以至赋予这些操作符</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句的行为。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>虽然它可能不是第一个这样做的工具，但是包含在</span><span
lang=EN-US>Bicking</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><span
lang=EN-US>SQLObject</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中的</span><span
lang=EN-US>SQLBuilder</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>库有着高度可信度，因为</span><span
lang=EN-US>Sqlalchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的语言表示中使用了</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象和操作符机制这个妙计。用这个方法，</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象表示一个</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句的词汇部分。这些</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象拥有的方法，以及重载的操作符，生成了来源于这些对象的新的词汇结构。最常见的对象是</span><span
lang=EN-US>Column</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象——</span><span
lang=EN-US>SQLObject</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在一个对象关系映射的类中通过</span><span
lang=EN-US>.q</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>属性用一个命名空间存取来表现这些；</span><span
lang=EN-US>SQLalchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>把那个属性命名为</span><span
lang=EN-US>.c</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>。这个</span><span
lang=EN-US>.c</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>属性到今天依然在核心可选择的元素中被维护着，比如那些有代表性的表和查询语句。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达树</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>如果你正解析一个</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句，一个</span><span
lang=EN-US>SQLalchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达结构非常符合你创建的那个类型——它是一个分析树，除开发者直接创建分析树之外，其他人都是从一个字符串得到它。这个分析树中的结点的核心类型叫做</span><span
lang=EN-US>ClauseElement</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，图</span><span
lang=EN-US>20.7</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>显示了</span><span
lang=EN-US>ClauseElement</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和一些重要的类之间的关系。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_26" o:spid="_x0000_i1034"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/expression-hierarchy.png"
 style='width:415.5pt;height:265.5pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image007.png" o:title="expression-hierarchy"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.7</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：基本的表达层</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>通过构造函数、方法和重写</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>操作符的使用，为一个像这样的</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>SELECT id FROM user WHERE name = ?<o:p></o:p></span></pre>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>创建的结构可能会在</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中像这样被创建：</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>from sqlalchemy.sql import table, column, select<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>user = table('user', column('id'), column('name'))<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>stmt = select([user.c.id]).where(user.c.name=='ed')<o:p></o:p></span></pre>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>上面的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>select</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>结构的构造显示在图</span><span
lang=EN-US>20.8</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中。注意字面值</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>'ed'</span></code><span class=apple-converted-space><span
lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333'>&nbsp;</span></span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的表示包含在</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>_BindParam</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的构造中，因此导致它作为一个有范围限制的参数标记被提出，且在</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句字符串中用一个问号来表示。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_25" o:spid="_x0000_i1033"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/example-expression.png"
 style='width:339pt;height:183.75pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image008.png" o:title="example-expression"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.8</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：表达树的例子</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>从属性图我们可以看到，一个简单的下行的对节点的遍历就可以迅速创建一个解析过的</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表述，我们将会在语句编译那一节看到更深入的细节。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-US
style='font-size:22.0pt;mso-bidi-font-size:11.0pt'>Python</span></b><b
style='mso-bidi-font-weight:normal'><span style='font-size:22.0pt;mso-bidi-font-size:
11.0pt;font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>操作符方法</span></b><b style='mso-bidi-font-weight:
normal'><span lang=EN-US style='font-size:22.0pt;mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在</span><span
lang=EN-US>SQLalchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中，一个像这样的表达式：</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>column('a') == 2<o:p></o:p></span></pre>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>产生的结果要么</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>True</span></code><span class=apple-converted-space><span
lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333'>&nbsp;</span></span><span class=apple-converted-space><span
style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:Helvetica;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Helvetica;mso-bidi-font-family:Helvetica;color:#333333'>要么</span></span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>False</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，但是替代了一个</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达式的构造。这样的根本实现是使用</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的特殊的操作符函数机制来重载操作符：例如像</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>__eq__</span></code><span lang=EN-US style='font-size:10.0pt;
font-family:"Helvetica",sans-serif;color:#333333'>,<span
class=apple-converted-space>&nbsp;</span></span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>__ne__</span></code><span
lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333'>,<span class=apple-converted-space>&nbsp;</span></span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>__le__</span></code><span lang=EN-US style='font-size:10.0pt;
font-family:"Helvetica",sans-serif;color:#333333'>,</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>__lt__</span></code><span lang=EN-US style='font-size:10.0pt;
font-family:"Helvetica",sans-serif;color:#333333'>,<span
class=apple-converted-space>&nbsp;</span></span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>__add__</span></code><span
lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333'>,<span class=apple-converted-space>&nbsp;</span></span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>__mul__</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>之类的方法。面向列的表达式节点通过一个叫</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>ColumnOperators</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的类提供了重载</span><span lang=EN-US>Python</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>操作符的行为。使用操作符重载，表达式</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>column('a') == 2</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>就等同于：</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>from sqlalchemy.sql.expression import _BinaryExpression<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>from sqlalchemy.sql import column, bindparam<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>from sqlalchemy.operators import eq<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><o:p>&nbsp;</o:p></span></pre><pre style='margin-bottom:6.75pt;
line-height:13.5pt;background:whitesmoke;word-break:break-all'><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#333333'>_BinaryExpression(<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp; </span>left=column('a'),<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp; </span>right=bindparam('a', value=2, unique=True),<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp; </span>operator=eq<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>)<o:p></o:p></span></pre>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>eq</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>构造实际上是一个发源于</span><span lang=EN-US>Python</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>内置的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>operator</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>中的一个函数。作为一个对象（也就是</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>operator.eq</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>）而不是一个字符串（也就是</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>=</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>）来代表操作符允许字符串表示在语句编译时被定义，当数据库方言已知的时候。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>编译</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>负责将文本</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句解析成</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达树的中心类是</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Compiled</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>这个类。这个类有两个主要的子类，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>SQLCompiler</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>和</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>DDLCompiler</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>类。</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>SQLCompiler</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>类翻译</span><span lang=EN-US>SQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的操作字段，这些字段有</span><span lang=EN-US>SELECT</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，</span><span lang=EN-US>INSERT</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，</span><span lang=EN-US>UPDATE</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>和</span><span lang=EN-US>DELETE</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>语句，共同地被分类为</span><span lang=EN-US>DQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>（</span><span lang=EN-US>data query language</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>）和</span><span lang=EN-US>DML</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>（</span><span lang=EN-US>data manipulation
language</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>）。而</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>DDLCompiler</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>处理各种各样的</span><span lang=EN-US>CREATE</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>和</span><span lang=EN-US>DROP</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>语句，被分类为</span><span lang=EN-US>DDL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>（</span><span lang=EN-US>data definition
language</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>）。还有个额外的类层专注于字符串表示的类型，这个类层起始于</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>TypeCompiler</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>类。独特的数据库方言之后提供它们自己的所有三种编译器类型的子类来针对目标数据库定义</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的语言方面。图</span><span
lang=EN-US>20.9</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>提供了一个关于</span><span
lang=EN-US>PostgreSQL</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>方言的这个类层的概观。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_24" o:spid="_x0000_i1032"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/compiler-hierarchy.png"
 style='width:328.5pt;height:241.5pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image009.png" o:title="compiler-hierarchy"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.9</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：编译器层，包括</span><span lang=EN-US>PostgreSQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>特有的实现</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Compiled</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的子类定义了一系列的访问函数，每个函数都被一个特殊的子类</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>ClauseElement</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>关联着。一个</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>ClauseElement</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>节点层被遍历并且一个语句通过递归连接每一个访问函数的输出字符串的方式被构造出来。由于这个过程，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Compiled</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象维护了匿名标识符名称、有限制范围的参数名和子查询的嵌套的一个状态，在其他事情中，所有的这些都是为了一个字符串</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句和有限制范围和默认值的参数的一个最终集合的产生。图</span><span
lang=EN-US>20.10</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>显示了访问函数作用于文本单元的过程。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_23" o:spid="_x0000_i1031"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/statement-compilation.png"
 style='width:415.5pt;height:117.75pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image010.png" o:title="statement-compilation"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.10</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：调用一个语句编译层</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>一个完全的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Compiled</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>结构包含整个</span><span lang=EN-US>SQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>字符串和有限制范围的值的集合。这些被一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>ExecutionContext</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象强制保证为</span><span lang=EN-US>DBAPI</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>execute</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>方法期盼的格式，这个格式包括像这样的注意事项：一个声明为</span><span
lang=EN-US>unicode</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象的处理，用于存储有限制范围的值的集合的类型，以及有限制范围的值如何比较它们自己的细节应该强制为适合</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和目标数据库相应表示出来。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.6. </span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>类映射和</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>ORM<o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>我们现在把注意力移到</span><span
lang=EN-US>ORM</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>上来。第一个目标是使用我们定义的元数据表去允许把用户定义的类映射到一个数据库表中元组的集合上去。第二个目标是允许用户定义的类间的关系的定义，这个定义是基于一个数据库中表之间的关系的。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>经典的</span><span
lang=EN-US> vs. </span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>声明式的</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>我们用术语“经典映射”来指</span><span
lang=EN-US>SQLalchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的允许一个对象关系的数据映射到一个出现的用户类的系统。这中形式考虑了</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Table</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象和用户定义的类来成为两个独立定义的实体，这两个实体通过函数</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>来连接在一起。</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>一旦</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>被应用到一个用户定义的类，那么这个类就会呈现出于表中的元组相一致的属性：</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>class User(object):<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp; </span>pass<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><o:p>&nbsp;</o:p></span></pre><pre style='margin-bottom:6.75pt;
line-height:13.5pt;background:whitesmoke;word-break:break-all'><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#333333'>mapper(User, user_table)<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><o:p>&nbsp;</o:p></span></pre><pre style='margin-bottom:6.75pt;
line-height:13.5pt;background:whitesmoke;word-break:break-all'><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#333333'># now User has an &quot;.id&quot; attribute<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>User.id<o:p></o:p></span></pre>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Mapper</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>函数也可以给类添加其他的属性，包括与其他种类的对象相一致的属性，还包括任意的</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达式。添加任意属性到一个类中的机制在</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中被称为“</span><span
lang=EN-US>monkeypatching</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>”；然而，由于我们正在用一个数据驱动和非任意的方式来做这件事，这个操作的精髓最好用术语</span><span
lang=EN-US>class instrumentation</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>现代的以声明扩展为中心的</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的使用，是一个与许多其他对象关系工具使用的普遍的像动作记录一样地类声明系统相似的结构的系统。在这个系统中，最终用户用类定义明确地定义了内嵌的属性，每一个内嵌属性都表示在这个类上被映射的属性。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Table</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象，大部分情况下，没有被明确地被提及，它也不是</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中的函数；只有这个类，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Column</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象，和其他</span><span
lang=EN-US>ORM</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>相关的属性被命名了：</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>class User(Base):<o:p></o:p></span></pre><pre style='margin-bottom:
6.75pt;line-height:13.5pt;background:whitesmoke;word-break:break-all'><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#333333'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp; </span>__tablename__ = 'user'<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp; </span>id = Column(Integer, primary_key=True)<o:p></o:p></span></pre>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>上面可能出现类仪器（</span><span
lang=EN-US>class instrumentation</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>）通过我们的配置</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>id = Column()</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>被直接获得的情况，但是事实不是这样的。声明扩展使用了一个</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的元类，这是一种每当一个新类被第一次声明时就运行一系列操作的很方便的方式，来从被声明的类中生成一个新的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Table</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象，并将这个对象随着这个类传递到</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>函数中。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>函数之后就用一模一样的方式做它的工作，将它自己的属性添加到这个类中，这种情况下朝向</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>id</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>属性，并将以前存在的替换掉。到元类初始化完成的时候（即当执行流离开</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>描绘的块的时候），被</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>id</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>标记的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Column</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象就已经被移动到一个新的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Table</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中了，并且</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User.id</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>已经被一个针对这个映射的新的属性所替代了。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>总打算要有个可速记的、声明的配置形式。然而，声明的创建为了有利于接下来的工作被延迟了，同时固化了经典映射的结构。一个叫做</span><span
lang=EN-US>ActiveMapper</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的临时性扩展，在早期就出现了，之后成为了</span><span
lang=EN-US>Elixir</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>项目。它在一个高水平的声明系统中重定义了映射结构。声明的目标是通过建立一个几乎精确保存</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>经典映射概念的系统来颠倒</span><span
lang=EN-US>Elixir</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的大量抽象出来的方法的方向，这个声明只是认识到它们如何被用来减少冗长和增多对类水平扩展的适应，相比一个经典的映射来说。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>无论使用的是经典的还是声明式的映射，一个被映射的类都会呈现新的允许它根据它的属性表达</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>结构的行为。</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>最初跟着</span><span
lang=EN-US>SQLObject</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的行为：使用一个特殊的属性作为</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>元组表达的来源，这个属性被</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>称作</span>
<code><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#DD1144;background:#F7F7F9'>.c</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>，像下面这个例子一样：</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>result = session.query(User).filter(User.c.username == 'ed').all()<o:p></o:p></span></pre>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>然而在</span><span
lang=EN-US>0.4</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本，</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>将这个功能移到被映射的属性自己身上了：</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>result = session.query(User).filter(User.username == 'ed').all()<o:p></o:p></span></pre>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>这个在属性存取上的变化结果是一个很大的改善，因为它允许像元组的对象出现在这个类中来获得额外的针对类的能力，而不是直接出现在那些起源于底层的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Table</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象的类中。它也允许在不同类属性之间的集成使用，例如直接引用表中元组的属性，引用来源与那些元组的</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达式的属性，以及引用一个相关类的属性。最后，它提供了一个在映射的类之间的一个对称性，和一个映射的类的实例，在这个实例中同样的属性依赖于父属性的类型将呈现不同的行为。与类绑定的属性返回</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达式，而与实例绑定的属性返回实际的数据。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>一个映射的剖析</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>与我们的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>类绑定的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>id</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>属性是一类在</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中叫做描述符的对象，它有</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>__get__</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>，</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>__set__</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>和</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>__del__</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>方法，</span><span lang=EN-US>Python</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>运行时为所有涉及这个属性的类和实例听从这个属性。</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的实现被称作一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>InstrumentedAttribute</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>，并且我们将用另一个例子阐释这个外观模式幕后的世界。以一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Table</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象和一个用户定义的类开始，我们建立了一个只有一个被映射的元组的映射，以及一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>relationship</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象，它定义了一个对相关类的引用：</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>user_table = Table(&quot;user&quot;, metadata,<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp; </span>Column('id', Integer, primary_key=True),<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>)<o:p></o:p></span></pre><pre style='margin-bottom:6.75pt;
line-height:13.5pt;background:whitesmoke;word-break:break-all'><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#333333'><o:p>&nbsp;</o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>class User(object):<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp; </span>pass<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><o:p>&nbsp;</o:p></span></pre><pre style='margin-bottom:6.75pt;
line-height:13.5pt;background:whitesmoke;word-break:break-all'><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#333333'>mapper(User, user_table, properties={<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp; </span>'related':relationship(Address)<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>})<o:p></o:p></span></pre>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>当一个映射完成了，这个与类相关的对象的结构的细节就显示在图</span><span
lang=EN-US>20.11</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_22" o:spid="_x0000_i1030"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/mapper-components.png"
 style='width:566.25pt;height:354.75pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image011.png" o:title="mapper-components"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.11</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：一个映射的剖析</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>这个图显示了一个</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>映射解释为在用户自定义类和它被映射到的元数据表之间交互的两个隔离层。类仪器是朝左边画的，而</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和数据库函数是朝右边画的。一般模式是：对象组合用来隔绝行为的角色，对象继承用来区分一个特别的角色的行为差异。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在类仪器的领域，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>ClassManager</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>与被映射的类相连接，而它的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>InstrumentedAttribute</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象集合与每一个类中的被映射的属性相连接。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>InstrumentedAttribute</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>也是之前提到的面向公共的</span><span lang=EN-US>Python</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>描述符，当在一个基于类的表示中使用的时候（例如</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User.id==5</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>），它还产生</span><span lang=EN-US>SQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>表达式。当处理一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的实例时，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>InstrumentedAttribute</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>将那个属性的行为委托给一个</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>AttributeImpl</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象，这个对象是针对被映射的数据类型定制的几个品种之一。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在映射这一方面，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象代表一个用户定义的类和一个可选择单元的连接，最典型的就是</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Table</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>维护了一个每个属性的对象集合叫做</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>MapperProperty</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>，这个集合处理</span><span lang=EN-US>SQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对特殊属性的表示。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>MapperProperty</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>最普遍的变体是</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>ColumnProperty</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，它代表一个映射的元组或</span><span lang=EN-US>SQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>表达式，和</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>RelationshipProperty</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，它代表一个与其他映射的连接。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>MapperProperty</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>将加载属性的行为——包括属性如何在一个</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句中呈现和它如何从一个结果行中被填充——委托给一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>LoaderStrategy</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象，这个对象有几个变体。不同的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>LoaderStrategies</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>决定一个属性的加载行为是否被推迟，饥饿，或立即执行。在映射配置时会选择一个默认版本，有在查询时使用一个轮流策略的选项。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>RelationshipProperty</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>也引用了一个</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>DependencyProcessor</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>类，这个类处理在刷新时映射之间的依赖性和属性同步应该如何进行。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>DependencyProcessor</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的选择基于相关的与关系连接的父亲和目标可选性的几何结构。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Mapper</span></code><span
lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333'>/</span><code><span lang=EN-US style='font-size:9.0pt;
font-family:"Courier New";color:#DD1144;background:#F7F7F9'>RelationshipProperty</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>结构形成了一个图，在这个图中，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象是节点，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>RelationshipProperty</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>是有向边。一旦一个应用程序声明了一整套映射，一个推迟的叫做配置过程的“初始化”步骤就开始进行了。它主要被每个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>RelationshipProperty</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>用来集结在它的父类和目标映射之间的细节，包括</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>AttributeImpl</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>以及</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>DependencyProcessor</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的选择。这个图是一个关键数据结构，它的使用贯穿了整个</span><span
lang=EN-US>ORM</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的操作。它参与操作，比如叫“</span><span
lang=EN-US>cascade</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>”的行为，定义操作如何通过对象路径传播，在查询操作中相关对象和集合在哪里被马上“饥饿”载入，以及在对象刷新方面，开始一系列持续步骤前，一个所有对象的依赖图在哪里被创建。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.7. </span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>查询和装载行为</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'><o:p></o:p></span></b></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>通过</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Query</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象启动所有的装载对象行为。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Query</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>以之开始的基本状态包括实体，就是映射的类的列表和</span><span
lang=EN-US>/</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>或要查询的个体</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达式。它也有对</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>类的引用，这个类代表与一个或多个数据库的连接，以及一个关于在这些连接上处理累计的数据缓冲。下面是一个基本的使用示例：</span></p>

<pre style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>from sqlalchemy.orm import Session<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>session = Session(engine)<o:p></o:p></span></pre><pre
style='margin-bottom:6.75pt;line-height:13.5pt;background:whitesmoke;
word-break:break-all'><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#333333'>query = session.query(User)<o:p></o:p></span></pre>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>我们创建了一个将会向</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的实例屈服的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Query</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象，这个对象与一个新的我们创建的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象有关。</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Query</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>提供了一个有生产力的建筑者模式，用的是和之前讨论的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>select</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>结构同样的方式，在这种方式中每一次一个方法被调用，额外的标准和修改器就和一个声明结构联系起来。当一个迭代的操作在</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Query</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中被调用时，它就会建立一个</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达式结构来代表一个</span><span
lang=EN-US>SELECT</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，将它发送给数据库，然后将结果集的行解释为面向</span><span
lang=EN-US>ORM</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的结果，并与被要求的实体的初始集相一致。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Query</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>使得很难区分操作的</span><span lang=EN-US>SQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>解析和数据加载两个部分。前者指一个</span><span
lang=EN-US>SELECT</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句的构造，后者指将</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>结果行解释为</span><span
lang=EN-US>ORM</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>映射的结构。数据加载实际上不需要</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>解析步骤就可以进行，但是</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Query</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>可能会被要求从一个用户手写的文本查询语句中解析结果。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>SQL</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>解析和数据加载都利用了对一系列重要的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象形成的图的自顶向下的遍历，把每个元组的或每个</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>表达式所承担的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>ColumnProperty</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>看作一个叶节点，把每个通过“</span><span lang=EN-US>eager-load</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>”包含在</span><span lang=EN-US>query</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>中的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>RelationshipProperty</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>看作一条指向另一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>节点的有向边。最后遍历和在每个节点采取的行动就是每个连接每个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>MapperProperty</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>LoaderStrategy</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的工作，它把元组和连接加到在</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>编译阶段产生的</span><span
lang=EN-US>SELECT</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句中，并产生出在数据加载阶段处理结果行的</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>函数。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>这些</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>函数在数据加载阶段产生，当它们被调用时，每个函数都收到一个数据库行，结果在内存中的一个映射的属性的声明上产生可能的变化。它们为一个特殊的属性富有条件地被产生出来，基于第一个在结果集中的行，以及基于加载的选项。如果属性的一个加载没有进行，那么就不会有相应的函数产生。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>图</span><span
lang=EN-US>20.12</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>显示了在一个贪心连接的加载策略下几个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>LoaderStrategy</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象的遍历，显示了它们与一个编译后的</span><span lang=EN-US>SQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>语句的连接，这个连接在</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Query</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>compile_context</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>方法中出现。它也显示了结果行处理函数的生成，这些函数接收结果行并填充个体对象的属性，这个过程出现在</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Query</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>instances</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>方法中。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_21" o:spid="_x0000_i1029"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/query-loading.png"
 style='width:562.5pt;height:453.75pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image012.png" o:title="query-loading"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.12</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：包括贪心连接加载的加载策略的遍历</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的早期填充结果的方法是使用一个传统的与每个策略连接的混合对象方法遍历，来接收每个行并根据这些来处理。首先在</span><span
lang=EN-US>0.5</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本中介绍的不可赎回的加载器系统，导致了性能方面戏剧性的增长，因为它的许多决策考虑了行处理能只预先进行一次，而不是为每个行都进行一次，以及大量的无效的函数调用应该被淘汰。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.8. </span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>会话</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>/</span></b><b><span
style='font-size:26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";
mso-ascii-theme-font:major-latin;mso-hansi-font-family:"Calibri Light";
mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>身份映射</span></b><b><span lang=EN-US
style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;mso-ascii-theme-font:
major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象显示了为</span><span lang=EN-US>ORM</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的实际使用而准备的公共接口——也就是，加载和维护数据。它为一个给定的数据库连接的查询和持续操作提供了起始点。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象，除作为数据库连通性的入口之外，它还维护了一个活动的对所有映射实体的引用，这些存在于内存中的实体是与这个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象相关的。</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>为恒等映射和工作单元模式实现的一个外观就是用这种方式实现的，恒等映射和工作单元模式都被</span><span
lang=EN-US>Fowler</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>鉴定过。恒等映射为一个特殊的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>维护了一个有着独一无二身份数据库的所有对象的映射，消除了二重身份带来的问题。工作单元在恒等映射上建立，提供了一个用尽可能有效的方式自动化所有的在数据库中变化的维护过程的系统。实际的持续性步骤叫做“</span><span
lang=EN-US>flush</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>”，在现代的</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中这个步骤通常是自动化的。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>发展历史</span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>是作为一个对发出一个</span><span lang=EN-US>flush</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的单任务负责的主要隐蔽的系统开始的。</span><span
lang=EN-US>Flush</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>过程包括发出</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句给数据库，保持对象的状态变化与工作单元系统的一致性，从而同步数据库现在的状态和内存中的状态。</span><span
lang=EN-US>Flush</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>总是</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中最复杂的操作之一。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>Flush</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>操作的调用在很早的版本中在一个叫</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>commit</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的方法后面开始，它是一个出现在一个含蓄的、本地线程的叫做</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>objectstore</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的对象中的方法。当你使用</span><span lang=EN-US>SQLAlchemy0.1</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>时，不需要调用</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Session.add</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>方法，也不需要一个明确的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>概念。只需要创建</span><span lang=EN-US>mappers</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，创建新的对象，编辑出现的对象通过</span><span
lang=EN-US>queries</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>加载（在</span><span
lang=EN-US>queries</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>自己被直接从</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象调用的地方），然后提交所有的改变，通过</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>objectstore.commit</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>方法。为一个操作集合准备的对象池是无条件地全局模块的，并且无条件本地线程的。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>objectstore.commit</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>方法是一个即时的操作，第一批用户使用它，但是这个模块的健壮性迅速地撞墙了。现代</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的新用户有时哀叹为</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象定义一个工厂，可能一个注册的需求，以及为每个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>组织他们的对象的需求，但是这比早期的更为可取，早期整个系统都是完全不明确的。</span><span
lang=EN-US>0.1</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本使用模式的方便仍然保持在现代的</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中，现代</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>以会话注册的正常配置为特点来使用本地范围的线程。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>自己仅在</span><span lang=EN-US>0.2</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>版本介绍，宽松地模仿出现在</span><span lang=EN-US>Hibernate</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>中的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象。这个版本以集成事务处理的控制为特点，在这里</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象可以通过</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>begin</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>方法被放置在一个事务中，并通过</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>commit</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>方法完成</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>。</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>objectstore.commit</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>方法重命名为</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>objectstore.flush</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，新的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象可以在任意时刻创建。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>自己从另一个叫</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>UnitOfWork</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的对象中消除，这个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>UnitOfWork</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象作为一个对执行实际的</span><span lang=EN-US>flush</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>操作负责的私有对象被维护。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>当</span><span
lang=EN-US>flush</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>过程作为一个被用户明确调用的方法开始的时候，</span><span
lang=EN-US>0.4</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本介绍了</span><span
lang=EN-US>autoflush</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的概念，即一个</span><span
lang=EN-US>flush</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在每个</span><span
lang=EN-US>query</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>之前就开始。</span><span
lang=EN-US>Autoflush</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的优势是被一个</span><span
lang=EN-US>query</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>发出的</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句总是可以访问相关的存在于内存中的确切状态，因为所有的变化都发送出去了。早期的版本没有这个特点，因为最普遍的使用模式是</span><span
lang=EN-US>flush</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>声明也永久提交变化。但是当</span><span
lang=EN-US>autoflush</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>被引进时，伴随有另一个特点叫做事务型的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>，它提供了一个</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，这个</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>将自动在一个在用户明确调用</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>commit</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>之前维护的事务中调用。随着这个特点的引进，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>flush</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>方法不再提交它冲刷的数据，而可以在一个自动化的底层被安全的调用。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>现在可以提供一个逐步的在内存和</span><span lang=EN-US>SQL</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>查询状态之间的同步，它通过必要时</span><span
lang=EN-US>flush</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，直到明确的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>commit</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>步骤才永久地存留做到这一点。实际上，这个行为准确地说和</span><span
lang=EN-US>java</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本的</span><span
lang=EN-US>Hibernate</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>是一样的。然而，</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>包含这个使用风格，基于和</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本的</span><span
lang=EN-US>Storm ORM</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>一样的行为，是在</span><span
lang=EN-US>0.3</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本引入的。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>0.5</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>版本带来了更多的事务处理集成，这时</span><span lang=EN-US>post-transaction
expiration</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>被引入了；在每个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>commit</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>或</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>rollback</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>之后，通过在消除</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>时默认定义所有的状态，来又一次移动到相应地方，当</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>子查询语句重复查询数据时，或者当过期的对象属性在新的事务的上下文需要访问时。起初，</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>是围绕这个假想创建的：</span><span
lang=EN-US>SELECT</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句应该无条件地尽可能少地发射出。提交时到期的行为因为这个原因而延迟了；然而，它完全地解决了</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>问题，这个</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>包含过期数据和滞后的事务处理，没有简单的方法来加载新数据时而不重建已经加载的所有对象集合。在早期，看起来这个难题不能被合理地解决，因为当</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>应该考虑现在将过期的状态时这个问题是不明显的，因此需要为下一次访问生产一个昂贵代价的新的</span><span
lang=EN-US>SELECT</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句对象集合。然而，一旦</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>移动到一个总是在一个事务处理中的模型时，事务处理的结束点就会表面化，相对数据终结的自然点来说因为一个高度隔离的事务的性质是它直到它被提交或者回滚了才能看到新的数据。不同的数据库和配置，当然有不同的事务隔离程度，包括根本就没有事务处理的情况。这些使用模式完全可以被</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的期满模式所接受；开发者只需要知道一个低程度隔离的水平可能曝光非孤立的改变在一个会话中，如果多会话分享同样的数据行的话。这和直接使用两个数据库连接将发生的有着根本的不同。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>会话概述</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>图</span><span
lang=EN-US>20.13</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>显示了一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>和它处理的私有结构。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_20" o:spid="_x0000_i1028"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/session-overview.png"
 style='width:580.5pt;height:238.5pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image013.png" o:title="session-overview"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.13</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：会话概述</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>面向公共的部分的上面是</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>自己和用户对象的集合，它们中的每一个都是一个映射类的实例。这儿我们可以看见映射的对象保持了对一个叫做</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>InstanceState</span></code><span lang=EN-US> </span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的</span><span lang=EN-US>SQLAlchemy</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>结构的引用，这个结构为一个个体的实例追踪了</span><span
lang=EN-US>ORM</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>状态，包括待定的属性变化和属性的生存周期状态。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>InstanceState</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>是之前某节讨论到的属性</span><span lang=EN-US>instrumentation</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的实例水平上的方面，那一节是“一个映射的解析”，在类水平上与</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>ClassManager</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>相关，并维护了映射的对象的字典状态（例如</span><span lang=EN-US>Python
</span><code><span lang=EN-US style='font-size:9.0pt;font-family:"Courier New";
color:#DD1144;background:#F7F7F9'>__dict__</span></code><span lang=EN-US> </span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>属性）为了与这个类联系起来的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>AttributeImpl</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>状态追踪</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>IdentityMap</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>是一个到</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>InstanceState</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象数据库实体的映射，为了那些有数据库特性的对象，这个特性是持久稳固的。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>IdentityMap</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的默认实现是和</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>InstanceState</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>一起自我管理它的大小，通过移除用户映射的实例，一旦所有对它们的强引用被移除时——用这种方式它和</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>WeakValueDictionary</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>是同样的工作模式。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>保护所有标记为</span><span lang=EN-US>dirty</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>或</span><span lang=EN-US>deleted</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的对象集合，以及待定的从垃圾集合来的标记为</span><span
lang=EN-US>new</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的对象，</span>
<span style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:
minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;
mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>通过创建对那些待定改变的对象的强引用。所有的强引用都会在</span><span
lang=EN-US>flush</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>后丢弃。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>InstanceState</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>也执行鉴定维护“什么被改变了”的任务，为一个特殊对象的属性，使用一个一改变就动作的系统，这个系统在设定到来的值到对象现在的字典之前在一个叫</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>committed_state</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的字典中存储了一个特殊属性的“之前的”值。在</span><span
lang=EN-US>flush</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>时，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>committed_state</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的内容和与这个对象联系起来的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>__dict__</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的内容就会比较以产生在每个对象上的净改变集合。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在集合的情况下，一个分离的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>collections</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>包和</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>InstrumentedAttribute</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>或</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>InstanceState</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>系统协调来维护一个特殊映射的对象集合的净改变集合。普通的</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>类例如</span><span
lang=EN-US>set</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，</span><span
lang=EN-US>list</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><span
lang=EN-US>dict</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在使用和用历史追踪的</span><span
lang=EN-US>mutator</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>方法增广之前都是子集。这个集合系统在</span><span
lang=EN-US>0.4</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本被重写以变得可扩充的和可用的为任何像集合的对象。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>事务处理的控制</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，在它的默认使用状态，为所有完成的操作维护了一个开放的事务，当</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>commit</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>或</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>rollback</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>被调用的时候。</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>SessionTransaction</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>维护了一个</span><span lang=EN-US>0</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的集合或者更多</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Connection</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象，每个都代表一个在一个特殊的数据库上的开放的事务。</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>SessionTransaction</span></code><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>是一个懒惰初始化的对象，它以无出现的数据库状态开始。作为一个被需要用来参加语句执行处理的后端，一个与那个数据库相关的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Connection</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象要被加到</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>SessionTransaction</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的链接列表中。当一个一次单独的连接是普遍的，而多连接的方案也是支持的，当决定基于与</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Table</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>或者这个操作中的</span><span
lang=EN-US>SQL</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>结构自己联系的配置，为一个特殊的操作使用特殊的连接时。多连接也可以使用双相的行为调整事务，为那些提供这个行为的</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.9. </span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>工作单元</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'><o:p></o:p></span></b></p>

<p class=MsoNormal><code><span lang=EN-US style='font-size:9.0pt;font-family:
"Courier New";color:#DD1144;background:#F7F7F9'>Session</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>提供的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>flush</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>方法将它的工作移交给一个隔离的模块叫做</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>unitofwork</span></code><span class=apple-converted-space><span
style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:Helvetica;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Helvetica;mso-bidi-font-family:Helvetica;color:#333333'>。</span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>正如前面提到的，</span><span lang=EN-US>flush</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>过程可能是</span><span lang=EN-US>SQLAlchemy</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>中最复杂的功能。</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>工作单元的工作是将所有出现在一个特殊的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>里的待定状态移出到数据库中，腾空这个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>维护的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>new</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>dirty</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>deleted</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>集合。一旦完成，</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的内存中状态和出现在现在的事务中的状态就匹配了。主要的挑战是决定正确的一系列的持续步骤，然后用正确的顺序执行它们。这个包括决定</span><span
lang=EN-US>INSERT</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，</span><span
lang=EN-US>UPDATE</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><span
lang=EN-US>DELETE</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句的列表，包括那些被删除或修改的行需要连坐的结果；确保</span><span
lang=EN-US>UPDATE</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句仅包含那些实际编辑的列；建立同步操作，即将要把主键列的状态复制到引用的外键列的操作，在那时新生成的主键指针就可以获得了；确保</span><span
lang=EN-US>INSERT</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>操作按对象加入</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Session</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的顺序发生，并且尽可能有效率；以及确保</span><span lang=EN-US>UPDATE</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>和</span><span lang=EN-US>DELETE</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>语句以确定性顺序发生，来减少死锁的机会。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>历史</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>工作单元这个实现是从一个业务方式的以特定方式写的复杂系统开始的；它的开发可以和在没有地图的情况下从一个森林里找出一条路相比较。早期的</span><span
lang=EN-US>bug</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和遗忘的行为用补丁修复了，</span><span
lang=EN-US>0.5</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本重构了几次代码改善了一些事情，直到</span><span
lang=EN-US>0.6</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>版本工作单元才具有时间稳定性，很好的理解性，并且被几百个测试覆盖——可以完全地从头重写。在许多周的考虑以一致数据结构的新方法驱动时后，重写它的进程就是使用这个几天产生的新的模型，因为这个想法可以很好被理解。新实现的行为可以被很认真地交叉检查这个事实也支持了出现的版本。这个过程展示了第一个迭代，然而可怕地，是如何仍然有价值的，只要它提供了一个工作模型。它更展示了一个子系统总的重写如何不仅仅经常适当，并且是一个很难开发的系统中的集成部分。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:22.0pt;mso-bidi-font-size:11.0pt;font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>拓扑排序</span></b><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:22.0pt;
mso-bidi-font-size:11.0pt'><o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在工作单元背后的主要范例是装配行为的整个列表来形成一个数据结构，这个结构中每个节点代表一个单独的步骤；在设计模式用语中它叫做命令模式。这个结构中的一系列的“命令”用拓扑排序组成一个特殊的顺序。一个拓扑排序是将事物基于一个局部排序来排序的过程，即，只有确定的元素必须排在其他的元素前面。图</span><span
lang=EN-US>20.14</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>显示了拓扑排序的行为。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_19" o:spid="_x0000_i1027"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/topological-sort.png"
 style='width:545.25pt;height:318pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image014.png" o:title="topological-sort"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.14</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：拓扑排序</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>工作单元建立了一个局部排序基于那些必须排在其他命令前面的持续性命令。这些命令之后被拓扑排序，并按顺序调用。一个命令优先与另一个命令的决定主要从一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>relationship</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>推断而来，这个</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>relationship</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>是两个</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>Mapper</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>对象的桥梁——通常，一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>被认为是依赖与另一个。相似的规则也对多对多的关联表适用，但这里我们仅关注一对多和多对一的情况。外键依赖需要解决为了预防违规的约束，且不依赖需要将约束标志为“延期的”。但顺序允许主键识别符同样重要，这个在许多平台都只是生成的，当一个</span><span
lang=EN-US>INSERT</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>实际发生的时候，来从一个刚刚执行的</span><span
lang=EN-US>INSERT</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>语句的结果粒子性增加到一个非独立的行的将要插入的参数列表。对于删除，同样的顺序相反地被使用——非独立的行在那些它们依赖的行之前删除，当这些行由于没有它们的外键的引用而不能再出现时。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>工作单元以一个拓扑排序表现在两个不同层面的系统为特点，基于出现的非独立结构。第一个层面将持续性的步骤组织成桶基于映射间的非独立性，即，满桶的与一个特别的类相关的对象。第二个层面打碎</span><span
lang=EN-US>0</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>或更多这样的桶分为更小的一批，来处理环形引用或自引用表的情况。图</span><span
lang=EN-US>20.15</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>显示了“桶”生成来插入一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象的集合，然后一个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Address</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象的集合，一个中间步骤在这个集合中复制新的生成的</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>主键的值到每个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Address</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>user_id</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>外键元组中。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_18" o:spid="_x0000_i1026"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/uow-mapper-buckets.png"
 style='width:244.5pt;height:345.75pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image015.png" o:title="uow-mapper-buckets"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.15</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：通过映射组织对象</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>在每个映射排序的情况，若干</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Address</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>对象可以被</span><span lang=EN-US>flush</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>，而不对步骤的复杂度或多少非独立性必须被考虑造成影响。</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>排序的第二个层面基于直接的单映射范围内个体的对象之间的非独立性组织持续性步骤。这种情况发生的最简单的例子是一个包含对它自己引用的外键的表；表中一个特殊的行需要在表中的引用这一行的某一行之前插入。另一个例子是当一系列的表有一个循环引用的时候：表</span><span
lang=EN-US>A</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>引用表</span><span
lang=EN-US>B</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，表</span><span
lang=EN-US>B</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>引用表</span><span
lang=EN-US>C</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，表</span><span
lang=EN-US>C</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>引用表</span><span
lang=EN-US>A</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>。一些</span><span
lang=EN-US>A</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的对象必须在其他</span><span
lang=EN-US>A</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象之前插入来允许</span><span
lang=EN-US>B</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>和</span><span
lang=EN-US>C</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象也被插入。引用自己的表是循环引用的一种特殊情况。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>为了决定哪一个操作可以在它们的聚集的每个</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>Mapper</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>桶，和将要被分为一个大的每个对象命令集合的桶中最后进行，一个循环的缺陷算法被应用到非独立性的集合中，这些非独立性出现在映射之间，这个算法使用了一个循环缺陷算法的改良版，这个改良版在</span><span
lang=EN-US><a
href="http://neopythonic.blogspot.com/2009/01/detecting-cycles-in-directed-graph.html"><span
style='font-size:10.0pt;font-family:"Helvetica",sans-serif'>Guido Van Rossum's
blog</span></a></span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>可以找到。那些被卷入循环中的桶之后被分成每个对象操作，并混合成每个映射桶的集合，通过新的非独立性规则的从每对象的桶添加回每映射的桶。图</span><span
lang=EN-US>20.16</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>显示了</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>对象的桶被分成个体的每对象的命令，来源于一个新的从</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>User</span></code><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>到它自己的叫做</span><code><span
lang=EN-US style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;
background:#F7F7F9'>contact</span></code><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>的</span><code><span lang=EN-US
style='font-size:9.0pt;font-family:"Courier New";color:#DD1144;background:#F7F7F9'>relationship</span></code><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>的添加。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;font-family:"Helvetica",sans-serif;
color:#333333;mso-no-proof:yes'><v:shape id="图片_x0020_17" o:spid="_x0000_i1025"
 type="#_x0000_t75" alt="http://www.aosabook.org/images/sqlalchemy/uow-element-buckets.png"
 style='width:265.5pt;height:404.25pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="sqlalchemy架构翻译.files/image016.png" o:title="uow-element-buckets"/>
</v:shape></span></p>

<p class=MsoNormal><span lang=EN-US><span style='mso-tab-count:1'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>图</span><span lang=EN-US>20.16</span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>：组织循环引用到个体的步骤</span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>桶结构背后的基本原理是它允许尽可能多的普通语句的配料，既减少</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中需要的步骤数量，也使更有效的与</span><span
lang=EN-US>DBAPI</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>之间的交互成为可能，这样有时可以用一个单独的</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>方法调用执行成千上万的语句。只有当一个循环引用在映射之间出现时，更多代价的每对象非独立模式才开始生效，甚至它只为那些需要它的对象图的部分发生。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><b><span lang=EN-US style='font-size:26.0pt;font-family:
"Calibri Light",sans-serif;mso-ascii-theme-font:major-latin;mso-fareast-font-family:
宋体;mso-hansi-theme-font:major-latin;mso-bidi-font-family:"Times New Roman";
mso-bidi-theme-font:major-bidi'>20.10. </span></b><b><span style='font-size:
26.0pt;font-family:宋体;mso-ascii-font-family:"Calibri Light";mso-ascii-theme-font:
major-latin;mso-hansi-font-family:"Calibri Light";mso-hansi-theme-font:major-latin;
mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'>总结</span></b><b><span
lang=EN-US style='font-size:26.0pt;font-family:"Calibri Light",sans-serif;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:宋体;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:"Times New Roman";mso-bidi-theme-font:major-bidi'><o:p></o:p></span></b></p>

<p class=MsoNormal><span lang=EN-US>SQLAlchemy</span><span style='font-family:
宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>从一开始目标就非常高远，目标是成为最富有特点和最通用的数据库产品。它已经做了许久保持专注与关系型数据库，意识到以一个深度和易于理解的方式支持关系型数据库的有用性是一个主要的事业；甚至现在，这个事业的范围仍继续扩大。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>基于组成元素的方法打算用来从函数的每个区域提取最可能的值，提供许多不同的单元，应用程序可以单独使用或组合使用这些单元。这个系统已经历经了创建、维护和交付的挑战。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>发展历程是缓慢的，基于那个理论：对一个坚实功能的一个有系统的、基础深厚的创建最终会比无根据的快速交货的创建更有价值。</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>建立一个一致的文档充分的用户故事花费了很长时间，但是通过这个过程，潜在的架构总是领先一步，导致某些情况下像“时间机器”一样，在用户需要某些特点之前，这些特点已经存在于</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>中了。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>Python</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>语言是一个可靠的主机（如果有一点过分讲究的话，特别是性能领域）。这个语言的一致性和惊人地运行时打开模式使</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>提供了一个比用其他语言写的相似产品更良好的体验。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN-US>Python</span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>获得前所未有的深度接受和被尽可能广泛的不同领域和工程采用是</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>项目的希望所在，关系型数据库的使用保持生气勃勃和先进的同样也是</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的希望。</span><span
lang=EN-US>SQLAlchemy</span><span style='font-family:宋体;mso-ascii-font-family:
Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>的目标是演示关系型数据库，</span><span
lang=EN-US>Python</span><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>，和好的考虑的对象模型都是非常值得做的开发工具。</span></p>

<p class=MsoNormal><span lang=EN-US><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span style='font-family:宋体;mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;mso-fareast-font-family:宋体;mso-fareast-theme-font:
minor-fareast;mso-hansi-font-family:Calibri;mso-hansi-theme-font:minor-latin'>这个工作在</span><span
lang=EN-US><a href="http://creativecommons.org/licenses/by/3.0/legalcode"><span
style='font-size:10.0pt;font-family:"Helvetica",sans-serif'>Creative Commons
Attribution 3.0 Unported</span></a></span><span style='font-family:宋体;
mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin'>许可协议下可获得，欲查看细节，请点击</span><span lang=EN-US><a
href="http://www.aosabook.org/en/intro1.html#license"><span style='font-size:
10.0pt;font-family:"Helvetica",sans-serif'>full description of the license</span></a></span><span
style='font-family:宋体;mso-ascii-font-family:Calibri;mso-ascii-theme-font:minor-latin;
mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
Calibri;mso-hansi-theme-font:minor-latin'>。</span></p>

</div>

</body>

</html>
