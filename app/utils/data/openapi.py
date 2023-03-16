import pandas as pd
import requests
from os import name
import xml.etree.ElementTree as et
import pandas as pd
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote


def get_openapi_xml_data(url: str, key: str, **params) -> pd.DataFrame:
    """
    openapi 공공데이터 xml 데이터 받아와서 DataFrame으로 변환.
    :param url: api endpoint url
    :param key: encoding personal api key
    :param params: params
    :return: pd.DataFrame
    """
    decoding_key = unquote(key, encoding="utf-8")
    params["serviceKey"] = decoding_key
    response = requests.get(url, params=params)
    content = response.text

    xml_obj = bs4.BeautifulSoup(content, "lxml-xml")
    rows = xml_obj.findAll("item")
    print(params)

    # 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
    row_list = []  # 행값
    name_list = []  # 열이름값
    value_list = []  # 데이터값

    # xml 안의 데이터 수집
    for i in range(0, len(rows)):
        columns = rows[i].find_all()
        # 첫째 행 데이터 수집
        for j in range(0, len(columns)):
            if i == 0:
                # 컬럼 이름 값 저장
                name_list.append(columns[j].name)
            # 컬럼의 각 데이터 값 저장
            value_list.append(columns[j].text)
        # 각 행의 value값 전체 저장
        row_list.append(value_list)
        # 데이터 리스트 값 초기화
        value_list = []

    # xml값 DataFrame으로 만들기
    df = pd.DataFrame(row_list, columns=name_list)
    return df
