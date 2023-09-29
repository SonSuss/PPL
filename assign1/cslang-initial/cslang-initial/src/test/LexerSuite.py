import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1bc", "1,bc,<EOF>", 100))
    def test_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1 bc", "1,bc,<EOF>", 101))
    def test_3(self):
        """test INTEGER"""
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 102))
    def test_4(self):
        """test INTEGER"""
        self.assertTrue(TestLexer.test("1", "1,<EOF>", 103))
    def test_5(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("1.", "1.,<EOF>", 104))
    def test_6(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("12e8", "12e8,<EOF>", 105))
    def test_7(self):
        """test bool"""
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 107))
    def test_8(self):
        """test blockcomment"""
        self.assertTrue(TestLexer.test("/*abc \nabc*/_a12", "_a12,<EOF>", 109))
    def test_9(self):
        """test blockcomment"""
        self.assertTrue(TestLexer.test("abc/*abc \tabc*/", "abc,<EOF>", 110))
    def test_10(self):
        """test blockcomment"""
        self.assertTrue(TestLexer.test("/*abc abc*/\nabcd", "abcd,<EOF>", 111))
    def test_11(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t\"", "This is a string containing tab \\t,<EOF>", 112))
    def test_12(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"This is a string\\\\\"", "This is a string\\\\,<EOF>", 113))
    def test_13(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 114))  
    def test_14(self):
        """test aray"""
        self.assertTrue(TestLexer.test("[1,2,3,4,2]", "[1,2,3,4,2],<EOF>", 115))      
    def test_15(self):
        """test aray"""
        self.assertTrue(TestLexer.test("[2.3, 4.2, 102e3]", "[2.3, 4.2, 102e3],<EOF>", 116))     
    def test_16(self):
        """test aray"""
        self.assertTrue(TestLexer.test("[1.32,true,3,4,2]", "[1.32,true,3,4,2],<EOF>", 117)) 
    def test_17(self):
        """test aray"""
        self.assertTrue(TestLexer.test("[1.32,true,\"het cuu \",4,2]", "[1.32,true,\"het cuu \",4,2],<EOF>", 118))  
    def test_18(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\n", "<EOF>", 119))
    def test_19(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("a := 5;//this is a line comment\n", "a,:=,5,;,<EOF>", 120))
    def test_20(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    def test_21(self):
        """test float"""
        self.assertTrue(TestLexer.test("9.0", "9.0,<EOF>", 122))
    def test_22(self):
        """test float"""
        self.assertTrue(TestLexer.test("0.33E-3", "0.33E-3,<EOF>", 123))
    def test_23(self):
        """test float"""
        self.assertTrue(TestLexer.test(".12", ".,12,<EOF>", 124))        
    def test_24(self):
        """test float"""
        self.assertTrue(TestLexer.test("143e ", "143,e,<EOF>", 125))
    def test_25(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"", "Unclosed String: He asked me: \\\"Where is John?\\\"", 126))
    def test_26(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("\"This is a error string \n", "Unclosed String: This is a error string ", 127))
    def test_27(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("a : \" Pham Trong Son \n", "a,:,Unclosed String:  Pham Trong Son ", 128))
    def test_28(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("_mynameisson:=\"I got skill issue \b", "_mynameisson,:=,Unclosed String: I got skill issue ", 129))
    def test_29(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("\"using operate on string\" ^ \"this is a wrong string\'\\\\\\try to write a comment", "using operate on string,^,Unclosed String: this is a wrong string'\\\\\\try to write a comment", 130))
    def test_30(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("@son= \"this string is at the end of the file", "@son,=,Unclosed String: this string is at the end of the file", 131))
    def test_31(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("\"this is a illegal escape\\", "Illegal Escape In String: this is a illegal escape\\", 132))
    def test_32(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("a : \" Pham Trong Son \o", "a,:,Illegal Escape In String:  Pham Trong Son \o", 133))
    def test_33(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("_mynameisson:=\"I got skill issue \ ", "_mynameisson,:=,Illegal Escape In String: I got skill issue \ ", 134))
    def test_34(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("\"using operate on string\" ^ \"this is a wrong string \\a \\\\try to write a comment", "using operate on string,^,Illegal Escape In String: this is a wrong string \\a", 135))
    def test_35(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("\"This is illegal, dont escape me: \\g", "Illegal Escape In String: This is illegal, dont escape me: \\g", 136))
    def test_36(self):
        """test separator"""
        self.assertTrue(TestLexer.test("( ) [ ] . , ; : { }", "(,),[,],.,,,;,:,{,},<EOF>", 137))
    def test_37(self):
        """test separator"""
        self.assertTrue(TestLexer.test(".,.,....,.", ".,,,.,,,.,.,.,.,,,.,<EOF>", 138))
    def test_38(self):
        """test separator"""
        self.assertTrue(TestLexer.test("{{][#]}}", "{,{,],[,Error Token #", 139))
    def test_39(self):
        """test separator"""
        self.assertTrue(TestLexer.test("::=:==",":,:=,:=,=,<EOF>" , 140)) 
    def test_40(self):
        """test separator"""
        self.assertTrue(TestLexer.test("{{][]}}", "{,{,],[,],},},<EOF>", 141))
    def test_41(self):
        """test linecomment"""
        
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 142))
    def test_42(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 143))
    def test_43(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 144))
    def test_44(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 145))
    def test_45(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 146))
    def test_46(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 147))
    def test_47(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 148))
    def test_48(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 149))
    def test_49(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 150))
    # def test_50(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_51(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_52(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_53(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_54(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_55(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_56(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_57(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_58(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_59(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_60(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_61(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_62(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_63(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_64(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_65(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_66(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_67(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_68(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_69(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_70(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_71(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_72(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_73(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_74(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_75(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_76(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_77(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_78(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_79(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_80(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_81(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_82(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_83(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_84(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_85(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_86(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_87(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_88(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_89(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_90(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_91(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_92(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_93(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_94(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_95(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_96(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_97(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_98(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    # def test_99(self):
    #     """test linecomment"""
    #     self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
