import unittest


def get_formmated_name(f_name, m_name, s_name):
    return (f_name + "" + m_name + " " + s_name).title()


class NameTestCase(unittest.TestCase):
    def test_formmated_name(self):
        formatted_name = get_formmated_name('lv', '1', 'hongfang')
        self.assertEqual(formatted_name, 'Lv Hongfang')


unittest.main()