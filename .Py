Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def decimal(binary_str):
    remove_0_and_1 = binary_str.replace('0', '').replace('1, '')
                                                         
SyntaxError: unterminated string literal (detected at line 2)
if len(remove_0_and_1) > 0:
                                                         raise ValueError('La cadena binaria de entrada solo puede contener 0 y 1')
                                                        place = 1:
                                                            
SyntaxError: unindent does not match any outer indentation level
dec = 0
for bit in binary_str[::-1]
SyntaxError: expected ':'
if (bit == '1'):
    dec += place
    place *= 2
    return dec
SyntaxError: 'return' outside function
import unittest
import bin_to_dec
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    import bin_to_dec
ModuleNotFoundError: No module named 'bin_to_dec'
class TestBinaryToDecimal(unittest.TestCase):
    def test_binario_decimal_con_entradas_validas(self):
        for d in range(100):
            binary = bin(d)
            binary = binary[2:]
            dec-output = bin_to_dec.decimal(binary)
            
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
self.assertEqual(d, dec_output)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    self.assertEqual(d, dec_output)
NameError: name 'self' is not defined
test_vals = [4000, 4001, 4002, 1024, 1099511627776, 1099511627777, 1099511627775]
for d in test_vals:
    binary = bin(d)
    binary = binary[2:]
    dec_output = bin_to_dec.decimal(binary)
    self.assertEqual(d, dec_output)
test_bin_str = [ '101010', '1111', '000111', '0', '1']
SyntaxError: invalid syntax
>>> expected_dec = [ 42, 15, 7, 0, 1]
>>> for binary_input, expected_dec_output in zip( test_bin_str, expected_dec) :
...     dec = bin_to_dec.decimal(binary_input)
...     self.assertEqual(dec, expected_dec_output)
... def test_binario_decimal_con_entradas_invalidas(self):
...     
SyntaxError: invalid syntax
>>> valid = '010101'
>>> valid2 = '111111'
>>> invalid = [ '123456', '101010012', 'abc', '@#$%$^%^%']
>>> for invalid_input in invalid:
...     with self.assertRaises(ValueError):
...         bin_to_dec.decimal(invaled_input)
... if __name__ == '__main__':
...     
SyntaxError: invalid syntax
>>> unittest.main()

----------------------------------------------------------------------
Ran 0 tests in 0.000s

NO TESTS RAN

