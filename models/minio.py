# -*- coding: utf-8 -*-

class Bucket:
    def __init__(self, name):
        self.name=name
        
    def serialize(self):
        return {
            'name': self.name,
            }
        