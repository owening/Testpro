import random

import pytest

from HttpAPI.request_wework.api.member import MemberCurd


class TestMember:

    def setup(self):
        self.member = MemberCurd()

    def test_create(self):
        print(self.member.create("nokeyion7", "newname7", "18863500007"))

    def test_update(self):
        print(self.member.update("nokeyion5", "newname45", "18863500055"))

    def test_getmemberlist(self):
        print(self.member.getMemberlist("nokeyion3"))

    def test_delete(self):
        print(self.member.delete("nokeyion5"))
