

import pytest
import sys
sys.path.insert(0, './colmore/')

from colmore.app.user import User


def test_User():
    user = User('test')
    assert isinstance(user, User)

def test_user_isValid():
    user = User('test')
    assert user.isValid() == True



