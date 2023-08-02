from selenium import webdriver
from keyword_search_service import KeywordSearchService


class NaverTabService(KeywordSearchService):
    def __init__(self, base_url, target_class):
        self.base_url = base_url
