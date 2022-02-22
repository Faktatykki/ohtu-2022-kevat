
from matchers import *

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def hasAtLeast(self, goals, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(goals, attr)))

    def hasFewerThan(self, goals, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(goals, attr)))

    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1, query2))

    def build(self):
        return self._matcher
    
