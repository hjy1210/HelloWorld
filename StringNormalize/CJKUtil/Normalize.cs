using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace CJKUtil
{
    public static class Normalize
    {
		public static Encoding unicode = new UnicodeEncoding();
		static string[] U3400 = { "3400", "4DB5" };
		static string[] U4E00 = { "4E00", "9FEA" };
		static string[] UF900 = { "F900", "FAD9" };
		static Dictionary<string, ushort[]> charRangeDict= new Dictionary<string, ushort[]>{
			{ "u3400", new ushort[]{ 0x3400, 0x4db5 } },
			{ "u4e00", new ushort[]{ 0x4e00, 0x9fea } },
			{ "u2e80", new ushort[]{ 0x2e80, 0x2ef3 } },
			{ "u2f00", new ushort[]{ 0x2f00, 0x2fd5 } },
			{ "u2ff0", new ushort[]{ 0x2ff0, 0x2ffb } },
			{ "u3100", new ushort[]{ 0x3100, 0x312f } },
			{ "u31a0", new ushort[]{ 0x31a0, 0x31bf } },
			{ "u31c0", new ushort[]{ 0x31c0, 0x31e3 } },
			{ "uf900", new ushort[]{ 0xf900, 0xfad9 } }
		};
		static string[] code ={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
			"A", "B", "C", "D", "E", "F"};
		static Dictionary<string, int> Hex = new Dictionary<string, int>{
			{ "0", 0 },{ "1", 1 },{ "2", 2 },{ "3", 3 },{ "4", 4 },{ "5", 5 },{ "6", 6 },{ "7", 7 },
			{ "8", 8 },{ "9", 9 },{ "A", 10 },{ "B", 11 },{ "C", 12 },{ "D", 13 },{ "E", 14 },{ "F", 15 }
		};
		static Encoding big5 = Encoding.GetEncoding("big5");
		static Encoding utf8 = Encoding.GetEncoding("utf-8");

		public static bool IsBig5(string s)
		{
			return s == Convert(s);
		}
		public static string ToBig5ToUnicode(string s)
		{
			Encoding big5 = Encoding.GetEncoding("big5");
			byte[] big5Bytes = big5.GetBytes(s);
			//int n = big5Bytes.Length;
			char[] big5Chars = new char[big5.GetCharCount(big5Bytes, 0, big5Bytes.Length)];
			big5.GetChars(big5Bytes, 0, big5Bytes.Length, big5Chars, 0);

			string data=new String(big5Chars);
			/*data = data + n.ToString() + ":";
			for (int i = 0; i < big5Bytes.Length; i++)
			{
				data = data + code[big5Bytes[i] / 16] + code[big5Bytes[i] % 16];
			}*/
			return data;
		}
		public static string Big5String(byte ubyte,byte lbyte)
		{
			byte[] bytes = new byte[2];
			bytes[0] = ubyte;
			bytes[1] = lbyte;
			Encoding big5 = Encoding.GetEncoding("big5");
			Char[] big5Chars = big5.GetChars(bytes);
			string s = new string(big5Chars);
			return s;
		}
		public static string Convert(string encodingFrom,string encodingTo,string data)
		{
			Encoding from = Encoding.GetEncoding(encodingFrom);
			Encoding to = Encoding.GetEncoding(encodingTo);
			byte[] fromBytes = from.GetBytes(data);
			byte[] toBytes = Encoding.Convert(from, to, fromBytes);
			char[] toChars = new Char[to.GetCharCount(toBytes, 0, toBytes.Length)];
			to.GetChars(toBytes, 0, toBytes.Length, toChars,0);
			return new string(toChars);
		}
		static string Convert(string big5String)
		{

			// convert string to bytes
			byte[] big5Bytes = big5.GetBytes(big5String);

			// convert encoding from big5 to utf8
			byte[] utf8Bytes = Encoding.Convert(big5, utf8, big5Bytes);

			char[] utf8Chars = new char[utf8.GetCharCount(utf8Bytes, 0, utf8Bytes.Length)];
			utf8.GetChars(utf8Bytes, 0, utf8Bytes.Length, utf8Chars, 0);

			return new string(utf8Chars);
		}
		public static void CJKNCNBig5(string s)
		{
			UnicodeEncoding unicode = new UnicodeEncoding();

			// Create a string that contains Unicode characters.
			//String unicodeString =
			//	"This Unicode string contains two characters " +
			//	"with codes outside the traditional ASCII code range, " +
			//	"Pi (\u03a0) and Sigma (\u03a3).";
			Console.WriteLine("Original string:");
			Console.WriteLine(s);

			// Encode the string.
			Byte[] encodedBytes = unicode.GetBytes(s);
			Console.WriteLine();
			Console.WriteLine("Encoded bytes:");
			foreach (Byte b in encodedBytes)
			{
				Console.Write("[{0:X2}]", b);
			}
			Console.WriteLine();

		}
		static ushort FourChar2UShort(string s)
		{
			ushort n = (ushort)((Hex[s.Substring(0, 1)] * 16 + Hex[s.Substring(1, 1)]) * 256 +
				Hex[s.Substring(2, 1)] * 16 + Hex[s.Substring(3, 1)]);
			return n;
		}
		public static string UnicodeRange(string start, string end)
		{
			ushort ustart = FourChar2UShort(start);
			ushort uend = FourChar2UShort(end);
			StringBuilder str = new StringBuilder();
			for (ushort n= ustart; n <= uend; n = (ushort)(n + 1))
			{
				str.Append(ushort2string(n));
			}
			return str.ToString();
		}
		public static string ushortCode(ushort n)
		{
			int un = n / 256;
			int ln = n % 256;
			return code[un / 16] + code[un % 16] + code[ln / 16] + code[ln % 16];
		}
		public static string ushort2string(ushort n)
		{
			byte[] buffer = new byte[2];
			buffer[0] =(byte)( n % 256);
			buffer[1] = (byte)(n / 256);
			return unicode.GetString(buffer);
		}
		public static string CJKNormalizeNotInBig5(string start,string end)
		{
			ushort ustart = FourChar2UShort(start);
			ushort uend = FourChar2UShort(end);
			StringBuilder sb = new StringBuilder();
			int count = 0;
			int normalorig=0;
			int normal = 0;
			int unnormal = 0;
			byte[] unicodeBytes;
			for (ushort n = ustart; n <= uend; n = (ushort)(n + 1))
			{
				string s = ushort2string(n);
				string snormal = s.Normalize(NormalizationForm.FormKC);
				if (IsBig5(snormal))
				{
					normal++;
					if (s != snormal)
					{
						sb.Append(ushortCode(n) + " ");
						sb.Append(s + " ");
						unicodeBytes = unicode.GetBytes(snormal);
						sb.Append(code[unicodeBytes[1] / 16] + code[unicodeBytes[1] % 16] + code[unicodeBytes[0] / 16] + code[unicodeBytes[0] % 16]);
						sb.Append(" " + snormal + " ");
						//sb.Append(ToBig5ToUnicode(snormal));
						count++;
						sb.AppendLine("");
					}
					else
					{
						normalorig++;
					}
				}
				else
				{
					unnormal++;
					sb.Append(ushortCode(n) + " ");
					sb.Append(s + " ");
					unicodeBytes = unicode.GetBytes(snormal);
					sb.Append(code[unicodeBytes[1] / 16] + code[unicodeBytes[1] % 16] + code[unicodeBytes[0] / 16] + code[unicodeBytes[0] % 16]);
					sb.AppendLine(" " + snormal + " ###");
				}
			}
			sb.AppendLine(string.Format("{0} characters,{1} characters is with normalized version in Big5, {2} characters is with normalized version outside Big5", uend - ustart + 1, normal,unnormal));
			sb.AppendLine(string.Format("{0} characters is normalized and in Big 5, {1} characters with normalized version in Big 5", normalorig, count));
			return sb.ToString();
		}
		public static void CJKNormalizeNotInBig5(string startend)
		{
			StreamWriter sw = new StreamWriter(startend+".txt",false,Encoding.UTF8);
			sw.WriteLine(CJKNormalizeNotInBig5(startend.Substring(0, 4), startend.Substring(4, 4)));
			sw.Flush();
			sw.Close();
		}
		public static Dictionary<char,string> GetKcDict()
		{
			Dictionary<char, StringBuilder> dictStem = new Dictionary<char, StringBuilder>();
			foreach (string name in charRangeDict.Keys)
			{
				//Console.WriteLine(name);
				for (long code=charRangeDict[name][0]; code <= charRangeDict[name][1]; code++)
				{
					char c = System.Convert.ToChar((ushort)code);
					char stem = (c.ToString().Normalize(NormalizationForm.FormKC))[0];
					if (dictStem.Keys.Contains(stem))
					{
						dictStem[stem].Append(c); 
					} else
					{
						StringBuilder sb = new StringBuilder();
						sb.Append(stem);
						dictStem.Add(stem, sb);
					}
				}
			}
			Dictionary<char, string> dict = new Dictionary<char, string>();
			foreach (char c in dictStem.Keys)
			{
				dict.Add(c, dictStem[c].ToString());
			}
			return dict;
		}
	}
}
