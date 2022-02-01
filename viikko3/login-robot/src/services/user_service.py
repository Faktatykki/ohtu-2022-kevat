from entities.user import User

import re
import sys, pdb


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if not re.match("^.[a-z]{2,}", username):
            raise UserInputError("Username must be over 2 letters")
        
        if not re.match("(?=.{8,})([a-zA-Z]*[^a-zA-Z]+[a-zA-Z]*)", password):
            raise UserInputError("Password must be over 7 characters long and have one nonalphabetic character")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
