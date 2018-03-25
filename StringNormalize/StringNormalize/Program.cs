using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using CJKUtil;

namespace StringNormalize
{
	class Program
	{
		static void test0()
		{
			string s1 = new String(new char[] { '\u0063', '\u0301', '\u0327', '\u00BE' });
			string s2 = null;
			string divider = new String('-', 80);
			divider = String.Concat(Environment.NewLine, divider, Environment.NewLine);

			Show("s1", s1);
			Console.WriteLine();
			Console.WriteLine("U+0063 = LATIN SMALL LETTER C");
			Console.WriteLine("U+0301 = COMBINING ACUTE ACCENT");
			Console.WriteLine("U+0327 = COMBINING CEDILLA");
			Console.WriteLine("U+00BE = VULGAR FRACTION THREE QUARTERS");
			Console.WriteLine(divider);

			Console.WriteLine("A1) Is s1 normalized to the default form (Form C)?: {0}",
										 s1.IsNormalized());
			Console.WriteLine("A2) Is s1 normalized to Form C?:  {0}",
										 s1.IsNormalized(NormalizationForm.FormC));
			Console.WriteLine("A3) Is s1 normalized to Form D?:  {0}",
										 s1.IsNormalized(NormalizationForm.FormD));
			Console.WriteLine("A4) Is s1 normalized to Form KC?: {0}",
										 s1.IsNormalized(NormalizationForm.FormKC));
			Console.WriteLine("A5) Is s1 normalized to Form KD?: {0}",
										 s1.IsNormalized(NormalizationForm.FormKD));

			Console.WriteLine(divider);

			Console.WriteLine("Set string s2 to each normalized form of string s1.");
			Console.WriteLine();
			Console.WriteLine("U+1E09 = LATIN SMALL LETTER C WITH CEDILLA AND ACUTE");
			Console.WriteLine("U+0033 = DIGIT THREE");
			Console.WriteLine("U+2044 = FRACTION SLASH");
			Console.WriteLine("U+0034 = DIGIT FOUR");
			Console.WriteLine(divider);

			s2 = s1.Normalize();
			Console.Write("B1) Is s2 normalized to the default form (Form C)?: ");
			Console.WriteLine(s2.IsNormalized());
			Show("s2", s2);
			Console.WriteLine();

			s2 = s1.Normalize(NormalizationForm.FormC);
			Console.Write("B2) Is s2 normalized to Form C?: ");
			Console.WriteLine(s2.IsNormalized(NormalizationForm.FormC));
			Show("s2", s2);
			Console.WriteLine();

			s2 = s1.Normalize(NormalizationForm.FormD);
			Console.Write("B3) Is s2 normalized to Form D?: ");
			Console.WriteLine(s2.IsNormalized(NormalizationForm.FormD));
			Show("s2", s2);
			Console.WriteLine();

			s2 = s1.Normalize(NormalizationForm.FormKC);
			Console.Write("B4) Is s2 normalized to Form KC?: ");
			Console.WriteLine(s2.IsNormalized(NormalizationForm.FormKC));
			Show("s2", s2);
			Console.WriteLine();

			s2 = s1.Normalize(NormalizationForm.FormKD);
			Console.Write("B5) Is s2 normalized to Form KD?: ");
			Console.WriteLine(s2.IsNormalized(NormalizationForm.FormKD));
			Show("s2", s2);
			Console.WriteLine();

		}
		static void test4()
		{
			string str = "凉";
			byte[] big5bytes = System.Text.Encoding.GetEncoding("BIG5").GetBytes(str);
			Console.WriteLine(big5bytes.Length); // output: 1
			string str2 = "\u51C9";
			byte[] big5bytes2 = System.Text.Encoding.GetEncoding("BIG5").GetBytes(str2);
			Console.WriteLine(big5bytes2.Length); // output: 1
		}
		static void test3()
		{
			string a = "㐀";
			string b = Normalize.Convert("utf-8", "big5", a);
			string data = String.Format("Source={0},Target={1},Is equal?{2}", a, b, a == b);
			System.IO.StreamWriter sw = new System.IO.StreamWriter("test.txt", false, Encoding.UTF8);
			string a2 = a.Normalize();
			string b2 = Normalize.Convert("utf-8", "big5", a2);
			sw.WriteLine(data);
			sw.Close();

		}
		static void test5()
		{
			Normalize.CJKNormalizeNotInBig5("4E009FEA");
			Normalize.CJKNormalizeNotInBig5("F900FAD9");
			Normalize.CJKNormalizeNotInBig5("34004DB5");
		}
		static void test6()
		{
			byte[] unicodeBytes = { 0,78,1,78,2,78,3,78};
			Encoding unicode = new UnicodeEncoding();
			Encoding big5 = Encoding.GetEncoding("big5");
			char[] unicodeChars =unicode.GetChars(unicodeBytes);
			string s=new String(unicodeChars);
			StreamWriter sw = new StreamWriter("test.txt", false, Encoding.GetEncoding("utf-8"));
			sw.WriteLine(s);
			sw.Close();
		}
		static void test7()
		{
			//byte[] unicodeBytes = {0, 52 };
			byte[] unicodeBytes = { 0, 78 };  // 0,78 = 0x4E00 --> A440=一
			Encoding unicode = new UnicodeEncoding();
			char[] unicodeChars = unicode.GetChars(unicodeBytes);
			string s = new String(unicodeChars);
			Console.WriteLine(s);
			Console.WriteLine(Normalize.IsBig5(s));
		}
		static void test8()
		{
			string s = Normalize.Big5String(164,65); // 一 A440->0x4E00 乙 A441=164,65 -> 0x4E59
			Console.WriteLine("U+{0:X4}", (int)s[0]);
			Console.WriteLine(s);
		}
		static void Main()
		{
			test3();
			//test5();
			//test6();
			//test7();
			//test8();
		}
		static void test2()
		{
			test("机機");
			test("數數");
			test("啟啓啓啟");
			test("兀兀");
			test("嗀嗀");
			test("黄黃");
			Console.WriteLine("{0} 是 Big5? {1}", "數", Normalize.IsBig5("數"));
			Console.WriteLine("{0} 是 Big5? {1}", "數", Normalize.IsBig5("數"));
			Normalize.CJKNCNBig5("數數");
			Console.WriteLine(Normalize.ushort2string((15*16+9)*256+(6*16+9)));
			Console.WriteLine(Normalize.UnicodeRange("F969","F973"));
			Normalize.CJKNormalizeNotInBig5("F900FAD9");
			Console.WriteLine("Press any key to continue");
			Console.ReadKey();
		}
		static void test(string s1)
		{
			// string s1 = "數數气氣"; //new String(new char[] { '\u0063', '\u0301', '\u0327', '\u00BE' });
			string s2 = s1.Normalize();
			string s3 = s1.Normalize(NormalizationForm.FormKC);
			string divider = new String('-', 80);
			divider = String.Concat(Environment.NewLine, divider, Environment.NewLine);

			Show(s1, s1);
			Show(s2, s2);
			Show(s3, s3);
			Console.WriteLine("s1) Is s1 normalized to the default form (Form C)?: {0}",
							 s1.IsNormalized(NormalizationForm.FormC));
			Console.WriteLine("s1) Is s1 normalized to the default form (Form KC)?: {0}",
							 s1.IsNormalized(NormalizationForm.FormKC));
			Console.WriteLine("s2) Is s2 normalized to the default form (Form C)?: {0}",
							 s2.IsNormalized(NormalizationForm.FormC));
			Console.WriteLine("s2) Is s2 normalized to the default form (Form KC)?: {0}",
							 s2.IsNormalized(NormalizationForm.FormKC));
			Console.WriteLine("s3) Is s3 normalized to the default form (Form C)?: {0}",
							 s3.IsNormalized(NormalizationForm.FormC));
			Console.WriteLine("s3) Is s3 normalized to the default form (Form KC)?: {0}",
							 s3.IsNormalized(NormalizationForm.FormKC));

			Console.WriteLine();

		}
		private static void Show(string title, string s)
		{
			Console.Write("Characters in string {0} = ", title);
			foreach (short x in s)
			{
				Console.Write("{0:X4} ", x);
			}
			Console.WriteLine();
		}

	}
}
