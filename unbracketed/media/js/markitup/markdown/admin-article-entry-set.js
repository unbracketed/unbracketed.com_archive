mySettings = {
	previewParserPath:	"/site_utils/markup/markdown/", // path to Markdown parser
	onShiftEnter:		{keepDefault:false,	openWith:'\n\n'},
	previewIFrame:  true,
	markupSet: [		 
		{name:'Heading 3', key:"3", openWith:'### ', placeHolder:'Your title here...', className:'header3' },
		{name:'Heading 4', key:"4", openWith:'#### ', placeHolder:'Your title here...', className:'header4' },
		{name:'Heading 5', key:"5", openWith:'##### ', placeHolder:'Your title here...', className:'header5' },
		{name:'Heading 6', key:"6", openWith:'###### ', placeHolder:'Your title here...', className:'header6' },							
		{separator:'---------------' },		
		{name:'Bold', key:"B", openWith:'**', closeWith:'**', className:'bold'},
		{name:'Italic', key:"I", openWith:'_', closeWith:'_', className:'italic'},
		{separator:'---------------' },
		{name:'Bulleted List', openWith:'- ', className:'bulletedList' },
		{name:'Numeric List', openWith:function(h) {
			return h.line+'. ';
		} , className:'numberedList' },
		{separator:'---------------' },
		{name:'Picture', key:"P", replaceWith:'![[![Alternative text]!]]([![Url:!:http://]!] "[![Title]!]")', className:'image'},
		{name:'Link', key:"L", openWith:'[', closeWith:']([![Url:!:http://]!] "[![Title]!]")', placeHolder:'Your text to link here...', className:'link' },
		{separator:'---------------'},	
		{name:'Quotes', openWith:'> ', className:'quotes' },
		{name:'Code Block / Code', openWith:'(!(\t|!|`)!)', closeWith:'(!(`)!)', className:'code'},																	
		{separator:'---------------'},
		{name:'Preview', key:"9", call:'preview', className:"preview"},
		{name:'Preview Refresh', key:"9", call:'togglePreviewRefresh', className:"previewRefresh"}
	]
}