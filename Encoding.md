## chardet
Use node module [chardet](https://www.npmjs.com/package/chardet) to detect encoding of text files.

Supported Encodings:
* UTF-8
* UTF-16 LE
* UTF-16 BE
* UTF-32 LE
* UTF-32 BE
* ISO-2022-JP
* ISO-2022-KR
* ISO-2022-CN
* Shift-JIS
* Big5
* EUC-JP
* EUC-KR
* GB18030
* SO-8859-1
* ISO-8859-2
* ISO-8859-5
* ISO-8859-6
* ISO-8859-7
* ISO-8859-8
* ISO-8859-9
* windows-1250
* windows-1251
* windows-1252
* windows-1253
* windows-1254
* windows-1255
* windows-1256
* KOI8-R

Following is the usage shown in chardet's home page.
```
var chardet = require('chardet');
chardet.detect(new Buffer('hello there!'));
// or 
chardet.detectFile('/path/to/file', function(err, encoding) {});
// or 
chardet.detectFileSync('/path/to/file');
```
#### Client side detect encoding
Scenario: correctly extract the text from upload/drag&drog file in client side.

Assume file is one of the drop file, reader is an instance of FileReader,
1. use `reader.readAsArrayBuffer(file)` to get ArrayBuffer,say arraybuf.
2. use `var enc=chardet.detect(new Buffer(arraybuf))` to detect the encoding as enc.
3. use `reader.readAsText(file,enc)` to extract the content of file.

Project pptxgen-react is an example.

## jschardet
Use node module [jschardet](https://www.npmjs.com/package/jschardet) to detect encoding of text files.

Support following encoding:
* Big5, GB2312/GB18030, EUC-TW, HZ-GB-2312, and ISO-2022-CN (Traditional and Simplified Chinese)
* EUC-JP, SHIFT_JIS, and ISO-2022-JP (Japanese)
* EUC-KR and ISO-2022-KR (Korean)
* KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, and windows-1251 (Russian)
* ISO-8859-2 and windows-1250 (Hungarian)
* ISO-8859-5 and windows-1251 (Bulgarian)
* windows-1252
* ISO-8859-7 and windows-1253 (Greek)
* ISO-8859-8 and windows-1255 (Visual and Logical Hebrew)
* TIS-620 (Thai)
* UTF-32 BE, LE, 3412-ordered, or 2143-ordered (with a BOM)
* UTF-16 BE or LE (with a BOM)
* UTF-8 (with or without a BOM)
* ASCII

Following is the usage shown in jschardet's home page.
```
var jschardet = require("jschardet")

// "àíàçã" in UTF-8
jschardet.detect("\xc3\xa0\xc3\xad\xc3\xa0\xc3\xa7\xc3\xa3")
// { encoding: "UTF-8", confidence: 0.9690625 }

// "次常用國字標準字體表" in Big5
jschardet.detect("\xa6\xb8\xb1\x60\xa5\xce\xb0\xea\xa6\x72\xbc\xd0\xb7\xc7\xa6\x72\xc5\xe9\xaa\xed")
// { encoding: "Big5", confidence: 0.99 }
```
#### Client side detect encoding
Scenario: correctly extract the text from upload/drag&drog file in client side.

Assume file is one of the drop file, reader is an instance of FileReader,
1. use `reader.readAsText(file,'ascii)` to get contents as string, say str.
2. use `var encoding=jschardet.detect(str).encoding` to detect the encoding as encoding.
3. use `reader.readAsText(file,encoding)` to extract the contents of file.

Project pptxgen is an example.
