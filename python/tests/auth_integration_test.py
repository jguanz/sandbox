import os
import unittest
import json
import time
import xmltodict
import cisco_dna_tickets
from .context import cisco_dna_policies

auth_token = "?auth_token=0370799e-722e-4928-b60d-ded509220893"
invalid_auth_token = "?auth_token=XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# PLEASE NOTE: THESE TESTS RELY ON A VALID AUTH_TOKEN FOR THE SUCCESSFUL TESTS TO WORK
# JUST USE THE LOG IN END POINT (http://127.0.0.1:8092/login IF RUNNING LOCALLY)
# TO GENERATE A VALID AUTH_TOKEN


class PoliciesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = cisco_dna_policies.app.test_client()

    def tearDown(self):
        pass


# ---------------------------------------------------------------------------
# Unit tests: Successesul auth
# ---------------------------------------------------------------------------
    def test_get_policy(self):
        rv = self.app.get('/policy' + auth_token)
        self.assertEqual(rv.status_code, 200)

    # We expect a TypeError because we're not posting a valid policy.  We just want
    # to test that we're getting past the auth check.
    def test_post_policy(self):
        rv = self.app.post('/policy' + auth_token)
        self.assertRaises("TypeError")

    def test_patch_policy(self):
        rv = self.app.patch('/policy/abc' + auth_token)
        self.assertRaises("TypeError")

    def test_delete_policy(self):
        rv = self.app.delete('/policy/abc' + auth_token)
        self.assertRaises("TypeError")

    def test_get_group(self):
        rv = self.app.get('/group' + auth_token)
        self.assertEqual(rv.status_code, 200)


# ---------------------------------------------------------------------------
# Unit tests: Failed auth
# ---------------------------------------------------------------------------
    def test_get_policy_fail(self):
        rv = self.app.get('/policy' + invalid_auth_token)
        self.assertEqual(rv.status_code, 403)

    def test_post_policy_fail(self):
        rv = self.app.post('/policy' + invalid_auth_token)
        self.assertEqual(rv.status_code, 403)

    def test_patch_policy_fail(self):
        rv = self.app.patch('/policy/abc' + invalid_auth_token)
        self.assertEqual(rv.status_code, 403)

    def test_delete_policy_fail(self):
        rv = self.app.delete('/policy/abc' + invalid_auth_token)
        self.assertEqual(rv.status_code, 403)

    def test_get_group_fail(self):
        rv = self.app.get('/group' + invalid_auth_token)
        self.assertEqual(rv.status_code, 403)

if __name__ == '__main__':
    unittest.main()
