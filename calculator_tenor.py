import unittest

import requests

from pyunitreport import HTMLTestRunner


base_url = 'https://gateway-alpha.awantunai.com/v1.0/patriot'
login_url = '/v2/consumer/login'
calculation_url = '/v1/consumer/protected/credits/calculator'
header = { 'Content-Type': 'application/json', 'Secret-Key': 'MOvrDHfVomtAcuD95dFxB3v4xNMXwM2t' }
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoie1wiaWRcIjozOTIyNixcImZ1bGxfbmFtZVwiOlwiR3VzdGFmaW4gU3VuZG9ybyBQdXRyb1wiLFwicGhvbmVfbnVtYmVyXCI6XCIwODU3ODE4MDYyNzNcIn0iLCJpc3MiOiJhd2FudHVuYWkiLCJleHAiOjE1NDI4ODc4NDAsImtleSI6Ik1PdnJESGZWb210QWN1RDk1ZEZ4QjN2NHhOTVh3TTJ0In0.geYzo1iZBbP287RNbi04gDUkiEY6aXJ9AOpkbp_PK7s'
headers = { 'Content-Type': 'application/json', 'Authorization': token}

class CreditCalculatorAlphaTest(unittest.TestCase):

    def get_token_1(self):
        request_json_1 = {
            "phone_number": "0895801339768",
            "pin": "qqqqqqqq"
        }
        response = requests.post(base_url + login_url, json=request_json_1, headers=header)
        self.assertEqual('OK', response.json()['status'], 'Error Login Please Check Phone / Pin')
        token = response.json()['data']['token']
        print token
        return token

    def get_token_2(self):
        request_json_2 = {
            "phone_number": "085781806273",
            "pin": "qwertyuiop"
        }
        response = requests.post(base_url + login_url, json=request_json_2, headers=header)
        self.assertEqual('OK', response.json()['status'], 'Error Login Please Check Phone / Pin')
        token = response.json()['data']['token']
        return token

    def test_baca_calculation_3_juta(self):
        test_token = self.get_token_1()
        test_headers = {'Content-Type': 'application/json', 'Authorization': test_token}

        request_json = {
            "partner_id": "33",
            "partner_agent_id": "58",
            "amount_to_finance": "3000000",
            "price": "3000000",
            "channel_id": "1"
        }

        # response = requests.post(base_url + 'calculation/patriot/v1/consumer/protected/credits/calculator', json=request_json, headers=headers)
        response = requests.post(base_url + calculation_url, json=request_json, headers=test_headers)

        print('\nTest 3 juta dengan akun 1 dengan id 38629 dan gaji 12.000.000')

        self.assertEqual('Success.', response.json()['message'], 'Response Error')
        self.assertEqual(len(response.json()['data']['installments']), 2, 'Jumlah tenor tidak sama dengan 2')
        self.assertEqual((response.json()['data']['installments'][0]['total_installment_in_month']), 4, 'Tenor pertama bukan 4')
        self.assertEqual((response.json()['data']['installments'][1]['total_installment_in_month']), 7, 'Tenor kedua bukan 7')

        test_token = self.get_token_2()
        test_headers = {'Content-Type': 'application/json', 'Authorization': test_token}

        request_json = {
            "partner_id": "33",
            "partner_agent_id": "58",
            "amount_to_finance": "500000",
            "price": "500000",
            "channel_id": "1"
        }

        # response = requests.post(base_url + 'calculation/patriot/v1/consumer/protected/credits/calculator', json=request_json, headers=headers)
        response = requests.post(base_url + calculation_url, json=request_json, headers=test_headers)

        print('\nTest 3 juta dengan akun 2 dengan id 39226 dan gaji 12.000.000')

        self.assertEqual('Success.', response.json()['message'], 'Response Error')
        self.assertEqual(len(response.json()['data']['installments']), 2, 'Jumlah tenor tidak sama dengan 2')
        self.assertEqual((response.json()['data']['installments'][0]['total_installment_in_month']), 4,'Tenor pertama bukan 4')
        self.assertEqual((response.json()['data']['installments'][1]['total_installment_in_month']), 7,'Tenor kedua bukan 7')

    def test_credit_calculation_4_juta(self):
        test_token = self.get_token_1()
        test_headers = {'Content-Type': 'application/json', 'Authorization': test_token}

        request_json = {
            "partner_id": "33",
            "partner_agent_id": "58",
            "amount_to_finance": "4000000",
            "price": "4000000",
            "channel_id": "1"
        }
        # response = requests.post(base_url + 'calculation/patriot/v1/consumer/protected/credits/calculator', json=request_json, headers=headers)
        response = requests.post(base_url + calculation_url, json=request_json, headers=test_headers)

        print('\nTest 4 juta dengan akun 1 dengan id 38629 dan gaji 12.000.000')

        self.assertEqual('Success.', response.json()['message'], 'Response Error')
        self.assertEqual(len(response.json()['data']['installments']), 2, 'Jumlah tenor tidak sama dengan 2')
        self.assertEqual((response.json()['data']['installments'][0]['total_installment_in_month']), 4, 'Tenor pertama bukan 4')
        self.assertEqual((response.json()['data']['installments'][1]['total_installment_in_month']), 7, 'Tenor kedua bukan 7')

        test_token = self.get_token_2()
        test_headers = {'Content-Type': 'application/json', 'Authorization': test_token}

        request_json = {
            "partner_id": "33",
            "partner_agent_id": "58",
            "amount_to_finance": "4000000",
            "price": "4000000",
            "channel_id": "1"
        }
        # response = requests.post(base_url + 'calculation/patriot/v1/consumer/protected/credits/calculator', json=request_json, headers=headers)
        response = requests.post(base_url + calculation_url, json=request_json, headers=test_headers)

        print('\nTest 4 juta dengan akun 2 dengan id 39226 dan gaji 4.000.000')

        self.assertEqual('Success.', response.json()['message'], 'Response Error')
        self.assertEqual(len(response.json()['data']['installments']), 1, 'Jumlah tenor tidak sama dengan 2')
        self.assertEqual((response.json()['data']['installments'][0]['total_installment_in_month']), 7, 'Tenor kedua bukan 7')

    def test_credit_calculation_5_juta(self):
        test_token = self.get_token_1()
        test_headers = {'Content-Type': 'application/json', 'Authorization': test_token}

        request_json = {
            "partner_id": "33",
            "partner_agent_id": "58",
            "amount_to_finance": "4000000",
            "price": "4000000",
            "channel_id": "1"
        }
        # response = requests.post(base_url + 'calculation/patriot/v1/consumer/protected/credits/calculator', json=request_json, headers=headers)
        response = requests.post(base_url + calculation_url, json=request_json, headers=test_headers)

        print('\nTest 5 juta dengan akun 1 dengan id 38629 dan gaji 12.000.000')

        self.assertEqual('Success.', response.json()['message'], 'Response Error')
        self.assertEqual(len(response.json()['data']['installments']), 2, 'Jumlah tenor tidak sama dengan 2')
        self.assertEqual((response.json()['data']['installments'][1]['total_installment_in_month']), 7, 'Tenor kedua bukan 7')

        test_token = self.get_token_2()
        test_headers = {'Content-Type': 'application/json', 'Authorization': test_token}

        request_json = {
            "partner_id": "33",
            "partner_agent_id": "58",
            "amount_to_finance": "4000000",
            "price": "4000000",
            "channel_id": "1"
        }
        # response = requests.post(base_url + 'calculation/patriot/v1/consumer/protected/credits/calculator', json=request_json, headers=headers)
        response = requests.post(base_url + calculation_url, json=request_json, headers=test_headers)

        print('\nTest 5 juta dengan akun 2 dengan id 39226 dan gaji 4.000.000')

        self.assertEqual('Success.', response.json()['message'], 'Response Error')
        # self.assertEqual(len(response.json()['data']['installments']), 0, 'Jumlah tenor tidak sama dengan 0')

    def test_credit_calculator_negative_partner_id(self):
        test_token = self.get_token_1()
        test_headers = {'Content-Type': 'application/json', 'Authorization': test_token}

        request_json = {
            "partner_id": "-55",
            "partner_agent_id": "58",
            "amount_to_finance": "3000000",
            "price": "3000000",
            "channel_id": "1"
        }
        # response = requests.post(base_url + 'calculation/patriot/v1/consumer/protected/credits/calculator', json=request_json, headers=headers)
        response = requests.post(base_url + calculation_url, json=request_json, headers=test_headers)

        print('\nPartner ID invalid akun 1 dengan id 38629')

        self.assertEqual('Mohon masukan Partner Id yang benar. ', response.json()['message'])

    def test_credit_calculator_amount_to_finance_lebih_dari_price(self):
        test_token = self.get_token_1()
        test_headers = {'Content-Type': 'application/json', 'Authorization': test_token}

        request_json = {
            "partner_id": "33",
            "partner_agent_id": "58",
            "amount_to_finance": "3000000",
            "price": "1000000",
            "channel_id": "1"
        }
        response_1 = requests.post(base_url + calculation_url, json=request_json, headers=test_headers)

        test_token = self.get_token_2()
        test_headers = {'Content-Type': 'application/json', 'Authorization': test_token}

        request_json = {
                "partner_id": "33",
                "partner_agent_id": "58",
                "amount_to_finance": "3000000",
                "price": "1000000",
                "channel_id": "1"
            }
        response_2 = requests.post(base_url + calculation_url, json=request_json, headers=test_headers)
        print('\nTest amount to finance lebih dari price')
        self.assertEqual((response_1.json()['data']['installments'][0]['monthly installment']), (response_2.json()['data']['installments'][0]['monthly installment']), 'Monthly Installment tenor 4 tidak sama')
        self.assertEqual((response_1.json()['data']['installments'][1]['monthly installment']), (response_2.json()['data']['installments'][1]['monthly installment']), 'Monthly Installment tenor 7 tidak sama')
        # self.assertGreater()

    def test_credit_calculator_negative_price(self):
        # testcase untuk mengecek negative price
        request_json = {
                "partner_id": "33",
                "partner_agent_id": "58",
                "amount_to_finance": "1000000",
                "price": "-2500000",
                "channel_id": "1"
            }
        response = requests.post(base_url + '/v1/consumer/protected/credits/calculator',json=request_json, headers=headers)
        self.assertEqual(response.json()['message'], 'Mohon masukan Price yang benar. ', 'Response Error')

    def test_credit_calculator_amount_to_finance_price(self):
        # testcase untuk mengecek negative price
        request_json = {
                "partner_id": "33",
                "partner_agent_id": "58",
                "amount_to_finance": "-1000",
                "price": "2500000",
                "channel_id": "1"
            }
        response = requests.post(base_url + '/v1/consumer/protected/credits/calculator',json=request_json, headers=headers)
        self.assertEqual(response.json()['message'],'Mohon masukan Amount to Finance yang benar. ', 'Response Error')

    def test_credit_calculator_partner_agent_id(self):
        # testcase untuk mengecek partner_agent_id
        request_json = {
                "partner_id": "33",
                "partner_agent_id": "abc",
                "amount_to_finance": "1000000",
                "price": "2500000",
                "channel_id": "1"
            }
        response = requests.post(base_url + '/v1/consumer/protected/credits/calculator',json=request_json, headers=headers)
        self.assertEqual(response.json()['message'], 'Internal Server Error', 'Response Error')

    # def test_credit_calculator_partner_agent_id_wrong(self):
    #     # testcase untuk mengecek negative price
    #     request_json = {
    #             "partner_id": "33",
    #             "partner_agent_id": "487358",
    #             "amount_to_finance": "1000000",
    #             "price": "2500000",
    #             "channel_id": "1"
    #         }
    #     response = requests.post(base_url + '/v1/consumer/protected/credits/calculator',json=request_json, headers=headers)
    #     print(response.json())
    #     self.assertEqual(response.json()['message'], 'Internal Server Error', 'Response Error')

    # def test_latefee_repayment_details(self):

    # def test_latefee_calculate_nextbill(self):
    #     # requests_json = {
    #     #     "loan_number": "AT1534415169334"
    #     #     "installment_number": 2,
    #     #     "amount_to_finance":461000
    #     # }
    #     header = {
    #         'Content-Type': 'application/json',
    #         'Authorization': token
    #     }
    #     response = requests.get(
    #         'https://gateway-alpha.awantunai.com//v1/consumer/protected/user/credit/next_bill',
    #         headers=header)
    #     print(response.json())
    #     result = response.json()
    #     self.assertEqual(50000, result['data']['late_fee_amount_unpaid'])

    # def test_get_overdues(self):
    #     response = requests.get(base_url + '/overdues', headers=header)
    #     print(response.json())
    #     result = response.json()
    #     self.assertEqual(200, result['status'])
    #     self.assertTrue(result['data'] is not None)
    #     self.assertTrue(len(result['data']['content']) > 0)
    #
    # def test_get_overdues_limit_3(self):
    #     size = 3
    #     response = requests.get(base_url + '/overdues?size=' + str(size), headers=header)
    #     result = response.json()
    #     self.assertEqual(3, len(result['data']['content']))

    def runTest(self):
        pass

if __name__ == '__main__':
    # CreditCalculatorAlphaTest().test_credit_calculator_partner_agent_id()
    # CreditCalculatorAlphaTest().test_baca_calculation_3_juta()
    # CreditCalculatorAlphaTest().get_token_1()
    unittest.main(testRunner=HTMLTestRunner(output='credit-calculator-report-test'))
    # unittest.main(testRunner=HTMLTestRunner(output='/Users/nezha/Documents/QA_Otomation/testAPI_py/automation-test-qa-backend/CreditsCalculator/reports/credit_calculator.html'))