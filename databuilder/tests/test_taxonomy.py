# import unittest
# from unittest import TestCase
# from model.Uri import Uri, UriPart
#
#
# class TestUri(TestCase):
#
#     def test_taxonomy_part_does_store_text(self):
#         # Given
#         tp = UriPart('Tax Part')
#
#         # Then
#         self.assertEqual(tp.text, 'Tax Part')
#
#     def test_taxonomy_part_does_remove_spaces_for_uri(self):
#         # Given
#         tp = UriPart('tax part')
#
#         # Then
#         self.assertEqual(tp.uri_part, 'taxpart')
#
#     def test_taxonomy_part_does_replace_commas_for_uri(self):
#         # Given
#         tp = UriPart('tax.part')
#
#         # Then
#         self.assertEqual(tp.uri_part, 'taxpart')
#
#     def test_taxonomy_part_does_send_to_lower_for_uri(self):
#         # Given
#         tp = UriPart('Tax Part')
#
#         # Then
#         self.assertEqual(tp.uri_part, 'taxpart')
#
#     def test_taxonomy_part_does_replace_ampersand_with_word_for_uri(self):
#         # Given
#         tp = UriPart('Apples & Pears')
#
#         # Then
#         self.assertEqual(tp.uri_part, 'applesandpears')
#
#     def test_taxonomy_does_initialise(self):
#         # Given
#         t = Uri(tier_1="alpha", tier_2="beta",
#                      tier_3="gamma", tier_4="delta")
#
#         # Then
#         self.assertEqual(t.tier_1.text, "alpha")
#         self.assertEqual(t.tier_2.text, "beta")
#         self.assertEqual(t.tier_3.text, "gamma")
#         self.assertEqual(t.tier_4.text, "delta")
#
#
#     def test_taxonomy_does_create_full_uri(self):
#         # Given
#         t1 = Uri(tier_1="alpha", tier_2="beta",
#                      tier_3="gamma", tier_4="delta")
#         t2 = Uri(tier_1="alpha", tier_2="beta",
#                      tier_3="gamma")
#         t3 = Uri(tier_1="alpha", tier_2="beta")
#         t4 = Uri(tier_1="alpha")
#         t5 = Uri()
#
#         # Then
#         self.assertEqual(t1.uri, "alpha/beta/gamma/delta")
#         self.assertEqual(t2.uri, "alpha/beta/gamma")
#         self.assertEqual(t3.uri, "alpha/beta")
#         self.assertEqual(t4.uri, "alpha")
#         self.assertEqual(t5.uri, "")
#
#     def test_taxonomy_does_make_taxonomy_parts_safe(self):
#         # Given
#         t1 = Uri(tier_1="Education", tier_2="Achievement.",
#                      tier_3="KS4", tier_4="Progress 8 & A star to C")
#
#         self.assertEqual(t1.uri,"education/achievement/ks4/progress8andastartoc")
#
# if __name__ == '__main__':
#     unittest.main()