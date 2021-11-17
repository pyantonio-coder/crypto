import unittest

from crypto import (atbash_decrypt,
                    atbash_encrypt,
                    ceaser_decrypt,
                    ceaser_encrypt,
                    vigenere_decrypt,
                    vigenere_encrypt,
                    playfair_decrypt,
                    playfair_encrypt)


class test_crypto(unittest.TestCase):

    def test_atbash_decrypt(self):

        input_var_1="GSRHRHMLGEVIBHVXIVGZGZOO"
        input_var_2="gSRHRHMLGEViBHVXIVGZGZOo"
        input_var_3="GSR HRH MLG EVI BHV XIV GZG ZOO"


        result_1=atbash_decrypt(cipher_text=input_var_1)
        result_2=atbash_decrypt(cipher_text=input_var_2)
        result_3=atbash_decrypt(cipher_text=input_var_3)

        expected_1="THISISNOTVERYSECRETATALL"
        expected_2="THISISNOTVERYSECRETATALL"
        expected_3="THISISNOTVERYSECRETATALL"


        self.assertEqual(result_1,expected_1)
        self.assertEqual(result_2,expected_2)
        self.assertEqual(result_3,expected_3)
        self.assertRaises(TypeError, atbash_decrypt, 34)
        self.assertRaises(TypeError, atbash_decrypt, "exclamation!")

    def test_atbash_encrypt(self):
    
        input_var_1="THISISNOTVERYSECRETATALL"
        input_var_2="THISiSNOTVERYsECRETATALL"
        input_var_3="TH ISISN OTVER YSECRE TATALL"


        result_1=atbash_encrypt(plain_text=input_var_1)
        result_2=atbash_encrypt(plain_text=input_var_2)
        result_3=atbash_encrypt(plain_text=input_var_3)

        expected_1="GSRHRHMLGEVIBHVXIVGZGZOO"
        expected_2="GSRHRHMLGEVIBHVXIVGZGZOO"
        expected_3="GSRHRHMLGEVIBHVXIVGZGZOO"


        self.assertEqual(result_1,expected_1)
        self.assertEqual(result_2,expected_2)
        self.assertEqual(result_3,expected_3)
        self.assertRaises(TypeError, atbash_encrypt, 34)
        self.assertRaises(TypeError, atbash_encrypt, "exclamation!")

    def test_ceaser_decrypt(self):
    
        input_var_1="MTBVZNHPQDINIDTZGWJFPYMNX"
        input_var_2="MTBVZN HPQDINIDT ZGWJFPY MNX"
        input_var_3="MTbVZNHPQDInIDTZGWJFPYMNX"

        result_1=ceaser_decrypt(cipher_text=input_var_1,
                             shift=5)

        result_2=ceaser_decrypt(cipher_text=input_var_2,
                             shift=5)

        result_3=ceaser_decrypt(cipher_text=input_var_3,
                             shift=5)

        expected_1="HOWQUICKLYDIDYOUBREAKTHIS"
        expected_2="HOWQUICKLYDIDYOUBREAKTHIS"
        expected_3="HOWQUICKLYDIDYOUBREAKTHIS"

        self.assertEqual(result_1,expected_1)
        self.assertEqual(result_2,expected_2)
        self.assertEqual(result_3,expected_3)
        self.assertRaises(TypeError, ceaser_decrypt, 34,3)
        self.assertRaises(TypeError, ceaser_decrypt, "exclamation!",4)
        self.assertRaises(TypeError, ceaser_decrypt, "EXCLAMATION","A")
    
    def test_ceaser_encrypt(self):
        
        input_var_1="HOWQUICKLYDIDYOUBREAKTHIS"
        input_var_2="HOWQUICKLYDIDYOUBREAKTHis"
        input_var_3="HOW QUICKLY DID YOU BREAK THIS"

        result_1=ceaser_encrypt(plain_text=input_var_1,
                             shift=5)
        result_2=ceaser_encrypt(plain_text=input_var_2,
                             shift=5)

        result_3=ceaser_encrypt(plain_text=input_var_3,
                             shift=5)

        expected_1="MTBVZNHPQDINIDTZGWJFPYMNX"
        expected_2="MTBVZNHPQDINIDTZGWJFPYMNX"
        expected_3="MTBVZNHPQDINIDTZGWJFPYMNX"

        self.assertEqual(result_1,expected_1)
        self.assertEqual(result_2,expected_2)
        self.assertEqual(result_3,expected_3)

        self.assertRaises(TypeError, ceaser_encrypt, 34,3)
        self.assertRaises(TypeError, ceaser_encrypt, "exclamation!",4)
        self.assertRaises(TypeError, ceaser_encrypt, "EXCLAMATION","A")

    def test_vigenere_decrypt(self):
        
        input_var_1="FGQVEQYONMCCHAXTPB"
        input_var_2="F G Q V E Q Y O N M C C H A X T P B"
        input_var_3="YDXGJHCJVODXUGGZ"
        perm_3="thislepgywnomarkdbfcjquvxz"

        result_1a=vigenere_decrypt(cipher_text=input_var_1,
                                keyword="FAMILY",
                                permutation="")

        result_1b=vigenere_decrypt(cipher_text=input_var_1,
                                keyword="family",
                                permutation="")

        result_2a=vigenere_decrypt(cipher_text=input_var_2,
                                keyword="FAMILY",
                                permutation="")

        result_2b=vigenere_decrypt(cipher_text=input_var_2,
                                keyword="fam ily",
                                permutation="")

        result_3=vigenere_decrypt(cipher_text=input_var_3,
                                keyword="NIGHT time",
                                permutation=perm_3)


        expected_1="AGENTSTOBERECALLED"
        expected_2="AGENTSTOBERECALLED"
        expected_3="VISABILITYISPOOR"

        self.assertEqual(result_1a,expected_1)
        self.assertEqual(result_1b,expected_1)
        self.assertEqual(result_2a,expected_2)
        self.assertEqual(result_2b,expected_2)
        self.assertEqual(result_3,expected_3)

        self.assertRaises(TypeError, vigenere_decrypt, 34,3,5)
        self.assertRaises(TypeError, vigenere_decrypt, "exclamation!",4,3)
        self.assertRaises(TypeError, vigenere_decrypt, "EXCLAMATION","A","BB")


    # def test_vigenere_encrypt(self):
        
    #     input_var=""

    #     result=vigenere_encrypt(plain_text=input_var,
    #                             keyword="",
    #                             permutation="")

    #     expected=""

    #     self.assertEqual(result,expected)


    # def test_playfair_decrypt(self):
        
    #     input_var=""

    #     result=playfair_decrypt(cipher_text=input_var,
    #                             keyword="")

    #     expected=""

    #     self.assertEqual(result,expected)


    # def test_playfair_encrypt(self):
        
    #     input_var=""

    #     result=playfair_encrypt(plain_text=input_var,
    #                             keyword="")

    #     expected=""

    #     self.assertEqual(result,expected)



if __name__=="__main__":
        unittest.main()


















