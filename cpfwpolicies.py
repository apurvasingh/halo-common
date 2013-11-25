#!/usr/bin/env python
import sys

import cpapi
import json

class FirewallPolicies:
    def __init__(self, obj):
        if 'name' in obj:
            self.name = obj['name']
        else:
            self.name = None
        if 'id' in obj:
            self.id = obj['id']
        else:
            self.id = None
        if 'platform' in obj:
            self.platform = obj['platform']
        else:
            self.platform = None
        if 'description' in obj:
            self.description = obj['description']
        else:
            self.description = None

    @staticmethod
    def all(apiCon):
        policyList = []
        (response, authError) = apiCon.getFirewallPolicyList()
        if ('firewall_policies' in response):
            for obj in response['firewall_policies']:
                policy = FirewallPolicies(obj)
                policyList.append(policy)
        return policyList

    def to_s(self):
        return "FirewallPolicy=%s platform=%s ID=%s" % (self.name, self.platform, self.id)
